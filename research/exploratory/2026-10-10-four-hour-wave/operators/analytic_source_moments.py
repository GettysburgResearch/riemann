#!/usr/bin/env python3
"""Directed literal F moments via complete source Laplace transforms only.

No quadrature. Mathematical derivation is in WEIGHTED_PRIMITIVE_RESIDUAL.md.
Independent review remains required before scientific acceptance.
"""
import argparse,hashlib,json,time
from pathlib import Path
from flint import arb,acb,arb_mat,ctx
from enclose_analytic_upper import Source,build,require
from enclose_residual import projection_gram


class MomentSource(Source):
    def fmoment(self,beta,test):
        z=self.val(beta)
        tz,_=self.laplace(beta)
        tmz,_=self.laplace((beta[0],-beta[1]))
        k0=tz;k1=z.exp()*tmz
        d0=self.double(('r',0),beta)
        if test==0:
            t0,tp0=self.laplace(('r',0))
            da=(z.exp()*(t0+tmz-tp0)-tp0-d0)/z
            return k0-k1+arb(1)/4*(d0-da)
        if isinstance(test,int):
            nu=arb.pi()*test
            ds=(self.double(('i',test),beta)-self.double(('i',-test),beta))/(2*acb(0,1))
            return k0-(-1)**test*k1-(nu+arb(1)/(4*nu))*ds
        require(test=='sinh','known real test moment')
        def expmoment(sign):
            alpha=self.val(('r',3*sign))
            return k0-alpha.exp()*k1+(alpha-arb(1)/(4*alpha))*self.double(('r',3*sign),beta)+arb(1)/(4*alpha)*alpha.exp()*d0
        return (expmoment(1)-expmoment(-1))/2

    def basis_moment(self,test,removed,trial):
        sins=[self.fmoment(('i',j),test).imag for j in range(1,removed+trial+1)]
        ep=self.fmoment(('r',1),test);em=self.fmoment(('r',-1),test)
        ch=(self.fmoment(('r',3),test)+self.fmoment(('r',-3),test))/2
        require(ep.imag.contains(0) and em.imag.contains(0) and ch.imag.contains(0),'real exponential moment symmetry')
        return sins[:removed]+[ep.real,em.real,ch.real]+sins[removed:]


def moments(removed=11,trial=100,bits=256,last=128):
    began=time.monotonic();ctx.prec=bits
    receipt,u,coeff=build(trial,removed,bits,True)
    source=MomentSource()
    tests=list(range(last+1))+['sinh']
    fc=arb_mat([source.basis_moment(test,removed,trial) for test in tests])*coeff
    fp=arb_mat([[fc[i,j] for j in range(coeff.ncols())] for i in list(range(removed+1))+[last+1]])
    gram=projection_gram(removed,source)
    proj=gram.solve(fp)
    protected=arb_mat(last-removed,coeff.ncols())
    for n in range(removed+1,last+1):
        cross=source.b*((-1)**n*source.b.cosh()-1)/(source.b**2+(arb.pi()*n)**2)
        for j in range(coeff.ncols()):
            protected[n-removed-1,j]=fc[n,j]-cross*proj[removed+1,j]
    result={'status':'DIRECTED_SOURCE_MOMENTS_PENDING_ANALYTIC_REVIEW','removed_sine_modes':removed,
       'trial_modes':trial,'last_cosine_mode':last,'precision_bits':bits,
       'projection_F_moment_balls':[[fp[i,j].str(55,more=True) for j in range(fp.ncols())] for i in range(fp.nrows())],
       'protected_high_cosine_moment_balls':[[protected[i,j].str(55,more=True) for j in range(protected.ncols())] for i in range(protected.nrows())],
       'source_U_receipt':receipt,'elapsed_seconds':time.monotonic()-began,
       'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'not_proved':['continuum FF integral','effective sign','all windows','RH']}
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--removed',type=int,default=11);p.add_argument('--trial',type=int,default=100)
    p.add_argument('--bits',type=int,default=256);p.add_argument('--last',type=int,default=128);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();r=moments(a.removed,a.trial,a.bits,a.last);a.out.write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({k:v for k,v in r.items() if k not in ['source_U_receipt','projection_F_moment_balls','protected_high_cosine_moment_balls']},indent=2))
