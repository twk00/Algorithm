N,K = map(int,input().split()) 
a=[]
for i in range(N):
    a.append(int(input()))
c=0
for i in reversed(range(N)):
    c+=K//a[i]
    K=K%a[i]
print(c)