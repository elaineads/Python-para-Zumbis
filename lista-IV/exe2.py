import random
lista = random.sample(range(100), 20)
par = []
impar = []

for x in lista[0:]:
    if x % 2 == 0:
        par.append(x)
    elif x % 2 == 1:
        impar.append(x)
print(f'Lista: {lista}\nPar: {par}\nÍmpar: {impar}')
