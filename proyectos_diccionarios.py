#En este archivo van los proyectos de diccionarios

#Ejercicio 1: Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
'''
divisas = {
    'euro':'€',
    'dollar':'$',
    'yen':'¥'
}

user = input('Introduce una divisa: ')
if user.lower() == 'euro':
    print(divisas['euro'])
else:
    if user == 'dollar':
        print(divisas['dollar']) 
    else:
        if user == 'yen':
            print(divisas['yen'])    
        else:
            print('La divisa no se encuentra en el diccionario')

#Otra solucion:

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
print(monedas.get(moneda.title(), "La divisa no está."))
'''

#Ejercicio 2: Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
'''
user = input('¿Cual es tu nombre?')
user2 = input('¿Cual es tu edad?')
user3 = input('¿Cual es tu dirección?')
user4 = input('¿Cual es tu teléfono?')

usuario_dicc = {
    'nombre':user,
    'edad':user2,
    'dirección':user3,
    'telefono':user4,
}

print(usuario_dicc.get('nombre'), 'tiene', usuario_dicc.get('edad'), 'años, vive en', usuario_dicc.get('dirección'), 'y su número de telefono es', usuario_dicc.get('telefono'))
'''

#Ejercicio 3:Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello
'''
user = input('Que fruta quieres? (platano, manzana, pera o naranja) ').lower()
kg = float(input('¿Cuantos kg necesitas? '))

fruta = {
    'platano':1.35,
    'manzana':0.80,
    'pera':0.85,
    'naranja':0.70
}

if user in fruta:
    print('El precio de',kg,'kg','de',user,'es de',fruta.get(user)* kg,'Dólares')
else:
    print('Esta fruta no esta disponible')
'''

#Ejercicio 4:Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
'''
user = input('Introduce tu fecha de nacimiento en el siguiente formato (dd/mm/aaaa) ')
mm = user[3:5]
meses = {'01':'Enero',
         '02':'Febrero',
         '03':'Marzo',
         '04':'Abril',
         '05':'Mayo',
         '06':'Junio',
         '07':'Julio',
         '08':'Agosto',
         '09':'Septiembre',
         '10':'Octubre',
         '11':'Noviembre',
         '12':'Diciembre'
}

print(user[0:2],'de',meses.get(mm),'de',user[6:])
'''

#Ejercicio 5:Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
'''
creditos = {
    'Matemáticas': 6,
    'Física': 4,
    'Química': 5,
    'Español':6,
}

print('El número total de créditos del curso es:',sum(creditos.values()))
for i in creditos:
    print(i,'tiene',creditos[i],'creditos')

#Otra solución:
curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5, 'Español':6,}
total_creditos = 0
for asignatura, creditos in curso.items():
    print(asignatura, 'tiene', creditos, 'créditos')
    total_creditos += creditos
print('Número total de créditos del curso: ', total_creditos)
'''

#Ejercicio 6:Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
'''
user = {}
continuar = True
while continuar:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    user[clave] = valor
    print(user)
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"
'''
#Ejercicio 7:Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
'''
user = {}
continuar = True
while continuar:
    clave = input('¿Qué articulo quieres introducir? ')
    valor = int(input(clave + ': $'))
    user[clave] = valor
    print(user)
    continuar = input('¿Quieres añadir más información (y/n)? ') == "y"
else:
    for i in user:
        print(i,user[i])

print('El coste total es de $',sum(user.values()))
rojo:red, azul:blue, amarillo:yellow
'''

#Ejercicio 8:Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
'''
diccionario = {}
palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in palabras.split(','):
    clave, valor = i.split(':')
    diccionario[clave] = valor
frase = input('Introduce una frase en español: ')
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')
'''

#Ejercicio 9:Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
'''
facturas = {
    '#0123':546,
    '#2133':231,
}
continuar = True
while continuar:
    user = int(input('Si quieres añadir una factura presiona (1), si quieres pagar una existente presiona (2), si quieres terminar presiona (3): '))
    if user == 1:
        fac = input('¿Cual es el número de tu factura (#1234)? ')
        costo = int(input('¿Cuanto se cobra en la factura? '))
        facturas[fac] = costo
        print(facturas)
        print('Queda por pagar $ ', sum(facturas.values()), ' MXN')
    else:
        if user == 2:
            print(facturas)
            busc = input('De las facturas que aparecen en pantalla cual desea pagar(#1234)? ')
            print('El monto a pagar es de $ ' + str(facturas.get(busc)) + ' MXN')
            print('¡El pago se ha realizado con éxito!')
            print('Se ha pagado $', str(facturas.get(busc)), ' MXN')
            print('Queda por pagar $', sum(facturas.values()), 'MXN')
            facturas.pop(busc)
        else:
            if  user == 3:
                continuar = input('¿Quieres seguir usando el programa(y/n)? ') == "y"
'''
            
#Ejercicio 10: Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar.
'''
base_datos = {
    'NF2314':{'nombre':'Alvaro Ortiz', 'direccion':'Avasolo #23', 'tel':'443-234-2122', 'correo':'Alvaro1@gmail.com', 'preferente':True,},
    'NF1234':{'nombre':'Alin Sanchez', 'direccion':'Martinez #344', 'tel':'876-345-9021', 'correo':'Gato23@gmail.com', 'preferente':False,}
}
continuar = True
while continuar:
    user = int(input('¿Que deseas hacer? (1)Añadir cliente, (2)Eliminar cliente, (3)Mostrar cliente, (4)Listar todos los clientes, (5)Listar clientes preferentes, (6)Terminar: '))
    if user == 1:
        Nif = input('Introduce el NIF del cliente: ')
        nombre = input('Introduce el nombre del cliente: ')
        direccion = input('Introduce la dirección del cliente: ')
        tel = input('Escribe el teléfono del cliente: ')
        correo = input('Introduce el correo del cliente: ')
        vip = input('¿El cliente es preferente? (S/N)')
        cliente = {'nombre':nombre, 'direccion':direccion, 'tel':tel, 'correo':correo, 'preferente':vip=='S'}
        base_datos[Nif] = cliente
        print('¡El cliente se añadio con éxito!')
    if user == 2:
        Nif = input('Introduce el NIF del cliente que quieres borrar: ')
        if Nif in base_datos:
            base_datos.pop(Nif)
            print('¡El cliente se ha eliminado de la base de datos correctamente!')
        else:
            print('Verifica que el NIF este correcto y vuelve a introducirlo')
    if user == 3:
        Nif = input('Introduce el NIF del cliente que deseas ver: ')
        print(base_datos.get(Nif))
    if user == 4:
        print('Lista de clientes')
        for clave, valor in base_datos.items():
            print(clave,valor['nombre'])
    if user == 5:
        print('Lista de clientes preferentes')
        for clave, valor in base_datos.items():
            if valor['preferente']:
                print(clave, valor['nombre'])
    if user == 6:
        continuar = input('¿Seguro que quieres cerrar el programa? (S/N)') == 'N'
'''


x = 0.0
for i in range(10):
    x += 0.1

if x == 1.0:
    print(f'x = {x}')
else:
    print(f'x != {x}')



 














