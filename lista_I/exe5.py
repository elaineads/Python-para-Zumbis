preco = float(input('Digite o preço da mercadoria: '))
percentual = float(input('Digite o percentual de desconto: '))

desconto = preco * percentual / 100
novoPreco = preco - desconto

print(f'O desconto será de R$ {desconto:.2f} e o novo preço será de R$ {novoPreco:.2f}.')
