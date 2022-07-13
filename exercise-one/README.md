# Exercise 1 (MPI)
Create an MPI program that generates a set of M random integers (indices) in the range [0,N),
on each process (rank). The random number generator is seeded differently on each rank. For
each index on a rank, the program must be able to compute which other ranks also have that
index. Bear in mind that M and the number of ranks may be large.