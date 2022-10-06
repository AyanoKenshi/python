valorDoProduto = float(input("digite o valor do produto: "))
valorComDesconto = valorDoProduto - (valorDoProduto * (5 / 100))
print("o valor do produto com desconto é {}R$".format(valorComDesconto))