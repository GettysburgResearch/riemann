import sys, time
import mpmath as mp
sys.path.insert(0,'/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/det')
from loewner import *
M=60; gam=zeta_ordinates(M,dps=40)
MUS=[g*mp.mpf("1.5") for g in gam]; WS=[mp.mpf(1)]*M
for N,mult in ((22,1),(22,2),(24,1),(24,2)):
    dps=mult*(40+6*N); mp.mp.dps=dps
    pred=1.6634-0.5316*N-0.05618*N*N; lo=int(pred)-30
    t0=time.time()
    Q0=Q_of_delta(N,MUS,WS,None,None); inr=inertia(Q0)
    lmin0=lambda_min(Q0); lmax0=lambda_max(Q0)
    dc,_=delta_critical(N,MUS,WS,0,lo_exp=lo,hi_exp=3,refine=32)
    print("  N=%2d dps=%3d inertia=%s lam_max=%.8e lam_min0=%.8e delta_c=%.8e [%.0fs]"
          %(N,dps,str(inr),float(lmax0),float(lmin0),float(dc),time.time()-t0))
    sys.stdout.flush()
