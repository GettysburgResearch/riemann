# R-98100 — The source-blind bounded-remainder argument has an exact logarithmic fourth-power frontier

Claim ID: `R-98100`  
Status: **PROVED METHOD FIREWALL**  
Created: 2026-08-18  
Depends on: `L-98101`; Mertens/PNT estimates  
RH status: **not assumed**

For an arbitrary child cutoff `Y=Y(X)`, the global absolute estimate in
`L-98101` gives

\[
|\mathfrak E_{\rm bulk}(X)|
\ll {E_Z\over\sqrt Y}{\log X\over\log Z}.
\tag{R-98100.1}
\]

The positive Euler main is comparable to `1/log X`. Thus the dimensionless
control parameter of this method is

\[
\boxed{
\mathcal C_Z(X,Y)
={E_Z(\log X)^2\over\sqrt Y\log Z}.
}
\tag{R-98100.2}
\]

The argument proves the bulk negligible only when `mathcal C_Z -> 0`.

Suppose

\[
Y=(\log X)^\alpha.
\]

Then

\[
\mathcal C_Z(X,Y)
={E_Z\over\log Z}
(\log X)^{2-\alpha/2}.
\tag{R-98100.3}
\]

For every cutoff `Z>=67`, the ratio `E_Z/log Z` is positive. Moreover it tends
to infinity as `Z->infinity`: by the prime number theorem,

\[
\log E_Z
\ge c\sum_{Z/2<p\le Z}p^{-1/2}
\gg {\sqrt Z\over\log Z}.
\tag{R-98100.4}
\]

It therefore has a positive global infimum on all admissible cutoffs.
Consequently:

```text
alpha<4:  C_Z(X,Y) -> infinity uniformly in Z;
alpha=4:  C_Z(X,Y) is bounded away from zero;
alpha>4:  L-98100 supplies a slowly growing Z with C_Z(X,Y)->0.
```

Hence

\[
\boxed{
\alpha=4
}
\tag{R-98100.5}
\]

is the exact frontier of the **source-blind absolute bounded-remainder method**.
This does not prove that the true signed bulk is large at or below the frontier;
it proves that the retained global estimate cannot certify it negligible.
Crossing the line requires signed source cancellation, an exact recurrence, or
a different state.

The appearance of the same fourth-power scale as in the First-Hermite heat
lane is recorded only as a scale coincidence. No norm map or theorem-level
identification between the two routes is asserted.