"""Certify twelve quaternion fields whose integrated harmonic mean is positive on GRH."""
import json
from math import isqrt
from flint import arb,ctx
from check_zhao_cubic_fields_nov18 import run_gp
from check_zhao_field_weight_nov18 import primes_through,weight_bounds

EXAMPLES = [
    ('8.0.12230590464.1', [1, 0, 12, 0, 36, 0, 36, 0, 9]),
    ('8.0.1340095640625.1', [1, -3, 22, -60, 201, -450, 1528, -3069, 4561]),
    ('8.0.7644119040000.1', [1, 0, 60, 0, 900, 0, 4500, 0, 5625]),
    ('8.8.29365647704064.1', [1, 0, -84, 0, 1764, 0, -12348, 0, 21609]),
    ('8.8.47775744000000.2', [1, 0, -60, 0, 810, 0, -1800, 0, 900]),
    ('8.8.74220378765625.1', [1, -3, -63, 90, 1311, -20, -7702, -5524, -1009]),
    ('8.8.101240302206976.2', [1, 0, -68, 0, 986, 0, -4624, 0, 4624]),
    ('8.8.116507435287321.1', [1, -3, -67, -16, 863, 1276, 392, -54, 1]),
    ('8.8.151939915084881.1', [1, -3, -62, 66, 1125, 264, -4982, -4245, 823]),
    ('8.8.179068074983424.2', [1, 0, -132, 0, 4356, 0, -47916, 0, 131769]),
    ('8.8.343064484000000.1', [1, 0, -105, 0, 3465, 0, -44100, 0, 176400]),
    ('8.8.359729184374784.2', [1, 0, -84, 0, 1890, 0, -10584, 0, 1764]),
]


def certify(label,coeff):
    _,r1,d,_=map(int,label.split('.'))
    r2=(8-r1)//2
    p=primes_through(4096)
    pre=(f'K=nfinit(Pol({coeff}));G=galoisinit(K);H=nfsubfields(K,4,1)[1];E=nfinit(H);P={p};\n')
    (order,disc,signature,df,degrees),=run_gp(pre+'print([galoisidentify(G),K.disc,K.sign,E.disc,vector(#P,j,my(v=idealprimedec(K,P[j]));vector(#v,k,v[k].f))]);\n')
    if order!=[8,4] or disc!=d or signature!=[r1,r2] or len(degrees)!=len(p):
        raise ArithmeticError('Quaternion field invariant mismatch')
    q=isqrt(d//df)
    if q*q*df!=d: raise ArithmeticError('Invalid Artin conductor')
    c=2*arb.pi()/arb(q).sqrt()
    N=int(195/float(c))+1
    program=(f'K=nfinit(Pol({coeff}));H=nfsubfields(K,4,1)[1];N={N};\n'
             'A=dirdiv(dirzetak(K,N),dirzetak(nfinit(H),N));v=vector(N);v[1]=1;\n'
             'for(n=2,N,v[n]=(A[n]-sumdiv(n,d,if(d>1 && d<n,v[d]*v[n/d],0)))/2);print(v);\n')
    a,=run_gp(program)
    if len(a)!=N or a[0]!=1: raise ArithmeticError('Incomplete Artin coefficients')
    values=[]
    for t in (arb(1)/2,arb(2)):
        x=c*t
        last=min(N,int(97/float(x))+1)
        if not (last+1)*x>96: raise ArithmeticError('Theta cutoff failed')
        theta=arb(0)
        for n,v in enumerate(a[:last],1):
            if v:
                z=x*n
                theta+=v*z.bessel_k(0)*(z if r2 else 1)
        e=(-x/2).exp()
        tail=2*e**(last+1)*((last+1)-last*e)/(1-e)**2
        values.append(theta+arb(0,tail.upper()))
    if not values[0]*values[1]<0: raise ArithmeticError('Root number unresolved')
    lo,hi=weight_bounds(d,r1,r2,4096,dict(zip(p,degrees)))
    if not hi<18: raise ArithmeticError('Noncentral weight unresolved')
    return {'label':label,'conductor':q,'theta_checks':list(map(str,values)),
            'spectral_lower':str(lo),'spectral_upper':str(hi)}


if __name__=='__main__':
    ctx.prec=100
    for label,coeff in EXAMPLES:
        print(json.dumps(certify(label,coeff)),flush=True)
