from email.mime import audio
from re import I


salario = float(input("digite o valor do salário do funcionario: "))
salarioComAumento = salario * 1.15
print("o salario com o aumento fica no valor de {}R$".format (salarioComAumento))