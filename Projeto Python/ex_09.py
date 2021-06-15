'''Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura 
em graus Celsius. C = (5 * (F-32) / 9)'''


f = input('Digite o valor de Farenheit: ')
vT = int(f) - 32                                #vT de variável temporária
c = 5 * float(vT) / 9

print ('Conversão de Farenheit para Celsius é',c,'°C')