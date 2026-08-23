# L-105201 — A canonical Bézout correction removes the complete second-derivative residue debt

Claim ID: `L-105201`  
Status: **PROVED EXACT FINITE-POLYNOMIAL THEOREM**  
Created: 2026-08-23  
Depends on: `L-105200`; PR #723 `L-105100`  
RH status: **not assumed**

Let `p` be a real polynomial of degree `n>=3`. Assume that every zero of `p'`
is simple and is not a zero of `p`. Then

\[
\gcd(p',p'')=1.
\]

## 1. Canonical Bézout interpolant

There is a unique polynomial `A_p` of degree less than `deg p''=n-2` such that

\[
\boxed{
A_p(z)p'(z)\equiv p(z)^2\pmod{p''(z)}.
}
\tag{L-105201.1}
\]

Indeed, choose polynomials `U,V` with

\[
Up'+Vp''=1
\]

and take `A_p` to be the remainder of `U p^2` modulo `p''`.

Define

\[
\boxed{
B_p(z)=\frac{p(z)^2-A_p(z)p'(z)}{p''(z)}.
}
\tag{L-105201.2}
\]

Congruence (L-105201.1) makes `B_p` a polynomial. Put

\[
\boxed{
\widetilde Q_p(z)=\frac{B_p(z)}{p'(z)}
=
\frac{p(z)^2-A_p(z)p'(z)}{p'(z)p''(z)}.
}
\tag{L-105201.3}
\]

## 2. Debt-free residue square

Let `c` be a zero of `p'`. Since `p''(c)!=0`,

\[
B_p(c)=\frac{p(c)^2}{p''(c)}.
\]

Therefore

\[
\boxed{
\operatorname{Res}_{z=c}\widetilde Q_p(z)
=\frac{p(c)^2}{p''(c)^2}
=\rho_c^2.
}
\tag{L-105201.4}
\]

The denominator of `widetilde Q_p` is only `p'`. Hence these are its only
finite poles. In particular, no zero of `p''` appears in the residue ledger.

Equivalently,

\[
\widetilde Q_p
=
\frac{p^2}{p'p''}-\frac{A_p}{p''}.
\tag{L-105201.5}
\]

At a simple zero `d` of `p''`, (L-105201.1) gives

\[
A_p(d)=\frac{p(d)^2}{p'(d)},
\]

so

\[
\operatorname{Res}_{z=d}\frac{A_p(z)}{p''(z)}
=\frac{p(d)^2}{p'(d)p'''(d)}
=\tau_d.
\tag{L-105201.6}
\]

Thus the correction in (L-105201.5) cancels the complete cross-residue debt of
`L-105100` and `L-105200` point by point.

## 3. Exact localized second moment

Retain the common localizer and boundary functional of `L-105200`. Since
`widetilde Q_p=O(z^3)` at infinity, the universal localized-residue identity
applies and gives

\[
\boxed{
\sum_{p'(c)=0}
\Omega_{a,T}(c)\rho_c^2
=
\mathfrak B_{a,T}[\widetilde Q_p].
}
\tag{L-105201.7}
\]

This is the debt-free replacement for (L-105200.8).

The equivalent subtraction formula is

\[
\boxed{
\mathfrak B_{a,T}[\widetilde Q_p]
=
\mathfrak B_{a,T}\!\left[\frac{p^2}{p'p''}\right]
-
\mathfrak B_{a,T}\!\left[\frac{A_p}{p''}\right],
}
\tag{L-105201.8}
\]

where the second boundary functional equals

\[
\sum_{p''(d)=0}\Omega_{a,T}(d)\tau_d.
\]

## 4. Complete boundary formula for coherence when the critical points are real

Suppose every zero of `p'` is real. Define

\[
N_{a,T}
=\mathfrak B_{a,T}\!\left[\frac{p''}{p'}\right],
\]

\[
M_{1;a,T}
=-\mathfrak B_{a,T}\!\left[\frac p{p'}\right],
\]

\[
M_{2;a,T}
=\mathfrak B_{a,T}[\widetilde Q_p].
\]

Then these are respectively the localized critical-point count, signed first
residue mass, and positive second residue moment. Consequently

\[
\boxed{
\mathfrak C_{a,T}
=
\frac{
\left[-\mathfrak B_{a,T}[p/p']\right]_+^2
}{
\mathfrak B_{a,T}[p''/p']
\mathfrak B_{a,T}[\widetilde Q_p]
}.
}
\tag{L-105201.9}
\]

If `p` has only simple real roots, every `rho_c<0`, and (L-105201.9) is the
literal smooth residue coherence with no correction term of any kind.

## 5. Interpolation meaning and entire-function frontier

Equation (L-105201.1) says that `A_p` interpolates the values

\[
A_p(d)=\frac{p(d)^2}{p'(d)}
\qquad(p''(d)=0).
\]

For an entire derivative ladder `F_(k-1),F_k,F_(k+1)`, the exact analogue is
to construct an entire function `A_k` satisfying

\[
A_k(d)F_k(d)=F_{k-1}(d)^2
\qquad(F_{k+1}(d)=0)
\]

with growth small enough that

\[
\frac{F_{k-1}^2-A_kF_k}{F_kF_{k+1}}
\]

has a controlled Poisson boundary functional. The finite theorem proves that
this is the correct debt-removal object. Existence with the required Xi growth,
canonical-product exhaustion, and nonreal-critical control remain open.
