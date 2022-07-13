# Poisson equation
This repository contains finite element code for solution of Poisson's equation.

$$
\begin{align}
-\nabla^{2} u&=f \text { in } \Omega \\
u&=0 \text { on } \partial \Omega \\
f&=4\left(-y^{2}+y\right) \sin (\pi x)
\end{align}
$$

on the square domain $\Omega:=(0,1) \times(0,1)$ using a structured mesh of four-noded quadrilateral Lagrange elements.

## Getting Started
This code is based on general purpose numerical libraries `numpy` and `matplotlib` and is based on python3.
### Dependencies
To install the libraries on your system first install python3 and then run the following commands in terminal.
```
pip install numpy
pip install matplotlib
```
### Running
Run the following in the directory which contains the `main.py` file.
```
python main.py
```
The file `utilities.py` contains all the functions and the `Mesh` class used in the `main.py` file. You can change the dimensions of the domain, the number of elements in each direction and the forcing function inside `main.py`. The boundary conditions are hard coded to be fixed on the complete boundary of the domain.

`RectangleMesh(point_1(list),point_2(list),nx(int),ny(int))`:
Quadilateral mesh of the 2D rectangle $(x_1, y_1) \times (x_2, y_2)$. Given the number of cells $(nx, ny)$ in each direction, the total number of quadilaterals will be $nx \times ny$ and the total number of vertices will be $(nx + 1)\times(ny + 1)$.
## Solution
![](./github/pic_1.png)
