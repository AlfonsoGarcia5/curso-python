import csv  #funciones especiales csv


def readCSV(path):  #function, name(variable)
  with open(path, 'r') as filecsv:
    lector = csv.reader(filecsv, delimiter=',')
    #csv.reader es una instrucción "reader" de la utilería "csv"
    #se manda el archivo (el creado antes como nombre en la instrucción open-as), y el caracter del delimitador (revisar archivo fuente)
    #delimiter es una palabra ya declarada, no es variable, se debe usar la misma
    for line in lector:

      print('***' * 5)
      print(line)


#Declaro el final para correr la función como un script, llamándolo de otro módulo y pudiendo ejecutarlo del main, de la consola (clases anteriores)
if __name__ == '__main__':
  readCSV('./App/dataWP.csv')

#ESTRUCTURA
'''
1- Función para mandar leer un scs (readCSV)
2- Anidado comando "with open" para abrir/cerrar archivo, declarado con su nombre "filecsv"
3- Funciones de lectura anidadas en "with open"
  3.1- Declaración de variable o archivo usando función impotada csv.reader, enviando nombre del archivo creado con "with open" y delimitador
  3.2- for anidado en "with open" para iterar la variable lector (3.1) línea por línea
'''
