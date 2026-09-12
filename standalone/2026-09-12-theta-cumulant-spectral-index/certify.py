#!/usr/bin/env python3
"""Complete native theta-cumulant finite Hankel certificate. NOT an RH proof."""
from pathlib import Path
import sys, json, hashlib, argparse
sys.path.insert(0,str(Path(__file__).resolve().parent))
from intervals import I, F, S, exp, pi_interval, factorial, comb, need, derivative_polynomials, poly_eval

ROOT=Path(__file__).resolve().parent
FILES={'PROOF.md','README.md','REVIEW.md','SOURCES.json','VALIDATION.md',
       'intervals.py','certify.py','test_check.py','certificate.json','SHA256SUMS'}

def strict_json(path):
    def pairs(items):
        out={}
        for k,v in items:
            need(k not in out,'duplicate JSON key');out[k]=v
        return out
    def nofloat(v):raise ValueError('noninteger JSON number')
    return json.loads(Path(path).read_text(),object_pairs_hook=pairs,parse_float=nofloat,parse_constant=nofloat)

def authenticate():
    need({p.name for p in ROOT.iterdir()}==FILES,'packet inventory')
    need(all((ROOT/f).is_file() and not (ROOT/f).is_symlink() for f in FILES),'regular files required')
    entries={}
    for row in (ROOT/'SHA256SUMS').read_text().splitlines():
        h,f=row.split('  ',1)
        need(f in FILES-{'SHA256SUMS'} and f not in entries,'manifest path')
        entries[f]=h
    need(set(entries)==FILES-{'SHA256SUMS'},'complete manifest')
    for f,h in entries.items():need(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h,'hash '+f)
    source=strict_json(ROOT/'SOURCES.json')
    need(source['base_commit']=='34ee76ed5bc8124a30aff7567152d4ae9f7f69cb','source base')
    need(source['rh_proved'] is False,'false source RH status')


def theta_moments(max_order=36,cells=128,degree=63,terms=8):
    n=degree+1;T=3;half=F(T,2*cells)
    orders=list(range(0,max_order+1,2))
    ps=derivative_polynomials(n)
    Bs=[F(5*terms,2)*sum(abs(c)*factorial(k-1) for k,c in p.items()) for p in ps]
    sums={m:I.point(0) for m in orders};pi=pi_interval()
    coeff={k:2*half**(k+1)/factorial(k+1) for k in range(0,n,2)}
    for j in range(cells):
        t=F(T*(2*j+1),2*cells);et=exp(I.point(2*t));fac=exp(I.point(t/2))
        deriv=[I.point(0) for k in range(n)]
        for index in range(1,terms+1):
            q=pi*(index*index)*et
            if q.lo>=400*S:
                # e>8/3; evaluate complete derivative envelopes BEFORE rounding.
                # This avoids underflow multiplied by a high-degree polynomial.
                cut=min(2048,q.lo//S)
                e_bound=F(3,8)**cut
                Q=2048 if cut==2048 else (q.hi//S+1)
                for k in range(n):
                    B=5*e_bound*sum(abs(c)*Q**r for r,c in ps[k].items())
                    deriv[k]=deriv[k]+I.bounds(-B,B)
            else:
                e=fac*exp(-q)
                for k in range(n):
                    deriv[k]=deriv[k]+e*poly_eval(ps[k],q)
        for m in orders:
            for k in range(0,n,2):
                df=sum((F(comb(k,v)*factorial(m),factorial(m-v))*t**(m-v)*deriv[k-v]
                        for v in range(min(k,m)+1)),I.point(0))
                sums[m]=sums[m]+coeff[k]*df
    raw={};errors={}
    for m in orders:
        C=sum(F(comb(n,j)*factorial(m),factorial(m-j))*T**(m-j)*Bs[n-j]
              for j in range(min(n,m)+1))
        error=2*half**n*C/factorial(n)
        ti=8*factorial(m)*59537*exp(I.point(-243))
        # Q0>1000*n^2 for t>=3. exp(-1000) <= (3/8)^1000.
        tp=I.point(8*factorial(m)*1002002*F(3,8)**1000)
        val=(2*sums[m]).widened(error)
        raw[m]=I(val.lo,val.hi+ti.hi+tp.hi)
        errors[str(m)]={'taylor_L1':str(error),'index_tail_upper':str(F(ti.hi,S)),
                       'physical_tail_upper':str(F(tp.hi,S))}
    need(raw[0].lo>9*S//20,'source mass exceeds nine twentieths')
    mu={m:raw[m]/raw[0] for m in orders};mu[0]=I.point(1)
    return raw,mu,errors

def power_sums(mu):
    n=max(mu)//2
    e={r:mu[2*r]/factorial(2*r) for r in range(n+1)}
    q={}
    for r in range(1,n+1):
        earlier=sum(((-1)**(k+1)*q[k]*e[r-k] for k in range(1,r)),I.point(0))
        q[r]=(-1)**(r+1)*(r*e[r]-earlier)
    return q

def cumulant_check(mu,q):
    # Independent binomial moment/cumulant recurrence, not Newton reuse.
    kap={0:I.point(0)}
    for r in range(1,max(mu)//2+1):
        kap[r]=mu[2*r]-sum((comb(2*r-1,2*k-1)*kap[k]*mu[2*(r-k)] for k in range(1,r)),I.point(0))
        alt=(-1)**(r+1)*kap[r]/(2*factorial(2*r-1))
        need(max(alt.lo,q[r].lo)<=min(alt.hi,q[r].hi),'disjoint cumulant/Newton enclosures')

def ldl(A):
    n=len(A);L=[[I.point(int(i==j)) for j in range(n)] for i in range(n)];D=[]
    for j in range(n):
        pivot=A[j][j]-sum((L[j][k]**2*D[k] for k in range(j)),I.point(0))
        need(pivot.lo>0,'unproved positive pivot at '+str(j))
        D.append(pivot)
        for i in range(j+1,n):
            L[i][j]=(A[i][j]-sum((L[i][k]*L[j][k]*D[k] for k in range(j)),I.point(0)))/pivot
    return D

def build():
    raw,mu,errors=theta_moments()
    q=power_sums(mu);cumulant_check(mu,q)
    need(pi_interval().hi*25<81*S,'pi Gaussian-envelope bound')
    mgf=sum((mu[2*k]*20**k/factorial(2*k) for k in range(19)),I.point(0))
    mgf=mgf+F(1024*5**19,factorial(19))*F(4,3)
    need(mgf.hi*5<9*S,'whole mgf disk bound')
    r={k:q[k]*200**k for k in q}
    tables={}
    for shift in [1,2]:
        A=[[r[i+j+shift] for j in range(9)] for i in range(9)]
        D=ldl(A)
        if shift==1:
            antecedent=I.point(1)
            for d in D[:4]:antecedent=antecedent*d
            antecedent=antecedent/200**16
            need(F(antecedent.lo,S)>F(11775,10**45) and F(antecedent.hi,S)<F(11777,10**45),'antecedent 4x4 interval')
        tables[str(shift)]={'dimension':9,'shift':shift,'scaled_entries':[[v.raw() for v in row] for row in A],
                            'ldl_pivots':[v.raw() for v in D], 'pivot_decimal':[v.decimal(70) for v in D]}
    return {'schema':1,'status':'PROPOSED_COMPONENTS_NOT_RH','rh_proved':False,
            'bits':768,'source':{'terms':8,'cells':128,'degree':63,'end':3,'moments_through':36},
            'raw_moments':{str(k):v.raw() for k,v in raw.items()},
            'normalized_moments':{str(k):v.raw() for k,v in mu.items()},
            'q_scaled_by_200_power':{str(k):v.raw() for k,v in r.items()},
            'error_budgets':errors,'hankel_certificates':tables,
            'antecedent_4x4_determinant':antecedent.raw(),
            'mgf_sqrt20_upper':mgf.raw(),
            'absolute_square_sum_upper':'1/8',
            'actual_zeros_used':0,'global_hankel_positivity_proved':False}

def main():
    ap=argparse.ArgumentParser();g=ap.add_mutually_exclusive_group(required=True);g.add_argument('--emit',type=Path);g.add_argument('--check',type=Path)
    args=ap.parse_args()
    if args.check:
        authenticate()
        got=strict_json(args.check)
        need(got.get('rh_proved') is False and got.get('global_hankel_positivity_proved') is False,'false global status')
        need(type(got.get('bits')) is int and got['bits']==768,'arithmetic class')
        from test_check import reconstruct
        reconstruct()
    result=build()
    data=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.emit:args.emit.write_text(data)
    if args.check:
        need(args.check.read_text()==data,'certificate differs from complete reconstruction')
    print(json.dumps({'passed':True,'sha256':hashlib.sha256(data.encode()).hexdigest(),
                      'hankel_pivots':{k:v['pivot_decimal'] for k,v in result['hankel_certificates'].items()}},indent=2))
if __name__=='__main__':
    try:main()
    except (ValueError,OSError,KeyError,TypeError) as e:
        print('REJECT: '+str(e),file=sys.stderr);sys.exit(1)
