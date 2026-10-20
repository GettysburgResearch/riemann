# Scope comparison for the pure cubic row-scale mean

20 October 2026. This note compares the proposed pure cubic mean
against the particular supplied structured-mean source. It is not
a comprehensive priority claim about the literature.

The mean in ../average/ANGULAR_SELF_ABSORPTION.md has completed
coefficient \(\alpha(c)^\ell\widetilde g(c)\), nonzero fixed
angular order ell, and conjugate cubic row character
\(\overline{(c/r)_3}\). It bounds its square over r<=R on
\(\sigma=1/2+\delta\) by \(R^{1+\epsilon}\), with the stated
height factor. Its exact finite-profile and entire-continuation
arguments are separate analytic dependencies.

The relevant comparison is
[rStation paper 5 v3](https://rstation.ai/problems/riemann_hypothesis/papers/5),
Theorem 5 and its completed estimate (11.4). Set the sextic
element row z=1 and its fourth-power label f=r. Thus K=1,
F=R and Q=1. Reciprocity on fixed ray sectors identifies
\(\chi_c(r)^4\) with the desired cubic twist. Undoing the
source's 1/F label normalization gives the completed annular bound
\[
                       R+R^2/D.
\tag{PC1}
\]
The complete cube variable and its common-prime zeros are retained.

The original-side cubic large sieve for the same completed annulus,
with at most a logarithmic cube mass, gives
\[
                       R+D+(RD)^{2/3}.
\tag{PC2}
\]
For D between \(R^{1/2}\) and R, the competing excess terms
in the minimum of (PC1)--(PC2) are
\((RD)^{2/3}\) and \(R^2/D\). They meet at
\[
                         D=R^{4/5},
\qquad
                         (RD)^{2/3}=R^{6/5}.
\tag{PC3}
\]
For smaller D the original bound returns to R, and for larger
D the completed long bound returns to R. In particular evaluating
only at D=R would miss the intermediate maximum.

For the Dirichlet-series mean on \(1/2+\delta\), insert the
dyadic factor \(D^{-2\delta}\). For \(0<\delta<1/4\),
Minkowski and geometric summation give from these two inputs
\[
            R^\epsilon\{R+R^{6/5-8\delta/5}\},
\tag{PC4}
\]
up to the inherited fixed-angular and height constants.
For delta below 1/8 this is weaker than the new row-scale
bound. For delta at least 1/8, it already has row-scale size.

The source's earlier cubic Theorem 1 has the different prescribed
coefficient \(\mu(c)\alpha(c)^{\pm2}\gamma_2(c)\), including its
Möbius sign. That multiplier is not present here and cannot be
removed by an arbitrary-coefficient interpretation of the theorem.
Its Theorem 6 is a quadratic-character mean, so also does not
identify this cubic family.

Thus no overlap found in these particular supplied results
eliminates the improvement of the pure cubic mean near the
half-line. This statement does not claim that every other
possible theorem or combination of inputs has been excluded.
In particular, the new joint quadratic/sextic exponent 28/11
has a different source comparison and is already recoverable
from (11.4) plus the sextic operator sieve; that overlap is
explicitly recorded in its own proof.
