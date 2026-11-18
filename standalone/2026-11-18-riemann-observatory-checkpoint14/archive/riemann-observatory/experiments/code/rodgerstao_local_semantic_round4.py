"""Exact elementary checks supporting the scoped PAPER-S004 local review.

No zeta zeros are numerically approximated. The classical-location lower bound
uses source Eq (44) analytically; the harmonic proxy here checks only indexing.
"""
from fractions import Fraction
from pathlib import Path
import json


def main():
    endpoint = []
    corrected = []
    for J in (4, 8, 16, 32, 64):
        I = range(J, 2 * J + 1)
        S = sum((Fraction(1, (k-J)**3) for k in I if 0 < abs(k-J) < Fraction(J, 2)), Fraction())
        assert S >= 1
        endpoint.append({"J": J, "S": str(S), "S_times_max_distance_squared": str(S*J*J)})
        total = Fraction()
        for j in I:
            Sj = sum((Fraction(1, (k-j)**3) for k in I if 0 < abs(k-j) < Fraction(j, 2)), Fraction())
            d = min(j-J, 2*J-j)
            assert abs(Sj) <= Fraction(2, (1+d)**2)
            total += abs(Sj)
        corrected.append({"J": J, "sum_absolute_inner_sums": str(total)})
    harmonic = []
    for n in (2, 4, 8, 16, 32, 64):
        # j=n..2n inclusive, r=1..n: no diagonal and all k<=3n.
        H = sum((Fraction(1, r) for r in range(1, n+1)), Fraction())
        direct = sum((Fraction(1, k-j) for j in range(n,2*n+1) for k in range(j+1,j+n+1)), Fraction())
        assert direct == (n+1)*H
        harmonic.append({"n":n,"harmonic_sum":str(H),"restricted_unit_spacing_sum":str(direct)})
    out = {"scope":"exact finite auxiliary indexing checks, not zeta computation or proof certification", "endpoint_max_failure": endpoint, "regularized_min_bound_checks": corrected, "harmonic_index_checks":harmonic, "all_assertions_passed":True}
    root=Path(__file__).resolve().parents[2]
    target=root/'experiments/results/rodgerstao_local_semantic_round4.json'
    target.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({"all_assertions_passed":True,"output":str(target)}))


if __name__ == '__main__':
    main()
