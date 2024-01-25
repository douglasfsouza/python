def fib(n):
    a,b = 0,1
    while a < int(n):
        a,b = b, a+b
        print(a, end=", ") #Com end, so funciona a partir de python3.12
    
    return a
        

f = input("Type a number: ")
r = fib(f)