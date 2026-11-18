#!/usr/bin/env python3
"""Numerical stress test of a stable divided-difference cluster basis.
Uses mpmath; observations only, not validated numerics or proof.
Analytic uniform proof: audits/adversarial_reviews/multicluster_skeptic_round2.md.
"""
from pathlib import Path
import json
import mpmath as mp
mp.mp.dps=70
R=80

def coefficients(nodes):
    ans=[]
    for j in range(len(nodes)):
        h=[mp.mpf(1)]+[mp.mpf(0)]*R
        for c in nodes[:j+1]:
            for r in range(1,R+1): h[r]+=c*h[r-1]
        a=[mp.mpc(0)]*j+[mp.factorial(j)*(1j**r)*h[r]/mp.factorial(r+j) for r in range(R+1)]
        ans.append(a)
    return ans

def values(a,x):
    out=[]
    for p in a:
        v=mp.mpc(0)
        for b in reversed(p):v=v*x+b
        out.append(v)
    return out

def continuous_gram(a):
    m=len(a); H=mp.matrix(m)
    for i in range(m):
        for j in range(m):
            H[i,j]=mp.fsum(a[i][p]*mp.conj(a[j][q])/mp.mpf(p+q+1) for p in range(len(a[i])) for q in range(len(a[j])))
    return H

def discrete_gram(a,L):
    m=len(a);H=mp.matrix(m)
    for k in range(L+1):
        v=values(a,mp.mpf(k)/L)
        for i in range(m):
            for j in range(m):H[i,j]+=v[i]*mp.conj(v[j])/(L+1)
    return H

def main():
    tiny=mp.mpf('1e-35')
    cases=[('two_separated',[-1,1]),('triple_collision',[0,0,0]),('triple_tiny_gaps',[0,tiny,2*tiny]),('two_double_clusters',[-1,-1,1,1]),('two_near_double_clusters',[-1,-1+tiny,1,1+tiny]),('five_separated',[-1,mp.mpf('-.5'),0,mp.mpf('.5'),1])]
    rows=[]
    for label,ns in cases:
        nodes=list(map(mp.mpf,ns));m=len(nodes);a=coefficients(nodes)
        H=continuous_gram(a);invH=H**-1;F=mp.re(invH[0,0]);sample=[]
        ends=[values(a,mp.mpf(0)),values(a,mp.mpf(1))]
        Bend=mp.matrix(m)
        for i in range(m):
            for j in range(m):Bend[i,j]=sum(v[i]*mp.conj(v[j]) for v in ends)/2
        beta=mp.re((invH*Bend*invH)[0,0])
        for L in sorted(set([m,m+1,10,30,100])):
            HL=discrete_gram(a,L);E=mp.re((HL**-1)[0,0])/(L+1)
            if label=='triple_collision':
                exact=1-mp.fprod(L-j for j in range(m))/mp.fprod(L+j for j in range(1,m+1))
                assert abs(E-exact)<mp.mpf('1e-60')
            sample.append({'L':L,'L_times_optimal_error':mp.nstr(L*E,25),'L_times_absolute_remainder':mp.nstr(L*abs(L*E-F),25),'L_squared_times_corrected_remainder':mp.nstr(L**2*abs(L*E-F+beta/(L+1)),25)})
        rows.append({'case':label,'nodes':[mp.nstr(c,45) for c in nodes],'F_continuous':mp.nstr(F,30),'beta_endpoint_correction':mp.nstr(beta,30),'samples':sample})
        print(label,mp.nstr(F,15))
    result={'status':'nonvalidated 70-digit observations; analytic theorem proved separately','basis':'Taylor-complete-homogeneous representation of confluent divided differences','series_terms':R+1,'rows':rows,'alias_warning':'Distinct frequencies separated by2piL alias on the grid. Actual polynomial multiplicity must replace repeated value constraints; inverse of the aliased value Gram is invalid.'}
    out=Path(__file__).resolve().parents[1]/'results'/'multicluster_skeptic.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()
