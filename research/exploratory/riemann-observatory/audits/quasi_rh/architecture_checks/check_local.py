import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zomega import *
import cmath, math, random
random.seed(1)
ps=eisenstein_primes(200)
def close(a,b,tol=1e-7): return abs(a-b)<tol
MINUS1=(-1,0)
def chip(p,x,j):  # chi_p^j(x) with zero extension, chi_p^0 = 1_{p not | x}
    k=sextic(x,p)
    if k is None: return 0
    return Z6**((k*j)%6)
def inv_mod(x,p):
    N=norm(p); return powmod(x,N-2,p) if False else next(y for y in residues(p) if divides(p,sub(mul(x,y),ONE)))
bad=[]; tested=0; badC=0
for p in ps[:12]+[make_primary((5,0)),make_primary((11,0))]:
    N=norm(p); R=residues(p); nz=[h for h in R if not divides(p,h)]
    gam={j%6: gauss([p],j) for j in range(-6,8)}
    def C(j,h): return sum(chip(p,y,j)*e_add(-cval(mul(h,y))/cval(p)) for y in R)/N
    # check (ray-fourier)
    for j in range(6):
        for h in R[:6]:
            c=C(j,h)
            if j!=0:
                ex = 0 if divides(p,h) else N**-0.5*chip(p,MINUS1,j)*gam[j]*chip(p,h,-j)
            else:
                ex = (1-1/N) if divides(p,h) else -1/N
            if not close(c,ex): badC+=1
    invs={h:inv_mod(h,p) for h in nz}
    for trial in range(3):
        sig=random.choice(nz); eps=random.choice(nz)
        for j in range(6):
            Cj={h:C(j,h) for h in nz}
            for x in R:
                lhs=sum(Cj[h]*chip(p,mul(sig,h),-2)*e_add(cval(mul(eps,mul(invs[h],x)))/cval(p)) for h in nz)
                if j not in (0,4):
                    om=chip(p,MINUS1,j)*gam[j]*gam[(j+2)%6]*chip(p,eps,-j-2); B=chip(p,x,-j-2)
                elif j==4:
                    om=gam[4]; B=N**-0.5*(-1+N*(1 if divides(p,x) else 0))
                else:
                    om=-gam[2]*chip(p,eps,-2); B=N**-0.5*chip(p,x,-2)
                rhs=chip(p,sig,-2)*om*B
                tested+=1
                if not close(lhs,rhs): bad.append((p,j,x))
print('C_{p,j} formula failures',badC)
print('local transform identity tested',tested,'failures',len(bad), bad[:5])
# B_{p,1} is quadratic: chi^{-3} = chi^3 values in {+-1,0}
p=ps[0]
print('B_{p,1} values', sorted(set(round(chip(p,x,-3).real) for x in residues(p))))
