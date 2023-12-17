from Solver import *

system = [
    lambda x, y, z: x ** 2 + np.sin(y) + z,
    lambda x, y, z: y ** 2 + np.cos(z) + x, 
    lambda x, y, z: z ** 2 + y / x + 2
]

print(Solver.Jacobi(system))