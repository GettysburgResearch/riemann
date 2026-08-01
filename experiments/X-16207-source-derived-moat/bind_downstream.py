#!/usr/bin/env python3
"""Bind a fully closed X-16207 v2 source moat into an X-16204 wrapper."""
from __future__ import annotations
import argparse, copy, hashlib, importlib.util, json, sys
from fractions import Fraction
from pathlib import Path
HERE=Path(__file__).resolve().parent
SPEC=importlib.util.spec_from_file_location('x16207_verify',HERE/'verify.py')
assert SPEC and SPEC.loader
vmod=importlib.util.module_from_spec(SPEC); sys.modules[SPEC.name]=vmod; SPEC.loader.exec_module(vmod)
def sha(obj): return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def fstr(x:Fraction)->str: return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def bind(source:dict,wrapper:dict)->dict:
 checked=vmod.verify(source)
 if checked['classification']!='PRODUCTION_PROFILE_GRAM_CLOSED':
  raise vmod.CertificateError('normalized endpoint and complete arithmetic profile-Gram moats are not both closed')
 endpoint=source['endpoint_relative_ledger']; complete=source['complete_arithmetic_alias']; repl=source['source_derived_replacements']
 out=copy.deepcopy(wrapper)
 radial=out['radial_replay']
 radial.update({'finite_interval_length':'1','transition_bound':'1','initial_error_upper':'0','residual_sup_upper':'0','tail_l2_sq_upper':repl['tail_l2_sq_upper'],'claimed_l2_sq_upper':repl['tail_l2_sq_upper'],'derivative_transition_bound':'1','derivative_initial_error_upper':'0','derivative_residual_sup_upper':'0','derivative_tail_l2_sq_upper':repl['derivative_tail_l2_sq_upper'],'claimed_derivative_l2_sq_upper':repl['derivative_tail_l2_sq_upper'],'primitive_sha256':source['source']['full_exact_proof_object_sha256'],'producer_sha256':source['source']['producer_sha256']})
 pe=out['poisson_endpoint']
 pe.update({'derivative_l1_upper':endpoint['normalized_fourth_derivative_l1_upper'],'claimed_point_upper':endpoint['poisson_endpoint_point_upper'],'claimed_l2_sq_upper':endpoint['poisson_endpoint_l2_sq_upper'],'polylog_channel_sha256':source['source']['full_exact_result_sha256']})
 out['profile_gram'].update({'lower':checked['profile_gram']['complete_lower'],'upper':checked['profile_gram']['complete_upper'],'directed_gram_sha256':sha({'source':source['source'],'complete_alias':complete})})
 deterministic=(vmod.frac(checked['source_derived']['radial_l2_sum_upper'],'radial')+vmod.frac(checked['source_derived']['frequency_derivative_l2_sum_upper'],'derivative')+vmod.frac(endpoint['poisson_endpoint_point_upper'],'point')+vmod.frac(endpoint['poisson_endpoint_l2_norm_upper'],'l2norm'))
 out['scalarization']['deterministic_error_upper']=fstr(deterministic)
 out['source_derived_binding']={'schema':source['schema'],'source_result_sha256':source['source']['full_exact_result_sha256'],'source_proof_object_sha256':source['source']['full_exact_proof_object_sha256'],'binding_sha256':sha({'checked':checked,'endpoint':endpoint,'complete_alias':complete})}
 out.pop('claimed_result_sha256',None); return out
def main()->int:
 ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--source',type=Path,required=True); ap.add_argument('--wrapper',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args()
 try: out=bind(json.loads(a.source.read_text()),json.loads(a.wrapper.read_text())); code=0
 except (OSError,json.JSONDecodeError,vmod.CertificateError,KeyError) as exc: out={'classification':'REJECTED','reason':str(exc)}; code=2
 a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); return code
if __name__=='__main__': raise SystemExit(main())
