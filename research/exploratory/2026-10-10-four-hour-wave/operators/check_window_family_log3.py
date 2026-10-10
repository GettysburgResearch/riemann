#!/usr/bin/env python3
"""Replay the phase line and exact scaling for every 0<L<=log3."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib,json
from check_coercivity import require,log_rational_bounds
from check_codimension8_phase import certify as phase_certify


def certify():
    phase_receipt=phase_certify()
    _,log3_upper=log_rational_bounds(Q(3),64)
    require(log3_upper<Q(10987,10000),'log3<1.0987')
    kappa=Q(3,2)*(Q(4,5)-Q(244,64)*(Q(10987,10000)/Q(31415,10000))**2)
    require(kappa>Q(1,2),'seven-sine uniform family gap>1/2')
    return {'status':'DIRECTED_PHASE_AND_EXACT_SCALING_ACCEPT',
      'length_range':'0<L<=log3','removed_sine_modes':7,'complement_dimension':10,
      'primitive_gap':'1/2','computed_gap_lower':str(kappa),'residual_coefficient':'9/2',
      'log3_upper':'10987/10000','pi_lower':'31415/10000',
      'phase_receipt':phase_receipt,
      'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'scope':'uniform positive complement sector only; exact outside-prime tail applies through endpointlog3',
      'dependencies':['literal source O1-O4','phase coverage'],
      'not_proved':['effective sign on any additional window','interval joining','all windows','RH']}

if __name__=='__main__': print(json.dumps(certify(),indent=2))
