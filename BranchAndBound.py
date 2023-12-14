
from Leitor import Leitor,Pecas,exeEncaixar,exeDesperdicio,exeDesperdicioMultiplasPecas
from Interface import Interface
import time



global melhor
global arranjo

melhor = float('inf')


def BranchAndBound(listaRestante, candidato=[]):
    global melhor
    global arranjo

    if len(listaRestante) == 0:
        if exeDesperdicioMultiplasPecas(candidato)[0] < melhor:
            melhor = exeDesperdicioMultiplasPecas(candidato)[0]
            arranjo = candidato
        # print(candidato)
 
    for i in range(len(listaRestante)):
 
        novoCandidato = candidato + [listaRestante[i]]
        novaListaRestante = listaRestante[0:i] + listaRestante[i+1:]

        if exeDesperdicioMultiplasPecas(novoCandidato)[0] <= melhor:
            BranchAndBound(novaListaRestante, novoCandidato)
    return arranjo


pecas= Pecas(Leitor())
Interface(BranchAndBound(pecas))
#
# print(melhor)
# print(arranjo)
#print(permutacao(arr))


def teste1(listaRestante, candidato=[]):

    if len(listaRestante) == 0:
        
        print(candidato)
 
    for i in range(len(listaRestante)):
 
        novoCandidato = candidato + [listaRestante[i]]
        novaListaRestante = listaRestante[0:i] + listaRestante[i+1:]

        teste1(novaListaRestante, novoCandidato)

# teste1(list('1234567'))

