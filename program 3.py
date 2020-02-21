a=int(input())
b=list(bin(a))
c=len(b)
l=0
e=[]
for i in range(2,c-1):
        d=int(b[i]+b[i+1])
        if d == 11:    
            l=l+1
            e.append(l)
        else:
            l=0           
g=max(e)
print(g+1)