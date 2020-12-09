import csv_file
import selection_sort
import bubble_sort
import time

def testando_selection_sort():
  tempos = []
  ##ordem alfabetica
  array = csv_file.ler_arquivo()
  tempo = time.time()
  selection_sort.ordem_alfabetica(array)
  tempo = time.time() - tempo
  tempos.append(tempo)
  csv_file.escrever_arquivo (array, 'ordemAlfabeticSelectionSort.csv')

  ## mais trabalhous
  array = csv_file.ler_arquivo()
  tempo = time.time()
  selection_sort.ordem_mais_trabalhado(array)
  tempo = time.time() - tempo
  tempos.append(tempo)
  csv_file.escrever_arquivo (array, 'ordemMaisTrabalhouSelectionSort.csv')

  ## mais receberams
  array = csv_file.ler_arquivo()
  tempo = time.time()
  selection_sort.ordem_maior_salario(array)
  tempo = time.time() - tempo
  tempos.append(tempo)
  csv_file.escrever_arquivo (array,'ordemMaiorSalarioSelectionSort.csv')

  return tempos


def testando_bubble_sort():
  tempos = []
  ##ordem alfabetica
  array = csv_file.ler_arquivo()
  tempo = time.time()
  bubble_sort.ordem_alfabetica(array)
  tempo = time.time() - tempo
  tempos.append(tempo)
  csv_file.escrever_arquivo (array, 'ordemAlfabeticBubbleSort.csv')

  ## mais trabalhou
  array = csv_file.ler_arquivo()
  tempo = time.time()
  bubble_sort.ordem_mais_trabalhado(array)
  tempo = time.time() - tempo
  tempos.append(tempo)
  csv_file.escrever_arquivo (array, 'ordemMaisTrabalhouBubbleSort.csv')

  ## mais receberams
  array = csv_file.ler_arquivo()
  tempo = time.time()
  bubble_sort.ordem_maior_salario(array)
  tempo = time.time() - tempo
  tempos.append(tempo)
  csv_file.escrever_arquivo (array,'ordemMaiorSalarioBubbleSort.csv')

  return tempos

  
t=[]
t.append(testando_selection_sort())
t.append(testando_bubble_sort())
print("Selection sort: ",t[0])
print("Bubble sort:    ",t[1])
csv_file.salvar_tempos(t, 'tempos.csv')