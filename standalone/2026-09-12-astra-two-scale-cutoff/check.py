#!/usr/bin/env python3
"""HBR29 bounded exact algebra, authenticated inventory, and real CLI controls.

Standard library only. This checks finite identities, NOT the infinite proofs.
"""
from __future__ import annotations
import argparse
import collections
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

DELAY_DEN = 4
PARENT = '45281093179434e08d28d8e589a8c70d70ead5b9'
PARENT_BLOB = 'd2f12cf36103161b36c21010051770fda8d7d585'


def need(test, message):
    if not test:
        raise ValueError(message)


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True) + '\n'


def strict_load(text):
    def pairs(items):
        out = {}
        for key, value in items:
            need(key not in out, 'duplicate JSON key')
            out[key] = value
        return out
    def forbidden(value):
        raise ValueError('noninteger JSON number: ' + value)
    return json.loads(text, object_pairs_hook=pairs,
                      parse_float=forbidden, parse_constant=forbidden)


def equal_typed(a, b):
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(equal_typed(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(equal_typed(x, y) for x, y in zip(a, b))
    return a == b


def mul(a, b, n=None):
    size = len(a) + len(b) - 1
    if n is not None:
        size = min(size, n + 1)
    out = [Q(0)] * size
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j < size:
                out[i+j] += x*y
    return out


def inverse(a, n):
    need(a[0] != 0, 'noninvertible series')
    out = [1/a[0]]
    for k in range(1, n+1):
        out.append(-sum(a[j]*out[k-j] for j in range(1, min(k, len(a)-1)+1))/a[0])
    return out


def add(a, b):
    out = [Q(0)] * max(len(a), len(b))
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    while len(out) > 1 and out[-1] == 0: out.pop()
    return out


def scale(a, s):
    return [x*s for x in a]


def value(a, x):
    out = Q(0)
    for coef in reversed(a): out = out*x + coef
    return out


def det(a):
    a = [list(row) for row in a]
    out = Q(1)
    for k in range(len(a)):
        pivot = next((j for j in range(k, len(a)) if a[j][k]), None)
        if pivot is None: return Q(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            out = -out
        p = a[k][k]
        out *= p
        for j in range(k+1, len(a)):
            factor = a[j][k]/p
            for h in range(k+1, len(a)):
                a[j][h] -= factor*a[k][h]
    return out


def a_m(m):
    return Q(1) if m == 0 else (1-Q(2)**(1-2*m))/Q(2*m-1)


def direct_B(m):
    out = [Q(0)] * m
    product = [Q(1)]
    for ell in range(m):
        factor = Q(4*math.comb(m-1, ell)*4**ell, math.factorial(2*ell+1))
        for j, x in enumerate(product): out[j] += factor*x
        product = mul(product, [-Q((ell+1)**2), Q(1)])
    return out


def cadd(a, b): return (a[0]+b[0], a[1]+b[1])
def cmul(a, b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def conj(a): return (a[0], -a[1])


def reconstruct():
    groups = collections.Counter()
    def test(group, condition):
        need(condition, 'mathematical failure: '+group)
        groups[group] += 1
    njet = 18
    den = [Q(6**n, math.factorial(2*n+1)) for n in range(njet+1)]
    L = inverse(den, njet)
    moments = [Q(1), Q(1)]
    for n in range(2, njet+1):
        moments.append(a_m(n)/(1-2*a_m(n))*sum(moments[j]*moments[n-j] for j in range(1,n)))
    for n in range(njet+1):
        test('source_coefficients', L[n] == (-1)**n*moments[n])

    modes = list(range(1,13))+[32,64]
    delta_out, ratio_jets = {}, []
    for m in modes:
        c = 2*m-1; eps = Q(2)**(-c); am = a_m(m)
        p, pt, pt_ode = [Q(1)], [Q(1)], [Q(1)]
        for n in range(1, njet+1):
            b = a_m(m+n)/am
            p.append(b/(1-b)*sum(p[j]*L[n-j] for j in range(n)))
            bt = Q(c,c+2*n)
            pt.append(bt/(1-bt)*sum(pt[j]*L[n-j] for j in range(n)))
            pt_ode.append(Q(c,2*n)*sum(L[j]*pt_ode[n-j] for j in range(1,n+1)))
            test('pareto_coefficients', pt[n] == pt_ode[n])
        H = mul(L,p,njet)
        for n in range(1,njet+1):
            test('native_delay_coefficients', (2*n+c)*p[n] == (1-eps*Q(DELAY_DEN)**(-n))/am*H[n])
        invpt = inverse(pt,njet)
        S = mul(p,invpt,njet)
        delayed = [H[n+1]*(1-Q(4)**(-n-1)) for n in range(njet)]
        right = scale(mul(delayed, invpt, njet-1),eps/(2*am))
        for n in range(njet):
            test('survival_derivative_coefficients', (n+1)*S[n+1] == right[n])
        delta = 3*eps*c*(c+2)/(16-(6*c+16)*eps)
        b1 = a_m(m+1)/am
        test('exact_mean_difference', delta == b1/(1-b1)-Q(c,2))
        test('survival_origin_density', -S[1] == delta)
        delta_out[str(m)] = str(delta)
        ratio_jets.append([str(x) for x in S])

    for c in [1,3,5,11,31]:
        m = (c+1)//2; eps = Q(2)**(-c)
        for q in [Q(1,5),Q(1,3),Q(1,2),Q(3,4)]:
            h = (1-q*q)/(1+q*q); hh=(1-q)/(1+q)
            b = (1+q*q)/(1+q)**2
            test('cutoff_density_algebra', eps*(2*hh/h)**c == b**c)
            db = (-q/2)*(2*q*(1+q)**2-2*(1+q*q)*(1+q))/(1+q)**4
            test('cutoff_density_algebra', db == b*q*(1-q)/((1+q)*(1+q*q)))
            for r in [Q(3,2),Q(7,3)]:
                sinh = (1-q**4)/(2*q*q)
                fc = Q(c,2)*h**(c-1)*4*q*q/(1+q*q)**2
                for j in [-1,0,1,2]:
                    t = r*r/6
                    left = t**(m-j-1)*(r/sinh)*(2*h/r)**c*r/3
                    right = Q(2)**(c+1)*Q(6)**(-m+j)/c*r**(1-2*j)*fc
                    test('mellin_normalization', left == right)

    for j in range(1,65):
        q=Q(j,64); b=(1+q*q)/(1+q)**2
        test('global_envelope_constants', 1-b >= q/2)
        if q <= Q(1,2):
            test('global_envelope_constants', (1+q*q)/(1-q)**2 <= 5)
    for c in range(3,128,2):
        eps=Q(2)**(-c)
        test('global_envelope_constants', 16-(6*c+16)*eps >= 8)
        test('global_envelope_constants', 5/(1-eps)<6)
    x=Q(1,3)
    loglo=2*sum(x**(2*k+1)/Q(2*k+1) for k in range(12))
    loghi=loglo+2*x**25/(25*(1-x*x))
    test('global_envelope_constants', Q(2,3)<loglo<loghi<Q(7,10))
    test('global_envelope_constants', Q(7,12)<Q(3,5))
    test('global_envelope_constants', 127**2*129*Q(3,5)**127<1)
    # Symbolic polynomial after c=h+5: 25c^2-9(c+2)(c+4).
    test('global_envelope_constants', add(scale(mul([Q(5),Q(1)],[Q(5),Q(1)]),25),
         scale(mul([Q(7),Q(1)],[Q(9),Q(1)]),-9)) == [Q(58),Q(106),Q(16)])
    budget=Q(12,65)+Q(6,2**32)+Q(1,6*2**128)+Q(194,2**64)
    test('explicit_gamma_window', budget < Q(1,4))
    for n in range(1,41):
        coef=Q(1,math.factorial(2*n-1))+Q(3,math.factorial(2*n+1))-Q(3,math.factorial(2*n))
        test('quantile_coth_bound', coef == Q(4*n*(n-1),math.factorial(2*n+1)) and coef >= 0)

    monic = [[Q(1)],[Q(0),Q(1)]]
    for n in range(1,40):
        monic.append(add([Q(0)]+monic[n],scale(monic[n-1],-Q(n*(n+1),4))))
    polys=[]
    generated=[]
    for m in range(1,21):
        n=m-1; B=direct_B(m); polys.append(B)
        p=monic[2*n]
        factor=Q(4*(-1)**n*2**(2*n),(2*n+1)*math.factorial(2*n))
        expected=[factor*(-1)**j*p[2*j] for j in range(n+1)]
        test('pollaczek_polynomial_identity', B == expected)
        for coefficient in B:
            test('shift_coefficient_positivity', coefficient>0)
        if n==0:
            g=[Q(1)]
        else:
            k=n-1
            numerator=mul([Q(2*(2*k+1)**2),Q(4)],generated[k])
            if k>=1:
                numerator=add(numerator,scale(generated[k-1],-Q(2*k*(2*k-1))))
            g=scale(numerator,Q(1,(2*k+3)*(2*k+2)))
        generated.append(g)
        test('generating_function_ode', scale(g,4)==B)
    for n in range(2,13):
        for x in [Q(-7,3),Q(-1,2),Q(0),Q(4,5),Q(9,2)]:
            a=[[Q(0) for j in range(n)] for i in range(n)]
            for i in range(n):
                a[i][i]=x
                if i+1<n:
                    a[i][i+1]=-Q((i+1)*(i+2),4)
                    a[i+1][i]=-1
            test('jacobi_determinants', det(a)==value(monic[n],x))
        if n%2==0:
            expected=Q((-1)**(n//2))
            for j in range(1,n//2+1): expected*=Q((2*j-1)*(2*j),4)
            test('jacobi_even_origin', monic[n][0]==expected and expected!=0)
    for k in range(1,25):
        A=(Q(k,7),Q(2-k,5)); G=(Q(k+1,3),Q(k-4,11)); H=(Q(1-k,13),Q(k+2,17))
        diff=(G[0]-H[0],G[1]-H[1])
        B=cmul(diff,(Q(0),Q(-1,2)))
        lhs=cmul(A,conj(B))[1]
        rhs=cmul(A,(G[0]-H[0],-G[1]+H[1]))[0]/2
        test('phase_conjugation_sign', lhs==rhs)

    coefficient_record={'ratio_jets':ratio_jets,'B':[[str(x) for x in row] for row in polys]}
    return {
      'schema':'HBR29_BOUNDED_V1','rh_proved':False,
      'scope':'finite exact algebra; no machine proof of analytic theorems or RH',
      'parent_head':PARENT,'parent_proof_blob':PARENT_BLOB,
      'groups':dict(sorted(groups.items())), 'total_checks':sum(groups.values()),
      'explicit_gamma_window_error_upper':str(budget),
      'selected_mean_differences':{str(m):delta_out[str(m)] for m in [1,2,3,12]},
      'first_five_shift_polynomials':[[str(x) for x in p] for p in polys[:5]],
      'coefficient_sha256':hashlib.sha256(canonical(coefficient_record).encode()).hexdigest()
    }


def inventory(root):
    entries={}
    for p in sorted(root.iterdir()):
        need(not p.is_symlink() and p.is_file(), 'nonregular packet entry: '+p.name)
        if p.name != 'SHA256.json':
            entries[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
    return entries


def seal(root):
    data={'schema':'HBR29_SHA256_V1','files':inventory(root)}
    (root/'SHA256.json').write_text(canonical(data),encoding='utf-8')


def authenticate(root):
    manifest=strict_load((root/'SHA256.json').read_text(encoding='utf-8'))
    expected={'schema':'HBR29_SHA256_V1','files':inventory(root)}
    need(equal_typed(manifest,expected),'packet inventory/hash mismatch')


def cli_tests(root):
    with tempfile.TemporaryDirectory(prefix='hbr29_cli_') as tmp:
        dest=Path(tmp)/'packet'
        command=[sys.executable,'-I','-S','-B']
        if sys.flags.optimize: command+=['-O']
        command+=['check.py','--check','result.json']
        def reset():
            if dest.exists(): shutil.rmtree(dest)
            shutil.copytree(root,dest)
        def execute(ok,label):
            p=subprocess.run(command,cwd=dest,text=True,capture_output=True,timeout=45)
            need((p.returncode==0)==ok,'CLI control failed '+label+': '+p.stdout+p.stderr)
            return {'case':label,'returncode':p.returncode}
        reset(); records=[execute(True,'pristine')]
        for name in ['false_rh','wrong_count','wrong_polynomial','boolean_alias','float_token','duplicate_key','wrong_budget','resealed_delay_primitive']:
            reset()
            receipt=dest/'result.json'
            data=strict_load(receipt.read_text(encoding='utf-8'))
            if name=='false_rh': data['rh_proved']=True
            elif name=='wrong_count': data['total_checks']+=1
            elif name=='wrong_polynomial': data['first_five_shift_polynomials'][0][0]='5'
            elif name=='boolean_alias': data['total_checks']=True
            elif name=='wrong_budget': data['explicit_gamma_window_error_upper']='0'
            if name in ['false_rh','wrong_count','wrong_polynomial','boolean_alias','wrong_budget']:
                receipt.write_text(canonical(data),encoding='utf-8')
            elif name=='float_token':
                text=receipt.read_text(encoding='utf-8')
                needle='"total_checks":'+str(data['total_checks'])
                need(text.count(needle)==1,'ambiguous float mutation')
                receipt.write_text(text.replace(needle,needle+'.0'),encoding='utf-8')
            elif name=='duplicate_key':
                text=receipt.read_text(encoding='utf-8')
                receipt.write_text(text.replace('{','{"rh_proved":false,',1),encoding='utf-8')
            else:
                code=dest/'check.py'; text=code.read_text(encoding='utf-8')
                needle='\nDELAY_DEN = 4\n'
                need(text.count(needle)==1,'ambiguous primitive mutation')
                code.write_text(text.replace(needle,'\nDELAY_DEN = 3\n'),encoding='utf-8')
            seal(dest)
            records.append(execute(False,name))
        return records


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--write',type=Path,help='producer only: no authentication')
    group.add_argument('--check',type=Path)
    parser.add_argument('--self-test',action='store_true')
    args=parser.parse_args()
    root=Path(__file__).resolve().parent
    if args.check is not None:
        authenticate(root)
    result=reconstruct(); text=canonical(result)
    if args.write is not None:
        args.write.write_text(text,encoding='utf-8')
        print('PRODUCER_ONLY',result['total_checks'])
        return
    supplied=strict_load(args.check.read_text(encoding='utf-8'))
    need(equal_typed(supplied,result),'reconstructed result mismatch')
    digest=hashlib.sha256(text.encode()).hexdigest()
    print('PASS bounded_checks='+str(result['total_checks'])+' result_sha256='+digest)
    if args.self_test:
        records=cli_tests(root)
        print(canonical({'cli_acceptances':1,'cli_refusals':8,'records':records}),end='')


if __name__=='__main__':
    try:
        main()
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        print('REJECT: '+str(exc),file=sys.stderr)
        sys.exit(1)
