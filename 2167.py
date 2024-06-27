# Variáveis

queda = 0

# Inicio

q_testes = int(input())
testes = input().split(" ")

# Processo

for i in range(0,q_testes): # converte os valores do array em int
    testes[i] = int(testes[i])
for i in range(1,q_testes): # verica se existe queda
    if(testes[i]<testes[i-1]): queda = i+1; break

print(f"{queda}")