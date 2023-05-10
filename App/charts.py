import matplotlib.pyplot as plt
#no viene incorporado en python, hay que bajarlo e instalarlo, buscando en el cubo "packager" directamente la librería e instalándola
#as "plt" para usarlo como alias


def gen_graf_barras(etiq, val):

  fig, ax = plt.subplots()  #declaración de uso de el figura y eje
  ax.bar(etiq, val)  #ax.bar set de grafica de barras, pide etiq y valores
  plt.show()  #comando para graficar


def gen_graf_pie(etiq, val):
  fig, ax = plt.subplots()
  ax.pie(val, labels=etiq)
  #labels=etiq es parte de las reglas de definición de variables de la gráfica de pie, igualar con labels
  ax.axis('equal')  #igualado para que sea pie de círculo
  plt.show()


if __name__ == '__main__':
  etiquetas = ['a', 'b', 'c']
  valores = [100, 800, 300]
  #gen_graf_barras(etiquetas, valores)
  gen_graf_pie(etiquetas, valores)
