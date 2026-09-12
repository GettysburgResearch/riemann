"""Source-complete N=5 moment separator. No roots or floating input are used.

Analytic remainder dependencies are in PROOF.md. Arithmetic is the credited,
frozen CCF26 dyadic implementation, not an independent primitive backend.
"""
from fractions import Fraction as Q
from math import factorial, comb
from functools import lru_cache
from pathlib import Path
import argparse, hashlib, json, sys
from exact_interval import I, SCALE, BITS, exp, pi

RATES = (1, 4, 9, 16, 25)
DEGREE = 48
ORDER = 14
B = Q('1.079529')
LLO, LHI = Q('1.07952912855616'), Q('1.07952912855618')
P = (3, -206, 3213, -19804, 56422, -72888, 33187)
SPECTRAL_SCALE = 200
PRIMITIVE_SHA256 = '083ef417bc5249e189fb08f1c7b9009ff69a97a19073ba2778e02512515bf427'


def authenticate_primitive():
    require(hashlib.sha256(Path(__file__).with_name('exact_interval.py').read_bytes()).hexdigest()
            == PRIMITIVE_SHA256, 'changed arithmetic primitive')


def require(ok, why):
    if not ok:
        raise ValueError(why)


def widen(v, error):
    e = I.q(error).hi
    return I(v.lo-e, v.hi+e)


def rows():
    rr = []
    for aa in RATES:
        a = Q(aa); b = a*a; c = Q(0)
        for dd in RATES:
            d = Q(dd)
            if d != a:
                b *= (d/(d-a))**2
                c -= 2/(d-a)
        rr.append((a, b, c))
    return rr


def panels():
    todo = [(Q(0), B)]; answer = []
    while todo:
        a, b = todo.pop(); c = (a+b)/2; d = (b-a)/2
        rho = min(Q(1,64), (LLO-c)/4)
        require(rho > 0, 'outside source support')
        if 8*d <= rho:
            answer.append((c, d, rho))
        else:
            todo.extend(((a,c), (c,b)))
    answer.sort(); endpoint = Q(0)
    for c,d,rho in answer:
        require(c-d == endpoint and 8*d <= rho, 'gap or Cauchy violation')
        endpoint = c+d
    require(endpoint == B, 'incomplete source cover')
    return answer


def mul(a, b, degree):
    z = I.q(0)
    return [sum((a[j]*b[k-j] for j in range(max(0,k-len(b)+1), min(k+1,len(a)))), z)
            for k in range(degree+1)]


def exp_series(a, degree):
    out = [exp(a[0])]
    for n in range(1, degree+1):
        out.append(sum((k*a[k]*out[n-k] for k in range(1,n+1)), I.q(0))/n)
    return out


def sqrt_series(a, degree):
    out = [a[0].sqrt()]
    require(out[0].lo > 0, 'source density not separated from zero')
    denominator = 2*out[0]
    for n in range(1,degree+1):
        out.append((a[n]-sum((out[k]*out[n-k] for k in range(1,n)), I.q(0)))/denominator)
    return out


def density_series(c, rho, sign, rr, tau, p, degree):
    xx = [p*exp(2*sign*c)]
    for k in range(1,degree+1):
        xx.append(xx[-1]*(2*sign*rho)/k)
    xx[0] = xx[0]-tau
    out = [I.q(0) for _ in range(degree+1)]
    for a,b,cc in rr:
        ee = exp_series([-a*v for v in xx],degree)
        lin = list(xx); lin[0] = lin[0]+cc
        term = mul(lin,ee,degree)
        out = [x+b*y for x,y in zip(out,term)]
    return out


@lru_cache(maxsize=4)
def stirling_rows(degree):
    """T_n(y)=sum S(n,k)y^k, the exact exponential Touchard polynomials."""
    rows = [(1,)]
    for n in range(1, degree+1):
        prev = rows[-1]
        rows.append(tuple((prev[k-1] if k else 0)+(k*prev[k] if k<len(prev) else 0)
                          for k in range(n+1)))
    return tuple(rows)


def density_series_fast(c, rho, sign, rr, tau, p, degree):
    X = p*exp(2*sign*c); r = 2*sign*rho; x = X-tau
    rp = [I.q(1)]
    for k in range(1,degree+2):
        rp.append(rp[-1]*r/k)
    out = [I.q(0) for _ in range(degree+1)]
    for a,b,cc in rr:
        y = -a*X; E0 = exp(-a*x); ee = []
        for k,row in enumerate(stirling_rows(degree+1)):
            value = I.q(row[-1])
            for coeff in reversed(row[:-1]):
                value = value*y+coeff
            ee.append(E0*value*rp[k])
        for k in range(degree+1):
            out[k] += b*((cc-tau)*ee[k]-(k+1)*ee[k+1]/(r*a))
    return out


def cell(c, d, rho, rr, tau, p, degree):
    xx = density_series_fast(c,rho,1,rr,tau,p,degree)
    yy = density_series_fast(c,rho,-1,rr,tau,p,degree)
    hh = sqrt_series(mul(xx,yy,degree),degree)
    # Integrate the entire product of the density Taylor polynomial with t^(2r).
    # Its degree is degree+2r, not silently truncated back to degree.
    vpow = [I.q(1)]
    for k in range(1,degree+2*ORDER+1):
        vpow.append(vpow[-1]*(d/rho))
    integrals = []
    for j in range(2*ORDER+1):
        integrals.append(2*d*sum((hh[k]*vpow[k+j]/(k+j+1)
                          for k in range(degree+1) if (k+j)%2 == 0), I.q(0)))
    moments = []
    for r in range(ORDER+1):
        n = 2*r
        moments.append(sum((comb(n,j)*c**(n-j)*rho**j*integrals[j]
                            for j in range(n+1)),I.q(0)))
    return moments


def guards(p, tau, rr):
    require(RATES == (1,4,9,16,25), 'changed native rates')
    require(p.inside(Q(31,10),Q(22,7)), 'pi guard')
    require(10*Q(100,36)*Q(32,31)+Q(37,100)<32,'large modulus')
    require(Q(22,7)*Q(32,31)+Q(37,100)<4,'small modulus')
    require(tau.inside(Q(36,100),Q(11,30)), 'exact mean centering')
    require((p/tau).lo > exp(2*LLO).hi, 'support lower')
    require((p/tau).hi < exp(2*LHI).lo, 'support upper')
    require(Q(31,10)*Q(31,32)*Q(2047,2048)-Q(37,100)>Q(13,5), 'large real part')
    require(Q(4,31)<Q(31,10)/24, 'small-argument simplex strip')
    a0,b0,c0 = rr[0]; x = Q(13,5)
    require(x+c0>0, 'leading factor')
    ratio = sum(((b/b0)*(2+abs(c)/x)/(1+c0/x)/2**int((a-1)*x)
                 for a,b,c in rr[1:]), Q(0))
    require(ratio<Q(1,4), 'density zero-free comparison')
    require(sum(b*(32+abs(c)) for a,b,c in rr)<2**11, 'large density bound')
    sc = Q(factorial(5)**4,factorial(9))
    require(sc<600 and sc*4**9<2**28, 'small density bound')
    require(LHI+Q(1,64)<Q(11,10), 'complex time bound')
    require(Q(11,10)**(2*ORDER)<16, 'all moment powers')
    require(16*2**20<2**32, 'full integrand ceiling')
    require(2400*Q(11,10)**9<80**2, 'endpoint density amplitude')
    gap = Q(13,10**8)
    require(0<LHI-B<gap and gap<Q(1,2000**2), 'full endpoint gap')
    return ratio, gap


def gamma_part(index, parts=8, degree=DEGREE, progress=False):
    require(type(index) is int and type(parts) is int and parts==8 and 0<=index<parts,'invalid partition')
    p = pi(); tau = p*p/3-2*sum((Q(1,n*n) for n in range(1,6)),Q(0))
    rr=rows();guards(p,tau,rr);pp=panels()
    start=len(pp)*index//parts;stop=len(pp)*(index+1)//parts
    out=[I.q(0) for _ in range(ORDER+1)]
    for j in range(start,stop):
        out=[a+b for a,b in zip(out,cell(*pp[j],rr,tau,p,degree))]
    return {'kind':'fresh_directed_gamma_moment_partition','part':index,'parts':parts,
            'degree':degree,'cells':[start,stop],'total_cells':len(pp),
            'raw_half_moment_integrals':[x.bounds() for x in out]}


def gamma_moments(degree=DEGREE,progress=False,part_dir=None):
    p=pi();tau=p*p/3-2*sum((Q(1,n*n) for n in range(1,6)),Q(0));rr=rows()
    ratio,gap=guards(p,tau,rr);pp=panels();out=[I.q(0) for _ in range(ORDER+1)]
    for index in range(8):
        if part_dir is None:
            record=gamma_part(index,8,degree,progress)
        else:
            record=strict_json(part_dir/f'part_{index}.json')
            require(record['kind']=='fresh_directed_gamma_moment_partition'
                    and type(record['part']) is int and record['part']==index
                    and type(record['parts']) is int and record['parts']==8
                    and type(record['degree']) is int and record['degree']==degree
                    and record['cells']==[len(pp)*index//8,len(pp)*(index+1)//8]
                    and record['total_cells']==len(pp),'invalid or incomplete part receipt')
        values=record['raw_half_moment_integrals']
        require(len(values)==ORDER+1,'missing moment coordinates')
        out=[x+I(I.q(Q(a)).lo,I.q(Q(b)).hi) for x,(a,b) in zip(out,values)]
        if progress: print('assembled gamma source partition',index+1,'/ 8',file=sys.stderr,flush=True)
    quad=2*B*2**32*Q(1,8)**(degree+1)/Q(7,8)
    tail=Q(2560,11)*gap**5/2000
    out=[widen(x,quad+tail) for x in out]
    require(out[0].lo>0,'normalizing integral not positive')
    coef=[x/out[0]/factorial(2*r) for r,x in enumerate(out)];coef[0]=I.q(1)
    return coef,{'degree':degree,'cells':len(pp),'half_normalizer':out[0].bounds(),
                 'mean_shift':tau.bounds(),'support':[str(LLO),str(LHI)],
                 'quadrature_error_each_raw_moment':str(quad),
                 'complete_endpoint_error_each_raw_moment':str(tail),'dominant_ratio':str(ratio)}


def theta_coefficients(mesh=128):
    require(mesh in (128,160),'unsupported theta mesh')
    p = pi(); out = [I.q(0) for _ in range(ORDER+1)]
    for j in range(3*mesh+1):
        t = Q(j,mesh); e2 = exp(2*t); e9 = exp(Q(9,2)*t); e5 = exp(Q(5,2)*t)
        ph = I.q(0)
        for n in range(1,21):
            nn=n*n
            ph += (4*p*p*nn**2*e9-6*p*nn*e5)*exp(-p*nn*e2)
        wt = Q(1 if j==0 else 2,mesh)
        for r in range(ORDER+1):
            out[r] += wt*t**(2*r)*ph/factorial(2*r)
    # The original factorial moment bound, rederived for every order in PROOF.md.
    out = [widen(x,Q(1,1<<237)) for x in out]
    require(out[0].lo>0,'theta normalizer')
    ans = [x/out[0] for x in out]; ans[0]=I.q(1)
    return ans


def power_sums(coef):
    # b_k is the coefficient of w^k in F(i sqrt(200w)).
    b = [v*SPECTRAL_SCALE**k for k,v in enumerate(coef)]
    q = [I.q(0) for _ in b]
    for n in range(1,len(b)):
        q[n] = (-1)**(n+1)*(n*b[n]-sum(((-1)**(j+1)*q[j]*b[n-j]
                                                      for j in range(1,n)),I.q(0)))
    return q


def form(q, vector=P):
    return sum((vector[i]*vector[j]*q[i+j+2]
                for i in range(len(vector)) for j in range(len(vector))),I.q(0))


def positive_pivots(q, d):
    a = [[q[i+j+2] for j in range(d)] for i in range(d)]
    pivots=[]
    for k in range(d):
        piv=a[k][k];require(piv.lo>0,'nonpositive interval LDL pivot')
        pivots.append(piv)
        for i in range(k+1,d):
            for j in range(i,d):
                a[j][i]=a[i][j]=a[i][j]-a[i][k]*a[j][k]/piv
    return pivots


def fit_box_form(coef, epsilon, radius=32):
    # E_14(radius)<=epsilon implies each coefficient lies in this outer box.
    inflated = [I.q(1)]+[widen(coef[k],epsilon/Q(radius)**(2*k)) for k in range(1,len(coef))]
    return form(power_sums(inflated))


def absq(x):
    return Q(max(abs(x.lo),abs(x.hi)),SCALE)


def robust_separator(coef):
    """Finite formal-log perturbation bound for the whole weighted l1 fit ball."""
    b=[v*SPECTRAL_SCALE**k for k,v in enumerate(coef)]
    recip=[I.q(1)]
    for n in range(1,len(b)):
        recip.append(-sum((b[k]*recip[n-k] for k in range(1,n+1)),I.q(0)))
    W=[0]*len(b)
    for i in range(len(P)):
        for j in range(len(P)):
            W[i+j+2]+=P[i]*P[j]
    gradient=[I.q(0)]
    for l in range(1,len(b)):
        gradient.append(sum(((-1)**(n+1)*n*W[n]*recip[n-l]
                             for n in range(max(2,l),len(b))),I.q(0)))
    radius=Q(3,4);t=Q(SPECTRAL_SCALE,32**2)
    linear=max(absq(gradient[l])*t**l for l in range(1,len(b)))
    invnorm=sum((absq(x)*radius**j for j,x in enumerate(recip)),Q(0))
    dual=max(Q(n*abs(W[n]))/radius**n for n in range(2,len(b)))
    require(linear<36787 and invnorm<71 and dual<3500000000000,'dual majorants failed')
    epsilon=Q(1,1<<26);u=epsilon*radius*t*71
    require(u<1,'formal logarithm remainder radius')
    error=epsilon*36787+Q(3500000000000)*u*u/(2*(1-u))
    require(error<Q(43,1000),'complete weighted-fit perturbation cost')
    base=form(power_sums(coef))
    require(Q(base.hi,SCALE)+error<Q(-1,20),'entire coefficient ball must remain negative')
    return {'radius':str(radius),'fit_radius':32,'excluded_E14_tolerance':str(epsilon),
            'linear_dual_bound':str(linear),'inverse_series_norm_bound':str(invnorm),
            'log_functional_norm':str(dual),'complete_perturbation_cost':str(error),
            'perturbed_form_upper':str(Q(base.hi,SCALE)+error),
            'method':'formal-log exact derivative plus complete nonlinear remainder, weighted l1 ball'}


def weighted_pivots(q,d):
    # ((i+j+1)! q_(i+j+2)) is a DIFFERENT matrix from the native unweighted one.
    a=[[factorial(i+j+1)*q[i+j+2] for j in range(d)] for i in range(d)]
    out=[]
    for k in range(d):
        piv=a[k][k];require(piv.lo>0,'factorial-weighted LDL')
        out.append(piv)
        for i in range(k+1,d):
            for j in range(i,d):a[j][i]=a[i][j]=a[i][j]-a[i][k]*a[j][k]/piv
    return out


def reconstruct(progress=False,degree=DEGREE,part_dir=None):
    authenticate_primitive()
    gamma, details = gamma_moments(degree,progress,part_dir)
    q = power_sums(gamma); sep = form(q)
    require(sep.inside(Q(-94,1000),Q(-93,1000)),'native separating form not negative')
    piv = positive_pivots(q,6)
    robust=robust_separator(gamma)
    weighted=weighted_pivots(q,7)
    require(all(x.lo>0 for x in q[1:]),'signed cumulant positivity')
    newton=[k*gamma[k]**2-(k+1)*gamma[k-1]*gamma[k+1] for k in range(1,ORDER)]
    require(all(x.lo>0 for x in newton),'finite Newton inequalities')
    theta = theta_coefficients(); tq=power_sums(theta);tpiv=positive_pivots(tq,7)
    errors = {}
    for bits in (40,48,56,64,72,80):
        test = fit_box_form(gamma,Q(1,1<<bits))
        errors[str(bits)] = test.bounds()
    require(I.q(Q(errors['80'][1])).hi<0,'robust coefficient-fit rejection failed')
    return {'status':'PROPOSED_SOURCE_COMPLETE_FINITE_CERTIFICATE','rh_proved':False,
            'max_raw_moment_degree':28,'source':'original mean-centered integer gamma N=5',
            'bits':BITS,'gamma_integration':details,'gamma_coefficients':[x.bounds() for x in gamma],
            'gamma_scaled_power_sums':[x.bounds() for x in q],
            'integer_separator':list(P),'spectral_scale':SPECTRAL_SCALE,
            'separating_form':sep.bounds(),'positive_gamma_H6_pivots':[x.bounds() for x in piv],
            'robust_separator':robust,'positive_factorial_H7_pivots':[x.bounds() for x in weighted],
            'positive_Newton_gaps':[x.bounds() for x in newton],
            'theta_coefficients':[x.bounds() for x in theta],
            'positive_theta_H7_pivots':[x.bounds() for x in tpiv],
            'theta_same_form':form(tq).bounds(),'coefficient_box_forms_at_R32':errors,
            'root_locations_used':False,'native_unbounded_feasibility_proved':False}


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=True)


def short_bounds(pair, digits=18):
    """Outward DECIMAL-rational display; the computation itself stays 512-bit."""
    a,b=map(Q,pair); scale=10**digits
    lo=(a.numerator*scale)//a.denominator
    hi=-((-b.numerator*scale)//b.denominator)
    return [str(Q(lo,scale)),str(Q(hi,scale))]


def receipt(full):
    """Small binding receipt. --dump-full exports every primitive result interval."""
    robust=full['robust_separator']
    return {
        'status':full['status'],'rh_proved':False,
        'source':full['source'],'bits':full['bits'],
        'max_raw_moment_degree':28,'spectral_scale':200,
        'integer_separator':list(P),'gamma_cells':full['gamma_integration']['cells'],
        'density_Taylor_degree':full['gamma_integration']['degree'],
        'separating_form':short_bounds(full['separating_form']),
        'gamma_H7_inertia':[6,1,0],
        'positive_gamma_H6_pivots':[short_bounds(x) for x in full['positive_gamma_H6_pivots']],
        'positive_factorial_H7_pivots':[short_bounds(x) for x in full['positive_factorial_H7_pivots']],
        'positive_theta_H7_pivots':[short_bounds(x) for x in full['positive_theta_H7_pivots']],
        'theta_same_form':short_bounds(full['theta_same_form']),
        'positive_Newton_inequality_count':len(full['positive_Newton_gaps']),
        'positive_signed_cumulant_count':len(full['gamma_scaled_power_sums'])-1,
        'fit_radius':32,'excluded_weighted_error':robust['excluded_E14_tolerance'],
        'robust_form_upper_less_than':'-1/20',
        'complete_perturbation_cost_less_than':'43/1000',
        'root_locations_used':False,'native_unbounded_feasibility_proved':False,
        'full_reconstruction_sha256':hashlib.sha256(canonical(full).encode()).hexdigest()
    }


def strict_json(path):
    def pairs(items):
        out={}
        for k,v in items:
            if k in out:raise ValueError('duplicate JSON key')
            out[k]=v
        return out
    return json.loads(path.read_text(),object_pairs_hook=pairs,
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError('nonfinite JSON')))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',type=Path);parser.add_argument('--check',type=Path)
    parser.add_argument('--progress',action='store_true');parser.add_argument('--degree',type=int,default=DEGREE)
    parser.add_argument('--part',type=int);parser.add_argument('--finish-parts',type=Path)
    parser.add_argument('--dump-full',type=Path)
    args=parser.parse_args()
    authenticate_primitive()
    require(bool(args.write)^bool(args.check),'specify exactly one of --write and --check')
    require(args.degree in (48,56),'only certified displayed degrees')
    if args.part is not None:
        require(args.write is not None and args.finish_parts is None and args.dump_full is None,
                'part requires write, not finish or full suffix')
        result=gamma_part(args.part,8,args.degree,args.progress)
    else:
        full=reconstruct(args.progress,args.degree,args.finish_parts)
        if args.dump_full:
            args.dump_full.write_text(json.dumps(full,sort_keys=True,indent=2)+'\n')
        result=receipt(full)
    if args.check:
        expected=strict_json(args.check)
        require(canonical(expected)==canonical(result),
                'receipt differs from fresh source reconstruction')
    else:
        args.write.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('DIRECTED_GAMMA_PART_RECONSTRUCTED' if args.part is not None else
          ('PARTS_ASSEMBLED_AND_SUFFIX_CHECKED' if args.finish_parts is not None else
           'SOURCE_COMPLETE_NATIVE_HANKEL_PASS'))

if __name__=='__main__':
    main()
