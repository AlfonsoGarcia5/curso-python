'''
Refactorizacion
Quebrar en funciones para asignar responsabilidades específicas. Hacer la corrida/ejecución del programa más legibles basado en funciones y así modificar en bloques independientees
'''

import random


def obt_opciones():
  opcionestupl = ('piedra', 'papel', 'tijera')
  usropt = input('Escoje: piedra, papel o tijera=> ')
  usropt = usropt.lower()
  compopt = random.choice(opcionestupl)
  return usropt, compopt, opcionestupl


def valid_opc(usropt, opciones):
  if not usropt in opciones:
    print('Escoje una opcion válida')
    return False
  else:
    return True


def corrida_chk(usropt, compopt):
  if usropt == 'piedra':
    if compopt == 'piedra':
      print('Empate!')
      return 0, 0, 1
    elif compopt == 'papel':
      print('Perdiste! piedra pierde contra papel')
      return 0, 1, 0
    elif compopt == 'tijera':
      print('Ganaste! piedra gana a tijera')
      return 1, 0, 0

  elif usropt == 'papel':
    if compopt == 'piedra':
      print('Ganaste! papel gana a piedra')
      return 1, 0, 0
    elif compopt == 'papel':
      print('Empate!')
      return 0, 0, 1
    elif compopt == 'tijera':
      print('Perdiste! papel pierde contra tijera')
      return 0, 1, 0

  elif usropt == 'tijera':
    if compopt == 'piedra':
      print('Perdiste! tijera pierde contra piedra')
      return 0, 1, 0
    elif compopt == 'papel':
      print('Ganaste! tijera gana a papel')
      return 1, 0, 0
    elif compopt == 'tijera':
      print('Empate!')
      return 0, 0, 1


def check_winer(uw, cw, emp):
  if cw > uw:
    print('Gano la computadora, mejor suerte la proxima')
  elif cw < uw:
    print('Felicidades, ganaste')
  elif cw == uw:
    print('Esto es un empate')


def run_game():
  rounds = 1
  uw = 0
  cw = 0
  emp = 0
  totround = int(input('Cuantas rondas deseas jugar? >>'))
  while rounds <= totround:
    print('*' * 10)
    print('ROUND ' + str(rounds))
    print('*' * 10)
    usropt, compopt, opciones = obt_opciones()
    opvalid = valid_opc(usropt, opciones)
    if opvalid:
      uc, cc, ec = corrida_chk(usropt, compopt)
      rounds += 1
      uw += uc
      cw += cc
      emp += ec
    else:
      continue
  print('Fin de la partida')
  check_winer(uw, cw, emp)
  return uw, cw, emp


usrw, compw, emp = run_game()
print('\nUsuario gana ' + str(usrw) + ' veces')
print('Computadora gana ' + str(compw) + ' veces')
print(str(emp) + ' empates')
