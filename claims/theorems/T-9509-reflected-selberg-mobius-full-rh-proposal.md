# T-9509 — Full RH proposal by reflected Selberg–Möbius contraction

Claim ID: `T-9509`  
Title: A reflected Selberg square and high-order Möbius boundary recombination force the rightmost-zero exponent to vanish  
Status: **FULL PROPOSED PROOF PENDING ADVERSARIAL REVIEW — `L-9517.5` IS THE DECISIVE HINGE; RH IS NOT YET CLAIMED AS VERIFIED**  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: `L-9516`, `L-9517`; `L-15151`, `L-15155`--`L-15159`; `L-23201`--`L-23204`; `T-15122`, `T-9506`  
Scope: complete proposed proof architecture with one explicit finite-combinatorial review hinge

## 1. Rightmost-zero front door

For every fixed order `K`, let
\[
H_K=H^{[K+1]}
\]
be the compact high-order safe window. Its bilateral Laplace transform has the
required vertical decay, vanishes to high order at the two boundary models, and
is nonzero throughout the open counterexample strip.

Let
\[
Q_K(x)
=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 H_K(x-\log n)
\]
and
\[
\mathcal B_{J,K}
=\int_J^{J+1}|Q_K(x)|^2dx.
\]
The safe-filter Hardy transfer gives
\[
\boxed{
\limsup_{J\to\infty}
\frac{\log(1+\mathcal B_{J,K})}{2J}
=\Theta_\zeta,
}
\tag{T-9509.1}
\]
where
\[
\Theta_\zeta
=\sup_{\zeta(\rho)=0}
\left(\Re\rho-\frac12\right).
\]
Thus a bound on the block exponent tending to zero with `K` proves RH.

## 2. Exact Hermitian Selberg square

The scalar Selberg equation produces a non-Hermitian square `H(z)^2`, which is
not enough for the vertical Hardy energy. `L-9516` resolves this mismatch.

Apply Selberg's coefficient identity to
\[
\zeta(s+it),\qquad
\zeta(s-it),\qquad
\zeta(s+it)\zeta(s-it),
\]
and subtract the first two identities from the third. One obtains exactly
\[
\boxed{
2\,\Lambda_t*\Lambda_{-t}
=
C_\times-C_t-C_{-t}.
}
\tag{T-9509.2}
\]
On a real vertical line, the left side is
\[
2\left|\frac{\zeta'}\zeta(s+it)\right|^2.
\]
After multiplication by
\[
|\widehat H_K(\alpha+it)|^2
\]
and integration in `t`, (T-9509.2) is the exact positive energy
`mathcal B_(J,K)` in product-scale coordinates. Compact support of `H_K` makes
the forcing a finite-ratio arithmetic packet.

## 3. Exact finite inverse packet

The reciprocal of the product zeta function has coefficients
\[
\sum_{de=n}\mu(d)\mu(e)(d/e)^{-it}.
\]
For endpoint
\[
X=e^{J+O_K(1)},
\qquad
V=\lceil X^{1/K}\rceil,
\]
apply the exact finite Möbius resolvent separately to both inverse factors:
\[
\mu(n)
=\sum_{r=0}^{K-1}
(\mu_V*r_V^{*r})(n)
\qquad(n\le X).
\tag{T-9509.3}
\]
There is no analytic remainder below the endpoint. This produces one finite,
source-bound, doubly reflected packet carrying the actual Möbius signs.

Use the fixed-reserve first-crossing partition and recombine equal destinations
before any norm. Balanced rows route to scale
\[
\le(1-\delta)J+O_K(1)
\]
for one fixed `delta>0`; reduced rows form a finite complexity DAG. The exact
induction of `L-23203` leaves only the signed terminal family.

## 4. Proposed terminal closure

Invoke `L-9517`.

The high-order safe window is piecewise linear, so the reflected block kernel is
piecewise cubic, while the null quotient annihilates every polynomial and
pole-model density through degree `K`. Abel summation of the **complete signed
terminal family**, first in the long factor and then in its reflected partner,
removes every bulk row. The surviving Hermitian diagonal is absorbed by
(T-9509.2). The only remaining rows are strict lower-scale terms and endpoint
faces with at most `C_*` free divisor coordinates, where `C_*` is absolute.

Since each free endpoint coordinate is at most
\[
V^{1+o(1)}
=\exp\{(1/K+o_K(1))J\},
\]
the terminal forcing obeys
\[
\boxed{
T_K(J)
\le
\exp\left\{
\left(\frac{C_*}{K}+o_K(1)\right)J
\right\}
\left[
1+\max_{u\le(1-\delta)J+O_K(1)}M_K(u)
\right].
}
\tag{T-9509.4}
\]

This is the explicit `STC(K)` rate
\[
\eta_K\le C_*/K.
\]

## 5. Scale contraction

Substitute (T-9509.4) into the finite auxiliary-energy recurrence. The
scale-contraction theorem gives
\[
2\Theta_\zeta
\le
\frac{C_*}{K\delta}.
\tag{T-9509.5}
\]
This holds for every sufficiently large fixed `K`. Letting `K` tend to infinity,
\[
\Theta_\zeta=0.
\]
Functional-equation symmetry yields
\[
\boxed{\mathrm{RH}.}
\tag{T-9509.6}
\]

## 6. Independent scalar audit

The proposal cannot close by deleting the coherent first Farey cell. Under the
fixed-logarithm `q_0=2` mutation, the terminal packet reduces to
\[
G_K(D)=\Delta_{2/3}^{K}M(D).
\]
`L-9517` gives
\[
G_K(D)
=O_{K,\varepsilon}
\left(D^{1/2+C_*/(2K)+\varepsilon}\right).
\]
The exact finite inversion
\[
M(D)=
\sum_{j\ge0}{K+j-1\choose j}
G_K((2/3)^jD)
\]
then gives the same exponent for `M(D)`. Given any `epsilon>0`, choose fixed
`K>C_*/epsilon`. This yields
\[
M(D)=O_\varepsilon(D^{1/2+\varepsilon}),
\]
the classical Mertens criterion for RH.

Thus the prime Hardy route and the direct Möbius route reach RH independently
from the same boundary-recombination estimate.

## 7. Why the proposal is stronger than the previous terminal schema

The earlier `STC(K)` proposal specified a positive exponential majorant but did
not produce the Hermitian vertical square or the vanishing coefficient rate.
The present proposal adds:

1. the exact reflected Selberg identity `L-9516`;
2. a finite product-zeta forcing with two explicit Möbius inverses;
3. exact double resolvent expansion through the output endpoint;
4. a source-specific null-quotient boundary recombination;
5. the explicit rate `eta_K<=C_*/K`;
6. the first-cell Mertens mutation as a mandatory independent audit.

No arbitrary-vector Farey norm, entrywise absolute value, finite numerical
ladder, or density-one support statement is used.

## 8. Decisive adversarial review target

The proof is accepted only if the complete packet enumeration confirms
\[
\boxed{
\#\{\text{free endpoint divisor coordinates on every recombined terminal face}\}
\le C_*
}
\tag{T-9509.7}
\]
with `C_*` independent of `K`.

A reviewer should attempt to construct a terminal face with `Omega(K)` free
coordinates. Such a face would replace `C_*/K` by a nonvanishing exponent and
break the proof. The following must also be checked explicitly:

- all interior rows lie in the high-order null quotient;
- every same-scale nonnull row lowers complexity;
- all reflected cross terms are absorbed by (T-9509.2);
- transition surfaces are included;
- the first-cell mutation reproduces the claimed Mertens exponent.

## 9. Exact status

```text
reflected Selberg Hermitian identity             PROPOSED EXACT
finite double Möbius resolvent                    PROPOSED EXACT
fixed-reserve packet and complexity reduction    PROPOSED EXACT
null-quotient terminal boundary recombination    PROPOSED NEW HINGE
endpoint exponent C_*/K                           PROPOSED PENDING ENUMERATION
conditional completion to RH                     COMPLETE
independently verified proof of RH                NO
```

This is a full proof proposal suitable for immediate adversarial review. It is
not represented as an accepted proof until (T-9509.7) survives the complete
terminal enumeration.
