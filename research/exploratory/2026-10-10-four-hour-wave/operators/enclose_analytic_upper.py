#!/usr/bin/env python3
"""Directed full-source finite Galerkin upper enclosure using Arb balls.

The exact source integrals are analytic, with the complete gamma rational tail
and a proven exponential-series remainder.  This does NOT prove S>=0: U is an
upper bound.  Install python-flint==0.8.0 and run with its module path available.
"""

import argparse
import hashlib
import json
from pathlib import Path
import time

import flint
from flint import arb, acb, arb_mat, acb_series, ctx


def require(condition, detail):
    if not condition:
        raise ArithmeticError(detail)


def block(a, rows, cols):
    return arb_mat([[a[i,j] for j in cols] for i in rows])


def identity(n):
    return arb_mat([[int(i==j) for j in range(n)] for i in range(n)])


def transpose(a):
    return a.transpose()


def cholesky(a):
    n=a.nrows()
    out=arb_mat(n,n)
    for i in range(n):
        for j in range(i+1):
            val=a[i,j]-sum((out[i,k]*out[j,k] for k in range(j)),arb(0))
            if i==j:
                require(val>0, ('positive Cholesky pivot',i,str(val)))
                out[i,j]=val.sqrt()
            else:
                out[i,j]=val/out[j,j]
    return out


def positive_ldl(a, shift=arb(0)):
    n=a.nrows()
    l=identity(n)
    d=[]
    for i in range(n):
        di=a[i,i]-shift-sum((l[i,k]*l[i,k]*d[k] for k in range(i)),arb(0))
        require(di>0, ('strict positive LDL pivot',i,str(di)))
        d.append(di)
        for j in range(i+1,n):
            val=a[j,i]-sum((l[j,k]*l[i,k]*d[k] for k in range(i)),arb(0))
            l[j,i]=val/di
    return d


def f(z, zero=False):
    # Entire identity also covers an interval argument containing zero.
    return acb(1) if zero else (z/2).exp()*(acb(0,1)*z/2).sinc()


def fp(z, zero=False):
    return acb(arb(1)/2) if zero else (z.exp()*(z-1)+1)/(z*z)


class Source:
    def __init__(self, exponential_terms=50):
        self.b=arb(3)/2
        self.cb=(1-arb.const_euler()-(2*arb.pi()).log())/3
        zetajet=acb_series([2,1],prec=2).zeta()
        self.p2=(-zetajet[1]/zetajet[0]).real
        require(self.p2>0,'positive completed prime constant')
        self.log2=arb(2).log()
        self.q2=self.log2/arb(2).sqrt()
        self.terms=exponential_terms
        self.gb=acb(arb(1)/2).digamma()
        self.gmb=acb(2).digamma()
        self.lp=(self.gb-self.gmb)/(2*self.b)
        self.cache={}
        lam0=2*(exponential_terms+1)+arb(1)/2
        self.gamma_error=(self.b-lam0).exp()/((lam0-self.b)**2*lam0*(1-arb(-2).exp()))
        self.gamma_derivative_error=self.gamma_error*(1+1/(lam0-self.b))

    def val(self,key):
        kind,index=key
        return acb(arb(index)/2) if kind=='r' else acb(0,arb.pi()*index)

    def a(self,z,key):
        b=self.b
        if key==('r',3) or key==('r',-3):
            arg=arb(1)/2 if key[1]==3 else arb(2)
            gp=-acb(arg).polygamma(1)/2
            gpp=acb(arg).polygamma(2)/4
            if key[1]==3:
                return -(gp-self.lp)/(4*b),-gpp/(8*b)+(gp-self.lp)/(8*b*b)
            return (gp-self.lp)/(4*b),gpp/(8*b)+(gp-self.lp)/(8*b*b)
        gv=(acb(arb(5)/4)-z/2).digamma()
        gp=-(acb(arb(5)/4)-z/2).polygamma(1)/2
        linear=((z+b)*self.gb+(b-z)*self.gmb)/(2*b)
        den=z*z-b*b
        return -(gv-linear)/(2*den),-(gp-self.lp)/(2*den)+(gv-linear)*z/(den*den)

    def segment(self,z,zero=False):
        d=self.log2
        width=1-d
        fv=f(z*width,zero)
        value=(z*d).exp()*width*fv
        deriv=(z*d).exp()*(width*d*fv+width*width*fp(z*width,zero))
        return value,deriv

    def laplace(self,key):
        if key in self.cache:
            return self.cache[key]
        z=self.val(key)
        b=self.b
        av,ap=self.a(z,key)
        expo=acb(0)
        expop=acb(0)
        for j in range(1,self.terms+1):
            lam=2*j+arb(1)/2
            base=(-lam).exp()/(lam*lam-b*b)
            expo+=base/(lam-z)
            expop+=base/(lam-z)**2
        delta=arb(0,self.gamma_error.upper())
        deltap=arb(0,self.gamma_derivative_error.upper())
        gv=av-z.exp()*expo+acb(delta,delta)
        gp=ap-z.exp()*(expo+expop)+acb(deltap,deltap)
        zero_plus=key==('r',-3)
        zero_minus=key==('r',3)
        zero_c=key==('r',-1)
        value=f(z+arb(1)/2,zero_c)/2+self.cb*f(z-b,zero_minus)+gv
        value-=self.p2*(f(z+b,zero_plus)+f(z-b,zero_minus))/(2*b)
        deriv=fp(z+arb(1)/2,zero_c)/2+self.cb*fp(z-b,zero_minus)+gp
        deriv-=self.p2*(fp(z+b,zero_plus)+fp(z-b,zero_minus))/(2*b)
        sp,spp=self.segment(z+b,zero_plus)
        sm,smp=self.segment(z-b,zero_minus)
        value+=self.q2*((-b*self.log2).exp()*sp-(b*self.log2).exp()*sm)/(2*b)
        deriv+=self.q2*((-b*self.log2).exp()*spp-(b*self.log2).exp()*smp)/(2*b)
        require(value.is_finite() and deriv.is_finite(),('finite primitive Laplace enclosure',key))
        self.cache[key]=value,deriv
        return value,deriv

    def double(self,alpha,beta):
        ta,tpa=self.laplace(alpha)
        tb,tpb=self.laplace(beta)
        if alpha[0]==beta[0] and alpha[1]+beta[1]==0:
            return ta+tb-tpa-tpb
        tma,_=self.laplace((alpha[0],-alpha[1]))
        tmb,_=self.laplace((beta[0],-beta[1]))
        if alpha[0]==beta[0]:
            s=self.val((alpha[0],alpha[1]+beta[1]))
        else:
            s=self.val(alpha)+self.val(beta)
        return (s.exp()*(tma+tmb)-ta-tb)/s


def basis(trial,removed):
    out=[]
    for j in range(1,removed+1):
        out.append([(('i',j),acb(0,-arb(1)/2)),(('i',-j),acb(0,arb(1)/2))])
    out.extend([[ (('r',1),acb(1)) ],[(('r',-1),acb(1))],
                [(('r',3),acb(arb(1)/2)),(('r',-3),acb(arb(1)/2))]])
    for j in range(removed+1,removed+trial+1):
        out.append([(('i',j),acb(0,-arb(1)/2)),(('i',-j),acb(0,arb(1)/2))])
    return out


def build(trial=100,removed=15,bits=192,return_internal=False):
    began=time.monotonic()
    ctx.prec=bits
    source=Source()
    funcs=basis(trial,removed)
    n=len(funcs)
    q=arb_mat(n,n)
    gram=arb_mat(n,n)
    for i in range(n):
        for j in range(i,n):
            qv=acb(0)
            gv=acb(0)
            for a,ca in funcs[i]:
                for b,cb in funcs[j]:
                    qv+=ca*cb*source.double(a,b)
                    zero=a[0]==b[0] and a[1]+b[1]==0
                    z=source.val((a[0],a[1]+b[1])) if a[0]==b[0] else source.val(a)+source.val(b)
                    gv+=ca*cb*f(z,zero)
            require(qv.imag.contains(0) and gv.imag.contains(0),'real symmetry enclosure')
            q[i,j]=q[j,i]=source.b*qv.real
            gram[i,j]=gram[j,i]=gv.real
    dim=removed+3
    ei=range(dim)
    hi=range(dim,n)
    gee=block(gram,ei,ei)
    orth=transpose(cholesky(gee)).inv()
    qee=transpose(orth)*block(q,ei,ei)*orth
    if trial:
        constraints=transpose(orth)*block(gram,ei,hi)
        qeh=transpose(orth)*block(q,ei,hi)
        qvv=(block(q,hi,hi)-transpose(constraints)*qeh-transpose(qeh)*constraints
             +transpose(constraints)*qee*constraints)
        qve=transpose(qeh)-transpose(constraints)*qee
        corrections=qvv.solve(qve)
        u=qee-transpose(qve)*corrections
        top=orth*(identity(dim)+constraints*corrections)
        zcoeff=arb_mat(n,dim)
        for i in range(dim):
            for j in range(dim):
                zcoeff[i,j]=top[i,j]
        for i in range(trial):
            for j in range(dim):
                zcoeff[i+dim,j]=-corrections[i,j]
    else:
        u=qee
        zcoeff=orth
    # Symmetric exact matrix is enclosed by either independent off-diagonal ball;
    # their arithmetic average still encloses that same exact entry.
    u=(u+transpose(u))/2
    pivots=positive_ldl(u,arb('1e-10'))
    result={
        'status':'DIRECTED_FULL_SOURCE_UPPER_ENCLOSURE_ACCEPT',
        'arithmetic':'Arb outward real/complex ball operations',
        'python_flint_version':flint.__version__,
        'precision_bits':bits,
        'gamma_exponential_terms':source.terms,
        'gamma_complete_remainder_upper':source.gamma_error.upper().str(45,more=True),
        'complement_dimension':dim,
        'removed_sine_modes':removed,
        'trial_modes':trial,
        'certified_U_lower_eigenvalue':'1e-10',
        'U_matrix_balls':[[u[i,j].str(45,more=True) for j in range(dim)] for i in range(dim)],
        'exact_trial_z_coefficients_balls':[[zcoeff[i,j].str(45,more=True) for j in range(dim)] for i in range(n)],
        'shifted_LDL_pivots':[d.str(45,more=True) for d in pivots],
        'elapsed_seconds':time.monotonic()-began,
        'scope':'finite Galerkin U only; U is an upper enclosure of the continuum effective S',
        'not_proved':['R continuum enclosure','U-(15/8)R positivity','S positivity','all-window positivity','RH'],
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    return (result,u,zcoeff) if return_internal else result


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--trial-modes',type=int,default=100)
    p.add_argument('--removed',type=int,default=15)
    p.add_argument('--bits',type=int,default=192)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    result=build(args.trial_modes,args.removed,args.bits)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['U_matrix_balls','shifted_LDL_pivots','exact_trial_z_coefficients_balls']},indent=2))
