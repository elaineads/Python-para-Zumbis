a = 80000
b = 200000

anos = 0
while a < b:
    a = a + (a * 0.03)
    b = b + (b * 0.015)
    anos = anos + 1
    
print(f'País A: {a:.0f}')
print(f'País B: {b:.0f}')
print(f'Foram necessários {anos} anos para que a população do país A ultrapassasse a de B.')
