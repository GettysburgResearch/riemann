# L-102897 — Positive critical-temperature drift is exactly the midpoint adverse mass

Claim ID: `L-102897`  
Status: **PROVED EXACT CRITERION TRANSLATION; RH-EQUIVALENT**  
Created: 2026-08-24  
Depends on: `L-102893`, `L-102895--L-102896`  
RH status: **unproved**

Let \(\vartheta(X)\) be the unique transition zero of `L-102896`.  On its
transition interval,

\[
\partial_t\mathscr S_t(X)
\asymp
{\sqrt X\over(\log X)^2}.
\]

Since

\[
\mathscr S_{\vartheta(X)}(X)=0,
\]

the mean-value theorem gives

\[
\mathscr S_{1/2}(X)
=
-\partial_t\mathscr S_{\xi_X}(X)
\left(\vartheta(X)-{1\over2}\right)
\]

for some \(\xi_X\) between \(1/2\) and \(\vartheta(X)\).  Therefore, for all
sufficiently large \(X\),

\[
\boxed{
c_1{\sqrt X\over(\log X)^2}
\left(\vartheta(X)-{1\over2}\right)_+
\le
(\mathscr S_{1/2}(X))_-
\le
c_2{\sqrt X\over(\log X)^2}
\left(\vartheta(X)-{1\over2}\right)_+,
}
\tag{L-102897.1}
\]

with fixed positive constants \(c_1,c_2\).

Define the temperature-drift functional

\[
\boxed{
\mathfrak T(Y)
=
\int_{X_0}^Y
{\sqrt X\over(\log X)^2}
\left(\vartheta(X)-{1\over2}\right)_+
{dX\over X}.
}
\tag{L-102897.2}
\]

Then

\[
\boxed{
\mathfrak T(Y)=Y^{o(1)}
\iff
\int_1^Y(\mathscr S_{1/2}(X))_-{dX\over X}=Y^{o(1)}.
}
\tag{L-102897.3}
\]

By `L-102895.7`, \(\mathscr S_{1/2}\) is exactly the arithmetic
geometric-midpoint square observation of `GMBC102893`.  The positive
square-lattice inverse in `L-102893` therefore gives

\[
\boxed{
\mathfrak T(Y)=Y^{o(1)}
\Longrightarrow
\mathrm{RH}.
}
\tag{L-102897.4}
\]

Conversely, RH gives the standard subpower bound for every fixed compact
zero-safe observation of

\[
{\zeta(2z)^{-1}\over\zeta(z)}
\]

and hence gives the right side of (L-102897.3).  Thus

\[
\boxed{
\mathrm{RH}
\iff
\mathfrak T(Y)=Y^{o(1)}.
}
\tag{L-102897.5}
\]

## New coordinate

The final arithmetic sign has become the direction in which one real zero of a
finite completion-temperature polynomial drifts away from the canonical
midpoint.

```text
theta(X)>1/2  <=>  midpoint square is adverse at X;
theta(X)<1/2  <=>  midpoint square is favorable at X.
```

The displacement is already unconditionally exponentially small by
`L-102896`; only its positive weighted drift remains conclusion-bearing.
