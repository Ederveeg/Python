'''
numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ['make a dishes', 'play videogames']
print (tasks)

types = [1, True, 'Hola']
print(types)

print(numbers[0])
print(tasks[0])
text = 'Hola'
#text[0] = 'W'

tasks[0] = 'Watch movies'
print(tasks)
'''
'''
numbers =[1, 2, 3, 4, 5]
print(numbers[1])

#Esto nos actualiza la list el [-1] es la ultima posicion y el = 10 es lo que vamos a agregar
numbers[-1] = 10
print(numbers)

#.append agrega elementos al final de la lista
numbers.append(700)
print(numbers)

#.insert pone el caracter que quieras en el lugar que quieras, el primer caracter '0' es el lugar donde va y el segundo caracter 'Hola' es lo que se añadira a la lista
numbers.insert(0, 'Hola')
print(numbers)

#Asi se pueden fusionar las listas
tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks
print(new_list)

#Esto sirve para preguntar donde esta cierto caracter, luego de encontrarlo lo reemplazamos asi
index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list)

#.remove sirve para borrar un elemento
new_list.remove('todo 1')
print(new_list)

#.pop elimina el ultimo elemento, si quieres eliminar un carcter especifico ponle entre parentesis el parametro
new_list.pop()
print(new_list)

#.reverse sirve para voltear todo el array
new_list.reverse()
print(new_list)

#.sort ordena los arrays de menor a mayor o en orden alfabetico. Ten cuidado ya que si combinas tipos de datos diferentes note ejecutara
numbers_a = [1, 6, 5, 2, 3]
numbers_a.sort()
print(numbers_a) 
'''

#PARTE 2
#List comprehension
'''
numbers = []
for element in range(1,11):
    numbers.append(element * 2)

print(numbers)

numbers_v2 = [element * 2 for element in range(1, 11)]
print(numbers_v2)
'''

numbers = []
for i in range(1,11):
    if i % 2 == 0:
        numbers.append(i * 2)

print(numbers)
#Esta forma de abajo es el list comprehension
numbers_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers_v2)


