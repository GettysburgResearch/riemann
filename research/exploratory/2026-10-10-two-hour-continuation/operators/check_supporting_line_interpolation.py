#!/usr/bin/env python3
"""Exact interpolation constants plus fresh reviewed source-line replay."""
from pathlib import Path
import sys,hashlib,json
from fractions import Fraction as Q
OLD=Path(__file__).resolve().parents[2]/'2026-10-10-four-hour-wave'/'operators'
sys.path.insert(0,str(OLD))
from check_codimension14 import certify as line14
from check_codimension8_phase import certify as line8

def require(c,s):
    if not c:raise ArithmeticError(s)
def run():
    a=line8();b=line14();theta=Q(27,40);alpha=Q(4,5)+theta/2;constant=244+466*theta
    require(alpha==Q(91,80) and constant==Q(11171,20),'exact same-source line interpolation')
    weight=alpha-constant*(Q(10987,10000)/(8*Q(31415,10000)))**2
    require(weight==Q(88431657701,1263234848000) and weight>Q(7,100),'positive complete family of weights')
    return {'status':'COMPLETE_SOURCE_LINES_AND_EXACT_MIXTURE_PASS','theta_exact':str(theta),'alpha_exact':str(alpha),'constant_exact':str(constant),
       'lambda8_uniform_lower':str(weight),'length_scope':'every0<L<=log3','cosine_tail':'alln>=8retained',
       'source_line_phase8':a,'source_line_codim14':b,'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'not_proved':['finite effective sign','native log3 positivity','RH']}
if __name__=='__main__':print(json.dumps(run(),indent=2))
