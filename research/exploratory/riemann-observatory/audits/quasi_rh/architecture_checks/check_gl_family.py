import sys, os, itertools; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zomega import *
# Lemma 6.5 (l.1903-1912): x -> (x/k)_2 * kappa_lambda(x)^{e_k}, e_k = 0 if N(k)=1 mod 4 else 1,
# should be trivial on the six units for squarefree primary k prime to 6.
ps=eisenstein_primes(150)
def quad(fs,x):  # (x/k)_2 = chi_k(x)^3
    v=chi(fs,x,3); return round(v.real)
def kappa(x):    # nontrivial character mod lambda: O/lambda = F_3, x = a+b w -> a+b*1 mod 3 (w = 1 mod lambda)
    r=(x[0]+x[1])%3
    return 0 if r==0 else (1 if r==1 else -1)
bad=0; n=0
for r in (1,2):
    for fs in itertools.combinations(ps[:12],r):
        k=prod(fs); e=0 if norm(k)%4==1 else 1
        for u in UNITS:
            n+=1
            if quad(list(fs),u)*kappa(u)**e!=1: bad+=1
print('unit-triviality cases',n,'failures',bad)
