#En este archivo aprendi sobre factoriales

"""
#Esto multiplica cada numero por uno mas pequeño para llegar al factorial
def factorial(n):
    '''Calcula el factorial de n.

    n int > 0
    return n!
    '''
    print(n)
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

n = int(input('Escribe un número: '))

print(factorial(n))
"""

def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)








