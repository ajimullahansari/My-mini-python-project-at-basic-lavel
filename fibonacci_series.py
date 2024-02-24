#a=0
#b=1
#num = int(input("enter the number to obtain fibonacci sequence:"))
#if num ==1:
#    print(a)
#else:
#    print(a)
#    print(b)
#    for i in range (1,num+1):
#        c=a+b
#        a=b
#        b=c
#        print(c)
                                 #OR

n = int(input("enter the number to obtain the fibonacci series :"))
x=0
y=1
z=1
while(x<=n):
    print(x)
    x=y
    y=z
    z=x+y
