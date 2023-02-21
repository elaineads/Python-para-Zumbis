salario = float(input('Digite o valor do salário: '))
porcentagem = float(input('Digite a porcentagem de aumento: '))

aumento = salario * porcentagem / 100
novoSalario = salario + aumento

print(f'O aumento foi de R$ {aumento:.2f} e o novo salário é de R$ {novoSalario:.2f}.')
