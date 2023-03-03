import random
v = random.sample(range(100), 10)
maior = 0
menor = 100

for x in v[0:]:
    if x > maior:
        maior = x
    elif x < menor:
        menor = x
print(f'Lista: {v}\nMaior: {maior}\nMenor: {menor}')
