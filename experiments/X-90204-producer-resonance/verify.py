#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80
ROOT = Path(__file__).resolve().parent
RESULT = ROOT / 'results' / 'verification.json'

UC = mp.mpc(
    '0.949355820679586211593486084525846386696284785705856800769148',
    '45.6758054724367699233385513742096251132291669065325170029954',
)
RADIUS = mp.mpf('1e-10')
M = 50000
NETA = 10000


def Delta(u):
    return 1 - mp.mpf('0.5') * (
        mp.power(2, 1-u) + mp.power(3, -u) + mp.power(mp.mpf(3)/2, -u)
    )


def Deltap(u):
    return mp.mpf('0.5') * (
        mp.log(2)*mp.power(2,1-u) + mp.log(3)*mp.power(3,-u)
        + mp.log(mp.mpf(3)/2)*mp.power(mp.mpf(3)/2,-u)
    )


def tau3(m: int) -> int:
    r=m%3
    if r==0: return 2*m//3
    if r==1: return (m+2)//3
    return (2*m-1)//3


def producer_a(N: int):
    # n=2 sparse producer trace: G(2)=2, G(3)=2, hence a(2)=2,a(3)=0,a(4)=2.
    a=[mp.mpf('0')]*(N+1)
    a[2]=2; a[3]=0; a[4]=2
    for m in range(5,N+1):
        a[m]=(a[(m+1)//2]+a[tau3(m)])/2
    return a


def numerator_partial(u, a):
    B=mp.mpc(0)
    for m in range(1,5):
        b=a[m]-a[(m+1)//2]/2-a[tau3(m)]/2
        B += b*mp.power(m,-u)
    R2=mp.mpc(0); R3=mp.mpc(0)
    for r in range(1,len(a)):
        ar=a[r]
        if ar == 0: continue
        R2 += ar*(mp.power(2*r-1,-u)-mp.power(2*r,-u))
        qr=mp.mpf(3*r)/2 if r%2==0 else mp.mpf(3*r+1)/2
        R3 += ar*(mp.power(3*r-2,-u)-mp.power(3*r,-u)
                  +mp.power(qr,-u)-mp.power(mp.mpf(3*r)/2,-u))
    return B, R2, R3, B+(R2+R3)/2


def eta_partial(u,N):
    return mp.fsum([(1 if n%2 else -1)*mp.power(n,-u) for n in range(1,N+1)])


def main():
    sigma_min=mp.re(UC)-RADIUS
    U=abs(UC)+RADIUS
    residual=abs(Delta(UC))
    dp=abs(Deltap(UC))
    # Directed interval re-evaluation of the two load-bearing point values.
    mp.iv.dps = 80
    uiv=mp.iv.mpc([str(mp.re(UC)),str(mp.re(UC))],[str(mp.im(UC)),str(mp.im(UC))])
    div=1-mp.iv.mpf('0.5')*(mp.iv.power(2,1-uiv)+mp.iv.power(3,-uiv)+mp.iv.power(mp.iv.mpf(3)/2,-uiv))
    dpiv=mp.iv.mpf('0.5')*(mp.iv.log(2)*mp.iv.power(2,1-uiv)+mp.iv.log(3)*mp.iv.power(3,-uiv)+mp.iv.log(mp.iv.mpf(3)/2)*mp.iv.power(mp.iv.mpf(3)/2,-uiv))
    residual_iv_upper=mp.mpf(str(float(abs(div).b)))
    dp_iv_lower=mp.mpf(str(float(abs(dpiv).a)))
    assert residual_iv_upper < mp.mpf('1e-55')
    assert dp_iv_lower > mp.mpf('0.67')
    d2_bound=mp.mpf('0.5')*((mp.log(2)**2)*mp.power(2,1-sigma_min)
                +(mp.log(3)**2)*mp.power(3,-sigma_min)
                +(mp.log(mp.mpf(3)/2)**2)*mp.power(mp.mpf(3)/2,-sigma_min))
    # Rouche on |w|=RADIUS comparing Delta(UC+w) with Delta'(UC)w.
    rouche_margin=dp*RADIUS-residual-d2_bound*RADIUS**2/2
    assert rouche_margin > mp.mpf('6e-11')

    a=producer_a(M)
    assert max(abs(x) for x in a[:5]) == 2
    B,R2,R3,part=numerator_partial(UC,a)
    # L-90205 tail: 1/2*(1+2.5)*A0*|u| sum_{r>M}r^{-sigma-1}
    A0=mp.mpf(2)
    tail=mp.mpf('1.75')*A0*U*mp.power(M,-sigma_min)/sigma_min

    # Global derivative bound on the numerator in the root disk.
    S0=1+1/sigma_min
    Slog=mp.mpf(3)  # safe bound for sum log(r) r^{-sigma-1}, sigma>0.949
    r2prime=A0*(S0+U*(mp.log(2)*S0+Slog))
    r3prime=A0*mp.mpf('2.5')*(S0+U*(mp.log(3)*S0+Slog))
    # producer defect b2=2,b3=-2,b4=0
    bprime=2*mp.log(2)*mp.power(2,-sigma_min)+2*mp.log(3)*mp.power(3,-sigma_min)
    nprime=bprime+(r2prime+r3prime)/2
    variation=nprime*RADIUS
    num_lower=abs(part)-tail-variation-mp.mpf('1e-50')
    assert num_lower > mp.mpf('0.009')

    eta=eta_partial(UC,NETA)
    eta_tail=U*mp.power(NETA,-sigma_min)/sigma_min
    # Crude finite-part derivative bound; 2* integral is very generous here.
    aa=1-sigma_min
    integral=mp.power(NETA,aa)*(mp.log(NETA)/aa-1/aa**2)+1/aa**2
    eta_var=2*integral*RADIUS
    eta_lower=abs(eta)-eta_tail-eta_var-mp.mpf('1e-50')
    assert eta_lower > mp.mpf('0.61')
    den=1-mp.power(2,1-UC)
    den_var=mp.log(2)*mp.power(2,1-sigma_min)*RADIUS
    den_lower=abs(den)-den_var
    assert den_lower > mp.mpf('0.24')

    result={
        'verdict':'PASS_X_90204_PRODUCER_RESONANCE',
        'root_center':{'re':mp.nstr(mp.re(UC),70),'im':mp.nstr(mp.im(UC),70)},
        'root_radius':mp.nstr(RADIUS,10),
        'delta_center_abs':mp.nstr(residual,20),
        'delta_center_interval_upper':mp.nstr(residual_iv_upper,20),
        'delta_prime_abs':mp.nstr(dp,20),
        'delta_prime_interval_lower':mp.nstr(dp_iv_lower,20),
        'delta_second_derivative_bound':mp.nstr(d2_bound,20),
        'rouche_margin':mp.nstr(rouche_margin,20),
        'producer_numerator':{
            'terms':M,
            'B':mp.nstr(B,30),'R2':mp.nstr(R2,30),'R3':mp.nstr(R3,30),
            'partial':mp.nstr(part,30),'partial_abs':mp.nstr(abs(part),20),
            'tail_bound':mp.nstr(tail,20),'disk_variation_bound':mp.nstr(variation,20),
            'certified_lower_abs':mp.nstr(num_lower,20),
        },
        'zeta_nonzero_via_eta':{
            'terms':NETA,'eta_partial':mp.nstr(eta,30),'eta_partial_abs':mp.nstr(abs(eta),20),
            'eta_tail_bound':mp.nstr(eta_tail,20),'eta_disk_variation_bound':mp.nstr(eta_var,20),
            'eta_certified_lower_abs':mp.nstr(eta_lower,20),
            'one_minus_2_power_certified_lower_abs':mp.nstr(den_lower,20),
        },
        'pole_s':{'re_lower':mp.nstr(mp.re(UC)-RADIUS-mp.mpf('0.5'),20),
                  're_upper':mp.nstr(mp.re(UC)+RADIUS-mp.mpf('0.5'),20)},
        'omega_exponent':mp.nstr(mp.re(UC)-RADIUS-mp.mpf('0.5'),20),
    }
    print(result['verdict'])
    print(json.dumps(result,indent=2))
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__': main()
