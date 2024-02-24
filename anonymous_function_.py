# >>>>>>anonymous function is a function that======>>>> Python Lambda Functions are anonymous functions means that the function is without a name. As we already know the def keyword is used to define a normal function in Python. Similarly, the lambda keyword is used to define an anonymous function in Python. >>>>>
nterms = int(input("Enter number of term here:"))


result = list(map(lambda x : 2 ** x,range(nterms+1)))


print(result)

for i in range(nterms+1):
    print("the value of 2 raised to power" ,i,"is" ,result[i])