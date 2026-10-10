#!/usr/bin/env python3
"""Exploratory directed continuum residual enclosure for the literal L=1 source.

Exact primitive replay, closed gamma convolution, Gauss rules with Cauchy error,
and bounded omitted endpoint/cusp intervals are used. Phase8 variant uses
epsilon2^-50,76-point Gauss, and the proven27/2 scalar cost.  The analytic identities
and bounds still require independent review before scientific acceptance.
"""

import argparse
from fractions import Fraction
import hashlib
import json
import multiprocessing as multiprocessing
from pathlib import Path
import time

from flint import arb,acb,arb_mat,ctx

from enclose_analytic_upper import build,require,positive_ldl,Source
from source_convolution import ConvolutionSource


WORKER=None


def rational_ball(x):
    return arb(x.numerator)/x.denominator


def panels():
    epsilon=Fraction(1,2**50)
    raw=[]
    current=epsilon
    while current<Fraction(1,2):
        right=min(2*current,Fraction(1,2))
        raw.append((current,right))
        raw.append((1-right,1-current))
        current=right
    # Uniform cap in normalized coordinates ensures physical Cauchy radius<=.01.
    out=[]
    for left,right in sorted(raw):
        stack=[(left,right)]
        while stack:
            a,b=stack.pop()
            if b-a>Fraction(1,100):
                middle=(a+b)/2
                stack.extend([(middle,b),(a,middle)])
            else:
                out.append((a,b))
    return sorted(out)


def init_worker(payload):
    global WORKER
    ctx.prec=payload['bits']
    source=ConvolutionSource()
    coeff=arb_mat([[arb(x) for x in row] for row in payload['coefficients']])
    nodes=[arb.legendre_p_root(payload['order'],k,weight=True) for k in range(payload['order'])]
    cuts=[arb(0),1-source.log2,source.log2,arb(1)]
    WORKER={'source':source,'coeff':coeff,'nodes':nodes,'cuts':cuts,
            'removed':payload['removed'],'trial':payload['trial'],'order':payload['order'],
            'uniform_f_bound':arb(payload['uniform_f_bound'])}


def panel_task(task):
    segment,left_num,left_den,right_num,right_den=task
    left=arb(left_num)/left_den
    right=arb(right_num)/right_den
    state=WORKER
    source=state['source']
    a,b=state['cuts'][segment:segment+2]
    center=a+(b-a)*(left+right)/2
    halfwidth=(b-a)*(right-left)/2
    radius=2*halfwidth
    require(center-radius>0 and center+radius<1,'Cauchy disk lies inside 0<Re(t)<1')
    require(radius<=arb(1)/100,'Cauchy disk radius<=1/100')
    dim=state['coeff'].ncols()
    pdim=state['removed']+2
    ff=arb_mat(dim,dim)
    fp=arb_mat(pdim,dim)
    active=(segment==2,segment==0)
    for node,weight in state['nodes']:
        t=center+halfwidth*node
        primitive_f=source.basis_f(acb(t),state['removed'],state['trial'],*active)
        fz=[sum((primitive_f[k]*state['coeff'][k,j] for k in range(len(primitive_f))),arb(0))
            for j in range(dim)]
        projection=[arb(1)]+[(arb.pi()*j*t).cos() for j in range(1,state['removed']+1)]
        projection.append((source.b*t).sinh())
        qw=halfwidth*weight
        for i in range(dim):
            for j in range(i,dim):
                ff[i,j]+=qw*fz[i]*fz[j]
        for i in range(pdim):
            for j in range(dim):
                fp[i,j]+=qw*projection[i]*fz[j]
    for i in range(dim):
        for j in range(i):
            ff[i,j]=ff[j,i]
    # On a disk of radius R=2h, the Taylor tail after degree2n-1 is
    # <=2 M 2^-2n.  Integral plus positive Gaussian rule error<=8h M 2^-2n.
    factor=8*halfwidth*arb((1,-2*state['order']))
    ff_error=factor*state['uniform_f_bound']**2
    fp_error=factor*3*state['uniform_f_bound']
    ff_ball=arb(0,ff_error.upper())
    fp_ball=arb(0,fp_error.upper())
    for i in range(dim):
        for j in range(dim):
            ff[i,j]+=ff_ball
    for i in range(pdim):
        for j in range(dim):
            fp[i,j]+=fp_ball
    return {
        'segment':segment,
        'left':f'{left_num}/{left_den}',
        'right':f'{right_num}/{right_den}',
        'ff':[[ff[i,j].str(65,more=True) for j in range(dim)] for i in range(dim)],
        'fp':[[fp[i,j].str(65,more=True) for j in range(dim)] for i in range(pdim)],
        'ff_error':ff_error.upper().str(45,more=True),
        'fp_error':fp_error.upper().str(45,more=True),
    }


def projection_gram(removed,source):
    # Exact integrals of 1, cos(j*pi*t), sinh(bt), on [0,1].
    n=removed+2
    g=arb_mat(n,n)
    g[0,0]=1
    for j in range(1,removed+1):
        g[j,j]=arb(1)/2
    b=source.b
    last=n-1
    g[0,last]=g[last,0]=(b.cosh()-1)/b
    for j in range(1,removed+1):
        cross=b*((-1)**j*b.cosh()-1)/(b*b+(arb.pi()*j)**2)
        g[j,last]=g[last,j]=cross
    g[last,last]=(2*b).sinh()/(4*b)-arb(1)/2
    positive_ldl(g)
    return g


def prepare(trial,removed,bits,order):
    source_receipt,u,coeff=build(trial,removed,bits,True)
    source=ConvolutionSource()
    require(abs(source.cb)<arb(1)/2,'|Cb|<1/2')
    require(source.p2<arb(3)/5,'P2<3/5')
    require(source.q2<arb(1)/2,'q2<1/2')
    require(source.b.cosh()<arb(12)/5,'cosh(b)<12/5')
    require((arb(1)/2).exp()<2,'exp(c)<2')
    require(source.b.exp()<5,'exp(b)<5')
    gamma0=arb(1)/6+source.log2/3
    require(gamma0<arb(2)/5,'gamma kernel zero<2/5')
    require(source.gprimitive0<arb(13)/100,'gamma primitive zero<13/100')
    gamma_a_b,_=source.a(acb(source.b),('r',3))
    require(gamma_a_b.real<arb(3)/10,'gamma real-frequency rational sum<3/10')
    freq=arb.pi()*(removed+trial)
    require(freq>source.b,'maximum frequency includes every basis frequency')
    # For every disk used below: |Im t|<=.01, 0<Re t<1.  See proof file.
    k_bound=16*(3+2*freq/100).exp()
    basic_f_bound=(freq+arb(1)/2)*k_bound+100
    column_sums=[sum((coeff[i,j].abs_upper() for i in range(coeff.nrows())),arb(0))
                 for j in range(coeff.ncols())]
    coefficient_sum=max(x.upper() for x in column_sums)
    uniform_f_bound=basic_f_bound*coefficient_sum
    require((removed*arb.pi()/100).exp()<3,'projection cosine bound on every Cauchy disk')
    epsilon=arb((1,-50))
    zsup=5*coefficient_sum
    zder=(freq+8)*coefficient_sum
    endpoint_variation=epsilon*(7+2*(-epsilon.log()))*(2*zsup+zder)+epsilon*zsup
    require(endpoint_variation<1,'omitted boundary/cusp interval F variation<1')
    for t,left_active,right_active,endpoint in [(arb(0),False,True,0),
          (1-source.log2,False,False,None),(source.log2,False,False,None),(arb(1),True,False,1)]:
        fv=source.basis_f(acb(t),removed,trial,left_active,right_active,endpoint)
        vals=[sum((fv[k]*coeff[k,j] for k in range(len(fv))),arb(0)) for j in range(coeff.ncols())]
        for val in vals:
            require(val.abs_upper()<1,'F at omitted interval anchor<1')
    payload={
        'bits':bits,'removed':removed,'trial':trial,'order':order,
        'uniform_f_bound':uniform_f_bound.upper().str(65,more=True),
        'coefficients':[[coeff[i,j].str(65,more=True) for j in range(coeff.ncols())]
                        for i in range(coeff.nrows())],
    }
    return source_receipt,u,source,payload,uniform_f_bound,endpoint_variation


def run(out,trial=100,removed=5,bits=256,order=76,workers=2,limit=None):
    require(removed==5,"phase8 producer requires exactly five removed sine modes")
    began=time.monotonic()
    ctx.prec=bits
    source_receipt,u,source,payload,f_bound,end_variation=prepare(trial,removed,bits,order)
    pp=panels()
    tasks=[(segment,a.numerator,a.denominator,b.numerator,b.denominator)
           for segment in range(3) for a,b in pp]
    if limit is not None:
        tasks=tasks[:limit]
    print(json.dumps({'status':'RUNNING','panels':len(tasks),'gauss_order':order,
                      'point_count':len(tasks)*order,'uniform_F_bound':f_bound.str(12),
                      'endpoint_variation':end_variation.str(12)}),flush=True)
    dim=removed+3
    pdim=removed+2
    ff=arb_mat(dim,dim)
    fp=arb_mat(pdim,dim)
    coverage=[]
    ff_error_total=arb(0)
    fp_error_total=arb(0)
    # CPU workers run independent directed panel calculations with shared read-only payload.
    with multiprocessing.get_context('fork').Pool(workers,init_worker,(payload,)) as pool:
        for count,result in enumerate(pool.imap_unordered(panel_task,tasks),1):
            ff+=arb_mat([[arb(x) for x in row] for row in result['ff']])
            fp+=arb_mat([[arb(x) for x in row] for row in result['fp']])
            ff_error_total+=arb(result['ff_error'])
            fp_error_total+=arb(result['fp_error'])
            coverage.append({k:result[k] for k in ['segment','left','right']})
            if count%10==0:
                print(json.dumps({'completed_panels':count,'total_panels':len(tasks),
                                  'elapsed_seconds':time.monotonic()-began}),flush=True)
    if limit is not None:
        result={'status':'INCOMPLETE_DIAGNOSTIC','covered_panels':len(coverage),
                'full_panels':len(pp)*3,'elapsed_seconds':time.monotonic()-began}
        out.write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps(result),flush=True)
        return result
    # At most six omitted pieces of length<=epsilon, |F|<2, |p|<3.
    epsilon=arb((1,-50))
    endpoint_ff=arb(0,(24*epsilon).upper())
    endpoint_fp=arb(0,(36*epsilon).upper())
    for i in range(dim):
        for j in range(dim):
            ff[i,j]+=endpoint_ff
    for i in range(pdim):
        for j in range(dim):
            fp[i,j]+=endpoint_fp
    gram=projection_gram(removed,source)
    r=ff-fp.transpose()*gram.solve(fp)
    r=(r+r.transpose())/2
    lower=u-arb(27)/2*r
    shift=arb('1e-11')
    try:
        pivots=positive_ldl(lower,shift)
        status='DIRECTED_FULL_SOURCE_LOWER_ACCEPT_PENDING_ANALYTIC_REVIEW'
        failure=None
    except ArithmeticError as err:
        status='DIRECTED_LOWER_INCONCLUSIVE'
        pivots=[]
        failure=str(err)
    result={
        'status':status,'source_U_receipt':source_receipt,
        'precision_bits':bits,'gauss_order':order,'workers':workers,
        'coverage':sorted(coverage,key=lambda x:(x['segment'],Fraction(x['left']))),
        'total_panels':len(coverage),'covered_subintervals':'three source cusp slabs with bounded omitted neighborhoods',
        'epsilon':'2^-50','uniform_F_bound':f_bound.str(45,more=True),
        'endpoint_variation_bound':end_variation.str(45,more=True),
        'entrywise_FF_quadrature_error_total':ff_error_total.str(45,more=True),
        'entrywise_Fp_quadrature_error_total':fp_error_total.str(45,more=True),
        'R_matrix_balls':[[r[i,j].str(45,more=True) for j in range(dim)] for i in range(dim)],
        'lower_matrix_balls':[[lower[i,j].str(45,more=True) for j in range(dim)] for i in range(dim)],
        'shifted_LDL_pivots':[x.str(45,more=True) for x in pivots],
        'strict_acceptance_shift':'1e-11','scalar_residual_coefficient':'27/2','failure':failure,
        'elapsed_seconds':time.monotonic()-began,
        'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'analytic_dependencies':['closed gamma Laplace identities','piecewise analytic F formula','Cauchy-Gauss error','endpoint modulus bound'],
        'not_proved':['weighted residual acceptance','independent primitive replay','xi/Weil terminal adapter','all-window positivity','RH'],
    }
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in
          ['source_U_receipt','coverage','R_matrix_balls','lower_matrix_balls','shifted_LDL_pivots']},indent=2),flush=True)
    return result


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--trial-modes',type=int,default=100)
    p.add_argument('--removed',type=int,choices=[5],default=5)
    p.add_argument('--bits',type=int,default=256)
    p.add_argument('--order',type=int,default=76)
    p.add_argument('--workers',type=int,default=2)
    p.add_argument('--limit',type=int)
    args=p.parse_args()
    run(args.out,args.trial_modes,args.removed,args.bits,args.order,args.workers,args.limit)
