"""Authenticate this research packet and reconstruct both complete zero witnesses.

This checks the supplied analytic certificate's finite arithmetic, not RH,
independent mathematical review, or any repository-wide validation.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
import sys

FILES = frozenset(('README.md','PROOF.md','CERTIFICATE.md','SOURCE_LOCK.json',
                  'VALIDATION.md','interval.py','certificate.py','verify.py',
                  'test_verify.py','results.json','SHA256SUMS'))
ROOT = Path(__file__).absolute().parent

def require(ok, message):
    if not ok: raise ValueError(message)

def strict_json(raw):
    def pairs(items):
        out = {}
        for key,value in items:
            require(key not in out,'duplicate JSON key: '+key)
            out[key] = value
        return out
    def bad_number(value):
        raise ValueError('floating or nonfinite JSON number: '+value)
    return json.loads(raw,object_pairs_hook=pairs,parse_float=bad_number,
                      parse_constant=bad_number)

def authenticate(root):
    require(root.is_dir() and not root.is_symlink(),'packet root')
    require(set(p.name for p in root.iterdir()) == FILES,'complete packet inventory')
    for name in FILES:
        p = root/name
        require(p.is_file() and not p.is_symlink(),'regular file required: '+name)
        require(p.stat().st_size < 2_000_000,'file size: '+name)
    lines = (root/'SHA256SUMS').read_text().splitlines()
    got = {}
    for line in lines:
        pieces = line.split('  ')
        require(len(pieces)==2,'checksum line')
        digest,name = pieces
        require(name in FILES-{'SHA256SUMS'} and name not in got,'checksum coverage')
        require(len(digest)==64 and all(c in '0123456789abcdef' for c in digest),'checksum format')
        require(hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,'changed file: '+name)
        got[name] = digest
    require(set(got)==FILES-{'SHA256SUMS'},'checksum inventory incomplete')
    return got

def typed_equal(a,b):
    if type(a) is not type(b): return False
    if type(a) is dict:
        return set(a)==set(b) and all(typed_equal(a[k],b[k]) for k in a)
    if type(a) is list:
        return len(a)==len(b) and all(typed_equal(x,y) for x,y in zip(a,b))
    return a==b

def receipt_shape(data):
    require(type(data) is dict,'receipt object')
    require(data.get('status')=='PROPOSED_COMPUTER_ASSISTED_COMPONENT','status')
    for key in ('rh_proved','zero_of_zeta_claimed','collision_location_certified'):
        require(data.get(key) is False,'false claim flag: '+key)
    for key,value in (('bits',512),('degree',40),('cells_per_case',256)):
        require(type(data.get(key)) is int and data[key]==value,'numeric coverage: '+key)
    cases=data.get('cases')
    require(type(cases) is list and len(cases)==2,'case coverage')
    names=('integer_N4','step_2_to_3_u_7_10')
    for j,row in enumerate(cases):
        require(type(row) is dict and row.get('name')==names[j],'case identity/order')
        require(row.get('one_simple_nonreal_zero') is True,'zero-count flag')
        require(row.get('disk_inside_xi_critical_band') is bool(j),'critical-band flag')
        require(row.get('radius')=='1/1000000000000','disk radius')
        require(type(row.get('guards')) is dict,'guards')
        for key in ('dominant_ratio','gamma_simplex_coefficient','tilt'):
            pair=row['guards'].get(key)
            require(type(pair) is list and len(pair)==2 and all(type(x) is int for x in pair),'rational guard')
        jets=row.get('integral_jets')
        require(type(jets) is list and len(jets)==3,'derivative coverage')
        for jet in jets:
            require(type(jet) is list and len(jet)==2,'complex enclosure')
            for pair in jet:
                require(type(pair) is list and len(pair)==2 and all(type(x) is str for x in pair),'dyadic endpoints')

def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

def primitive_controls(cert):
    expected=((Q(1),Q(4),Q(9),Q(16)),(Q(1),Q(4),Q(90,7)))
    require(tuple(row[1] for row in cert.CASES)==expected,'literal gamma rates')
    for rates in expected:
        for q in (Q(0),Q(1,5),Q(1),Q(7),Q(31,3)):
            product=Q(1)
            for a in rates: product *= (a/(q+a))**2
            expanded=sum((b/(q+a)**2+b*c/(q+a) for a,b,c in cert.rows(rates)),Q(0))
            require(product==expanded,'independent gamma transform control')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',type=Path,required=True)
    args=parser.parse_args()
    before=authenticate(ROOT)
    require(args.check.is_file() and not args.check.is_symlink(),'receipt regular file')
    require(args.check.stat().st_size<200_000,'receipt size')
    raw=args.check.read_bytes();wanted=strict_json(raw);receipt_shape(wanted)
    cert=load_module('_gamma_certificate',ROOT/'certificate.py')
    primitive_controls(cert)
    actual=cert.reconstruct()
    require(typed_equal(wanted,actual),'complete reconstruction disagrees')
    require(args.check.read_bytes()==raw,'receipt changed during reconstruction')
    require(authenticate(ROOT)==before,'packet changed during reconstruction')
    print('PASS_COMPLETE_TWO_DISK_RECONSTRUCTION')

if __name__=='__main__':
    try: main()
    except (ValueError,OSError,TypeError,KeyError,ArithmeticError) as exc:
        print('FAIL_GAMMA_CERTIFICATE: '+str(exc),file=sys.stderr)
        sys.exit(1)
