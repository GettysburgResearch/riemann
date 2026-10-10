# Affine arithmetic for note O (hybrid induction). Top level: width M=1 (rho=1,q=0), kappa=3/4, beta_Theta=7/8.
kappa=0.75; beta=7/8
def regions(m):
    out={}
    out['S17 plain-as-mark (r+2m<=1, 2r+8m<=3)'] = min(1-2*m, (3-8*m)/2)
    out['S18 Mobius-as-slots (m+6k r<=1)'] = (1-m)/(6*kappa)
    out['large sieve (r+m<=1/2)'] = 0.5-m
    out['descent+Hecke+S17 terminal (r<=8m/19, r+m<=1)'] = min(8*m/19, 1-m)
    out['note G claim (r+min(m,1-m)<=1)'] = 1-min(m,1-m)
    out['exceptional cond. alone (m*+(2b-1)r<=5/6)'] = (5/6-min(m,1-m))/(2*beta-1)
    out['target theta=1/4 (r+m<=5/4)'] = 1.25-m
    return out
for m in (0.41,0.5,1/3):
    print(f"\nm = {m:.3f}")
    for k,v in regions(m).items(): print(f"  {k:60s} r_max = {v:.3f}")
# clean-stage ledger (18.32): c=d=R=E=0, K=K0=2A-rho, J=0, g=sigma, g2=t2=V=0
def clean(A,rho,q,sigma):
    K=2*A-rho; g=sigma; a0=A
    mprime=2*a0-K-g; qprime=q; return (A, mprime+qprime)
print("\nclean stage (A,M)->", clean(1.0,1.0,0.0,0.01), " from A=1,M=1,sigma=0.01")
# theta reflection at Gauss-row stage: dual length 2(K+m)-r with K=2A-rho
def theta_dual(r,m,rho=1.0):
    A=r+m; K=2*A-rho; return 2*(K+m)-r
for r,m in ((0.72,0.41),(0.5,0.5),(0.59,0.41),(0.2,0.1)):
    print(f"theta reflection of Mobius-dual at Gauss-row stage: (r,m)=({r},{m}) -> dual length {theta_dual(r,m):.2f} (shortens iff r+3m<=rho: {r+3*m<=1})")
