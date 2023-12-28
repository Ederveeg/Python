#Archivo sobre el uso distinto de funciones

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

