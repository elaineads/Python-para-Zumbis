cigarrosDia = int(input('Quantos cigarros você fuma por dia? '))
anos = int(input('Por quantos anos você fuma? '))

cigarrosTotal = anos * 365 * cigarrosDia
minutos = cigarrosTotal * 10
dias = minutos / 1440

print(f'Você perdeu {dias:.1f} dias da sua vida! Pare de fumar!')
