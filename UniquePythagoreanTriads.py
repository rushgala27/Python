#Find Unique Pythagorean Triads in range 0-100 such that the triad is not multiple of any previous triad

import math

def rep(a,b):
    m = math.gcd(a,b)
    if m <2:
        return True
    return False

print(0,0,0)
for a in range(0,101):
    for b in range(a+1,101):
        d = a**2 + b**2
        for c in range(0,150):
            if d == c**2:
                if(rep(a,b)):
                    print(a,b,c)