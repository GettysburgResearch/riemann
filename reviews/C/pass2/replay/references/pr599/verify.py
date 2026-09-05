#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
import hashlib, json, math
from pathlib import Path

HERE=Path(__file__).resolve().parent


def base_u(x: Fraction) -> Fraction:
    # Zero extension plus a nontrivial rational model.
    return Fraction(0) if x < 1 else x + 2 + Fraction(1, x.numerator + x.denominator)


def euler(primes, x):
    total=Fraction(0)
    for r in range(len(primes)+1):
        for subset in combinations(primes,r):
            d=1
            for p in subset:
                d*=p
            total += (-1)**r * Fraction(1,d) * base_u(x/Fraction(d))
    return total


def largest_prime_telescope(small, large, x):
    current=euler(small,x)
    debt=Fraction(0)
    installed=list(small)
    for p in sorted(large):
        child=euler(installed,x/Fraction(p))
        debt += Fraction(1,p)*child
        installed.append(p)
    return current-debt


def product_boundary_split(small, large, x, constant, cutoff):
    uz=lambda y:euler(small,y)
    main=constant
    for p in large:
        main*=Fraction(p-1,p)
    bulk=Fraction(0); boundary=Fraction(0)
    for r in range(len(large)+1):
        for subset in combinations(large,r):
            v=1
            for p in subset:
                v*=p
            eps=uz(x/Fraction(v))-constant
            term=(-1)**r*Fraction(1,v)*eps
            if v<=cutoff:
                bulk+=term
            else:
                boundary+=term
    return main,bulk,boundary


x=Fraction(420)
small=[2,3]
large=[5,7]
full=euler(small+large,x)
tel=largest_prime_telescope(small,large,x)
assert full==tel

# Exact positive-main plus product-boundary identity on a finite toy source.
constant=Fraction(17,11)
main,bulk,boundary=product_boundary_split(small,large,x,constant,6)
assert full==main+bulk+boundary

# Numerical asymptotic sanity for kappa=0.1 and beta=0.7<1-2kappa.
kappa=0.1; beta=0.7
rows=[]
for L in [10**4,10**5,10**6,10**7,10**8]:
    ell=math.log(L)
    Z=(kappa*L*ell)**2
    logZ=math.log(Z)
    error_exp=2*math.sqrt(Z)/logZ/L
    boundary_exp=kappa+(beta-1)/2
    omega=max(2.0,math.log(max(3.0,ell)))
    H=math.sqrt(L/logZ)/omega
    strip_ratio=H*H*logZ/L
    rows.append({
      'logX':L,
      'error_exponent_over_logX':error_exp,
      'bulk_power_exponent':boundary_exp,
      'terminal_strip_ratio_proxy':strip_ratio})
assert rows[-1]['error_exponent_over_logX'] < 0.5
assert rows[-1]['bulk_power_exponent'] < 0
assert rows[-1]['terminal_strip_ratio_proxy'] < rows[0]['terminal_strip_ratio_proxy']

result={
 'schema':'riemann.x97910.near-critical-factor67.v2',
 'frozen':{
  'pr576':'0f6ea6eae813c1d867ae50744cf5fd57e2720bb7',
  'pr578':'981bfef5fcfa3a39ccf4f50875cf8a6057650268',
  'pr589':'ff5156cf6aa469bb7a2155ff4aa7c094bd75b9b6',
  'pr590':'223f11259b3e7134f78d6492795e6e94caca8be3'},
 'toy_full_euler':str(full),
 'toy_largest_prime_telescope':str(tel),
 'toy_positive_main':str(main),
 'toy_bulk_error':str(bulk),
 'toy_product_boundary':str(boundary),
 'cutoff':'kappa^2*(logX*loglogX)^2 with kappa<1/2',
 'product_bulk_condition':'beta<1-2*kappa',
 'terminal_strip_condition':'H^2*logZ=o(logX)',
 'asymptotic_sanity':rows,
 'proved_by_replay':[
  'finite_euler_factorization',
  'largest_prime_owner_telescope',
  'positive_main_plus_product_boundary_identity',
  'normalized_1_over_p_coefficient'],
 'not_proved_by_replay':['PNT','Mertens','DLPBR67','RH'],
 'rh_established':False,
 'verdict':'PASS_X97910_NEAR_CRITICAL_FACTOR67_ALGEBRA'}
canon=json.dumps(result,sort_keys=True,separators=(',',':')).encode()
result['proof_object_sha256']=hashlib.sha256(canon).hexdigest()
out=HERE/'results'/'verification.json';out.parent.mkdir(parents=True,exist_ok=True)
# Pin UTF-8 and LF so replay regenerates the same retained artifact on every OS.
with out.open('w', encoding='utf-8', newline='\n') as handle:
    handle.write(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(result['verdict']);print(result['proof_object_sha256'])
