import main

print(
  'Example => ', main.database
)  #así solo corre todo el main, no solo el archivo .database que se quiso jalar
'''Hay que modulizar para que solo se ejecute lo que queremos y no todo el contenido del módulo que imporamos, una forma es en ese módulo definir todo dentro de funciones'''

main.run()
'''Correrá lo que esté dentro de main run()'''
'''Ejecutar como scrip
Main se metió todo dentro de una función run para poder comandar desde example una parte sin correr el resto de main, pero al ejecutar main ya no corre
Se buscará: correr main desde examp, pero también que corra main, cuando se ejecute directo desde el Shell

En el main, se agregará al final el comando en el curso previo

if __name__=='__main__':
  run()
  
  '''
