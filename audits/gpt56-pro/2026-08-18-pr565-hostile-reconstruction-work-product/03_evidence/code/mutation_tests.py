#!/usr/bin/env python3
from __future__ import annotations
import json
import mpmath as mp
from pathlib import Path
mp.mp.dps=80
PRIMES=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
X=184

def divisors(cap, flip_two=False):
    out=[]
    def rec(i,d,mu):
        if i==len(PRIMES): out.append((d,mu)); return
        rec(i+1,d,mu)
        p=PRIMES[i]
        if d<=cap//p:
            next_mu=-mu
            if flip_two and p==2: next_mu=mu
            rec(i+1,d*p,next_mu)
    rec(0,1,1)
    return out

def evaluate(q4=3, flip_two=False):
    def q(m):
        if m<2:return 0
        if m==2:return 15
        if m==3:return 6
        if m==4:return q4
        return 6
    def H(x,n):
        if x<=n:return mp.mpf(0)
        return min(mp.log(4),mp.log(x/n))
    def A(x):
        return mp.fsum(mp.mpf(q(m))/mp.sqrt(m)*H(x,m) for m in range(2,int(mp.floor(x))+1)) if x>=2 else mp.mpf(0)
    ds=divisors(X//2,flip_two)
    F=mp.fsum(mp.mpf(mu)/mp.sqrt(d)*A(mp.mpf(X)/d) for d,mu in ds)
    M=mp.fsum(mp.mpf(1)/mp.sqrt(d)*A(mp.mpf(X)/d) for d,mu in ds)
    return F,M,F/M

base=evaluate()
q4=evaluate(q4=4)
flip=evaluate(flip_two=True)
original_verify=Path(__file__).resolve().parents[2]/'02_original_recovery_packet/extracted/riemann-parity-contractive-annular-97100-recovery/experiments/X-97100-parity-contraction/results/verification.json'
old=json.loads(original_verify.read_text())
result={
 'baseline_ratio':mp.nstr(base[2],50),
 'baseline_refutes_1_over_40':bool(base[2] < mp.mpf(1)/40),
 'mutate_q4_ratio':mp.nstr(q4[2],50),
 'mutate_q4_detected':bool(abs(q4[2]-base[2])>mp.mpf('1e-8')),
 'mutate_prime2_mobius_ratio':mp.nstr(flip[2],50),
 'mutate_prime2_detected':bool(abs(flip[2]-base[2])>mp.mpf('1e-8')),
 'old_checker_replayed_directed_certificate':old['bias_contract']['directed_certificate_replayed_here'],
 'old_checker_rh_established':old['rh_established'],
}
assert result['baseline_refutes_1_over_40']
assert result['mutate_q4_detected']
assert result['mutate_prime2_detected']
assert result['old_checker_replayed_directed_certificate'] is False
assert result['old_checker_rh_established'] is False
print(json.dumps(result,indent=2))
