jugador_1 = input('hola jugador1, selecciona piedra, papel o tijera: ')
jugador_2 = input('hola jugador2, selecciona piedra, papel o tijera: ')

if jugador_1 == jugador_2:
    print('Empate')
elif (jugador_1 == 'piedra' and jugador_2 == 'tijeras') or (jugador_1 == 'tijeras' and jugador_2 == 'papel') or (jugador_1 == 'papel' and jugador_2 == 'piedra'):
    print('Gana el jugador1')
else:
    print('Gana el jugador2')


