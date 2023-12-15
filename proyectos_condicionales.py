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