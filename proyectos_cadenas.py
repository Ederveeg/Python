#En este archivo encontraremos distintos ejercicios de cadenas ya resueltos

#Ejercicio 1: Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
'''
print('¡Este programa repite tu nombre las veces que quieras!')
user = input('¿Cual es tu nombre? ')
number = input ('Digita un numero: ')
print((user + '\n') * int(number))
'''
#Ejercicio 2: Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
'''
user = str(input('Introduce tu nombre completo: '))
print(user.lower())
print(user.upper())
print(user.title())
'''

#Ejercicio 3:Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
'''
user = input('¿Cual es tu nombre? ')
print(user.upper() + ' Tiene ' + str(len(user)) + ' letras ')
'''

#Ejercicio 4:Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
'''
tel = input ('Introduce un numero de telefono con el formato +xx-xxxxxxxxx-xx')
print('El numero de telefono es ', tel[4:-3])
'''

#Ejercicio 5: Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
'''
user = int(input('¿Cual es tu edad? '))
ingreso = int(input('¿Cuanto ingreso recibes al mes? '))

if user >= 16:
    if ingreso >= 1000:
        print('Puedes tributar')
    else:
        print('Debes ganar mas de 1000 Euros mensuales para poder tributar')
else:
    print('Debes tener mas de 16 años para poder tributar')
'''

#Ejercicio 6: Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
'''
name = input('Introduce tu primer nombre: ')
gender = input('Introduce tu sexo:("M" o "F") ')

if gender == 'M':
    if name.lower() < 'm':
        group = 'A'
    else:
        group = 'B'
else:
    if name.lower() > 'n':
        group = 'A'
    else:
        group = 'B'

print('Tu equipo es ' + group)
'''

#Ejercicio 7:Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
'''
user = int(input('¿Cual es su renta anual?(Euros)'))
if user < 10000:
    print('Tu tipo impositivo es del 5%')
else:
    if user >= 10000 and user <= 20000:
        print('Tu tipo impositivo es del 15%')
    else:
        if user >= 20000 and user <= 35000:
            print('Tu tipo impositivo es del 20%')
        else:
            if user >= 35000 and user <= 60000:
                print('Tu tipo impositivo es del 30%')    
            else:
                 if user >= 60000:
                    print('Tu tipo impositivo es del 45%')     
'''











