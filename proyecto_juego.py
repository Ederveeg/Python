#Juego piedra papel o tijera

import random
options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0
rounds = 1

while True:

    print('*' * 10 )
    print('ROUND', rounds)
    print('*' * 10)

    print('victorias del jugador', user_wins)
    print('victorias de la computadora', computer_wins)


    #Declarar 2 variables: jugador y pc
    jugador = input('piedra, papel o tijera: ').lower().strip()
    pc = random.choice(options)

    if not jugador in options:
        print('Esa opcion no es valida')
        continue

    print('El jugador escogio: ', jugador)
    print('El pc escogio: ', pc)

    #Condicionales
    if jugador == pc:
        print('¡Empate!')
    elif (jugador == 'piedra' and pc == 'tijera') or (jugador == 'papel' and pc == 'piedra') or (jugador == 'tijera' and pc == 'papel'):
        print('¡Ganaste!')
        user_wins += 1
    else:
        print('Perdiste')
        computer_wins += 1

    if computer_wins == 3:
        print('¡El computador gano!')
        break

    if user_wins == 3:
        print('¡Ganaste la partida!')
        break

    rounds += 1




