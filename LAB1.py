'''
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
d=b**2-4*a*c
if d<0:
    print(" NU EXISTA SOLUTII")
elif d==0:
    x=(-b+d**0.5)/(2*a)
    print("Ecuatia are o singura solutie: ",  x)
else:
    x=(-b+d**0.5)/(2*a)
    print("Ecuatia are doua solutii: ",x,end=" ")
    x=(-b-d**0.5)/(2*a)
    print(x)
    PROBLEMA 1
'''
'''
L1=int(input("L1= "))
L2=int(input("L2= "))
L1,L2=min(L1,L2),max(L1,L2)
Aria_pardoseala=(L1*L2)
while L1:
    c=L2%L1
    L2=L1
    L1=c
Aria_placa=(L2*L2)
print("Latura placii de gresie este: ", L2,end=" ")
Nrplaci=Aria_pardoseala//Aria_placa
print( " numarul placilor de gresie este de : ",Nrplaci)
PROBLEMA 2
'''
'''
x = int(input("x= "))
n = int(input("n= "))
p = int(input("p= "))

m = int(input("m= "))
distanta = 0
for i in range(m):
    distanta += x
    if (i + 1) % 10 == 0:
      x =x-p/100*x
print("distanta parcursa este:  ", distanta)
PROBLEMA 3
'''
'''
n=int(input("n="))
z1=float(input("curs ziua 1= "))
difmax=0
zi=0 #variabila folosita cu scopul de a retine prima zi din cele doua cu diferenta de curs cea mai mare
for i in range(n-1):
    print("curs ziua: ",i+2,end=" ")
    z2=float(input())
    if abs(z2-z1)>difmax:
        difmax=abs(z2-z1)
        zi=i+1
    z1=z2
print("cea mai mare crestere a fost de",difmax," RON","intre zilele ",zi," si ",zi+1)
PROBLEMA 4
'''
'''
n=int(input("n= "))
val1=0
val2=0
for i in range(n):
    nrsir=int(input())
    if nrsir>val1 and nrsir>val2:
        val1=val2
        val2=nrsir
    elif nrsir>val1 and nrsir<val2:
       val1=nrsir
if (val1 or val2) :
    print("IMPOSIBIL")
else:
    print("cele mai mari doua numere distincte din sir sunt: ",val1,val2)
PROBLEMA 5
'''
'''
n=int(input("n= "))
copie=n
nrmax=0
nrmin=0
for i in range(9,0,-1):
    while copie!=0:
        if copie%10==i:
            nrmax=nrmax*10+i
            copie//=10
        else:
            copie//=10
    copie=n
print("numarul maxim este: ",nrmax)  #pentru numar maxim
for i in range(10):
    while copie!=0:
        if copie%10==i:
            nrmin=nrmin*10+i
            copie//=10
        else:
            copie//=10
    copie=n
print("numarul min este: ",nrmin)  #pentru numar minim
PROBLEMA 6
'''

