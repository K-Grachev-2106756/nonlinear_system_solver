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

for i in range(len(systems)):
    start = time.time()
    result = Solver.Jacobi(systems[i])
    end = time.time()

    print('Jacobi')
    print(f'Answer: {result[0]}')
    print(f'MaxError: {result[1]}')
    print(f'Time: {(end - start) * 10 ** 3} ms')
    print('=' * 100)

    start = time.time()
    result = Solver.GaussSeidel(systems[i])
    end = time.time()

    print('Gauss-Seidel')
    print(f'Answer: {result[0]}')
    print(f'MaxError: {result[1]}')
    print(f'Time: {(end - start) * 10 ** 3} ms')
    print('=' * 100)

'''OUTPUT is THERE:
    Jacobi
    Answer: [0.73094]
    MaxError: 0.009704890968720292
    Time: 88267.02237129211 ms
    ====================================================================================================
    Gauss-Seidel
    Answer: [0.73094]
    MaxError: 0.009704890968720292
    Time: 96886.09671592712 ms
    ====================================================================================================
    Jacobi
    Answer: [-0.43667  0.00058]
    MaxError: 0.2150171466575846
    Time: 27429.88085746765 ms
    ====================================================================================================
    Gauss-Seidel
    Answer: [-0.4372   0.00164]
    MaxError: 0.23235776146263315
    Time: 25781.8124294281 ms
    ====================================================================================================
    Jacobi
    Answer: [ 0.00975 -0.04684  1.68808]
    MaxError: 0.10507099066161898
    Time: 20147.756814956665 ms
    ====================================================================================================
    Gauss-Seidel
    Answer: [ 0.00196 -0.00897  1.61729]
    MaxError: 0.04443646351709192
    Time: 18273.061275482178 ms
    ====================================================================================================
'''