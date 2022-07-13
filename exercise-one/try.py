# Create an MPI program that generates a set of M random integers
# (indices) in the range [0,N), on each process (rank). The random
# number generator is seeded differently on each rank. For each
# index on a rank, the program must be able to compute which other
# ranks also have that index. Bear in mind that M and the number of
# ranks may be large.
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

N = 10  # Range [0,N)
M = 3  # Size of set with each processor

check = np.zeros((M, size))
check[:, rank] = 1

np.random.seed(rank)
data = np.random.choice(N, M, replace=False)
received_data = np.random.choice(N, M, replace=False)

print("This is processor ", rank, " and output", data)
# Send data to other processors
for i in range(0, size):
    if not i==rank:
        comm.Send(data, dest=i, tag=4)

# Receive data from other processors
for i in range(0, size):
    if not i==rank:
        comm.Recv(received_data, source=i, tag=4)
        # print("This is processor ", rank, " and received",received_data, " from processor ", i)
        common_elements = np.intersect1d(data, received_data)
        # print("This is processor ", rank, " common with rank ",i,"is ", common_elements)
        # print("This is processor ", rank, " \n", data == common_elements)
        for ele in common_elements: 
            check[data == ele, i] = 1
    
print("This is processor ", rank, " and check matrix \n", check)
