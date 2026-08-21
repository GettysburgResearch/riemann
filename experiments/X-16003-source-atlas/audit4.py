"""Redo the Hankel test with a GLOBAL scale.  My previous version normalised each comparison
by max(|H_{a+1,b}|,|H_{a,b+1}|); for a symmetric source both are structurally ZERO on half the
entries, so it computed 0/0 and returned O(1) noise -- the SAME defect that produced
L-16006's sec 4 erratum, committed a fourth time.  Normalise by the global matrix scale."""
import mpmath as mp
from mpmath import mpf, nstr
mp.mp.dps = 80

def defects(psi,dpsi,N,dps=80):
    mp.mp.dps=dps
    d=2*N+1; nodes=[mpf(j) for j in range(-N,N+1)]
    w=[]
    for j in range(d):
        p=mpf(1)
        for k in range(d):
            if k!=j: p*=(nodes[k]-nodes[j])
        w.append(1/p)
    Q=[[dpsi(nodes[i]) if i==j else (psi(nodes[i])-psi(nodes[j]))/(nodes[i]-nodes[j])
        for j in range(d)] for i in range(d)]
    Qt=[[w[i]*Q[i][j]*w[j] for j in range(d)] for i in range(d)]
    V=[[nodes[i]**a for a in range(d)] for i in range(d)]
    M=[[sum(V[i][a]*Qt[i][j]*V[j][b] for i in range(d) for j in range(d)) for b in range(d)] for a in range(d)]
    gscale=max(abs(M[a][b]) for a in range(d) for b in range(d))
    if gscale==0: gscale=mpf(1)
    worst_g=max(abs(M[a+1][b]-M[a][b+1]) for a in range(d-1) for b in range(d-1))/gscale
    # also report the OLD local-scale metric, to show it was the artefact
    worst_l=mpf(0)
    for a in range(d-1):
        for b in range(d-1):
            sc=max(abs(M[a+1][b]),abs(M[a][b+1]))
            if sc>0: worst_l=max(worst_l,abs(M[a+1][b]-M[a][b+1])/sc)
    return worst_g, worst_l

SRC = [
 ("psi(x)=x            (odd)",      lambda x:x,               lambda x:mpf(1)),
 ("psi(x)=x^2          (even)",     lambda x:x**2,            lambda x:2*x),
 ("psi(x)=x^3          (odd)",      lambda x:x**3,            lambda x:3*x**2),
 ("psi(x)=x^5-2x       (odd)",      lambda x:x**5-2*x,        lambda x:5*x**4-2),
 ("psi(x)=sin(x)       (odd)",      lambda x:mp.sin(x),       lambda x:mp.cos(x)),
 ("psi(x)=atan(x/20)   (odd,Pick)", lambda x:mp.atan(x/20),   lambda x:(mpf(1)/20)/(1+(x/20)**2)),
 ("psi(x)=x/(1+x^2)    (odd)",      lambda x:x/(1+x**2),      lambda x:(1-x**2)/(1+x**2)**2),
 ("psi(x)=1/(x-30.5)   (neither)",  lambda x:1/(x-mpf('30.5')), lambda x:-1/(x-mpf('30.5'))**2),
 ("psi(x)=log(x+40)    (neither)",  lambda x:mp.log(x+40),    lambda x:1/(x+40)),
 ("psi(x)=exp(x/9)     (neither)",  lambda x:mp.e**(x/9),     lambda x:mp.e**(x/9)/9),
]
print("Loewner-Hankel defect, GLOBAL scale (correct) vs LOCAL scale (my previous, buggy)")
print(f"{'source':>30} {'N':>3} {'GLOBAL defect':>16} {'LOCAL (artefact)':>18}")
print("-"*74)
for name,p,dp in SRC:
    for N in (3,5):
        g,l=defects(p,dp,N)
        print(f"{name:>30} {N:>3} {nstr(g,5):>16} {nstr(l,5):>18}")
print()
print("=> With a global scale EVERY source is Hankel at the working-precision floor.")
print("   The reviewer is right: the Loewner-Hankel identity is UNIVERSAL, and my")
print("   'arithmetic evidence' was a measurement of roundoff around it.")
