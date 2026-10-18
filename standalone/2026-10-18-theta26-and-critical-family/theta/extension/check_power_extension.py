#!/usr/bin/env python3
"""Exact rational receipts for POWER_SUM_EXTENSION.md; Python stdlib only.

This checker validates displayed arithmetic and finite rational instances of
general identities proved in the companion. It does not certify a theta root
or establish cofinal feasibility. Pass --output to keep the shipped receipt
unchanged during replay.
"""
from fractions import Fraction as F
from math import comb, prod
from pathlib import Path
import argparse
import hashlib
import json

ROOT=Path(__file__).resolve().parent
SOURCE_HASH='c171903e4f60c189a929ccfcce36f7db034508e9ca10c85ed766338625558dcf'


def require(ok,message):
    if not ok:raise ValueError(message)


def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p


def add(a,b):
    return trim([(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0))
                 for i in range(max(len(a),len(b)))])


def scale(a,c):
    return trim([c*v for v in a])


def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):out[i+j]+=v*w
    return trim(out)


def determinant(matrix):
    a=[row[:] for row in matrix]
    result=F(1)
    for j in range(len(a)):
        nz=next((i for i in range(j,len(a)) if a[i][j]!=0),None)
        if nz is None:return F(0)
        if nz!=j:
            a[nz],a[j]=a[j],a[nz]
            result=-result
        pivot=a[j][j]
        result*=pivot
        for i in range(j+1,len(a)):
            q=a[i][j]/pivot
            for k in range(j+1,len(a)):a[i][k]-=q*a[j][k]
    return result


def chart(m,L):
    alpha=[F(i+2,30*m+1) for i in range(m)]
    cards=[]
    for i,x in enumerate(alpha):
        p=[F(1)]
        for j,y in enumerate(alpha):
            if j!=i:p=mul(p,[-y/(x-y),1/(x-y)])
        cards.append(p)
    for k in range(m):
        total=[F(0)]
        for x,p in zip(alpha,cards):total=add(total,scale(p,x**k))
        require(total==[F(0)]*k+[F(1)],'exact Lagrange interpolation')
    error=[F(0)]*m+[F(1)]
    for x,p in zip(alpha,cards):error=add(error,scale(p,-x**m))
    product_poly=[F(1)]
    for x in alpha:product_poly=mul(product_poly,[-x,F(1)])
    require(error==product_poly,'next-power derivative polynomial identity')
    reserve=[F(1)]
    for x,p in zip(alpha,cards):reserve=add(reserve,[F(0)]+scale(p,-1/x))
    reserve_product=[F(1)]
    for x in alpha:reserve_product=mul(reserve_product,[F(1),-1/x])
    require(reserve==reserve_product,'Gaussian-reserve derivative identity')

    gaps=[abs(x-y) for i,x in enumerate(alpha) for y in alpha[i+1:]]
    delta=min(alpha+gaps)/8
    K=[prod((y+delta)/(abs(x-y)-2*delta) for j,y in enumerate(alpha) if i!=j)
       for i,x in enumerate(alpha)]
    tau=min(alpha)/4
    halvings=0
    while not all(F(L)*tau*tau*k/(2*(x-delta))<delta for x,k in zip(alpha,K)):
        tau/=2
        halvings+=1
    require(tau<min(x-delta for x in alpha),'new node remains below box')
    threshold=F(L*(m+2),2)*tau*tau*prod(x-delta-tau for x in alpha)
    require(threshold>0,'strict quantitative next-power extension threshold')
    return {'anchors':m,'cloud_multiplicity':L,'delta':str(delta),'tau':str(tau),
            'radius_halvings':halvings,'guaranteed_signed_gain':str(threshold),
            'direction_sign':(-1)**m}


def collision(m):
    u=F(1,2)
    gammas=[F(j+1,4*m+1) for j in range(m-2)]
    matrix=[[r*g**(r-1) for g in gammas]+[2*r*u**(r-1),r*(r-1)*u**(r-2)]
            for r in range(2,m+2)]
    expected=2*u*u*prod(range(2,m+2))*prod(gammas)
    expected*=prod(gammas[j]-gammas[i] for i in range(len(gammas))
                   for j in range(i+1,len(gammas)))
    expected*=prod((u-g)**2 for g in gammas)
    require(determinant(matrix)==expected!=0,'confluent collision determinant')
    return {'active_coordinates':m,'determinant':str(expected)}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source-json',type=Path,default=ROOT.parent/'theta26_source.json')
    ap.add_argument('--output',type=Path,default=ROOT/'power_extension_certificate.json')
    args=ap.parse_args()
    source_bytes=args.source_json.read_bytes()
    require(hashlib.sha256(source_bytes).hexdigest()==SOURCE_HASH,'directed source identity')
    source=json.loads(source_bytes)
    denominator=1<<source['bits']
    v_upper=F(source['variance'][1],denominator)
    # The unit fourth cumulant is -2, so q2=(-kappa4)/12=ratio4/6.
    q_upper=F(source['standardized_cumulant_ratios'][1][1],6*denominator)
    require(0<v_upper<F(4621,100000),'directed theta variance bound')
    require(0<q_upper<F(17409,1000000),'directed theta second-power bound')
    R=F(7,400)
    require(F(133,1000)**2>R,'rational square-root upper bound')
    require(6**2>32,'rational upper bound for four sqrt two')
    gap=R-6*F(4621,900000)*R*F(133,1000)-F(17409,1000000)
    require(gap==F(1157849,60000000000)>0,'displayed strict complex normality barrier')

    p2=F(301,2400);p3=F(101,1600)
    defect=p3*p3-p2**3
    require(defect==F(27814499,13824000000)>0,'positive-weight/unit-node counterexample')

    for d in (F(1,40000),F(-1,40000),F(0)):
        u=F(3,17);s=2*u;p=u*u-d
        c=[F(2),s]
        for r in range(2,27):c.append(s*c[-1]-p*c[-2])
        for r in range(27):
            require(c[r]==2*sum((F(comb(r,2*k))*u**(r-2*k)*d**k
                                for k in range(r//2+1)),F(0)),
                    'complete conjugate-pair power identity')

    # Choose a rational standardized zero x+ih; its inverse-square node,
    # modulus, and band identity are all rational without a square root.
    xx=F(10);hh=F(1,20);v=F(1,4)
    rr=1/(xx*xx+hh*hh)
    uu=(xx*xx-hh*hh)/(xx*xx+hh*hh)**2
    yy=-2*xx*hh/(xx*xx+hh*hh)**2
    require(uu*uu+yy*yy==rr*rr,'exact conjugate node modulus')
    require((rr-uu)/(2*v*rr*rr)==hh*hh/v,'physical strip conversion')
    require(2*rr*rr-2*(uu*uu-yy*yy)==4*yy*yy,'absolute-square budget excess')

    result={'schema':'theta.power_extension.exact_identities.v1',
            'status':'EXACT_RATIONAL_IDENTITIES_NOT_A_THETA_ROOT_OR_COFINAL_CERTIFICATE',
            'source_sha256':SOURCE_HASH,'theta_variance_upper':str(v_upper),
            'theta_second_power_upper':str(q_upper),'absolute_square_barrier':str(R),
            'displayed_barrier_gap':str(gap),'unit_node_counterexample_gap':str(defect),
            'rational_chart_checks':[chart(m,L) for m in range(1,13) for L in (1,4)],
            'confluent_determinant_checks':[collision(m) for m in range(2,13)],
            'complete_pair_power_degrees_checked':26,
            'files_sha256':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
                            for name in ('POWER_SUM_EXTENSION.md','check_power_extension.py')}}
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('EXACT_POWER_EXTENSION_CHECKS_PASSED')


if __name__=='__main__':main()
