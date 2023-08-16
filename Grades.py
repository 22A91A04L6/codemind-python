a,b,c,d,e = map(int,input().split())
t = (a+b+c+d+e)/5
if t>=90:
    print("Grade A")
elif t>=80:
    print("Grade B")
elif t>=70:
    print("Grade C")
elif t>=60: 
    print("Grade D")
elif t>=40: 
    print("Grade E")
elif t<40:
    print("Grade F")