import numpy as np
import math
#First step:
#Factor the number
endnum = 1165547315017833928671818221519514360217364769512850694972634276966608764777139685632107196533251916113636826873618982702626918260245806732321339626796631711528838400321866758812099562803500967678699400226626798016068690575469938736199168207523212687169370000
primes = filter(lambda g: not any(g % u == 0 for u in range(2, g)), range(2, 10000))
exps = []
#get prime factorization
for i in primes:
    k = 0
    while(endnum % i == 0):
        k+=1
        endnum /= i
    exps.append(k)
    if(endnum == 1):
        break
print("exponents = %s" %exps)
#Factorization obtained
def floorSqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

jkx2 = ""
for k in exps:
    jkx2 += str(k)
jkx2 = int(jkx2)
while(True):
    breakEarly = False
    try:
        jkxapprox = floorSqrt(jkx2)
        assert jkx2 == jkxapprox*(jkxapprox+1)
        print("jkx2 = %s" % jkx2)
        print("jkx  = %s" % (jkxapprox+1))
        breakEarly = True
        break
    except AssertionError:
        pass
    if(breakEarly):
        break
    jkx2 *= 10
