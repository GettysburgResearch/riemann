#!/usr/bin/env python3
"""Independent count-free geometry, source binding, rational guards and prefix signs.

This audit never invokes a complete-zero-count routine. The original 8049
endpoint sign facts are imported. It separately replays all 222 refined
endpoint signs from direct Gamma/zeta expressions, without count assumptions.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
import flint
from flint import acb, arb, ctx, fmpq

HERE = Path(__file__).resolve().parent
WAVE = HERE.parents[1]
SOURCE = WAVE/'xi'/'outer-ray'


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit('FAIL: '+message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = 224
    require(flint.__version__ == '0.9.0' and flint.__FLINT_VERSION__ == '3.6.0', 'native backend versions')
    receipts = {name:json.loads((SOURCE/name).read_text()) for name in
                ['count_free_census.json','native_slab_certificate.json','refined_prefix_moments.json']}
    countfree = receipts['count_free_census.json']
    require(countfree['status'] == 'PASS_DIRECTED_COUNT_FREE_CENSUS_GUARDS', 'accepted owner guard receipt')
    authenticated = set()
    for receipt in receipts.values():
        for path, expected in receipt['source_sha256'].items():
            require(sha(WAVE/path) == expected, 'direct source binding '+path)
            authenticated.add(path)
    owner_tree = ast.parse((SOURCE/'check_count_free_census.py').read_text())
    owner_attributes = {node.attr for node in ast.walk(owner_tree) if isinstance(node,ast.Attribute)}
    require('zeta_nzeros' not in owner_attributes, 'no native complete count invocation')
    require('zeta_zeros' not in owner_attributes, 'no native complete zero enumeration invocation')
    require(not any(isinstance(node, ast.Assert) for node in ast.walk(owner_tree)), 'explicit acceptance branches survive optimized Python')
    original = json.loads((SOURCE/'native_candidates.json').read_text())
    refined = json.loads((SOURCE/'refined_prefix_candidates.json').read_text())
    require(original['normalization'] == refined['normalization'] == countfree['normalization'] == 'Xi(z)=xi(1/2+i*z)', 'actual-source normalization')
    oldden,newden = 2**24,2**80
    require(original['denominator'] == oldden and refined['denominator'] == newden, 'exact denominators')
    selected=[]
    previous=Q(0)
    for j,(lo,hi) in enumerate(original['interval_numerators']):
        a,b=Q(lo,oldden),Q(hi,oldden)
        require(previous<a<b<Q(8192), 'strict original positive disjoint geometry')
        previous=b
        if j<len(refined['interval_numerators']):
            nlo,nhi=refined['interval_numerators'][j]
            na,nb=Q(nlo,newden),Q(nhi,newden)
            require(a<na<nb<b and nhi==nlo+1, 'strict refined nesting')
            a,b=na,nb
        selected.append((a,b))
    require(len(selected) == 8049 and len(refined['interval_numerators']) == 111, 'selected interval cardinalities only')
    half=arb(fmpq(1,2))
    pi_log=arb.pi().log()
    def hardy(t:arb)->arb:
        phase=acb(arb(fmpq(1,4)),t/2).lgamma().imag-t*pi_log/2
        result=acb(0,phase).exp()*acb(half,t).zeta()
        require(result.imag.contains(0), 'direct Hardy reality enclosure')
        return result.real
    for lo,hi in refined['interval_numerators']:
        lv,hv=hardy(arb(fmpq(lo,newden))),hardy(arb(fmpq(hi,newden)))
        require((lv>0 and hv<0) or (lv<0 and hv>0), 'direct strict refined Hardy crossing')
    require(Q(22,7)**3/63<Q(99,200), 'zero-free-disk rational margin')
    require(Q(countfree['strict_native_xi_zero_seed_lower'])>Q(99,200), 'directed native seed receipt margin')
    # Independent Gaussian-integer multiplication obtains cos(6 atan(1/10)).
    re,im=Q(1),Q(0)
    for _ in range(6):
        re,im=5*re-Q(1,2)*im,Q(1,2)*re+5*im
    projection=re/Q(101,4)**3
    require(projection==Q(851499,1030301)==Q(countfree['exact_global_angular_projection'])>0, 'independent exact angular projection')
    lower,upper=map(Q,countfree['residual_inverse_sixth_moment_interval'])
    require(0<lower<=upper, 'strict complete residual enclosure')
    recovered=[]
    for domain in countfree['recovered_domains']:
        H=domain['height']
        require(all(b<H or a>H for a,b in selected), 'no interval crosses selected height')
        ratio=upper*(Q(H*H)+Q(1,4))**3/projection
        below=sum(b<H for a,b in selected)
        require(ratio<Q(1) and ratio==Q(domain['exclusion_ratio_upper']), 'strict whole-source rational exclusion')
        require(Q(1)-ratio==Q(domain['strict_exclusion_margin']), 'literal guard margin')
        require(below==domain['recovered_complete_simple_positive_zero_count'], 'finite geometric census size')
        require(domain['maximum_derivative_order']==2*H-3, 'precise positive column width range')
        recovered.append({'height':H,'selected_intervals_below_height':below,'exclusion_ratio_upper':str(ratio)})
    package=Path(flint.__file__).resolve().parent
    binaries=[package/'types'/name for name in ['arb.abi3.so','acb.abi3.so','acb_series.abi3.so']]
    binaries.extend(sorted((package.parent/'python_flint.libs').glob('lib*.so*')))
    for binary in binaries:
        require(sha(binary)==countfree['backend_binary_sha256'][binary.name], 'current native binary binding')
    sources=sorted(authenticated | {'xi/outer-ray/'+name for name in receipts})
    sources.append(str(Path(__file__).resolve().relative_to(WAVE)))
    report={
        'status':'PASS_INDEPENDENT_COUNT_FREE_SOURCE_GEOMETRY_GUARDS_AND_REFINED_SIGNS',
        'reviewed_proof_sha256':sha(SOURCE/'COUNT_FREE_CENSUS_RECOVERY.md'),
        'reviewed_owner_checker_sha256':sha(SOURCE/'check_count_free_census.py'),
        'owner_receipt_sha256':sha(SOURCE/'count_free_census.json'),
        'all_transitive_receipt_direct_source_hashes_checked':True,
        'refined_native_endpoint_signs_independently_replayed_without_count':222,
        'original_8049_interval_endpoint_signs_imported_not_replayed':True,
        'original_interval_geometry_checked':8049,
        'count_routine_called':False,'different_arithmetic_backend_used':False,
        'analytic_theta_product_strip_column_theorems_authenticated_by_finite_audit':False,
        'recovered_domains':recovered,'rh_proved':False,
        'source_sha256':{path:sha(WAVE/path) for path in sources},
        'backend_binary_sha256':{path.name:sha(path) for path in binaries},
    }
    args.output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(report['status'],flush=True)


if __name__=='__main__':
    main()
