a = int(input('a: '))
b = int(input('b: '))

while a % b != 0:
    a, b = b, a % b
    print(a, b)
print(f'O menor divisor comum é {b}.')
