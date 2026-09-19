# PET26 L-family continuation: logarithmic boundaries, not a zeta-to-GRH claim

This is a bounded extension for issue #738. Its original programme concerns
quadratic GL(2) twists. Burungale--Tian's CM cubic twists are a distinct,
explicitly declared reference family. The rank-one and central-deflation
material already in BCP26/SBC26 is preserved; this file adds different algebra.

## 1. Preserve the source-specific logarithmic relation under Newton

Let A(1)=1 be arithmetic L-series coefficients, nu its Dirichlet inverse,
and Lambda_A=(DA)*nu, Df(n)=f(n)log n. Then

    Dnu + Lambda_A*nu = 0.

For a finite prefix-preserving source c, set

    e = delta-A*c,
    v = 2c-A*c*c,
    L_A(c) = Dc+Lambda_A*c.

The exact identity from PROOF.md is

    L_A(v) = 2e*L_A(c).

Thus both the ordinary inverse defect and the logarithmic defect move beyond
the square cutoff. This is formal coefficient algebra for ANY such A,
including finite Euler products; no automorphy, zero-free region, or analytic
rank theorem is assumed in the calculation. The check uses prime-valuation
derivations D_p instead of floating logarithms.

## 2. The entire prime-power tail has a finite local numerator

Write the inverse local Euler polynomial as

    P_l(T) = 1+c_1*T+...+c_D*T^D.

Define the local logarithmic coefficients by

    -T*P_l'(T)/P_l(T) = sum_(k>=1) L_(l,k)*T^k.

Multiplying the k>=2 tail by P_l gives EXACTLY

    P_l(T) sum_(k>=2) L_(l,k) T^k
      = -T P_l'(T) - L_(l,1)*T*P_l(T).

The right side has degree at most D+1 and no constant or linear term.
Restoring the reciprocal coefficients at primes other than l therefore
collapses infinitely many prime-power interactions to finitely many local
repeated-prime insertions. This is not an analytic truncation.

For a good elliptic prime in ARITHMETIC normalization,

    P_l(T)=1-a_l*T+l*T^2,

the local tail numerator is

    (a_l^2-2l)*T^2 - a_l*l*T^3.

For a good inert CM prime, a_l=0, so it is simply

    -2l*T^2.

The sign is NEGATIVE. For zeta, P_l(T)=1-T and the corresponding tail is
+T^2. Importing the zeta sign into the inert GL(2) family is therefore wrong.
SBC26 already derived a squared cutoff window for this family; the present
statement is the logarithmic-tail numerator and its Newton propagation,
not a rediscovery claimed as a new cutoff window.

In UNITARY normalization replace a_l by lambda_l=a_l/sqrt(l), and l by 1.
The numerator becomes (lambda_l^2-2)T^2-lambda_l*T^3. These two normalizations
must not be mixed. PET26's quantitative 1/12 zeta covariance bound has NOT
been proved for this different signed local measure or for GL(2) families.

## 3. Exact good-prime examples from the paper's reference curves

For E_m: y^2=x^3+m^2/4 and an odd prime l not dividing 3m, the code directly
counts the points over F_l, including the point at infinity, and obtains
a_l=l+1-#E_m(F_l). The twelve checked values are:

| m | l=5 | l=7 | l=11 | l=13 | l=19 | l=23 |
|---|---:|---:|---:|---:|---:|---:|
| 17 | 0 | 5 | 0 | -7 | 8 | 0 |
| 53 | 0 | 5 | 0 | 5 | -1 | 0 |

These are exact integer counts, not L-value or zero computations. The finite
three-prime fixture in algebra.py uses the good factors at 5,7,11 for E_17.
It OMITS every other local factor and is therefore not the global L-function.
It verifies the source inversion, the logarithmic defect, its square cutoff,
and the first excluded endpoint. Additional local polynomials test the cubic
term and both normalization patterns. An invalid bad-prime count and a
wrong inert-square sign are rejected.

## 4. What the Sylvester paper supplies, and what it does not

The supplied arXiv:2609.14893v2, Theorem 1.1, states exact analytic rank one
for E_p and E_(p^2), for primes p=8 mod 9. This remains an EXTERNAL theorem,
not certified by the point counts or formal Euler algebra here. Its
nonzero division boundary and integral norm/projector argument motivate
retaining arithmetic relations before projection; this packet constructs
no analogue of its Tate-cohomological boundary for zeta.

The reference family's central-zero deflation fixtures in BCP26 remain
useful. The present continuation supplies a second, independently specified
kind of regression: can a proposed family source operator preserve the
correct logarithmic relations and repeated-prime signs?

Neither the finite point counts nor the external rank-one theorem controls
all zeros. No GRH conclusion or family moment bound is claimed.
