import random
v1 = random.sample(range(100), 10)
v2 = random.sample(range(100), 10)
v3 = []

for x in range(10):
    v3.append(v1[x])
    v3.append(v2[x])
print(f'v1: {v1}\nv2: {v2}\nv3: {v3}')
