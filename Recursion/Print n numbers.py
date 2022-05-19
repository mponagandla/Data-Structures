arr= []
def recursive_print(n):
    if n>=1:
        #print(n)
        recursive_print(n-1)
        arr.append(n)
        print(n)


recursive_print(8)
print(arr)


