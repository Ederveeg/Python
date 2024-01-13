#Uso de diccionarios en python
'''
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
'''
#Asi puedes ver si alguna llave esta dentro del diccionario
'''
print('avion' in my_dicc)
print('age' in my_dicc)
'''
#PARTE 2

#Aqui aprendimos a hacer actualizacion e incersion en el diccionario
'''
person = {
    'name': 'Eder',
    'last_name' : 'Vega',
    'langs' : ['Python', 'Javascript'],
    'age' : 19
}
print(person)
'''
#Esta es la forma para actualizar cosas del diccionario
'''
person['name'] = 'Aldhair'
person['age'] -= 1
person['langs'].append('rust')
print(person)
'''
#con del podemos eliminar cosas del diccionario al igual que con .pop
'''
del person['age']
person.pop('name')
print(person)
'''
#.items devuelve en pares las tuplas
'''
print('items')
print(person.items())
'''
#devuelve las llaves que se estan usando
'''
print('keys')
print(person.keys())
'''
#Retorna lista de los valores de las tuplas
'''
print('values')
print(person.values())
'''

#PARTE 3
#Dicc comprehension
'''
dict = {}
for i in range(1, 5):
    dict[i] = i * 2

print(dict)
'''
#Esta solucion de abajo es con dicc comprehension
'''
dict_v2 = {i: i * 2 for i in range(1, 5)}
print(dict_v2)
'''
#Otro ejemplo
'''
import random
countries = ['COL', 'MEX', 'BOL', 'PE']
population = {}
for country in countries:
    population[country] = random.randint(1,100)

print(population)
'''
#Esta solucion es la de dicc comprehension
'''
population_v2 = { country: random.randint(1, 100) for country in countries}
print(population_v2)
'''
#Asi se fusionan dos listas
'''
names = ['nico', 'zule', 'alex']
ages = [12, 34, 21]

print(list(zip(names, ages)))
'''
#Esta solucion es con dicc comprehension
'''
new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)
'''

#Dictionary comprehension: Condicionales

#Programa que pone de manera random la poblacion de cada pais, luego filtra y solo si es mayor a 20 lo imprime
'''
import random
countries = ['COL', 'MEX', 'BOL', 'PE']

population_v2 = { country: random.randint(1, 100) for country in countries}
print(population_v2)

result = { country: population for (country, population) in population_v2.items() if population >= 20}
print(result)
'''

#Programa que cuenta las vocales
'''
text = 'Hola soy Eder'
unique = { c.upper() : c.count(c)  for c in text if c in 'aeiou'}
print(unique)
'''

#Map con diccionarios

items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pantalones',
        'price': 300
    },
    {
        'product': 'pantalones 2',
        'price': 200
    }
]

prices = list(map(lambda item: item['price'], items ))
print(prices)

def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .19
    return item

new_items = list(map(add_taxes, items))
print('new list')
print(new_items)
print('old list')
print(items)








