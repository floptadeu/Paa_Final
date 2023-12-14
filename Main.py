from Teste import *
from Graficos import *
from Leitor import *
from Otimizacoes import *
from BranchAndBound import *
from Interface import *
from Trapezio import *
from Permutacao import *

# Definindo pecas
pecas = Pecas(Leitor())
trapezoids_sets = generate_trapezoids_sets()
trapezoids_data_sets = transform_trapezoids_sets(trapezoids_sets)


# Fazendo testes
def exec_time(trapezoids_data_sets, algoritmo):
    times = list()
    for trapezio_set in trapezoids_data_sets:
        time = measure_execution_time(algoritmo,trapezio_set)
        times.append(time)
    return times

desperdicio = exeDesperdicioMultiplasPecas(pecas)
print(desperdicio[0])
greedy_layout = greedy_algorithm(pecas)
desperdicio_greedy = exeDesperdicioMultiplasPecas(greedy_layout)
#print(desperdicio_greedy[0])
greedy_time = measure_execution_time(greedy_algorithm,pecas)

# greedy_times = exec_time(trapezoids_data_sets,greedy_algorithm)
#print(greedy_time)
# print(greedy_times)
# plot_performance_with_waste(["Algoritmo Guloso(Maior Área)"],[greedy_time],[desperdicio_greedy[0]])
#plot_execution_time_growth([100,200,300,400,500,600,700,800,900,1000],greedy_times,"Algoritmo Guloso(Maior Área)")

greedy_time2 = measure_execution_time(greedy_algorithm_with_heuristic,pecas)
greedy_layout2 = greedy_algorithm_with_heuristic(pecas)
desperdicio_greedy2 = exeDesperdicioMultiplasPecas(greedy_layout)
#print(desperdicio_greedy2[0])
# greedy_times2 = exec_time(trapezoids_data_sets,greedy_algorithm_with_heuristic)
#print(greedy_time2)
# print(greedy_times2)

#plot_execution_time_growth([100,200,300,400,500,600,700,800,900,1000],greedy_times2,"Algoritmo Guloso(Guiado por Score)")

# plot_waste_comparison( ['Sem Otimização','Algoritmo Guloso(Maior Área)','Algoritmo Guloso(Guiado por Score)'],[desperdicio[0],desperdicio_greedy[0],desperdicio_greedy2[0]])
# plot_performance_with_waste(['Algoritmo Guloso(Maior Área)','Algoritmo Guloso(Guiado por Score)'],[greedy_time,greedy_time2*1000],[desperdicio_greedy[0],desperdicio_greedy2[0]])


dynamic_time = measure_execution_time(dynamic_programming,pecas)
dynamic_layout = dynamic_programming(pecas)
print(dynamic_layout)
desperdicio_dinamic =exeDesperdicioMultiplasPecas(dynamic_layout[0])
print(desperdicio_dinamic)

# dynamic_times = exec_time(trapezoids_data_sets,dynamic_programming)
print(dynamic_time)
#print(dynamic_times)
#plot_execution_time_growth([4,8,12,16],dynamic_times,"Algoritmo Dinâmico")

bb_time = measure_execution_time(BranchAndBound,pecas)
print(bb_time)
bb_layout = BranchAndBound(pecas)
desperdicio_bb =exeDesperdicioMultiplasPecas(bb_layout)
print(desperdicio_bb)

# bb_times = exec_time(trapezoids_data_sets,BranchAndBound)
# plot_execution_time_growth([4,8,12,16],bb_times,"Algoritmo Branch And Bound")

# plot_waste_comparison( ['Sem Otimização','Algoritmo Dinâmico','Algoritmo Branch And Bound'],[desperdicio[0],desperdicio_dinamic[0],desperdicio_bb[0]])
plot_performance_with_waste(['Algoritmo Dinâmico','Algoritmo Branch And Bound'],[dynamic_time*1000,bb_time],[desperdicio_dinamic[0],desperdicio_bb[0]])

# plot_waste_comparison( ['Sem Otimização','Algoritmo Dinâmico'],[desperdicio[0],desperdicio_dinamic[0]])
# plot_performance_with_waste(['Algoritmo Dinâmico'],[dynamic_time],[desperdicio_dinamic[0]])

