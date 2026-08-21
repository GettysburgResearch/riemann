# L-9513 — Exact Bohr energy of the truncated Möbius fractional-part packet

Claim ID: `L-9513`  
Title: The full-period square energy has a positive Jordan-totient factorization and critical size `O(D)`  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: elementary Fourier series and Jordan's divisor identity  
Scope: moment route to the analytic totient error  
Related counterexample candidates: none

## Packet

Let

\[
f(t)=\{t\}^2-\frac13
\tag{L-9513.1}
\]

and, for an integer `D>=1`, define the periodic Möbius packet

\[
\boxed{
S_D(x)=\sum_{d<=D}\mu(d)f(x/d).}
\tag{L-9513.2}
\]

Its period divides

\[
L_D=\operatorname{lcm}(1,2,\ldots,D).
\]

Define its Bohr square energy

\[
\mathcal B_D
=\frac1{L_D}\int_0^{L_D}|S_D(x)|^2dx.
\tag{L-9513.3}
\]

## Exact two-denominator covariance

For positive integers `d,e`, put `g=(d,e)`. Then

\[
\boxed{
\frac1{\operatorname{lcm}(d,e)}
\int_0^{\operatorname{lcm}(d,e)}
 f(x/d)f(x/e)dx
=
\frac{g^2}{12de}
+\frac{g^4}{180d^2e^2}.}
\tag{L-9513.4}
\]

### Fourier proof

For `h != 0`, the Fourier coefficient of `{t}^2` is

\[
\boxed{
c_h=\frac{i}{2\pi h}+\frac1{2\pi^2h^2},}
\tag{L-9513.5}
\]

while `c_0=1/3`. Write `d=ga`, `e=gb` with `(a,b)=1`. The zero-frequency
condition in the product is

\[
{h\over d}+{k\over e}=0,
\]

so `h=a ell`, `k=-b ell`. Summing
`c_(a ell)c_(-b ell)` over nonzero integers `ell`, and using

\[
\sum_{ell!=0}\ell^{-2}=\frac{\pi^2}{3},
\qquad
\sum_{ell!=0}\ell^{-4}=\frac{\pi^4}{45},
\]

gives (L-9513.4). The imaginary cross terms cancel between `ell` and `-ell`.

## Positive Jordan factorization

Jordan's identity

\[
n^r=\sum_{q|n}J_r(q)
\tag{L-9513.6}
\]

gives

\[
\boxed{
\begin{aligned}
\mathcal B_D={}&
\frac1{12}\sum_{q<=D}J_2(q)
\left(
 \sum_{\substack{d<=D\\q|d}}\frac{\mu(d)}d
\right)^2\\
&+\frac1{180}\sum_{q<=D}J_4(q)
\left(
 \sum_{\substack{d<=D\\q|d}}\frac{\mu(d)}{d^2}
\right)^2.
\end{aligned}}
\tag{L-9513.7}
\]

Every term on the right is nonnegative. This is an exact Selberg-square
factorization of the complete resonant/Bohr energy.

## Unconditional critical upper bound

One has

\[
\boxed{\mathcal B_D\ll D.}
\tag{L-9513.8}
\]

Indeed,

\[
\left|
\sum_{q|d<=D}\frac{\mu(d)}d
\right|
\le\frac1qH_{\lfloor D/q\rfloor},
\]

and `J_2(q)<=q^2`. Hence the first line of (L-9513.7) is at most

\[
\frac1{12}\sum_{q<=D}H_{\lfloor D/q\rfloor}^2
\ll D,
\]

because `sum_(q<=D)(1+log(D/q))^2=O(D)`.

Similarly,

\[
\left|
\sum_{q|d<=D}\frac{\mu(d)}{d^2}
\right|
\le\frac{\zeta(2)}{q^2},
\]

while `J_4(q)<=q^4`, so the second line is `O(D)`.

Thus the complete periodic packet has root-mean-square size `O(sqrt D)` without
RH.

## Exact blocker exposed

The analytic totient criterion requires moments on physical intervals of length
comparable with the denominator cutoff, not averages over a full common period.
Farey frequencies with denominators `d,e about D` can be separated by only

\[
\left|{h\over d}-{k\over e}\right|\asymp D^{-2},
\]

while an interval of length `D` resolves frequencies only at scale `D^-1`.
The unresolved clusters contain the Möbius cancellation detected by the local
moment criteria.

Therefore:

\[
\boxed{
\text{Bohr/resonant energy is already closed at the critical scale;}
\quad
\text{the local near-resonant Farey block is RH-bearing.}}
\tag{L-9513.9}
\]

A phase-blind large sieve pays `D^2` for the minimum Farey spacing and loses one
full power. A successful proof must exploit the Möbius coefficients and the
coupling to the exact tail before taking absolute values.

## Relation to the all-moments program

`T-9505` asks for local physical moments. `L-9513` proves that the global
resonant component already has the conjectured size at order two. The natural
next theorem is a local-to-Bohr transference with a Möbius-weighted
near-resonance correction bounded at the same scale, followed by its
multilinear extension to unbounded even moments.

## Gap audit

- Formula (L-9513.7) is a theorem for the truncated periodic packet, not the
  complete analytic part.
- A full-period mean does not control a specified interval of length `D`.
- The `O(D)` bound therefore does not imply RH or even a new pointwise zero-free
  half-plane by itself.
- The near-resonant block must not be discarded or replaced by independent
  absolute estimates.
