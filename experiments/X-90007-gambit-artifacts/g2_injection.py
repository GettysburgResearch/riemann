"""G2 — injection hunt, decisive tests.

Object algebra (dG-form): Sigma(p) = p * sum_{(m,k): m>=n, k sf, mk<=X} mu(k) w(mk) dW(m),
  W(m) = G(m)/p = (1/2)^len path-count gen.fn., dW(m)=W(m)-W(m-1), W(n-1):=0.
A-objects: mu(k)*sign(dW(m)) = +1 ; B-objects: = -1 ; weight w(mk)*|dW(m)|.

Test 1 (free injection): sorted domination b_r <= a_r for all r.
Test 2 (node-fiber injection): same, restricted to each node q = mk fiber.
Test 3 (row injection): same, restricted to each row m.
Test 4 (R-form objects): Sigma(p)/p = sum_m R(m) W(m) => objects (m,k) weight
  |w(mk)-w((m+1)k)1| * W(m), sign mu(k) (+ edge objects k in (X/(m+1),X/m]).
  Same three levels.
Report: where domination fails (r, sizes), slack min(a_r - b_r), and Sigma check.
"""
from fractions import Fraction
from mpmath import mp, mpf, log, sqrt
mp.dps = 40

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

def build(X, n, p):
    mu = mobius_sieve(X)
    w = [mpf(0)]*(X+2)
    for q in range(1,X+1): w[q]=log(mpf(X)/q)/sqrt(mpf(q))
    # exact W via Fractions: W(M)=G(M)/p ; G harmonic
    W = [Fraction(0)]*(X+2)
    for M in range(n, min(2*n,X+1)): W[M] = Fraction(1 if M==p else 0)
    for M in range(2*n, X+1):
        s = Fraction(0)
        for c in children(M):
            if c>=n: s += W[c]
        W[M] = s/2
    dW = {}
    for m in range(n, X+1):
        dW[m] = W[m] - (W[m-1] if m-1>=n else Fraction(0))
    return mu, w, W, dW

def dom_test(pos, neg):
    """pos, neg: lists of mpf weights. Returns (ok, first_fail_r, slack_min, len_ok)."""
    pos = sorted(pos, reverse=True); neg = sorted(neg, reverse=True)
    if len(neg) > len(pos): return (False, None, None, False)
    slack = None;
    for r,(b) in enumerate(neg):
        a = pos[r]
        s = a - b
        if slack is None or s < slack: slack = s
        if b > a: return (False, r, float(s), True)
    return (True, None, float(slack) if slack is not None else 0.0, True)

def run(X, n, p, form="dG"):
    mu, w, W, dW = build(X, n, p)
    objs = []  # (signed weight mpf, node q, row m)
    if form=="dG":
        for m in range(n, X+1):
            if dW[m]==0: continue
            dWf = mpf(dW[m].numerator)/mpf(dW[m].denominator)
            for k in range(1, X//m+1):
                if mu[k]==0: continue
                objs.append((mu[k]*w[m*k]*dWf, m*k, m))
        tot = sum(o[0] for o in objs)
    else:  # R-form: R(m) = sum_{k<=X/(m+1)} mu(k)(w(mk)-w((m+1)k)) + sum_{edge} mu(k)w(mk)
        for m in range(n, X+1):
            if W[m]==0: continue
            Wf = mpf(W[m].numerator)/mpf(W[m].denominator)
            kmax_i = X//(m+1); kmax_o = X//m
            for k in range(1, kmax_o+1):
                if mu[k]==0: continue
                if k<=kmax_i: wt = (w[m*k]-w[(m+1)*k])*Wf
                else: wt = w[m*k]*Wf
                objs.append((mu[k]*wt, m*k, m))
        tot = sum(o[0] for o in objs)
    # Sigma check
    Sig_obj = tot  # = Sigma(p)/p
    # levels
    pos_all = [o[0] for o in objs if o[0]>0]; neg_all=[-o[0] for o in objs if o[0]<0]
    free = dom_test(pos_all, neg_all)
    # node fibers
    from collections import defaultdict
    fib = defaultdict(lambda: ([],[]))
    for wt,q,m in objs:
        if wt>0: fib[q][0].append(wt)
        else: fib[q][1].append(-wt)
    nf_fail = 0; nf_tot=0; nf_fail_ex=[]
    for q,(P,N) in sorted(fib.items()):
        if not N: continue
        nf_tot += 1
        ok,_,_,_ = dom_test(P,N)
        if not ok:
            nf_fail += 1
            if len(nf_fail_ex)<6: nf_fail_ex.append(q)
    # rows
    rows = defaultdict(lambda: ([],[]))
    for wt,q,m in objs:
        if wt>0: rows[m][0].append(wt)
        else: rows[m][1].append(-wt)
    r_fail=0; r_tot=0; r_fail_ex=[]
    for m,(P,N) in sorted(rows.items()):
        if not N: continue
        r_tot+=1
        ok,_,_,_ = dom_test(P,N)
        if not ok:
            r_fail+=1
            if len(r_fail_ex)<6: r_fail_ex.append(m)
    print(f"X={X} n={n} p={p} [{form}-form] Sigma/p={float(Sig_obj):+.6e}  #obj={len(objs)} (+{len(pos_all)}/-{len(neg_all)})")
    print(f"   FREE injection: exists={free[0]} first_fail_r={free[1]} min_slack={free[2]}")
    print(f"   NODE fibers with negatives: {nf_tot}, fail {nf_fail}, ex {nf_fail_ex}")
    print(f"   ROW  fibers with negatives: {r_tot}, fail {r_fail}, ex {r_fail_ex}")
    return free, (nf_fail, nf_tot), (r_fail, r_tot), float(Sig_obj)

if __name__ == "__main__":
    for form in ("dG","R"):
        for (X,n,plist) in [(100,8,[8,10,12,15]), (100,6,[6,9,11]), (100,13,[13,20,25])]:
            for p in plist: run(X,n,p,form)
        print("-"*80)
