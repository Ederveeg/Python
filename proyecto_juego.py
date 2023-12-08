#Juego piedra papel o tijera

import random
options = ('piedra', 'papel', 'tijera')

#Declarar 2 variables: jugador y pc
jugador = input('piedra, papel o tijera: ').lower().strip()
pc = random.choice(options)

print('El jugador escogio: ', jugador)
print('El pc escogio: ', pc)

#Condicionales
if jugador == pc:
    print('¡Empate!')
elif (jugador == 'piedra' and pc == 'tijera') or (jugador == 'papel' and pc == 'piedra') or (jugador == 'tijera' and pc == 'papel'):
    print('¡Ganaste!')
else:
    print('Perdiste')