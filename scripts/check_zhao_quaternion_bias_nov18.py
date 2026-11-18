"""Certify the forced central zero and spectral mean margin for a quaternion field."""
from flint import arb,ctx,dirichlet_char
from check_zhao_cubic_fields_nov18 import run_gp
from check_zhao_abelian_fields_nov18 import spectral_weight


def certificate():
    ctx.prec=120
    f='x^8+12*x^6+36*x^4+36*x^2+9'
    count=2048
    program=(f'F={f};K=nfinit(F);H=nfsubfields(K,4,1)[1];E=nfinit(H);N={count};\n'
             'A=dirdiv(dirzetak(K,N),dirzetak(E,N));v=vector(N);v[1]=1;\n'
             'for(n=2,N,v[n]=(A[n]-sumdiv(n,d,if(d>1 && d<n,v[d]*v[n/d],0)))/2);\n'
             'print([galoisidentify(galoisinit(F)),K.disc,E.disc,K.sign,vecsort(apply(nfdisc,nfsubfields(E,2,1))),v]);\n')
    (row,)=run_gp(program)
    group,disc,disc4,signature,quadratics,coeff=row
    if (group,disc,disc4,signature,quadratics)!=([8,4],12230590464,2304,[0,4],[8,12,24]):
        raise ArithmeticError(f'Unexpected algebraic invariants: {row[:-1]}')
    if len(coeff)!=count or any(abs(a)>n for n,a in enumerate(coeff,1)):
        raise ArithmeticError('Invalid Artin coefficients')
    # disc(K)=disc(F)*q^2, so this field has q=2304.
    c=2*arb.pi()/48
    def theta(t):
        base=c*t
        last=min(count,int(257/float(base))+1)
        value=arb(0)
        for n,a in enumerate(coeff[:last],1):
            if a:
                z=base*n
                value+=a*z*z.bessel_k(0)
        return value,last
    def signed(t):
        value,last=theta(t)
        q=(-c*t/2).exp()
        tail=2*q**(last+1)*((last+1)-last*q)/(1-q)**2
        return value+arb(0,tail.upper())
    low,high=signed(arb(1)/2),signed(arb(2))
    if not (low<0 and high>0):
        raise ArithmeticError('Functional equation sign unresolved')
    den,num=arb(0),arb(0)
    for j in range(1,1000):
        u=arb(j)/20;t=u.exp()
        if c*t>256: break
        v,last=theta(t)
        if not (last+1)*c*t>256:
            raise ArithmeticError('Missing kernel terms')
        den+=(t-1)*v
        num+=u*(t+1)*v
    else: raise ArithmeticError('Theta grid too short')
    # For root sign -1 the central mesh value theta(1) vanishes.
    den=den/20+arb(0,'1e-12')
    num=num/20+arb(0,'1e-12')
    if not den>0:
        raise ArithmeticError('Unresolved denominator')
    bbase=2+arb.const_euler()-(4*arb.pi()).log()
    for d in quadratics:
        chars=[dirichlet_char(d,j) for j in range(1,d) if j*j%d==1]
        chars=[ch for ch in chars if ch.is_primitive() and not ch.parity()]
        if len(chars)!=1: raise ArithmeticError('Missing real quadratic character')
        bbase+=spectral_weight(chars[0])
    total=bbase+4*num/den
    print('theta(1/2), theta(2), B*_K:',low,high,total)
    if not total<18: raise ArithmeticError('Central multiplicity does not give strict positivity')
    return total


if __name__=='__main__':
    certificate()
