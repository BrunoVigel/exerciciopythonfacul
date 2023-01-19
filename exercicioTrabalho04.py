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
                            'salario': salario}
    listaFuncionario.append(dicionarioFuncionario.copy())

def consultarFuncionario():
    print('----------------------- MENU CONSULTAR FUNCIONÁRIO -----------------------')
    while True:
        opcaoMenuConsultar = input('\nEscolha a opção desejada: \n' +
                            '1-Consultar Todos os Funcionários \n' +
                            '2-Consultar Funcionários por ID \n' +
                            '3-Consultar Funcionário por SETOR \n' +
                            '4-Retornar \n' +
                            '>>')

        if opcaoMenuConsultar == '1':
            print('teste1')
            for funcionario in listaFuncionario:
                print('\n')
                for key, value in funcionario.items():
                    print('{}: {}'.format(key, value))
        elif opcaoMenuConsultar == '2':
            codigoSelecionado = input('Digite o ID do funcionário: ')
            for funcionario in listaFuncionario:
                if funcionario['codigo'] == codigoSelecionado:
                    print('\n')
                    for key, value in funcionario.items():
                        print('{}: {}'.format(key, value))
        elif opcaoMenuConsultar == '3':
            codigoSelecionado = input('Digite o setor do(s) funcionários: ')
            for funcionario in listaFuncionario:
                if funcionario['setor'] == codigoSelecionado:
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
    codigoSelecionado = int(input('Digite o codigo do funcionário a ser removido: '))
    for funcionario in listaFuncionario:
        if funcionario['codigo'] == codigoSelecionado:
            listaFuncionario.remove(funcionario)


print('Bem vindo ao Controle de Funcionários do Bruno da Rosa Vigel')

while True:
    opcaoMenuPrincipal = input('\nEscolha a opção desejada: \n' +
                        '1-Cadastrar Funcionário \n' +
                        '2-Consultar Funcionário(s) \n' +
                        '3-Remover Funcionário \n' +
                        '4-Sair \n' +
                        '>>')

    if opcaoMenuPrincipal == '1':
        codigoFuncionario += 1
        cadastrarFuncionario(codigoFuncionario)
    elif opcaoMenuPrincipal == '2':
        consultarFuncionario()
    elif opcaoMenuPrincipal == '3':
        removerFuncionario()
    elif opcaoMenuPrincipal == '4':
        break
    else:
        print('!!!!! OPÇÃO INVÁLIDA !!!!!')
        continue