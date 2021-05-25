lanche = ("Hamburger", "Suco", "Pizza", "Pudim")
print(lanche[1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-1])#Começa mostrando o ultimo
#
print(len(lanche)) #Mostra quantidade de itens dentro da tupla
#
#Os dois for exibem o mesmo resultado, mas o range determina o começo e o fim
#
for comida in lanche:
    print(f"Eu vou comer {comida}")
for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posicao {cont}")
#
#Outra forma de identificar o indice com o objeto correspondente.
#
for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posicao {pos}")
