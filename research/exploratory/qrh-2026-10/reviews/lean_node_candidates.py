#!/usr/bin/env python3
"""Keyword candidate search: paper node -> Lean declarations in the Nonvanishing closure.

Status: EXPLORATORY tooling. A hit is a *candidate* only (name or keyword match); it is not a
checked statement correspondence. Spot checks are recorded by hand in SEP30_LEAN_CORRESPONDENCE.md.

Usage:
  python3 -I lean_node_candidates.py <decls.tsv from lean_closure_map.py> <out.json>

For each paper node the script lists the closure modules whose declaration *names* match the
node's name patterns, ranked by number of matching declarations (top 6), plus up to 8 example
declaration names. Patterns were chosen from the paper's titles and notation before looking at
hit counts; they are deliberately broad.
"""
import csv
import json
import re
import sys
from collections import Counter, defaultdict

NODES = {
    "Prop 2.1 continuation": r"common_signal|CommonProbe|PrimitiveContract|continuationMargin|nonzero_of_probe_bounds",
    "Lem 4.1 ray characters": r"RayCharacter|rayCharacter|fixedNumerator|FixedNumerator|RayFour",
    "Lem 4.2 prime Gauss identities": r"PrimeGauss|primeGauss|prime_gauss|gaussSum_prime|cubicGauss|CubicGauss",
    "Lem 4.3 quadratic four-term": r"fourTerm|FourTerm|four_term|QuadraticNormalization|quadraticGauss",
    "Lem 4.4 sextic reciprocity / Gauss phase": r"[Rr]eciprocity|KubotaCharacter|kubota|sexticPhase|SexticNormalization|gaussPhase|GaussPhase",
    "Lem 4.5 smooth calculus": r"LogProfiles|logProfile|smoothCalculus|SmoothCalculus|UniformKernelBounds",
    "Lem 4.6 Gaussian annular decomposition": r"annularDecomposition|AnnularDecomposition|gaussianAnnular|GaussianAnnular|annular_decomp",
    "Lem 4.7 finite seminorms": r"[Ss]eminorm",
    "Lem 4.8 Hecke strip growth": r"HeckeStrip|strip_growth|stripGrowth|StripActual|Hecke\.Strip|convexity",
    "Lem 4.9 logarithmic control": r"LogarithmicControl|borelCaratheodory|borel_caratheodory|BorelCarath|logarithmic_control",
    "Lem 4.10 deleted Euler factors": r"FiniteDeletion|DeletionBounds|deletion_bound|excludePrimes",
    "Prop 5.1 completed cubic reflection": r"completedReflection|CompletedReflection|cubic_reflection|CubicReflection|reflection_identity",
    "Lem 5.2 fixed ray sectors": r"[Ss]ector",
    "Lem 5.3 common annular kernel": r"annularKernel|AnnularKernel|commonProfile|CommonProfile",
    "Lem 5.4 lattice kernel tails": r"lattice_tail|latticeTail|LatticeTail|LatticeEnvelopes",
    "Lem 5.5 quadratic reduction": r"quadraticReduction|QuadraticReduction|quadratic_reduction",
    "Def 5.6/Lem 5.7 unmarked reflected block": r"[Uu]nmarkedReflected|unmarked_block|UnmarkedBlock|reflectedBlock|ReflectedBlock",
    "Sec 7.1 probe Poisson identity": r"probe_poisson|ProbePoisson|probePoisson|exact_poisson|ExactPoisson",
    "Lem 7.1 complete local identity": r"LocalEulerIdentities|localIdentity|local_identity|completeLocal|CompleteLocal",
    "Lem 8.1 buffered zero-free bins": r"[Bb]uffered",
    "Lem 8.2 pointwise dyadic estimates": r"DyadicPointwise|dyadic_pointwise|pointwise_dyadic|DyadicEstimates",
    "Prop 8.3 two saturated witnesses": r"[Ss]aturat|twoWitness|two_witness|DetectorWitness",
    "Def 10.1-Lem 10.6 high representation": r"retained|Retained|outerRow|OuterRow|principalSignal|PrincipalSignal|exactHigh|ExactHigh",
    "Lem 11.1 late height choice": r"height_choice|heightChoice|chosen_data_height|lateHeight",
    "Prop 11.3 quadratic transfer": r"dirichlet_seven_eighths_of_hecke|LFunction_eq_dirichlet_product|baseChange",
    "Lem 13.1 ray prime normalizer": r"RayPrimeNormalizer|rayPrimeNormalizer|RayAsymptotic|normalizer",
    "Lem 13.2 prime-power Fourier sums": r"PrimePowerGauss|primePowerGauss|prime_power_fourier|primePowerFourier",
    "Lem 13.3/13.4 correlations": r"[Cc]orrelation|commonSupport|CommonSupport",
    "Cor 14.1 marked completed reflection": r"wholeIndex|WholeIndex|markedReflection|MarkedReflection|whole_index",
    "Lem 14.2 quadratic-cubic norm": r"quadraticCubic|QuadraticCubic|HeathBrown|heathBrown|heath_brown|cubic_large_sieve|cubicLargeSieve",
    "Lem 14.3 reflected energy": r"reflectedEnergy|ReflectedEnergy|reflected_energy",
    "Lem 15.1 compensated row norm": r"compensatedRow|CompensatedRow|compensated_row|completedRowNorm",
    "Prop 15.2 additive Gram bound": r"[Gg]ram\b|[Gg]ram_|Gram[A-Z]",
    "Prop 15.3 compensated low estimate": r"probe_low|lowEstimate|low_estimate|LowEstimate|compensatedLow",
    "Prop 16.1 conductor allocation": r"conductorAllocation|ConductorAllocation|dynamicLocal|DynamicLocal|localError",
    "Lem 16.2 absolute local tuple bounds": r"tupleBound|TupleBound|tuple_bound|TupleWeights|absoluteLocal",
    "Lem 17.1 marked inverse moment": r"inverse_marked|inverseMarked|InverseMarked|markedInverse|MarkedInverse",
    "Lem 17.2 canonical marked estimate": r"canonicalMarked|CanonicalMarked|canonical_marked",
    "Lem 17.3/Cor 17.4 seminorm propagation": r"[Pp]ropagation|propagate",
    "Lem 17.5 masked primitive Poisson": r"maskedPoisson|MaskedPoisson|masked_poisson|maskedPrimitive|MaskedPrimitive",
    "Lem 17.6 sixth-power amplification": r"[Aa]mplification|sixthPower|SixthPower|sixth_power",
    "Lem 18.1 fourth moment (plain)": r"plain_marked|plain_unmarked|PlainMarked|PlainUnmarked|fourthMoment|FourthMoment",
    "Lem 18.2 common coefficient": r"commonCoefficient|CommonCoefficient|completeExtraction|CompleteExtraction",
    "Lem 18.3 masked rectangle cancellation": r"[Rr]ectangle",
    "Lem 19.1 prime bound in a bin": r"PrimeBin|primeBin|prime_bin",
    "Prop 19.2 row counts": r"RowCount|rowCount|row_count",
    "Lem 20.1 high exponent for one bin": r"highExponent|HighExponent|high_exponent|bin_exponent",
    "Lem 20.2 endpoint certificate": r"endpoint_identity|balanced_endpoint|balancedExponent|Endpoint\.",
    "Prop 20.3 order of choices": r"FinalAssembly|HighData|exists_high_data|central_budget",
}


def main(argv):
    decls, out = argv[1], argv[2]
    rows = list(csv.DictReader(open(decls), delimiter="\t"))
    res = {}
    for node, pat in NODES.items():
        rx = re.compile(pat)
        mods = Counter()
        ex = defaultdict(list)
        for r in rows:
            if rx.search(r["name"]) or rx.search(r["module"]):
                mods[r["module"]] += 1
                if len(ex[r["module"]]) < 3:
                    ex[r["module"]].append(r["name"].split(".")[-1])
        top = mods.most_common(6)
        res[node] = {
            "pattern": pat,
            "n_decls": sum(mods.values()),
            "n_modules": len(mods),
            "top_modules": [{"module": m.replace("OAI.NumberTheory.DirichletL.", ""), "hits": c,
                             "examples": ex[m]} for m, c in top],
        }
        print(f"{node}: {sum(mods.values())} decls in {len(mods)} modules")
        for m, c in top[:4]:
            print(f"    {c:4d} {m.replace('OAI.NumberTheory.DirichletL.', '')}  e.g. {', '.join(ex[m][:2])}")
    json.dump(res, open(out, "w"), indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
