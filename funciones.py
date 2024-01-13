#Archivo sobre funciones

#Aqui aprendi el comportamiento de las funciones
'''
def my_print(text):
    print(text * 2)

my_print('Este es mi texto')
'''
#Aqui hice una funcion con matematica
'''
def suma(a,b,):
    print(a + b)

suma(1 ,5)
suma(10, 2)
'''
#Funciones retun
'''
def sum_with_range(a, b):
    print(a, b)
    sum = 0
    for x in range(a,b):
        sum += x
    return sum

result = sum_with_range(1, 10)
print(result)
#Aqui  le damos el parametro 45 o sea result y luego suma 45 + 10
result_2 = sum_with_range(result, result + 10)
print(result_2)
'''
#parametros por defecto y múltiples returns

#Este programa encuentra el volumen de algun objeto o cuerpo
'''
def find_volume(length=1, width=1, depth=1):
    return length * width * depth, width, 'Hola'
#Podemos hacer que solo tome un valor espicifacndo el argumento y asignando un valor
result = find_volume(width=10)

print(result)
'''
#El scope es el alcance de una variable 
'''
price = 100 # global

def increment():
    price = 200
    result = price + 10
    print(result)
    return result

print(price)
price_2 = increment()
print(price_2)
'''

#Argumentos de otras funciones
'''
def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
        return resultados

nums = [1, 2, 3]
aplicar_operacion(multiplicar_por_dos, nums)
[2, 4, 6]

aplicar_operacion(sumar_dos, nums)
[3, 4, 5]
'''

#Funciones en expresiones

'''
Una forma de definir una función en una expresión es utilizando el keyword lambda. lambda tiene la siguiente sintaxis: lambda : .

Otro ejemplo interesante es que las funciones se pueden utilizar en una expresión directamente. Esto es posible ya que como lo hemos platicado con anterioridad, en Python las variables son simplemente nombres que apuntan a un objeto (en este caso a una función). Por ejemplo:

sumar = lambda x, y: x + y

sumar(2, 3)
5
'''

#Funciones en estructuras de datos
'''
def aplicar_operaciones(num):
    operaciones = [abs, float]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))

    return resultado

 aplicar_operaciones(-2)
[2, -2.0]
'''

#Lambdas
'''
#Esta funcion es sin lambda
def increment(x):
    return x + 1

result = increment(10)
print(11)

#Esta es con lambda

increment_v2 = lambda x : x + 1

result = increment_v2(20)
print(result)

#Otra lambda

full_name = lambda name, last_name: f'Full name es {name.title()} {last_name.title()}'
text = full_name('eder', 'Vega')
print(text)
'''

#HOF: Higher order function
'''
def increment(x):
    return x + 1

increment_v2 = lambda x: x + 1

def hof(x, func):
    return x + func(x)

hof_v2 = lambda x, func: x + func(x)

result = hof(2, increment)
#Al final se ejecta 2 + (2 + 1)
print(result)

result = hof_v2(2, increment_v2)
print(result)
result = hof_v2(2, lambda x: x * 2)
'''

#Map/transformacion de elementos y es de los elementos mas usados
'''
numbers = [1,2,3,4]
numbers_v2 = []
for i in numbers:
    numbers_v2.append(i * 2)

#Aqui usamos map
numbers_v3 = list(map(lambda i: i * 2, numbers))

print(numbers)
print(numbers_v2)
print(numbers_v3)

numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

print(numbers_1)
print(numbers_2)
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)
'''





























