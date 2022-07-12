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

# print(size)

N = 10 # Range [0,N)
M = 3 # Size of set with each processor

np.random.seed(rank)
data = np.random.choice(N, M, replace=False)
print("This is processor ", rank, " and output", data)
# Send data to other destinations
for i in range(rank+1,size):
    comm.Send([data, MPI.INT], dest=i)
# Receive data from other destinations
for i in range(0,rank):
    comm.Recv([data, MPI.INT], source=i)
    print("This is processor ", rank, " and received", data, " from processor ", i)