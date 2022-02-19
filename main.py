# Comentar  el  python

''' 
comentario de bloque

'''

# ----------Variables--------------


from operator import truediv


#x = 5
y = "John"
# print(x)
# print(y)

# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0

nombre = 'Carlos'
# salida en consola
print(nombre)

# Concatenar
print('Su nombre es : ', nombre, 'coma')
print('Su nombre es : ' + nombre + 'mas')

print(f'Su nombre es {nombre}')

# variables datos primintivos
edadUsuario = 43
estatura = 1.84
variableBoolean = True

print(f'Su nombre es : {nombre} su edad es {edadUsuario} tiene una estatura de {estatura} mts y es incha del mejor {variableBoolean}?')

# entrada de datos por consola
#nomero1 = int(input('Ingrese el numero :'))
#nomero2 = int(input('Ingrese el numero :'))

#suma = numero1  + numero2
#print(f'la suma es  {numero1} + {numero2} = {suma}')

# condicionales logicas (IF) OJO CON LA TABULACION

d = 2
if(d > 4):
    print('es mayor Positivo')
else:
    print('fallo')
    print('ok')
print('ok fuera del if')
