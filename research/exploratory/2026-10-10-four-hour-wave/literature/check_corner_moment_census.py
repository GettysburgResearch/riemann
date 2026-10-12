"""Exact joint-corner census refinement using authenticated native primitives."""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import hashlib
import json

HERE = Path(__file__).resolve().parent
WAVE = HERE.parent
OUTER = WAVE / 'xi' / 'outer-ray'


def need(ok, message):
    if not ok:
        raise ArithmeticError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_power(real, imag, degree):
    out = (Q(1), Q(0))
    for _ in range(degree):
        out = (out[0] * real - out[1] * imag,
               out[0] * imag + out[1] * real)
    return out


def projection(k, real, imag):
    return complex_power(real, -imag, 2*k)[0] / (real*real + imag*imag)**k


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--eighth-receipt', type=Path,
                        default=OUTER / 'eighth_moment_census.json')
    args = parser.parse_args()
    receipt = json.loads(args.eighth_receipt.read_text())
    need(receipt['status'] == 'PASS_DIRECTED_COUNT_FREE_EIGHTH_MOMENT_CENSUS',
         'successful full source residual receipt')
    need(receipt['normalization'] == 'Xi(z)=xi(1/2+i*z)' and
         receipt['refined_endpoint_signs_replayed'] == 556 and
         receipt['remaining_original_sign_intervals_imported'] == 7771 and
         receipt['selected_interval_inverse_eighth_terms_replayed'] == 8049 and
         receipt['native_logarithmic_jet_degree_replayed'] == 8,
         'literal native primitive and import scope')
    for filename, expected in receipt['source_sha256'].items():
        need(digest(WAVE / filename) == expected, 'direct source hash ' + filename)
    need(digest(OUTER / 'check_eighth_moment_census.py') ==
         'c2b21b3e5c913904ecfa0c7add770523853fddf5d264d602155df53c744ff9a1',
         'independently reviewed literal native checker')
    need(digest(OUTER / 'EIGHTH_MOMENT_CENSUS_RECOVERY.md') ==
         'd5414e8f8de70b00f1b4dc4e66a091174a64552a0684b270d4c8fb3a539043dc',
         'frozen analytic residual source')
    need(Q(receipt['strict_native_xi_zero_seed_lower']) > Q(99, 200),
         'actual native positive theta seed')
    lower, upper = (Q(x) for x in receipt['residual_inverse_eighth_moment_interval'])
    need(0 < lower <= upper, 'full interval residual upper endpoint')

    k, R, A, B = 4, Q(27, 5), Q(1, 2), Q(11, 2)
    need(R*R + A*A < B*B, 'complete source initial real-part exclusion')
    need((2*k + 1)*A/R == Q(5, 6) < Q(3, 2),
         'strong monotonicity angle protected by atan x<x and pi>3')

    def ratio(height):
        H = Q(height)
        c = projection(k, H, A)
        need(c > 0, 'positive exact corner projection')
        return upper * (H*H + A*A)**k / c

    lo, hi = 6, 8192
    need(ratio(lo) < 1 and ratio(hi) >= 1, 'exact search bracket')
    while lo + 1 < hi:
        middle = (lo + hi)//2
        if ratio(middle) < 1:
            lo = middle
        else:
            hi = middle
    need(lo == 3296 and hi == 3297, 'largest integer admitted by this predicate')
    accepted, following = ratio(lo), ratio(hi)
    need(accepted < 1 <= following, 'exact accepted and failed next guards')

    original = json.loads((OUTER / 'native_candidates.json').read_text())
    refined = json.loads((OUTER / 'eighth_prefix_candidates.json').read_text())
    old, new = original['interval_numerators'], refined['interval_numerators']
    need(len(old) == 8049 and len(new) == 278,
         'complete literal selected-root interval inventory')
    below = 0
    previous = Q(0)
    for index, bracket in enumerate(old):
        denominator = 2**24
        if index < 278:
            bracket, denominator = new[index], 2**80
        a, b = bracket
        need(type(a) is int and type(b) is int, 'exact endpoint numerators')
        qlo, qhi = Q(a, denominator), Q(b, denominator)
        need(previous < qlo < qhi, 'ordered disjoint full selected intervals')
        need(qhi < lo or qlo > lo, 'no selected interval meets accepted boundary')
        previous = qhi
        below += qhi < lo
    need(below == 2761, 'derived complete simple real census size')

    # Original doubled-angle positivity alone does not imply x monotonicity.
    counter_R, counter_A = Q(3, 2), Q(1)
    need(projection(1, counter_R, counter_A) > 0 and
         2*counter_A/counter_R < Q(3, 2), 'countercontrol original acute guard')
    need(complex_power(counter_R, -counter_A, 3)[0] < 0,
         'countercontrol real derivative increases without stronger angle')

    proof = HERE / 'CORNER_MOMENT_CENSUS_REFINEMENT.md'
    record = dict(
        status='PASS_EXACT_JOINT_CORNER_COUNT_FREE_CENSUS',
        arithmetic='exact Fraction and integer source/geometry predicates',
        moment_order=k, R=str(R), A=str(A),
        accepted_height=lo, next_height_fails_this_predicate=hi,
        accepted_ratio_exact=str(accepted), strict_margin_exact=str(1-accepted),
        following_ratio_exact=str(following),
        accepted_projection_exact=str(projection(k, Q(lo), A)),
        complete_simple_positive_real_zero_count=below,
        maximum_derivative_order=2*lo-3,
        all_lambda_positive=True, all_y_nonnegative=True,
        horizontal_range='abs(T)<3296-(r+2)/2',
        imported_native_refined_signs=556, imported_older_sign_intervals=7771,
        selected_full_root_interval_terms=8049,
        new_native_endpoint_or_jet_evaluations=0,
        historical_count_or_uniqueness_contract_used=False,
        complete_analytic_source_authenticated_by_checker=False,
        rh_proved=False,
        eighth_receipt_sha256=digest(args.eighth_receipt),
        checker_sha256=digest(Path(__file__).resolve()),
        proof_sha256=digest(proof),
        imported_direct_source_sha256=receipt['source_sha256'])
    print(json.dumps(record, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
