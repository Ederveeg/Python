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



