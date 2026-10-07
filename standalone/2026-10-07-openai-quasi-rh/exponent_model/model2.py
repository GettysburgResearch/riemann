import numpy as np
KMIN=0.75
alpha=5/6
T=np.linspace(1,1.5,1001)[:,None]
S=np.linspace(0,1,301)[None,:]   # r = t-1/2 + S*(1/2)
def Rcount(delta,x,kappa,supply,mode='paper',amp=5/6,tmax=1.5):
    if mode=='DH': return 1-delta
    Tl=np.linspace(1,tmax,301)[:,None]
    r=np.maximum(0.5,Tl-0.5)+S*(Tl-np.maximum(0.5,Tl-0.5))
    m=np.maximum(Tl-r,0)
    q=x*delta
    if mode=='paper':
        e=np.maximum(1,(1-amp)+amp*r); zM=np.maximum((1-r)/2,0); zP=np.maximum((1-2*m)/(6*kappa),0)
    elif mode=='optLS':
        e=np.maximum(1,(1-amp)+amp*r); zM=np.maximum(1-r,0); zP=np.maximum(1-2*m,0)
    elif mode=='invOnly':
        e=np.maximum(1,(1-amp)+amp*r); zM=np.maximum(1-r,0); zP=np.maximum((1-2*m)/(6*kappa),0)
    elif mode=='plainOnly':
        e=np.maximum(1,(1-amp)+amp*r); zM=np.maximum((1-r)/2,0); zP=np.maximum(1-2*m,0)
    elif mode=='msMob':  # optimal mean square for Mobius family only (like 11/12 paper thm:ms) : inverse capacity unchanged, amplification replaced by e=max(1,r)
        e=np.maximum(1,r); zM=np.maximum((1-r)/2,0); zP=np.maximum((1-2*m)/(6*kappa),0)
    b=e-delta*r
    inv=1-delta*r-2*q*np.minimum(zM,supply)
    b=np.where(r<1,np.minimum(b,inv),b)
    pl=np.where(m<0.5,1-2*delta*m-2*q*np.minimum(zP,supply),1-2*delta*m)
    b=np.minimum(b,pl)
    return b.max(axis=1).min()
def F(delta,x,beta,geo,mode='paper',d=None,**kw):
    lx,b,ell=geo; ly=lx+b; h=1+ell-lx; z0=17/50
    if d is None: d=h
    a=(1+delta)/2; kappa=max(2*beta-1,KMIN)
    R=Rcount(delta,x,kappa,ell/d,mode,**kw)
    return a*(1-ly)-ell/2+z0*(h-d)+d*(R+delta/2)+x*delta*ell-h/6
def sigma_low(geo):
    lx,b,ell=geo; ly=lx+b; h=1+ell-lx; M=lx+ly
    return 1-h/6+max(b/12,b-ly/2)+max(0,(1+3*ell-2*M)/8)
def worst(beta,geo,mode='paper',nd=60,xs=(0,0.1,0.2,0.3,0.4,0.5),**kw):
    mx=-9;arg=None
    for delta in np.linspace(0.0,2*beta-1,nd+1):
        for x in xs:
            v=F(delta,x,beta,geo,mode,**kw)-beta
            if v>mx: mx=v;arg=(round(delta,4),x)
    return mx,arg
def sigma_low2(geo,nd=50):
    lx,b,ell=geo; ly=lx+b; h=1+ell-lx; M=lx+ly
    best=-9
    for d in np.linspace(0,ell,nd+1):
        exc=max(0,M+ell-1-3*d,(1+3*ell-2*M+d)/4)
        low=lx/2-d+0.5*max(b/6,2*b-ly+d)+exc/2
        best=max(best,low)
    return best-(lx/2-1+h/6)
