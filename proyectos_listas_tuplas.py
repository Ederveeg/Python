#En este archivo veras proyectos de listas y tuplas hechos por mi
'''
materias = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
print(materias)
'''

#Ejercicio 2: Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
'''
materias = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
for materias in materias:
    print('Yo estudio', materias)
'''

#Ejercicio 3:Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
'''
materias = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
calificacion_mate = input('¿Cual es tu calificacion en Matemáticas? ')
calificacion_fisica = input('¿Cual es tu calificacion en Física? ')
calificacion_quimica = input('¿Cual es tu calificacion en Química? ')
calificacion_hist = input('¿Cual es tu calificacion en Historia? ')
calificacion_leng = input('¿Cual es tu calificacion en Lengua? ')
calif = [calificacion_mate, calificacion_fisica, calificacion_quimica, calificacion_hist, calificacion_leng]
for i in materias:
    print('En', materias[0], 'has sacado', calif[0])
    print('En', materias[1], 'has sacado', calif[1])
    print('En', materias[2], 'has sacado', calif[2])
    print('En', materias[3], 'has sacado', calif[3])
    print('En', materias[4], 'has sacado', calif[4])

#Otra solucion: 

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])
'''

#Ejercicio 4: Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
'''
ganadores = []
for i in range(6):
    ganadores.append(int(input('Introduce un numero ganador')))
ganadores.sort()
print('Los números ganadores son: ' + str(ganadores))
'''
    
#Ejercicio 5: Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
'''
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list.sort(reverse=True)
print(list)
'''

#Ejercicio 6: Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
'''
materias = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
calificacion = []
for materia in materias:
    calif = float(input('¿Que calificacion has sacado en ' + materia + ' ?' ))
    if calif > 5:
        calificacion.append(materia)
for materia in calificacion:
    materias.remove(materia)
print('Tienes que recursar', str(materias))
'''

#Ejercicio 7: Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
'''
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]  
for i in range(27):
    if not numbers[i] % 3 == 0:
        print(abc[i])
'''

#Ejercicio 8: Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
'''
print('Este programa indica si tu palabra en un palíndromo')
palabra = str(input('Introduce una palabra:'))
inversa = palabra[::-1]

if palabra == inversa:
    print('Tu palabra es un palíndromo')
else:
    print('Tu palabra no es un palíndromo')
'''

#Ejercicio 9: Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
'''
print('Este programa muestra cuantas veces repite vocales una palabra')
palabra = input('Introduce tu palabra: ')
print('tiene la "a"', palabra.count('a'), 'veces')
print('tiene la "e"', palabra.count('e'), 'veces')
print('tiene la "i"', palabra.count('i'), 'veces')
print('tiene la "o"', palabra.count('o'), 'veces')
print('tiene la "u"', palabra.count('u'), 'veces')

# otra solucion
word = input("Introduce una palabra: ")
vocals = ['a', 'e', 'i', 'o', 'u']
for vocal in vocals: 
    times = 0
    for letter in word: 
        if letter == vocal:
            times += 1
    print("La vocal " + vocal + " aparece " + str(times) + " veces")
'''

#Ejercicio 10: Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
'''
precio = [50, 75, 46, 22, 80, 65, 8,]
precio.sort()

print('El precio más bajo es de:', precio[0])
print('El precio más alto es de:', precio[-1])
'''

#Ejercicio 11: Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
'''
print('Este programa calcula el producto escalar: a = (1,2,3) y b = (-1,0,2)')
a = (1,2,3)
b = (-1,0,2)
m = [a*b for a,b in zip(a,b)]
print('El resultado de la multiplicacion es', m)
for i in m:
    print('el resultado total es:', sum(m))

#Otra solucion:

a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(a)):
    product += a[i]*b[i]
print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product))
'''

#Ejercicio 12: Escribir un programa que almacene las matrices 
'''
a = ((1, 2, 3),
     (4, 5, 6))
b = ((-1, 0),
     (0, 1),
     (1,1))
result = [[0,0],
          [0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
for i in range(len(result)):
    result[i] = tuple(result[i])
result = tuple(result)
for i in range(len(result)):
    print(result[i])
'''
















