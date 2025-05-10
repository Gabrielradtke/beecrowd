valor = float(input())

if (valor > 0.00) and (valor < 2000.00):
    imposto = 'Isento'
elif (valor > 2000.01) and (valor < 3000.00):
    imposto = valor * 0.08 
elif (valor > 3000.01) and (valor < 4500.00):
    imposto = valor * 0.18
elif (valor > 4500.00):
    imposto = valor * 0.28
    
print(f'R$ {imposto}')
    
    
