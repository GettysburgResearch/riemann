# Small-divisor attack: native shell observability

**PROPOSED pending independent mathematical review. RH remains unproved.**
Continuation of PR845 at `be78f076b9abe8d8d6a40c14f71d0df36a4e0407`.
The parent is retained unchanged. Read [PROOF.md](PROOF.md) for every hypothesis,
normalization, analytic domain and closing limitation.

## The new result and the important correction in strategy

The native inverse has a globally compact discrete derivative:

    T(n,d)=1_(d|n)mu(n/d)/n,      ||T||_HS^2=3/2.

Its entire omitted-row norm has a proved tail. But integration back to the
response is NOT uniformly compact. For the ACTUAL source, not just a model,

    ||D_A 1_(d<A/q)|| -> infinity as A=3^r -> infinity

for EVERY fixed q>=1, where D_A=L_A V_A transmits old forcing into the new
shell [A,3A). A uniform forcing-only bound is therefore false. This does not
refute Q-AC26: its old-response penalty eta||V_A f||^2 is indispensable.

The proof supplies an explicit rational witness for the growth, using
Q(A/d)-Q(3A/d), and uses only the classical existence of a critical-line zero.
No zero coordinates, simplicity, RH, or infinite explicit formula are needed
for this native unboundedness result.

## The full coupling has an honest continuum limit

On retained columns d>=A/q, the normalized complete old-and-new matrix
converges in Hilbert--Schmidt norm to the literal-source kernel

    k(s,t)=m(s/t)/(2t),  0<s<3, 1/q<t<1.

The complete error is at most sqrt(200q^6/A), including every activation
strip and the small boundary sliver. This also holds for increasing q(A)
with q(A)^6/A->0. It is not permission to retain d=1 by setting q=A.
No band interaction is dropped in the matrix or the limiting operator.

After a unitary logarithmic change of coordinates the limiting inequality
becomes a prediction estimate: control one future window by the ENTIRE old
response plus forcing, for h(t)=e^(t/2)m(e^t). This necessary consequence
of Q-AC26 is proved; a converse uniform lattice adapter is not asserted.

Any successful uniform constants must pay for actual critical resonances.
If Q-AC26 holds and rho is a critical-line zero of multiplicity m, then

    liminf_(eta->0) eta^(2m-1) C_eta >= c_rho >0.

The explicit constant is in AC27-4. This is a conditional NECESSARY lower
bound, not existence of C_eta or a bound on zeta derivatives.

## A finite all-vector test of the band shortcut

At A=81 and eta=1/100, EACH of the four multiplicative forcing bands admits
an all-vector constant 3/5. Their coherent combination, forty unit entries,
requires more than 94/100. Its off-diagonal contribution alone exceeds 1/2
of the forcing norm squared. A complete C=1 certificate still passes.
Thus proving the band estimates and adding them as though orthogonal is not
valid. All these finite comparisons are exact rational certificates.

## What is and is not closed

| Claim | Scope |
|---|---|
| AC27-1 | Global Hilbert--Schmidt derivative and complete tail; sign-exact squarefree conjugacy. |
| AC27-2 | Exact native mean-row identity, rational probes, and unbounded transmission in every small-relative-forcing sector. |
| AC27-3 | Quantified all-vector approximation on fixed or explicitly controlled growing relative ranges. |
| AC27-4 | Necessary native future/past estimate; conditional critical-zero lower cost for compactness constants. |
| AC27-5 | Exact finite full-vector band bounds and a coherent cross-band counterexample to summing them. |
| Section 6 | A weaker subpower-defect shell estimate would suffice for RH; its premise is OPEN. |

No global upper bound for the coupled response, no uniform no-concentration
proof, and no RH solution is established. The new compactness theorem is
about the derivative, not the operator required by the closing argument.
The parent synthetic system has an even smaller compact derivative norm and
still fails the desired shell property, so that inference cannot be used.

## Reproduce and review

    python -B check.py --check results.json --self-test
    python -O -B check.py --check results.json --self-test
    python -OO -B check.py --check results.json --self-test

The checker reconstructs the primitive arithmetic, full band matrices,
certified mean probes and complete expected payload. It validates the seven
manifest entries before accepting a stored report. Exact large fractions
are represented by outward rational intervals plus hashes, after the exact
comparisons have been made; these are not floating estimates.

Read [VALIDATION.md](VALIDATION.md) for actual executions and exclusions,
[ATTEMPT.md](ATTEMPT.md) for the remaining proof step, and SOURCES.json for
exact attribution. Same-author implementation checks are not independent
mathematical review. No previous result's canonical status is changed.
