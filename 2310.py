stats_total = [0]*3; stats_acertos = [0]*3; aux1 = [0]*3; aux2 = [0]*3
repet = int(input())
for i in range(0,repet,1):
    nome = input()
    aux1 = input().split(" ")
    aux2 = input().split(" ")
    for j in range(0,3,1):
        stats_total[j] += int(aux1[j])
        stats_acertos[j] += int(aux2[j])

print("Pontos de Saque: %.2f %%.\nPontos de Bloqueio: %.2f %%.\nPontos de Ataque: %.2f %%."%(stats_acertos[0]/stats_total[0]*100, stats_acertos[1]/stats_total[1]*100, stats_acertos[2]/stats_total[2]*100))
