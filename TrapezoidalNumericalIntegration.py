import math, time 

def f(x):
  return x*math.sin(x**2)
  
(a, b)= (0, 1) # range from 0 - 1
n = 6 # 6 steps
h = (b - a) / n # change in x aka Delta x
Sum = 0

tic = time.time()

for k in range(n):
  x = a + k * h  # function value of kTh term
  r = a + (k + 1) * h # gets the function value of k+1 
  Sum += (f(x) + f(r)) / 2 * h # trapezoid area is defined by (A+B)/2 * height

M = 3.1 # max value of 2nd derivative over [0,1]
ErrorUpperBound =  (((b - a) ** 3) * M) / (12 * (n ** 2)) # upper error bound
toc = time.time()

print("The estimated value of the definite integral over ["+str(a)+","+str(b)+"] is "+str(Sum)+" when using "+str(n)+" steps.")
print("The error upper bound associated with this estimate is "+str(ErrorUpperBound)+".")
print("This program took "+str(toc-tic)+" seconds to run.")