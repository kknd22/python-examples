
def fib(n) :
    if (n == 0) :
        return 0
    elif (n == 1):
        return 1
    return fib(n-1) + fib(n-2)


for i in range(0, 10) :
    holder = "fib {} is {}"
    print (holder.format(i , fib(i)))