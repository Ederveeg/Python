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

#Ejercicio 5: Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
'''
print('Este programa invierte frases')
user = input('Introduce una frase:')
print('Tu frase invertida es: ' + user[::-1])
'''
#Ejercicio 6: Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
'''
print('Este programa hace que la vocal que indiques se ponga en mayuscula')
user = input('Introduce una palabra: ')
vocal = input('Introduce una vocal en minuscula: ')
print(user.replace(vocal, vocal.upper()))
'''

#Ejercicio 7: Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
'''
user = input('Introduce tu correo electronico: ')
print(user[:user.find('@')] + '@ceu.es')
'''

#Ejercicio 8: Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
'''
euros = str(input('¿Cual es el precio de tu producto en euros? (Con dos decimales) '))
print('El precio del producto es de ' + euros[: euros.find('.')] + ' euros y ' + euros[euros.find('.')+1:] + ' centimos.' )
'''

#Ejercicio 9:Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
'''
fecha = str(input('Escribe tu fecha de nacimiento en el siguiente fromato: (dd/mm/aaaa)'))
print('Tu dia de nacimiento es ' + fecha[: fecha.find('/')] + ' del mes ' + fecha[fecha.find('/')+1:-5] + ' y año ' + fecha[fecha.find('/')+4:])

#otra solucion
fecha = input("Introduce la fecha de tu nacimiento en formato dd/mm/aaaa: ")
print('Día', fecha[:2])
print('Mes', fecha[3:5])
print('Año', fecha[6:])
'''

#Ejercicio 10:Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
'''
user = input('Introduce tu lista de compras separado por coma: ')
print(user.replace(',', '\n'))
'''
#Ejercicio 11:Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
'''
producto = input('Introduce el nombre del producto: ')
precio = float(input('Introducde el precio unitario: '))
unidades = int(input('Introduce el {número de unidades: '))
print('{producto}: {unidades:03d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))
'''
