cust_a, cust_c, km_a, km_c = input().split(" ")

cust_km_a = float(km_a)/float(cust_a)
cust_km_c = float(km_c)/float(cust_c)

if(cust_km_c<=cust_km_a):
    print("A")
else:
    print("C")