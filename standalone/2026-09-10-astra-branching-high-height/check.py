"""Exact finite controls for BHH26. Does not prove analytic asymptotics or RH."""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import argparse
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
DELAY_COEFFICIENT = 2
FILES = {'PROOF.md', 'README.md', 'SOURCES.json', 'VALIDATION.md',
         'check.py', 'test_check.py', 'result.json', 'SHA256SUMS'}
BASE = '3f1984867d23b588d09c88a892882411724b174b'

def require(value, message):
    if not value:
        raise ValueError(message)

def rising(a, j):
    r = F(1)
    for i in range(j):
        r *= a + i
    return r

def a(j):
    return F(1) if j == 0 else (1-F(2)**(1-2*j))/(2*j-1)

def moment_controls():
    k=F(5,2); degree=12; m=[rising(k,j)/k**j for j in range(degree+1)]
    checked=0; third=[]
    for depth in range(6):
        ell=[(-1)**j*m[j]/factorial(j) for j in range(degree+1)]
        nxt=[a(j)*sum((comb(j,i)*m[i]*m[j-i] for i in range(j+1)),F())
             for j in range(degree+1)]
        for j in range(degree+1):
            convolution=sum((ell[i]*ell[j-i] for i in range(j+1)),F())
            lhs=(2*j-1)*(-1)**j*nxt[j]/factorial(j)
            rhs=(1-DELAY_COEFFICIENT*F(4)**(-j))*convolution
            require(lhs==rhs,'literal shared-uniform differential identity')
            checked+=1
        require(nxt[1]==1 and nxt[2]==F(7,5),'orbit mean/variance')
        third.append(str(nxt[3])); m=nxt
    require(third[0]=='651/250','wrong prescribed first iterate')
    return {'depths':6,'moment_order':degree,'coefficient_identities':checked,
            'third_moments':third}

def zadd(x,y): return (x[0]+y[0],x[1]+y[1])
def zmul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def zscale(x,y): return (x[0]*y,x[1]*y)
def norm2(x): return x[0]**2+x[1]**2

def evaluate(coeffs,z):
    v=(F(),F())
    for c in reversed(coeffs):
        v=zadd(zmul(v,z),(F(c),F()))
    return v

def encoded_row(row):
    out=bytearray()
    for v in row:
        b=abs(v).to_bytes(max(1,(abs(v).bit_length()+7)//8),'big')
        out.extend(bytes([int(v<0)]));out.extend(len(b).to_bytes(4,'big'));out.extend(b)
    return bytes(out)

def polynomial_controls():
    b=[1]; c=[F(1)]; summaries=[]; points=0; ode=0; gaps=0
    dirs=[(F(1),F()),(F(),F(1)),(F(-1),F()),(F(3,5),F(4,5)),(F(5,13),F(12,13))]
    for n in range(13):
        d=[v*v for v in b]; beta=3*2**n+2; gamma_pair=5*2**n
        require(d[0]==1,'constant coefficient')
        require(gamma_pair-beta==2**(n+1)-2,'singular and gamma shapes conflated')
        for j in range(1,len(d)):
            require(d[j]>=4*d[j-1]>0,'coefficient-growth invariant');gaps+=1
        require([v/c[0] for v in c]==[F(x) for x in b],'independent pole normalization')
        q=[F(d[j],4**j) for j in range(n+1)]
        product=[q[0]]+[q[j]-q[j-1] for j in range(1,n+1)]+[-q[-1]]
        require(all(x>=0 for x in product[:-1]),'Enestrom multiplier sign')
        require(sum(product)==0 and product[-1]<0,'complete multiplier identity')
        if n<=6:
            for rad in [F(1,2),F(1)]:
                for direction in dirs:
                    z=zscale(direction,rad);p=evaluate(d,z)
                    derivative=evaluate([j*d[j] for j in range(1,n+1)],z)
                    require(norm2(p)>=d[-1]**2*(rad-F(1,4))**(2*n),'polynomial modulus floor')
                    require(norm2(zmul(z,derivative))<=4*n*n*norm2(p),'logarithmic derivative bound')
                    points+=1
        record={'depth':n,'degree':n,'beta':beta,'gamma_pair_shape':gamma_pair,
                'largest_integer_bits':max(abs(x).bit_length() for x in b),
                'coefficient_sha256':hashlib.sha256(encoded_row(b)).hexdigest()}
        if n<=5:
            record['b']=b[:];record['P']=d;record['first_pole_coefficient']=str(c[0])
        summaries.append(record)
        old=b[:];oldc=c[:];newbeta=3*2**(n+1)+2
        b=[(old[j] if j<len(old) else 0)**2
           -DELAY_COEFFICIENT*(old[j-1] if j else 0)**2 for j in range(n+2)]
        # Separate normalization route from the local ODE, with literal factor two.
        c=[((oldc[j] if j<len(oldc) else F())**2
            -2*(oldc[j-1] if j else F())**2)/newbeta for j in range(n+2)]
        for j in range(n+2):
            require(newbeta*c[j]==(oldc[j] if j<len(oldc) else F())**2
                    -2*(oldc[j-1] if j else F())**2,'local leading coefficient');ode+=1
    require(summaries[1]['P']==[1,4] and summaries[2]['P']==[1,4,64]
            and summaries[3]['P']==[1,4,3136,16384],'first actual polynomials')
    return {'rows':summaries,'growth_checks':gaps,'ode_checks':ode,
            'Gaussian_rational_points':points,'root_radius':'1/4'}

def local_pole_controls():
    rows=[]
    for forcing in [F(1),F(-2)]:
        co={4:forcing/8}
        for j in [3,2,1]:
            co[j]=F(2*j+3,2*j)*co[j+1]
        log=-F(3,2)*co[1]
        # All negative powers of 2(delta-1)y'-y, including the first log derivative.
        rhs={}
        for j,v in co.items():
            rhs[-j]=rhs.get(-j,F())-(2*j+1)*v
            rhs[-j-1]=rhs.get(-j-1,F())+2*j*v
        rhs[-1]=rhs.get(-1,F())-2*log
        rhs={e:x for e,x in rhs.items() if x}
        require(rhs=={-5:forcing},'complete first local polar equation')
        rows.append({'forcing':str(forcing),'polar':{str(j):str(co[j]) for j in sorted(co)},
                     'leading_log':str(log)})
    require(sum([F(1,8)**2,F(-1,4)**2])==F(5,64),'principal value at zero')
    return {'first_depth_local_expansions':rows,'principal_pair_mass':'5/64',
            'actual_pair_mass':'1','comparison_is_probability_law':False}

def gamma_model_controls():
    panels=[]
    for beta in [5,8,14,26]:
        for p in range(10):
            primary=rising(beta,p);lower=rising(beta-1,p)
            require(lower/primary==F(beta-1,beta-1+p),'gamma comparison normalization')
            panels.append([beta,p,str(lower/primary)])
    return {'synthetic_gamma_ratios':panels,'meaning':'finite rational gamma identities, not actual zero data'}

def result():
    return {'schema':'BHH26-1','source_pr':857,'source_head':BASE,
            'rh_proved':False,'all_height_zero_safety_proved':False,
            'thresholds_numerically_instantiated':False,
            'analytic_claim':'for every fixed depth there exists a high-height confinement threshold; paper proof only',
            'moments':moment_controls(),'polynomials':polynomial_controls(),
            'local_poles':local_pole_controls(),'gamma_models':gamma_model_controls()}

def pairs(items):
    d={}
    for k,v in items:
        require(k not in d,'duplicate JSON key');d[k]=v
    return d

def read(path):
    def bad(_):raise ValueError('noninteger JSON numeric value')
    return json.loads(Path(path).read_text(encoding='utf-8'),object_pairs_hook=pairs,
                      parse_float=bad,parse_constant=bad)

def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True)

def authenticate():
    actual={p.name for p in HERE.iterdir()}
    require(actual==FILES,'package inventory mismatch')
    require(all((HERE/name).is_file() and not (HERE/name).is_symlink() for name in FILES),'nonregular package file')
    lines=(HERE/'SHA256SUMS').read_text().splitlines();seen=set()
    for line in lines:
        h,name=line.split('  ')
        require(name not in seen and name in FILES-{'SHA256SUMS'},'bad hash entry')
        require(hashlib.sha256((HERE/name).read_bytes()).hexdigest()==h,'file integrity mismatch')
        seen.add(name)
    require(seen==FILES-{'SHA256SUMS'},'incomplete manifest')
    source=read(HERE/'SOURCES.json')
    require(source['parent_head']==BASE and source['source_pr']==857,'source freeze drift')

def main():
    parser=argparse.ArgumentParser();g=parser.add_mutually_exclusive_group(required=True)
    g.add_argument('--write');g.add_argument('--check');args=parser.parse_args()
    if args.check:authenticate()
    computed=result()
    if args.write:
        Path(args.write).write_text(json.dumps(computed,indent=2,sort_keys=True)+'\n')
        print('PRODUCED_BHH26')
    else:
        require(canonical(read(args.check))==canonical(computed),'primitive reconstruction mismatch')
        print('PASS_BHH26 '+hashlib.sha256(canonical(computed).encode()).hexdigest())

if __name__=='__main__':
    try:main()
    except (ValueError,TypeError,OSError,KeyError,ZeroDivisionError) as exc:
        print('REJECT_BHH26: '+str(exc),file=sys.stderr);sys.exit(1)
