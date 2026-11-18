"""Prove simultaneous nonreal heat zeros and nearby derivative zeros from indexed close pairs."""

import argparse
import hashlib
import json
import lzma
from pathlib import Path

from flint import acb, arb, ctx
from spacing_census import outward, UNIT

SIDE = 20


def meromorphic_bounds(x, y):
    # x <= t <= y, all points s=2+it or 1/2+it used below.
    t = arb(x).union(arb(y))
    def elementary(s):
        return 1/s + 1/(s-1) - arb.pi().log()/2 + (s/2).digamma()/2
    right = elementary(acb(2, t))
    mid = elementary(acb(arb(1)/2, t))
    if not (right.real + 2 < 16 and abs(right.imag)+2 < 3 and
            mid.real > 13 and mid.real < 14 and abs(mid.imag) < 1):
        raise ArithmeticError("Universal digamma enclosures failed")


def gaussian_test(h, mass, v):
    D = 1 - 8*mass*v
    if not D > 0:
        return None
    var = 2*v/D
    for k in range(5, 25):
        radius2 = k*v/2
        coef = mass*(arb(1)/2+2*mass*radius2).exp()/(2*D.sqrt())
        constant = coef*(3*var**2 + h**2*var)
        quadratic = coef*(radius2 + 6*var + h**2)
        if (constant < 2*v-h**2 and quadratic < 1 and
                constant+quadratic*radius2 < radius2-2*v):
            return radius2.sqrt()
    return None


def derivative_test(h, mass, slope, outside):
    # Seek a small circle on which 2z dominates (z^2+h^2)G(z).
    # The scaled grid avoids assuming a lower bound for h.
    for numerator in range(1, 12):
        R = h*numerator/8
        if not R < outside:
            continue
        gp = mass/(1-R/outside)**2 + 1
        G = 15 + slope + R*gp
        new_radius = G*(R**2+h**2)/2
        if not new_radius < R:
            continue
        error = (gp*new_radius*h**2 + G*new_radius**2)/2
        # For an actual half-gap h0 <= h, the relative error needs to scale
        # with h0^2. From |z| <= G(|z|^2+h0^2)/2 and |z|<R obtain:
        scale = G/(2-G*R)
        if not 2-G*R > 0:
            continue
        relative_error = (gp*new_radius + G*scale**2*h**2)/2
        if relative_error < arb(13)/2:
            return R, 7*h**2 + error
    return None


def geometry(rows, j):
    a, b = rows[j:j+2]
    low = (a[0]+b[0])//2
    high = (a[1]+b[1]+1)//2
    below, above = rows[j-SIDE:j], rows[j+2:j+2+SIDE]
    distances = [(arb(low-y)/UNIT, arb(high-x)/UNIT) for x,y in below]
    distances += [(arb(x-high)/UNIT, arb(y-low)/UNIT) for x,y in above]
    if any(not d > 0 for d,_ in distances):
        return None
    far = min(distances[0][0], distances[-1][0])
    outside = min(distances[SIDE-1][0], distances[SIDE][0])
    # Each known critical-line zero contributes 1.5 / (2.25+d^2) to P.
    r = arb(3)/2
    local_P = sum(r/(r**2+hi**2) for _,hi in distances)
    h = arb(b[1]-a[0])/(2*UNIT)
    far_P = 16-local_P-2*r/(r**2+h**2)
    if not far_P > 0:
        raise ArithmeticError("Inconsistent Poisson upper bound")
    mass = sum(1/d**2 for d,_ in distances) + (1+4/far**2)*far_P
    # For our known real zeros d=t-gamma has known sign. The signed
    # difference of real logarithmic derivatives is r^2/[d(d^2+r^2)].
    signed = arb(0)
    def corr(d):
        return r**2/(d*(r**2+d**2))
    for n,(lo,hi) in enumerate(distances):
        term = corr(hi).union(corr(lo))
        signed += term if n < SIDE else -term
    slope = 3 + abs(signed) + arb(15)*far_P/(4*far)
    return arb(low).union(arb(high))/UNIT, h, mass, slope, outside


def census(checkpoint):
    ctx.prec = 128
    data = json.loads(checkpoint.read_text())
    if data.get("independent_guarded_count") != data["last_certified_index"]-1:
        raise ValueError("Need a counted checkpoint")
    meromorphic_bounds(data["published_height"]-1, data["verified_integer_height"]+3)
    v = arb(1)/5000
    thermal, derivative = [], []
    thresholds = [100, 500, 1000, 5000, 10000]
    narrow = {k: 0 for k in thresholds}
    previous_heat = previous_zeta = None
    root = hashlib.sha256()
    for block in range(data["complete_blocks"]):
        path = checkpoint.parent / "blocks" / f"{block:04d}.xz"
        meta = json.loads(path.with_suffix(".json").read_text())
        raw = lzma.decompress(path.read_bytes())
        digest = hashlib.sha256(raw).hexdigest()
        if digest != meta["stream_sha256"]:
            raise ValueError(f"Archive mismatch in block {block}")
        root.update(f"{block}\t{digest}\n".encode())
        rows = []
        for line in raw.splitlines():
            a,e,b,f = (int(word,16) for word in line.split())
            rows.append((outward(a,e,False), outward(b,f,True)))
        if len(rows) != 10001 or meta["first_index"] != data["published_zero_count"] + block*10000:
            raise ValueError(f"Index mismatch in block {block}")
        for j in range(SIDE, len(rows)-SIDE-1):
            if (rows[j+1][1]-rows[j][0])*100 > 9*UNIT:
                continue
            bounds = geometry(rows, j)
            if bounds is None:
                continue
            mid, h, mass, slope, outside = bounds
            idx = meta["first_index"] + j
            radius = gaussian_test(h, mass, v)
            if radius is not None:
                box = mid + arb(0,(radius+2*v*slope).upper())
                if previous_heat is None or previous_heat < box:
                    thermal.append(idx)
                    previous_heat = box
            proof = derivative_test(h, mass, slope, outside)
            if proof is not None:
                radius, bound = proof
                box = mid + arb(0,radius.upper())
                if previous_zeta is None or previous_zeta < box:
                    derivative.append(idx)
                    previous_zeta = box
                    for cut in thresholds:
                        if bound*1000000 < cut:
                            narrow[cut] += 1
    if root.hexdigest() != data["ordered_stream_digest"]:
        raise ArithmeticError("Census checkpoint digest mismatch")
    def summary(indices):
        return {"count": len(indices), "first_indices": indices[:8],
                "indices_sha256": hashlib.sha256("".join(f"{i}\n" for i in indices).encode()).hexdigest()}
    return {"checkpoint": checkpoint.name, "ordered_stream_digest": root.hexdigest(),
            "backward_heat_time": "1/5000", "disjoint_conjugate_pairs": summary(thermal),
            "disjoint_simple_zeta_derivative_zeros_right_of_line": summary(derivative),
            "derivative_zero_counts_by_strict_distance_in_millionths": narrow}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkpoint", type=Path)
    args = parser.parse_args()
    print(json.dumps(census(args.checkpoint), indent=2))
