import csv
import utils
import matplotlib.pyplot as plot


def runapp():
  dic = utils.readCSVorig('./App/dataWP.csv')
  # paises = list(map(lambda x: x['Country/Territory'], dic))
  # pobl = list(map(lambda x: x['World Population Percentage'], dic))
  filtrado = list(filter(lambda x: x['Continent'] == 'Asia', dic))
  paises = list(map(lambda x: x['Country/Territory'], filtrado))
  pobl = list(map(lambda x: x['World Population Percentage'], filtrado))

  utils.gen_graf_barras(paises, pobl)


if __name__ == '__main__':
  runapp()
