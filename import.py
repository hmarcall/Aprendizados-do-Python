import random
i=0
sorteio=[]
for i in range (5):
    nome=input(str('Digite seu nome para o sorteio:'))
    sorteio.append(nome)
    i+=1
    if i ==5:
        escolhido=random.choice(sorteio)
        print('O escolhido foi:',escolhido)
        break