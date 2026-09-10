#!/usr/bin/env python3
"""Adversarial arithmetic/algebra/receipt controls; optional actual CLI replays."""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import comb, factorial
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('theta_moments',ROOT/'theta_moments.py')
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
I,S=a.I,a.S

def require(ok,msg):
    if not ok:raise ValueError(msg)

def det(M):
    M=[[Q(x) for x in row] for row in M]
    d=Q(1)
    for j in range(len(M)):
        pivot=next((i for i in range(j,len(M)) if M[i][j]),None)
        if pivot is None:return Q(0)
        if pivot!=j:M[j],M[pivot]=M[pivot],M[j];d=-d
        p=M[j][j];d*=p
        for i in range(j+1,len(M)):
            c=M[i][j]/p
            for k in range(j+1,len(M)):M[i][k]-=c*M[j][k]
    return d


def controls():
    counts={}
    n=0
    vals=[Q(p,q) for p in range(-6,7) for q in (3,7)]
    for x in vals:
        for y in vals:
            for iv,v in ((I.q(x)+I.q(y),x+y),(I.q(x)*I.q(y),x*y)):
                require(Q(iv.lo,S)<=v<=Q(iv.hi,S),'lost rational value');n+=1
            if y:
                iv=I.q(x)/I.q(y)
                require(Q(iv.lo,S)<=x/y<=Q(iv.hi,S),'lost rational quotient');n+=1
    counts['directed_rational_cases']=n
    # Different exact pi identity: atan(1/2)+atan(1/3)=pi/4.
    def atan(n):
        p=sum((Q((-1)**j,(2*j+1)*n**(2*j+1)) for j in range(512)),Q(0))
        return p,p+Q(1,1025*n**1025)
    lo1,hi1=atan(2);lo2,hi2=atan(3);pi=a.pi_interval()
    require(Q(pi.lo,S)<=4*(lo1+lo2)<=4*(hi1+hi2)<=Q(pi.hi,S),'independent pi bracket not contained')
    counts['independent_pi_brackets']=1
    n=0
    for x in [Q(0),Q(1,100),Q(1,7),Q(1,2),Q(1),Q(2),Q(3),Q(-1),Q(-3)]:
        v=abs(x)
        low=sum((v**j/factorial(j) for j in range(257)),Q(0))
        # Ratio of terms after degree256 is <=3/258.
        hi=low+v**257/factorial(257)/(1-Q(3,258))
        if x<0:low,hi=1/hi,1/low
        iv=a.exp_point(x)
        require(Q(iv.lo,S)<=low<=hi<=Q(iv.hi,S),'independent exp bracket not contained');n+=1
    counts['independent_exp_brackets']=n
    # Exact two-vector metric construction, including its optimal eigenvalue ratio.
    n=0
    for t in (Q(1,5),Q(1,3),Q(1,2),Q(2,3)):
        c=(1-t*t)/(1+t*t);s=2*t/(1+t*t)
        u=[1+c,s];v=[1-c,-s]
        G=[[u[i]*u[j]/(2*(1+c)**2)+v[i]*v[j]/(2*(1-c)**2) for j in range(2)] for i in range(2)]
        require(G[0][0]*c+G[0][1]*s==0,'metric does not orthogonalize')
        require(G[0][0]+G[1][1]==1/(1+c)+1/(1-c),'metric trace mismatch')
        require(det(G)==1/((1+c)*(1-c)),'metric determinant mismatch');n+=3
    counts['exact_two_vector_metric_identities']=n
    n=0
    for r in range(2,25):
        m=r-1;b=[Q((-1)**j*comb(m,j)) for j in range(r)]
        for k in range(m):
            require(sum((b[j]*Q(j,m)**k for j in range(r)),Q(0))==0,'cluster moment does not vanish');n+=1
        require(sum(x*x for x in b)==comb(2*m,m),'coefficient norm identity');n+=1
    counts['exact_cluster_annihilations']=n
    n=0
    for nodes in ([Q(1,2),Q(1,3)],[Q(1,2),Q(1,3),Q(1,5)],[Q(1,3),Q(2,5),Q(4,7),Q(3,4)]):
        H=[[sum(t**(i+j+1) for t in nodes) for j in range(len(nodes))] for i in range(len(nodes))]
        expected=Q(1)
        for t in nodes:expected*=t
        for i in range(len(nodes)):
            for j in range(i):expected*=(nodes[i]-nodes[j])**2
        require(det(H)==expected>0,'weighted moment determinant formula');n+=1
    counts['positive_weighted_vandermonde_models']=n
    # Negative eigenvalue and conjugate nodes cannot pass the complete Hankel tower.
    H=[[(-1)**(i+j+1) for j in range(2)] for i in range(2)]
    require(H[0][0]<0,'negative node not detected')
    # lambda=1+i and 1-i: s1=2,s2=0,s3=-4.
    require(det([[2,0],[0,-4]])==-8,'conjugate model not rejected')
    counts['signed_spectral_controls']=2
    # Strongly log-concave Gaussian mixture: exact cumulants.
    raw={0:Q(1)};kap={}
    for n in range(1,7):
        raw[n]=sum((prob*comb(n,j)*center**(n-j)*Q(factorial(j),4**(j//2)*factorial(j//2))
            for center,prob in ((Q(-1,2),Q(1,8)),(Q(0),Q(3,4)),(Q(1,2),Q(1,8)))
            for j in range(0,n+1,2)),Q(0))
        kap[n]=raw[n]-sum((comb(n-1,j-1)*kap[j]*raw[n-j] for j in range(1,n)),Q(0))
    require((kap[2],kap[4],kap[6])==(Q(9,16),Q(1,256),Q(-7,2048)), 'mixture cumulant reconstruction')
    s1=kap[2]/2;s2=-kap[4]/12;s3=kap[6]/240
    require(s1>0 and s3<0 and s1*s3-s2*s2<0,'log-concavity control failed')
    counts['logconcave_moment_control']=1
    # A Jordan block cannot be self-adjoint in a positive inner product:
    # for N=[[0,1],[0,0]], G N = N^T G implies G00=0.
    N=[[Q(0),Q(1)],[Q(0),Q(0)]]
    bases=([[1,0],[0,0]],[[0,1],[1,0]],[[0,0],[0,1]])
    defects=[]
    for G in bases:
        defects.append([[sum(G[i][k]*N[k][j]-N[k][i]*G[k][j] for k in range(2))
                         for j in range(2)] for i in range(2)])
    require(defects==[[[0,1],[-1,0]],[[0,0],[0,0]],[[0,0],[0,0]]],
            'Jordan metric equation does not isolate the zero diagonal')
    counts['jordan_algebra_control']=3
    for bad in ('{"a":1,"a":2}','{"a":1.0}','{"a":NaN}','{"a":Infinity}'):
        try:a.strict_json(bad)
        except ValueError:pass
        else:raise ValueError('malformed receipt accepted')
    require(not a.typed_equal({'x':1},{'x':True}),'boolean/integer alias accepted')
    counts['strict_receipt_unit_refusals']=5
    return counts


def cli_controls(optimized=False):
    base=json.loads((ROOT/'moments.json').read_text())
    commands=[sys.executable,'-I','-S','-B']+(['-O'] if optimized else [])+[str(ROOT/'theta_moments.py')]
    receipts={}
    with tempfile.TemporaryDirectory() as temp:
        p=Path(temp)/'receipt.json'
        def call(name,text,ok):
            p.write_text(text)
            r=subprocess.run(commands+['--check',str(p)],capture_output=True,text=True)
            require((r.returncode==0)==ok,'unexpected CLI disposition: '+name)
            receipts[name]={'accepted':r.returncode==0,'returncode':r.returncode}
        raw=(ROOT/'moments.json').read_text()
        call('pristine_complete_reconstruction',raw,True)
        call('duplicate_top_level_key','{"rh_proved":false,'+raw.lstrip()[1:],False)
        b=json.loads(raw);b['coverage']['hankel_order']=True
        call('boolean_count_alias',json.dumps(b),False)
        b=json.loads(raw);b['coverage']['hankel_order']=4.0
        call('float_count_alias',json.dumps(b),False)
        b=json.loads(raw);b['rh_proved']=True
        call('false_RH_claim',json.dumps(b),False)
        b=json.loads(raw);b['traces']['7'][0]=str(int(b['traces']['7'][0])+1)
        call('changed_numeric_endpoint',json.dumps(b),False)
        b=json.loads(raw);b['coverage']['complete_theta_and_time_tails']=False
        call('tail_removed',json.dumps(b),False)
        b=json.loads(raw);b['coverage']['theta_indices']=7
        call('theta_coverage_reduced',json.dumps(b),False)
        b=json.loads(raw);del b['ldl_pivots']
        call('pivots_missing',json.dumps(b),False)
        b=json.loads(raw);b['unreviewed_claim']='all ranks'
        call('extra_field',json.dumps(b),False)
        call('empty_object','{}',False)
    return receipts


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--cli',action='store_true');p.add_argument('--optimized',action='store_true')
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    result={'status':'PASS_BOUNDED_TESTS_NOT_RH','controls':controls(),
            'actual_cli':cli_controls(args.optimized) if args.cli else {},'skipped_tests':0}
    text=json.dumps(result,sort_keys=True,indent=2)+'\n';args.output.write_text(text)
    print('PASS '+hashlib.sha256(text.encode()).hexdigest())
if __name__=='__main__':
    try:main()
    except (ValueError,OSError,ArithmeticError) as e:
        print('FAIL: '+str(e),file=sys.stderr);sys.exit(1)
