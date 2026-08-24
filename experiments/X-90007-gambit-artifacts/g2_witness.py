"""G2 — structure of the extremal objects + X=1000 persistence + fractional cover need."""
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

def build_W(X,n,p):
    W=[Fraction(0)]*(X+2)
    for M in range(n,min(2*n,X+1)): W[M]=Fraction(1 if M==p else 0)
    for M in range(2*n,X+1):
        s=Fraction(0)
        for c in children(M):
            if c>=n: s+=W[c]
        W[M]=s/2
    dW={}
    for m in range(n,X+1):
        dW[m]=W[m]-(W[m-1] if m-1>=n else Fraction(0))
    return W,dW

def objects(X,n,p,form,mu,w,W,dW):
    objs=[]
    if form=="dG":
        for m in range(n,X+1):
            if dW[m]==0: continue
            dWf=mpf(dW[m].numerator)/mpf(dW[m].denominator)
            for k in range(1,X//m+1):
                if mu[k]: objs.append((mu[k]*w[m*k]*dWf,m,k))
    else:
        for m in range(n,X+1):
            if W[m]==0: continue
            Wf=mpf(W[m].numerator)/mpf(W[m].denominator)
            for k in range(1,X//m+1):
                if not mu[k]: continue
                wt=(w[m*k]-w[(m+1)*k])*Wf if k<=X//(m+1) else w[m*k]*Wf
                objs.append((mu[k]*wt,m,k))
    return objs

def analyze(X,n,p,form,topN=5):
    mu=mobius_sieve(X)
    w=[mpf(0)]*(X+2)
    for q in range(1,X+1): w[q]=log(mpf(X)/q)/sqrt(mpf(q))
    W,dW=build_W(X,n,p)
    objs=objects(X,n,p,form,mu,w,W,dW)
    pos=sorted([o for o in objs if o[0]>0],key=lambda t:-t[0])
    neg=sorted([o for o in objs if o[0]<0],key=lambda t:t[0])
    Sig=sum(o[0] for o in objs)
    print(f"X={X} n={n} p={p} [{form}] Sigma/p={float(Sig):+.4e}  +{len(pos)}/-{len(neg)}")
    print("   top A:", [(f"{float(t[0]):+.4f}",f"m={t[1]}",f"k={t[2]}") for t in pos[:topN]])
    print("   top B:", [(f"{float(t[0]):+.4f}",f"m={t[1]}",f"k={t[2]}") for t in neg[:topN]])
    if neg:
        b0=-neg[0][0]; a0=pos[0][0] if pos else mpf(0)
        # fractional cover need: how many top-A objects to cover top-B
        need=0; acc=mpf(0)
        for a in pos:
            acc+=a[0]; need+=1
            if acc>=b0: break
        print(f"   largest B/largest A = {float(b0/a0):.4f}; top-B needs {need} largest A-objects to cover fractionally")
    return objs

if __name__=="__main__":
    for form in ("dG","R"):
        analyze(100,8,10,form)
        analyze(100,13,20,form)
    print("="*90)
    # X=1000, deep n
    for form in ("dG","R"):
        analyze(1000,13,20,form)
        analyze(1000,29,40,form)
        analyze(1000,50,70,form)
