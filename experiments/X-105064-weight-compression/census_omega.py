"""W2 census over the deposited Xi-derivative census (X-105061 zeros.json).

For random pairs p = (x, y) placed against the ACTUAL real-zero gap
structure of rungs 0..3 (heights [0, 500]), verify the weight-compression
bound omega(p) <= mu_p + 2 mu_p^2 (Lemma W2, L-105064) and report max omega.
Deposited per hostile-review MAJOR-W2 (the 80000-config census previously
had no shipped artifact; independent review reproduced max omega ~ 2.976).
"""
import json, random, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
Z = json.load(open(os.path.join(HERE, "..", "X-105061-xi-derivative-census", "zeros.json")))

def zeros_of(k):
    key = "k%d" % k
    row = Z[key] if isinstance(Z, dict) else Z[k]
    # rows may be dicts with bracket lo/hi or plain floats
    out = []
    for z in row:
        if isinstance(z, dict):
            lo = float(z.get("a", 0.0)); hi = float(z.get("b", lo))
            out.append(0.5 * (lo + hi))
        else:
            out.append(float(z))
    return sorted(out)

def omega(pair_x, pair_y, zs):
    # gaps overhung by (x, y): consecutive-zero intervals meeting (x-y, x+y)
    import bisect
    a, b = pair_x - pair_y, pair_x + pair_y
    i = bisect.bisect_left(zs, a) - 1
    tot, gmax = 0.0, 0.0
    while i < len(zs) - 1:
        lo, hi = zs[max(i, 0)], zs[max(i, 0) + 1]
        if lo >= b:
            break
        if hi > a and lo < b and max(i, 0) >= 0:
            g = hi - lo
            gmax = max(gmax, g)
            tot += min(1.0, g * g / (4 * pair_y * pair_y))
        i += 1
    mu = min(1.0, gmax / (2 * pair_y)) if pair_y > 0 else 1.0
    return tot, mu

def main(trials=80000, seed=105064):
    rng = random.Random(seed)
    worst = (0.0, None)
    viol = 0
    for t in range(trials):
        k = rng.randrange(4)
        zs = zeros_of(k)
        x = rng.uniform(zs[0] + 1, zs[-1] - 1)
        y = 10 ** rng.uniform(-3, 0) * 0.5   # y in (0.0005, 0.5]
        om, mu = omega(x, y, zs)
        if om > mu + 2 * mu * mu + 1e-12:
            viol += 1
        if om > worst[0]:
            worst = (om, (k, round(x, 3), round(y, 5), round(mu, 4)))
    print("trials:", trials, "| violations of W2:", viol, "| max omega:", round(worst[0], 4), "at", worst[1])
    assert viol == 0, "W2 violated"
    assert worst[0] < 3.0, "omega >= 3 impossible (Lemma W2)"
    print("CENSUS PASS")

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 80000)
