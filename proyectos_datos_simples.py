#Este archivo tiene proyectos de datos simples

#Ejercicio 1: Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde
'''
usuario = (input('Cual es tu nombre de usuario? '))
horas = float(input('Hola ' + usuario + '! cuantas horas trabajaste? '))
pago = 3.47
resultado_final = pago * horas 
print('Tu pago sera de ' + str(resultado_final) + ' Dolares :D')
'''

#Ejercicio 2: Escribir un programa que lea un entero positivo, , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta . La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:
'''
print('Este programa lee numeros y te muestra la suma de todos los enteros hasta el numero que solicitaste')
numero = int(input('Introduce un numero: '))
suma = numero * (numero + 1) / 2
print('Tu resultado es: ' + str(suma))
'''

#Ejercicio 3: Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.


user = (input('Cual es tu nombre? '))
weight = float(input('Muy bien ' + user + ', cual es tu peso? (Kg) '))
height = float(input('Cual es tu altura? (mts) '))
body = weight / height ** 2
print('Tu indice de masa corporal es: ' + str(body))


#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

'''
n = input("Introduce el dividendo (entero): ")
m = input("Introduce el divisor (entero): ")
print(n + " entre " +  m + " da un cociente " + str(int(n) // int(m)) + " y un resto " + str(int(n) % int(m)))
'''

#Ejercicio 4:Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

'''
print('¡Bienvenido a Mexbanc!')
inversion = float(input('¿Cuanto deseas invertir? '))
interes_anual = 8/100
print('El interes anual es de 8%')
año = float(input('¿Cuantos años deseas invertir? '))
resultado_final = inversion * interes_anual * año
total_obtenido = inversion + resultado_final
print('Tu capital obtenido sera de: ' + str(resultado_final) + ' MXN')
print('En total otendras: ' + str(total_obtenido) + ' MXN')
'''

#Ejercicio 5:Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

'''
peso_muñecas = 75
peso_payasos = 112
cantidad_muñecas = int(input('¿Cual es la cantidad de muñecas vendidas? '))
cantidad_payasos = int(input('¿Cual es la cantidad de payasos vendidos? '))
total_peso_muñecas = cantidad_muñecas * peso_muñecas
total_peso_payasos = cantidad_payasos * peso_payasos
peso_kg_muñecas = total_peso_muñecas / 1000
peso_kg_payasos = total_peso_payasos / 1000
print('EL peso de las muñecas es de ' + str(total_peso_muñecas) + 'gramos, o de ' + str(peso_kg_muñecas) + ' Kg')
print('EL peso de los payasos es de ' + str(total_peso_payasos) + 'gramos, o de ' + str(peso_kg_payasos) + ' Kg')
'''

#Ejercicio 6: Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

'''
precio_pan = 3.49
precio_descuento = 2.09
pan_total = int(input('¿Cuanto pan se hizo en el dia? '))
pan_vendido = int(input('¿Cuanto pan se vendio en ese dia? '))
total_no_vendido = pan_total - pan_vendido
print('Quedan ' + str(total_no_vendido) + ' panes de ayer')
ganancia_total = total_no_vendido * precio_descuento
perdida_total = total_no_vendido * 1.4
print('El precio habitual de este pan es de 3.49 Euros')
print('Tiene descuento de 60% por ser del dia de ayer y queda en 2.09 Euros')
print('El coste total final de todo el pan con descuento es de ' + str(round(ganancia_total)) + ' Euros,la perdida es de ' + str(round(perdida_total)) + ' Euros')
'''







