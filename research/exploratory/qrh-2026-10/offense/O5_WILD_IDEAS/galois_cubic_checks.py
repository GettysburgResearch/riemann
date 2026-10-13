"""galois_cubic_checks.py -- EMPIRICAL / exact-integer sanity checks for O5 (finite; proves nothing).

(1) Galois descent of the sextic symbol (exact integer arithmetic in Z[omega], via the read-only
    import of moments/eisenstein.py): for split p = pi*conj(pi) and any u,
        (u/pi)_6 (u/conj pi)_6 = (u/pi)_6 conj((conj u/pi)_6),
    so the symbol at a rational column m is principal on rational rows; and A_{conj u} = conj(A_u)
    (checked with the C kernel of moments/, double precision).
(2) Least prime p = 1 (mod 3) with m a cubic non-residue mod p, for non-cubes m <= MMAX (exact).
Run: python3 -I galois_cubic_checks.py   (about 1-2 minutes, single thread)
"""
import math, os, sys, json, random
HERE = os.path.dirname(os.path.abspath(__file__))
MOM = os.path.normpath(os.path.join(HERE, "..", "..", "moments"))
sys.path.insert(0, MOM)
import numpy as np
import eisenstein as E
import common as C

res = {}
# ---------- (1a) exact symbol identity
primes = E.prime_ideals(4000)
split = [P for P in primes if P.kind == "split"]
byp = {}
for P in split:
    byp.setdefault(P.p, []).append(P)
pairs = [v for v in byp.values() if len(v) == 2][:40]
rng = random.Random(7)
ok = bad = rat_ok = 0
for (P1, P2) in pairs:
    for _ in range(25):
        u = (rng.randint(-60, 60), rng.randint(-60, 60))
        if u == (0, 0):
            continue
        k1 = E.sextic_symbol_exact(u, P1.gen)
        k2 = E.sextic_symbol_exact(u, P2.gen)
        kb = E.sextic_symbol_exact(E.conj(u), P1.gen)
        if E.ZERO in (k1, k2, kb):
            continue
        if (k1 + k2) % 6 == (k1 - kb) % 6:
            ok += 1
        else:
            bad += 1
    for a in range(2, 40):            # rational rows
        k1 = E.sextic_symbol_exact((a, 0), P1.gen)
        k2 = E.sextic_symbol_exact((a, 0), P2.gen)
        if E.ZERO in (k1, k2):
            continue
        assert (k1 + k2) % 6 == 0
        rat_ok += 1
res["galois_symbol_identity"] = {"pass": ok, "fail": bad, "rational_rows_trivial": rat_ok}
print("symbol identity pass/fail", ok, bad, "rational-row triviality checks", rat_ok)
assert bad == 0

# ---------- (1b) A_{conj u} = conj(A_u) with the C kernel
lib = C.load_kernel()
D = 1000.0
prs = E.prime_ideals(int(2 * D) + 10)
pd = C.PrimeData(prs)
ns, facs, norms, w = C.family(prs, D)
tree = C.Tree(facs, w)
H = 1500
bm = int(2 * math.sqrt(H / 3)) + 2
segs, (a, b, N) = C.lattice_segments(H, bmin=-bm)
Au = C.eval_rows(lib, pd, tree, segs, workers=1)
idx = {(int(x), int(y)): i for i, (x, y) in enumerate(zip(a, b))}
dev = 0.0
for i, (x, y) in enumerate(zip(a, b)):
    cx, cy = E.conj((int(x), int(y)))
    j = idx.get((cx, cy))
    if j is not None:
        dev = max(dev, abs(Au[j] - np.conj(Au[i])))
ratrows = [i for i, y in enumerate(b) if y == 0]
imag_rat = max(abs(Au[i].imag) for i in ratrows)
scale = float(np.sqrt(np.mean(np.abs(Au) ** 2)))
res["conj_rows"] = {"D": D, "H": H, "rows": int(len(a)), "max|A_conj(u)-conj(A_u)|": dev,
                    "max|Im A_u| on rational rows": imag_rat, "rms|A_u|": scale}
print("max |A_conj(u) - conj A_u| =", dev, " max |Im A_u| (rational u) =", imag_rat, " rms =", scale)

# ---------- (2) least prime p = 1 mod 3, p !| m, with m a cubic non-residue mod p
MMAX = 200000
ps = [p for p in range(7, 20000) if all(p % q for q in range(2, int(p ** 0.5) + 1)) and p % 3 == 1]
def is_cube(m):
    r = round(m ** (1 / 3))
    return any((r + d) ** 3 == m for d in (-1, 0, 1))
worst = []
mx_ratio2 = 0.0
arg = None
for m in range(2, MMAX + 1):
    if is_cube(m):
        continue
    for p in ps:
        if m % p and pow(m, (p - 1) // 3, p) != 1:
            r2 = p / math.log(m) ** 2
            if r2 > mx_ratio2:
                mx_ratio2, arg = r2, (m, p)
            if not worst or p > worst[-1][1]:
                worst.append((m, p))
            break
    else:
        raise RuntimeError(m)
res["least_cubic_nonresidue_prime"] = {"MMAX": MMAX, "record_holders(m,p)": worst,
                                       "max p/(log m)^2": mx_ratio2, "argmax": arg}
print("records (m, p):", worst)
print("max p/(log m)^2 =", mx_ratio2, "at", arg)
json.dump(res, open(os.path.join(HERE, "galois_cubic_checks.json"), "w"), indent=1, default=str)
