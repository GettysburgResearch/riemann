"""G2 final checks:
 (a) detached-band decomposition Sigma = pR(p) + sum_{m>=2n} U(m) dG'(m), dG'(2n):=G(2n),
     valid for ALL band p including p=2n-1;
 (b) I4 convexity lemma sample: D_j(m) > D_{2j}(m) whenever (2m+2)j<=X  (analytic proof exists);
 (c) clean cardinality counts of dG-algebra chains (#pos vs #neg) at several deep (X,n,p);
 (d) rank-2 mechanism: identify rank-1/rank-2 A and B objects at each tested point;
 (e) exit-dipole ratio law w(p+1)/w(p) and w(2p)/w(2p+2).
"""
from fractions import Fraction
from mpmath import mp, mpf, log, sqrt
mp.dps = 30

def mobius_sieve(n):
    mu=[0]*(n+1); mu[1]=1; pr=[]; comp=[False]*(n+1)
    for i in range(2,n+1):
        if not comp[i]: pr.append(i); mu[i]=-1
        for p in pr:
            if i*p>n: break
            comp[i*p]=True
            if i%p==0: mu[i*p]=0; break
            mu[i*p]=-mu[i]
    return mu

def children(m): return (m//2, m-m//2, (m+2)//3, m-(m+2)//3)

def setup(X):
    mu=mobius_sieve(X)
    w=[mpf(0)]*(X+2)
    for q in range(1,X+1): w[q]=log(mpf(X)/q)/sqrt(mpf(q))
    U=[mpf(0)]*(X+2)
    for m in range(1,X+1):
        U[m]=sum(mu[k]*w[m*k] for k in range(1,X//m+1) if mu[k])
    R=[U[m]-U[m+1] for m in range(X+1)]
    return mu,w,U,R

def Wtab(X,n,p):
    W=[Fraction(0)]*(X+2)
    for M in range(n,min(2*n,X+1)): W[M]=Fraction(1 if M==p else 0)
    for M in range(2*n,X+1):
        s=Fraction(0)
        for c in children(M):
            if c>=n: s+=W[c]
        W[M]=s/2
    return W

print("(a) detached-band decomposition, all p incl. 2n-1:")
for (X,n) in [(100,8),(100,6),(200,15)]:
    mu,w,U,R=setup(X)
    worst=mpf(0)
    for p in range(n,min(2*n,X+1)):
        W=Wtab(X,n,p)
        Sig=sum(m*R[m]*mpf((W[m]*p).numerator)/mpf((W[m]*p).denominator)/m for m in range(n,X+1))  # mR(m)E = mR*(p W/m)= p R W
        far=mpf(0)
        for m in range(2*n,X+1):
            gm1 = W[m-1]*p if m-1>=2*n else Fraction(0)   # detached: G'(2n-1):=0
            d=(W[m]*p)-gm1
            far+=U[m]*mpf(d.numerator)/mpf(d.denominator)
        worst=max(worst,abs(Sig-(p*R[p]+far)))
    print(f"   X={X} n={n}: max |Sigma - (pR(p)+far_detached)| = {float(worst):.2e}")

print("(b) I4 sample check D_j(m) > D_{2j}(m):")
for X in (100,1000):
    mu,w,U,R=setup(X)
    bad=0; tot=0
    for m in range(2,X):
        for j in range(1,X//(2*(m+1))+1,2):
            if not mu[j]: continue
            tot+=1
            Dj=w[m*j]-w[(m+1)*j]; D2j=w[2*m*j]-w[2*(m+1)*j]
            if not Dj>D2j: bad+=1
    print(f"   X={X}: {bad}/{tot} violations")

print("(c,d,e) cardinalities and rank mechanism (dG-algebra):")
for (X,n,p) in [(100,13,13),(1000,13,20),(1000,23,30),(1000,29,40),(1000,50,70),(1000,50,99)]:
    mu,w,U,R=setup(X)
    W=Wtab(X,n,p)
    dW={}
    for m in range(n,X+1):
        dW[m]=W[m]-(W[m-1] if m-1>=n else Fraction(0))
    A=[];B=[]
    for m in range(n,X+1):
        if dW[m]==0: continue
        dWf=mpf(dW[m].numerator)/mpf(dW[m].denominator)
        for k in range(1,X//m+1):
            if not mu[k]: continue
            v=mu[k]*w[m*k]*dWf
            (A if v>0 else B).append((v,m,k))
    A.sort(key=lambda t:-t[0]); B.sort(key=lambda t:t[0])
    r1=f"A1=({A[0][1]},{A[0][2]}) B1=({B[0][1]},{B[0][2]})"
    r2=f"A2=({A[1][1]},{A[1][2]}) B2=({B[1][1]},{B[1][2]})"
    print(f"   X={X} n={n} p={p}: #A={len(A)} #B={len(B)} inj_possible={len(B)<=len(A)}; {r1}; {r2}; "
          f"B2/A2={float(-B[1][0]/A[1][0]):.4f}; w(p+1)/w(p)={float(w[p+1]/w[p]):.4f}; w(2p)/w(2p+2)={float(w[2*p]/w[2*p+2]):.4f}")
