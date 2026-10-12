#!/usr/bin/env python3
"""Exact physical-coordinate source controls; not a continuum sign checker."""
import hashlib,json
from pathlib import Path
from flint import arb,acb,ctx
from physical_length_source import PhysicalSource,LengthSource,OLD,projection_gram
from enclose_analytic_upper import f,fp,require,positive_ldl
from source_convolution import ConvolutionSource

def close(a,b,label):require(a.overlaps(b),label)
def ff(z):return f(z,z.is_zero())

class Synthetic(PhysicalSource):
    def __init__(self):
        self.rate=arb(2);super().__init__();L=self.length
        self.w0=acb(1);self.w1=(-self.rate*L).exp();self.h1=(1-self.w1)/self.rate
    def laplace(self,key):
        z=self.val(key)-self.rate;L=self.length
        return L*ff(z*L),L*L*fp(z*L,z.is_zero())
    def partial(self,key,t,active):
        return t*ff((self.val(key)-self.rate)*t)
    def w(self,t,active):return (-self.rate*t).exp()
    def primitive(self,t,active):return (1-(-self.rate*t).exp())/self.rate
    def independent_coeffs(self,key):
        beta=self.val(key);a=self.rate;L=self.length
        return [(beta,1/(a+beta)-1/(beta-a)),(-a,-1/(a+beta)),(a,((beta-a)*L).exp()/(beta-a))]
    def independent_f(self,key,t):
        ans=acb(0)
        for r,k in self.independent_coeffs(key):ans+=k*((-r+1/(4*r))*(r*t).exp()-1/(4*r))
        return ans
    def independent_moment(self,key,test):
        L=self.length
        def ex(alpha):
            ans=acb(0)
            for r,k in self.independent_coeffs(key):
                ans+=k*((-r+1/(4*r))*L*ff((r+alpha)*L)-L*ff(alpha*L)/(4*r))
            return ans
        if test==0:return ex(acb(0))
        if test=='sinh':return (ex(acb(self.b))-ex(acb(-self.b)))/2
        alpha=acb(0,arb.pi()*test/L)
        return (ex(alpha)+ex(-alpha))/2

def run():
    ctx.prec=256;s=PhysicalSource();baseline=LengthSource(s.length)
    keys=[('r',k) for k in[-3,-1,0,1,3]]+[('i',k) for k in[1,7,8,107]]
    transforms=0
    for key in keys:
        av,ap=s.laplace(key);bv,bp=baseline.laplace(key)
        close(av,bv,('literal full transform',key));close(ap,bp,('literal full derivative',key));transforms+=2
    gamma=0
    for key in [('r',-3),('r',3),('i',1),('i',7),('i',107)]:
        for x in [arb(1)/10000,arb(1)/100,arb(1)/10,arb(3)/10]:
            a=s.gamma_incomplete(key,acb(x));b=ConvolutionSource.gamma_incomplete(s,key,acb(x))
            close(a,b,('complete gamma Taylor/native control',key,str(x)));gamma+=1
    synthetic=Synthetic();point_count=moment_count=0
    for key in [('r',-3),('r',-1),('r',1),('r',3),('i',1),('i',7),('i',107)]:
        for t,endpoint in[(arb(0),0),(s.length/5,None),(s.length/2,None),(s.length*4/5,None),(s.length,1)]:
            close(synthetic.beta_f(key,acb(t),False,False,endpoint),synthetic.independent_f(key,t),('independent exponential kernel F',key,str(t)));point_count+=1
        for test in[0,1,7,8,128,'sinh']:
            close(synthetic.moment(key,test),synthetic.independent_moment(key,test),('independent exponential kernel moment',key,test));moment_count+=1
    gram=projection_gram(7,s);positive_ldl(gram)
    require(arb.pi()*107/s.length<arb.pi()*111,'reviewed Taylor frequency cap')
    return {'status':'DIRECTED_LITERAL_AND_INDEPENDENT_ALGEBRA_CONTROLS_PASS','precision_bits':256,'exact_length':'21/20',
      'complete_literal_transform_and_derivative_controls':transforms,'complete_gamma_taylor_hypergeometric_controls':gamma,
      'independent_synthetic_exponential_kernel_F_controls':point_count,'independent_synthetic_moment_controls':moment_count,
      'projection_gram_dimension':9,'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'physical_adapter_sha256':hashlib.sha256(Path(__file__).with_name('physical_length_source.py').read_bytes()).hexdigest(),
      'not_proved':['fullR sign','source primitive second replay','all windows','RH']}

if __name__=='__main__':print(json.dumps(run(),indent=2))
