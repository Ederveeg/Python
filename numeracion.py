#Este programa es para ver si el numero tiene una raiz cuadrada exacta
'''
user = int(input('Escoge un entero: '))
respuesta = 0

while respuesta**2 < user:
    print(respuesta)
    respuesta += 1

if respuesta**2 == user:
    print(f'La raiz cuadrada de {user} es {respuesta}')
else:
    print(f'{user} no tiene una raiz cuadrada exacta')
'''
#La enumeracion exhaustiva ews para recorrer todas las variables posibles y terminar cuando llegue al resultado

#Aproximacion de soluciones: es como la enumeración exhaustiva pero no necesita respuesta exacta.
#Podemos aproximar soluciones con un margen de error que llamaremos epsilon.
    
#En este programa encontraremos la raiz cuadrada exacta pero con aproximacion de soluciones.
'''
user = int(input('Escoge un número: '))
epsilon = 0.0001
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - user) >= epsilon and respuesta <= user:
    print(abs(respuesta**2 - user), respuesta)
    respuesta += paso

if abs(respuesta**2 - user) >= epsilon:
    print(f'No se encontro la raiz cuadrada {user}')
else:
    print(f'La raiz cuadrada de {user} es {respuesta}')
'''

    





