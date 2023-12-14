from Trapezio import Trapezio


def Leitor(num_lines=None):
  trapezios = []

  with open("trapezios.txt", "r") as f:
    ntrapezios = int(f.readline().strip())  # Read the number of trapezoids in the file

    for _ in range(min(ntrapezios, num_lines if num_lines is not None else ntrapezios)):
      linha = f.readline().strip()
      if linha:  # Check if the line is not empty
        trapezios.append(linha.split())

  return trapezios


def Pecas(trapezios):
  pecas = list()
  for x in range (len(trapezios)):
    # print(x)
    pecas.append(Trapezio(float(trapezios[x][0]),float(trapezios[x][1]),float(trapezios[x][2])))
    # print(pecas[x])

  return pecas


def exeEncaixar(pecas):
  distancias = list()
  for x in range (len(pecas)-1):
    # print(x)
    distancias.append(pecas[x].Encaixar(pecas[x+1])[0])
  return distancias

def exeDesperdicio(pecas):
  desperdicio = list()
  for x in range (len(pecas)-1):
    # print(x)
    desperdicio.append(pecas[x].Encaixar(pecas[x+1])[1])
  return desperdicio
# exeDesperdicio(Pecas(Leitor()))


def exeDesperdicioMultiplasPecas(pecas):
  partesDosTrapezios = list()
  areaDosTrapezios = list()
  for x in range (len(pecas)):
    areaDosTrapezios.append(pecas[x].AreaTrapezio())
    # print("Area do trapezio "+str(x+1)+" = "+str(pecas[x].AreaTrapezio()))
  for x in range (len(pecas)-1):
    if(x==0):
      partesDosTrapezios.append(pecas[x].Encaixar(pecas[x+1])[3])
      partesDosTrapezios.append(pecas[x].Encaixar(pecas[x+1])[4])
    else:
      partesDosTrapezios.append(pecas[x].Encaixar(pecas[x+1])[4])
  ladoDoRetangulo=sum(partesDosTrapezios)
  areaDoRetangulo = ladoDoRetangulo*100

  # print("Lista de partes dos trapezios: " + str(partesDosTrapezios))
  # print("Area do retangulo = "+ str(areaDoRetangulo))
  # print("Area dos trapezios = "+ str(sum(areaDosTrapezios)))
  desperdicio = areaDoRetangulo - sum(areaDosTrapezios)
  # print("Desperdicio = "+ str(desperdicio))
  return desperdicio,areaDoRetangulo,sum(areaDosTrapezios)

# print(exeDesperdicioMultiplasPecas(Pecas(Leitor())))

def generate_trapezoids_sets(filename = "grande.txt", step=4, max_size=16):
    """
    Generates an array of trapezoid lists, with each list increasing in size by the specified step.

    Parameters:
    - filename: The name of the file containing trapezoid data.
    - step: The step size for increasing the number of trapezoids in each subsequent list.
    - max_size: The maximum size of the trapezoid list. If None, includes all trapezoids in the file.

    Returns:
    - A list of lists, where each inner list contains trapezoids.
    """
    trapezoids_sets = []

    with open(filename, "r") as f:
      ntrapezios = int(f.readline().strip())  # Read the total number of trapezoids
      trapezios = [f.readline().strip().split() for _ in range(ntrapezios)]

    max_size = max_size or ntrapezios
    for size in range(step, max_size + 1, step):
      trapezoids_sets.append(trapezios[:size])

    return trapezoids_sets


# Example usage
# Assuming 'trapezios.txt' contains the trapezoid data
# trapezoids_sets = generate_trapezoids_sets()
# for trapezoid_set in trapezoids_sets:
#   print(trapezoid_set)  # Each list will have 5, 10, 15, 20 trapezoids
def transform_trapezoids_sets(trapezoids_sets):
    trapezio_objects_sets = []
    for trapezoid_set in trapezoids_sets:
      trapezio_objects_sets.append(Pecas(trapezoid_set))

    return trapezio_objects_sets

# transform = transform_trapezoids_sets(trapezoids_sets)
# for transforms in transform:
#   print(transforms)  # Each list will have 5, 10, 15, 20 trapezoids




