a = int(input('Lado a: '))
b = int(input('Lado b: '))
c = int(input('Lado c: '))

if a > (b + c) or b > (a + c) or c > (a + b):
    print('Os valores não correspondem à um triângulo.')
    print('Um dos lados é maior que a soma dos outros dois lados.')
elif a == b == c:
    print('Triângulo equilátero.')
elif a == b or a == c or b == c:
    print('Triângulo isósceles.')
else:
    print('Triângulo escaleno.')
    
