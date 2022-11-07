import math
import os
import random
import re
import sys


#number = 18
number = random.randint(1,100)
# n & 2 = 1, impar si no si es 0 donc es par

print(f'my random number is {number}')
if(number % 2==1):
    print('weird')
elif((number)% 2 == 0 and (number >=2 and number <=5)):
    print('Not weird')
elif((number)% 2 == 0 and (number >= 6 and number <= 20)):
    print('weird')
else:
    print('Weird')

    


