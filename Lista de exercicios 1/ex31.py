jogada = int(input("digite 1 para pedra, 2 para papel e 3 para tesoura: "))
import random
a = random.randint(1,3)
if a == jogada:
    print("empatou!")
elif a == 1 and jogada == 2:
    print("a maquina jogou pedra, você ganhou!")
elif a == 1 and jogada == 3:
    print("a maquina jogou pedra, você perdeu :(")
elif a == 2 and jogada == 1:
    print("a maquina jogou papel, você perdeu :(")
elif a == 2 and jogada == 3:
    print("a maquina jogou papel, você ganhou!")
elif a == 3 and jogada == 1:
    print("a maquina jogou tesoura, você ganhou!")
elif a == 3 and jogada == 2:
    print("a maquina jogou tesoura, você perdeu :(")
else:
    print("por favor, escolha uma jogada valida")
    print(a)
