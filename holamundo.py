import random

x = random.randrange(1,100)
y = random.random()
#print(x)
#print(y)

#------------------
# STRINGS
#------------------
#SLICING
txt = 'seguimos trabajando con strings'
#print(txt[8:19])
txt2 = 'NO ESTOY GRITANDO'
#print(txt2.lower())
txt3 = 'estoy gritando'
mayus = txt3.upper()
#print(mayus)

espacios = '            me deje espacios          '
corregido = espacios.strip()

#print(corregido)

horas = 10
clases = 30
cont = 'el curso dura: {} horas y tendra {} clases'
#print(cont.format(horas, clases))

#con la barra \ podemos hacer escape de caracteres

texto = 'La serie \'GAME OF TRHONES\''
print(texto)