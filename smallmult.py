#s = 20
#stop = False
#while(not stop):
#    divs = (19,18,17,16,15,14,12,11,9,8,7,6,3)
##    print(s)
#    for d in divs:
#        if(s % d != 0):
#            break
#        if(d == 20):
#            stop = True
#            break
#    s += 20
#print("Solution found")
#print(s)
import math as m
def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1:
                factors.append(n)
                break
    return factors
#factorization
d_fac = []

for d in range(2,21):
    d_fac.append(prime_factors(d))
#counting
maxs = [0]*20
for r in d_fac:
    for i in set(r):
        comp = r.count(i)
        if comp > maxs[i-1]:
            maxs[i-1] = comp
#compiling
res = 1
for x in range(1,21):
    if(maxs[x-1] > 0):
        res *= m.pow(x,maxs[x-1])
print(res)
