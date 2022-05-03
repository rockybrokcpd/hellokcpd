w=list(map(int,input("enter the weights:").split(",")))
pr=list(map(int,input("enter the profits:").split(",")))
capacity=int(input("enter the capacity:"))
f=[]
p=0
for i in range(0,len(w)):
    a=pr[i]/w[i]
    f.append(a)
for j in range(0,len(f)):
    k=f.index(max(f))
    if capacity>=w[k]:
        p=p+pr[k]
        capacity-=w[k]
        f[k]=0
        w[k]=0
    elif capacity!=0 and w[k]>capacity:
        p=p+pr[k]*(capacity/w[k])
        print("Total Profit: ",p)
        break