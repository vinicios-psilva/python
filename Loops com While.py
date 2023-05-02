sal = int(input('Salario? '))
i = 27.
while i > 0:
    i = input('Imposto ou (s) para sair: ')
    if not i:
        i = 27.
    elif i == 's':
        break
    else:
        i = float(i)
    print("Valor real: {0}".format(sal - (sal * i * 0.01)))
        
