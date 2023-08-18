a=int(input())
b=(a*(1.20))+100
c=(a*(1.50))+100
d=(a*(1.80))+((a*(1.80))*(0.15))
e=(a*(2.00))+((a*(2.00))*(0.15))
if a<200:
    print("%.2f"%b)
elif a<400 and a>=200:
    print("%.2f"%c)
elif a<600 and a>=400:
    print("%.2f"%d)    
elif a>=600:
    print("%.2f"%e)