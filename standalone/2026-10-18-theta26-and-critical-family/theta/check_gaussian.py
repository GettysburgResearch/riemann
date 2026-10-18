#!/usr/bin/env python3
"""Directed existence certificates for real-zero theta jets22,24,26.

No numerical root finder, zeta-zero table, stochastic simulation, or empirical
residual is trusted. The complete source intervals and every finite polynomial
value/Jacobian are recomputed with directed integer interval arithmetic.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import argparse,hashlib,json
import source26

ROOT=Path(__file__).resolve().parent
SOURCE_HASH='c171903e4f60c189a929ccfcce36f7db034508e9ca10c85ed766338625558dcf'


def require(ok,message):
    if not ok:raise ValueError(message)


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'))+'\n'


def check_model(model,source,b):
    I=b.I;S=b.SCALE
    degree=model['degree'];N=model['nodes'];m=degree//2-1
    require(degree in (22,24,26),'supported even theta order')
    centers=[F(x)for x in model['centers']]
    active=model['active'];radius=F(model['radius'])
    require(len(centers)==N and len(active)==m,'finite model dimensions')
    require(len(set(active))==m and all(type(j)is int and 0<=j<N for j in active),'distinct valid active coordinates')
    require(radius>0,'positive rational radius')
    R=[[I.coerce(F(x))for x in row]for row in model['preconditioner']]
    require(len(R)==m and all(len(row)==m for row in R),'square rational preconditioner')
    point=[I.coerce(x)for x in centers]
    rad=I.coerce(radius)
    cube=[I(x.lo-rad.hi,x.hi+rad.hi)if j in active else x
          for j,x in enumerate(point)]
    require(all(x.lo>0 for x in cube),'every quadratic node stays strictly positive')
    gaussian=I.rat(1,2)-sum(cube,I.coerce(0))
    require(gaussian.lo>0,'strictly positive remaining Gaussian variance budget')
    # The complete source uses the actual standardized theta law, not a
    # polynomial truncation or an imported zeta-zero list.
    moments=[I(*pair)for pair in source['standardized_moments']]
    kap=b.cumulants(moments)
    targets=[((-1)**(r+1))*r*kap[2*r]/factorial(2*r)
             for r in range(2,m+2)]
    values=[sum((x**r for x in point),I.coerce(0))for r in range(2,m+2)]
    residual=[x-y for x,y in zip(values,targets)]
    correction=[sum((v*x for v,x in zip(row,residual)),I.coerce(0))for row in R]
    beta=max(b.absup(x)for x in correction)
    jacobian=[[r*cube[j]**(r-1)for j in active]for r in range(2,m+2)]
    defect=[]
    for i in range(m):
        row=[]
        for j in range(m):
            row.append(I.coerce(int(i==j))-sum((R[i][k]*jacobian[k][j]
                                                for k in range(m)),I.coerce(0)))
        defect.append(row)
    lip=max(sum(b.absup(x)for x in row)for row in defect)
    require(lip<S,'whole-cube Newton contraction')
    # beta and lip are upward bounds in units1/S. This exact rational
    # inequality proves T(B) lies strictly inside B for the actual source.
    require(F(beta,S)+F(lip,S)*radius<radius,'strict self mapping of full parameter cube')
    return {
        'degree':degree,'nodes':N,'active':active,
        'status':'DIRECTED_EXISTENCE_AND_UNIQUENESS_IN_ACTIVE_CUBE',
        'radius':str(radius),'beta_upper_units':beta,'jacobian_contraction_upper_units':lip,
        'strict_self_mapping_slack':str(radius-F(beta,S)-F(lip,S)*radius),
        'minimum_node_lower_units':min(x.lo for x in cube),
        'gaussian_parameter_interval':gaussian.record(),
        'whole_plane_envelope':'exp(abs(z)^2/2) in variance-one theta variable',
        'all_zeros':'real; exactly the roots +/-1/sqrt(b_j), with multiplicity',
        'matching':'all Taylor coefficients through the stated even degree',
        'target_power_sum_intervals':[x.record()for x in targets],
        'point_power_sum_residual_intervals':[x.record()for x in residual],
    }


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--source',type=Path,default=source26.DEFAULT_SOURCE)
    p.add_argument('--source-json',type=Path,default=ROOT/'theta26_source.json')
    p.add_argument('--parameters',type=Path,default=ROOT/'gaussian_parameters.json')
    p.add_argument('--rebuild-source',action='store_true')
    p.add_argument('--output',type=Path,default=ROOT/'gaussian_certificate.json')
    args=p.parse_args()
    b,primitive_sha=source26.load_primitive(args.source)
    if args.rebuild_source:
        source=source26.reconstruct(args.source,progress=True)
        text=canonical(source)
        require(hashlib.sha256(text.encode()).hexdigest()==SOURCE_HASH,'fresh full-source reconstruction digest')
        if args.source_json.exists():require(args.source_json.read_text()==text,'source JSON equals fresh complete reconstruction')
        else:args.source_json.write_text(text)
    else:
        raw=args.source_json.read_bytes()
        require(hashlib.sha256(raw).hexdigest()==SOURCE_HASH,'authenticated complete-source digest')
        source=json.loads(raw)
    require(source['bits']==b.BITS and source['degree']==b.DEGREE and source['max_moment']==26,'source arithmetic configuration')
    require(source['primitive_sha256']==primitive_sha,'source primitive binding')
    parameters_raw=args.parameters.read_bytes();parameters=json.loads(parameters_raw)
    require(parameters['schema']=='gaussian.theta.jets.parameters.v1','parameter schema')
    records=[]
    for model in parameters['models']:
        item=check_model(model,source,b);records.append(item)
        print('CERTIFIED_REAL_ZERO_THETA_JET',item['degree'],'NODES',item['nodes'],
              'BETA',float(F(item['beta_upper_units'],b.SCALE)),
              'CONTRACTION',float(F(item['jacobian_contraction_upper_units'],b.SCALE)),flush=True)
    require([r['degree']for r in records]==[22,24,26],'complete declared order coverage')
    result={'schema':'gaussian.theta.jets.certificate.v1','status':'DIRECTED_PASS',
            'bits':b.BITS,'source_sha256':SOURCE_HASH,
            'primitive_sha256':primitive_sha,
            'parameters_sha256':hashlib.sha256(parameters_raw).hexdigest(),
            'source_producer_sha256':hashlib.sha256(Path(source26.__file__).read_bytes()).hexdigest(),
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'models':records,
            'claim_limit':'Finite real-zero entire approximants only; cofinal construction and a new zeta boundary are not proved.'}
    output=canonical(result);args.output.write_text(output)
    print('GAUSSIAN_THETA_JETS_DIRECTED_PASS',hashlib.sha256(output.encode()).hexdigest(),flush=True)


if __name__=='__main__':main()
