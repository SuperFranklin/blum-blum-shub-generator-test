import sympy
import time

def lcm(a, b):
    #lowest common multiple of a and b
    return a * b / gcd(a, b)

def gcd(a,b):
    #greatest common divisor of a and b
    while b > 0:
        a, b = b, a % b
    return a

def next_prime(x):
        p = sympy.nextprime(x)
        while (p % 4 != 3):
            p = sympy.nextprime(p)
        return p

def generate(logEnabled):
    x = 5 * 1e10
    y = 6 * 1e10
    p = next_prime(x)
    q = next_prime(y)
    M = p * q

    N = 10000

    x = 9823428823 # initial value
    summaryBinary = ""
    for _ in range(N):
        x = x * x % M
        b = x % 2
        summaryBinary += str(b)

    if(logEnabled):
        print(summaryBinary)
        print("Number of zeros:   ", summaryBinary.count("0"))
        print("Number of ones:  ", summaryBinary.count("1"))

print("Tests:")
print("1. execution time. Blum-blum-shub algorithm is computationally heavy and slow.")
generations = 1 * 10 ** 3
start_time = time.time()
for _ in range(generations):
    # in each generation method invocation, algorithm generates 10000 pseudo random numbers
    generate(False)

print("execution time: ", (time.time() - start_time), " [s]")

print()
print("# 2. Blum-blum-shub algorithm returns almost identical number of zeros and ones in binary output")
generate(True)