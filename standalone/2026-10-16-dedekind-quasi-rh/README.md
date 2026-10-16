# Dedekind quasi-RH: annotated import and two source-faithful extensions

Status: external result IMPORTED as reported; new mathematics PROPOSED,
with complete written component proofs and exact finite checks. No independent
mathematical review, full native moment theorem, improved zero-free exponent,
or RH proof is claimed. This directory changes no integrated status.

## Start here

The current Cureton--Thorner/AxiomProver manuscript is **v2 (Oct 14, 2026)**:
for every number field K, zeta_K is zero-free in Re(s)>31/32, away from one;
finite-order Hecke L-functions have the same region wherever holomorphic.
This extends the field scope rather than improving the earlier Riemann-zeta
7/8 bound. The user-linked v1 PDF instead states 1-1/6000, despite its landing
abstract displaying 31/32. The version distinction is preserved in [IMPORT.md](IMPORT.md).

The mechanism compares two evaluations of one fixed average. A cubic theta
transformation and quadratic large sieve provide the upper bound; Poisson
summation identifies an inverse-zeta detector whose numerator must not vanish.
The general-field automorphic setup is the reusable advance, but it does not
supply the repository's missing full signed 2k-th moment estimates.

## What was actually pushed forward

**1. A coupled source with a safe numerator down to Re(s)>1/2.**
[EULER_STRIPPING.md](EULER_STRIPPING.md) factors the paper's correction as

    H(s)=L^S(6s-3,eta,F) J(s),

and proves J and its inverse bounded on each closed half-plane inside
Re(s)>1/2. The normalized coefficients of J/zeta have only prime exponents
0, 1 and 6, with local polynomial

    1-(1-1/Np)x-eta(p)(Np)^2 x^6.

The corresponding FULL physical polynomials and native Mobius polynomials
compare in BOTH directions at critical normalization with root-norm cost
O_F(log(D)^(12[F:Q])), on the SAME row measure and all shorter column scales.
This is a concrete general-field application of our source-preserving
completion programme, not a generic randomness argument.

There is also an exact warning: stripping the isolated shifted L-factor
AFTER bounding the old detector incurs the termwise exponent floor 2/3.
One must preserve the coupled prime/sixth-power cancellation before taking
absolute values. The character eta has an angular component in the paper;
it is not covered merely by the finite-order Hecke corollary.

**2. A complete conditional general-field moment bridge.**
[FIELD_MOMENT_BRIDGE.md](FIELD_MOMENT_BRIDGE.md) gives balanced finite
Minkowski rows, genuine principal-prime sixth-power replicas, and the exact
recursive prime-mask removal. A full moment bound of size D^(h+k+e+epsilon)
would imply the zero-free boundary

    1/2 + 5h/(12k) + e/(2k).

The exponent formula is ALREADY present in earlier repo work. The contribution
here is the fully specified general-field implementation and proof of the
mask bootstrap, not a new claim to the formula or a proof of its hypothesis.
Near-linear height and zero excess recover the conditional 17/24 fourth-
moment and 23/36 sixth-moment targets; cofinal orders with sublinear excess
would reach the critical line. Mere norm balls would be infinite in fields
with positive unit rank, so that field adapter is not optional.

**3. Exact limits of parameter-only improvements.**
[PARAMETER_BARRIER.md](PARAMETER_BARRIER.md) reconstructs all seven v2
Table 1 margins and proves that the displayed positive Cauchy/mean-square
model, in its stated M>1 and beta<=alpha regime, has saving strictly below
1/12. This is an upper-estimate limitation, not an arithmetic lower bound
or an obstruction to a signed or different transformation.

## Recommended next attacks, in order

1. Insert the COUPLED 0/1/6 source into the theta and Poisson evaluations
   before Cauchy; prove the transformed-family and common-prime adapters.
   The two-way comparison prices its relation to the native source, but
   does not establish that new transform or its needed signed estimate.
2. Attack the actual compensated signed correlation I_k-D_k in #946,
   retaining #944's masks and surviving conductor window. Establish the
   original-field fourth moment before asserting general-field transport.
   Do not apply bounded-coefficient sector estimates directly to the new
   unbounded sixth-power coefficients; use the proved convolution interface.
3. Seek a direct signed bilinear estimate for the additive/theta pairing,
   rather than two independent positive norms. The fixed weights and zero
   detector must remain compatible. This changes a binding inequality,
   whereas repeated field extension, naive phase randomization or a tiny
   retuning of alpha and beta cannot deliver the required critical saving.

The full signed moment, the transformed bound for the new source, and any
critical detector estimate remain OPEN. A useful algebraic bridge is not a
resolution of these analytic estimates.

## Reproduce and inspect

Run `python verify.py` and `python -O verify.py`; both reproduce
[results.json](results.json): **791 explicit finite checks**, including five
false-substitution controls. These check local rational power series,
convolution signs, prime-mask recursions and exponent arithmetic, not infinite
moments or the upstream Lean proof. See [VALIDATION.md](VALIDATION.md).

[IMPORT.md](IMPORT.md) records exact source heads, reading levels, formal
scope and limits. [sources/EXTRACTS.md](sources/EXTRACTS.md) contains attributed
selected manuscript equations. `python fetch_sources.py NEW_DIRECTORY`
retrieves full version-specific PDFs/TeX on a networked machine; it was not
network-run here. This is an annotated import, not a full upstream mirror.
