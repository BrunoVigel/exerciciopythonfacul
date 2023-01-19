listaFuncionario = []
codigoFuncionario = 0

def cadastrarFuncionario(codigo):
    print('----------------------- MENU CADASTRAR FUNCIONÁRIO -----------------------')
    print('Código do funcionário {}'.format(codigo))
    nome = input('Por favor entre com o NOME: ')
    setor = input('Por favor entre com o SETOR: ')
    salario = int(input('Por favor entre com o SALÁRIO: '))
    dicionarioFuncionario = {'codigo': codigo,
                            'nome'   : nome,
                            'setor'  : setor,
                            'salario': salario} # Recebe todas informações do funcionário e coloca no dicionário
    listaFuncionario.append(dicionarioFuncionario.copy()) # Envia uma cópia do dicionário do funcionário para a lista de funcionários

def consultarFuncionario():
    print('----------------------- MENU CONSULTAR FUNCIONÁRIO -----------------------')
    while True:
        opcaoMenuConsultar = input('\nEscolha a opção desejada: \n' +
                            '1-Consultar Todos os Funcionários \n' +
                            '2-Consultar Funcionários por ID \n' +
                            '3-Consultar Funcionário por SETOR \n' +
                            '4-Retornar \n' +
                            '>>') # Recebe o valor da opção do menu

        if opcaoMenuConsultar == '1': # Verifica a opção do menu
            for funcionario in listaFuncionario: # Percorre todos os dicionários de funcionários da lista
                print('\n')
                for key, value in funcionario.items(): # Percorre todos as chaves e valores do dicionário do funcionário
                    print('{}: {}'.format(key, value)) # Faz um print de todas as chaves e valores dos dicionários dos funcionários
        elif opcaoMenuConsultar == '2':
            codigoSelecionado = input('Digite o ID do funcionário: ') # Recebe o ID do funcionário
            for funcionario in listaFuncionario:
                if funcionario['codigo'] == codigoSelecionado: # Se o ID do funcionário for igual ao ID passado
                    print('\n')
                    for key, value in funcionario.items():
                        print('{}: {}'.format(key, value)) # Faz um print de todas as chaves e valores do dicionário do funcionário
        elif opcaoMenuConsultar == '3':
            codigoSelecionado = input('Digite o setor do(s) funcionários: ') # Recebe o setor do funcionário
            for funcionario in listaFuncionario:
                if funcionario['setor'] == codigoSelecionado: # Se o setor do funcionário for igual ao setor passado
                    print('\n')
                    for key, value in funcionario.items():
                        print('{}: {}'.format(key, value))
        elif opcaoMenuConsultar == '4':
            return
        else:
            print('!!!!! OPÇÃO INVÁLIDA !!!!!')
            continue

def removerFuncionario():
    print('----------------------- MENU REMOVER FUNCIONÁRIO -----------------------')
    codigoSelecionado = int(input('Digite o codigo do funcionário a ser removido: ')) # Recebe o código
    for funcionario in listaFuncionario:
        if funcionario['codigo'] == codigoSelecionado: # Se o código do funcionário for igual ao código passado
            listaFuncionario.remove(funcionario)    # Remove da lista de funcionários


print('Bem vindo ao Controle de Funcionários do Bruno da Rosa Vigel')

while True:
    opcaoMenuPrincipal = input('\nEscolha a opção desejada: \n' +
                        '1-Cadastrar Funcionário \n' +
                        '2-Consultar Funcionário(s) \n' +
                        '3-Remover Funcionário \n' +
                        '4-Sair \n' +
                        '>>') # Recebe o valor da opção do menu

    if opcaoMenuPrincipal == '1': # verifica o valor da opção do menu
        codigoFuncionario += 1 # recebe o código do funcionário + 1 
        cadastrarFuncionario(codigoFuncionario) # envia como parâmetro para a função cadastrarFuncionario
    elif opcaoMenuPrincipal == '2':
        consultarFuncionario()
    elif opcaoMenuPrincipal == '3':
        removerFuncionario()
    elif opcaoMenuPrincipal == '4':
        break
    else:
        print('!!!!! OPÇÃO INVÁLIDA !!!!!')
        continue # se a opção for inválida retorna para o início do laço