"""NON-CERTIFYING reconnaissance of unrelaxed ES residuals; no proof dependency."""
import json, time
import numpy as np
from scipy.linalg import toeplitz, qr, eigvalsh, solve
from numpy.polynomial.legendre import leggauss
import mpmath as mp
mp.mp.dps=50
P=float(-mp.diff(mp.zeta,2)/mp.zeta(2))
C=float((1-mp.euler-mp.log(2*mp.pi))/3)
S0=float(mp.mpf(1)/6+mp.log(2)/3)
W0=.5+C+S0-P/1.5
b=1.5;c2=.25

def W(x):
    x=np.abs(x)
    safe=np.where(x==0,1.,x)
    v=np.exp(-safe)
    # log forms stable for small positive x; W0 supplied separately.
    A=np.log1p(v)-np.log(-np.expm1(-safe))
    B=np.log(-np.expm1(-2*safe))
    gamma=(np.exp(-b*safe)*A+np.exp(b*safe)*B+np.exp(-safe/2))/6
    out=.5*np.exp(safe/2)+C*np.exp(-b*safe)+gamma-P/b*np.cosh(b*safe)
    # Only 2 is below exp(1). Correct full local formula uses P2 for all tail.
    y=np.maximum(safe-np.log(2.),0.)
    out+=np.log(2.)/(b*np.sqrt(2.))*np.sinh(b*y)
    return np.where(x==0,W0,out)

results=[]
for n in (256,512,1024):
    t0=time.monotonic();L=1.;K=101;step=L/n
    t=(np.arange(n)+.5)*step
    # Orthogonalized sampled exceptional basis; quadrature/discretization NOT certified.
    chi=np.column_stack([np.exp(-.5*t),np.exp(.5*t),np.cosh(b*t)] + [np.sin(j*np.pi*t) for j in range(1,K+1)])
    Q=qr(chi,mode='economic')[0]
    psis=np.column_stack([np.ones(n)] + [np.cos(j*np.pi*t) for j in range(1,K+1)] + [np.sinh(b*t)])
    Qd=qr(psis,mode='economic')[0]
    inds=np.arange(n)*step
    # 16-point cell-averaged difference kernel (split the triangular weight at zero).
    nodes,weights=leggauss(16);nodes=(nodes+1)/2;weights=weights/2
    avg=sum(w*(1-r)*(W(inds+r*step)+W(inds-r*step)) for r,w in zip(nodes,weights))
    Op=b*step*toeplitz(avg)
    U=Q.T@Op@Q
    # K_z at midpoints by 16-point cell integration.
    avg1=sum(w*(W(inds+(r-.5)*step)) for r,w in zip(nodes,weights))
    Ko=step*toeplitz(avg1)
    kval=(Ko@Q)/np.sqrt(step)
    # Exact derivative of convolution with piecewise-constant sampled trial.
    diff=t[:,None]-(np.arange(n)+.5)[None,:]*step
    Dk=W(diff+step/2)-W(diff-step/2)
    kp=(Dk@Q)/np.sqrt(step)
    # Midpoint primitive approximation; all numerical error remains unbounded.
    jval=step*(np.cumsum(kval,axis=0)-.5*kval)
    Fop=(-Dk+c2*step*np.cumsum(Ko,axis=0)-c2*.5*step*Ko)
    # Fop applied to sampled orthonormal columns yields sqrt(step) times F_z.
    for rank in ([0] if n<1024 else [0,32,128,384,704,880]):
        Z=Q.copy()
        if rank:
            vv=np.column_stack([np.sin(j*np.pi*t) for j in range(K+1,K+rank+1)])
            vv-=Q@(Q.T@vv)
            V=qr(vv,mode='economic')[0]
            G=V.T@Op@V; G=(G+G.T)/2
            Z-=V@solve(G,V.T@Op@Q,assume_a='pos')
        U=Z.T@Op@Z
        FF=Fop@Z
        FF-=Qd@(Qd.T@FF)
        R=FF.T@FF
        lower=(U-3*R);lower=(lower+lower.T)/2
        results.append({'grid':n,'dimension':K+3,'positive_trial_rank':rank,
                        'upper_matrix_min_eigenvalue':float(eigvalsh((U+U.T)/2)[0]),
                        'residual_bound_min_eigenvalue':float(eigvalsh(lower)[0]), 'refined_lower_min_eigenvalue':float(eigvalsh((U+U.T)/2-1.875*(R+R.T)/2)[0]),
                        'residual_trace':float(np.trace(R)), 'generalized_residual_ratio':float(eigvalsh((R+R.T)/2,(U+U.T)/2)[-1]),
                        'wall_seconds':round(time.monotonic()-t0,3)})
print(json.dumps({'classification':'NON_CERTIFYING_FLOATING_RECONNAISSANCE','proof_dependency':False,
                  'actual_full_window_sign_certified':False,'warnings':['No interval arithmetic.',
                  'No analytic discretization remainder.','Sampled constraints are not exact continuum constraints.',
                  'This is not an actual Schur matrix or a theorem about its sign.'],
                  'source_P2_50_digit_input':str(mp.nstr(-mp.diff(mp.zeta,2)/mp.zeta(2),50)),
                  'results':results},indent=2))
