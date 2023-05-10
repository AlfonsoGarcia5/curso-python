'''Mi proyecto para plotear población anual por país seleccionado'''

import matplotlib.pyplot as plot
import csv
import utils


def gen_graf_pie(etiq, val, 'Name_test'):
  fig, ax = plot.subplots()
  ax.pie(val, labels=etiq)
  ax.axis('equal')
  plot.show()


def gen_graf_barras(etiq, val, "Name_test"):
  fig, ax = plot.subplots()
  ax.bar(etiq, val)
  plot.show()


def readCSV(path, paisfil):
  with open(path, 'r') as filecsv:
    lector = csv.reader(filecsv, delimiter=',')
    encab = next(lector)  #saves header in encab
    for line in lector:
      pais = {llave: valor for (llave, valor) in zip(encab, line)}
      if pais['Country/Territory'] == paisfil:
        break
      else:
        continue
  return pais

def run():
  

if __name__ == '__main__':
  '''Primero filtro país, y obtengo de retorno el diccionario con ese país'''
  dicc = readCSV('./App/dataWP.csv', 'Brazil')
  '''Segundo: obtengo valores de población por las décadas que incluye ya'''
  d70, d80, d90, d00, d10, d15, d20, d22 = utils.filtropob(dicc)
  # print(d70, d80, d90, d00, d10, d15, d20, d22)

  etiquetas = ['70s', '80s', '90s', '00s', '10', '15', '20', '22']
  valores = [d70, d80, d90, d00, d10, d15, d20, d22]
  gen_graf_barras(etiquetas, valores)
  # gen_graf_pie(etiquetas, valores)
