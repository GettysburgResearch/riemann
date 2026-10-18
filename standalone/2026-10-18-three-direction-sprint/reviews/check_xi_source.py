"""Independent original-theta moment check from the completed-zeta Taylor jet.

This imports none of the theta quadrature, cumulant recurrence, model, or
certificate code. Arb's analytic series for Gamma and zeta evaluate xi(1/2+t).
The imported mathematical interface is the classical theta/xi Fourier identity.
This corroborates the complete-source enclosures and their normalization;
it does not replace the finite model's whole-box existence certificate.
"""
import argparse
import hashlib
import json
from math import factorial
from pathlib import Path
import sys
import time


def demand(ok, reason):
    if not ok:
        raise ValueError(reason)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--dependency-dir', type=Path)
    ap.add_argument('--degree', type=int, default=32)
    ap.add_argument('--bits', type=int, default=640)
    ap.add_argument('--source', type=Path)
    ap.add_argument('--output', type=Path)
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[1]
    source = args.source or root/'theta/source32.json'
    if args.dependency_dir:
        sys.path.insert(0, str(args.dependency_dir.resolve()))
    import flint
    from flint import arb, arb_series, ctx
    demand(flint.__version__ == '0.9.0', 'Pinned python-flint required.')
    demand(args.degree >= 22 and args.degree % 2 == 0 and args.bits >= 512,
           'Requested independent-check range or precision too small.')
    ctx.prec = args.bits
    ctx.cap = args.degree+1
    started = time.monotonic()
    # An analytic jet of xi(s), centered at s=1/2, independent of quadrature.
    s = arb_series([arb(1)/2, 1], prec=args.degree+1)
    xi = s*(s-1)/2*(-s*arb.pi().log()/2).exp()*(s/2).gamma()*s.zeta()
    mgf = xi/xi[0]
    variance = mgf[2]*2
    logmgf = mgf.log()
    fair_mgf = arb_series([arb(1)/factorial(j) if j % 2 == 0 else arb(0)
                           for j in range(args.degree+1)], prec=args.degree+1)
    logfair = fair_mgf.log()
    source_bytes = source.read_bytes()
    src = json.loads(source_bytes)
    demand(src['degree'] >= args.degree, 'Complete-source record too short.')
    scale = 1 << src['bits']

    def recorded(pair):
        lo, hi = pair
        demand(type(lo) is int and type(hi) is int and lo <= hi,
               'Malformed integer enclosure.')
        return arb(lo+hi, hi-lo)/(2*scale)

    def text(x):
        out = x.str(65, more=True)
        demand(arb(out).contains(x), 'Serialization lost directed enclosure.')
        return out

    demand(recorded(src['variance']).contains(variance),
           'Independent xi variance outside complete theta source.')
    rows = []
    for j in range(args.degree+1):
        if j % 2:
            demand(mgf[j].contains(0), 'xi functional symmetry failed.')
            demand(abs(mgf[j]) < arb(10)**(-100), 'Odd coefficient too wide.')
            continue
        r = j//2
        # Normalization fixes the order-zero coefficient exactly; a numerical
        # xi[0]/xi[0] ball would introduce artificial dependency width there.
        moment = arb(1) if j == 0 else mgf[j]*factorial(j)/variance**r
        demand(recorded(src['standardized_moments'][j]).contains(moment),
               'Independent xi moment outside complete theta enclosure at '+str(j))
        row = {'order': j, 'standardized_moment': text(moment)}
        if j:
            ratio = logmgf[j]/logfair[j]/variance**r
            demand(recorded(src['standardized_cumulant_ratios'][r-1]).contains(ratio),
                   'Independent logarithmic-jet cumulant ratio disagrees.')
            row['standardized_cumulant_ratio'] = text(ratio)
        rows.append(row)
    result = {'status': 'PASS', 'arithmetic': 'DIRECTED_ANALYTIC_SERIES',
              'python_flint': flint.__version__, 'precision_bits': args.bits,
              'degree': args.degree, 'variance': text(variance),
              'source_sha256': hashlib.sha256(source_bytes).hexdigest(),
              'independent_even_orders': rows,
              'finite_model_existence_certified_by_this_check': False,
              'elapsed_seconds': time.monotonic()-started}
    out = args.output or Path(__file__).with_name('XI_SOURCE_CHECK.json')
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': 'PASS', 'degree': args.degree,
                      'source_sha256': result['source_sha256'],
                      'variance': text(variance), 'output': str(out),
                      'elapsed_seconds': result['elapsed_seconds']}), flush=True)


if __name__ == '__main__':
    main()
