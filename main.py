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
    lambda x, y, z: x ** 2 + np.sin(y),
    lambda x, y, z: y ** 2 + np.cos(z) + x, 
    lambda x, y, z: z ** 2 + y / x + 2
])

for i in range(len(systems))[2:]:
    start = time.time()
    result = Solver.Jacobi(systems[i])
    end = time.time()

    print(f'Answer: {result[0]}')
    print(f'MaxError: {result[1]}')
    print(f'Time: {(end - start) * 10 ** 3} ms')
    print('=' * 100)

'''OUTPUT is THERE:
    Answer: [0.73094]
    MaxError: 0.009704890968720292
    Time: 48953.95803451538 ms
    ====================================================================================================
    Answer: [-0.43667  0.00058]
    MaxError: 0.2150171466575846
    Time: 15633.9693069458 ms
    ====================================================================================================
    Answer: [ 0.00975 -0.04684  1.68808]
    MaxError: 0.10507099066161898
    Time: 12255.637407302856 ms
    ====================================================================================================
'''