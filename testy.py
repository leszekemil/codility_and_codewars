x = int(input("podja ile ma fibo: "))
count = 0

def fibo(x):
    if x <= 1:
        print(x)
        return
    else:
        return(fibo(x-1) + fibo(x-2))

print(fibo(x))