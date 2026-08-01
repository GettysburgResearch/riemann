#!/usr/bin/env python3
"""Bind X-16207 source fields into an X-16204 wrapper certificate.

The adapter is fail-closed.  It will not emit a wrapper until a complete
arithmetic-alias lower/upper ledger is present in the source certificate.
"""
from __future__ import annotations
import argparse, copy, hashlib, importlib.util, json, sys
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
SPEC=importlib.util.spec_from_file_location('x16207_verify',HERE/'verify.py')
assert SPEC and SPEC.loader
vmod=importlib.util.module_from_spec(SPEC); sys.modules[SPEC.name]=vmod; SPEC.loader.exec_module(vmod)

def sha(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def fstr(x: Fraction)->str:
    return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"

def bind(source: dict, wrapper: dict)->dict:
    checked=vmod.verify(source)
    if checked['classification']!='PRODUCTION_PROFILE_GRAM_CLOSED':
        raise vmod.CertificateError('complete arithmetic profile-Gram moat is not closed')
    complete=source['complete_arithmetic_alias']
    if complete.get('full_upper') is None:
        raise vmod.CertificateError('complete arithmetic profile-Gram upper bound is missing')
    out=copy.deepcopy(wrapper)
    repl=source['source_derived_replacements']
    full_lower=checked['profile_gram']['complete_lower']
    full_upper=fstr(vmod.frac(complete['full_upper'],'complete_alias.full_upper'))

    radial=out['radial_replay']
    radial.update({
      'finite_interval_length':'1','transition_bound':'1','initial_error_upper':'0','residual_sup_upper':'0',
      'tail_l2_sq_upper':repl['tail_l2_sq_upper'],'claimed_l2_sq_upper':repl['tail_l2_sq_upper'],
      'derivative_transition_bound':'1','derivative_initial_error_upper':'0','derivative_residual_sup_upper':'0',
      'derivative_tail_l2_sq_upper':repl['derivative_tail_l2_sq_upper'],
      'claimed_derivative_l2_sq_upper':repl['derivative_tail_l2_sq_upper'],
      'primitive_sha256':source['source']['full_exact_proof_object_sha256'],
      'producer_sha256':source['source']['producer_sha256']
    })
    endpoint=out['poisson_endpoint']
    endpoint.update({
      'derivative_l1_upper':repl['source_fourth_derivative_l1_upper'],
      'lambda_lower':repl['lambda_lower'],'v_lower':repl['lambda_lower'],
      'pi_lower':repl['pi_lower'],'zeta4_minus_one_upper':repl['zeta4_minus_one_upper'],
      'claimed_point_upper':repl['poisson_endpoint_point_upper'],
      'claimed_l2_sq_upper':repl['poisson_endpoint_l2_sq_upper'],
      'polylog_channel_sha256':source['source']['full_exact_result_sha256']
    })
    out['profile_gram'].update({
      'lower':full_lower,'upper':full_upper,
      'directed_gram_sha256':sha({'source':source['source'],'complete_alias':complete})
    })
    out['scalarization']['deterministic_error_upper']=repl['deterministic_error_upper']
    out['source_derived_binding']={
      'schema':source['schema'],
      'source_result_sha256':source['source']['full_exact_result_sha256'],
      'source_proof_object_sha256':source['source']['full_exact_proof_object_sha256'],
      'binding_sha256':sha({'checked':checked,'complete_alias':complete})
    }
    out.pop('claimed_result_sha256',None)
    return out

def main()->int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source',type=Path,required=True); ap.add_argument('--wrapper',type=Path,required=True); ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    try:
        out=bind(json.loads(args.source.read_text()),json.loads(args.wrapper.read_text())); code=0
    except (OSError,json.JSONDecodeError,vmod.CertificateError,KeyError) as exc:
        out={'classification':'REJECTED','reason':str(exc)}; code=2
    args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    return code
if __name__=='__main__': raise SystemExit(main())
