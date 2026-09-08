#!/usr/bin/env python3
"""Bounded exact algebra and source checks for FC26; not an RH verifier."""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as Q
import hashlib
import json
from math import comb, isqrt
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

FILES = ('PROOF.md', 'README.md', 'REVIEW.md', 'SOURCES.md', 'SOURCE_LOCK.json',
         'VALIDATION.md', 'check.py', 'verification.json', 'SHA256SUMS')
PARENT = '2026-09-07-astra-future-realization'
PINS = {
    'PROOF.md': (17291, 'a50fe8b3f8b1f7d974058144173f6b48e51961178126008e8852868cc837079e',
                 'cd5d68c82169f32da6b41eb788b7313ed5d7e547'),
    'verification.json': (4366, '683ca58d6a6d627e7810a23b14f8603542bc6af4d1997e09e1248c171bb01265',
                         'bd1d5915847416c22a7daa49046d195441b2081d'),
}
LOCK = {
    'repository': 'GettysburgResearch/riemann', 'pr': 812,
    'commit': 'cc5277c34fdbc48787cf650b4627a44a77862f1d',
    'root': 'standalone/' + PARENT,
    'files': {k: {'bytes': v[0], 'sha256': v[1], 'git_blob': v[2]} for k, v in PINS.items()},
    'parent_python_executed': False,
}


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def no_float(value: str):
    raise ValueError('floating or nonfinite JSON number rejected: ' + value)


def pairs(items):
    result = {}
    for k, v in items:
        require(k not in result, 'duplicate JSON key: ' + k)
        result[k] = v
    return result


def loads(text: str):
    return json.loads(text, object_pairs_hook=pairs, parse_float=no_float, parse_constant=no_float)


def encode(data) -> str:
    return json.dumps(data, indent=2, sort_keys=True, ensure_ascii=True) + '\n'


def same(a, b) -> bool:
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(same(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(same(x, y) for x, y in zip(a, b))
    return a == b


def plain(path: Path) -> bytes:
    require(not path.is_symlink(), 'symlink input: ' + str(path))
    require(path.is_file(), 'missing regular file: ' + str(path))
    require(not path.parent.is_symlink(), 'symlink source directory')
    return path.read_bytes()


def source(root: Path):
    lock = loads(plain(root / 'SOURCE_LOCK.json').decode('utf-8'))
    require(same(lock, LOCK), 'source lock drift')
    values = {}
    for name, (size, sha, blob) in PINS.items():
        data = plain(root.parent / PARENT / name)
        require(len(data) == size, 'parent byte length: ' + name)
        require(hashlib.sha256(data).hexdigest() == sha, 'parent SHA256: ' + name)
        git = hashlib.sha1(b'blob ' + str(size).encode() + b'\0' + data).hexdigest()
        require(git == blob, 'parent Git blob: ' + name)
        values[name] = data
    return loads(values['verification.json'].decode('utf-8'))


def inventory(root: Path):
    require(not root.is_symlink(), 'symlink packet')
    require(sorted(p.name for p in root.iterdir()) == sorted(FILES), 'exact inventory differs')
    for name in FILES:
        plain(root / name)
    entries = {}
    for line in plain(root / 'SHA256SUMS').decode('ascii').splitlines():
        bits = line.split('  ')
        require(len(bits) == 2, 'bad manifest row')
        sha, name = bits
        require(name not in entries and name in FILES and name != 'SHA256SUMS', 'bad manifest name')
        require(len(sha) == 64 and all(c in '0123456789abcdef' for c in sha), 'bad manifest digest')
        entries[name] = sha
    require(set(entries) == set(FILES) - {'SHA256SUMS'}, 'manifest is not complete')
    for name, sha in entries.items():
        require(hashlib.sha256(plain(root / name)).hexdigest() == sha, 'manifest mismatch: ' + name)


def seal(root: Path):
    (root / 'SHA256SUMS').write_text(''.join(
        hashlib.sha256((root / n).read_bytes()).hexdigest() + '  ' + n + '\n'
        for n in sorted(FILES) if n != 'SHA256SUMS'), encoding='ascii')


def peval(a, x):
    result = Q(0)
    for value in reversed(a):
        result = result * x + value
    return result


def pmul(a, b):
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def inverse(a):
    n = len(a)
    rows = [[Q(x) for x in a[i]] + [Q(i == j) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if rows[i][j]), None)
        require(pivot is not None, 'singular synthetic matrix')
        rows[j], rows[pivot] = rows[pivot], rows[j]
        divisor = rows[j][j]
        rows[j] = [x / divisor for x in rows[j]]
        for i in range(n):
            if i != j:
                q = rows[i][j]
                rows[i] = [x - q * y for x, y in zip(rows[i], rows[j])]
    return [row[n:] for row in rows]


def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def reconstruct(root: Path):
    parent = source(root)
    counts = Counter()
    def test(name, condition):
        require(bool(condition), 'algebra control: ' + name)
        counts[name] += 1
    coeff = [Q(x) for x in parent['actual_source']['coefficients']]
    test('authenticated_trial_coefficients', coeff == [Q(x, 10000) for x in (4284,-1839,-1199,-742,-371)])
    feed = sum(coeff)
    atom = -feed * feed
    test('ideal_feedthrough', feed == Q(133, 10000))
    test('second_iterate_atom', atom == -Q(17689, 100000000))
    comp = [sum(coeff[j] * comb(j, r) * (-1)**r for j in range(r, len(coeff)))
            for r in range(len(coeff))]
    cor = pmul([Q(1), Q(-1)], comp)
    test('independent_feedthrough_square', pmul(cor, cor)[0] == -atom)
    for a in range(1, 17):
        u = Q(a, 19)
        test('rational_feedback_expansion', peval(cor, u) == (1-u)*peval(coeff, 1-u))
    for trial in ([Q(1)], [Q(1),Q(-1)], coeff, [Q(2),Q(-3),Q(1)]):
        c0 = sum(trial)
        # Two independent computations of the degree-zero rational feedthrough.
        local = [sum(trial[j]*comb(j,r)*(-1)**r for j in range(r,len(trial)))
                 for r in range(len(trial))]
        test('arbitrary_polynomial_feedthrough', pmul(pmul([Q(1),Q(-1)],local),
                                                    pmul([Q(1),Q(-1)],local))[0] == c0*c0)
    pset = [p for p in range(2, 258) if prime(p)]
    families = [[Q(2)], [Q(3,2),Q(5,3),Q(7)], [Q(49,25),Q(9,4),Q(11,7)],
                [Q(2),Q(4),Q(8),Q(16)]]
    aliases = []
    for ratios in families:
        exceptional = {r.numerator for r in ratios if prime(r.numerator)}
        hits = {p for p in pset if any((Q(p)/r).denominator == 1 for r in ratios)}
        test('exceptional_prime_classification', hits == exceptional.intersection(pset))
        for p in pset:
            test('uncancelled_prime_frequency', p in exceptional or
                 all((Q(p)/r).denominator != 1 for r in ratios))
        aliases.append({'dilations': list(map(str,ratios)), 'exceptional_primes':sorted(exceptional)})
    for n in range(1, 129):
        a = sum(c for d,c in ((1,1),(2,-2)) if n%d == 0)
        test('actual_seed_dirichlet_coefficients', a == (1 if n%2 else -1))
    test('jensen_log_ratio_constant', Q(1,13)/(1+Q(1,13)) == Q(1,14))
    test('harnack_radius_ratio', (Q(13,8)+Q(3,2))/(Q(13,8)-Q(3,2)) == 25)
    test('near_zero_disk_cover', Q(25,16)**2+Q(1,4)**2 < Q(13,8)**2)
    test('safe_exponential_constant', Q(8,3)**9 > 3744)
    test('count_coefficient_majorant', 416*938 < 2**19)
    for t in [Q(j,3) for j in range(31)]:
        test('safe_source_polynomial_envelope', (t+4)*(4*t+13) <= 52*(1+t)**2)
    ranks = list(range(1, 65)) + [2**j for j in range(7,33)]
    floor_rows = []
    for n in ranks:
        k = (n-1).bit_length()
        N = 14*(64*n+3)*(9+k)
        delta = Q(1,128*n*N)
        E = 42*k*k+726*k+3128
        J = 168*k*k+2904*k+12513
        S = 4*(J+k+10)
        test('small_set_budget', Q(1,16*n)+2*delta*N == Q(5,64*n))
        test('exceptional_radius_range', 0 < delta < Q(1,16))
        test('count_log_budget', 416*n*N < 2**(23+3*k))
        test('squared_floor_exponent', J == 1+4*E and E == (9+k)*(347+42*k)+k+5)
        test('source_cutoff_integer_budget', (12*n*(S+3) << J) <= (1 << (S//2)))
        if n in (1,2,16,64,2**16,2**24,2**32):
            floor_rows.append({'dimension':n, 'dyadic_log_ceiling':k,
                               'floor_denominator_power_of_2':J, 'source_time_cutoff':S})
    for x in range(65):
        test('cutoff_induction_bound', 12*(4*x+43) <= 2**(x+20))
        test('dyadic_log_auxiliary', 9+x <= 2**(x+4))
    synthetic=[]
    for n in range(1,9):
        # Construct Gram directly from the shifted coefficient vectors of 1-2w.
        vectors=[]
        for i in range(n):
            v=[Q(0)]*(n+1); v[i]=1; v[i+1]=-2; vectors.append(v)
        gram=[[sum(a*b for a,b in zip(v,w)) for w in vectors] for v in vectors]
        test('synthetic_gram_entries', all(gram[i][j] == (5 if i==j else -2 if abs(i-j)==1 else 0)
                                          for i in range(n) for j in range(n)))
        err=1-inverse(gram)[0][0]
        exact=Q(3*4**n,4**(n+1)-1)
        test('nonzero_limit_fast_convergence', err == exact and err-Q(3,4)==Q(3,4*(4**(n+1)-1)))
        synthetic.append({'dimension':n, 'squared_error':str(err)})
    return {
        'schema':'riemann-feedback-conditioning-v1',
        'scientific_status':'PROPOSED_COMPONENT_PROOFS_REVIEW_REQUIRED',
        'rh_proved':False, 'growing_horizon_bound_proved':False,
        'fixed_controller_schur_premise_proved':False,
        'new_actual_zeta_values_evaluated':False,
        'parent_numerical_certificate_replayed':False,
        'scope':{'prime_fixture_max':257, 'rational_feedback_points':16,
                 'rank_dimensions':ranks, 'synthetic_max_dimension':8,
                 'arithmetic':'integers_and_Fraction_only'},
        'ideal_parent_polynomial':list(map(str,coeff)),
        'ideal_feedthrough':str(feed), 'second_iterate_dirac_mass':str(atom),
        'finite_alias_controls':aliases, 'rational_floor_panels':floor_rows,
        'synthetic_nonzero_floor':synthetic,
        'controls':dict(sorted(counts.items())), 'bounded_control_count':sum(counts.values()),
    }


def check(root: Path):
    inventory(root)
    actual=loads(plain(root/'verification.json').decode('utf-8'))
    expected=reconstruct(root)
    require(same(actual,expected), 'primitive reconstruction differs')
    return expected


def rejections(root: Path):
    labels=('rh_flag','boolean_alias','wrong_atom','narrowed_scope','wrong_floor',
            'false_multiplier_status','float_value','duplicate_key','extra_file',
            'empty_manifest','changed_parent','symlink')
    cmd=[sys.executable,'-B']+(['-O'] if sys.flags.optimize else [])
    results=[]
    with tempfile.TemporaryDirectory(prefix='fc26-tests-') as tmp:
        base=Path(tmp)
        for label in ('pristine',)+labels:
            parent=base/label/'standalone'; dst=parent/root.name
            shutil.copytree(root,dst)
            (parent/PARENT).mkdir()
            for name in PINS:
                shutil.copyfile(root.parent/PARENT/name,parent/PARENT/name)
            obj=loads((dst/'verification.json').read_text())
            if label=='rh_flag': obj['rh_proved']=True
            elif label=='boolean_alias': obj['bounded_control_count']=True
            elif label=='wrong_atom': obj['second_iterate_dirac_mass']='17689/100000000'
            elif label=='narrowed_scope': obj['scope']['prime_fixture_max']=127
            elif label=='wrong_floor': obj['rational_floor_panels'][0]['floor_denominator_power_of_2']+=1
            elif label=='false_multiplier_status': obj['fixed_controller_schur_premise_proved']=True
            elif label=='float_value': obj['bounded_control_count']=1.0
            elif label=='duplicate_key':
                text=(dst/'verification.json').read_text().replace('{','{"rh_proved":false,',1)
                (dst/'verification.json').write_text(text); seal(dst)
            elif label=='extra_file': (dst/'unexpected.txt').write_text('untracked input\n')
            elif label=='empty_manifest': (dst/'SHA256SUMS').write_text('')
            elif label=='changed_parent':
                with (parent/PARENT/'PROOF.md').open('ab') as f: f.write(b'\n')
            elif label=='symlink':
                data=(dst/'README.md').read_bytes(); (dst/'README.md').unlink()
                outside=base/label/'outside.md'; outside.write_bytes(data)
                (dst/'README.md').symlink_to(outside)
            if label in labels[:7]:
                (dst/'verification.json').write_text(encode(obj)); seal(dst)
            p=subprocess.run(cmd+[str(dst/'check.py')],capture_output=True,text=True,timeout=20)
            expected_ok=(label=='pristine')
            require((p.returncode==0)==expected_ok,'rejection outcome: '+label+' '+p.stdout+p.stderr)
            results.append({'case':label,'returncode':p.returncode,'expected_accept':expected_ok})
    return {'cases':results,'corruption_refusals':len(labels),'pristine_controls':1}


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--rejections',action='store_true')
    args=parser.parse_args(); root=Path(__file__).resolve().parent
    try:
        data=check(root)
        if args.rejections:
            print(encode(rejections(root)),end='')
        else:
            print(encode({'result':'PASS_BOUNDED_FC26','checks':data['bounded_control_count'],
                          'verification_sha256':hashlib.sha256(encode(data).encode()).hexdigest(),
                          'rh_proved':False}),end='')
        return 0
    except (ValueError, OSError, KeyError, StopIteration, TypeError, subprocess.TimeoutExpired) as exc:
        print('REJECT: '+str(exc),file=sys.stderr); return 1


if __name__=='__main__':
    raise SystemExit(main())
