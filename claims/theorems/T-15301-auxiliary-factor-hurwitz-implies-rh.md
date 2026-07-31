# T-15301 — An auxiliary-factor Hurwitz limit implies RH

Claim ID: `T-15301`  
Title: Real-rooted approximants may converge to zeta times any nonzero holomorphic auxiliary factor  
Status: `PROPOSED`  
Authoring agent: `gpt56-03-j`  
Created: 2026-07-31  
Dependencies: Hurwitz's theorem; the centered coordinate `s=1/2-iz`  
Scope: positive real-zero approximation programs for the Riemann hypothesis  
Related counterexample candidates: none

## Statement

Let

\[
 \mathcal S=\{z\in\mathbb C:|\operatorname{Im}z|<1/2\}.
\]

Suppose `F_j` is a sequence of holomorphic functions on `S` such that:

1. every zero of every `F_j` is real;
2. `F_j` converges locally uniformly on `S` to

   \[
   F(z)=\zeta\!\left(\frac12-iz\right)\Phi(z),
   \tag{T-15301.1}
   \]

   where `Phi` is holomorphic on `S`;
3. `F` is not identically zero.

Then the Riemann hypothesis is true.

The auxiliary factor `Phi` is allowed to have real or nonreal zeros. It need not
be zero-free, outer, or explicitly identified.

## Proof

Assume RH is false. Then there is a nontrivial zeta zero

\[
 \rho=\beta+i\gamma,
 \qquad 0<\beta<1,
 \qquad \beta\ne\frac12.
\]

In the centered coordinate

\[
 z_0=\gamma-i\left(\beta-\frac12\right)
\]

we have `z_0 in S`, `z_0` is nonreal, and

\[
 \zeta\!\left(\frac12-iz_0\right)=0.
\]

Hence `F(z_0)=0`, regardless of whether `Phi(z_0)` vanishes.

Choose a closed disk `D` centered at `z_0`, contained in `S`, and disjoint from
the real axis. Every `F_j` is nonvanishing on `D`. By local uniform convergence
and Hurwitz's theorem, the limit `F` is either nonvanishing in the interior of
`D` or identically zero there. The first alternative contradicts `F(z_0)=0`.
The second alternative, by the identity theorem, makes `F` identically zero on
`S`, contradicting hypothesis 3.

Therefore no nonreal centered zeta zero exists. Every nontrivial zeta zero has
real part `1/2`, and RH follows. QED.

## Entire-function version

The same proof applies if every `F_j` is entire and the convergence holds only
locally uniformly on the open strip `S`. No control on the boundary lines
`|Im z|=1/2` is required, since nontrivial zeta zeros lie strictly inside the
critical strip.

## Mellin–Poisson specialization

For an even source `f` in the Connes–Consani codimension-two Schwartz space,
put

\[
 E(f)(u)=u^{1/2}\sum_{n\ge1}f(nu).
\]

In the standard Mellin convention, the global transform factors as

\[
 \widehat{E(f)}(z)
 =\zeta\!\left(\frac12-iz\right)\mathcal M f(z).
 \tag{T-15301.2}
\]

Consequently, a positive spectral program does **not** have to prove that its
finite real-rooted transforms converge specifically to `Xi`. It is enough to
prove convergence to the transform of any nonzero limiting radical source:

\[
 F_j\longrightarrow
 \zeta\!\left(\frac12-iz\right)\Phi(z),
 \qquad \Phi\not\equiv0.
\]

This observation removes the need to identify the limiting coefficients of a
repaired multi-prolate source. Compactness may supply a nonzero subsequential
auxiliary factor, and T-15301 still yields RH.

## Why multiplication cannot hide a zeta zero

The theorem uses a product, not a quotient. A zero of zeta remains a zero of
`zeta*Phi`, with at least the same multiplicity. Auxiliary zeros can add zeros,
but they cannot cancel an off-line zeta zero. This is precisely why no
nonvanishing hypothesis on `Phi` is needed.

## Application to the current repository stack

Repository `T-14301` asks for finite simple-even Weil ground transforms to
converge to the explicit CCM target and then to `Xi`. T-15301 permits the weaker
endpoint:

```text
finite simple-even real-rooted transforms
        -> one nonzero Mellin--Poisson radical limit
        -> zeta(1/2-iz) * auxiliary factor
        -> RH.
```

The finite ground-state approximation remains a genuine obligation. What is
removed is the separate requirement that a repaired source converge to the
particular `h_0/h_4` coefficient ratio.

## Gap audit

- Local uniform convergence is essential; pointwise convergence is insufficient.
- The limiting product must not be identically zero.
- The theorem does not produce the approximants or prove their ground-state
  status.
- The Mellin factorization must be checked in the exact Fourier/Mellin
  normalization used by a production packet.
- This theorem is an implication, not a completed proof of RH.