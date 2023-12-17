import numpy as np
import warnings
warnings.simplefilter('ignore')




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
    def Jacobi(cls, system: list, values=None, eps=1e-4) -> (list, float):
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
                new_values = np.array([round(values[i] - wsystem[i](values) * 0.01, 5) for i in range(n)]) # Calculating new values at i-step
                if any(np.isnan(new_values)) or any(np.isinf(new_values)) or np.any(new_values[abs(new_values) > 1e10]): # Avoiding problems
                    break
                error_cur = Solver.__max_error(system, new_values) 
                if error_cur == np.inf:
                    break
                if error_cur < min_error:
                    answer, min_error = new_values, error_cur
                if max(np.absolute(new_values - values)) < eps:
                    break
                error_last = error_cur
                values = new_values

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
        for step_rate in [0.025, 0.1]: # Attempts to find the optimal starting point
            start_rate = step_rate
            start = np.ones((n, )) + eps
            for i in range(1000): 
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
                            answer, min_error = ans, cur_err
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