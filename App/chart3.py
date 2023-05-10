import csv
import utils
import matplotlib.pyplot as plot


def runapp():
  keys = utils.readCSV('dataWP.csv', 2) #pais indexado en columna 2 del csv ruteado
  # print(keys)
  values = utils.readCSV('dataWP.csv', 16) #col 16 es el % de pobl mundial
  # print(values)
  utils.gen_graf_barras(keys, values, "Name_test")
  utils.gen_graf_pie(keys, values, "Name_test")


if __name__ == '__main__':
  runapp()
