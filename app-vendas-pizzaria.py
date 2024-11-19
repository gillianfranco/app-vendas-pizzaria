# Mostra o menu com o cardápio
def mostrar_menu():
    print('=' * 34 + ' Cardápio ' + '=' * 35)
    print('-' * 79)
    print('=' * 11 + ' |  Tamanho  |  Pizza Salgada(PS)  |  Pizza Doce(PD)  | ' + '=' * 12)
    print('=' * 11 + ' |     P     |       R$30.00       |      R$34.00     | ' + '=' * 12)
    print('=' * 11 + ' |     M     |       R$45.00       |      R$48.00     | ' + '=' * 12)
    print('=' * 11 + ' |     G     |       R$60.00       |      R$66.00     | ' + '=' * 12)
    print('-' * 79)

# Verifica se o sabor escolhido pelo usuário é válido
def valida_sabor(mensagem):
    while True:
        sabor = input(mensagem)
        if sabor.lower() != 'ps' and sabor.lower() != 'pd':
            print('Sabor inválido! Tente novamente.\n')
            continue
        break
    return sabor

# Verifica se o tamanho da pizza escolhido pelo usuário é válido
def valida_tamanho(mensagem):
    while True:
        tamanho = input(mensagem)
        if tamanho.lower() != 'p' and tamanho.lower() != 'm' and tamanho.lower() != 'g':
            print('Tamanho inválido! Tente novamente.\n')
            continue
        break
    return tamanho

# Calcula o valor total que deve ser pago conforme as pizzas escolhidas pelo usuário
def calcula_valor_total(sabor, tamanho):
    if sabor.lower() == 'ps':
        if tamanho.lower() == 'p':
            total = 30
        elif tamanho.lower() == 'm':
            total = 45
        else:
            total = 60
    elif sabor.lower() == 'pd':
        if tamanho.lower() == 'p':
            total = 34
        elif tamanho.lower() == 'm':
            total = 48
        else:
            total = 66
    return total

# Verifica se a opção que o usuário digitou é válida
def valida_saida(mensagem):
    while True:
        opcao = input(mensagem)
        if opcao.lower() != 's' and opcao.lower() != 'n':
            print('Escolha Inválida! Tente novamente.')
            continue
        break
    return opcao

# Programa Principal

mostrar_menu()

valor_total = 0

while True:
    # Solicita que o usuário escolha o sabor da pizza
    sabor_pizza = valida_sabor('Digite o sabor da pizza [PS/PD]: ')

    # Solicita que o usuário escolha o tamanho da pizza
    tamanho_pizza = valida_tamanho('Digite o tamanho da pizza [P/M/G]: ')

    # Soma com o valor atual da variável o preço da pizza escolhida
    valor_total += calcula_valor_total(sabor_pizza, tamanho_pizza)

    # Verifica se o usuário deseja sair ou continuar utilizando o sistema
    continuar = valida_saida('\nDeseja mais alguma coisa? [S/N]: ')
    if continuar.lower() == 'n':
        print('\nFinalizando pedido...')
        break

    print()

print(f'Valor total a ser pago: R${valor_total:.2f}')