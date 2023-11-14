import math, time

def f(x):
    return x*math.sin(x**2)

(a, b) = (0, 1) # range from 0 - 1
n = 4 # 4 steps, must be even
h = (b - a) / n # delta X
Sum = 0

tic = time.time()

for k in range(n+1):
    x = a + k * h # gets function value
    if k == 0 or k == 1000: # if first or last term, sets to 1.
        r = 1
    else:
        r = (2 * (k % 2) + 2) # multiplies remainder of index mod 2 times 2, then + 2. formula for doing 2, 4, 2 .... 4, 2, 4
    Sum += (r * (f(x))) # adds the term to the sum

Sum *= (h / 3)

M = 80.249 # max value of 4th derivative over [0,1] (MUST BE PRECOMUPTED AND PLACED HERE)
ErrorUpperBound = (M * ((b - a) ** 5)) / (180 * (n ** 4)) # M*((b-a)^5 / 180*n^4)

toc = time.time()

print("The estimated value of the definite integral over ["+str(a)+","+str(b)+"] is "+str(Sum)+" when using "+str(n)+" steps.")
print("The error upper bound associated with this estimate is "+str(ErrorUpperBound)+".")
print("This program took "+str(toc-tic)+" seconds to run.")