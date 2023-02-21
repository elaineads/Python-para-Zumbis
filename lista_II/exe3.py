peso = float(input('Digite o peso: '))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    multa = excesso = 0

print(f'Excesso: {excesso:.2f}kg')
print(f'Multa: R$ {multa:.2f}')
