# L-96303 — Two fixed native rows detect every open-strip zero

Claim ID: `L-96303`
Status: **PROVED EXACT ALGEBRAIC/ANALYTIC REDUCTION — SOURCE-LEVEL REVIEW REQUESTED**
Created: 2026-08-16
Inputs: `L-96302`; fixed-row transform of PR #542; exact two-row algebra of PR #546
RH status: **unproved**

For fixed `j>=2`, put

\[
 f_j(X)=c_X(j)\ge0.
\]

Absolute termwise integration for `Re s>1/2` gives

\[
 \boxed{
 \int_1^\infty f_j(X)X^{-s-1}\,dX
 = {C_j\over s^2}
 +{P_j(s+1/2)\over s^2\zeta(s+1/2)},
 }
\tag{L-96303.1}
\]

where

\[
 P_j(z)=A_jj^{-z}-B_j(j+1)^{-z}
       -C_j\sum_{m=1}^{j+1}m^{-z}.
\]

For rows two and three, with `x=2^(-z)` and `y=3^(-z)`, direct simplification
gives

\[
 P_2(z)=2x-1-y,
\]

\[
 3P_3(z)=5y-x-1-3x^2.
\]

If both vanish, substitution yields

\[
 3(x-1)(x-2)=0.
\]

For `0<Re z<1`, `|x|=2^{-Re z}` lies strictly between `1/2` and `1`; hence
neither root is possible.  Therefore

\[
 \boxed{P_2(z)\text{ and }P_3(z)\text{ have no common zero in }0<Re z<1.}
\tag{L-96303.2}
\]

Every hypothetical nontrivial zeta zero is detected by at least one of the two
fixed nonnegative rows.  No large-row asymptotic or effective row choice is
needed.

For real `s>0`, the right side of (L-96303.1) is analytic: zeta has no real zero
in `1/2<s+1/2`, and its pole at one becomes a zero of `1/zeta`.  Landau's
abscissa theorem for the Mellin transform of a nonnegative function therefore
forces the defining integral for each of rows two and three to be holomorphic
throughout `Re s>0`.

```text
full-row nonnegativity                  L-96302
fixed-row reciprocal-zeta transform     exact
rows 2 and 3 common cancellation        impossible
real positive axis                      analytic
Landau input                            nonnegative Mellin density
```
