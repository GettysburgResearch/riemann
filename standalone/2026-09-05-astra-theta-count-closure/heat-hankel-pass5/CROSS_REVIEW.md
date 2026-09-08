# Cross-branch reading, source locks, and the abandoned closure shortcuts

Status: focused mathematical synthesis, not a repository-wide review verdict.
RH remains unproved. The component proofs in PROOF.md are proposed for review.

## What was actually read

The live PR descriptions were surveyed, then four full proof texts were read
at pinned heads. No claim here imports an unreviewed PR title as a theorem.

### PR #793: finite capture in a different Hardy metric

Head: f22b67db113d1aa4f986fe35a2fc0321fdff7d47.
Files under standalone/2026-09-05-three-route-assault/pass2/:

- R3_HARDY_CAPTURE.md, Sections C1--C7;
- R2_CAUSAL_ENERGY.md, Sections B1--B7.

R3 constructs a damped Toeplitz-type zero kernel with rational resolvent
weights. Its central useful idea is to remove the whole non-target zero
background with a Blaschke product, then preserve a negative pair direction
with explicit trace/time error budgets. The local Gram, trace-class bound,
and interpolation mechanism were followed in this pass; its code was not
independently rerun. The arithmetic positivity statement is still open.

R2 is different: causal log-time Mobius energy is positive by construction,
its diagonal is finite for every positive damping, and the complete signed
off-diagonal upper bound remains open. Its causal/anti-causal counterexample
is correct and essential: a meromorphic boundary integral is not by itself
the Hardy boundary value of the causal arithmetic transform.

The present packet imports the METHOD of complete Hardy interpolation, not
an unproved positivity theorem. It rederives trace convergence, exact index,
and source formulas for the DIFFERENT Hankel kernel S(tau+s+t). The dyadic
finite spaces do not depend on zero nodes and come with source-only error
bounds. They are not the target-adapted witness spaces of R3.

### PR #792: actual-prime diagonal and boundary integrability

Head: 875e8dd47186e924445533513a1ad405af09d7a7.
Files under standalone/2026-09-05-bernstein-chebyshev-growth/prime-energy-boundary/:

- PROOF.md, especially PE-1 through PE-4;
- BOUNDARY.md, BR-1 and BR-2.

PE-1's moving-degree argument uses exact ordinary Laguerre moments, a
localized variation bound, and quantitative PNT; it obtains a polynomial
prime diagonal. PE-2 retains the full signed two-variable source. The
polynomial-loss comparison of full energy with that diagonal is NOT proved.
We checked the displayed moment/cross-term arithmetic and the structure of
the PNT split, not its complete external analytic proof chain or code.

The same-prime altered-weight counterexample is particularly relevant:
positive weights tending to log p, PNT, and the diagonal scale still permit
an extra meromorphic pole. Therefore the diagonal cannot be used to orient
our equation (29) without an exact adapter and a new arithmetic estimate.
No such adapter or estimate is claimed here.

BR-1 correctly separates meromorphic radial p-means from holomorphic Hardy
membership. BR-2 proposes an area norm whose local integrability excludes
interior poles while allowing boundary poles. Its finiteness is still an
RH-strength question. Our trace norm is unconditionally finite, so its
RH-bearing datum must instead be the NEGATIVE spectral mass. We retain that
distinction rather than importing the area conclusion from a radial bound.

### Existing #790 and older structural boundaries

Own exact base: 634d9a8ec4b0819442e601686a109ff7015b7b0b.
The local extracted original packet and joint-ray-pass4 packet were read.
The invariant product and the unconditional explicit formula are the analytic
inputs used, not the proposed finite-depth heat inequalities. No finite zero
verification, parent numerical certificate, or claimed depth 10^22 is needed
for the present component theorems.

The #765 raw-innerness warning, #785 spectral-to-coefficient warning, and
#778 principal-mode warning remain relevant boundaries from earlier reading;
this pass does not claim a new full review of those branches. In particular
we do not posit an inner raw xi quotient, infer coefficient positivity from
an aggregate positive transform, or extract a principal theorem from an
average without a bound.

## Classical literature boundary

These references are credits, not claims of external novelty. No priority
search covering the entire literature has been completed.

1. D. R. Yafaev, *On finite rank Hankel operators*, arXiv:1304.2677 (2013),
   https://arxiv.org/abs/1304.2677.
   The abstract states explicit positive/negative inertia formulas. General
   finite-rank Hankel inertia is not new here. We prove the required special
   exponential case directly and extend it using the summable zero source.
2. D. R. Yafaev, *Quasi-diagonalization of Hankel operators*, arXiv:1403.3941
   (2014), https://arxiv.org/abs/1403.3941.
   General Laplace/Hankel sign-definiteness and inertia are established
   theory. Its abstract was checked; its full 42-page proof was not audited.
3. Classical right-half-plane Hardy/Paley--Wiener, normalized Blaschke products,
   model spaces, and Takenaka--Malmquist bases. The exact formulas used are
   reproduced and checked in the finite confluent cases, not called new.
4. DLMF 5.9(ii), https://dlmf.nist.gov/5.9,
   digamma integral representations; their elementary positive remainder
   proves the inequality used in PROOF.md (22).
5. The unconditional Guinand--Weil explicit formula in the normalization of
   Chirre--Goncalves, Mathematische Zeitschrift 300 (2022), Proposition 5,
   https://doi.org/10.1007/s00209-021-02820-9.
   It is inherited from prime-heat-pass3, not from the source paper's
   RH-conditional headline theorems. The endpoint, Fourier convention, and
   rational-test admissibility are rederived in PROOF.md (29).
6. Standard invariant xi genus-zero product and zero count, already stated
   in the original #790 packet. No zero distribution premise beyond the
   unconditional critical strip and ordinary finite-order theory is used.

No PDF was rendered or reviewed in this pass. The web literature inspection
was of abstracts/HTML and the DLMF formula page, not an independent replay of
all classical proofs. GitHub source reading used the connected repository.

## The all-out completion attempt and its honest result

The attempted synthesis was:

literal heat source -> Hankel operator -> dyadic finite matrices
-> use positive heat / source energy to prove every matrix positive -> RH.

The first two arrows now have complete component proofs with explicit global
errors. The final matrix-positivity arrow was attacked in two ways:

(a) A positive heat kernel makes every raw entry positive. It does not orient
    signed coefficient vectors; equation (33) gives an exact negative test.
(b) The literal-prime diagonal in #792 has an unconditional polynomial bound.
    It is a different energy, and no source-preserving domination of the
    current rational-test form follows. The same-prime counterexample there
    excludes replacing that missing argument by a generic diagonal bound.

The remaining inequality is therefore precisely the full signed form (29),
on a predetermined sequence of source-only finite spaces. The trace-class
approximation is NOT an approximation by positive operators. A positive
construction or negative-mass estimate tending to zero is still required.
No unconditional end-to-end RH proof has been found or claimed in this pass.
