#Ejercicio 1: Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
'''
user = int(input('Digita tu edad: '))

if user >= 18:
    print('¡Eres mayor de edad!')
else:
    print('¡Eres menor edad!')
'''

#Ejercicio 2: Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''
password = 'contraseña'
user = input('Escribe tu contraseña: ')

if password == user.lower():
    print('Acceso concedido')
else:
    print('Contraseña incorrecta')
'''

#Ejercicio 3:Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
'''
num1 = int(input('Digita el divisor: '))
num2 = int(input('Digita el dividendo: '))
resultado = num1 / num2

if num1 == 0:
    print('Introduce un valor que no sea 0 o negativo')
else: 
    print('El resultado es', resultado)
'''

#Ejercicio 4: Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
'''
print('Este programa te dirá si tu número entero es par o impar')
user = int(input('Digita un número entero: '))

if user % 2 == 0:
    print('Tu número es par')
else:
    print('Tu número es impar')
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

#Ejercicio 8: Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
'''
puntuacion = float(input('Digite la puntuacion del usuario: '))
pago = 2400.00 * puntuacion

if puntuacion <= 0.3:
    print('El nivel de rendimiento es inaceptable, recibirias la cantidad de', str(pago), 'euros')
else:
    if puntuacion >= 0.4 and puntuacion <= 0.5:
        print('El nivel de rendimiento es aceptable, recibirias la cantidad de', str(pago), 'euros ademas de tu sueldo base de 2,400 euros')
    else:
        if puntuacion >= 0.6 and puntuacion <= 2.0:
            print('El nivel de rendimiento es meritorio, recibirias la cantidad de', str(pago), 'euros ademas de tu sueldo base de 2,400 euros')
'''

#Ejercicio 9: Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
'''
print('¡Bienvenido a sala de videojuegos nova!')
user = int(input('¿Cual es tu edad? '))

if user <= 4:
    print('¡Tu entrada es gratis!')
    print('¡Disfruta de la sala de videojuegos :D!')
else:
    if user >= 5 and user <= 18:
        print('El valor de la entrada es de 5 euros')
        print('¡Gracias por tu preferencia!, Disfruta de la sala de videojuegos :D')
    else:
        if user >= 18:
            print('El valor de la entrada es de 10 euros')
            print('¡Gracias por tu preferencia!, Disfruta de la sala de videojuegos :D')
 '''   

#Ejercicio 10: La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
#
#    Ingredientes vegetarianos: Pimiento y tofu.
#    Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
'''
print('¡Bienvenido a pizzería Bella Napoli!')
user = input('Su pizza sera vegana o no vegana? ')

if user.lower() == 'vegana':
    print('¡Gran elección!')
    print('Todas las pizzas llevan mozzarella y tomate')
    ingredients = input('Selecciona uno de los ingredientes: Pimiento o Tofu ')
    if ingredients.lower() == 'tofu': 
        print('¡Perfecto! elegiste una pizza vegana de mozzarella y', ingredients.lower())
        print('En un momento estara lista su orden :D')
    else:
        if ingredients.lower() == 'pimiento': 
            print('¡Perfecto! elegiste una pizza vegana de mozzarella y', ingredients.lower())
            print('En un momento estara lista su orden :D')       
        else:
            print('¡Lamentamos no tener el ingrediente que solicitas, por favor elige un ingrediente disponible!')
else:
    if user.lower() == 'no vegana':
        print('¡Gran elección!')
        print('Todas las pizzas llevan mozzarella y tomate')
        ingredients = input('Selecciona uno de los ingredientes: Peperoni, jamón o salmón ')
        if ingredients.lower() == 'peperoni':
            print('¡Perfecto! elegiste una pizza no vegana de mozzarella y', ingredients.lower())
            print('En un momento estara lista su orden :D')
        else:
            if ingredients.lower() == 'jamon':
                print('¡Perfecto! elegiste una pizza no vegana de mozzarella y', ingredients.lower())
                print('En un momento estara lista su orden :D')
            else: 
                if ingredients.lower() == 'salmon':
                    print('¡Perfecto! elegiste una pizza no vegana de mozzarella y', ingredients.lower())
                    print('En un momento estara lista su orden :D')
                else:
                    print('¡Lamentamos no tener el ingrediente que solicitas, por favor elige un ingrediente disponible!')
    else:
        print('Por favor Elige una opcion valida :D')
'''
# Presentación del menú con los tipos de pizza
print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduce el número correspondiente al tipo de pizza que quieres:")
# Decisión sobre el tipo de pizza
if tipo == "1":
    print("Ingredientes de pizzas vegetarianas\n\t 1- Pimiento\n\t2- Tofu\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else: 
        print("tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetarina con mozarrella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("salmón")

