while(True):
    jog_m = 0; jog_j = 0

    quat = int(input())
    if(quat==0): break

    n = input().split(" ") # preenche o vetor n dinamicamente
    for i in range(0,quat): # compara os valores e os adiciona as variáveis segundo seu valor
        if(n[i]=="0"):
            jog_m+=1
        else: 
            jog_j+=1
    print(f"Mary won {jog_m} times and John won {jog_j} times")

