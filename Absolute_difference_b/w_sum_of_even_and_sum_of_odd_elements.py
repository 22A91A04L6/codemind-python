n=int(input())
ls=list(map(int,input().split()))
s1=0
s2=0
for element in ls:
    if(element%2==0):
        s1+=element
    else:
        s2+=element
if(s1>s2):
    print(s1-s2)
else:
    print(s2-s1)