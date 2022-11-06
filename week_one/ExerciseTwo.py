# Escribir un programa que lea un entero positivo n, introduciendo por el usuario y despues
# muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros
# enteros positivos puede ser calculada de la siguiente forma
#
#              n(n+1)
#  suma = ________________ 
#                2   
print('SUMANDO ENTEROS POSITIVOS HSATA N')
# la variable number representa a n en la formula
number = int(input('Introdusca un numero entero positivo: '))
total = int((number*(number+1))/2)
print(f'Sumatoria: {total}')