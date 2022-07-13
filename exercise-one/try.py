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
# received_data = np.random.choice(N, M, replace=False)
# received_data =  np.zeros(M)
print("This is processor ", rank, " and output", data)
# Send data to other processors
for i in range(0, size):
    if not i == rank:
        comm.Send(data, dest=i, tag=4)

# Receive data from other processors
for i in range(0, size):
    if not i == rank:
        received_data = np.empty(M, dtype=data.dtype)
        comm.Recv(received_data, source=i, tag=4)
        common_elements = np.intersect1d(data, received_data)
        for ele in common_elements:
            check[data == ele, i] = 1

print("This is processor ", rank, " and check matrix \n", check)
