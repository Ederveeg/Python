#Aqui aprendi a usar conjuntos
'''
set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))
'''
#Los sets eliminan los caracteres repetidos
'''
set_numbers = {1, 2, 2, 3, 435, 324}
print(set_numbers)
'''
#Los sets altera el orden que tiene escrito dentro
'''
set_types = {1, 'hola', False, 12.12}
print(set_types)
'''
#Asi se puede deividir la 'palabra letra por letra
'''
set_from_string = set('hoola')
print(set_from_string)

set_from_tuples = set(('abc', 'des', 'sa', 'abc'))
print(set_from_tuples)
'''
#Puedes transformar una lista a un set para que no tengas que revisar toda la lista y sacar los numeros o caracteres repetidos
'''
numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)
'''
#PARTE 2
#Se pueden buscar las cosas cómo en cualquier lista con len
'''
set_fruit = {'pear', 'apple', 'strawberry'}

size  = len(set_fruit)
print(size)

print('apple' in set_fruit)
print('pineapple' in set_fruit)
'''
#con .add podemos agregar caracteres al set
'''
set_fruit.add('pineapple')
print(set_fruit)
set_fruit.add('pineapple')
print(set_fruit)
'''
#.update
'''
set_fruit.update({'watermelon', 'banana', 'apple'})
print(set_fruit)
'''
#.remove si no encuentra tu caracter o esta mal escrito te lanzara error
'''
set_fruit.remove('apple')
print(set_fruit)
'''
#.discard si no encuentra el caracter no lanza error, solo te avisa que no encontro la key
'''
set_fruit.discard('orange')
print(set_fruit)
'''
#.clear limpia todo el conjunto
'''
set_fruit.clear()
print(set_fruit)
'''
#PARTE 3
#Operaciónes en conjunto

set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

#.union une los conjuntos, el segundo metodo es lo mismo y se encuentra en print
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

#.intersection sirve para ver cuales son los caracteres que son iguales
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

#.difference le resta el segundo conjunto al primero
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

#.symmetric_difference solo hace unión si los elementos coinciden
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)



