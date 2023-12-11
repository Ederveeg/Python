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
