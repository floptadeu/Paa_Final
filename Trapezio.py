class Trapezio(object):
    x1 = float()
    x2 = float()
    x3 = float()
    superiorEsquerdo = []
    superiorDireito = []
    inferiorEsquerdo = []
    inferiorDireito = []
    altura = 100

    def __init__(self, x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

        # coordenadas
        self.superiorEsquerdo = [0,100]
        # print(self.superiorEsquerdo)
        self.superiorDireito = [x1,100]
        # print(self.superiorDireito)
        if(x3<= 0 and  x2<=0  ):
            self.inferiorEsquerdo = [x3 + x2,0]
            # print(self.inferiorEsquerdo)
        else:
            
            self.inferiorEsquerdo = [x3,0]
            # print(self.inferiorEsquerdo)



        if(x3> 0 and x2>0  ):
            self.inferiorDireito = [x3+x2,0]
            # print(self.inferiorDireito)

        else:
            self.inferiorDireito = [x2,0]
            # print(self.inferiorDireito)


    def TamanhoDaBase(self):
        if (self.inferiorEsquerdo[0]>=0):
            return self.inferiorDireito[0]
        else:
            return self.inferiorDireito[0] - self.inferiorEsquerdo[0]
    
    def AreaTrapezio(self):
        return ((self.x1+self.TamanhoDaBase())*self.altura/2)

    def ExtremaDireita(self):
        return max(self.inferiorDireito[0],self.superiorDireito[0])

    def ExtremaEsquerda(self):
        return min(self.inferiorEsquerdo[0],self.superiorEsquerdo[0])

    def PontaEmCimaNaDireta(self):
        return self.superiorDireito[0]>=self.inferiorDireito[0]
    
    def PontaEmCimaNaEsquerda(self):
        #Como e para valores negativos o lado esquerdo inferior sera ponta se for menor que 0
        return self.superiorEsquerdo[0]<=self.inferiorEsquerdo[0]
    # def distanciaNoEixoX(self):
    # def DistanciaNaDireita(self):
        
    # def DistanciaNaEsquerda(self):
    #     return
  
    def OndeToca(self,pecaB):
 
        if(self.PontaEmCimaNaEsquerda() and pecaB.PontaEmCimaNaDireta()):
            #Cima
            
           
            return True
        elif(self.PontaEmCimaNaEsquerda()):
            # nesse caso a distancia do lado inferior direito ja e o tamanho da ponta de cima a esquerda
            if(self.inferiorEsquerdo[0] >= abs(pecaB.inferiorDireito[0]-pecaB.superiorDireito[0])):
                return True
            else:
                #Baixo
                return False
        elif(pecaB.PontaEmCimaNaDireta()):
            if(abs(pecaB.superiorDireito[0]-pecaB.inferiorDireito[0])>=abs(self.inferiorEsquerdo[0])):
                return True
            else:
                return False
        else:
            return False
    def Encaixar(pecaA,pecaB):
        baseRetangulo = float()
        distanciaDeVertices = float()
        if(pecaA.OndeToca(pecaB)):
            #Tocam em Cima

            baseRetangulo = pecaB.superiorDireito[0]+abs(pecaB.ExtremaEsquerda())+pecaA.ExtremaDireita()+abs(pecaA.ExtremaEsquerda())
            # print("Base do Retangulo = "+ str(baseRetangulo))
            distanciaDeVertices = pecaB.superiorDireito[0]
            # print("Distancia dos vertices de 1 e 2 ="+ str(distanciaDeVertices))

            retanguloParteTrapezioA = pecaA.ExtremaDireita()+abs(pecaA.ExtremaEsquerda())
            # print("retangulo Parte do Trapezio A = "+ str(retanguloParteTrapezioA))
            retanguloParteTrapezioB = pecaB.superiorDireito[0]+abs(pecaB.ExtremaEsquerda())
            # print("retangulo Parte do Trapezio B = "+ str(retanguloParteTrapezioB))
        else:
            #Tocam em baixo

            baseRetangulo = pecaB.inferiorDireito[0]+abs(pecaB.ExtremaEsquerda())+pecaA.ExtremaDireita()+abs(pecaA.ExtremaEsquerda())
            # print("Base do Retangulo = "+ str(baseRetangulo))
            distanciaDeVertices = pecaB.inferiorDireito[0] +( pecaA.superiorEsquerdo[0]-pecaA.inferiorEsquerdo[0])
            # print("Dinstancia dos vertices de 1 e 2 = "+ str(distanciaDeVertices))
            retanguloParteTrapezioA = pecaA.ExtremaDireita()+abs(pecaA.ExtremaEsquerda())
            # print("retangulo Parte do Trapezio A = "+ str(retanguloParteTrapezioA))
            retanguloParteTrapezioB = pecaB.inferiorDireito[0]+abs(pecaB.ExtremaEsquerda())
            # print("retangulo Parte do Trapezio B = "+ str(retanguloParteTrapezioB))
        

        
        areaRetangulo = baseRetangulo*100
        # print("Area Retangulo = "+ str(areaRetangulo))

        areaTrapezioA = pecaA.AreaTrapezio()
        # print("Area Trapezio 1 = "+ str(areaTrapezioA))
        areaTrapezioB = pecaB.AreaTrapezio()
        # print("Area Trapezio 2 = "+ str(areaTrapezioB))

        areaDosTrapezios = areaTrapezioA + areaTrapezioB
        # print("Area dos dois trapezios "+ str(areaDosTrapezios))
        desperdicio = areaRetangulo - areaDosTrapezios 
        # print("Desperdicio = "+ str(desperdicio))

        # print("Porcentagem do desperdicio = "+ str(desperdicio/areaRetangulo*100)+"%")

        return distanciaDeVertices,desperdicio,baseRetangulo,retanguloParteTrapezioA,retanguloParteTrapezioB


