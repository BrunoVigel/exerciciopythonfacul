print('Bem-Vindo a Sorveteria do Bruno da Rosa Vigel')
print('-------------------------------------------Cardápio--------------------------------------------')
print('| Código | Descrição            | Tamanho P (500ml) | Tamanho M (1000ml) | Tamanho G (1000ml) |')
print('|   TR   | Sabores Tradicionais |      R$ 6,00      |      R$ 10,00      |      R$ 18,00      |')
print('|   ES   | Sabores Especiais    |      R$ 7,00      |      R$ 12,00      |      R$ 21,00      |')
print('|   PR   | Sabores Premium      |      R$ 8,00      |      R$ 14,00      |      R$ 24,00      |')
print('-----------------------------------------------------------------------------------------------')

acumulador = 0
# trocar no valor final o ponto por vírgula no preço

while True:
    tamanho = input('Entre com o TAMANHO do pote desejado (P/M/G): ').upper()
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('!!!!!!! TAMANHO ou CÓDIGO inválido(s) !!!!!!!')
        continue # Se o usuário digitar algo inválido volta para o começo do while.
    codigo = input('Entre com o CÓDIGO do sabor desejado (TR/ES/PR): ').upper()
    if codigo != 'TR' and codigo != 'ES' and codigo != 'PR':
        print('!!!!!!! TAMANHO ou CÓDIGO inválido(s) !!!!!!!')
        continue
    
    if codigo == 'TR' and tamanho == 'P': # verifica o código e o tamanho do pedido para retornar o valor
        print('Você pediu um sorvete sabor TRADICIONAL P de R$ 6,00')
        acumulador += 6 # Pega o valor do produto e soma com o acumulador

    elif codigo == 'TR' and tamanho == 'M':
        print('Você pediu um sorvete sabor TRADICIONAL M de R$ 10,00')
        acumulador += 10

    elif codigo == 'TR' and tamanho == 'G':
        print('Você pediu um sorvete sabor TRADICIONAL G de R$ 18,00')
        acumulador += 18 

    elif codigo == 'ES' and tamanho == 'P':
        print('Você pediu um sorvete sabor ESPECIAL P de R$ 7,00')
        acumulador += 7 

    elif codigo == 'ES' and tamanho == 'M':
        print('Você pediu um sorvete sabor ESPECIAL M de R$ 12,00')
        acumulador += 12 

    elif codigo == 'ES' and tamanho == 'G':
        print('Você pediu um sorvete sabor ESPECIAL G de R$ 21,00')
        acumulador += 21 

    elif codigo == 'PR' and tamanho == 'P':
        print('Você pediu um sorvete sabor PREMIUM P de R$ 8,00')
        acumulador += 8 

    elif codigo == 'PR' and tamanho == 'M':
        print('Você pediu um sorvete sabor PREMIUM M de R$ 14,00')
        acumulador += 14 

    elif codigo == 'PR' and tamanho == 'G':
        print('Você pediu um sorvete sabor PREMIUM G de R$ 24,00')
        acumulador += 24
    
    maisPedidos = input('Deseja pedir mais alguma coisa? (S/N): ').upper() 
    if maisPedidos == 'S': # Se o usuário continuar a operação retorna ao início do laço
        continue
    elif maisPedidos == 'N': # Termina o laço e retorna o valor final
        print('O total a ser pago é: R${:.2f}'.format(acumulador))
        break
