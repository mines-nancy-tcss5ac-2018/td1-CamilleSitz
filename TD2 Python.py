# Euler 16

def sum(n):
    N=2**n
    S=0
    q=N
    while q>=10:
        q,r=divmod(q,10)
        S+=r
    S+=q
    return S

assert sum(15)==26  
print(sum(1000)) 
#1366





# Euler 22


def liste(): 
    f = open('p022_names.txt', 'r')
    for ligne in f:
        ch+=ligne
    f.close
    Chaine=sorted(ch[0].split(','))
    for i in range(0,len(Chaine)):
        Chaine[i]=Chaine[i].replace('"','')
    return(Chaine)
    
def total():
    T=0
    C=liste()
    for k in range(0,len(C)):
        nom=0
        for elt in C[k]:
            nom+=(ord(elt)-64)
        T+=(k+1)*nom
    return(T)







#Euler 55


def estunPalyndrome(x):
    y=int(str(x)[::-1])
    if x==y:
        return True
    else:
        return False


def Lychrel(n):
    NB=0
    for i in range (1,n+1):
        c=0
        N=i
        while c<50:
            N+=int(str(N)[::-1])
            if not estunPalyndrome(N):
                c+=1
            else:
                c=51
        if c==50:
            NB+=1
    return NB

print(Lychrel(10000))
#249