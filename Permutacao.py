from Trapezio import Trapezio
from Leitor import Leitor,Pecas,exeEncaixar,exeDesperdicio,exeDesperdicioMultiplasPecas
from Interface import Interface
import time



def Permutacao(pecas):
 
 
    permPecas = list()

    if len(pecas) == 0:
        return []
    if len(pecas) == 1:
        return [pecas]
 
    # Calcular o numero de permutacoes 
    for x in range(len(pecas)):
        m = pecas[x]
        #removendo a peca atual da lista
        listaRestante = pecas[:x] + pecas[x+1:]
 
            #Gera todas as permutacoes em que o elemento m 
            #está na primeira posição
        for p in Permutacao(listaRestante):
            permPecas.append([m] + p)
    return permPecas


def exePermutacao(permPecas):
    
    tempoInicial = time.time()
   
    desperdicioPerm = list()
    
    salvaPerm = 0
    menorDesperdicio = 0

    y = 0
    for x in permPecas:
        desperdicioPerm.append((exeDesperdicioMultiplasPecas(x)))
        if(desperdicioPerm[y]== min(desperdicioPerm)):
            # print("Menor desperdicio ate agora ")
            menorDesperdicio = desperdicioPerm[y]
            # print( menorDesperdicio)
            # print("Permutacao: ")
            salvaPerm = x
        # print(y)
        y = y + 1

    print("Menor desperdicio: ")
    print(menorDesperdicio[0])
    tempoFinal = time.time()
    tempoDeExecucao = tempoFinal - tempoInicial
    print("Tempo de execucao: " + str(tempoDeExecucao) + " segundos")
    return salvaPerm,menorDesperdicio,tempoDeExecucao

# pecas = Pecas(Leitor())
# permPecas = Permutacao(pecas)
# print(exePermutacao(permPecas)[0])
# print(exePermutacao(permPecas)[2])
# Interface(exePermutacao(permPecas)[0])