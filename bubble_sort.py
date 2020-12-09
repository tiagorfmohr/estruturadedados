def ordem_alfabetica(array):
    ordenado = False
    while not ordenado:
      ordenado = True
      for i in range(len(array)-1):
        if array[i][0]> array[i+1][0]:
          ordenado=False
          array[i], array[i+1] = array[i+1], array[i]

def ordem_mais_trabalhado(array):
    ordenado = False
    while not ordenado:
      ordenado = True
      for i in range(len(array)-1):
        if array[i][2]< array[i+1][2]:
          ordenado = False
          array[i], array[i+1] = array[i+1], array[i]


def ordem_maior_salario(array):
    ordenado = False
    while not ordenado:
      ordenado = True
      for i in range(len(array)-1):
        if array[i][1]*array[i][2] < array[i+1][1]*array[i+1][2]:
          ordenado = False
          array[i], array[i+1] = array[i+1], array[i]