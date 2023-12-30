#Aqui aprendi a usar ciclos en python

#while: mientras // cuando usas este comando se va a repetir indefinidamente a menos que tu declares el numero de repeticiones
'''
while True:
    print('se ejecuta')
'''
'''
counter = 0

#Si el contador es menor a 10 se ejecutara el programa
while counter < 10:
    counter += 1
    print(counter)
'''

'''
counter = 0

while counter < 20:
    counter += 1
    if counter == 15:
        break
    print(counter)
'''

counter = 0

while counter < 20:
    counter += 1
    if counter < 15:
        continue
    print(counter)

#Break rompe la cadena y continue pone el sobrante de la cadena

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


