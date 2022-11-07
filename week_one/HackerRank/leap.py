# El año puede ser dividido uniformemente por 4, es un año bisiesto, a menos que:
# El año puede ser dividido uniformemente por 100, NO es un año bisiesto, a menos que:
# El año también es divisible uniformemente por 400. Entonces es un año bisiesto

def is_leap(year):
    leap = False
    # Write your logic here
    if year % 4 != 0:
        return leap
    elif year % 4 == 0 and year % 100 != 0:
        leap = True
        return leap
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        return leap
    elif year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
        leap = True
        return leap
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        leap = True
        return leap


year = 1990
print(is_leap(year))