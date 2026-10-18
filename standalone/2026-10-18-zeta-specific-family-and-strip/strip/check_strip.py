#!/usr/bin/env python3
"""Source-bound finite strip example and exact independent graph identities.

No numerical assertion proves S1, S3, or S4. Those are paper theorems in PROOF.md.
The primitive source is reconstructed fresh unless --source-only is requested
(which only reconstructs it and stops). This is the inherited directed backend,
not an independent transcendental implementation.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import product
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
DEFAULT_SOURCE = (ROOT.parent.parent /
                  "2026-10-18-theta20-and-native-cancellation" / "theta")

EXPECTED_BLOBS = {
    "pr886_primitive.py": "c32015f110d10186538ffabcb4689ba5bbc060d0",
    "theta_source.py": "fc51d49fe2bdbbde3fcb3928f1d82fd8baffbf53",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def authenticate(source_directory):
    result = {}
    for name, expected in EXPECTED_BLOBS.items():
        data = (source_directory / name).read_bytes()
        actual = sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        require(actual == expected, "inherited source identity: " + name)
        result[name] = {"bytes": len(data), "git_blob": actual,
                        "sha256": sha256(data).hexdigest()}
    return result


def exact_graph_check():
    """Five-spin fixture, all 32 configurations, rational Gibbs edge factors.

    Graph 0--1--2 with branches 1--3,3--4. Its automorphism swaps 0 and 2.
    Fields are opposite on that pair; other fields zero. The three remaining
    vertices include a zero-weight vertex 4 with zero field.
    """
    edges = [(0, 1, F(1, 5)), (1, 2, F(1, 5)),
             (1, 3, F(1, 7)), (3, 4, F(1, 9))]
    weights = [F(2, 5), F(1, 3), F(2, 5), F(1, 7), F(0)]
    field_tanh = [F(1, 19), F(0), F(-1, 19), F(0), F(0)]
    tau = [2, 1, 0, 3, 4]
    laws = []
    total0 = F(0)
    totalh = F(0)
    raw0 = [F(0) for _ in range(9)]
    rawh = [F(0) for _ in range(9)]
    correlations = {mask: F(0) for mask in range(1 << 5)}
    for spin in product((-1, 1), repeat=5):
        mass0 = F(1, 1 << 5)
        for i, j, q in edges:
            mass0 *= 1 + q * spin[i] * spin[j]
        field_factor = F(1)
        for r, s in zip(field_tanh, spin):
            field_factor *= 1 + r * s
        massh = mass0 * field_factor
        y = sum((w * s for w, s in zip(weights, spin)), F(0))
        total0 += mass0
        totalh += massh
        for k in range(9):
            raw0[k] += mass0 * y**k
            rawh[k] += massh * y**k
        for mask in correlations:
            sign = 1
            for i in range(5):
                if mask >> i & 1:
                    sign *= spin[i]
            correlations[mask] += mass0 * sign
        transformed = tuple(-spin[tau[i]] for i in range(5))
        laws.append((spin, massh, y, transformed))
    require(total0 == 1, "tree zero-field normalization")
    require(totalh > 0, "biased normalization")
    byspin = {spin: (m, y) for spin, m, y, _ in laws}
    for spin, m, y, transformed in laws:
        require(byspin[transformed] == (m, -y), "involution symmetry")
    require(all(rawh[k] == 0 for k in (1, 3, 5, 7)), "all odd fixture moments")
    require(all(value >= 0 for value in correlations.values()),
            "nonnegative full spin correlations")

    # Independent high-temperature enumeration of every edge subset.
    graph_sums = {mask: F(0) for mask in correlations}
    for flags in product((0, 1), repeat=len(edges)):
        boundary = 0
        term = F(1)
        for flag, (i, j, q) in zip(flags, edges):
            if flag:
                boundary ^= (1 << i) | (1 << j)
                term *= q
        graph_sums[boundary] += term
    for mask in correlations:
        require(correlations[mask] == graph_sums[mask] / graph_sums[0],
                "spin enumeration versus graph boundary expansion")

    # Derive all path products independently by DFS from each vertex.
    adjacency = {i: [] for i in range(5)}
    for i, j, q in edges:
        adjacency[i].append((j, q))
        adjacency[j].append((i, q))
    var_formula = sum((w*w for w in weights), F(0))
    for source in range(5):
        todo = [(source, -1, F(1))]
        while todo:
            i, parent, corr = todo.pop()
            if i > source:
                var_formula += 2 * weights[source] * weights[i] * corr
            for j, q in adjacency[i]:
                if j != parent:
                    todo.append((j, i, corr*q))
    require(var_formula == raw0[2], "tree reference variance formula")
    return {"status": "EXACT_RATIONAL_PASS", "spins_enumerated": 32,
            "edge_subsets_enumerated": 16,
            "all_spin_correlations": 32,
            "reference_variance": str(var_formula),
            "biased_variance": str(rawh[2] / totalh),
            "zero_weight_vertex": 4,
            "odd_orders_checked": [1, 3, 5, 7]}


def finite_example(source):
    import pr886_primitive as b
    I, SCALE = b.I, b.SCALE
    from math import comb

    v = I(*source["variance"])
    m4 = I(*source["standardized_moments"][4])
    k = 3 - m4
    q, r = F(1, 10000), F(1, 32)
    a_rat = (1-q)/(1+q) * (1+r*r)/(1-r*r)
    a = I.coerce(a_rat)
    c, d = 2-a, I.rat(1, 8)
    discriminant = (c+d)*k-c*d
    require(discriminant.lo > 0, "positive exact theta discriminant")
    t = (d + discriminant.sqrt()) / (c+d)
    require(t.lo > 0 and t.hi < SCALE, "fractional variance strictly between 0 and 1")
    w = ((a+1)*v*t).sqrt()
    u = (v*(1-t)/16).sqrt()
    require(a.lo > SCALE and a.hi < 2*SCALE, "genuinely nonreal dimer")

    # h = atanh(r) < r/(1-r^2), from its positive series.
    h_upper = I.coerce(r/(1-r*r))
    require((w/6 - h_upper).lo > 0, "physical field/weight band strictly below 1/3")
    reference_var = w*w*(1+q)/2 + 16*u*u
    require(reference_var.hi < I.rat(1, 20).lo, "reference variance below 1/20")

    def cosh(x):
        return (b.exp(x)+b.exp(-x))/2

    require(cosh(w*F(3,10)).hi < a.lo, "nonreal height above 3/10")
    require((1+(w*F(31,100))**2/2).lo > a.hi,
            "nonreal height below 31/100")

    # Direct moment assembly via polynomial product, independent of cumulants.
    # First recover the dimer probabilities from its four Gibbs configurations.
    # Divide edge/field factors by their full sum; all masses are rational.
    masses = {}
    for s, z in product((-1,1), repeat=2):
        raw = (1+q*s*z)*(1+r*s)*(1-r*z)
        level = (s+z)//2
        masses[level] = masses.get(level, F(0)) + raw
    total = sum(masses.values(), F(0))
    masses = {level: value/total for level, value in masses.items()}
    require(masses[0] == a_rat/(a_rat+1), "dimer zero mass from exact Gibbs law")
    require(masses[1] == masses[-1] == 1/(2*(a_rat+1)), "dimer side masses")

    # The exact identities in PROOF.md establish equality to the nonrational
    # theta moments. Here the independently multiplied raw-moment boxes check
    # those identities against the directed construction; overlap alone is not
    # the existence/equality proof.
    moments = [I.coerce(1), I.coerce(0), w*w/(a+1),
               I.coerce(0), w**4/(a+1)]
    for _ in range(16):
        block = [I.coerce(1), I.coerce(0), u*u, I.coerce(0), u**4]
        moments = [sum((comb(n,j)*moments[j]*block[n-j]
                        for j in range(n+1)), I.coerce(0)) for n in range(5)]
    target2, target4 = v, m4*v*v
    for n, target in ((2,target2),(4,target4)):
        require(max(moments[n].lo,target.lo) <= min(moments[n].hi,target.hi),
                "direct raw moment diagnostic overlap")

    data = {"status": "DIRECTED_FINITE_EXAMPLE_PASS",
            "arithmetic": "320-bit outward integer intervals; inherited backend",
            "bits": b.BITS,
            "physical_zero_band": "1/3",
            "nonreal_zero_height_strict_interval": ["3/10","31/100"],
            "observed_spins": 18, "positive_edges": 1,
            "matched_moments": [2,4], "higher_moments_claimed": False,
            "q": str(q), "r": str(r), "a": str(a_rat),
            "source_variance": v.record(),
            "negative_standardized_fourth_cumulant": k.record(),
            "discriminant": discriminant.record(), "variance_fraction": t.record(),
            "dimer_total_amplitude": w.record(), "fair_spin_weight": u.record(),
            "field_upper_bound": h_upper.record(),
            "reference_variance": reference_var.record(),
            "direct_raw_moments": [x.record() for x in moments],
            "exact_dimer_masses": {str(i):str(m) for i,m in masses.items()},
            "acceptance": {
                "strict_discriminant": True, "positive_weights": True,
                "a_strictly_greater_than_one": True,
                "physical_field_band": True,
                "reference_variance_less_than_1_over_20": True,
                "nonreal_height_in_claimed_interval": True,
                "direct_four_configuration_gibbs_identity": True,
                "direct_moment_overlap_is_diagnostic_only": True}}
    return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-only", action="store_true")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE,
                        help="Exact inherited theta directory; defaults to the sibling repo packet")
    args = parser.parse_args()
    source_directory = args.source.resolve()
    identities = authenticate(source_directory)
    sys.path.insert(0, str(source_directory))
    import theta_source
    source = theta_source.reconstruct()
    serialized = json.dumps(source,sort_keys=True,separators=(",",":"))+"\n"
    (ROOT / "theta_source_replay.json").write_text(serialized)
    if args.source_only:
        print("COMPLETE_THETA_SOURCE", sha256(serialized.encode()).hexdigest())
        return
    result = {"status": "PASS", "source_commit":
              "c93ca65a510b6acaf167f929b9bf7e67d742b05a",
              "source_files": identities,
              "source_replay_sha256": sha256(serialized.encode()).hexdigest(),
              "finite_example": finite_example(source),
              "independent_graph_check": exact_graph_check(),
              "not_proved_by_this_run": ["RH", "improved zeta strip",
                    "cofinal moment matching", "independent primitive backend"]}
    body = json.dumps(result,indent=2,sort_keys=True)+"\n"
    (ROOT / "certificate.json").write_text(body)
    print("STRIP_FINITE_AND_GRAPH_PASS",sha256(body.encode()).hexdigest())
    e=result["finite_example"];scale=2**e["bits"]
    for key in ("source_variance","negative_standardized_fourth_cumulant",
                "variance_fraction","dimer_total_amplitude","fair_spin_weight",
                "reference_variance"):
        lo,hi=e[key]
        print(key, (lo+hi)/(2*scale), "width", (hi-lo)/scale)


if __name__ == "__main__":
    main()
