"""Complete directed Taylor-integral and Rouche certificate; no zeta oracle."""
from fractions import Fraction as Q
from math import factorial
import json
from pathlib import Path
import importlib.util
_spec=importlib.util.spec_from_file_location('_gamma_interval',Path(__file__).with_name('interval.py'))
_mod=importlib.util.module_from_spec(_spec);_spec.loader.exec_module(_mod)
I,C,PI,S,BITS,exp_series,sqrt_series,mul,cm_sincos=(getattr(_mod,k) for k in
    ('I','C','PI','S','BITS','exp_series','sqrt_series','mul','cm_sincos'))

CASES = (
    ('integer_N4', (Q(1),Q(4),Q(9),Q(16)),
     '28.0555855384091825810295021076097455522309',
     '2.6219979332686197954925378014004831147962'),
    ('step_2_to_3_u_7_10', (Q(1),Q(4),Q(90,7)),
     '26.8135855368140614010181412691765400069731',
     '0.4209949404628029929584207065487732398251'),
)
DEGREE = 40
CELLS = 256
DELTA = Q(1,256)
RADIUS = Q(1,10**12)

def require(ok, message):
    if not ok: raise ValueError(message)

def rows(rates):
    out = []
    for a in rates:
        B = Q(1); ss = Q(0)
        for b in rates:
            if b == a: continue
            B *= (b/(b-a))**2; ss += 1/(b-a)
        out.append((a,a*a*B,-2*ss))
    return out

def analytic_guards(rates):
    require(rates[0] == 1 and len(set(rates)) == len(rates), 'rates')
    require(all(1 <= a <= 16 for a in rates), 'rate domain')
    rr = rows(rates); a0,b0,c0 = rr[0]
    lower_R = Q(29,10)
    require(c0 < 0 and lower_R+c0 > 0, 'dominant polynomial')
    ratio = Q(0)
    for a,b,c in rr[1:]:
        k = ((a-1)*lower_R).__floor__()
        ratio += b/b0*(2+abs(c)/lower_R)/(1+c0/lower_R)/2**k
    require(ratio < Q(1,2), 'dominant exponential failed')
    C0 = Q(1, factorial(2*len(rates)-1))
    tilt = Q(1)
    for a in rates:
        C0 *= a*a
        if a != 1: tilt *= (a/(a-1))**2
    require(C0 < 66 and tilt <= 4, 'density envelopes')
    # Cauchy circles: rho=1/32; real part of x>29/10.
    require(Q(31,10)*Q(15,16)*Q(511,512) > lower_R, 'circle x bound')
    # simplex phases: (16-1)/2 * pi/15 = pi/2, strict exp/sin bounds.
    require((max(rates)-min(rates))/2 <= Q(15,2), 'simplex sector')
    require(66*4**7 < 2**21 and 3**7 < 2**12, 'Cauchy magnitude')
    # A deliberately larger common M=2^36 for j<=2 avoids relying on exp(-3).
    require(Q(2*2**36,1)*Q(1,8)**(DEGREE+1)/Q(7,8) < Q(1,2**84), 'Taylor error')
    return {'dominant_ratio': [ratio.numerator,ratio.denominator],
            'gamma_simplex_coefficient':[C0.numerator,C0.denominator],
            'tilt':[tilt.numerator,tilt.denominator]}

def density_series(center, sign, rr, n):
    xx = [PI*(I(2*sign*center).exp())]
    for k in range(1,n+1): xx.append(xx[-1]*(2*sign)/k)
    out = [I(0) for _ in range(n+1)]
    for a,b,c in rr:
        ex = exp_series([-a*x for x in xx],n)
        aa = list(xx); aa[0] = aa[0]+c
        term = mul(aa,ex,n)
        out = [old+b*v for old,v in zip(out,term)]
    return out

def jet_cell(center, rr, z, n):
    fx=density_series(center,1,rr,n);fy=density_series(center,-1,rr,n)
    h=sqrt_series(mul(fx,fy,n),n)
    si,co=cm_sincos(z*center)
    cs=[co,-z*si];ss=[si,z*co];zz=z*z
    for k in range(2,n+1):
        cs.append(-zz*cs[k-2]/(k*(k-1)))
        ss.append(-zz*ss[k-2]/(k*(k-1)))
    cp=[sum((cs[k-j]*h[j] for j in range(k+1)),C(0)) for k in range(n+1)]
    sp=[sum((ss[k-j]*h[j] for j in range(k+1)),C(0)) for k in range(n+1)]
    jets=[C(0),C(0),C(0)]
    for k in range(0,n+1,2):
        factor=2*DELTA**(k+1)/Q(k+1)
        jets[0]=jets[0]+cp[k]*factor
        jets[1]=jets[1]-(sp[k]*center+(sp[k-1] if k else C(0)))*factor
        jets[2]=jets[2]-(cp[k]*center**2+(cp[k-1]*2*center if k else C(0))+(cp[k-2] if k>=2 else C(0)))*factor
    return jets

def tail_bound():
    # For t>=2, h<=4*pi*exp(-pi*cosh(2t)).
    # t^j exp(3t), j<=2: replace t^2 by exp(t); put v=exp(2t).
    # integral <=2*pi int_(e^4)^infty v exp(-pi*v/2)dv.
    # e^4>54, pi>3 and 2*pi<8 give a rational/enclosed bound.
    bound=I(8)*I(Q(2,3)*(54+Q(2,3)))*I(-81).exp()
    require(bound.hi < I(Q(1,2**105)).lo, 'complete time tail')
    return bound

def abs_upper(z):
    return (I(0, Q(z.r.absmax(),S))**2+I(0, Q(z.i.absmax(),S))**2).sqrt().hi

def abs_lower(z):
    def component(x):
        if x.lo<=0<=x.hi:return 0
        return min(abs(x.lo),abs(x.hi))
    return (I(Q(component(z.r),S))**2+I(Q(component(z.i),S))**2).sqrt().lo

def reconstruct(progress=False):
    result=[];tail=tail_bound();error=Q(1,2**84)+Q(tail.hi,S)
    for name,rates,re,im in CASES:
        require(abs(Q(re)) < 29 and abs(Q(im)) < 3, 'spectral bounds')
        guards=analytic_guards(rates);rr=rows(rates);z=C(Q(re),Q(im))
        jets=[C(0),C(0),C(0)]
        for j in range(CELLS):
            center=Q(2*j+1,256)
            values=jet_cell(center,rr,z,DEGREE)
            jets=[a+b for a,b in zip(jets,values)]
            if progress and (j+1)%64==0:print(name,j+1,flush=True)
        jets=[v.widen(error) for v in jets]
        residual=Q(abs_upper(jets[0]),S)
        slope=Q(abs_lower(jets[1]),S)
        curve=Q(abs_upper(jets[2]),S)
        # |I'''|<1 in |Im z|<=3, proved using full real-line density majorant.
        margin=RADIUS*slope-residual-RADIUS**2*curve/2-RADIUS**3/6
        require(margin>0, 'Rouche inequality')
        require(Q(im)>RADIUS and Q(im)+RADIUS<3,'disk domain')
        result.append({'name':name,'rates':[str(r) for r in rates],
          'center':[re,im],'radius':str(RADIUS),'guards':guards,
          'integral_jets':[v.pair() for v in jets],
          'residual_upper':str(residual),'derivative_lower':str(slope),
          'second_derivative_upper':str(curve),'rouche_margin_lower':str(margin),
          'one_simple_nonreal_zero':True,
          'disk_inside_xi_critical_band':Q(im)+RADIUS<Q(1,2)})
    return {'status':'PROPOSED_COMPUTER_ASSISTED_COMPONENT','rh_proved':False,
      'bits':BITS,'degree':DEGREE,'cells_per_case':CELLS,'complete_time_tail':tail.pair(),
      'complete_quadrature_error':str(error),'cases':result,
      'zero_of_zeta_claimed':False,'collision_location_certified':False}

if __name__=='__main__':
    from pathlib import Path
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--write',type=Path,required=True)
    parser.add_argument('--progress',action='store_true');args=parser.parse_args()
    args.write.write_text(json.dumps(reconstruct(args.progress),indent=2,sort_keys=True)+'\n')
    print('COMPLETE_INTEGRAL_AND_ROUCHE_RECONSTRUCTION')
