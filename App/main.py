import utils  #archivo modulo python que hice
import chart3

database = [{
  'Country': 'Mex',
  'Pop': 200
}, {
  'Country': 'Fra',
  'Pop': 300
}, {
  'Country': 'Can',
  'Pop': 250
}, {
  'Country': 'Jap',
  'Pop': 120
}]


 
def run():
  ke, val = utils.get_population()
  print(ke, val)
  '''al correrla en el shell, como está en un folder "python app/main.py" (este archivo)'''

  #print(utils.texto)  #variable de mod
  '''Modulización: hacer varios módulos/programas con las funciones que usaremos, para en otro       programas'''
  '''
  inpais = input('Escoge el País: Mex-Fra-Can-Jap =>   ')
  if inpais == 'Mex' or 'Fra' or 'Can' or 'Jap':
    popul = utils.popul_by_country(database, inpais)
    print(popul)
  else:
    print('Opción no existe')
  '''

  chart3.runapp()
  

'''Lo siguiente para que se pueda correr main desde el shell directo y también como módulo desde otro donde se importe'''
if __name__ == '__main__':
  run()
  