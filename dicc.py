#Uso de diccionarios en python
my_dicc = {}
print(type(my_dicc))

#Asi se crea un diccionario
my_dicc = {
    'Carro' : "Vehiculo",
    'name' : 'Eder',
    'last_name' : 'Ayala Vega',
    'age' : 19
}

print(my_dicc)
print(len(my_dicc))

print(my_dicc['age'])
print(my_dicc['last_name'])
print(my_dicc.get('age'))

#Asi puedes ver si alguna llave esta dentro del diccionario
print('avion' in my_dicc)
print('age' in my_dicc)

#PARTE 2

#Aqui aprendimos a hacer actualizacion e incersion en el diccionario

person = {
    'name': 'Eder',
    'last_name' : 'Vega',
    'langs' : ['Python', 'Javascript'],
    'age' : 19
}
print(person)

#Esta es la forma para actualizar cosas del diccionario
person['name'] = 'Aldhair'
person['age'] -= 1
person['langs'].append('rust')
print(person)

#con del podemos eliminar cosas del diccionario al igual que con .pop
del person['age']
person.pop('name')
print(person)

#.items devuelve en pares las tuplas
print('items')
print(person.items())

#devuelve las llaves que se estan usando
print('keys')
print(person.keys())

#Retorna lista de los valores de las tuplas
print('values')
print(person.values())





