n_teste = 1
while(True):
    opt = int(input())
    if opt==0: break

    lista = input().split(" ")
    for i in range(0,opt):
        if(int(lista[i])==(i+1)):
            print(f"Teste {n_teste}\n{lista[i]}\n")
            break
    n_teste += 1
