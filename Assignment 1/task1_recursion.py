

# --- FACTORIAL SECTION ---

# 1. Naive Factorial
def factorial_naive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_naive(n - 1)

# 2. Memoized Factorial 
# We store results in a dictionary so we never calculate the same factorial twice
fact_memo = {}
def factorial_memo(n):
    if n == 0 or n == 1:
        return 1
    if n in fact_memo:
        return fact_memo[n]
    
    fact_memo[n] = n * factorial_memo(n - 1)
    return fact_memo[n]


# --- FIBONACCI SECTION ---

# 1. Naive Fibonacci (Very slow)
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

# 2. Memoized Fibonacci (Very fast)
fib_cache = {}
def fib_memo(n):
    if n <= 1:
        return n
    if n in fib_cache:
        return fib_cache[n]
    
    fib_cache[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return fib_cache[n]

# --- USER INPUT SECTION ---

try:
    n_fact = int(input("Enter a number to calculate its factorial: "))
    print("Factorial (Memo):", factorial_memo(n_fact))
except ValueError:
    print("Invalid input for factorial.")

try:
    n_fib = int(input("Enter a number to calculate its Fibonacci: "))
    print("Fibonacci (Memo):", fib_memo(n_fib))
except ValueError:
    print("Invalid input for Fibonacci.")

    