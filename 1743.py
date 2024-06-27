cl1 = input().split(" ")
cl2 = input().split(" ")
compatible = True

for i in range(0, 5):
    if(cl1[i]==cl2[i]):
        compatible = False
        break
    
if(compatible==True):
    print("Y")
else:
    print("N")