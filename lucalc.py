from utils import *

def calcular(historico: list): # Função de calcular os valores.
    valor1, valor2 = obter_numeros()
    operacao = str.strip(input("Insira a operação (+,-,/,*,**): "))
    resultado = None # Deixar sem valor por enquanto.

    if operacao == "+": # Operação para mais.
        resultado = valor1 + valor2
    elif operacao == "-": # Operação para menos.
        resultado = valor1 - valor2
    elif operacao == "/": # Operação para dividir.
        if valor2 == 0: # Verifica se o segundo valor for zero, para não dividir e dar erro.
            log_error("Impossível dividir por zero.",2)
        resultado = valor1 / valor2
    elif operacao == "*": # Operação para multiplicar.
        resultado = valor1 * valor2
    elif operacao == "**": # Operação para potenciação.
        resultado = valor1 ** valor2
    else: # Se digitou outra operação, relatar o erro.
        log_error("Operação inválida! Digite somente os operadores válidos.",3)
    
    # Formatando os números.
    resultado = formatar_numero(resultado)
    valor1 = formatar_numero(valor1)
    valor2 = formatar_numero(valor2)

    calculo = f"{valor1} {operacao} {valor2} = {resultado}"

    historico.append(calculo)
    print(calculo)

historico_de_calculos = []
calcular(historico_de_calculos)

while True: # Nesse loop, perguntar para o usuário se quer calcular novamente.
            # Se sim, executar a função calcular() novamente.
            # Se não, Parar o loop e sair do programa.
    calcular_novamente = input("Quer calcular outro valor? (y/n): ")
    if calcular_novamente.lower() == "y":
        calcular(historico_de_calculos)
    else:
        # Aqui exibirá uma lista de cálculos que o usuário fez.
        if historico_de_calculos:
            print("Calculos que você fez:")
            for calculo in historico_de_calculos:
                print(calculo)
        
        # Encerrar o programa.
        print("Obrigado por usar o LuCalc!")
        break