import numpy as np
from copy import deepcopy




class Solver:
    def __init__():
        pass

    @staticmethod # Metric
    def __max_error(system: list, args: list) -> float:
        return max([abs(lam(*args)) for lam in system])
    
    @staticmethod # For comfortable lambdas exploitation
    def __wrapper(lambda_function) -> 'function':
        def wrapped_function(args: list):
            return lambda_function(*args)

        return wrapped_function

    @classmethod # The simple iteration method
    def Jacobi(cls, system: list, values=None, eps=1e-7) -> (list, float):
        '''
            The simple iteration method (Jacobi method). 
            Example:
                Input:
                    system = [
                        lambda x, y, z: x ** 2 + np.sin(y) + z,
                        lambda x, y, z: y ** 2 + np.cos(z) + x, 
                        lambda x, y, z: z ** 2 + y / x + 2
                    ]
                    values = [1., 1., 1.] (if None - automatic answer search)
                Output:
                    ([x1, x2, x3], max_error)
        '''
        
        def epoch(values: np.ndarray): # Method implementation
            answer = []
            min_error = np.inf
            error_last = np.inf
            iter = 0
            while error_last > eps and iter < 1000:
                iter += 1
                values = np.array([values[i] - wsystem[i](values) for i in range(n)]) # Calculating new values at i-step
                error_cur = Solver.__max_error(system, values) 
                if (error_cur > error_last) or (error_cur >= np.inf) or (None in values):
                    break
                elif error_cur < min_error:
                    answer, min_error = deepcopy((values, error_cur))
                error_last = error_cur

            if len(answer):
                return answer, min_error

            return values, error_last
        
        n = len(system)
        wsystem = [Solver.__wrapper(lam) for lam in system]        
        if values is not None: # The result for the proposed first approximation will be returned
            if not isinstance(values, np.ndarray): 
                values = np.array(values)
            return epoch(values)

        answer = []
        min_error = np.inf   
        for step_rate in [0.025, 0.05, 0.1]: # Attempts to find the optimal starting point
            start_rate = step_rate
            start = np.zeros((n, )) + eps
            for i in range(5000): 
                if not i % 20:
                    step_rate += (start_rate - (start_rate / 5) * (i // 1000))  
                err = epoch(start)[1]
                for j in range(n):
                    sign = 1
                    iter = 1
                    while True:
                        if not iter % 10:
                            break
                        start[j] += sign * step_rate
                        ans, cur_err = epoch(start)
                        if cur_err < eps:
                            return ans, cur_err
                        elif cur_err < min_error:
                            answer, min_error = deepcopy((ans, cur_err))
                        if cur_err < err:
                            err = cur_err
                        else:
                            if iter == 1 and cur_err > err:
                                sign *= -1
                                start[j] += sign * step_rate
                            elif iter != 1 and cur_err >= err:
                                break
                        iter += 1

        return answer, min_error