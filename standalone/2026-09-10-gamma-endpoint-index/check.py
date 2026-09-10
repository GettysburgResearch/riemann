#!/usr/bin/env python3
"""Authenticate this packet and reconstruct bounded identities / the full disk.

Default --check runs the complete centered-N5 integral, not only hashes.
--quick is explicitly not a zero-certificate replay. No network is used.
"""
from fractions import Fraction as Q
from math import factorial, comb
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import sys

ROOT=Path(__file__).resolve().parent
FILES=('PROOF.md','CERTIFICATE.md','README.md','SOURCE_LOCK.json','VALIDATION.md',
       'interval.py','certificate.py','check.py','test_check.py','results.json',
       'bounded.json','SHA256SUMS')


def require(ok,message):
    if not ok: raise ValueError(message)


def no_duplicates(pairs):
    out={}
    for k,v in pairs:
        require(k not in out,'duplicate JSON key')
        out[k]=v
    return out


def read_json(path):
    def invalid(x): raise ValueError('nonfinite JSON number')
    return json.loads(path.read_text(),object_pairs_hook=no_duplicates,parse_constant=invalid)


def canonical(obj):
    return json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=True,allow_nan=False)


def authenticate():
    require(sorted(p.name for p in ROOT.iterdir())==sorted(FILES),'packet inventory')
    for name in FILES:
        p=ROOT/name
        require(p.is_file() and not p.is_symlink(),'nonregular packet member')
        require(p.stat().st_size<2_000_000,'oversized packet member')
    records={}
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        digest,name=line.split('  ',1)
        require(name in FILES and name!='SHA256SUMS' and name not in records,'manifest record')
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,'content hash: '+name)
        records[name]=digest
    require(set(records)==set(FILES)-{'SHA256SUMS'},'manifest coverage')
    lock=read_json(ROOT/'SOURCE_LOCK.json')
    require(lock['parent_commit']=='0e19b74fe6dfb39bef69a5edd3f0b3098b10a6ad','parent source')
    data=(ROOT/'interval.py').read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    require(blob=='36d6341b574fe5a512196bfa0d66fbae897365a6','inherited arithmetic byte identity')


def certificate_module():
    spec=importlib.util.spec_from_file_location('_ge_certificate',ROOT/'certificate.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def inv_moments(rates, upto):
    cumulants=[Q(0)]+[2*factorial(k-1)*sum((a**(-k) for a in rates),Q(0)) for k in range(1,upto+1)]
    ans=[Q(1)]
    for k in range(1,upto+1):
        ans.append(sum((comb(k-1,j-1)*cumulants[j]*ans[k-j] for j in range(1,k+1)),Q(0)))
    return ans


def exact_inertia(matrix):
    """Rational symmetric congruence, including zero-diagonal 2x2 pivots."""
    a=[list(row) for row in matrix];pos=neg=zero=0
    while a:
        n=len(a)
        pivot=next((i for i in range(n) if a[i][i]),None)
        if pivot is not None:
            order=[pivot]+[i for i in range(n) if i!=pivot]
            a=[[a[i][j] for j in order] for i in order]
            d=a[0][0];pos+=int(d>0);neg+=int(d<0)
            a=[[a[i][j]-a[i][0]*a[0][j]/d for j in range(1,n)] for i in range(1,n)]
            continue
        pair=next(((i,j) for i in range(n) for j in range(i+1,n) if a[i][j]),None)
        if pair is None:
            zero+=n;break
        i,j=pair;order=[i,j]+[k for k in range(n) if k not in pair]
        a=[[a[i][j] for j in order] for i in order];b=a[0][1]
        pos+=1;neg+=1
        a=[[a[i][j]-(a[i][0]*a[1][j]+a[i][1]*a[0][j])/b for j in range(2,n)] for i in range(2,n)]
    return [pos,neg,zero]


def c_mul(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])


def c_pow(a,k):
    ans=(Q(1),Q(0))
    for _ in range(k):ans=c_mul(ans,a)
    return ans


def bounded():
    c=certificate_module()
    groups={'gamma_moments':0,'density_origin_coefficients':0,
            'endpoint_log_jets':0,'phase_algebra':0,'finite_index_controls':0,
            'positive_tail_controls':0,'partition_controls':0}
    for n in range(1,9):
        rates=tuple(Q(k*k) for k in range(1,n+1));rr=c.rows(rates);mm=inv_moments(rates,12)
        for k in range(13):
            direct=sum((b*(Q(factorial(k+1))/a**(k+2)+d*Q(factorial(k))/a**(k+1)) for a,b,d in rr),Q(0))
            require(direct==mm[k],'complete gamma moment')
            groups['gamma_moments']+=1
        cc=Q(factorial(n)**4,factorial(2*n-1))
        for k in range(2*n+2):
            coeff=sum((b*(((-a)**(k-1)/factorial(k-1) if k else 0)+d*(-a)**k/factorial(k)) for a,b,d in rr),Q(0))
            if k<2*n-1:require(coeff==0,'origin multiplicity')
            if k==2*n-1:require(coeff==cc,'origin leading density')
            if k==2*n:require(coeff==-cc*Q((n+1)*(2*n+1),6),'simplex first derivative')
            if k==2*n+1:
                total=2*sum(rates,Q(0)); squares=2*sum((a*a for a in rates),Q(0))
                second=(total*total+squares)/((2*n)*(2*n+1))
                require(coeff==cc*second/2,'simplex second moment')
            groups['density_origin_coefficients']+=1
        # Abstract endpoint first jets: the actual source values remain symbols.
        for tau in (Q(1,3),Q(1,2),Q(1)):
            for value,derivative in ((Q(2),Q(-1)),(Q(3),Q(1)),(Q(5),Q(-4))):
                x0=9/tau;p=2*n-1;mean=Q((n+1)*(2*n+1),6)
                small_log=p-2*tau*mean
                large_log=-2*x0*derivative/value
                b_formula=Q(p,2)-tau*mean-x0*derivative/value
                require((small_log+large_log)/2==b_formula,'endpoint square-root jet')
                groups['endpoint_log_jets']+=1
    for alpha in (Q(3,2),Q(5,2),Q(11,2),Q(13,2)):
        for b in (Q(-2),Q(0),Q(3)):
            for co,si in ((Q(1),Q(2)),(Q(-3),Q(1)),(Q(1,2),Q(-2,3))):
                z=Q(7)
                plus=c_mul((co,si),(Q(1),-alpha*b/z))
                minus=c_mul((co,-si),(Q(1),alpha*b/z))
                require((plus[0]+minus[0],plus[1]+minus[1])==(2*co+2*alpha*b*si/z,Q(0)),'endpoint phase sign')
                groups['phase_algebra']+=1
    spectra=[[],[(Q(1),Q(1,2))],[(Q(1),Q(1,2)),(Q(2),Q(1))],
             [(Q(1),Q(1,2)),(Q(2),Q(1)),(Q(3),Q(1,3))]]
    recorded=[]
    for nodes in spectra:
        for weight in (1,3):
            def moment(k):
                # Complete infinite tail t_j=(1/8)2^-j, j>=1, no truncation.
                return Q(1,8)**k/(2**k-1)+Q(1,10)**k+Q(1,5)**k+sum((2*weight*c_pow(a,k)[0] for a in nodes),Q(0))
            last=0
            for d in range(9):
                a=[[moment(i+j+2) for j in range(d+1)] for i in range(d+1)]
                inertia=exact_inertia(a)
                require(last<=inertia[1]<=len(nodes),'negative-index bounds')
                if d==8:require(inertia[1]==len(nodes),'finite-index saturation control')
                last=inertia[1];groups['finite_index_controls']+=1
            recorded.append({'nonreal_pairs':len(nodes),'multiplicity_weight':weight,'degree8_inertia':inertia})
    for k in range(2,14):
        full=Q(1,8)**k/(2**k-1)
        for j in range(1,6):
            prefix=sum((Q(1,8)**k/Q(2)**(i*k) for i in range(1,j+1)),Q(0))
            tail=full/Q(2)**(j*k)
            require(prefix+tail==full,'complete positive tail identity')
            groups['positive_tail_controls']+=1
    pp=c.panels()
    groups['partition_controls']=len(pp)
    g=c.guards(c.rows())
    require(c.N==5 and c.DEGREE==40 and c.B==Q('1.079529'),'certificate constants')
    require(c.TAU.lo>c.I(Q(36,100)).hi and c.TAU.hi<c.I(Q(11,30)).lo,'exact centered mean')
    return {'status':'BOUNDED_IDENTITIES_NOT_INFINITE_THEOREM_PROOF','rh_proved':False,
            'groups':groups,'finite_index_models':recorded,'partition_cells':len(pp),
            'source_guards':g,'actual_zero_evaluated_in_this_subset':False}


def expect_equal(actual,expected):
    require(canonical(actual)==canonical(expected),'fresh reconstruction differs from receipt')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check',type=Path,default=ROOT/'results.json')
    p.add_argument('--quick',action='store_true')
    p.add_argument('--write-bounded',type=Path)
    args=p.parse_args()
    if args.write_bounded:
        args.write_bounded.write_text(json.dumps(bounded(),sort_keys=True,indent=2)+'\n')
        print('PRODUCED_BOUNDED_IDENTITIES_NOT_ACCEPTANCE');return
    authenticate()
    expect_equal(bounded(),read_json(ROOT/'bounded.json'))
    if args.quick:
        print('PASS_BOUNDED_ONLY_NO_ZERO_REPLAY');return
    expected=read_json(args.check)
    require(expected.get('rh_proved') is False and expected.get('zero_of_xi_claimed') is False,'false conclusion flag')
    require(type(expected.get('N')) is int and expected['N']==5,'typed N')
    actual=certificate_module().reconstruct()
    expect_equal(actual,expected)
    print('PASS_COMPLETE_CENTERED_INTEGER_N5_ZERO; NO_RH_CLAIM')


if __name__=='__main__':
    try:main()
    except (ValueError,OSError,TypeError,KeyError) as e:
        print('FAIL_GAMMA_ENDPOINT_PACKET: '+str(e),file=sys.stderr)
        sys.exit(1)
