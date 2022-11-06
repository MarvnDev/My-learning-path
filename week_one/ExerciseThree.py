# escribir un programa que pida al usuario su peso en KG y estatura en metros, calcule el indice de masa corporal
# y lo almacena en una variable, y muestre en pantalla la frase 'Tu indice de masa corporal es: <imc>'
# donde <imc> es el indice de masa corporal calculado redondeado con dos decimales

weight = float(input('Ingrese su peso en kg: ')) 
height = float(input('Ingrese su altura en metros: '))

# el peso de una persona en kilogramos dividido por el cuadrado de la estatura en metros
imc = float(weight/pow(height,2))

print(f'Tu indice de masa corporal es: {imc}')