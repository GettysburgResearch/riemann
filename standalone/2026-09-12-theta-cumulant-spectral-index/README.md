# Whole-theta cumulant spectral index

**Proposed component proofs, pending independent review. NOT an RH proof.**
Prepared as an add-only continuation of PR #842 at
`34ee76ed5bc8124a30aff7567152d4ae9f7f69cb`.

This pass changes the completion target rather than asserting an unsupported
Ising moment induction. The whole-theta cumulant form has exactly one negative
direction per distinct off-line quartet, including the possible infinite case.
Every selected finite collection has a finite polynomial witness whose entire
remaining complex spectral tail is bounded. A positive cyclic realization is
then supplied CONDITIONALLY on positivity of this form at every degree.
No positive metric on the old theta-weighted exponential modes is presumed.
A complete source-only bound sum m_j|lambda_j|^2<=1/8 supplies an explicit
tail budget for every finite witness; it does not prove its signed form positive.

For the actual law w=phi/Xi(0), define

```
q_n=(-1)^(n+1) kappa_(2n)(w)/(2(2n-1)!),
H_d=(q_(i+j+2))_(i,j=0)^d.
```

The exact conclusion is

```
sup_d ind_-(H_d) = number of DISTINCT off-line Xi quartets (possibly infinity).
```

Analytic multiplicities remain as weights, not as additional independent
negative directions. This adapts the classical power-sum/moment criterion and
extends #858's finite-approximant index argument to the actual whole xi source.
#839 already proves the whole-source shift2 positivity criterion; #841 supplies
the shift1 version and a complete4x4 source certificate. Their work is credited
explicitly. No external novelty is claimed for Hermite/Hankel criteria, GNS or quadrature.

The new complete source integration encloses raw theta moments through36 and
certifies TWO nine-dimensional forms, shifts1 and2, by all18 positive interval
LDL pivots. It uses768-bit outward integer arithmetic,128 midpoint Taylor cells
of degree63 on[0,3], eight theta terms, and analytic bounds for BOTH complete
infinite tails. No zeta or zero oracle is used. These finite forms provide a
positive nine-node Gaussian spectral quadrature, not a finite Ising model or
an all-order sign theorem. Their LDL pivots are not spectral gaps.

Start with PROOF.md Sections1--4 and7. Section5 and certify.py specify the
computer-assisted finite claim. REVIEW.md lists the exact potential failure
points. SOURCES.json records frozen SHA/path/depth, not an exhaustive review
of every repository branch. The early finite-spin scouts failed to deliver a
new certified fit and are explicitly excluded from the proof.

```
python -I -S -B certify.py --check certificate.json
python -I -S -B -O certify.py --check certificate.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

Each accepting certify command reconstructs the entire native source and both
matrices; it does not merely hash a prior computation. --emit is producer mode,
not acceptance. The same implementation runs normally and optimized; that is
not independent mathematical or numerical-backend review.

The missing theorem is H_d>=0 for EVERY d. Ordinary probability moments are
positive Grams; the connected cumulants used here are not automatically so.
Neither the finite certificate, local Ising feasibility, nor an approximant's
finite exceptional index proves that all-order assertion.
