if True:
    print('Deberia ejecutarse')

if False:
    print('Nunca se ejecuta')


pet = input ('¿Cual es tu mascota favorita?')

if pet == 'perro':
    print('Genial tienes buen gusto')
elif pet == 'gato':
    print('Espero tengas suerte')
elif pet == 'pez':
    print('Que bien')
else:
    print('No tienes ninguna mascota interessante')



stock = int(input('Digita el stock => '))

if stock >= 100 and stock <= 1000:
    print('El stock es correcto')
else:
    print('El stock es incorrecto')