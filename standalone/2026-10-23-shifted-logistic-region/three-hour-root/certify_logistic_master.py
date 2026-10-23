"""Directed-interval certificate for the proposed exact-logistic inequality.

The mathematical reduction and all imported theorems are separate obligations.
This program certifies a sufficient scalar inequality over a full rectangle.
Requires mpmath 1.3.0, whose iv context uses outward-rounded libmp arithmetic.
"""
from pathlib import Path
import sys, json, hashlib, time, math
from fractions import Fraction as Q

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'python-deps'))
import mpmath
from mpmath import iv
iv.dps = 70

def q(x):
    x = Q(x)
    return iv.mpf(x.numerator) / x.denominator

def box(lo, hi):
    return iv.mpf([q(lo).a, q(hi).b])

theta = q('1.1338')
k = iv.tan(theta)
cot = 1/k
sec2 = 1/iv.cos(theta)**2
U = 2*theta*cot
w0 = sec2*(theta*k+3*theta*cot-3)
a1 = q(Q(865534,497079))
aP = q(Q(2919857,828465))
N = 24
J_N = 48

# Exact integral recurrence C_n = int_0^U v^n exp(i k v) dv.
ik = iv.mpc(0,k)
ep = iv.exp(ik*U)
cs = [(ep-1)/ik]
for n in range(1,N+2):
    cs.append(U**n*ep/ik-n*cs[-1]/ik)
moments = []
for n in range(N+1):
    moments.append(sec2*((sec2*theta*cot-1)*cs[n].real
        -sec2*cs[n+1].real/2
        +(2*theta*cot-2)*U**(n+1)/(n+1)-U**(n+2)/(n+2)
        +(2*cot-1/iv.tan(2*theta))*cs[n].imag))

def W(z):
    if not (z >= -1 and z <= 1):
        raise ValueError('W Taylor domain exceeded')
    out = moments[-1]/math.factorial(N)
    for n in range(N-1,-1,-1):
        out = out*(-z)+moments[n]/math.factorial(n)
    # w<=6, U<1.1: exponential Taylor remainder < 1e-20.
    return out+box('-1e-20','1e-20')

def J(z,a):
    """int exp(-zu)/(1+exp(a u)) du with a positive beta series."""
    b = z+a
    if not (a>0 and b>0):
        raise ValueError('J convergence domain exceeded')
    term = 1/(2*b)
    out = term
    for n in range(1,J_N+1):
        term = term*n*a/(2*(b+n*a))
        out += term
    # Terms after index J_N sum <= 2^(-J_N-1)/b.
    tail = 1/(2**(J_N+1)*b)
    return out+iv.mpf([0,tail.b])

def margin(A,l):
    c = iv.log(16+q(10**10)*iv.exp(-l))
    mu = 1/(1+c/l)
    eta = A/l
    sigma = 1-A/(l+c)
    a = 2*sigma-1
    z0 = sigma-1
    z1 = z0+eta
    z2 = sigma-eta
    base = a1*W(1-mu)-W(-mu)
    corr = eta*w0*(a1/z2+J(z0,a)-a1*J(z1,a)-a1*J(z2,a))
    # Global Taylor bound |w(v)-w0| <= 1000 v^2/2, also beyond U.
    error = 1000*eta**3*(1/(z0+a)**3+a1/(z1+a)**3+a1/z2**3)
    # Carch <= -3.0126. The 1e-7 budget absorbs the bounded errors.
    resource = w0*(A*aP/4-q('3.0126')*eta/2)+q('1e-7')
    return base+corr-error-resource

def main():
    start = time.monotonic()
    if not (w0>q('5.67') and w0<6 and U<q('1.1')):
        raise RuntimeError('kernel constant check failed')
    if not (q('6.6')*q('3.1')*q('1.1')**25/math.factorial(25)<q('1e-20')):
        raise RuntimeError('Taylor remainder check failed')
    if not (iv.exp(q('21.233')*q(Q(25,121)))<81):
        raise RuntimeError('Littlewood endpoint check failed')
    if not (iv.log(q(3*10**12))>28):
        raise RuntimeError('verified-height lower endpoint check failed')
    pending = [(Q(0),Q(25,121),Q(28),Q(81),0)]
    accepted = []
    worst = None
    evaluations = 0
    while pending:
        al,ah,ll,lh,depth = pending.pop()
        value = margin(box(al,ah),box(ll,lh))
        evaluations += 1
        if value>0:
            lower = value.a
            if worst is None or lower<worst:
                worst = lower
            accepted.append([str(al),str(ah),str(ll),str(lh),str(value)])
            continue
        if depth>=28:
            raise RuntimeError(f'unresolved box: {al,ah,ll,lh,value}')
        # Width sensitivity: resource changes by about 5 dA, height by .001 dl.
        if 5*(ah-al)>Q('0.001')*(lh-ll):
            mid = (al+ah)/2
            pending.extend([(al,mid,ll,lh,depth+1),(mid,ah,ll,lh,depth+1)])
        else:
            mid = (ll+lh)/2
            pending.extend([(al,ah,ll,mid,depth+1),(al,ah,mid,lh,depth+1)])
    out = {
        'status':'PASS',
        'scope':'scalar sufficient inequality only; analytic and imported inputs separate',
        'arithmetic':f'mpmath {mpmath.__version__} iv, {iv.dps} decimal digits, outward rounded',
        'domain':{'A':['0','25/121'],'log_t':['28','81']},
        'W_degree':N,'J_last_index':J_N,
        'strict_rule':'every closed rational subrectangle has interval lower endpoint > 0',
        'accepted_boxes':len(accepted),'evaluations':evaluations,
        'minimum_certified_lower_bound':str(worst),
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'seconds':time.monotonic()-start,
        'boxes':accepted,
    }
    dest=Path(__file__).with_name('LOGISTIC_MASTER_CERTIFICATE.json')
    dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='boxes'},indent=2))

if __name__=='__main__':
    main()
