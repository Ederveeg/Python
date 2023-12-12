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

