#Este programa calcula el tiempo de trabajo de una persona y da como resultado el salario por hora

usuario = (input("Cual es tu nombre? "))
horas = int(input('Hola ' + usuario + ', Cuantas hora trabajaste? '))
paga_hora = 23.97
calculador = horas * paga_hora

print(usuario, 'Tu paga es de: ', calculador, 'Dolares')