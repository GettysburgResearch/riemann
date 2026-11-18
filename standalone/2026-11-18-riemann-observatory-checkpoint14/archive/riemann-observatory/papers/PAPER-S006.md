# PAPER-S006 — Kuipers,Hummel and Richter,2014

**Identity.** Jack Kuipers, Quirin Hummel and Klaus Richter, *Quantum graphs whose spectra mimic the zeros of the Riemann zeta function*, Physical Review Letters112,070406(2014); DOI10.1103/PhysRevLett.112.070406. arXiv1307.6055, first2013-07-23; inspected v2 dated2014-02-26, https://arxiv.org/pdf/1307.6055v2 . The generated PDF's internal date says2018-09-22; bibliographic version is grounded in arXiv metadata rather than that typesetting date. Access2026-11-17.

**Audit scope.** Level0 verified. Main text pp1–5 read, AppendixA and the beginning of AppendixB inspected; remaining appendices not fully read. Whole-work Level1 incomplete. Single-butterfly secular equation and first correction coefficients independently checked; convergence of the infinite collection and every recursive construction not fully audited. No claim that a Hilbert–Pólya operator is constructed.

## Precise inspected construction

A butterfly has two directed bonds of equal lengthL and a unitary2×2 vertex matrixS. Its wave numbers solve det(I−e^(ikL)S)=0, so if S has eigenvalues e^(iθ_j) they are k=(2πn−θ_j)/L, n∈Z. Its mean density isL/π. For realTrS the oscillating trace contribution is(1/π)∑_(m≥1)L Tr(S^m)cos(kmL), equation(7),p3, with smoothing/interpretation still required.

The zeta prime-power trace coefficient has one minus sign for every repetition, rather than alternating under a single negative orbit amplitude. The authors avoid interpreting each prime as one orbit: they recursively add uncoupled butterflies of lengths mlogp so their *combined* coefficient at each prime power matches the target. Equation(11),p3, is

    ∑_(d|m) d Tr(S_(p,d)^(m/d))=−p^(−m/2).

The recursion(12) need not keep |TrS|≤2; adding multiple identical copies repairs the matrix-trace restriction. Equation(14),p4, supplies that multiplicity construction. Their first p=2 butterfly has TrS=−1/sqrt2, so TrS²=(TrS)²−2=−3/2. At length2log2 the desired target is−1/2, hence a new butterfly with TrS=1/2 contributes2TrS=1, restoring the required coefficient. This checks the first nontrivial repetition repair directly.

## Exact limitation stated by the authors

The infinite collection has a divergent mean density and an infinitely dense composite spectrum; subtracting the mean can produce the desired oscillatory pattern but not the zeta spectral measure. The main text explicitly explains that its spectra differ and that it cannot prove reality of the zeros (pp4–5). Finite cutoffs match only the included coefficients and differ thereafter. The Gaussian smoothing used in plots is part of the limiting prescription, not a proof that the raw prime series converges.

## Knowledge gained

This is a concrete counterexample to the inference 'correct prime-side oscillations plus self-adjoint component operators gives the zeta spectrum'. Positivity/local finiteness of the *full* spectral measure, and control of its mean/tail, remain independent requirements. It complements the finite-graph counting obstruction: infinitely many components evade finite-channel bounds by losing local spectral finiteness.

## Precise next question

Can butterflies be connected/reused so that their aggregate length and local density are finite while retaining the prime-power coefficient identities and a single self-adjoint domain? The authors suggest bonds log((n+1)/n) whose partial sums generate logp (p4), but unwanted composite lengths must then cancel. State the resulting infinite graph's domain and prove compact resolvent/local finiteness before pursuing coefficient matching. A necessary first lemma is a rigorous bound on the integrated positive spectral mass under the proposed truncation; subtracting a divergent constant is not itself such a bound.
