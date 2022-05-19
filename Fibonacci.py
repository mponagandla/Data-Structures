
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

def fibonacci(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        print(result)
    return result
res = recur_fibo(5)
print(res)