def metragemLimpeza():
    print('----------------- Menu 1 de 3 - Metragem Limpeza ------------------')
    while True:
        try:
            metragemCasa = int(input('Entre com a metragem da casa: ')) # Recebe o valor do tamanho da casa
            if metragemCasa >= 30 and metragemCasa < 300: # Verifica o tamanho recebido
                print('É necessário contratar 1 pessoa')
                return 60 + 0.3 * metragemCasa  # Retorna ********** TERMINAR
            elif metragemCasa >= 300 and metragemCasa < 700:
                print('É necessário contratar 2 pessoas')
                return 12 + 0.5 * metragemCasa
            else:
                print('!! Não aceitamos casas com metragem menor que 30m² ou maior que 700m²')
                continue # Caso o valor sejá inválido retorna ao início do laço
        except ValueError:
            print('Valor inválido, apenas valores númericos inteiros são aceitos.')
            continue # Caso o valor sejá inválido retorna ao início do laço

def tipoLimpeza():
    print('------------------ Menu 2 de 3 - Tipo de Limpeza ------------------')
    while True:
        limpezaEscolhida = input('Entre com o tipo de limpeza: \n' + 
                                'B - Básica - Indicada para sujeiras semanais ou quizenais \n' + 
                                'C - Completa - (30% a mais) - Indicada para sujeiras antigas e/ou não rotineiras. \n' +
                                '>>').upper() # Recebe o valor do tipo de limpeza e o deixa em caixa alta para deixar o tratamento de erros mais fácil
        if limpezaEscolhida == 'B': # Checa o tipo escolhido
            return 1.00 # Retorna o multiplicador
        elif limpezaEscolhida == 'C':
            return 1.30
        else:
            print('!!!!!!! Opção inválida !!!!!!!')
            continue # Caso o valor sejá inválido retorna ao início do laço

def adicionalLimpeza():
    print('--------------- Menu 2 de 3 - Adicional de Limpeza ----------------')
    acumulador = 0
    while True:
        adicional = input('Deseja mais algum adicional? \n' +
                '0 - Não desejo mais nada (encerrar) \n' +
                '1 - Passar 10 peças de roupas - R$ 10,00 \n' +
                '2 - Limpeza de 1 Forno/Micro-ondas - R$ 12,00 \n' +
                '3 - Limpeza de 1 Geladeira/Freezer - R$ 20,00 \n' +
                '>>') # Recebe o valor referente ao tipo de adicional
        if adicional == '0': # verifica o valor recebido
            return acumulador # retorna o valor do acumulador
        elif adicional == '1':
            acumulador += 10 # recebe o acumulador + 10
            continue # retorna ao início do laço
        elif adicional == '2':
            acumulador += 12
            continue
        elif adicional == '3':
            acumulador += 20
            continue
        else:
            print('!!!!!!! Opção inválida !!!!!!!')
            continue # Caso o valor sejá inválido retorna ao início do laço

        
print('Bem vindo ao Programa de Serviços de Limpeza do Bruno da Rosa Vigel')
print('*******************************************************************')
valorMetragem = metragemLimpeza()
tipo = tipoLimpeza()
totalAdicional = adicionalLimpeza()
valorTotal = valorMetragem * tipo + totalAdicional # calcula o valor total

print('TOTAL: R$ {:.2f} (metragem: {:.2f} * tipo: {:.2f} + adicional: {:.2f}'.format(valorTotal, valorMetragem, tipo, totalAdicional))


