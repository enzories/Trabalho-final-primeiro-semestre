def trocar(pos1,pos2):
    aux = posicao_jogo[pos1-1]
    posicao_jogo[pos1-1] = posicao_jogo[pos2-1]
    posicao_jogo[pos2-1] = aux

posicao_jogo = [0]*3
repet = int(input())
pos_i = input()

if pos_i=="A":
    posicao_jogo[0] = 1
elif pos_i=="B":
    posicao_jogo[1] = 1
elif pos_i=="C":
    posicao_jogo[2] = 1

for i in range(0,repet):
    troca = int(input())
    if troca==1:
        trocar(1,2)
    elif troca==2:
        trocar(2,3)
    elif troca==3:
        trocar(1,3)

for i in range(0,3):
    if posicao_jogo[i]==1:
        if i==0:
            print("A")
        elif i==1:
            print("B")
        elif i==2:
            print("C")


