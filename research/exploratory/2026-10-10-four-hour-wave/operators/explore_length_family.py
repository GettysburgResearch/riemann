#!/usr/bin/env python3
"""Directed analytic U and ordinary sampled R for the exact X2 length family.

Only U is directed. Neither sampled R nor weighted lower eigenvalues certify
an effective sign. Length must lie between1 andlog3 for this model.
"""
import argparse,json,math,time
from pathlib import Path
import numpy as np
from scipy.special import roots_legendre
from scipy.linalg import qr
from flint import arb,acb,arb_mat,ctx
from enclose_analytic_upper import Source,f,fp,basis,require,block,transpose,cholesky,identity,positive_ldl
from explore_effective import kernel,primitive,B,C2


class LengthSource(Source):
    def __init__(self,length):
        self.length=length
        super().__init__()
        lam0=2*(self.terms+1)+arb(1)/2
        self.gamma_error=((self.b-lam0)*length).exp()/((lam0-self.b)**2*lam0*(1-(-2*length).exp()))
        self.gamma_derivative_error=self.gamma_error*(length+1/(lam0-self.b))

    def val(self,key):
        return acb(arb(key[1])/2) if key[0]=='r' else acb(0,arb.pi()*key[1]/self.length)

    def laplace(self,key):
        if key in self.cache:return self.cache[key]
        z=self.val(key);b=self.b;L=self.length
        av,ap=self.a(z,key);expo=acb(0);expop=acb(0)
        for j in range(1,self.terms+1):
            lam=2*j+arb(1)/2;base=(-lam*L).exp()/(lam*lam-b*b)
            expo+=base/(lam-z);expop+=base/(lam-z)**2
        delta=arb(0,self.gamma_error.upper());deltap=arb(0,self.gamma_derivative_error.upper())
        gv=av-(z*L).exp()*expo+acb(delta,delta)
        gp=ap-(z*L).exp()*(L*expo+expop)+acb(deltap,deltap)
        zp=key==('r',-3);zm=key==('r',3);zc=key==('r',-1)
        value=L*f((z+arb(1)/2)*L,zc)/2+self.cb*L*f((z-b)*L,zm)+gv
        value-=self.p2*L*(f((z+b)*L,zp)+f((z-b)*L,zm))/(2*b)
        deriv=L*L*fp((z+arb(1)/2)*L,zc)/2+self.cb*L*L*fp((z-b)*L,zm)+gp
        deriv-=self.p2*L*L*(fp((z+b)*L,zp)+fp((z-b)*L,zm))/(2*b)
        width=L-self.log2;factor=(z*self.log2).exp()*width
        vplus=f((z+b)*width,zp);vminus=f((z-b)*width,zm)
        value+=self.q2*factor*(vplus-vminus)/(2*b)
        deriv+=self.q2*factor*(self.log2*(vplus-vminus)+width*(fp((z+b)*width,zp)-fp((z-b)*width,zm)))/(2*b)
        require(value.is_finite() and deriv.is_finite(),'finite length-family transform')
        self.cache[key]=value,deriv;return value,deriv

    def double(self,alpha,beta):
        ta,tpa=self.laplace(alpha);tb,tpb=self.laplace(beta)
        if alpha[0]==beta[0] and alpha[1]+beta[1]==0:return self.length*(ta+tb)-tpa-tpb
        tma,_=self.laplace((alpha[0],-alpha[1]));tmb,_=self.laplace((beta[0],-beta[1]))
        s=self.val((alpha[0],alpha[1]+beta[1])) if alpha[0]==beta[0] else self.val(alpha)+self.val(beta)
        return ((s*self.length).exp()*(tma+tmb)-ta-tb)/s


def build_length(length,removed=7,trial=100):
    source=LengthSource(length);funcs=basis(trial,removed);n=len(funcs);dim=removed+3
    q=arb_mat(n,n);gram=arb_mat(n,n)
    for i in range(n):
        for j in range(i,n):
            qv=acb(0);gv=acb(0)
            for a,ca in funcs[i]:
                for beta,cb in funcs[j]:
                    qv+=ca*cb*source.double(a,beta)
                    zero=a[0]==beta[0] and a[1]+beta[1]==0
                    z=source.val((a[0],a[1]+beta[1])) if a[0]==beta[0] else source.val(a)+source.val(beta)
                    gv+=ca*cb*length*f(z*length,zero)
            require(qv.imag.contains(0) and gv.imag.contains(0),'real length-family matrix symmetry')
            q[i,j]=q[j,i]=source.b*qv.real;gram[i,j]=gram[j,i]=gv.real
    ei=range(dim);hi=range(dim,n);orth=transpose(cholesky(block(gram,ei,ei))).inv()
    qee=transpose(orth)*block(q,ei,ei)*orth
    constraints=transpose(orth)*block(gram,ei,hi);qeh=transpose(orth)*block(q,ei,hi)
    qvv=block(q,hi,hi)-transpose(constraints)*qeh-transpose(qeh)*constraints+transpose(constraints)*qee*constraints
    qve=transpose(qeh)-transpose(constraints)*qee;correction=qvv.solve(qve)
    u=qee-transpose(qve)*correction;u=(u+u.transpose())/2
    top=orth*(identity(dim)+constraints*correction);coeff=arb_mat(n,dim)
    for i in range(dim):
        for j in range(dim):coeff[i,j]=top[i,j]
    for i in range(trial):
        for j in range(dim):coeff[i+dim,j]=-correction[i,j]
    try:
        pivots=positive_ldl(u,arb('1e-10'))
    except ArithmeticError:
        pivots=[]
    return source,u,coeff,pivots


def sampled_lower(length,u,coeff,removed,trial,order):
    L=float(length.mid());coef=np.array([[float(coeff[i,j].mid()) for j in range(coeff.ncols())] for i in range(coeff.nrows())])
    unum=np.array([[float(u[i,j].mid()) for j in range(u.ncols())] for i in range(u.nrows())])
    x,w=roots_legendre(order);t=L*(x+1)/2;w*=L/2;low=np.arange(1,removed+1);high=np.arange(removed+1,removed+trial+1)
    def sins(m):return np.sin(np.pi*t[:,None]*m/L)
    def dsins(m):return np.pi*m/L*np.cos(np.pi*t[:,None]*m/L)
    zbase=np.column_stack((sins(low),np.exp(t/2),np.exp(-t/2),np.cosh(B*t),sins(high)))
    zpbase=np.column_stack((dsins(low),.5*np.exp(t/2),-.5*np.exp(-t/2),B*np.sinh(B*t),dsins(high)))
    z0=np.r_[np.zeros(removed),[1,1,1],np.zeros(trial)]@coef
    z1=np.r_[np.zeros(removed),[np.exp(L/2),np.exp(-L/2),np.cosh(B*L)],np.zeros(trial)]@coef
    kmat=kernel(t[:,None]-t)*w[None,:]
    ff=-kernel(t)[:,None]*z0+kernel(t-L)[:,None]*z1-kmat@(zpbase@coef);del kmat
    intk=(primitive(t[:,None]-t)+primitive(t)[None,:])*w[None,:]
    ff+=C2*(intk@(zbase@coef));del intk
    p=np.column_stack((np.ones(order),np.cos(np.pi*t[:,None]*low/L),np.sinh(B*t)))
    qp,_=qr(np.sqrt(w)[:,None]*p,mode='economic');rf=np.sqrt(w)[:,None]*ff;rf-=qp@(qp.T@rf)
    r=rf.T@rf
    # The reviewed uniform family gap1/2 gives scalarcost9/2.
    eigen=np.linalg.eigvalsh((unum+unum.T)/2-4.5*r)
    return {'sampled_scalar_lower_eigenvalues':eigen.tolist(),'sampled_R_matrix':r.tolist(),'sampled_R_operator_norm':float(np.linalg.norm(r,2)),
            'limitations':['ordinary sampledR','unenclosedcusp quadrature','directed balls replacedbyfloatmidpoints']}


def run(kind,out,order=2000):
    ctx.prec=256;start=time.monotonic();length=arb(21)/20 if kind=='21/20' else arb(3).log()
    source,u,coeff,pivots=build_length(length)
    model=sampled_lower(length,u,coeff,7,100,order)
    result={'status':'DIRECTED_U_AND_SAMPLED_LOWER_NOT_FULL_SIGN_CERTIFICATE','exact_length':kind,'length_ball':length.str(45,more=True),
      'removed_sines':7,'complement_dimension':10,'trial_modes':100,'precision_bits':256,'ordinary_quadrature_order':order,
      'directed_U_eigenvalue_lower':'1e-10' if pivots else None,'U_matrix_balls':[[u[i,j].str(55,more=True) for j in range(10)] for i in range(10)],
      'exact_trial_z_coefficients_balls':[[coeff[i,j].str(55,more=True) for j in range(10)] for i in range(coeff.nrows())],
      'shifted_U_LDL_pivots':[x.str(45,more=True) for x in pivots],**model,'elapsed_seconds':time.monotonic()-start,
      'not_proved':['directedR','weighted lower','uniformeffectiveblock','allwindows','RH']}
    out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['U_matrix_balls','exact_trial_z_coefficients_balls','sampled_R_matrix','shifted_U_LDL_pivots']},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--length',choices=['21/20','log3'],default='log3');p.add_argument('--order',type=int,default=2000);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();run(a.length,a.out,a.order)
