import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zomega import *
ps=eisenstein_primes(200)
def close(a,b,tol=1e-8): return abs(a-b)<tol
def residues_ok(m):
    R=residues(m)
    for i in range(len(R)):
        for k in range(i):
            if divides(m,sub(R[i],R[k])): return False
    return len(R)==norm(m)
assert all(residues_ok(p) for p in ps[:10]); assert residues_ok(mul(ps[0],ps[2])); assert residues_ok(mul(ps[0],ps[6]))
FOUR=(4,0); MINUS1=(-1,0)
def G(fs): return chi(fs,FOUR).conjugate()*gauss(fs,3)
bad=[]
for p in ps:
    fs=[p]; g1=gauss(fs,1); g2=gauss(fs,2); gm1=gauss(fs,-1); g3=gauss(fs,3)
    a=alpha(p)
    t1=close(g2**3, -a)                       # gamma_2^3 = mu*alpha
    t2=close(g1*g2, -a*G(fs))                 # gamma_1 gamma_2 = mu alpha G
    t3=close(g1*gm1, chi(fs,MINUS1))          # gamma_1 gamma_{-1} = chi(-1)
    t4=close(a.conjugate()*g2*g1, -G(fs))     # convert1
    t5=close(-gm1, chi(fs,MINUS1)/G(fs)*a.conjugate()*g2)  # convert2
    if not (t1 and t2 and t3 and t4 and t5): bad.append((p,t1,t2,t3,t4,t5))
print('primes tested',len(ps),'(norm<=200, incl. inert -5,-11)', 'failures',bad)
# squarefree composites
import itertools
comp=[(p,q) for p,q in itertools.combinations(ps[:14],2) if norm(p)!=norm(q) or p!=q]
bad=[]
for p,q in comp:
    fs=[p,q]; n=mul(p,q)
    g1=gauss(fs,1); g2=gauss(fs,2); gm1=gauss(fs,-1)
    a=alpha(n)
    ok=close(g2**3,a) and close(g1*g2,a*G(fs)) and close(g1*gm1,chi(fs,MINUS1)) and close(gm1, chi(fs,MINUS1)/G(fs)*a.conjugate()*g2)
    # crt-a with xi trivial: a(pq)=a(p)a(q)chi_q(p)^4
    ap=alpha(p).conjugate()*gauss([p],2); aq=alpha(q).conjugate()*gauss([q],2)
    ok2=close(a.conjugate()*g2, ap*aq*chi([q],p,4))
    if not(ok and ok2): bad.append((p,q,ok,ok2))
print('composites tested',len(comp),'failures',bad)
