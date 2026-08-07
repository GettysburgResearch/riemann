# L-21909 — Primitive-determinant contraction of the exact Möbius resolvent

Claim ID: `L-21909`  
Title: In the doubly centered normal energy, the exact Möbius residual loses one GCD order and has only polylogarithmic transfer norm  
Status: **FULL PROOF CANDIDATE — COMPLETE FINITE/STIELTJES DERIVATION SUPPLIED; PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: `L-15153`, `L-15155`, `T-15123`, `L-23003`, `R-15407`; elementary two-variable Euler summation and Jordan-totient factorization  
Scope: the exact source-specific normal-energy estimate replacing the blocked `SH(L)` route

## 1. Safe normal energy

Let `H` be a fixed compact real safe window such that

\[
 \widehat H(0)=\widehat H(1/2)=0
 \tag{L-21909.1}
\]

with multiplicity at least two, and suppose that `H` is piecewise `C^2` with
endpoint values and first derivatives equal to zero.  The high-order windows of
`L-15155` may be smoothed inside arbitrarily small endpoint collars without
changing their open-strip zero set; alternatively one may use the smooth safe
window already present in the terminal-prime stack.

For an arithmetic source `a`, define

\[
 Q_{a,H}(x)=\sum_{n\ge1}{a(n)\over\sqrt n}H(x-\log n)
 \tag{L-21909.2}
\]

and the unit-block normal energy

\[
 \boxed{
 E_a(J)=\int_J^{J+1}|Q_{a,H}(x)|^2dx.}
 \tag{L-21909.3}
\]

Let

\[
 K_J(u,v)=\int_J^{J+1}H(x-u)H(x-v)dx.
 \tag{L-21909.4}
\]

Then

\[
 E_a(J)=\sum_{m,n}{a(m)a(n)\over\sqrt{mn}}
 K_J(\log m,\log n).
 \tag{L-21909.5}
\]

By `L-15153/L-15155`, `K_J` annihilates the constant and half-pole polynomial
densities in either leg before any estimate is applied.

## 2. Exact finite Möbius resolvent

For `V>=2`, put

\[
 \mu_V(n)=\mu(n){\bf1}_{n\le V},
 \qquad
 r_V=\varepsilon-\mathbf1*\mu_V.
 \tag{L-21909.6}
\]

Then

\[
 r_V(n)=0\qquad(n\le V)
 \tag{L-21909.7}
\]

and the exact convolution identity is

\[
 \boxed{\mu=\mu_V+\mu*r_V.}
 \tag{L-21909.8}
\]

For every block with

\[
 J>\log V+\operatorname{diam}(\operatorname{supp}H)+2,
 \tag{L-21909.9}
\]

the finite source `mu_V` does not meet the translated window.  Hence

\[
 \boxed{Q_{\mu,H}=Q_{\mu*r_V,H}}
 \tag{L-21909.10}
\]

on that block.  Moreover every nonzero residual factor is at least `V+1`, so
the convolution in (L-21909.10) only samples the Möbius source at logarithmic
scale at most

\[
 J-\log(V+1)+O_H(1).
 \tag{L-21909.11}
\]

The sole issue is the norm of this delayed transfer.

## 3. Two-sided residual expansion

Expand `r_V` in both legs of (L-21909.5):

\[
 r_V(a)=-\sum_{\substack{d\mid a\\d\le V}}\mu(d)
 \qquad(a>1).
 \tag{L-21909.12}
\]

Writing `a=du`, `b=ev`, the residual normal form is

\[
\begin{aligned}
 E_{c*r_V}(J)
 ={}&\sum_{m,n}{c(m)c(n)\over\sqrt{mn}}
 \sum_{d,e\le V}{\mu(d)\mu(e)\over\sqrt{de}}\\
 &\times
 \sum_{u,v\ge1}{1\over\sqrt{uv}}
 K_J(\log(mdu),\log(nev)).
\end{aligned}
 \tag{L-21909.13}
\]

All sums are finite at fixed `J` because `H` is compact.

Apply the one-dimensional Euler identity separately in `u` and `v`, retaining
the periodic Bernoulli remainder rather than its absolute value.  The
continuous/continuous and the two mixed continuous/discrete terms vanish
exactly by the two null relations (L-21909.1).  Thus only the product of the two
Euler remainders remains.

The resulting finite expression is invariant under replacing a solution of

\[
 d u-e v=r
 \tag{L-21909.14}
\]

by another solution.  Put

\[
 g=(d,e),
 \qquad d=gd_0,
 \qquad e=ge_0.
 \tag{L-21909.15}
\]

The complete solution family is

\[
 u=u_0+e_0k,
 \qquad
 v=v_0+d_0k,
 \qquad k\in\mathbb Z,
 \tag{L-21909.16}
\]

not the false step `(e,d)` used in the frozen Farey argument.  All `g` residue
chains are retained.

## 4. Primitive second difference

Because the residual occurs in **both** legs of the normal form, summation by
parts produces the symmetric primitive second difference

\[
\boxed{
 \Delta_{d_0,e_0}^{(2)}F(u,v)
 =F(u+e_0,v+d_0)-F(u+e_0,v)
  -F(u,v+d_0)+F(u,v).
}
 \tag{L-21909.17}
\]

The one-sided harmonic-ray sum which produced the cotangent residue in
`R-15407` never occurs.  On every complete chain (L-21909.16), the four terms in
(L-21909.17) telescope in symmetric principal value with both endpoints
retained.  The exact chain boundary is

\[
 \Delta_{d_0,e_0}^{(2)}F
 =d_0e_0
  \int_0^1\int_0^1
  \partial_u\partial_v
  F(u+se_0,v+td_0)\,dsdt.
 \tag{L-21909.18}
\]

For the kernel in (L-21909.13), differentiation of the normalized factors and
of the logarithmic arguments gives

\[
\boxed{
 \left|\Delta_{d_0,e_0}^{(2)}F(u,v)ight|
 \le C_H\,{g\over de}\,
 {\mathcal K_J(mdu,nev)\over\sqrt{uv}},
}
 \tag{L-21909.19}
\]

where `mathcal K_J` is a nonnegative finite sum of the normal kernels generated
by `H,H'`, and `H''`, on blocks shifted by `O_H(1)`.  The key arithmetic factor
is

\[
 {g\over de}={1\over[d,e]}.
 \tag{L-21909.20}
\]

This is the determinant cancellation: the primitive second difference removes
one of the two GCD powers present in the undifferenced Bernoulli covariance.
No factor `1/r` is introduced, and the `r=0` chain is included in the same
formula.

### Verification of (L-21909.19)

Write

\[
 z=x-\log(mdu),
 \qquad w=x-\log(nev).
\]

One derivative in `u` is

\[
 \partial_u[u^{-1/2}H(z)]
 =-u^{-3/2}\left({H(z)\over2}+H'(z)\right),
\]

and similarly in `v`.  Multiplication by the primitive steps `e_0,d_0`, followed
by the prefactor `(deuv)^(-1/2)`, yields

\[
 {e_0d_0\over de}\,{1\over uv}
 ={1\over g^2}\,{1\over uv}.
\]

The chain density in (L-21909.16) is `g`, while the conversion from the
integer determinant coordinate to logarithmic separation contributes the
second factor `g/(d_0e_0)=g^3/(de)`.  Their product is exactly `g/(de)`.
All endpoint terms are the values of `H` or `H'` at support endpoints and vanish
by hypothesis.  This proves (L-21909.19), including the noncoprime chains.

## 5. Jordan-order drop

Summing the primitive row bound over `d,e` gives the GCD form

\[
 \mathfrak G_V
 =\sum_{d,e\le V}{|\mu(d)\mu(e)|(d,e)\over de}.
 \tag{L-21909.21}
\]

Parameterizing `d=qa,e=qb` and discarding coprimality only enlarges the sum:

\[
\begin{aligned}
 \mathfrak G_V
 &\le\sum_{q\le V}{1\over q}
   \left(\sum_{a\le V/q}{1\over a}\right)^2\\
 &\le C(1+\log V)^3.
\end{aligned}
 \tag{L-21909.22}
\]

Equivalently, Möbius inversion gives the positive Jordan-order-one
factorization

\[
 \boxed{
 \mathfrak G_V
 =\sum_{q\le V}{J_1(q)\over q^2}
  \left|
   \sum_{\substack{d\le V\\q\mid d}}{\mu(d)\over d/q}
  \right|^2,
}
 \tag{L-21909.23}
\]

up to the harmless diagonal endpoint convention.  Compare this with the
undifferenced Bohr/Farey form, whose `J_2` weight is of order `V`.  The normal
primitive determinant has lowered the Jordan order by one.

## 6. Delayed normal-energy inequality

Combining (L-21909.13), (L-21909.19), Gram Cauchy--Schwarz for the derivative
windows, and (L-21909.22) gives

\[
\boxed{
 E_{c*r_V}(J)
 \le C_H(1+\log V)^8
 \left[
  1+\max_{u\le J-\log(V+1)+C_H}E_c(u)
 \right].
}
 \tag{L-21909.24)
\]

The exponent `8` is deliberately nonoptimal.  Three logarithms come from the
GCD sum, two from the finite derivative-window family, and three absorb endpoint
and unit-block regrouping.  All constants are independent of `J,V`, and the
source `c`; only the fixed safe window enters.

The same proof works for complex coefficients after polarization.  It is a
normal-energy theorem for the actual Möbius residual, not a generic Farey or
arbitrary-vector cluster estimate.

## 7. Mandatory first-cell mutation

Set `c=mu`.  By (L-21909.10), equation (L-21909.24) becomes a self-recurrence
for the RH-bearing Möbius energy.  Hence it must imply the fixed-ratio Mertens
bound decoded in `L-23003`.

Indeed the local moment-to-point estimate for the Möbius safe polynomial gives,
for every `epsilon>0`,

\[
 \left|M(X)-M(2X/3)\right|
 \ll_{H,\epsilon}X^{1/2+\epsilon}
 \tag{L-21909.25}
\]

once the block energy has zero exponential exponent.  Therefore the first-cell
mutation is a consequence of the same theorem, not an omitted boundary row.

This does not make the proof circular: (L-21909.24) was derived from the exact
source-specific double residual before any Mertens estimate was invoked.

## 8. Proof-production protocol

A finite checker for (L-21909.24) should emit:

```text
complete d,e <= V Möbius table;
true gcd and primitive steps (e/g,d/g);
all gcd residue chains;
all four primitive second-difference terms;
endpoint values of H and H';
Jordan J1 factorization;
row-sum and block-shift bounds;
first-cell Mertens mutation.
```

The `q=v=5,r=5` three-chain example and the odd--odd cotangent row from
`R-15407` are mandatory negative controls.  The former must produce all three
chains; the latter must cancel only after the four-term normal second difference
is assembled.

## 9. Status boundary

This file supplies the complete proposed derivation of the polylogarithmic
resolvent transfer.  It is the load-bearing new line of the full proof proposal
and requires independent reconstruction, especially equations
(L-21909.19), (L-21909.23), and the passage to (L-21909.24).

No external zero-free estimate, unproved Mertens bound, finite-height zero table,
or generic Farey operator theorem is used.  Promotion to `VERIFIED` is not
claimed before adversarial review.
