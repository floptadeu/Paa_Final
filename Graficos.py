import matplotlib.pyplot as plt

def plot_algorithm_performance(algorithm_names, execution_times):
    """
    Plots a bar chart showing the performance of different algorithms.

    Parameters:
    - algorithm_names: A list of names of the algorithms.
    - execution_times: A list of execution times corresponding to each algorithm.
    """
    # Creating the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(algorithm_names, execution_times, color='blue')

    # Adding titles and labels
    plt.title('Algorithm Performance Comparison')
    plt.xlabel('Algorithms')
    plt.ylabel('Execution Time (seconds)')

    # Displaying the plot
    plt.show()

# # Example usage
# algorithm_names = ['Algorithm 1', 'Algorithm 2', 'Algorithm 3']
# execution_times = [0.5, 0.8, 0.3]  # Example execution times
# plot_algorithm_performance(algorithm_names, execution_times)



def plot_performance_with_waste(algorithm_names, execution_times, waste_amounts):
    """
    Plots a bar chart for execution times and a line chart for waste amounts of different algorithms.

    Parameters:
    - algorithm_names: A list of names of the algorithms.
    - execution_times: A list of execution times corresponding to each algorithm.
    - waste_amounts: A list of waste amounts corresponding to each algorithm.
    """
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Bar chart for execution times
    ax1.bar(algorithm_names, execution_times, color='blue', label='Execution Time')
    ax1.set_xlabel('Algorithms')
    ax1.set_ylabel('Execution Time (seconds)', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Secondary axis for waste amounts
    ax2 = ax1.twinx()
    ax2.plot(algorithm_names, waste_amounts, color='red', marker='o', label='Waste Amount')
    ax2.set_ylabel('Waste Amount', color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    # Adding title and legend
    plt.title('Algorithm Performance and Waste Comparison')
    # Adding observation text
    ax1.text(0.5, max(execution_times), 'Obs: Algoritmo Dinamico tempo multiplicado por 1000',
             fontsize=8, color='black')

    fig.tight_layout()

    # Displaying the plot
    plt.show()

# # Example usage
# algorithm_names = ['Algorithm 1', 'Algorithm 2', 'Algorithm 3']
# execution_times = [0.5, 0.8, 0.3]  # Example execution times
# waste_amounts = [20, 15, 25]  # Example waste amounts
# plot_performance_with_waste(algorithm_names, execution_times, waste_amounts)

def plot_waste_comparison(algorithm_names, waste_amounts):
    """
    Plots a bar chart showing the waste comparison of different algorithms.

    Parameters:
    - algorithm_names: A list of names of the algorithms.
    - waste_amounts: A list of waste amounts corresponding to each algorithm.
    """
    # Creating the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(algorithm_names, waste_amounts, color='green')

    # Adding titles and labels
    plt.title('Algorithm Waste Comparison')
    plt.xlabel('Algorithms')
    plt.ylabel('Waste Amount')

    # Displaying the plot
    plt.show()

# Example usage
# algorithm_names = ['Algorithm 1', 'Algorithm 2', 'Algorithm 3']
# waste_amounts = [100, 150, 120]  # Example waste amounts
# plot_waste_comparison(algorithm_names, waste_amounts)


def plot_execution_time_growth(database_sizes, execution_times,title):
    """
    Plots a line chart showing the growth of execution time for an algorithm
    with increasing database sizes.

    Parameters:
    - database_sizes: A list of database sizes.
    - execution_times: A list of execution times corresponding to each database size.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(database_sizes, execution_times, marker='o', color='blue', linestyle='-')

    plt.title(title)
    plt.xlabel('Database Size')
    plt.ylabel('Execution Time (seconds)')

    plt.grid(True)
    plt.show()

# Example usage
# database_sizes = [100, 200, 300, 400, 500]  # Example database sizes
# execution_times = [0.1, 0.2, 0.4, 0.8, 1.6]  # Corresponding execution times
# plot_execution_time_growth(database_sizes, execution_times)


