#Este archivo tiene proyectos de datos simples

#Ejercicio 1: Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde

usuario = (input('Cual es tu nombre de usuario? '))
horas = float(input('Hola ' + usuario + '! cuantas horas trabajaste? '))
pago = 3.47
resultado_final = pago * horas 
print('Tu pago sera de ' + str(resultado_final) + ' Dolares :D')