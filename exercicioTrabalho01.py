print('Bem vindo a loja do Bruno da Rosa Vigel')
produto = float(input('Entre com o valor do produto: '))
quantidade = int(input('Entre com valor do quantidade: '))

valorProduto = (produto * quantidade)   # multiplica o produto e a quantidade e registra o valor do produto

if(quantidade >= 0 and quantidade < 11): # verifica a quantidade do produto para definir o valor do frete
    valorfrete = 30.00
elif(quantidade >= 11 and quantidade < 101):
    valorfrete = 60.00
elif(quantidade >= 101 and quantidade < 1001):
    valorfrete = 120.00
elif(quantidade >= 1001):
    valorfrete = 240.00

valorFinal = valorProduto + valorfrete # soma o valor do produto com o valor do produto para registrar o valor final

print('O valor sem frete foi: R$ {:.2f}'.format(valorFinal))
print('O valor com frete foi: R$ {:.2f}'.format(valorFinal))
