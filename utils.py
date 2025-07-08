import sys

def log_error(mensagem: str, codigo: int): # Função para relatar erro no terminal. E sair do programa.
    print(f"ERRO {codigo}: {mensagem}")
    sys.exit(codigo)

def formatar_numero(numero: float): # Formatar o número corretamente quando o decimal for zero ou outro número decimal
    if numero == int(numero):
        numero = int(numero)
    else:
        numero = round(numero, 5)
    return numero

def obter_numeros(): # Tentar obter os números com o usuário.
    try: # Tentar definir os valores pedindo para o usuário.
        numero1 = float(input("Insira o primeiro valor: "))
        numero2 = float(input("Insira o segundo valor: "))

    except ValueError: # Se digiar um valor que não é um número, relatar o erro.
        log_error("Valor inválido! Insira somente números.",1)
    else:
        return numero1, numero2 