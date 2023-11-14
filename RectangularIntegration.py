import math, time 

def f(x):
  return x*math.sin(x**2) # Function to be integrated
  
(a,b)= (0,(math.pi)**(1/2))
n = int(float(input("How many steps (rectangles) should we use? "))) # Precision variable/Amount of rectangles, higher n = higher accuracy
h = (b - a) / n 
Sum = 0

tic = time.time()

for k in range(n):
  x = a + k*h 
  Sum += f(x)*h

M = 2

ErrorUpperBound = M * (b - a) ** 2/n 
toc = time.time()

print("The estimated value of the definite integral over ["+str(a)+","+str(b)+"] is "+str(Sum)+" when using "+str(n)+" steps.")