#!/usr/bin/env python3
"""Nonvalidated high-precision checks of weighted local Selberg obstruction.
Only the shrinking physical-space interval is integrated, not the full zeta norm.
The proof is audits/adversarial_reviews/weighted_selberg_round2.md.
"""
from pathlib import Path
import json
import mpmath as mp
mp.mp.dps=60

def mobius(n):
    p=2;ans=1
    while p*p<=n:
        if n%p==0:
            n//=p;ans=-ans
            if n%p==0:return 0
            while n%p==0:n//=p
        p+=1
    if n>1:ans=-ans
    return ans

def g_over_u(u,q):
    # g=-sin(2piu)/pi; each I multiplies u^(2k+1) by1/(2k+1).
    return mp.fsum((-1)**(k+1)*(2*mp.pi)**(2*k+1)*u**(2*k)/(mp.pi*mp.factorial(2*k+1)*(2*k+1)**(q-1)) for k in range(70))

def main():
    rows=[]
    for N in [2,10,100]:
        C=mp.fsum(mobius(n)*(1-mp.log(n)/mp.log(N)) for n in range(1,N+1))
        for q in range(1,7):
            endpoint=mp.mpf(1)/N
            local=mp.sqrt(mp.quad(lambda u:(C-g_over_u(u,q))**2,[0,endpoint]))
            lower=abs(C+2)/mp.sqrt(N)-4*mp.pi**2/(3**q*mp.sqrt(5))*N**(-mp.mpf(5)/2)
            assert local+mp.mpf('1e-50')>=lower
            if q==2:
                u=endpoint
                assert abs(u*g_over_u(u,q)+mp.si(2*mp.pi*u)/mp.pi)<mp.mpf('1e-50')
            rows.append({'N':N,'q':q,'C_N':mp.nstr(C,25),'local_norm_lower_bound_for_full_dq':mp.nstr(local,25),'explicit_triangle_bound':mp.nstr(lower,25)})
    out=Path(__file__).resolve().parents[1]/'results'/'weighted_selberg_local.json'
    out.write_text(json.dumps({'status':'nonvalidated60-digit observations; full d_q not computed','series_terms':70,'rows':rows},indent=2)+'\n')
    print('Checked18 local norm bounds; q2 primitive also agrees with sine integral.')
if __name__=='__main__':main()
