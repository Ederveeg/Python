#Este archivo es para los proyectos de bucles copn while y for

#Ejercicio 1: Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
'''
user = input('Escribe una palabra: ')
number = input('Digita un número: ')
print((user + '\n') *  int(number))
'''

#Ejercicio 2: Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''
edad = int(input('¿Cual es tu edad? '))
counter = 0

while edad < 100:
    counter += 1
    if counter > edad:
        break
    print(counter)

#otra solución

age = int(input("¿Cuántos años tienes? "))
for i in range(age):
    print("Has cumplido " + str(i+1) + " años")
'''

#Ejercicio 3: Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''
number = int(input('Digita un número entero positivo: '))

for i in range(1, number+1, 2):
    print(i, end=', ')
'''

#Ejercicio 4: Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
'''
n = int(input('Digita un número entero positivo: '))

for i in range(n, -1, -1):
    print(i, end=', ')
'''

#Ejercicio 5: Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
'''
monto = int(input('Cuanto desea invertir?' ))
interes = int(input('¿Cual es el interes anual de su inversion? '))
time = int(input('¿Cuantos años invertira? '))
for i in range(time):
    monto *= 1 + interes/100
    print('Capital tras ' + str(i+1) + ' años: ' + str(round(monto,2)))
'''
#Ejercicio: 6 Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
'''
print('Este programa dibuja triangulos')
n = int(input('Introduce un numero entero: '))
simbolo = '*'
print(simbolo)
for i in range(n-1):
    simbolo = '*' + simbolo 
    print(simbolo)
'''

#Ejercicio 7: Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10
'''
print('Este programa enseña la tabla de multiplicar del 1 al 10')
tabla1 = int(input('¿Que tabla quieres ver? (del 1 al 10)'))

for i in range(1, 11):
    result = int(i) * tabla1
    print(str(i) + ' * '+ str(tabla1) + ' = ' + str(result))

#Otra solucion:
    for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")
'''

#Ejercicio 8:Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
'''
print('Este programa dibuja triangulos')
n = int(input('Introduce un numero entero: '))

for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=' ')
    print('')
'''
#Ejercicio 9: Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
'''
contraseña = input('Ingresa tu nueva contraseña: ')
contraseña_entrada = input('Ingresa tu contraseña: ')

if contraseña == contraseña_entrada:
    print('Accediste')
else:
    print('Contraseña incorrecta')
'''
#otra solucion
'''
key = 'contraseña'
password = ''
while password != key:
    password = input("Introduce la contraseña: ")
print("Contraseña correcta")
'''

#Ejercicio 10: Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
'''
numero= int(input("¿Qué número quieres saber si es primo? "))
valor= range(2,numero)
contador = 0
for n in valor:
  if numero % n == 0:
    contador +=1
    print("divisor:", n)
 
if contador > 0 :
  print("El número no es primo" )
else:
  print("El nÚmero es primo")
'''

#Ejercicio 11: Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
'''
p = input('Introduce una palabra: ')
for i in p[::-1]:
    print(i)
'''

#Ejercicio 12: Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
'''
f = input('Introduce una frase: ')
l = input('Introduce una letra: ')
print(f.count(l))

#otra solucion:

frase = input("Introduce una frase: ")
letra = input("Introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))
'''

#Ejercicio 13: Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
'''
while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        break
    print(frase)
'''




