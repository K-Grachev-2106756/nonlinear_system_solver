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
    print()

    start = time.time()
    result = Solver.Seidel(systems[i])
    end = time.time()

    print('Seidel')
    print(f'Answer: {result[0]}')
    print(f'MaxError: {result[1]}')
    print(f'Time: {(end - start) * 10 ** 3} ms')
    print('=' * 100)

'''OUTPUT is THERE:
    Jacobi
    Answer: [0.73094]
    MaxError: 0.009704890968720292
    Time: 47661.5777015686 ms

    Seidel
    Answer: [0.73094]
    MaxError: 0.009704890968720292
    Time: 50439.61000442505 ms
    ====================================================================================================
    Jacobi
    Answer: [-0.43667  0.00058]
    MaxError: 0.2150171466575846
    Time: 15375.513553619385 ms

    Seidel
    Answer: [-0.4372   0.00164]
    MaxError: 0.23235776146263315
    Time: 14543.545722961426 ms
    ====================================================================================================
    Jacobi
    Answer: [ 0.00975 -0.04684  1.68808]
    MaxError: 0.10507099066161898
    Time: 12150.553464889526 ms

    Seidel
    Answer: [ 0.00196 -0.00897  1.61729]
    MaxError: 0.04443646351709192
    Time: 10573.805570602417 ms
    ====================================================================================================
'''