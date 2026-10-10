import math, sys
N=int(sys.argv[1])
sieve=bytearray([1])*(N+1); sieve[0]=sieve[1]=0
for i in range(2,int(N**0.5)+1):
    if sieve[i]: sieve[i*i::i]=bytearray(len(sieve[i*i::i]))
def check(weights, x0, C, name):
    # weights: dict jump point -> jump size; function f is a step fn; x real >= x0
    pts=sorted(weights); f=0.0; worst=(0,None,None)
    for q in pts:
        left=f; right=f+weights[q]
        if q> x0:   # left limit at q is the sup over x in [prev, q) with x>=x0 (x0 itself is a jump point here)
            r=abs(left-q)/(q**0.875*math.log(q)**2); worst=max(worst,(r,q,'left'))
        if q>=x0:
            r=abs(right-q)/(q**0.875*math.log(q)**2); worst=max(worst,(r,q,'right'))
        f=right
    print(name, "x>=",x0, "C=",C, "max ratio on [x0, N]:", worst, "OK" if worst[0]<=C else "FAIL")
psi={}
th={}
for p in range(2,N+1):
    if sieve[p]:
        lp=math.log(p); th[p]=lp; q=p
        while q<=N: psi[q]=psi.get(q,0.0)+lp; q*=p
check(psi,227,0.0026,"psi")
check(th,967,0.0026,"theta")
