import random

contador = 0
num = random.randint(0,101)
cant_intentos = 0
cantidad_max = 5
correcto = False

while not correcto:
    if not cant_intentos < cantidad_max:
        print('Game over')
        break

    entrada = int(input('Escribe un numero del 0 al 100: '))
    
    if entrada == num:
        print('acertaste')
    elif entrada < num:
        print('el numero es mas grande')
    else:
        print('el numero es mas chico')
    
    cant_intentos += 1