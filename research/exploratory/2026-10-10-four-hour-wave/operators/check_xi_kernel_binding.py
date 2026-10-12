#!/usr/bin/env python3
"""Exact algebra controls for the complete source binding, not an RH proof."""
import argparse
import hashlib
import json
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def zero(expr, message):
    require(sp.cancel(expr) == 0, message)


def certify():
    s, a, lam = sp.symbols('s a lambda')
    gamma, log2, logpi, psi, zp, p2 = sp.symbols('gamma log2 logpi psi zp P2')
    esd, ebd = sp.symbols('exp_minus_sd exp_minus_bd')
    b, c = sp.Rational(3, 2), sp.Rational(1, 2)
    cb = (1 - gamma - log2 - logpi) / 3
    denominator = s*s - b*b
    partial = (1/(2*b*(s+b)*(lam-b)) - 1/(2*b*(s-b)*(lam+b))
               + 1/(denominator*(lam+s)))
    zero(partial - 1/((lam*lam-b*b)*(lam+s)), 'complete gamma partial fractions')
    zero(1/(2*b*(s+b)) - 1/(2*b*(s-b)) + 1/denominator,
         'gamma coefficients cancel divergent digamma constant')
    gamma_transform = (-psi/2 - 1/(s+c) + (1+2*log2)*s/6
                       + sp.Rational(1, 4) - gamma/2 - log2/2) / denominator
    prime_split = (esd-ebd)/(b-s) + esd/(s+b) + ebd/(s+b)
    zero(prime_split - 2*(s*ebd-b*esd)/denominator,
         'literal two-sided prime splitting')
    arch_numerator = ((s/b)*(sp.Rational(3, 2)-(logpi+gamma)/2)
                      - 1/(s-c) - 1/(s+c) + logpi/2 - psi/2)
    source_arch = 1/(2*(s-c)) + cb/(s+b) + gamma_transform
    zero(source_arch - arch_numerator/denominator,
         'complete gamma/growing/Cb archimedean numerator')
    source_transform = source_arch + (-zp-(s/b)*p2)/denominator
    xi_log = 1/(s-c) + 1/(s+c) - logpi/2 + psi/2 + zp
    xi_at_b = sp.Rational(3, 2) - (logpi+gamma)/2 - p2
    target = ((s/b)*xi_at_b - xi_log)/denominator
    zero(source_transform - target, 'complete literal xi Laplace identity')
    pair = 2*s/((s*s-a*a)*(b*b-a*a))
    pair_target = ((s/b)*(2*b/(b*b-a*a)) - 2*s/(s*s-a*a))/denominator
    zero(pair-pair_target, 'complete opposite-zero partial fraction identity')
    gamma_zero = sp.Rational(1, 6) + log2/3
    zero(sp.Rational(1, 2)+cb+gamma_zero-p2/b-xi_at_b/b,
         'literal kernel at zero equals xi logarithmic derivative ratio')
    # Binding controls must see changes to constants and the prime normalization.
    require(sp.cancel(source_transform + sp.Rational(1, 3)/(s+b) - target) != 0,
            'altered Cb normalization is rejected')
    require(sp.cancel(source_transform + (-zp-(s/b)*p2)/denominator - target) != 0,
            'doubled prime normalization is rejected')
    return {
        'status': 'PASS_EXACT_XI_KERNEL_BINDING_ALGEBRA',
        'sympy_version': sp.__version__,
        'controls': ['complete gamma partial fractions', 'digamma constant cancellation',
                     'two-sided prime Laplace splitting', 'literal archimedean numerator',
                     'complete xi Laplace identity', 'complete opposite-zero partial fractions',
                     'literal W(0) identity', 'altered Cb rejection', 'doubled prime rejection'],
        'b_exact': str(b), 'c_exact': str(c),
        'proof_sha256': hashlib.sha256((HERE/'COMPLETE_XI_KERNEL_BINDING.md').read_bytes()).hexdigest(),
        'reviewed_literal_source_sha256': hashlib.sha256((HERE/'enclose_analytic_upper.py').read_bytes()).hexdigest(),
        'producer_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'limitations': ['analytic convergence and Laplace uniqueness require the independent proof',
                        'all-window sign is not established', 'RH remains open',
                        'no predecessor coefficient-trace criterion is authenticated'],
    }


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    result = certify()
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
