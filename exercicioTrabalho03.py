def metragemLimpeza():
    print('----------------- Menu 1 de 3 - Metragem Limpeza ------------------')
    while True:
        try:
            metragemCasa = int(input('Entre com a metragem da casa: '))
            if metragemCasa >= 30 and metragemCasa < 300:
                print('É necessário contratar 1 pessoa')
                return 60 + 0.3 * metragemCasa
            elif metragemCasa >= 300 and metragemCasa < 700:
                print('É necessário contratar 2 pessoas')
                return 12 + 0.5 * metragemCasa
            else:
                print('!! Não aceitamos casas com metragem menor que 30m² ou maior que 700m²')
                continue
        except ValueError:
            print('Valor inválido, apenas valores númericos inteiros são aceitos.')
            continue

def tipoLimpeza():
    print('------------------ Menu 2 de 3 - Tipo de Limpeza ------------------')
    while True:
        limpezaEscolhida = input('Entre com o tipo de limpeza: \n' + 
                                'B - Básica - Indicada para sujeiras semanais ou quizenais \n' + 
                                'C - Completa - (30% a mais) - Indicada para sujeiras antigas e/ou não rotineiras. \n' +
                                '>>').upper()
        if limpezaEscolhida == 'B':
            return 1.00
        elif limpezaEscolhida == 'C':
            return 1.30
        else:
            print('!!!!!!! Opção inválida !!!!!!!')
            continue

def adicionalLimpeza():
    print('--------------- Menu 2 de 3 - Adicional de Limpeza ----------------')
    acumulador = 0
    while True:
        adicional = input('Deseja mais algum adicional? \n' +
                '0 - Não desejo mais nada (encerrar) \n' +
                '1 - Passar 10 peças de roupas - R$ 10,00 \n' +
                '2 - Limpeza de 1 Forno/Micro-ondas - R$ 12,00 \n' +
                '3 - Limpeza de 1 Geladeira/Freezer - R$ 20,00 \n' +
                '>>')
        if adicional == '0':
            return acumulador
        elif adicional == '1':
            acumulador += 10
            continue
        elif adicional == '2':
            acumulador += 12
            continue
        elif adicional == '3':
            acumulador += 20
            continue
        else:
            print('!!!!!!! Opção inválida !!!!!!!')
            continue

        
print('Bem vindo ao Programa de Serviços de Limpeza do Bruno da Rosa Vigel')
print('*******************************************************************')
valorMetragem = metragemLimpeza()
tipo = tipoLimpeza()
totalAdicional = adicionalLimpeza()
valorTotal = valorMetragem * tipo + totalAdicional

print('TOTAL: R$ {:.2f} (metragem: {:.2f} * tipo: {:.2f} + adicional: {:.2f}'.format(valorTotal, valorMetragem, tipo, totalAdicional))


