# TRG26 — sharp centered divisor gaps and a two-reservoir reduction

**Proposed complete component proofs; independent review required. RH remains
unproved.** This packet resolves the centered all-support sharpness question
left open in PR825/PR828. It is not an RH proof.

Use the unchanged prime-power form in the harmonic metric. For a prime cutoff P,
split the primes at the last Q with Z(Q)^3<=Z(P), Z(x)=product_(p<=x)(1+1/p).
Take the UNION of the two squarefree prime boxes, identifying their common root 1.
All allowed edges are retained and the support is divisor closed.

The new complete proof gives

    gap(S(P))=3 zeta(2)/log log P+O((log log P)^(-2)).

Every eigenvalue except zero and that one slow mode is at least (3/2)log2. The
old upper bound and this family establish that the worst inverse CENTERED gap
on the entire divisor-closed support class has order log log P. Product boxes
alone have constant centered gaps. Nothing transfers this asymptotic to n<=N.

The first gap is the unique zero of a finite strictly decreasing scalar function
built from the two root resolvents. The complete eigenvector is explicit. Shared
root mass and coincident root-killed poles are handled without discarding terms.

Read PROOF.md, then ATTEMPT.md. Section 3 of ATTEMPT.md states the still-open
arithmetic input and the full conditional deduction to RH; it is not supplied
by the graph theorem. CLAIMS.json separates new proofs, inherited comparisons,
and the open source inequality. SOURCES.json records versions and read scopes.

Two directed finite certificates use ACTUAL logarithmic prime rates:

- P=17, 65 vertices and 193 edges: gap in (0.73956963541318,0.73956963541319).
- P=31, 1025 vertices and 5121 edges: gap in (0.72552568064883,0.72552568064885).

All 64/1024 nonconstant product modes needed by the root equation are included.
These small examples are not evidence for the asymptotic or for RH. Other finite
panels use declared rational test rates to verify exact spectral/gluing algebra.

Run from this directory:

    python -I -S -B verify.py --check result.json
    python -I -S -B -O verify.py --check result.json
    python -I -S -B test_rejections.py

`--emit` is an unauthenticated producer, not an acceptance command. See VALIDATION.md
for exact execution boundaries. No parent campaign, full checkout, Lean build,
external referee acceptance or novelty assessment is claimed.
