import csv

def ler_arquivo():
  array=[]
  with open('MOCK_DATA.csv', mode='r') as reader:
    for x in reader:
      array.append(x.split(','))
  array.pop(0)
  for x in range(len(array)):
    array[x][2]= int(array[x][2])
    array[x][1]= float(array[x][1])  
  return array

def escrever_arquivo(array, fileName):
  with open('./arquivos_ordenados/{}'.format(fileName), mode='w') as writer:
    writer = csv.writer(writer)
    writer.writerow(['nome','valor_hora','horas_trabalhadas'])
    for x in array:
      writer.writerow(x)

def salvar_tempos(array, fileName):
  with open('./arquivos_ordenados/{}'.format(fileName), mode='w') as writer:
    writer = csv.writer(writer)
    writer.writerow(["Selection Sort: {}".format(array[0])])
    writer.writerow(["Bubble Sort: {}".format(array[1])])
