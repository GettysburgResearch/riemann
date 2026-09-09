# Verified-height transfer and the prime-square drift

**PROPOSED COMPLETE COMPONENT PROOFS. Independent mathematical/code review
required. RH and the eventual sharp arithmetic bound remain unproved.**

This continuation proves a large uniform range of the actual annular
prime-power inequality from PR #803, instead of only proposing another
criterion. With the unchanged normalization

    D(m)=B(m)/(192m^3)-45m/128+1/4,

one has

    D(m)>1/10   for every REAL 2<=m<=50,000,000,000,
    D(m)>1/200  for every REAL 2<=m<=100,000,000,000.

The result covers the continuous scale range 4<=X=m^2<=10^22. It is NOT
10^11 separate checks, a new zero verification, or a full-window PSD result.
It imports Platt--Trudgian's published RH verification only through
H=3*10^12 and supplies a complete bound for every zero above H. Neither
simplicity nor the actual ordinates of verified zeros are used. Their
large verification is NOT rerun here. The analytic counting estimate and
tail calculation are proved in PROOF.md; the finite endpoint arithmetic is
reconstructed by the checker.

For every m>=2 there is also the weaker unconditional bound

    B(m)>(135/2-1887/(5*10^12))*m^4-19m^3.

The small but fixed m^4 loss makes it INSUFFICIENT for RH. It must not be
reported as positivity of D at unbounded scales.

The direct arithmetic decomposition also proves:

* the prime-square contribution to B/(192m^3) tends to 49/288;
* ALL exponents k>=3 contribute O(m^-1/3+m^-1/2 log m), with an explicit
  elementary bound and a PNT-based leading cube asymptotic;
* a prime-only endpoint must use the corrected offset 121/288, not 1/4.

PNT is used for the prime-square/cube asymptotics, not for the finite-height
transfer. The prime-only eventual inequality remains open. The exact
signed Chebyshev-discrepancy integral and the failure of the attempted
absolute-value domination are given in Section 8 of PROOF.md.

## Read and replay

Read PROOF.md, SOURCES.md and VALIDATION.md. Keep the unchanged sibling
annular-scalar-route directory in place. The checker authenticates its two
consumed files before importing the standard-library interval primitives.

    python -B validate.py
    python -B verify.py --check result.json
    python -B -O verify.py --check result.json
    python -B test_rejections.py
    python -B test_rejections.py --optimized

The code checks finite arithmetic, not the truth of the external theorem,
Jensen's theorem, the infinite product, or PNT. No floating-point library,
optimizer, new prime/zero campaign, formal build, or external-priority claim
is used. All previous packets remain unchanged; this is proposed research,
not reviewer acceptance of our own earlier work.
