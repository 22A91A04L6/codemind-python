n=int(input())
ls=list(map(int,input().split()))
s1=0
s2=0
for i in range(n):
    if(i%2==0):
        s1+=ls[i]
    else:
        s2+=ls[i]
if(s1>s2):
    print(s1-s2)
else:
    print(s2-s1)