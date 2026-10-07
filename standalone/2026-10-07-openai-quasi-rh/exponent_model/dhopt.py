import numpy as np
best=(9,None)
z0=17/50
for lx in np.linspace(0.05,1.2,231):
  for b in np.linspace(0,0.6,121):
    ly=lx+b
    for ell in np.linspace(0,1.0,201):
      h=1+ell-lx; M=lx+ly
      sl=1-h/6+max(b/12,b-ly/2)+max(0,(1+3*ell-2*M)/8)
      # high under DH at d=h, x=1/2, delta in {0, 2sl-1}
      def Fd(delta): return (1+delta)*(1-ly)/2-h/6-ell/2+delta*ell/2+h*(1-delta/2)
      s=max(sl,Fd(0)+1e-9,Fd(2*sl-1)+1e-9)
      # small rows
      if h*(z0-1/6)-ly/2>=0: continue
      if s<best[0]: best=(s,(lx,b,ell,h))
print('DH-architecture optimum sigma',best)
