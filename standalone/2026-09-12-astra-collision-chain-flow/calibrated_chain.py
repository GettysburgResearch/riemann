"""Complete native six-moment seed with all three real-field growth coefficients.

The certified root is independent (q=0). The analytic parameter theorem in
ISING.md gives genuinely connected infinite chains for every sufficiently
small positive q; no numerical positive-q radius is claimed.
"""
from fractions import Fraction as Q
from math import comb,factorial
from exact_interval import I,SCALE,log_q
from native_theta import cumulants
from research_algebra import require

MULTIPLICITIES=(25,4,1,1)
CENTERS=tuple(Q(s) for s in (
'0.02214740729441991945467506172554831495554696774107269533',
'0.06294208128372751271228155631799086369338395596615177837',
'0.1113970777650096508879646441011077685460850985953812789',
'0.0047318790614544977006562261968942563874719938269197464'))
RADIUS=Q(1,10**12)


def bounds_to_i(b):
    return I(I.q(Q(b[0])).lo,I.q(Q(b[1])).hi)


def derivative_poly(p,s):
    """D[x^-s p(log x)] = x^(-s-1) [p' - s p]."""
    out=[-s*a for a in p]
    for j in range(1,len(p)):out[j-1]+=j*p[j]
    return out


def evaluate_poly(p,t):
    out=I.q(0)
    for a in reversed(p):out=out*t+a
    return out


def integral_log_power(s,j,M):
    """Exact integral from M to infinity of x^-s(log x)^j, with log enclosure."""
    if s<=1 or j<0:raise ValueError('integrable power and nonnegative log degree required')
    L=log_q(Q(M))
    z=I.q(0)
    for l in range(j+1):
        z=z+Q(factorial(j),factorial(j-l)*(s-1)**(l+1))*L**(j-l)
    return Q(1,M**(s-1))*z


def log_power_tail(s,j,M=1024):
    """Entire sum n>=32, B4 Euler--Maclaurin and absolute B6 remainder."""
    if type(s) is not int or type(j) is not int or s<=1 or not 0<=j<=8:raise ValueError('unsupported tail')
    L=log_q(Q(M));z=I.q(0)
    for n in range(32,M+1):z=z+log_q(Q(n))**j/Q(n**s)
    p=[Q(0)]*j+[Q(1)];polys=[p]
    for k in range(6):polys.append(derivative_poly(polys[-1],s+k))
    z=z+integral_log_power(s,j,M)-L**j/Q(2*M**s)
    z=z-evaluate_poly(polys[1],L)/Q(12*M**(s+1))
    z=z+evaluate_poly(polys[3],L)/Q(720*M**(s+3))
    r=I.q(0)
    for k,a in enumerate(polys[6]):
        r=r+abs(a)*integral_log_power(s+6,k,M)/30240
    # With only B4 displayed, the B6 term must ALSO be retained as an error.
    # Integration by parts gives tail remainder -B6 f^(5)/6! plus its
    # periodic B6 integral. Include both explicitly; do not omit the term.
    b6term=evaluate_poly(polys[5],L)/Q(30240*M**(s+5))
    err=r.hi+max(abs(b6term.lo),abs(b6term.hi))
    return I(z.lo-err,z.hi+err)


def euler_gamma(M=4096):
    H=sum((Q(1,n) for n in range(1,M+1)),Q(0))
    z=I.q(H)-log_q(Q(M))-Q(1,2*M)+Q(1,12*M**2)-Q(1,120*M**4)+Q(1,252*M**6)
    r=I.q(Q(1,240*M**8)).hi
    return I(z.lo-r,z.hi+r)


def invert(matrix):
    n=len(matrix);a=[list(row)+[Q(i==j) for j in range(n)] for i,row in enumerate(matrix)]
    for j in range(n):
        pivot=next((k for k in range(j,n) if a[k][j]),None)
        if pivot is None:raise ArithmeticError('singular preconditioner')
        a[j],a[pivot]=a[pivot],a[j];v=a[j][j];a[j]=[x/v for x in a[j]]
        for i in range(n):
            if i!=j:
                v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[j])]
    R=[row[n:] for row in a]
    for i in range(n):
        for j in range(n):
            require(sum((R[i][k]*matrix[k][j] for k in range(n)),Q(0))==Q(i==j),'exact inverse identity')
    return R


def maxabs(x):return max(abs(x.lo),abs(x.hi))


def seed_certificate(theta):
    mm=[bounds_to_i(z) for z in theta['normalized_even_moments']]
    kappas=cumulants(mm);s=[kappas[i]/[1,-2,16,-272][i] for i in range(4)]
    ell=-log_q(Q(2));d=Q(7,8)/ell
    gamma=euler_gamma();S=log_power_tail(2,1)
    H31=sum((Q(1,n) for n in range(1,32)),Q(0))
    A=H31/2-gamma-log_q(Q(2))-d*S
    tails=[]
    for k in (2,4,6,8):
        z=I.q(0)
        for j in range(k+1):z=z+Q(comb(k,j),2**(k-j))*d**j*log_power_tail(k+j,j)
        tails.append(z)
    target=[A]+[s[i]-tails[i] for i in range(3)]
    powers=(1,2,4,6)
    F=[sum((nu*x**k for nu,x in zip(MULTIPLICITIES,CENTERS)),Q(0))-tar for k,tar in zip(powers,target)]
    J=[[Q(nu*k)*x**(k-1) for nu,x in zip(MULTIPLICITIES,CENTERS)] for k in powers]
    R=invert(J)
    beta=max(maxabs(sum((R[i][j]*F[j] for j in range(4)),I.q(0))) for i in range(4))
    box=[I(I.q(x-RADIUS).lo,I.q(x+RADIUS).hi) for x in CENTERS]
    Jbox=[[nu*k*x**(k-1) for nu,x in zip(MULTIPLICITIES,box)] for k in powers]
    L=0
    for i in range(4):
        row=0
        for j in range(4):
            err=I.q(int(i==j))-sum((R[i][k]*Jbox[k][j] for k in range(4)),I.q(0))
            row+=maxabs(err)
        L=max(L,row)
    require(L<SCALE,'whole-box contraction')
    require(Q(beta,SCALE)+Q(L,SCALE)*RADIUS<RADIUS,'whole-box invariant map')
    require(all(x.lo>0 for x in box),'positive weights')
    require(all(box[i].hi<box[j].lo or box[j].hi<box[i].lo for i in range(4) for j in range(i)),'separated weights')
    mismatch=-272*(sum((nu*x**8 for nu,x in zip(MULTIPLICITIES,box)),I.q(0))+tails[3]-s[3])/(s[0]**4)
    require(mismatch.lo>0 or mismatch.hi<0,'complete eighth moment separation')
    return {'head_multiplicities':list(MULTIPLICITIES),'centers':[str(x) for x in CENTERS],
            'box_radius':str(RADIUS),'q_seed':'0','tail_from_n':32,
            'tail_rule':'a_n=1/(2n)+d(q)*log(n)/n^2; d(q)=7/(8*log((1+q)/2))',
            'd0':d.bounds(),'head_sum_A0':A.bounds(),'euler_gamma':gamma.bounds(),
            'tail_power_sums_2_4_6_8':[z.bounds() for z in tails],
            'preconditioner_inverse_identities':16,'preconditioner_inf_norm':str(max(sum(abs(x) for x in row) for row in R)),
            'beta_upper':str(Q(beta,SCALE)),'contraction_upper':str(Q(L,SCALE)),
            'standardized_eighth_moment_mismatch':mismatch.bounds(),
            'even_moments_matched_in_complete_limit':6,
            'growth_coefficients':['1/2','-(1+log(2*pi))/2','7/4'],
            'positive_q_scope':'there exists epsilon>0; for every 0<q<epsilon via analytic IFT; no numerical epsilon certified',
            'explicit_positive_q_radius_certified':False,'all_order_theta_realization_proved':False,
            'Euler_Maclaurin_finite_cut':1024,'Euler_Maclaurin_periodic_remainder':'complete B6 plus omitted B6 boundary term'}

if __name__=='__main__':
    import json
    r=seed_certificate(json.load(open('theta_intervals.json')))
    open('calibrated_chain_results.json','w').write(json.dumps(r,indent=2,sort_keys=True)+'\n')
    for k in ['d0','head_sum_A0','standardized_eighth_moment_mismatch']:
        print(k,[float(Q(x)) for x in r[k]])
    for k in ['beta_upper','contraction_upper','preconditioner_inf_norm']:print(k,float(Q(r[k])))
