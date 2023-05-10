import csv


def readCSV(path):
  with open(path, 'r') as filecsv:
    lector = csv.reader(filecsv, delimiter=',')
    encab = next(lector)
    # print(encab), encabezado de columnas
    # ya puedo iterar la sig linea ya son los datos
    datapaises = []
    for line in lector:
      pais = {llave: valor for (llave, valor) in zip(encab, line)}
      datapaises.append(pais)  #lista con dicc
  return datapaises


if __name__ == '__main__':
  info = readCSV('./App/dataWP.csv')
  print(len(info))
  print(info[55])

#ESTRUCTURA
