f = open("A-large-practice.in")
t = int(f.readline().rstrip())  # read a line with a single integer

b = [x for x in range(61)]
b[0] = 1
b[1] = 0
o = [] 

for i in range(t): 
   a = f.readline().rstrip()  
   sa = set(a) 
   al = len(a)
   sl = len(sa)
   o = b[:al]
   if ( al != sl):
      ai = 1
      ot = []
      ot.append(b[0])
      ab = a[1:]
      for ci,c in enumerate(ab,1):
            fi = a[:ci].find(c)
            if fi > -1 :
               ot.append(ot[fi]) 
            else:
               ot.append(b[ai]) 
               ai=ai+1
      o = ot
   s = 0
   if sl == 1:
      sl = 2
   for k in range(al): 
       s = s+o[k]*(sl**(al-k-1))
   print("Case #{}: {}".format(i+1,s)) 
