import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zomega import *
import itertools
ps=eisenstein_primes(400)
def close(a,b,tol=1e-8): return abs(a-b)<tol
FOUR=(4,0); MINUS1=(-1,0)
def G(fs): return chi(fs,FOUR).conjugate()*gauss(fs,3)
def cls(x,m=4):  # residue class of primary x modulo m*O as tuple
    return (x[0]%m, x[1]%m)
# 1. R(a,b)=chi_b(a)/chi_a(b) is +-1 and depends only on classes mod 4 of a,b
Rtab={}; incons=0; nonsign=0
for a,b in itertools.combinations(ps[:40],2):
    r=chi([b],a)/chi([a],b)
    if not (close(r,1) or close(r,-1)): nonsign+=1; continue
    r=round(r.real)
    key=(cls(a),cls(b))
    for kk in (key,(key[1],key[0])):
        if kk in Rtab and Rtab[kk]!=r: incons+=1
        Rtab[kk]=r
print('R: non-sign',nonsign,'inconsistent-with-mod4-dependence',incons,'classes seen',len(Rtab))
# 2. paper's closed form: square classes rep (-1)^e lam^f ; R=(-1)^{eh+fg+fh}
# determine square class of c in (O/4)^x modulo squares by Gamma_quad values table: 1,-1 ->1 ; lam -> i ; -lam -> -i
def Gq(c):
    a,b=c; I=1j
    return (1+I**(-b)+I**a+I**(b-a))/2
# check Gamma_quad(p) = gamma_3(p) and closed formula = definition |c|^-1 sum e(x^2/c)
bad=0
for p in ps[:30]:
    g3=gauss([p],3)
    direct=sum(e_add(cval(mul(x,x))/cval(p)) for x in residues(p))/abs(cval(p))
    if not (close(g3,Gq(p)) and close(direct,Gq(p))): bad+=1
print('Gamma_quad closed form vs gamma_3 and direct sum: failures',bad)
# R as ratio of Gamma_quad
bad=0
for a,b in itertools.combinations(ps[:40],2):
    r=chi([b],a)/chi([a],b)
    if not close(r, Gq(mul(a,b))/(Gq(a)*Gq(b))): bad+=1
print('R = Gq(ab)/(Gq(a)Gq(b)) failures',bad)
# 3. G depends only on class mod 4 (via Gq) and chi_c(4) depends on c mod 2
bad=0
for p in ps[:40]:
    if not close(G([p]), chi([p],FOUR).conjugate()*Gq(p)): bad+=1
Gcls={}; inc=0
for p in ps[:60]:
    k=(p[0]%4,p[1]%4); v=G([p])
    if k in Gcls and not close(Gcls[k],v): inc+=1
    Gcls[k]=v
print('G = conj(chi(4))*Gq failures',bad,'; G not a function of class mod 4:',inc,'classes',len(Gcls))
# 4. G(ab)=G(a)G(b)R(a,b) and R(c,c)=chi_c(-1)
bad=0
for a,b in itertools.combinations(ps[:25],2):
    if not close(G([a,b]), G([a])*G([b])*(chi([b],a)/chi([a],b))): bad+=1
bad2=0
for p in ps[:40]:
    if not close(Gq(mul(p,p))/(Gq(p)**2), chi([p],MINUS1)): bad2+=1
print('G(ab)=G(a)G(b)R failures',bad,'; R(c,c)=chi_c(-1) failures',bad2)
# 5. quotient identity: chi_a(-1) conj(G(a)) G(b) R(a,b) = G(b a^{-1}) where G evaluated on a prime c with c = b a^{-1} in classes mod 4 (and mod 2 for chi(4))
bad=0; tested=0
for a,b in itertools.combinations(ps[:25],2):
    lhs=chi([a],MINUS1)*G([a]).conjugate()*G([b])*(chi([b],a)/chi([a],b))
    # find prime c with c*a == b mod 4
    for c in ps:
        if c in (a,b): continue
        t=sub(mul(c,a),b)
        if t[0]%4==0 and t[1]%4==0:
            tested+=1
            if not close(lhs,G([c])): bad+=1
            break
print('quotient identity tested',tested,'failures',bad)
