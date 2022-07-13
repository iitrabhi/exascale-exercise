from utilities import *
import numpy as np

mesh = RectangleMesh([0, 0], [1, 1], 20, 20)
mesh.plot()
K, F = assemble(mesh, load_expression=lambda x,
                y: 4 * (-y**2+y) * np.sin(np.pi * x))
K, F = apply_boundary(mesh, K, F)
u_sol = np.linalg.solve(K, F)
plot_attribute(mesh, u_sol)