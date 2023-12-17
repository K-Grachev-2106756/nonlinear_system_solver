from Solver import *
import time




systems = []

systems.append([
    lambda x: np.log2(x) + 2 * x - 1
])

systems.append([
    lambda x, y: x ** 2 + np.sqrt(y) - x * y,
    lambda x, y: y ** 2 + np.exp(x) + x
])

systems.append([
    lambda x, y, z: x ** 2 + np.sin(y) + z,
    lambda x, y, z: y ** 2 + np.cos(z) + x, 
    lambda x, y, z: z ** 2 + y / x + 2
])

for i in range(len(systems)):
    start = time.time()
    result = Solver.Jacobi(systems[i])
    end = time.time()

    print(f'Answer: {result[0]}')
    print(f'MaxError: {result[1]}')
    print(f'Time: {(end - start) * 10 ** 3} ms')
    print('=' * 100)