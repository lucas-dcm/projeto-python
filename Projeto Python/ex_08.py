'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.'''

ph = input('Quanto você ganha por hora? ') 
ht = input('Quantas horas você trabalha por mês? ')

salario = float(ph) * float(ht)

print ('O seu salário é de R$',salario, 'reais por mês')