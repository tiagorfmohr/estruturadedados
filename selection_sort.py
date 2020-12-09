def ordem_alfabetica(array):
  for x in range(len(array)):
    menor = x
    for i in range(x + 1, len(array)):
      if array[i][0] < array[menor][0]:
        menor = i
    array[x], array[menor] = array[menor], array[x]

def ordem_mais_trabalhado(array):
  for x in range(len(array)):
    maior = x
    for i in range(x + 1, len(array)):
      if array[i][2] > array[maior][2]:
        maior = i
    array[x], array[maior] = array[maior], array[x]

def ordem_maior_salario(array):
  for x in range(len(array)):
    maior = x
    for i in range(x + 1, len(array)):
      if array[i][1]*array[i][2] > array[maior][1]*array[maior][2]:
        maior = i
    array[x], array[maior] = array[maior], array[x]

