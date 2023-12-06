#Juego piedra papel o tijera

#Declarar 2 variables: jugador y pc
jugador = input('piedra, papel o tijera: ')
pc = 'papel'

#Condicionales
if jugador == pc:
    print('¡Empate!')
elif (jugador == 'piedra' and pc == 'tijera') or (jugador == 'papel' and pc == 'piedra') or (jugador == 'tijera' and pc == 'papel'):
    print('¡Ganaste!')
else:
    print('Perdiste')