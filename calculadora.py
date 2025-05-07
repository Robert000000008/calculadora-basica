def calcular(num1, num2, operacao):
    if operacao == '1':
        return num1 + num2
    elif operacao == '2':
        return num1 - num2
    elif operacao == '3':
        return num1 * num2
    elif operacao == '4':
        if num2 != 0:
            return num1 / num2
        else:
            return " Erro: não é possivel dividir por zero!"
    else:
        return "Opçao inválida!"


while True:
    num1 = float(input('Digite o primeiro número:'))
    num2 = float(input('Digite o segundo número:'))
    print('escolha a operação:')
    print('1. Soma(+)')
    print('2. Subtração(-)')
    print('3. Multiplicaçao(*)')
    print('4. Divisão (/)')
    operacao = input('Digite a opção (1/2/3/4:')

    resultado = calcular(num1, num2, operacao)
    print('Resultado:', resultado)

    continuar = input('Deseja realizar outra operação? (sim/não):').lower()
    if continuar != 'sim':
        break
