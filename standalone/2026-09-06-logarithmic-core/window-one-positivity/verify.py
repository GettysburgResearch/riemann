#!/usr/bin/env python3
"""Verify an all-functions, length-one arithmetic positivity certificate.
No floats, optimizer, zero table, external numerical library, or parent
producer is imported. Infinite passages are proved in PROOF.md.
"""
from fractions import Fraction as Q
from pathlib import Path
import json,sys,hashlib,time
from intervals import I,PI,LOG2,GAMMA,CB,P2,exp_i,sincos,cos_i,sinh,cosh,psi_real,S,BITS
ROOT=Path(__file__).resolve().parent
b=I(Q(3,2));c=I(Q(1,2));d=LOG2
q=LOG2/exp_i(LOG2/2)

def reject_pairs(pairs):
    out={}
    for k,v in pairs:
        if k in out:raise ValueError('duplicate JSON key')
        out[k]=v
    return out

def strict_equal(a,b):
    if type(a) is not type(b):return False
    if isinstance(a,dict):return set(a)==set(b) and all(strict_equal(a[k],b[k]) for k in a)
    if isinstance(a,list):return len(a)==len(b) and all(strict_equal(x,y) for x,y in zip(a,b))
    return a==b

def rational(s):
    if type(s) is not str:raise TypeError('rational string required')
    return Q(s)

def load(path):
    cert=json.loads(Path(path).read_text(),object_pairs_hook=reject_pairs)
    keys={'schema','source_interval','half_period','finite_modes','gamma_tail_modes','scaled_margin','frequencies','weights','extension_values','note'}
    if set(cert)!=keys or cert['schema']!='riemann.positive_extension.v1':raise ValueError('schema mismatch')
    if cert['source_interval']!='1' or cert['half_period']!='2':raise ValueError('fixed source interval')
    if type(cert['finite_modes']) is not int or cert['finite_modes']!=2048:raise ValueError('mode denominator')
    if type(cert['gamma_tail_modes']) is not int or cert['gamma_tail_modes']!=1024:raise ValueError('gamma denominator')
    if rational(cert['scaled_margin'])!=Q(1,2**35):raise ValueError('margin contract')
    if len(cert['frequencies'])!=20 or len(cert['weights'])!=20 or len(cert['extension_values'])!=64:raise ValueError('witness dimension')
    freq=list(map(rational,cert['frequencies']));weights=list(map(rational,cert['weights']));vals=list(map(rational,cert['extension_values']))
    if not all(0<x<100 for x in freq) or not all(x>=0 for x in weights):raise ValueError('positive atom range')
    if not all(abs(x)<1 for x in vals):raise ValueError('extension range')
    return cert,freq,weights,vals

F0=I(Q(1,2))+CB-P2/b
F1=exp_i(c)/2+CB*exp_i(-b)-P2/b*cosh(b)+q/b*sinh(b*(1-d))
FP0=c/2-b*CB
FP1=c*exp_i(c)/2-b*CB*exp_i(-b)-P2*sinh(b)+q*cosh(b*(1-d))

# Integrate exp(k*x)*cos(w*x) from0 toL.
def eint(k,L,w,sl=None,cl=None):
    k=I(k);L=I(L)
    if sl is None:sl,cl=sincos(w*L)
    return (exp_i(k*L)*(k*cl+w*sl)-k)/(k*k+w*w)

def f_integral(w):
    sl,cl=sincos(w)
    val=eint(c,1,w,sl,cl)/2+CB*eint(-b,1,w,sl,cl)-P2/(2*b)*(eint(b,1,w,sl,cl)+eint(-b,1,w,sl,cl))
    sd,cd=sincos(w*d)
    val+=q/(2*b)*(exp_i(-b*d)*(eint(b,1,w,sl,cl)-eint(b,d,w,sd,cd))-exp_i(b*d)*(eint(-b,1,w,sl,cl)-eint(-b,d,w,sd,cd)))
    return val

# Gamma source on [0,2]. Partial fraction/digamma identity includes full sum.
def gamma_integral(w,n):
    val=(2*psi_real(Q(5,4),w/2)+2*GAMMA+2*LOG2-1)/(4*(b*b+w*w))
    corr=I(0)
    for j in range(1,33):
        al=I(2*j)+Q(1,2)
        corr+=al*exp_i(-2*al)/((al*al-b*b)*(al*al+w*w))
    corr=corr.widen(Q(1,2**132))
    return val-((-1)**n)*corr

# Exact periodic-grid cosines are evaluated only at 256 residues.
COS=[cos_i(PI*r/128) for r in range(256)]
SIN=[sincos(PI*r/128)[0] for r in range(256)]

def extension_scaled(n,values):
    """w^2 * integral_1^2 of affine extension, for n>0."""
    w=PI*n/2
    slopes=[64*(values[k+1]-values[k]) for k in range(64)]
    # -F1*w*sin(w) + endpoint slopes - interior jumps
    out=-F1*w*SIN[(64*n)%256]+slopes[-1]*((-1)**n)-slopes[0]*COS[(64*n)%256]
    for k in range(1,64):out-=(slopes[k]-slopes[k-1])*COS[((64+k)*n)%256]
    return out

def atom_integral(lam,w,n):
    lam=I(lam)
    # n=0 works too; denominators nonzero for these fixed parameters.
    return ((-1)**n)*lam*sincos(2*lam)[0]/(lam*lam-w*w)

def run(certpath):
    cert,freq,weights,vv=load(certpath)
    if not (0<LOG2.low() and LOG2.high()<1 and exp_i(1).low()>2 and exp_i(1).high()<3):
        raise ValueError('source geometry')
    values=[F1]+list(map(I,vv)); margin=rational(cert['scaled_margin'])
    gamma_calls=0;worst=None;worstn=None;digest=hashlib.sha256()
    for n in range(cert['finite_modes']+1):
        w=PI*n/2
        val=f_integral(w)+gamma_integral(w,n)
        if n==0:val+=sum(((values[k]+values[k+1])/128 for k in range(64)),I(0))
        else:val=val*w*w+extension_scaled(n,values)
        for lam,weight in zip(freq,weights):
            if weight:
                ai=atom_integral(lam,w,n)*weight
                val-=ai if n==0 else ai*w*w
        if val.low()<=margin:raise ValueError(f'finite coefficient failed: n={n}, bounds={val.bounds()}')
        if worst is None or val.low()<worst:worst,worstn=val.low(),n
        digest.update((str(n)+':'+','.join(val.bounds())+'\n').encode())
    # All n>2048: derivative-jump phase depends only on n modulo256.
    slopes=[64*(values[k+1]-values[k]) for k in range(64)]
    atomlim=sum((I(we*lam)*sincos(2*I(lam))[0] for lam,we in zip(freq,weights)),I(0))
    residues=[]
    for r in range(256):
        val=(FP1-slopes[0])*COS[(64*r)%256]-FP0+((-1)**r)*(slopes[-1]+atomlim)
        for k in range(1,64):val-=(slopes[k]-slopes[k-1])*COS[((64+k)*r)%256]
        residues.append(val.low())
    beta=min(residues)
    # pi>3, w>=w0. e>2 bounds gamma exponentials.
    if PI.low()<=3:raise ValueError('pi lower')
    w0=Q(3*(cert['finite_modes']+1),2)
    gamlow=I(0)
    for j in range(1,cert['gamma_tail_modes']+1):
        al=Q(4*j+1,2)
        gamlow+=I(al/(al*al-Q(9,4))*w0*w0/(al*al+w0*w0))*(1-I(Q(1,2**(4*j+1))))
    # The regular F'' integral, after one integration by parts.
    er=c*c/2*exp_i(c)+CB.abs()*b*b*exp_i(-b)+P2*b*cosh(b)+q*b*sinh(b*(1-d))
    er+=c*c/2*(exp_i(c)-1)+CB.abs()*b*b*(1-exp_i(-b))+P2*b*(cosh(b)-1)+q*b*sinh(b*(1-d))
    err=er/w0
    err+=sum((I(we*lam**3/(w0*w0-lam*lam)) for lam,we in zip(freq,weights)),I(0))
    tail=I(gamlow+beta)-q-err
    if tail.low()<=Q(2,5):raise ValueError('all-frequency tail failed')
    return {'schema':'riemann.window1.verified.v1','rh_proved':False,'source_window':'1','full_source_positivity':True,'finite_coefficients':2049,'phase_residues':256,'tail_gamma_terms':1024,'scaled_margin':str(margin),'worst_finite_mode':worstn,'worst_finite_lower':str(worst),'all_tail_lower':str(tail.low()),'phase_lower':str(beta),'right_derivative_mismatch':(slopes[0]-FP1).bounds(),'coefficient_digest':digest.hexdigest(),'constant_enclosures':{'pi':PI.bounds(),'gamma':GAMMA.bounds(),'P2':P2.bounds(),'Cb':CB.bounds()},'arithmetic':'192-bit outward dyadic; exact rational analytic remainders','scope':'all complex L2 tests supported in an interval of length at most1; not all window lengths'}

def main():
    cert=ROOT/'certificate.json'
    if '--certificate' in sys.argv:cert=Path(sys.argv[sys.argv.index('--certificate')+1])
    result=run(cert)
    if '--check' in sys.argv:
        expected=json.loads(Path(sys.argv[sys.argv.index('--check')+1]).read_text(),object_pairs_hook=reject_pairs)
        if not strict_equal(result,expected):raise ValueError('result mismatch')
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
