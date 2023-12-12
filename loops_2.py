'''
for element in range(1, 21):
    print(element)
'''
my_list = [23, 45, 67, 89, 43]
for element in my_list:
    print(element)

my_tupla = ('Eder', 'July', 'Santi')
for element in my_tupla:
    print(element)

product = {
    'name': 'Camisa',
    'Precio': 100,
    'stock': 89
}

#Primera forma de que nos retorne(iteraciones) los valores junto con sus llaves
for key in product:
    print(key, ':', product[key])

#Segunda forma de que nos retorne(iteracion) los valores junto con sus llaves
for key, value in product.items():
    print(key, ':', value)

people = [
    {
        'name': 'Juan',
        'age': 45 
    },
    {
        'name': 'Abel',
        'age': 32 
    },
    {
        'name': 'azul',
        'age': 24
    },
]

for person in people:
    print('name:', person['name'])


