valorHora = float(input('Quanto você ganha por hora? '))
horasTrabalhadas = float(input('Quantas horas você trabalhou no mês? '))

salarioBruto = horasTrabalhadas * valorHora
IR = salarioBruto * 0.11
INSS = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - (IR + INSS + sindicato)

print(f'+ Salário Bruto:\t R$ {salarioBruto:.2f}') #\t tab
print(f'- IR(11%):\t\t R$ {IR:.2f}')
print(f'- INSS(8%):\t\t R$ {INSS:.2f}')
print(f'- Sindicato(5%):\t R$ {sindicato:.2f}')
print(f'= Salário Líquido:\t R$ {salarioLiquido:.2f}')

      
