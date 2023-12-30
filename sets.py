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
#Se pueden buscar las cosas cómo en cualquier lista con len
set_fruit = {'pear', 'apple', 'strawberry'}

size  = len(set_fruit)
print(size)

print('apple' in set_fruit)
print('pineapple' in set_fruit)

#con .add podemos agregar caracteres al set
set_fruit.add('pineapple')
print(set_fruit)
set_fruit.add('pineapple')
print(set_fruit)

#.update
set_fruit.update({'watermelon', 'banana', 'apple'})
print(set_fruit)

#.remove si no encuentra tu caracter o esta mal escrito te lanzara error
set_fruit.remove('apple')
print(set_fruit)

#.discard si no encuentra el caracter no lanza error, solo te avisa que no encontro la key
set_fruit.discard('orange')
print(set_fruit)

#.clear limpia todo el conjunto
set_fruit.clear()
print(set_fruit)






