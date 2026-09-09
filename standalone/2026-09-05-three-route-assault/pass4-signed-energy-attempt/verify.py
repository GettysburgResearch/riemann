"""Bounded exact controls and an elementary rational enclosure of the source H.

No finite check establishes an infinite Laguerre sum, Tauberian theorem,
all-radius norm bound, matrix positivity, or RH. See PROOF.md.
Standard library only. No assert statement is used for acceptance.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from math import comb, factorial, isqrt
from pathlib import Path
import argparse
import hashlib
import json
import unittest


def rational(x):
    if isinstance(x, (bool, float)):
        raise TypeError('exact rational input required')
    return F(x)


@dataclass(frozen=True)
class Q:
    re: F = F(0)
    im: F = F(0)
    def __post_init__(self):
        object.__setattr__(self, 're', rational(self.re))
        object.__setattr__(self, 'im', rational(self.im))
    @staticmethod
    def of(x):
        return x if isinstance(x, Q) else Q(x)
    def __add__(self, x):
        x = Q.of(x); return Q(self.re + x.re, self.im + x.im)
    __radd__ = __add__
    def __neg__(self):
        return Q(-self.re, -self.im)
    def __sub__(self, x):
        return self + -Q.of(x)
    def __rsub__(self, x):
        return Q.of(x) + -self
    def __mul__(self, x):
        x = Q.of(x)
        return Q(self.re*x.re-self.im*x.im, self.re*x.im+self.im*x.re)
    __rmul__ = __mul__
    def conj(self):
        return Q(self.re, -self.im)
    def norm2(self):
        return self.re**2+self.im**2
    def __truediv__(self, x):
        x = Q.of(x)
        if not x.norm2(): raise ZeroDivisionError('Gaussian rational zero')
        y = self*x.conj()
        return Q(y.re/x.norm2(), y.im/x.norm2())
    def __rtruediv__(self, x):
        return Q.of(x)/self


def log_interval(x, terms=40):
    x = rational(x)
    if x <= 0: raise ValueError('positive logarithm argument required')
    if type(terms) is not int or terms < 1: raise ValueError('positive integer terms')
    if x < 1:
        lo, hi = log_interval(1/x, terms)
        return -hi, -lo
    k = 0
    while x >= 2:
        x /= 2; k += 1
    def base(t):
        z = (t-1)/(t+1)
        lo = 2*sum((z**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
        err = 2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
        return lo, lo+err
    a, b = base(x); c, d = base(F(2))
    return a+k*c, b+k*d


def atan_interval(x, terms=16):
    x = rational(x)
    if not 0 <= x <= 1: raise ValueError('atan argument must be in [0,1]')
    if type(terms) is not int or terms < 1: raise ValueError('positive integer terms')
    s = sum((F((-1)**j)*x**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    other = s+F((-1)**terms)*x**(2*terms+1)/F(2*terms+1)
    return min(s, other), max(s, other)


def interval_text(lo, hi, digits=24):
    scale = 10**digits
    a = (lo*scale).numerator//(lo*scale).denominator
    q = hi*scale
    b = -((-q.numerator)//q.denominator)
    def fixed(n):
        sign = '-' if n < 0 else ''; n = abs(n)
        return f'{sign}{n//scale}.{n%scale:0{digits}d}'
    return [fixed(a), fixed(b)]


def source_certificate():
    # H_N-log(N+1) < gamma_E < H_N-log N, proved by integral comparison.
    n = 512
    harmonic = sum((F(1,k) for k in range(1,n+1)), F(0))
    ln = log_interval(F(n)); lnp = log_interval(F(n+1))
    glo, ghi = harmonic-lnp[1], harmonic-ln[0]
    a = atan_interval(F(1,5)); b = atan_interval(F(1,239))
    plo, phi = 16*a[0]-4*b[1], 16*a[1]-4*b[0]
    llo = log_interval(4*plo)[0]; lhi = log_interval(4*phi)[1]
    hlo, hhi = 1+glo/2-lhi/2, 1+ghi/2-llo/2
    if not (0 < hlo <= hhi < F(1,40)):
        raise ArithmeticError('source H enclosure did not certify 0<H<1/40')
    clo, chi = 1+F(201,68)/phi**2, 1+F(201,68)/plo**2
    return {
        'method': 'EXACT_RATIONAL_SERIES_AND_ELEMENTARY_ANALYTIC_REMAINDERS',
        'harmonic_n': n, 'log_terms': 40, 'atan_terms': 16,
        'H_outward_decimal_interval': interval_text(hlo,hhi),
        'pi_outward_decimal_interval': interval_text(plo,phi),
        'linear_diagonal_constant_outward_decimal_interval': interval_text(clo,chi),
        'proved_bound': '0 < H < 1/40',
        'signed_convergence_radius_squared': '317/325',
        'no_zero_data_used': True,
    }


def mobius(n):
    if type(n) is not int or n < 1: raise ValueError('positive integer required')
    out, p, v = 1, 2, n
    while p*p <= v:
        if v % p == 0:
            v //= p; out = -out
            if v % p == 0: return 0
        p += 1
    return -out if v > 1 else out


def hh_coefficient(n,a,b):
    total=F(0)
    for j in range(min(a,b)+1):
        k,l=a-j,b-j
        if j+k+l <= n:
            total += F((-1)**(k+l)*comb(n+j,n-j-k-l),
                       factorial(j)**2*factorial(k)*factorial(l))
    return total


class Checks:
    def __init__(self): self.counts={}
    def __call__(self, name, condition):
        if not condition: raise ArithmeticError('control failed: '+name)
        self.counts[name]=self.counts.get(name,0)+1


def reconstruct():
    check=Checks()
    for n in range(8):
        for a in range(n+1):
            for b in range(n+1):
                lhs=F((-1)**(a+b)*comb(n,a)*comb(n,b),factorial(a)*factorial(b))
                check('Hille_Hardy_coefficient_identity', lhs==hh_coefficient(n,a,b))
    for q in [F(1,2),F(2,3),F(3,4),F(4,5),F(9,10),F(99,100)]:
        r=q*q; alpha=4*r/(1-r); beta=4*q/(1-r)
        s=(3+r)/(2*(1-r)); radius=2*q/(1-r)
        check('continuous_diagonal_discriminant', (2+alpha)**2-beta**2==4)
        check('Bessel_weight_exponent', 3+alpha-beta==(3-q)/(1+q)>1)
        check('Abel_error_constant', beta>=2/(1-r))
        for t in [F(0),F(1,3),F(1),F(2)]:
            z=Q((1-t*t)/(1+t*t),2*t/(1+t*t))
            phi=(z-q)/(1-q*z)
            w=F(1,2)+(1+q*z)/(1-q*z)
            check('disk_automorphism',w==s+radius*phi)
            check('disk_automorphism',phi.norm2()==1)
    for rho in [F(-1),F(0),F(3,4),F(4,5)]:
        c=F(3,2)-rho; d=F(1,2)+rho
        for r in [F(1,16),F(1,4),F(9,25),F(1,2),F(4,5),F(99,100)]:
            s=(3+r)/(2*(1-r)); radius2=4*r/(1-r)**2
            lhs=(s-rho)**2-radius2
            rhs=(c*c-r*d*d)/(1-r)
            check('pole_norm_threshold_identity',lhs==rhs)
    # Deliberate inside-pole case: finite meromorphic circle integral is NOT the Taylor norm.
    rho=F(3,4);r=F(1,2);s=(3+r)/(2*(1-r));radius2=4*r/(1-r)**2
    check('meromorphic_circle_is_not_Taylor_norm',(s-rho)**2-radius2<0)
    for q in [2,3,67]:
        for x in range(1,129):
            literal=sum(mobius(k)**2 for k in range(1,x+1) if k%q)
            inverse=0;power=1;sign=1
            while power<=x:
                inverse+=sign*sum(mobius(k)**2 for k in range(1,x//power+1))
                power*=q;sign=-sign
            check('squarefree_local_factor_inverse',literal==inverse)
    for x in [F(80),F(100),F(1000)]:
        for delta in [F(1,100),F(1,10),F(1,4),F(49,100)]:
            gamma2=x-F(1,4)+delta**2
            z2=(gamma2+(delta-1)**2)/(gamma2+(delta+1)**2)
            check('off_line_source_radius_geometry',
                  1-z2==4*delta/(x+F(3,4)+2*delta+2*delta**2))
            check('off_line_source_radius_geometry',z2>F(317,325))
    check('constant_arithmetic',1-F(2)/(79+F(9,4))==F(317,325))
    check('constant_arithmetic',14**2<2*10**2)
    check('constant_arithmetic',F(24,7)+F(67,66)<5)
    source=source_certificate()
    return {'status':'PASS_BOUNDED_ALGEBRA_AND_H_SOURCE',
            'arithmetic':'EXACT_RATIONAL_AND_GAUSSIAN_RATIONAL',
            'controls':check.counts,'distinct_controls':sum(check.counts.values()),
            'source_certificate':source,
            'RH_proved':False,'all_radius_energy_bound_proved':False,
            'analytic_proofs_machine_verified':False}


def canonical(result):
    return json.dumps(result,sort_keys=True,indent=2)+'\n'


def check_saved(text,result):
    if text!=canonical(result): raise ValueError('stored result differs from recomputation')


class Tests(unittest.TestCase):
    def test_float_rejected(self):
        with self.assertRaises(TypeError):Q(0.1)
    def test_bool_rejected(self):
        with self.assertRaises(TypeError):Q(True)
    def test_invalid_log(self):
        with self.assertRaises(ValueError):log_interval(0)
    def test_invalid_terms(self):
        with self.assertRaises(ValueError):log_interval(2,True)
    def test_bad_atan(self):
        with self.assertRaises(ValueError):atan_interval(2)
    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):Q(1)/Q()
    def test_log_reciprocal(self):
        lo,hi=log_interval(F(2,3));a,b=log_interval(F(3,2))
        self.assertEqual((lo,hi),(-b,-a))
    def test_changed_result(self):
        with self.assertRaises(ValueError):check_saved('{"RH_proved":true}\n',{'RH_proved':False})
    def test_bool_integer_alias(self):
        with self.assertRaises(ValueError):check_saved(canonical({'n':True}),{'n':1})
    def test_mobius_domain(self):
        with self.assertRaises(ValueError):mobius(True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true')
    p.add_argument('--tests',action='store_true');args=p.parse_args()
    if args.tests:
        result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Tests))
        raise SystemExit(0 if result.wasSuccessful() else 1)
    result=reconstruct();path=Path(__file__).with_name('RESULTS.json')
    if args.write: path.write_text(canonical(result))
    else: check_saved(path.read_text(),result)
    print(result['status']);print(result['distinct_controls'],'bounded controls; analytic proof not machine verified')
