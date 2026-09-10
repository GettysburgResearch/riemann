"""Directed defining-integral certificate for the MEAN-CENTERED integer N=5.

The arithmetic module is copied byte-for-byte from frozen CG26; this is not
an independent primitive backend. No scout or numerical package is imported.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import importlib.util
import json

_spec = importlib.util.spec_from_file_location('_endpoint_interval', Path(__file__).with_name('interval.py'))
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
I, C, PI, S, BITS, exp_series, sqrt_series, mul, cm_sincos = (
    getattr(_mod, k) for k in ('I','C','PI','S','BITS','exp_series','sqrt_series','mul','cm_sincos'))

N = 5
RATES = tuple(Q(k*k) for k in range(1,N+1))
DEGREE = 40
B = Q('1.079529')
LLO, LHI = Q('1.07952912855616'), Q('1.07952912855618')
CENTER = ('31.0835163803300613860836804713778137956057544691',
          '0.2347791171837078741080118319340221394471947526')
RADIUS = Q(1,10**12)
TAU = PI*PI/3 - 2*sum((Q(1,k*k) for k in range(1,N+1)), Q(0))


def require(ok, message):
    if not ok:
        raise ValueError(message)


def rows(rates=RATES):
    answer = []
    for a in rates:
        b, c = a*a, Q(0)
        for other in rates:
            if other != a:
                b *= (other/(other-a))**2
                c -= 2/(other-a)
        answer.append((a,b,c))
    return answer


def panels():
    """Dyadic partition. Every disk radius is at least eight half-cell widths."""
    todo = [(Q(0),B)]
    out = []
    while todo:
        a,b = todo.pop()
        center,delta = (a+b)/2,(b-a)/2
        rho = min(Q(1,64), (LLO-center)/4)
        require(rho > 0, 'panel crosses declared support')
        if delta*8 <= rho:
            out.append((center,delta,rho))
        else:
            todo.extend(((center,b),(a,center)))
    out.sort()
    end = Q(0)
    for center,delta,rho in out:
        require(center-delta == end, 'gap/overlap')
        require(delta*8 <= rho, 'Cauchy ratio')
        end = center+delta
    require(end == B, 'missing integral region')
    return out


def guards(rr):
    require(PI.lo>I(Q(31,10)).hi and PI.hi<I(Q(22,7)).lo, 'pi elementary bounds')
    require(Q(10)*Q(100,36)*Q(32,31)+Q(37,100)<32, 'large modulus')
    require(Q(22,7)*Q(32,31)+Q(37,100)<4, 'small modulus')
    require(2400*Q(11,10)**9<80**2, 'endpoint amplitude')
    require(N == 5 and RATES == tuple(Q(k*k) for k in range(1,6)), 'wrong gamma law')
    require(TAU.lo > I(Q(36,100)).hi and TAU.hi < I(Q(11,30)).lo, 'mean shift')
    require((PI/TAU).lo > I(2*LLO).exp().hi, 'support lower')
    require((PI/TAU).hi < I(2*LHI).exp().lo, 'support upper')
    # On |t-c|<=rho<=1/64, Re(pi exp(2t)-tau)>13/5.
    # e^-1/32 >=31/32 and cos(1/32)>=1-1/2048.
    require(Q(31,10)*Q(31,32)*Q(2047,2048)-Q(37,100)>Q(13,5), 'large argument')
    # |Im(pi exp(-2t)-tau)| < 4*(32/31)/32=4/31 < pi/24.
    require(Q(4,31) < Q(31,10)/24, 'simplex sector')
    # rho<= (L-c)/4: e^(2(L-c-rho)) cos(2rho)>1, so Re y>tau.
    # The proof uses cos(2rho)>=exp(-4rho^2), valid here.
    # exp-power dominant row at Re x>=13/5; imag x is <Re x.
    a0,b0,c0=rr[0]
    x=Q(13,5)
    require(x+c0>0, 'dominant linear factor')
    ratio=Q(0)
    for a,b,c in rr[1:]:
        ratio += (b/b0)*(2+abs(c)/x)/(1+c0/x)/2**int((a-1)*x)
    require(ratio<Q(1,4), 'large-argument zero exclusion')
    # Uniform complete complex-circle integrand ceiling M=2^32 for j<=2.
    require(sum(b*(Q(32)+abs(c)) for a,b,c in rr) < 2**11, 'large density ceiling')
    smallc=Q(factorial(N)**4,factorial(2*N-1))
    require(smallc < 600 and smallc*4**9<2**28, 'small density ceiling')
    require(32*Q(1,64)+Q(1,4)*Q(11,10)<1, 'complex cosine ceiling')
    # sqrt(2^11 * 2^28) < 2^20; exp(1)<3; |t|^2<2.
    require(6*2**20 < 2**32, 'integrand ceiling')
    return {'dominant_ratio':[str(ratio.numerator),str(ratio.denominator)],
            'tau_interval':TAU.pair(), 'support_interval':[str(LLO),str(LHI)],
            'simplex_coefficient':str(smallc), 'cauchy_integrand_ceiling':str(2**32)}


def density_series(center, rho, sign, rr, degree):
    xx=[PI*I(2*sign*center).exp()]
    for k in range(1,degree+1):
        xx.append(xx[-1]*(2*sign*rho)/k)
    xx[0]=xx[0]-TAU
    out=[I(0) for _ in range(degree+1)]
    for a,b,c in rr:
        exponential=exp_series([-a*v for v in xx],degree)
        linear=list(xx);linear[0]=linear[0]+c
        term=mul(linear,exponential,degree)
        out=[old+b*v for old,v in zip(out,term)]
    return out


def cell_jets(center,delta,rho,rr,z,degree):
    fx=density_series(center,rho,1,rr,degree)
    fy=density_series(center,rho,-1,rr,degree)
    h=sqrt_series(mul(fx,fy,degree),degree)
    si,co=cm_sincos(z*center)
    cs,ss=[co,-z*rho*si],[si,z*rho*co]
    zz=z*z*rho*rho
    for k in range(2,degree+1):
        cs.append(-zz*cs[k-2]/(k*(k-1)))
        ss.append(-zz*ss[k-2]/(k*(k-1)))
    cp=[sum((cs[k-j]*h[j] for j in range(k+1)),C(0)) for k in range(degree+1)]
    sp=[sum((ss[k-j]*h[j] for j in range(k+1)),C(0)) for k in range(degree+1)]
    out=[C(0),C(0),C(0)]
    for k in range(0,degree+1,2):
        factor=2*delta*(delta/rho)**k/(k+1)
        out[0]=out[0]+factor*cp[k]
        out[1]=out[1]-factor*(center*sp[k]+(rho*sp[k-1] if k else C(0)))
        out[2]=out[2]-factor*(center**2*cp[k]+(2*center*rho*cp[k-1] if k else C(0))+(rho*rho*cp[k-2] if k>=2 else C(0)))
    return out


def abs_upper(z):
    return (I(0,Q(z.r.absmax(),S))**2+I(0,Q(z.i.absmax(),S))**2).sqrt().hi


def abs_lower(z):
    def lower(x):
        return 0 if x.lo<=0<=x.hi else min(abs(x.lo),abs(x.hi))
    return (I(Q(lower(z.r),S))**2+I(Q(lower(z.i),S))**2).sqrt().lo


def reconstruct(progress=False):
    rr=rows();gg=guards(rr);pp=panels();z=C(Q(CENTER[0]),Q(CENTER[1]))
    require(abs(Q(CENTER[0]))<32 and abs(Q(CENTER[1]))+RADIUS<Q(1,4), 'spectral disk')
    require(Q(CENTER[0])>RADIUS and Q(CENTER[1])>RADIUS, 'disk separated from axes')
    require(LHI+Q(1,64)<Q(11,10), 'complex time ceiling')
    jets=[C(0),C(0),C(0)]
    for j,(center,delta,rho) in enumerate(pp):
        values=cell_jets(center,delta,rho,rr,z,DEGREE)
        jets=[old+new for old,new in zip(jets,values)]
        if progress and (j+1)%128==0:
            print('centered-N5 cells',j+1,'/',len(pp),flush=True)
    quad=2*B*2**32*Q(1,8)**(DEGREE+1)/Q(7,8)
    # r=L-t<13/10^8; h<=80 r^(9/2), j<=2 and |Im z|<1/4.
    d=Q(13,10**8)
    require(0<LHI-B<d and d<Q(1,2000**2), 'endpoint gap')
    tail=Q(640,11)*d**5/2000
    jets=[x.widen(quad+tail) for x in jets]
    residual,slope,curve=Q(abs_upper(jets[0]),S),Q(abs_lower(jets[1]),S),Q(abs_upper(jets[2]),S)
    # ||I'''|| <= 2L*(11/10)^3*8 <32, using h<=4*pi*e^tau*e^-pi <8.
    third=Q(32)
    margin=RADIUS*slope-residual-RADIUS**2*curve/2-RADIUS**3*third/6
    require(margin>0,'Rouche disk does not certify')
    return {'status':'PROPOSED_SOURCE_COMPLETE_FINITE_CERTIFICATE','rh_proved':False,
        'source':'mean-centered integer N=5; not raw interpolation; not xi',
        'N':N,'bits':BITS,'degree':DEGREE,'panels':len(pp),'interval':[str(Q(0)),str(B)],
        'center':list(CENTER),'radius':str(RADIUS),'guards':gg,
        'quadrature_error':str(quad),'endpoint_tail_error':str(tail),
        'integral_jets':[v.pair() for v in jets],
        'residual_upper':str(residual),'derivative_lower':str(slope),
        'second_derivative_upper':str(curve),'third_derivative_upper':str(third),
        'rouche_margin_lower':str(margin),'exactly_one_simple_zero':True,
        'inside_critical_band':True,'zero_of_xi_claimed':False,
        'exhaustive_zero_census':False,'global_zero_threshold_computed':False}


if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--write',type=Path,required=True)
    p.add_argument('--progress',action='store_true')
    a=p.parse_args()
    a.write.write_text(json.dumps(reconstruct(a.progress),sort_keys=True,indent=2)+'\n')
    print('COMPLETE_CENTERED_INTEGER_DISK_CERTIFICATE')
