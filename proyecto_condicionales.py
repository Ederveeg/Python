#Proyecto de creacion de programa que evalue si un numero es par o impar

#variable numero con la cual trabajaremos para obetener su dato de entrada
numero = int(input('Ingresa un numero: '))

if numero % 2 == 0:
    print('Tu numero es par')
else:
    print('Tu numero es impar')