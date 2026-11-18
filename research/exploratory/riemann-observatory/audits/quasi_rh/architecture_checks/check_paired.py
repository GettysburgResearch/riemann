import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zomega import *
import itertools, cmath, math
ps=eisenstein_primes(120)
def close(a,b,tol=1e-7): return abs(a-b)<tol
FOUR=(4,0); MINUS1=(-1,0)
def G(fs): return chi(fs,FOUR).conjugate()*gauss(fs,3)
def Gq(c):
    a,b=c; I=1j
    return (1+I**(-b)+I**a+I**(b-a))/2
def Gelt(c):  # G on a primary element prime to 6 via closed form (class function)
    # chi_c(4) via sextic symbol multiplicativity over factors is needed; use class-function: find a prime in same class mod 4
    for p in ps:
        t=sub(p,c)
        if t[0]%4==0 and t[1]%4==0: return G([p])
def a2(fs):  # conj(alpha(n)) gamma_2(n)
    return alpha(prod(fs)).conjugate()*gauss(fs,2)
def gamma_prod(f1,j1,f2,j2):
    # normalized Gauss sum of chi_{z1}^{j1} chi_{z2}^{j2} modulo z1 z2 with e(x/(z1 z2))
    m=mul(prod(f1),prod(f2)); s=0
    for x in residues(m):
        c=chi(f1,x,j1)*chi(f2,x,j2)
        if c==0: continue
        s+=c*e_add(cval(x)/cval(m))
    return s/math.sqrt(norm(m))
mu=lambda fs: (-1)**len(fs)
bad=0; tested=0; bad2=0
pairs=[([p],[q]) for p,q in itertools.permutations(ps[:10],2)]
pairs+=[([ps[0],ps[2]],[ps[4]]),([ps[1]],[ps[3],ps[6]])]
for f1,f2 in pairs:
    z1=prod(f1); z2=prod(f2)
    # (initial-paired-gauss) with nu trivial: mu mu gamma(conj chi_{z1} chi_{z2}) = G(z2 z1^{-1}) a(z1) conj(a(z2))
    lhs=mu(f1)*mu(f2)*gamma_prod(f1,-1,f2,1)
    # class of z2 * z1^{-1}: find primary c with c*z1 == z2 mod 4
    c=None
    for p in ps:
        t=sub(mul(p,z1),z2)
        if t[0]%4==0 and t[1]%4==0: c=p; break
    rhs=G([c])*a2(f1)*a2(f2).conjugate()
    tested+=1
    if not close(lhs,rhs): bad+=1
    # (paired-first-gauss): a(u1) conj a(u2) gamma(chi_{u1} conj chi_{u2}) = mu mu G(u1 u2^{-1})
    lhs2=a2(f1)*a2(f2).conjugate()*gamma_prod(f1,1,f2,-1)
    c2=None
    for p in ps:
        t=sub(mul(p,z2),z1)
        if t[0]%4==0 and t[1]%4==0: c2=p; break
    if not close(lhs2, mu(f1)*mu(f2)*G([c2])): bad2+=1
print('paired identities tested',tested,'failures (initial-paired-gauss)',bad,'failures (paired-first-gauss)',bad2)
# finite Fourier transform used in Lemma 4.2: sum_x chi(x) e(xh/m) = sqrt(N m) gamma(chi) conj(chi(h)), chi primitive
bad=0
for f1,f2 in pairs[:8]:
    m=mul(prod(f1),prod(f2)); gam=gamma_prod(f1,-1,f2,1)
    for h in [(1,0),(2,1),(3,-1),(0,0),prod(f1),(5,2)]:
        s=sum(chi(f1,x,-1)*chi(f2,x,1)*e_add(cval(mul(x,h))/cval(m)) for x in residues(m))
        ch=chi(f1,h,-1)*chi(f2,h,1)
        if not close(s, math.sqrt(norm(m))*gam*ch.conjugate()): bad+=1
print('finite Fourier/Gauss identity failures',bad)
