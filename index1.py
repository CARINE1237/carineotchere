i=1
r=1
def factoriel(i,r):
    i=1
    r=1
    while i <= n:
        r=r*i
        i+=1
    return r 
def multiple (i):
    for i in range(1,51):
        if i%3==0:
             print(i,"OTCHERE")
        if i%5==0:
             print(i,"Carine")
        if i%3==0 and i%5==0:
             print(i,"OTCHERE Carine")



n=int(input("entrez un nombre:"))
print("le factoriel est",factoriel(i,r))
print(multiple(i))
