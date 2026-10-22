# T-23812 — Weighted shell-tail stability is equivalent to RH

Claim ID: `T-23812`  
Title: The dyadic weighted shell remainder is not merely sufficient; under the standard Chebyshev consequence of RH it is polylogarithmic  
Status: **PROPOSED COMPLETE EQUIVALENCE THEOREM — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23823`--`L-23826`, `T-23811`; the classical RH estimate for the Chebyshev function  
Scope: exact status boundary for the consolidated proposal; this file does not prove `WSTS` or RH

## 1. Weighted shell-tail stability

Let

\[
\vartheta(x)=\sum_{p\le x}\log p.
\tag{T-23812.1}
\]

For an integer endpoint `X`, put

\[
Y=\lfloor X/2\rfloor,
\qquad c=Y/X,
\tag{T-23812.2}
\]

and let `s_(X,Y)(p)` be the finite parabolic shell residual of `L-23825`.
Define

\[
\boxed{
\mathcal B_X
=
\max_{2\le z\le X}
\left[
\sum_{z\le p\le X}(\log p)s_{X,Y}(p)
\right]_+.
}
\tag{T-23812.3}
\]

The **Weighted Shell-Tail Stability theorem**, `WSTS`, is

\[
\boxed{
\mathcal B_X=O_\varepsilon(X^\varepsilon)
\quad\text{for every }\varepsilon>0.
}
\tag{T-23812.4}
\]

`T-23811` proves

\[
\mathrm{WSTS}\Longrightarrow\mathrm{RH}.
\tag{T-23812.5}
\]

The purpose of this theorem is to prove the converse and therefore identify the
exact logical strength of the remaining review hinge.

## 2. Exact prime-sampling remainder

`L-23825` gives

\[
\sum_{z\le p\le X}(\log p)s_{X,Y}(p)
=
\sqrt X\,H_c(z/X)
+
\mathcal E_{X,Y}(z)
+
O((1+\log X)^2),
\tag{T-23812.6}
\]

where

\[
H_c(\theta)\le0
\tag{T-23812.7}
\]

and

\[
\boxed{
\mathcal E_{X,Y}(z)
=
X^{-1/2}
\int_{[z,X]}
E_c(t/X)\,d[\vartheta(t)-t].
}
\tag{T-23812.8}
\]

Thus the positive shell charge is bounded by the positive part of one
source-specific Chebyshev sampling remainder.

## 3. Elementary profile bounds

There is an absolute constant `C` such that, uniformly for

\[
0<u\le1
\]

and uniformly for

\[
1/3\le c\le2/3,
\]

one has

\[
\boxed{
|E_c(u)|
\le
C u^{-1/2}[1+\log(1/u)],
}
\tag{T-23812.9}
\]

and, away from the reciprocal knots where the one-sided derivatives are used,

\[
\boxed{
|E_c'(u)|
\le
C u^{-3/2}[1+\log(1/u)].
}
\tag{T-23812.10}
\]

### Proof

On the reciprocal cell `1/(N+1)<u<=1/N`, the exact formula is

\[
E(u)
=u^{-1/2}
\left[A_N+(S_N+1)\log u+4S_N\right]-4N,
\tag{T-23812.11}
\]

where

\[
S_N=\sum_{k\le N}k^{-1/2},
\qquad
A_N=\sum_{k\le N}k^{-1/2}\log k.
\]

The elementary sum-integral estimates

\[
S_N=2\sqrt N+O(1),
\tag{T-23812.12}
\]

\[
A_N=2\sqrt N\log N-4\sqrt N+O(1)
\tag{T-23812.13}
\]

are uniform.  Writing `Nu=1+O(1/N)` in (T-23812.11) cancels the terms of size
`N` and gives (T-23812.9).  Differentiating the exact cell formula leaves a
bracket of size `O(1+log N)`, which gives (T-23812.10).  The shell profile is a
fixed-ratio difference of two such profiles, so the same bounds hold uniformly
for `c` in the displayed compact interval.

The reciprocal entering term is zero; hence `E_c` is continuous and the
piecewise integration by parts below has no hidden atomic boundary term.

## 4. RH gives a polylogarithmic remainder

Assume RH.  The classical von Koch consequence is

\[
\boxed{
\vartheta(t)-t
=O\!\left(t^{1/2}\log^2(2t)\right).
}
\tag{T-23812.14}
\]

Put

\[
R(t)=\vartheta(t)-t.
\]

Apply Stieltjes integration by parts to (T-23812.8), separately across the
finitely many reciprocal knots and the shell cutoff.  The endpoint at `X`
vanishes because `E_c(1)=0`.  Equations (T-23812.9) and (T-23812.14) give,
uniformly in `2<=z<=X`,

\[
X^{-1/2}|E_c(z/X)R(z)|
\ll (1+\log X)^3.
\tag{T-23812.15}
\]

For the integral term, (T-23812.10) and (T-23812.14) give

\[
\begin{aligned}
&X^{-1/2}
\int_z^X
|R(t)|\,X^{-1}|E_c'(t/X)|dt\\
&\qquad\ll
\int_2^X
\frac{\log^2(2t)[1+\log(X/t)]}{t}\,dt\\
&\qquad\ll(1+\log X)^4.
\end{aligned}
\tag{T-23812.16}
\]

Therefore

\[
\boxed{
\sup_{2\le z\le X}
|\mathcal E_{X,Y}(z)|
\ll(1+\log X)^4.
}
\tag{T-23812.17}
\]

Substitution into (T-23812.6), using `H_c<=0`, gives

\[
\boxed{
\mathcal B_X\ll(1+\log X)^4.
}
\tag{T-23812.18}
\]

In particular RH implies `WSTS`.

The harmless use of `Y=floor(X/2)` instead of `X/2` keeps `c` in `[1/3,2/3]`
and changes only the already displayed endpoint/floor ledger.

## 5. Equivalence

Combining (T-23812.5) and (T-23812.18),

\[
\boxed{
\mathrm{RH}
\iff
\mathrm{WSTS}.
}
\tag{T-23812.19}

More explicitly,

\[
\boxed{
\mathrm{RH}
\iff
\mathcal B_X=O_\varepsilon(X^\varepsilon)
\quad\text{for every }\varepsilon>0.
}
\tag{T-23812.20}

Under RH the stronger polylogarithmic bound (T-23812.18) holds.

## 6. Interpretation

The equivalence has two consequences for review.

First, `WSTS` is not routine discretization cleanup.  It is the complete
RH-bearing arithmetic statement after the following components have been
removed exactly:

```text
continuum parabolic geometry;
fixed-ratio density drift;
carry-floor error;
finite weighted transport geometry;
proper prime-power tail;
physical nonnegativity.
```

Second, it is still a materially useful formulation.  It is one one-sided
maximum of one explicitly written Stieltjes remainder, with a quantitative
negative continuum moat.  A proposed proof can therefore be accepted or
rejected at one source-specific scalar interface rather than through a generic
balanced Type-II, Green-energy, face-rank, or Carry-Saturation theorem.

## 7. Proof boundary

Closed here, subject to review of the standard imported Chebyshev estimate:

1. elementary profile and derivative bounds;
2. `RH -> WSTS` with an explicit polylogarithmic envelope;
3. exact equivalence of `WSTS` and RH when composed with `T-23811`.

Not proved:

1. `WSTS` unconditionally;
2. RH.
