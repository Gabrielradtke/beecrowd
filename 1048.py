sal = float(input())

while True:
    if (sal > 0) and (sal <= 400.00):
        novo_sal = (sal * 0.15) + sal
        reajuste = novo_sal - sal
        print(f'Novo salario: {novo_sal:.2f}')
        print(f'Reajuste ganho: {reajuste:.2f}')
        print(f'Em percentual: 15 %')
    elif (sal > 400.01) and (sal <= 800.00):
        novo_sal = (sal * 0.12) + sal
        reajuste = novo_sal - sal
        print(f'Novo salario: {novo_sal:.2f}')
        print(f'Reajuste ganho: {reajuste:.2f}')
        print(f'Em percentual: 12 %')
    elif (sal >= 800.01) and (sal <= 1200.00):
        novo_sal = (sal * 0.10) + sal
        reajuste = novo_sal - sal
        print(f'Novo salario: {novo_sal:.2f}')
        print(f'Reajuste ganho: {reajuste:.2f}')
        print(f'Em percentual: 10 %')
    elif (sal >= 1200.01) and (sal <= 2000.00):
        novo_sal = (sal * 0.07) + sal
        reajuste = novo_sal - sal
        print(f'Novo salario: {novo_sal:.2f}')
        print(f'Reajuste ganho: {reajuste:.2f}')
        print(f'Em percentual: 7 %')
    elif sal > 2000.00:
        novo_sal = (sal * 0.04) + sal
        reajuste = novo_sal - sal
        print(f'Novo salario: {novo_sal:.2f}')
        print(f'Reajuste ganho: {reajuste:.2f}')
        print(f'Em percentual: 4 %')
    break