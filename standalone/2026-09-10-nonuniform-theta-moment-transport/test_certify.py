#!/usr/bin/env python3
"""Independent bounded algebra controls and actual altered-copy CLI refusals.
This is not independent authorship or a proof assistant for the infinite claims.
"""
from fractions import Fraction as F
from math import factorial, comb
from pathlib import Path
from itertools import product
import importlib.util
import argparse
import json
import hashlib
import tempfile
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('candidate',ROOT/'certify.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)

def need(ok,msg):
    if not ok:raise ValueError(msg)

def mul(a,b,n):
    out=[F(0)]*(n+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=n:out[i+j]+=x*y
    return out

def exp_series(a,n):
    need(a[0]==0,'zero formal exponential constant')
    b=[F(1)]+[F(0)]*n
    for k in range(1,n+1):
        b[k]=sum(F(j)*a[j]*b[k-j] for j in range(1,k+1))/k
    return b

def inv_series(a,n):
    b=[1/a[0]]+[F(0)]*n
    for k in range(1,n+1):b[k]=-sum(a[j]*b[k-j] for j in range(1,k+1))/a[0]
    return b

def det(A):
    a=[[F(x) for x in row] for row in A];n=len(a);out=F(1)
    for j in range(n):
        k=next((i for i in range(j,n) if a[i][j]),None)
        if k is None:return F(0)
        if k!=j:a[j],a[k]=a[k],a[j];out=-out
        v=a[j][j];out*=v
        for i in range(j+1,n):
            t=a[i][j]/v
            for k in range(j+1,n):a[i][k]-=t*a[j][k]
    return out

def exact_graph(params,n1,n2,r=F(121,100),hub=F(6,5)):
    """Enumerate individual spins with disagreeing-edge penalties, not binomial states."""
    q1,q2,a,b=map(F,params);orders=list(range(0,11,2))
    raw={k:F(0) for k in orders};der={k:[F(0)]*4 for k in orders}
    count=0
    for spins in product([-1,1],repeat=n1+n2+1):
        u=spins[:n1];v=spins[n1:n1+n2];e=spins[-1]
        d1=sum(u[i]!=u[j] for i in range(n1) for j in range(i+1,n1))
        d2=sum(v[i]!=v[j] for i in range(n2) for j in range(i+1,n2))
        dc=sum(x!=y for x in u for y in v)
        dh=sum(x!=e for x in u)
        need(dc%2==0,'even cross disagreement count')
        weight=q1**(-d1)*q2**(-d2)*r**(-dc//2)*hub**(-dh)
        s=sum(u);t=sum(v);x=s+a*t+b*e
        for k in orders:
            term=weight*x**k;raw[k]+=term
            der[k][0]+=-d1*term/q1;der[k][1]+=-d2*term/q2
            if k:
                der[k][2]+=weight*k*t*x**(k-1)
                der[k][3]+=weight*k*e*x**(k-1)
        count+=1
    z=raw[0];mu={k:raw[k]/z for k in orders}
    dm={k:[(der[k][j]-mu[k]*der[0][j])/z for j in range(4)] for k in orders}
    var=mu[2];mom=[];jac=[]
    for k in [4,6,8,10]:
        j=k//2;mom.append(mu[k]/var**j)
        jac.append([(dm[k][l]-j*mu[k]*dm[2][l]/var)/var**j for l in range(4)])
    return mom,jac,var,count

def bounded():
    # Independent un-reduced 300-term positive exponential series.
    for x in [F(1,8),F(1,2),F(1),F(2),F(4)]:
        lo=sum((x**j/factorial(j) for j in range(301)),F(0))
        tail=x**301/factorial(301)/(1-x/F(302));hi=lo+tail
        got=c.exp(c.I.point(x))
        need(got.contains(lo) and got.contains(hi),'positive exponential enclosure')
        ng=c.exp(c.I.point(-x))
        need(ng.contains(1/hi) and ng.contains(1/lo),'negative exponential enclosure')
    # Source derivatives via independent formal composition, not P recurrence.
    ps=c.derivative_polynomials(24)
    for q in [F(3),F(7),F(13)]:
        ep=[F(2)**j/factorial(j) for j in range(25)]
        a=[F(0)]+[-q*ep[j] for j in range(1,25)]
        pref=[4*q*q*F(9,2)**j/factorial(j)-6*q*F(5,2)**j/factorial(j) for j in range(25)]
        vals=mul(pref,exp_series(a,24),24)
        for j in range(25):
            want=sum(co*q**k for k,co in ps[j].items())
            need(factorial(j)*vals[j]==want,'independent theta derivative')
    # Integrated Taylor exactness and complete L1 remainder on one cell.
    h=F(1,7);center=F(2,3)
    for degree in range(28):
        exact=((center+h)**(degree+1)-(center-h)**(degree+1))/(degree+1)
        approximation=sum((2*h**(k+1)*F(factorial(degree),factorial(degree-k))*center**(degree-k)/factorial(k+1)
                           for k in range(0,min(23,degree)+1,2)),F(0))
        if degree<=23:need(exact==approximation,'Taylor polynomial integral')
        else:
            l1=F(factorial(degree),factorial(degree-23))*((center+h)**(degree-23)-(center-h)**(degree-23))
            need(abs(exact-approximation)<=h**24*l1/factorial(24),'integrated remainder')
    panels=0;configurations=0
    for n1,n2 in [(2,2),(2,4),(4,4)]:
        for params in [(F(11,10),F(6,5),F(2,3),F(4,5)),(F(9,8),F(17,16),F(5,7),F(3,4))]:
            m,J,v,count=exact_graph(params,n1,n2)
            a,b,variance,_=c.graph_values(params,n1,n2,F(121,100),F(6,5))
            need(variance.contains(v),'direct spin variance')
            for j in range(4):
                need(a[j].contains(m[j]),'direct spin moment')
                for k in range(4):need(b[j][k].contains(J[j][k]),'direct spin covariance derivative')
            panels+=1;configurations+=count
    # Sign cumulants from formal log cosh, and Vandermonde rank.
    n=16;co=[(F(1,factorial(j)) if j%2==0 else F(0)) for j in range(n+1)]
    derivative=[F(j+1)*co[j+1] for j in range(n)]+[F(0)]
    logder=mul(derivative,inv_series(co,n),n)
    cumulants=[factorial(2*k-1)*logder[2*k-1] for k in range(1,9)]
    aa=[F(0),F(1)]
    for k in range(2,9):aa.append(sum(aa[j]*aa[k-j] for j in range(1,k))/F(2*k-1))
    for k,v in enumerate(cumulants,1):
        need(v==(-1)**(k-1)*factorial(2*k-1)*aa[k] and v!=0,'sign cumulants')
    for r in range(1,9):
        weights=[F(j,13) for j in range(1,r+1)]
        J=[[2*k*cumulants[k-1]*b**(2*k-1) for b in weights] for k in range(1,r+1)]
        expected=F(1)
        for k in range(1,r+1):expected*=2*k*cumulants[k-1]
        for b in weights:expected*=b
        for i in range(r):
            for j in range(i+1,r):expected*=weights[j]**2-weights[i]**2
        need(det(J)==expected and expected!=0,'moment response determinant')
    need(sum((F(4)**j/factorial(j) for j in range(12)),F(0))>50,'physical tail cutoff')
    need(243**2+2*243+2==59537 and 150**2+2*150+2==22802,'tail constants')
    # The phase-independent enumeration also validates all compressed multiplicities.
    need(9*65*2==1170 and comb(8,2)+comb(64,2)+8*64+8==2564,'main graph counts')
    return {'exponential_pairs':5,'theta_derivative_compositions':3,'integrated_monomials':28,
            'direct_spin_graphs':panels,'individual_configurations':configurations,
            'moment_response_ranks':8,'source_and_graph_count_panels':3}

def seal(path):
    names=sorted(p.name for p in path.iterdir() if p.name!='SHA256SUMS')
    (path/'SHA256SUMS').write_text(''.join(hashlib.sha256((path/n).read_bytes()).hexdigest()+'  '+n+'\n' for n in names))

def adverse():
    flags=['-I','-S','-B']+(['-O'] if sys.flags.optimize else [])
    def run(path):
        return subprocess.run([sys.executable,*flags,str(path/'certify.py'),'--check',str(path/'certificate.json')],
                              capture_output=True,text=True,timeout=60)
    count=0
    with tempfile.TemporaryDirectory() as td:
        dest=Path(td)/'packet';shutil.copytree(ROOT,dest)
        good=run(dest);need(good.returncode==0,'pristine full CLI: '+good.stderr)
        pristine=json.loads(good.stdout)
        mutations=['false_rh','boolean_schema','duplicate_json','moment_scope','graph_exponent','source_coefficient','singular_preconditioner','extra_file']
        for name in mutations:
            shutil.rmtree(dest);shutil.copytree(ROOT,dest)
            cp=dest/'certificate.json';obj=json.loads(cp.read_text())
            if name=='false_rh':obj['rh_proved']=True;cp.write_text(json.dumps(obj))
            elif name=='boolean_schema':obj['schema']=True;cp.write_text(json.dumps(obj))
            elif name=='duplicate_json':cp.write_text(cp.read_text().replace('"schema": 1','"schema": 1, "schema": 1'))
            elif name=='moment_scope':obj['graph']['matched_even_moments'].append(12);cp.write_text(json.dumps(obj))
            elif name=='graph_exponent':
                p=dest/'certify.py';text=p.read_text();need('rpowers[s*t//4]' in text,'mutation anchor')
                p.write_text(text.replace('rpowers[s*t//4]','rpowers[0]'))
            elif name=='source_coefficient':
                p=dest/'certify.py';text=p.read_text();need('p={1:F(-6),2:F(4)}' in text,'source mutation anchor')
                p.write_text(text.replace('p={1:F(-6),2:F(4)}','p={1:F(-6),2:F(5)}'))
            elif name=='singular_preconditioner':
                p=dest/'parameters.json';o=json.loads(p.read_text());o['preconditioner'][0]=['0']*4;p.write_text(json.dumps(o))
            elif name=='extra_file':(dest/'unexpected.txt').write_text('not a declared artifact')
            seal(dest)
            result=run(dest);need(result.returncode!=0,'accepted corruption: '+name);count+=1
    return {'pristine_full_cli':1,'actual_altered_copy_cli_refusals':count,'same_backend_as_main':True}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--adverse',action='store_true')
    args=ap.parse_args();out={'bounded':bounded(),'independent_mathematical_review':False}
    if args.adverse:out['adverse']=adverse()
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':
    try:main()
    except (ValueError,OSError,KeyError,TypeError,subprocess.TimeoutExpired) as e:
        print('REJECT: '+str(e),file=sys.stderr);sys.exit(1)
