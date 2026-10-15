"""
Calculadora simples em Python (linha de comando).

Operações disponíveis:
    +   soma
    -   subtração
    *   multiplicação
    /   divisão
    **  potência
    %   resto da divisão
    r   raiz quadrada

Como usar:
    python calculadora.py
"""

import math


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b


def potencia(a, b):
    return a ** b


def resto(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível calcular o resto da divisão por zero.")
    return a % b


def raiz_quadrada(a):
    if a < 0:
        raise ValueError("Não existe raiz quadrada real de número negativo.")
    return math.sqrt(a)


OPERACOES = {
    "+": ("Soma", somar),
    "-": ("Subtração", subtrair),
    "*": ("Multiplicação", multiplicar),
    "/": ("Divisão", dividir),
    "**": ("Potência", potencia),
    "%": ("Resto da divisão", resto),
}


def ler_numero(mensagem):
    """Pede um número ao usuário até que ele digite um valor válido."""
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("Valor inválido. Digite um número (ex.: 10 ou 3.5).")


def formatar(resultado):
    """Mostra números inteiros sem casas decimais (ex.: 4.0 -> 4)."""
    if isinstance(resultado, float) and resultado.is_integer():
        return str(int(resultado))
    return str(round(resultado, 10))


def mostrar_menu():
    print("\n===== CALCULADORA =====")
    for simbolo, (nome, _) in OPERACOES.items():
        print(f"  {simbolo:<3} {nome}")
    print("  r   Raiz quadrada")
    print("  s   Sair")
    print("=======================")


def main():
    print("Bem-vindo à Calculadora em Python!")

    while True:
        mostrar_menu()
        opcao = input("Escolha a operação: ").strip().lower()

        if opcao == "s":
            print("Até logo!")
            break

        try:
            if opcao == "r":
                a = ler_numero("Digite o número: ")
                resultado = raiz_quadrada(a)
                print(f"\nResultado: √{formatar(a)} = {formatar(resultado)}")

            elif opcao in OPERACOES:
                nome, funcao = OPERACOES[opcao]
                a = ler_numero("Digite o primeiro número: ")
                b = ler_numero("Digite o segundo número: ")
                resultado = funcao(a, b)
                print(f"\nResultado: {formatar(a)} {opcao} {formatar(b)} = {formatar(resultado)}")

            else:
                print("Opção inválida. Tente novamente.")

        except (ZeroDivisionError, ValueError) as erro:
            print(f"\nErro: {erro}")


if __name__ == "__main__":
    main()
