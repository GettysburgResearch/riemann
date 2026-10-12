#!/usr/bin/env python3
"""Negative control: same source U/fullcoverage must reject stale R producer."""
import hashlib,json
from pathlib import Path
from enclose_residual_phase8 import panels
from enclose_weighted_lower import enclose
from enclose_analytic_upper import require

p=Path(__file__).parent
source=json.loads((p/'directed_upper_codim8_trial100.json').read_text())
coverage=[{'segment':segment,'left':str(a),'right':str(b)} for segment in range(3) for a,b in panels()]
synthetic={'epsilon':'2^-50','coverage':coverage,'total_panels':len(coverage),
   'endpoint_variation_bound':'.0002','uniform_F_bound':'6e14','entrywise_FF_quadrature_error_total':'0',
   'gauss_order':76,'precision_bits':256,'source_U_receipt':source,'producer_sha256':'0'*64,
   'status':'SYNTHETIC_STALE_PRODUCER_NEGATIVE_CONTROL'}
temporary=p/'.stale_R_negative_control.json'
temporary.write_text(json.dumps(synthetic))
try:
    try:
        enclose(temporary)
    except ArithmeticError as error:
        require(str(error)=='R receipt uses frozen reviewed continuum producer','negative control failed for expected provenance reason')
        result={'status':'STALE_R_PRODUCER_REJECTED','scope':'synthetic diagnostic, no claimed continuum integral',
           'rejection_reason':str(error),'valid_coverage_panels':len(coverage),
           'same_exact_source_U_definition':True,
           'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'weighted_checker_sha256':hashlib.sha256((p/'enclose_weighted_lower.py').read_bytes()).hexdigest()}
    else:
        raise ArithmeticError('stale R producer accepted')
finally:
    temporary.unlink()
print(json.dumps(result,indent=2))
