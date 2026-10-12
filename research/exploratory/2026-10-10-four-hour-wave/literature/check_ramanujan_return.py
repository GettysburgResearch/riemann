"""Exact Fourier/mask/phase controls for the complete Ramanujan return.

No asymptotic higher moment is proved by these finite controls.
"""
import argparse
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


def require(ok,context):
    if not ok:raise ArithmeticError(context)


def add(a,b):return (a[0]+b[0],a[1]+b[1])
def mul(a,b):
    x,y=a;u,v=b
    return (x*u-y*v,x*v+y*u-y*v)
def conjugate(a):return (a[0]-a[1],-a[1])
def equal_mod_phi(a,b):
    diff=[add(x,(-y[0],-y[1])) for x,y in zip(a,b)]
    return len(set(diff))==1


def controls():
    counts={'ramanujan_fourier':0,'cubic_return_with_nonunit':0,
            'opposite_gauss_negative_control':0,'inactive_signed_cancellation':0}
    for q in (7,13,19,31,37,43):
        g=next(g for g in range(2,q) if len({pow(g,j,q) for j in range(q-1)})==q-1)
        log={pow(g,j,q):j for j in range(q-1)}
        powers=((1,0),(0,1),(-1,-1))
        cubic={m:powers[log[m]%3] for m in range(1,q)}
        original=[(0,0)]+[cubic[m] for m in range(1,q)]
        wrong=[(0,0)]+[conjugate(cubic[m]) for m in range(1,q)]
        require(not equal_mod_phi(original,wrong),'gamma2 is not gamma4')
        counts['opposite_gauss_negative_control']+=1
        for m in range(q):
            # Multiplying R by sqrt(q) avoids any approximation to a root.
            inverse=[(0,0) for _ in range(q)]
            for h in range(1,q):
                inverse[(h*m)%q]=add(inverse[(h*m)%q],(1,0))
            literal=[(-1+q*(m==0),0)]+[(0,0)]*(q-1)
            require(equal_mod_phi(inverse,literal),'complete Ramanujan Fourier support')
            counts['ramanujan_fourier']+=1
            for epsilon in (1,g,pow(g,2,q)):
                left=[(0,0) for _ in range(q)]
                for y in range(1,q):
                    left[(epsilon*m*y)%q]=add(left[(epsilon*m*y)%q],cubic[y])
                if m==0:
                    right=[(0,0)]*q
                else:
                    factor=conjugate(cubic[(epsilon*m)%q])
                    right=[mul(x,factor) for x in original]
                require(equal_mod_phi(left,right),'gamma2 return after frequency inversion')
                counts['cubic_return_with_nonunit']+=1
    # Every inactive prime has opposite equal amplitudes. The complete
    # finite divisor sum is zero unless there are no inactive primes.
    for n in range(11):
        total=sum((-1)**sum(bits) for bits in product((0,1),repeat=n))
        require(total==(1 if n==0 else 0),'full inactive Mobius cancellation')
        counts['inactive_signed_cancellation']+=1
    return counts


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    here=Path(__file__).resolve().parent
    source=Path('/workspace/.riemann-research/sources/qrh11-12.tex')
    digest=sha256(source.read_bytes()).hexdigest()
    require(digest=='d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d',
            'literal finite Fourier source')
    record={'status':'PASS_EXACT_RAMANUJAN_RETURN_CONTROLS','checks':controls(),
      'source_sha256':{str(source):digest},
      'support_adapter_sha256':sha256((here/'CUSP_VECTOR_SUPPORT_RETURN.md').read_bytes()).hexdigest(),
      'manuscript_sha256':sha256((here/'CUSP_RAMANUJAN_RETURN.md').read_bytes()).hexdigest(),
      'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
      'full_generalized_moment_proved':False,'strict_scalar_contraction_paid':False,
      'imported_theta_analysis_independently_rebuilt':False,'rh_proved':False}
    args.output.write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(record['status'])


if __name__=='__main__':main()
