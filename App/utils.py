''' Todos los archivos con terminación .py son/se comportan como módulos. Podemos importar/mandar llamar funciones, variables, etc de otros módulos (programas)'''

import csv
import matplotlib.pyplot as plot


def get_population():
  keys = ['mex', 'col', 'bra']
  values = [200, 300, 400]
  return keys, values


texto = 'Hola'


def readCSVorig(path):
  with open(path, 'r') as filecsv:
    lector = csv.reader(filecsv, delimiter=',')
    encab = next(lector)  #para brincar el encabezado
    datapaises = []
    for line in lector:
      pais = {llave: valor for (llave, valor) in zip(encab, line)}
      datapaises.append(pais)  #lista con dicc
  return datapaises #retorna lista con diccionarios


def readCSV(path, index):  #function, name(variable)
  with open(path, 'r') as filecsv:
    lector = csv.reader(filecsv, delimiter=',')
    next(lector)
    dict = []
    for i in lector:
      dict.append(i[index])
  return dict #retorna lista con solo la información de la columa indexada (index dado desde donde se llama la función)


def popul_by_country(dicc, pais):
  #datos esperados de entrada dicc (países y población y país del que se quiere obtener la información)
  result = list(filter(lambda llave: llave['Country'] == pais, dicc))
  return result


def filtropob(dicc):
  d70 = dicc.get('1970 Population')
  d80 = dicc.get('1980 Population')
  d90 = dicc.get('1990 Population')
  d00 = dicc.get('2000 Population')
  d10 = dicc.get('2010 Population')
  d15 = dicc.get('2015 Population')
  d20 = dicc.get('2020 Population')
  d22 = dicc.get('2022 Population')
  return d70, d80, d90, d00, d10, d15, d20, d22


def gen_graf_pie(etiq, val, name):
  fig, ax = plot.subplots()
  ax.pie(val, labels=etiq)
  ax.axis('equal')
  plot.savefig (f'./imgs/{name}_pie.png') #Evitando errores
  '''este formato para guardar la imagen con el nombre que le mandemos
  al llamar la función'''
  plot.close()


def gen_graf_barras(etiq, val, name):
  fig, ax = plot.subplots()
  ax.bar(etiq, val)
  plot.savefig (f'./imgs/{name}_bar.png') #Evitando errores
  plot.close()


def getcountries(dicc):
  encab = next(dicc)
  for line in dicc:
    keys = {'Country/Territory': valor for (valor) in zip(encab, line)}
  return result
