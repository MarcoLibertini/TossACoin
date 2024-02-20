import random
from random import *

lista = [n*2 for n in range(4,21)]
def lanzarMoneda():
    monedas = ['Cara', 'Cruz']
    return choice(monedas)

def probarSuerte(lanzarMoneda, lista):
    if lanzarMoneda == 'Cara':
        lista.clear()
        mensaje = 'La lista se ELIMINARA'
        return f'{mensaje}: La lista contiene {lista}'
    else:
        mensaje = 'La lista se SALVARA'
        return f'{mensaje}: La lista contiene {lista}'


print(probarSuerte(lanzarMoneda(),lista))


