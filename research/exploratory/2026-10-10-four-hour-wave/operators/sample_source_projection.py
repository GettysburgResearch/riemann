#!/usr/bin/env python3
"""Uncertified discovery fit for the exact Galerkin source-projection lemma."""
import argparse,json,math
from pathlib import Path
import numpy as np
from scipy.linalg import qr,solve_triangular
from scipy.special import roots_legendre
from flint import arb
from explore_effective import B,C2,kernel,primitive


def run(path,order,coefficient):
    data=json.loads(path.read_text());removed=data['removed_sine_modes'];trial=data['trial_modes']
    coeff=np.array([[float(arb(x).mid()) for x in row] for row in data['exact_trial_z_coefficients_balls']])
    u=np.array([[float(arb(x).mid()) for x in row] for row in data['U_matrix_balls']])
    nodes,weight=roots_legendre(order);t=(nodes+1)/2;weight/=2;sqrtw=np.sqrt(weight)
    low=np.arange(1,removed+1);high=np.arange(removed+1,removed+trial+1)
    def sins(m):return np.sin(math.pi*t[:,None]*m)
    def dsins(m):return math.pi*m*np.cos(math.pi*t[:,None]*m)
    ebase=np.column_stack((sins(low),np.exp(t/2),np.exp(-t/2),np.cosh(B*t)))
    zbase=np.column_stack((ebase,sins(high)))
    dbase=np.column_stack((dsins(low),.5*np.exp(t/2),-.5*np.exp(-t/2),B*np.sinh(B*t),dsins(high)))
    z0=np.concatenate((np.zeros(removed),[1,1,1],np.zeros(trial)))
    z1=np.concatenate((np.zeros(removed),[math.exp(.5),math.exp(-.5),math.cosh(B)],np.zeros(trial)))
    kmat=kernel(t[:,None]-t)*weight[None,:]
    fbase=-kernel(t)[:,None]*z0+kernel(t-1)[:,None]*z1-kmat@dbase
    del kmat
    intk=(primitive(t[:,None]-t)+primitive(t)[None,:])*weight[None,:]
    fbase+=C2*(intk@zbase);del intk
    q,r=qr(sqrtw[:,None]*ebase,mode='economic')
    projection_coef=solve_triangular(r,q.T@(sqrtw[:,None]*sins(high)))
    vcoef=np.vstack((-projection_coef,np.eye(trial)))
    fz=fbase@coeff;fv=fbase@vcoef
    pbase=np.column_stack((np.ones(order),np.cos(math.pi*t[:,None]*low),np.sinh(B*t)))
    qp,_=qr(sqrtw[:,None]*pbase,mode='economic')
    weighted_z=sqrtw[:,None]*fz;weighted_v=sqrtw[:,None]*fv
    rz=weighted_z-qp@(qp.T@weighted_z);rv=weighted_v-qp@(qp.T@weighted_v)
    fit,_,rank,singular=np.linalg.lstsq(rv,rz,rcond=1e-12)
    # Freeze discovery coefficients to exact decimal rationals for a later directed replay.
    rational_strings=[[format(x,'.12g') for x in row] for row in fit]
    frozen=np.array(rational_strings,dtype=float)
    shifted=rz-rv@frozen
    raw_r=rz.T@rz;shift_r=shifted.T@shifted
    return {'status':'EMPIRICAL_SOURCE_PROJECTION_NOT_CERTIFIED','source_artifact':str(path),
       'order':order,'trial_modes':trial,'removed_sines':removed,'residual_coefficient':coefficient,
       'raw_lower_eigenvalues':np.linalg.eigvalsh((u+u.T)/2-coefficient*raw_r).tolist(),
       'shifted_lower_eigenvalues':np.linalg.eigvalsh((u+u.T)/2-coefficient*shift_r).tolist(),
       'raw_R_operator_norm':float(np.linalg.norm(raw_r,2)),
       'shifted_R_operator_norm':float(np.linalg.norm(shift_r,2)),
       'source_fit_rank':int(rank),'source_fit_singular_min':float(singular[-1]),
       'fit_coefficient_maximum':float(np.max(np.abs(frozen))),
       'fit_decimal_rational_coefficients':rational_strings,
       'limitations':['ordinary arithmetic','unenclosed cusp quadrature','float Eprojection','exactfittrial membership not replayed yet','directed Uballs replaced by midpoints']}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('artifact',type=Path);p.add_argument('--order',type=int,default=2000)
    p.add_argument('--coefficient',type=float,required=True);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();r=run(a.artifact,a.order,a.coefficient);a.out.write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({k:v for k,v in r.items() if k!='fit_decimal_rational_coefficients'},indent=2))
