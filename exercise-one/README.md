# Exercise 1 (MPI)
Create an MPI program that generates a set of M random integers (indices) in the range [0,N),
on each process (rank). The random number generator is seeded differently on each rank. For
each index on a rank, the program must be able to compute which other ranks also have that
index. Bear in mind that M and the number of ranks may be large.

### Running
The file `try.py` contains a working prototype. To run use the following command in terminal
```
mpirun -np 3 python3 try.py
```

### Algorithm design
- The seeding for each processor to generate the sequence of a random integer is done with the rank of that processor.
- Once each processor has generated the set of random numbers (NumPy vector $I_r$), then we have a dense vector of $(M\times1)$ dimension with each of the $r$ processors.
- Every processor needs the knowledge of the index vector of every other processor to figure out which other processors have the same index. To do this, we send the whole NumPy vector with `comm.Send` to every other processor in the world.
- The current processor receives $I_r$ from the $r^{th}$ process. Now we have to make a matrix that will store boolean value at the $m^{th}$ row and the $r^{th}$ column of the `check` matrix. This will be a sparse matrix whose row number corresponds to the value we need to check, and column number corresponds to the rank of the other processor. Suppose we have set size $M=3$ and world size $P=4$. The check matrix with processor $2$ will look like.

$$
  \underbrace{\left[ \begin{array}{c}
      4   \\
      1   \\
      5
    \end{array}\right]}_{\text{Index Matrix}} ,
  \underbrace{\left[ \begin{array}{c|c|c|c}
      1 & 0 & 1 & 1 \\
      0 & 0 & 1 & 1 \\
      0 & 0 & 1 & 1
    \end{array}\right]}_{\text{Check Matrix}}
$$

By looking at the check matrix we can say that value (4) that is on rank 2 is also available with rank 0 and 3. Similarly value (1) is available on rank 3.

![](./github/pic_1.png)