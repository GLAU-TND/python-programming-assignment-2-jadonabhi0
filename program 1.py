a=list(input().split())
b=[]
q=0
c=len(a)
b.append(a[0])
for i in range(0,c):
    for j in range(0,c):
        if b[q][-1] == a[j][0]:
            b.append(a[j])
            q=q+1
d=[]          
for i in b:
    if i not in d:
        d.append(i)
if len(a)!=len(d):       
    for i in range(c):
        if a[0][0] == a[i][-1]:
            d.append(a[i])
print(d)       
       