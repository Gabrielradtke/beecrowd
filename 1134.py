gasol = 0
alcool = 0
diesel = 0

while True:
    n = int(input())
    
    if n == 1:
        alcool += 1
    elif n == 2:
        gasol += 1
    elif n == 3:
        diesel += 1
    elif n == 4:
        break
    
    
print(f'MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasol}')
print(f'Diesel: {diesel}')