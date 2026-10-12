#!/usr/bin/env python3
"""Ordinary weighted-lower discovery in the uniform log3 family; never certified."""
import argparse,json
from pathlib import Path
import numpy as np
from flint import arb,acb,arb_mat,ctx
from explore_length_family import LengthSource,build_length
from enclose_analytic_upper import require


class LengthMomentSource(LengthSource):
    def moment(self,key,test):
        beta=self.val(key);L=self.length
        tb,_=self.laplace(key);tmb,_=self.laplace((key[0],-key[1]));k0=tb;kL=(beta*L).exp()*tmb
        d0=self.double(('r',0),key)
        if test==0:
            t0,tp0=self.laplace(('r',0))
            da=((beta*L).exp()*(L*(t0+tmb)-tp0)-tp0-d0)/beta
            return k0-kL+arb(1)/4*(L*d0-da)
        if isinstance(test,int):
            nu=arb.pi()*test/L
            ds=(self.double(('i',test),key)-self.double(('i',-test),key))/(2*acb(0,1))
            return k0-(-1)**test*kL-(nu+arb(1)/(4*nu))*ds
        require(test=='sinh','known length-family moment')
        def ex(sign):
            a=self.val(('r',3*sign));e=(a*L).exp()
            return k0-e*kL+(a-arb(1)/(4*a))*self.double(('r',3*sign),key)+arb(1)/(4*a)*e*d0
        return(ex(1)-ex(-1))/2

    def basis_moment(self,test,removed,trial):
        sin=[self.moment(('i',j),test).imag for j in range(1,removed+trial+1)]
        ep=self.moment(('r',1),test).real;em=self.moment(('r',-1),test).real
        ch=(self.moment(('r',3),test).real+self.moment(('r',-3),test).real)/2
        return sin[:removed]+[ep,em,ch]+sin[removed:]


def run(path,last=128):
    ctx.prec=256;data=json.loads(path.read_text());kind=data['exact_length'];L=arb(21)/20 if kind=='21/20' else arb(3).log()
    source,u,coef,pivots=build_length(L);m=data['removed_sines'];trial=data['trial_modes'];dim=m+3
    source=LengthMomentSource(L);tests=list(range(last+1))+['sinh']
    fc=arb_mat([source.basis_moment(test,m,trial) for test in tests])*coef
    pp=arb_mat([[fc[i,j] for j in range(dim)] for i in list(range(m+1))+[last+1]])
    g=arb_mat(m+2,m+2);g[0,0]=L
    for j in range(1,m+1):g[j,j]=L/2
    g[0,m+1]=g[m+1,0]=((source.b*L).cosh()-1)/source.b
    for j in range(1,m+1):
        cross=source.b*((-1)**j*(source.b*L).cosh()-1)/(source.b**2+(arb.pi()*j/L)**2)
        g[j,m+1]=g[m+1,j]=cross
    g[m+1,m+1]=(2*source.b*L).sinh()/(4*source.b)-L/2
    projection=g.solve(pp)
    protected=arb_mat(last-m,dim)
    for n in range(m+1,last+1):
        cross=source.b*((-1)**n*(source.b*L).cosh()-1)/(source.b**2+(arb.pi()*n/L)**2)
        for j in range(dim):protected[n-m-1,j]=fc[n,j]-cross*projection[m+1,j]
    fl=float(L.mid());r=np.array(data['sampled_R_matrix']);un=np.array([[float(u[i,j].mid()) for j in range(dim)] for i in range(dim)])
    tail=1/(.8-244*(fl/((last+1)*np.pi))**2)
    cost=1.5*tail*r
    for n in range(m+1,last+1):
        row=np.array([float(protected[n-m-1,j].mid()) for j in range(dim)])
        cost+=3/fl*(1/(.8-244*(fl/(n*np.pi))**2)-tail)*np.outer(row,row)
    return {'status':'EMPIRICAL_WEIGHTED_LENGTH_NOT_CERTIFIED','exact_length':kind,'removed_sines':m,
       'last_cosine_mode':last,'weighted_lower_eigenvalues':np.linalg.eigvalsh((un+un.T)/2-cost).tolist(),
       'U_eigenvalues_ordinary':np.linalg.eigvalsh(un).tolist(),'quadrature_order':data['ordinary_quadrature_order'],
       'limitations':['Rordinarycuspquadrature','directedmomentsconvertedtofloat','generalizedformulasauditpending'],
       'not_proved':['nativeeffective sign','lengthintervalsign','RH']}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('input',type=Path);p.add_argument('--last',type=int,default=128);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();r=run(a.input,a.last);a.out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
