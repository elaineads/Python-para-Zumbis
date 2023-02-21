metros = int(input('Qual o tamanho em metros quadrados? '))

latas = metros // 54

if metros % 54 != 0:
    latas = latas + 1

print(f'A quantidade de latas de tinta necessária é {latas:.0f} e o preço total será de R$ {latas * 80:.2f}')
