# R-102870 — Fixed partial-completion positivity is masked by a rightmost real branch

Claim ID: `R-102870`  
Status: **PROVED ANALYTIC SCOPE FIREWALL**  
Created: 2026-08-24  
Depends on: `L-102891--L-102893`  
RH status: **not assumed**

For every fixed \(0<c<1\), `L-102891` proves that the partially completed
outer observation \(H_c(X)\) is eventually positive.  This does not imply RH.

Indeed,

\[
B_c(z)=\zeta(z)^{c-1}G_c(z)
\]

with \(c-1\in(-1,0)\).  At the real point \(z=1\),

\[
B_c(z)
=
G_c(1)(z-1)^{1-c}
\bigl(1+O_c(z-1)\bigr).
\]

Therefore the Mellin transform of \(H_c\) has a nonanalytic real branch point
at

\[
s=1/2.
\]

It is this rightmost real branch which produces the positive asymptotic

\[
H_c(X)
\asymp_c
\sqrt X(\log X)^{c-2}.
\]

A hypothetical off-line zero \(\rho\) of \(\zeta\) would produce another
branch singularity at

\[
s=\rho-1/2,
\]

but

\[
\Re(\rho-1/2)<1/2.
\]

Thus the fixed real branch at \(s=1/2\) dominates every possible off-line
singularity.  Landau stops at that real singularity and detects nothing about
the deeper zero set.

At the native endpoint \(c=0\), the coefficient

\[
1/\Gamma(c-1)
\]

vanishes.  The fractional real branch becomes the analytic zero
\(1/\zeta(z)\) at \(z=1\), and the deeper reciprocal-zeta singularities again
become conclusion-bearing.  The positivity threshold in `L-102891` is
therefore necessarily nonuniform as \(c\downarrow0\).

## Consequences

The following implications are invalid:

```text
H_c eventually positive for one fixed c>0
  -> native H_0 has subpower negative mass;

geometric-midpoint half-source eventually positive
  -> its arithmetic source square is nonnegative;

fixed partial-completion positivity
  -> RH.
```

A valid use of the midpoint must first recombine the complete arithmetic source
square and then remove the squared completion by the positive inverse of
`L-102893`.  The open criterion is `GMBC102893`, not the first-order tail sign.
