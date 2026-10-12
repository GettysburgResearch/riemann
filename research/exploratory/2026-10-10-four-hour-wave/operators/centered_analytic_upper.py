#!/usr/bin/env python3
"""Directed finite U for the centered reflection-invariant complement.

Literal transforms are imported unchanged from enclose_analytic_upper. The
reflection proof in CENTERED_REFLECTION_REDUCTION makes cross-parity entries
exactly zero. This is an U-only experiment, not a lower continuum certificate.
"""
import argparse
import hashlib
import json
from pathlib import Path
import time

import flint
from flint import arb,acb,arb_mat,ctx
from enclose_analytic_upper import Source,require,block,identity,cholesky,positive_ldl,f


def sine(j):
    return [(('i',j),acb(0,-arb(1)/2)),(('i',-j),acb(0,arb(1)/2))]


def centered_hyperbolic(index,odd=False):
    a=arb(index)/4
    return [(('r',index),acb((-a).exp()/2)),
            (('r',-index),acb((-1 if odd else 1)*a.exp()/2))]


def basis(trial=100,removed=5):
    even=[sine(j) for j in range(1,removed+1) if j%2]
    even.extend([centered_hyperbolic(1),centered_hyperbolic(3)])
    odd=[sine(j) for j in range(1,removed+1) if not j%2]
    odd.append(centered_hyperbolic(1,True))
    high=[sine(j) for j in range(removed+1,removed+trial+1)]
    signs=[1]*len(even)+[-1]*len(odd)+[(-1)**(j+1) for j in range(removed+1,removed+trial+1)]
    return even+odd+high,signs,len(even),len(odd)


def build(trial=100,removed=5,bits=256,return_internal=False):
    began=time.monotonic();ctx.prec=bits
    source=Source();funcs,signs,ne,no=basis(trial,removed)
    dim=ne+no;n=len(funcs)
    q=arb_mat(n,n);g=arb_mat(n,n)
    checked_cross=0
    for i in range(n):
        for j in range(i,n):
            qv=acb(0);gv=acb(0)
            for a,ca in funcs[i]:
                for z,cz in funcs[j]:
                    qv+=ca*cz*source.double(a,z)
                    zero=a[0]==z[0] and a[1]+z[1]==0
                    az=source.val((a[0],a[1]+z[1])) if a[0]==z[0] else source.val(a)+source.val(z)
                    gv+=ca*cz*f(az,zero)
            require(qv.imag.contains(0) and gv.imag.contains(0),'real native test forms')
            if signs[i]!=signs[j]:
                require(qv.real.contains(0) and gv.real.contains(0),'literal source cross-parity zero control')
                checked_cross+=1
            else:
                q[i,j]=q[j,i]=source.b*qv.real
                g[i,j]=g[j,i]=gv.real
    ei=range(dim);hi=range(dim,n)
    orth=cholesky(block(g,ei,ei)).transpose().inv()
    qee=orth.transpose()*block(q,ei,ei)*orth
    if trial:
        constraints=orth.transpose()*block(g,ei,hi)
        qeh=orth.transpose()*block(q,ei,hi)
        qvv=(block(q,hi,hi)-constraints.transpose()*qeh-qeh.transpose()*constraints
             +constraints.transpose()*qee*constraints)
        qve=qeh.transpose()-constraints.transpose()*qee
        positive_ldl(qvv)
        corrections=qvv.solve(qve)
        u=qee-qve.transpose()*corrections
        top=orth*(identity(dim)+constraints*corrections)
        coeff=arb_mat(n,dim)
        for i in range(dim):
            for j in range(dim):coeff[i,j]=top[i,j]
        for i in range(trial):
            for j in range(dim):coeff[i+dim,j]=-corrections[i,j]
    else:
        u=qee;coeff=orth
    u=(u+u.transpose())/2
    for i in range(ne):
        for j in range(ne,dim):
            require(u[i,j].contains(0),'finite U reflection control')
            u[i,j]=u[j,i]=0
    pivots=positive_ldl(u,arb('1e-12'))
    result={'status':'CENTERED_DIRECTED_U_ONLY_ACCEPT',
      'scope':'literal finite Galerkin U; continuum effective sign not certified',
      'length':'1','removed_sine_modes':removed,'trial_modes':trial,
      'precision_bits':bits,'python_flint_version':flint.__version__,
      'even_dimension':ne,'odd_dimension':no,'complement_dimension':dim,
      'certified_U_lower_eigenvalue':'1e-12','checked_literal_cross_entries':checked_cross,
      'basis_parities':signs,
      'exact_basis_coefficients_balls':[[{'key':list(k),'real':c.real.str(65,more=True),
          'imag':c.imag.str(65,more=True)} for k,c in row] for row in funcs],
      'exact_trial_z_coefficients_balls':[[coeff[i,j].str(65,more=True) for j in range(dim)] for i in range(n)],
      'U_matrix_balls':[[u[i,j].str(65,more=True) for j in range(dim)] for i in range(dim)],
      'shifted_LDL_pivots':[x.str(65,more=True) for x in pivots],
      'literal_transform_source_sha256':hashlib.sha256(Path(__file__).with_name('enclose_analytic_upper.py').read_bytes()).hexdigest(),
      'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'elapsed_seconds':time.monotonic()-began}
    return (result,u,coeff,funcs,signs,source) if return_internal else result


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--trial',type=int,default=100)
    p.add_argument('--removed',type=int,default=5);p.add_argument('--bits',type=int,default=256)
    p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    result=build(a.trial,a.removed,a.bits)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in
      ['exact_basis_coefficients_balls','exact_trial_z_coefficients_balls','U_matrix_balls','basis_parities']},indent=2))
