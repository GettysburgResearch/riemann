#!/usr/bin/env python3
"""Ordinary quadrature discovery for centered U and residual parity blocks.

Exact coefficient balls are replaced by floating midpoints; every reported
lower sign is exploratory and must not be treated as a certificate.
"""
import argparse,json,math
from pathlib import Path
import numpy as np
from scipy.linalg import qr
from scipy.special import roots_legendre
from flint import arb,acb
from explore_effective import B,C2,kernel,primitive


def run(path,order):
    data=json.loads(path.read_text())
    coeff=np.array([[float(arb(x).mid()) for x in row] for row in data['exact_trial_z_coefficients_balls']])
    u=np.array([[float(arb(x).mid()) for x in row] for row in data['U_matrix_balls']])
    nodes,weights=roots_legendre(order);t=(nodes+1)/2;weights/=2
    functions=data['exact_basis_coefficients_balls'];m=data['removed_sine_modes'];ne=data['even_dimension']
    base=np.zeros((order,len(functions)),dtype=complex);der=base.copy()
    b0=np.zeros(len(functions),dtype=complex);b1=b0.copy()
    for j,terms in enumerate(functions):
        for term in terms:
            kind,index=term['key'];beta=index/2 if kind=='r' else 1j*math.pi*index
            ca=complex(float(arb(term['real']).mid()),float(arb(term['imag']).mid()))
            values=ca*np.exp(beta*t)
            base[:,j]+=values;der[:,j]+=beta*values;b0[j]+=ca;b1[j]+=ca*np.exp(beta)
    imaginary=max(np.max(np.abs(base.imag)),np.max(np.abs(der.imag)))
    z=base.real@coeff;zp=der.real@coeff;z0=b0.real@coeff;z1=b1.real@coeff
    kmat=kernel(t[:,None]-t)*weights[None,:]
    ff=-kernel(t)[:,None]*z0+kernel(t-1)[:,None]*z1-kmat@zp
    del kmat
    intk=(primitive(t[:,None]-t)+primitive(t)[None,:])*weights[None,:]
    ff+=C2*(intk@z);del intk
    protect=np.column_stack((np.ones(order),np.cos(math.pi*t[:,None]*np.arange(1,m+1)),np.sinh(B*(t-.5))))
    p,_=qr(np.sqrt(weights)[:,None]*protect,mode='economic')
    wf=np.sqrt(weights)[:,None]*ff;res=wf-p@(p.T@wf);r=res.T@res
    even=u[:ne,:ne]-(45/8)*r[:ne,:ne]
    odd=u[ne:,ne:]-(27/2)*r[ne:,ne:]
    return {'status':'CENTERED_SAMPLED_R_NOT_CERTIFIED','quadrature_order':order,
      'trial_modes':data['trial_modes'],'even_dimension':ne,'odd_dimension':data['odd_dimension'],
      'even_U_eigenvalues':np.linalg.eigvalsh(u[:ne,:ne]).tolist(),
      'odd_U_eigenvalues':np.linalg.eigvalsh(u[ne:,ne:]).tolist(),
      'even_lower_eigenvalues':np.linalg.eigvalsh(even).tolist(),
      'odd_lower_eigenvalues':np.linalg.eigvalsh(odd).tolist(),
      'residual_cross_block_norm':float(np.linalg.norm(r[:ne,ne:],2)),
      'literal_basis_imaginary_roundoff':float(imaginary),'residual_matrix':r.tolist(),
      'limitations':['ordinary arithmetic','unproved quadrature error','coefficient-ball midpoint substitution'],
      'source_artifact':str(path)}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('artifact',type=Path)
    p.add_argument('--order',type=int,default=2000);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();result=run(a.artifact,a.order)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='residual_matrix'},indent=2))
