# Escribir un programa que pregunte al usuario por el numero de horas trabajadas y el coste por hora.
# Despues debe mostrar por pantalla la paga correspondiente
# 
print('Calculando salario')
hoursWorked = float(input('Ingrese las horas trabajadas: '))
hourlyLaborCost = float(input('Ingrese el precio por hora trabajada: '))
currentSalary = hoursWorked * hourlyLaborCost

print(f'Su salario total es: ${currentSalary}')


