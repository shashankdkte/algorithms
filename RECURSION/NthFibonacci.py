# TIME COMPLEXITY O(2^n)
# SPACE COMPLEXITY O(n)
def getNthFib(n):
    if n == 2:
        return 1
    if n == 1:
        return 0
    else:
        return getNthFib(n-1)+getNthFib(n-2)

# TIME COMPLEXITY O(n)
# SPACE COMPLEXITY O(N)
def getNthFib(n,memoize={1:0,2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n-1,memoize) + getNthFib(n-2,memoize)
        return memoize[n]   
    
# TIME COMPLEXITY O(n)
# SPACE COMPLEXITY O(1)
def getNthFib(n):
    first = 0
    second = 1
    if n == 2:
        return 1
    if n == 1:
        return 0
    for i in range(3,n+1):
        fib = first + second
        first = second
        second = fib
    return fib    

        