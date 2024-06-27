tamanho = int(input()); menor = 0

num = input().split(" ")
for i in range(0,tamanho):
    num[i] = int(num[i])
    if(num[i]<num[menor]): menor = i

print(f"Menor valor: {num[menor]}\nPosicao: {menor}")