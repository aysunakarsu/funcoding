import numpy as np
from functools import lru_cache

f = open("C-large-practice.in")
t = int(f.readline())  # read a line with a single integer

def bribes(p, r):
   @lru_cache(maxsize=None)
   def solve(a, b):
       ri = 0
       for pi in r:
           if (pi>=a) & (pi <=b) :
              tmp = b - a + solve(a, pi-1) + solve(pi+1, b)
              if (not ri) or (tmp < ri):
                 ri = tmp
       return ri 
   return solve(1, p)

for i in range(t):
   p, q = np.array(f.readline().split(),dtype=int)
   r = np.array(f.readline().split(),dtype=int)
   g = bribes(p,r)
   print("Case #{}: {}".format(i+1,g))

f.close()
