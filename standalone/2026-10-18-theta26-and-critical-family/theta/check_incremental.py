#!/usr/bin/env python3
"""Directed existence of the 84/order24 and 104/order26 extension endpoints.

This checker certifies a complete active parameter cube. It does not certify
the numerical path which produced the center or rely on its tiny residual.
"""
from pathlib import Path
import argparse,hashlib,json
import check_gaussian as g
import source26

ROOT=Path(__file__).resolve().parent


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source',type=Path,default=source26.DEFAULT_SOURCE)
    p.add_argument('--source-json',type=Path,default=ROOT/'theta26_source.json')
    p.add_argument('--parameters',type=Path,default=ROOT/'incremental_parameters.json')
    p.add_argument('--output',type=Path,default=ROOT/'incremental_certificate.json')
    args=p.parse_args()
    b,primitive_sha=source26.load_primitive(args.source)
    raw=args.source_json.read_bytes()
    g.require(hashlib.sha256(raw).hexdigest()==g.SOURCE_HASH,
              'authenticated complete theta source')
    source=json.loads(raw)
    g.require(source['bits']==b.BITS and source['degree']==b.DEGREE
              and source['max_moment']==26,'source configuration')
    g.require(source['primitive_sha256']==primitive_sha,'source primitive binding')
    parameter_raw=args.parameters.read_bytes();parameters=json.loads(parameter_raw)
    g.require(parameters['schema']=='gaussian.theta.incremental.parameters.v1',
              'incremental parameter schema')
    g.require([(m['degree'],m['nodes'])for m in parameters['models']]==[(24,84),(26,104)],
              'declared incremental model coverage')
    records=[]
    for model in parameters['models']:
        old=model['nodes']-20
        g.require(all(j<old for j in model['active']),
                  'only old nodes vary in the endpoint certificate')
        g.require(len(model['centers'])==model['nodes'] and
                  all(x==model['centers'][old]for x in model['centers'][old:]),
                  'the 20 appended nodes are identical and fixed')
        record=g.check_model(model,source,b)
        record['fixed_cloud']={'multiplicity':20,'node':model['centers'][old]}
        records.append(record)
        print('CERTIFIED_INCREMENTAL_THETA_ENDPOINT',model['degree'],model['nodes'],flush=True)
    hashes={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
            for name in ['source26.py','check_gaussian.py',Path(__file__).name]}
    result={'schema':'gaussian.theta.incremental.certificate.v1','status':'DIRECTED_PASS',
            'bits':b.BITS,'source_sha256':g.SOURCE_HASH,
            'primitive_sha256':primitive_sha,
            'parameters_sha256':hashlib.sha256(parameter_raw).hexdigest(),
            'code_sha256':hashes,'models':records,
            'claim_limit':'The 84/order24 and 104/order26 endpoints exist, each with 20 equal fixed cloud nodes. The numerical continuation paths, cofinal construction, and a new zeta boundary are not certified.'}
    text=g.canonical(result);args.output.write_text(text)
    print('INCREMENTAL_THETA_ENDPOINTS_DIRECTED_PASS',
          hashlib.sha256(text.encode()).hexdigest(),flush=True)


if __name__=='__main__':main()
