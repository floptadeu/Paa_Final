import time

def measure_execution_time(algorithm_function, *args, **kwargs):
    """
    Measures the execution time of a given algorithm function.

    Parameters:
    - algorithm_function: The function representing the algorithm whose execution time is to be measured.
    - *args: Argument list for the algorithm function.
    - **kwargs: Keyword arguments for the algorithm function.

    Returns:
    - float: Execution time in seconds.
    """
    start_time = time.perf_counter()  # Start timing
    algorithm_function(*args, **kwargs)  # Execute the algorithm
    end_time = time.perf_counter()  # End timing

    # Calculate execution time
    execution_time = end_time - start_time
    return execution_time

def run_algorithms(algorithms, *args, **kwargs):
    """
    Runs a list of algorithms and measures their execution times.

    Parameters:
    - algorithms: A list of tuples, each containing the name of the algorithm and the algorithm function.
    - *args, **kwargs: Arguments and keyword arguments to be passed to each algorithm function.

    Returns:
    - List of tuples with each algorithm's name and its execution time.
    """
    results = []
    for name, algorithm in algorithms:
        start_time = time.perf_counter()
        algorithm(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        results.append((name, execution_time))
    return results

# Example usage:
# Assuming you have defined algorithms as functions:
# def algorithm1(*args, **kwargs): ...
# def algorithm2(*args, **kwargs): ...
# algorithms_to_run = [('Algorithm 1', algorithm1), ('Algorithm 2', algorithm2)]
# execution_results = run_algorithms(algorithms_to_run, arg1, arg2, ...)
# print(execution_results)

