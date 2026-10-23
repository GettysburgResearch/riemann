"""Exact Euler-sum upper bounds for the below-one shifted detector."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib,json,runpy
ENGINE=Path(__file__).resolve().parents[1]/'three-hour-type/verify_logistic_master_fraction.py'
SHA='cefd18641114b6fedd8cf3334bcdd2857da7d4694bbbbc951238603e90fc2413'
if hashlib.sha256(ENGINE.read_bytes()).hexdigest()!=SHA:raise RuntimeError('engine hash')
ns=runpy.run_path(str(ENGINE))
I,check,exp_i,log_point=(ns[k] for k in ('I','check','exp_i','log_point'))

def primes(n):
    sieve=bytearray(b'\x01')*(n+1);sieve[:2]=b'\x00\x00'
    for p in range(2,n+1):
        if sieve[p]:
            yield p
            if p*p<=n:sieve[p*p:n+1:p]=b'\x00'*(((n-p*p)//p)+1)

def main():
    nmax=10000;lam=Q(1,160);sig=1-lam;tweta=1-2*lam;s=2-3*lam
    cs=I(0);zs=I(0);terms=0
    for p in primes(nmax):
        lp=log_point(Q(p));n=p;m=1
        while n<=nmax:
            ln=m*lp
            cs+=lp*exp_i(-sig*ln)/(exp_i(tweta*ln)-1)
            zs+=lp*exp_i(-Q(37,25)*ln)
            n*=p;m+=1;terms+=1
    ln=log_point(Q(nmax))
    # Lambda(n)<=log n. Both continuous majorants decrease past nmax.
    ct=exp_i((1-s)*ln)*(ln/(s-1)+1/(s-1)**2)
    ct/=1-exp_i(-tweta*log_point(Q(nmax+1)))
    zt=exp_i((1-Q(37,25))*ln)*(ln/Q(12,25)+1/Q(12,25)**2)
    check((s*ln).lo>1 and (Q(37,25)*ln).lo>1,'decreasing tails')
    check((cs+ct).hi<Q(9,10),'C(lambda)<.9')
    check((zs+zt).hi<2,'Z(1.48)<2')
    check(cs.lo>Q(4,5) and zs.lo>Q(3,2),'false small bounds rejected')
    out={'status':'PASS','domain':'0<=lambda<=1/160','terms':terms,'cutoff':nmax,
         'C_upper':str((cs+ct).hi),'C_tail_upper':str(ct.hi),
         'Z_37_25_upper':str((zs+zt).hi),'Z_tail_upper':str(zt.hi),
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'engine_sha256':SHA,'negative_controls':2}
    Path(__file__).with_name('SHIFTED_EULER_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
