from Trapezio import Trapezio
from Leitor import Leitor,Pecas,exeEncaixar,exeDesperdicio,exeDesperdicioMultiplasPecas
from Interface import Interface

pecas= Pecas(Leitor())


def greedy_algorithm(pecas):
    # Sort trapezoids based on their area or another heuristic
    sorted_pecas = sorted(pecas, key=lambda peca: peca.AreaTrapezio(), reverse=True)
    layout = [sorted_pecas[0]]  # Start with the largest piece

    for i in range(1, len(sorted_pecas)):
        min_waste = float('inf')
        best_position = -1

        # Find the position that results in the least waste
        for j in range(len(layout)):
            _, waste, _, _, _ = Trapezio.Encaixar(layout[j], sorted_pecas[i])
            if waste < min_waste:
                min_waste = waste
                best_position = j

        layout.insert(best_position + 1, sorted_pecas[i])

    return layout



def dynamic_programming(pecas):
    n = len(pecas)
    dp = [float('inf')] * (1 << n)  # Initialize DP table with infinite waste
    dp[0] = 0  # Base case: no trapezoids, no waste
    layout = [[] for _ in range(1 << n)]  # Store the layout for each scenario

    for mask in range(1 << n):
        for i in range(n):
            if mask & (1 << i):  # Check if the ith trapezoid is in the current set (mask)
                prev_mask = mask ^ (1 << i)
                new_layout = layout[prev_mask] + [pecas[i]]
                waste = exeDesperdicioMultiplasPecas(new_layout)[0]
                if dp[mask] > waste:
                    dp[mask] = waste
                    layout[mask] = new_layout

    return layout[-1], dp[-1]

def trapezoid_heuristic(trapezoid):
    # Calculate the difference between inferiorDireito and superiorDireito
    diff_inferior_superior = abs(trapezoid.inferiorDireito[0] - trapezoid.superiorDireito[0])

    # Consider the absolute value of x3
    abs_x3 = abs(trapezoid.x3)

    # Combine these two factors into a single score
    # Note: You might need to adjust the weights based on empirical results
    score = diff_inferior_superior + abs_x3

    return score

def greedy_algorithm_with_heuristic(pecas):
    # Sort trapezoids based on the heuristic score
    sorted_pecas = sorted(pecas, key=trapezoid_heuristic)
    layout = []

    for peca in sorted_pecas:
        # Place the trapezoid in the layout
        # The placement logic depends on the specifics of your problem
        layout.append(peca)

    return layout





Interface(greedy_algorithm_with_heuristic(pecas))
optimal_layout, min_waste = dynamic_programming(pecas)
print(optimal_layout)
print(min_waste)
Interface(optimal_layout)
Interface(greedy_algorithm(pecas))





