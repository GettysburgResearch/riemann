"""O-108523 checker — the torsion multiplicity law for disc_z M_m.

For a torsion point with alpha of order M (per Galois-conjugate root;
class counts n_c(m) = #{0 <= j <= m: 2j - m == c mod M}), the
multiplicity of the point's minimal polynomial in the exact
factorization of disc_z M_m(a, 1) obeys, at ODD m:

    mult = sum over interior class-pairs {c, -c}  mu_c (mu_c - 1)
         + 2 * floor(mu_{M/2} / 2)^2              (boundary z = -2),
    mu_c = n_c - 1,

verified 40/40 against every odd-m cell of the committed exact
factorizations (m = 5..17, ten torsion points). At EVEN m the same
formula overshoots systematically (deviations printed); the correct
boundary/trivial-factor bookkeeping at z = +-2 is the deposited open
piece. rh_established = false.
"""
import json
from collections import Counter

PTS = {
    'a': 4, 'a - 1': 6, 'a + 1': 3, 'a**2 - 2': 8, 'a**2 - 3': 12,
    'a**2 - a - 1': 10, 'a**2 + a - 1': 5,
    'a**3 - a**2 - 2*a + 1': 14, 'a**3 + a**2 - 2*a - 1': 7,
    'a**4 - 4*a**2 + 2': 16,
}


def predict(M, m):
    n = Counter(((2 * j - m) % M) for j in range(m + 1))
    tot = 0
    done = set()
    for c in list(n):
        if c in done:
            continue
        done.add(c)
        done.add((-c) % M)
        mu = n[c] - 1
        if mu < 2:
            continue
        if c == 0 or (M % 2 == 0 and c == M // 2):
            tot += 2 * (mu // 2) ** 2
        else:
            tot += mu * (mu - 1)
    return tot


def main():
    rows = {}
    for f in ['matrix/disc_slice_factor_lcs.json',
              'matrix/disc_slice_m16_m17.json']:
        d = json.load(open(f))
        for m, fl in d.items():
            rows[int(m)] = fl
    out = {"odd": [], "even": [], "rh_established": False}
    for parity in (1, 0):
        ok = bad = 0
        for m in sorted(rows):
            if m % 2 != parity:
                continue
            for (fs, mult, deg, lc) in rows[m]:
                key = fs.replace(' ', '')
                for t, M in PTS.items():
                    if key == t.replace(' ', ''):
                        p = predict(M, m)
                        rec = {"m": m, "factor": t, "M": M,
                               "data": mult, "predicted": p,
                               "ok": p == mult}
                        (out["odd"] if parity else out["even"]).append(rec)
                        if p == mult:
                            ok += 1
                        else:
                            bad += 1
        print(f"{'odd' if parity else 'even'} m: {ok} ok, {bad} off")
    # m = 18, 19 rows from the memory-lean sieve (multiplicities keyed
    # directly by the psi index N = the per-root cyclotomic order M)
    import os
    out["sieve_rows"] = []
    for m in (18, 19):
        f = f'matrix/m{m}_sieve.json'
        if not os.path.exists(f):
            continue
        mults = {int(k): v for k, v in
                 json.load(open(f))["torsion_multiplicities"].items()}
        ok = bad = 0
        for N in sorted(mults):
            p = predict(N, m)
            rec = {"m": m, "M": N, "data": mults[N], "predicted": p,
                   "ok": p == mults[N]}
            out["sieve_rows"].append(rec)
            if p == mults[N]:
                ok += 1
            else:
                bad += 1
        print(f"m = {m} (sieve, {'odd' if m % 2 else 'even'}): "
              f"{ok} ok, {bad} off; details "
              f"{[(r['M'], r['data'], r['predicted']) for r in out['sieve_rows'] if r['m'] == m]}")
    json.dump(out, open('matrix/mult_law_check.json', 'w'), indent=1)


if __name__ == "__main__":
    main()
