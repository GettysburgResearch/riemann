import numpy as np
# dipole profile levels (per unit mult): f(s;y)=2(y^2-s^2)/(s^2+y^2)^2
# f''(s;y) = -12(s^4-6s^2y^2+y^4)/(s^2+y^2)^4
# f''''(s;y) = -240(s^2-y^2)(s^2-4sy+y^2)(s^2+4sy+y^2)/(s^2+y^2)^6
def f0(s,y): return 2*(y*y-s*s)/(s*s+y*y)**2
def f2(s,y): return -12*(s**4-6*s*s*y*y+y**4)/(s*s+y*y)**4
def f4(s,y): return -240*(s*s-y*y)*(s*s-4*s*y+y*y)*(s*s+4*s*y+y*y)/(s*s+y*y)**6

# sanity vs finite differences
s0,y0=0.37,0.81; hh=1e-4
num2=(f0(s0+hh,y0)-2*f0(s0,y0)+f0(s0-hh,y0))/hh**2
num4=(f0(s0+2*hh,y0)-4*f0(s0+hh,y0)+6*f0(s0,y0)-4*f0(s0-hh,y0)+f0(s0-2*hh,y0))/hh**4
print("deriv check:", abs(num2-f2(s0,y0)), abs(num4-f4(s0,y0)))

def triple_margin(pairs, tgrid):
    """pairs: list of (x,y,m). Returns max over t of min(L0,L2,L4) normalized margins,
    and the argmax t."""
    L0=np.zeros_like(tgrid); L2=np.zeros_like(tgrid); L4=np.zeros_like(tgrid)
    S0=np.zeros_like(tgrid); S2=np.zeros_like(tgrid); S4=np.zeros_like(tgrid)
    for (x,y,mm) in pairs:
        s=tgrid-x
        a,b,c=mm*f0(s,y),mm*f2(s,y),mm*f4(s,y)
        L0+=a; L2+=b; L4+=c
        S0+=np.abs(a); S2+=np.abs(b); S4+=np.abs(c)
    # normalized margins (scale-free)
    M=np.minimum(np.minimum(L0/np.maximum(S0,1e-300), L2/np.maximum(S2,1e-300)), L4/np.maximum(S4,1e-300))
    i=int(np.argmax(M))
    return M[i], tgrid[i], (L0[i],L2[i],L4[i])

# 1) verify single pair: T empty
t=np.linspace(-4,4,400001)
print("m=1:", triple_margin([(0.0,1.0,1.0)],t)[0])

# 2) my hand example: equal scales y=1, pair C at 0 mult1, pair B at 0.7 mult 3.4
print("equal-scale mu=3.4:", triple_margin([(0.0,1.0,1.0),(0.7,1.0,3.4)],t)[:2])

# 3) m=2 exploration: y1=1,x1=0; y2=rho, x2=c; mults (1,mu). Cluster iff |c| < R4(1+rho).
R4=2+np.sqrt(3)
best=None
rows=[]
for rho in [1.0,0.8,0.6,0.4,0.25,0.15]:
    mu_min_ne=None
    for c in np.linspace(0.05, R4*(1+rho)*0.99, 60):
        for mu in [1.0,1.1,1.25,1.5,1.75,2.0,2.5,3.0,3.5,4.0,5.0,7.0,10.0]:
            # t-grid covering both pairs finely
            tg=np.linspace(-1.5, c+1.5*rho+1.5, 120001)
            M,tstar,_=triple_margin([(0.0,rho,1.0),(c,1.0,mu)],tg)  # pair1 small scale rho mult1; pair2 scale1 mult mu
            if M>0:
                if mu_min_ne is None or mu<mu_min_ne[0]: mu_min_ne=(mu,c,tstar,M)
                break
    rows.append((rho,mu_min_ne))
for r in rows: print("rho=%.2f min mu with T nonempty:"%r[0], r[1])
