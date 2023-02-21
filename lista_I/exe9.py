qtd_km = float(input('Digite a quantidade de km percorridos pelo carro: '))
qtd_dias = int(input('Digite a quantidade de dias pelos quais o carro foi alugado: '))

preco = (qtd_dias * 60) + (qtd_km * 0.15)

print(f'O preço a pagar será de R$ {preco:.2f}.')
