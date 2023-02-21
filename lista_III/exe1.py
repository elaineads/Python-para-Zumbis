print('Digite uma nota entre 0 e 10.')
nota = float(input('Nota: '))

while nota < 0 or nota > 10:
    print('Digite uma nota entre 0 e 10.')
    nota = float(input('Nota: '))
