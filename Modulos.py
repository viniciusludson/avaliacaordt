'''#está trazendo o tipo e o ano mes dia hora minutos segundos
import datetime
print(type(datetime))
data=datetime.datetime(2022,5,15,10,4,5)
print(data)

#usando alias ou apelidos
#continua trazendo ano mes dia hora minuto segundo usando uma alias ou aplelido
import datetime as tempo
data= tempo.datetime(2022, 5,15,10,4,5)
print(data)

#random
#esta importando uma biblioteca random que esta retornando um numero aleatorio entre 10 e 199
import random
print(random.randrange(10,199))

from random import randrange as num_aleatorio
print(num_aleatorio(10,100))

#traz um numero aleatorio
from random import*
print(randrange(10,100))
'''
import random
dir(random)
import random
dir(random.randrange)

import random
print(random.+name_ )

