# Independent review of the narrow tangent certificate

20 October 2026. Reviewer: the type-I subagent, independently of the
root agent who wrote the checker and readable certificate.
Verdict: no unresolved defect found in the stated scalar certificate.
This is not a review or certification of every analytic premise.

Frozen files reviewed:

* ../scalar/verify_tangent.py, SHA256
  74d4fe6d3d0fd6727a4f352d3fd1cfc629ca97f8c842c724a3caa1d0b81cad89.
* ../scalar/TANGENT_CERTIFICATE.md, SHA256
  70ce8146419c289f5643566001ab46c16aa1fc3e7c8aede2393f7c455108de64.

The source formulas were compared directly with Liu
arXiv:2610.26835v1, equations (14.3), (14.8), (14.10), Remark 14.1,
and Lemmas 14.8--14.10. The pinned source HTML has SHA256
5b128f3cedb4d6ecfe3a3d57b1290cb576cac03092cf0b807c6f8092abf864c6.

## Source algebra and critical identity

The definitions of D, P, J, R, the derivative R_delta, and the endpoint
E agree with the source. At x=1/2, an independent expansion gives

\[
16J E_b=(50-20c)/9
       +\delta(-14+3c+5c^2/6)+\delta^2(6-c^2/2),
\qquad c=1/(3\kappa).
\]

Multiplication by \(-54\kappa^2\) gives the source critical polynomial
coefficient by coefficient. Thus

\[
E_b=\frac{\operatorname{cr}}{-864\kappa^2J}.
\]

Since \(\bar J=6\kappa J\) and \(Z=96\kappa\bar J\), this is exactly
the checker's identity \(3N_b+2\operatorname{cr}=0\). The three
primitive numerator formulas in equation (1) of the readable proof
have the correct signs and normalization.

At the critical root, \(\ell=-N_0/N_\ell\) gives E=0 independently
of b. Differentiating with ell and b held fixed gives the displayed
formula for b. Terms from differentiating the denominator vanish
because the numerator is zero. Consequently E=E_delta=0 exactly;
this conclusion is not inferred from interval values near zero.

An independent expansion of -2JE gives exactly the three polynomials
A, B, C in equation (5). In particular the coefficients 9hP/4,
-3hD/2, -5DU/3, 5hD/4, and -5hP/8 all have the stated signs.
The polynomial in delta has a double root at y=0. This licenses
discarding its exactly zero discriminant constant coefficient.
For y>0 the four positive remaining discriminant coefficients and
the four positive coefficients of A give the completed-square result.

The affine ell derivative is bounded on the entire source rectangle
by \(5/16>1/8\), using \(R\ge1-\delta\). The code's ell-derivative
test is at the critical point only; the readable proof explicitly
supplies this separate global inequality.

## Implementation and coverage

All acceptance arithmetic uses Fraction. Interval multiplication uses
all four endpoint products. Reciprocal intervals correctly reject any
denominator containing zero, including negative-denominator cases.
The elementary repeated-product power operation is an enclosure even
when dependency makes it wider than an optimal power enclosure.

Both critical-root bisections preserve certified outer bounds for
every kappa in the current box. They do not assume monotonicity in
kappa. The positive delta derivative and endpoint signs certify the
needed critical branch. The 64 closed kappa boxes cover exactly
the stated interval, and their adjacency is checked.

All strict side conditions agree with Remark 14.1 and (14.10).
The code proves coefficient positivity on full interval boxes,
not just at a finite selection of delta, x, or kappa points.
Reported margins are rounded downward using integer division;
acceptance uses the unrounded exact endpoints.

The custom two-variable polynomial operations are correct for the
identities in use. The four-by-four Sylvester determinant uses the
proper coefficient ordering and permutation signs. Its exact
factorization identifies the same quartic as the source.
The total derivative of ell along cr=0, and hence G', uses
delta_prime=-cr_kappa/cr_delta with the correct signs.
G'>0 on every covered box, the endpoint G signs, the resultant,
and the quartic derivative/sign test together identify the relevant
root branch. They do not merely choose a numerical root of a resultant.

The final frozen checker passed independently with both
Python -I -S -B and Python -I -S -B -O. All checks use explicit
exceptions; optimized mode removes none. The two negative controls
are algebraic coefficient/sign controls, as accurately described in
the proof. They are not a mutation suite for the upstream analysis.

## Repair and limits

One wording repair was requested and applied before freezing:
positivity of the completed quadratic holds for all real delta,
whereas E<0 additionally needs J>0. The final text restricts the
latter assertion to the source rectangle.

The certificate proves the narrow tangent family, its continuous
delta/x inequalities, its strict side conditions, and the bracket
for the self-consistent scalar endpoint. It does not certify the
canonical large sieve, the moment estimates, the source probe,
the constant-term guard, or an analytic zero-free theorem.
It does not cover the larger kappa range of the source's full
Lemma 14.9. Nothing in this review implies a boundary smaller than
the scalar endpoint already present in the source.
