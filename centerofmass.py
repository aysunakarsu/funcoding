import math

f=  open("B-large-practice.in")
t = int(f.readline().rstrip())  # read a line with a single integer

for i in range(t):
    dm = 0.0
    tm = 0.0
    n = int(f.readline().rstrip())
    ns=n*n
    o = [0.0 for j in range(6)]
    for k in range(n):
        d = [float(p) for p in f.readline().rstrip().split()]
        for m in range(6):
            o[m] += d[m]
    a = (sum(o[x]*o[x] for x in range(5,2,-1)))/ns
    b = 2*(sum(o[x]*o[x+3] for x in range(3)))/ns
    c = (sum(o[x]*o[x] for x in range(3)))/ns
    if b>=0 :
            tm = 0.0
            dm = math.sqrt(c)
    elif a>=1e-8:
            tm = -b/(2*a)
            dm = math.sqrt(math.fabs(c-b*b/(4*a)))
    print("Case #{}: {} {}".format(i+1,dm,tm))

f.close()
