# Poisson equation
This repository contains finite element code for solution of Poisson's equation.
$$\begin{aligned}
-\nabla^{2} u&=f \text { in } \Omega \\
u&=0 \text { on } \partial \Omega \\
f&=4\left(-y^{2}+y\right) \sin (\pi x)
\end{aligned}$$
on the square domain $\Omega:=(0,1) \times(0,1)$ using a structured mesh of four-noded quadrilateral Lagrange elements  $f=4\left(-y^{2}+y\right) \sin (\pi x)$.