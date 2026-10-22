# L-91320 — Reordering the inner factors gives a zero-factor-independent stable port

Claim ID: `L-91320`  
Status: **EXACT MODEL-SPACE IDENTITY; ARITHMETIC SOURCE INTERTWINER REMAINS OPEN**  
Created: 2026-08-12  
Depends on: PR #396 `L-91034`, `L-91313`  
RH status: **unproved**

## 1. Inner factors

Retain

\[
 \Theta_a(z)
 =\frac{\xi(\frac12-a+z)}
        {\xi(\frac12+a+z)},
 \tag{L-91320.1}
\]

its crossed-zero Blaschke factor `B_a`, and the deterministic stable Cauchy
factor

\[
 \Delta_a(z)=b_a(z)^2b_{2a}(z)^2b_{4a}(z)^2.
 \tag{L-91320.2}
\]

Then

\[
 A_a=B_a\Theta_a
 \tag{L-91320.3}
\]

and

\[
 I_a=\Delta_aB_a\Theta_a
 \tag{L-91320.4}
\]

are analytic inner functions in the right half-plane.

For a scalar function `F`, write

\[
 K_F(z,w)=\frac{1-F(z)\overline{F(w)}}{z+\bar w}.
 \tag{L-91320.5}
\]

## 2. Apply the product rule in the useful order

Instead of grouping `I_a=Delta_a(B_a Theta_a)`, group

\[
 I_a=B_a(\Delta_a\Theta_a).
 \tag{L-91320.6}
\]

The product rule gives

\[
 K_{I_a}
 =K_{B_a}
  +B_a\overline{B_a}K_{\Delta_a\Theta_a},
 \tag{L-91320.7}
\]

and

\[
 K_{\Delta_a\Theta_a}
 =K_{\Delta_a}
  +\Delta_a\overline{\Delta_a}K_{\Theta_a}.
 \tag{L-91320.8}
\]

Dividing by
`Delta_a B_a overline(Delta_a B_a)` yields

\[
 \boxed{
 \mathcal K_a^{\rm src}
 =\mathcal K_a^{\rm crit}
  +\mathcal K_a^{\rm st,0}
  +\mathcal K_a^{\rm zero,\Delta},
 }
 \tag{L-91320.9}
\]

where

\[
 \boxed{
 \mathcal K_a^{\rm crit}=K_{\Theta_a},
 }
 \tag{L-91320.10}
\]

\[
 \boxed{
 \mathcal K_a^{\rm st,0}
 =\frac{K_{\Delta_a}}
        {\Delta_a\overline{\Delta_a}},
 }
 \tag{L-91320.11}
\]

and

\[
 \boxed{
 \mathcal K_a^{\rm zero,\Delta}
 =\frac{K_{B_a}}
        {\Delta_a B_a\overline{\Delta_a B_a}}.
 }
 \tag{L-91320.12}
\]

All divisions are scalar congruences on points away from the declared stable
zeros and crossed poles.

## 3. Positivity and interpretation

The source, deterministic stable, and zero-port kernels are positive:

```text
K_(I_a)      inner source model;
K_(Delta_a)  six known stable states;
K_(B_a)      one state per crossed xi pole.
```

Crucially, `K_a^(st,0)` is independent of the unknown zero factor `B_a`.
Every dependence on crossed zeros is confined to the single positive term
`K_a^(zero,Delta)`.

## 4. One-node diagonal

At a positive real node `eta` avoiding the stable zeros,

\[
 \boxed{
 \mathcal K_a^{\rm crit}(\eta,\eta)
 =\frac{1-|\Theta_a(\eta)|^2}{2\eta},
 }
 \tag{L-91320.13}
\]

\[
 \boxed{
 \mathcal K_a^{\rm st,0}(\eta,\eta)
 =\frac{1-|\Delta_a(\eta)|^2}
        {2\eta|\Delta_a(\eta)|^2},
 }
 \tag{L-91320.14}
\]

and

\[
 \boxed{
 \mathcal K_a^{\rm zero,\Delta}(\eta,\eta)
 =\frac{1-|B_a(\eta)|^2}
        {2\eta|\Delta_a(\eta)|^2|B_a(\eta)|^2}.
 }
 \tag{L-91320.15}
\]

The first two quantities are explicit from safe Xi values and the known
rational Cauchy factor. The third is zero exactly when `B_a` is constant.

Thus the RH-expected nonzero-port norm is the completely explicit scalar

\[
 \boxed{
 \mathscr T_a(\eta)
 :=\frac{|\Delta_a(\eta)|^{-2}-|\Theta_a(\eta)|^2}
         {2\eta}.
 }
 \tag{L-91320.16}
\]

The actual source norm is

\[
 \boxed{
 \mathcal K_a^{\rm src}(\eta,\eta)
 =\mathscr T_a(\eta)
  +\mathcal K_a^{\rm zero,\Delta}(\eta,\eta).
 }
 \tag{L-91320.17}
\]

## 5. Correct minimal exhaustion theorem

At any pole-, anchor-, or cocycle-aligned node, the arithmetic theorem should
be stated as follows:

> Construct, from the completed Jordan/Fock source and without using `B_a`, a
> vector whose norm is the model source norm in (L-91320.17), and prove that
> its explicitly constructed critical and deterministic stable outputs already
> have total norm `T_a(eta)`.

The exact isometry then forces the residual norm
`K_a^(zero,Delta)(eta,eta)` to vanish.

Defining the arithmetic source norm to equal `T_a(eta)` would be circular; the
source norm must first be obtained independently from the prime/gamma/theta
construction.

## 6. Advantage over the first ledger

The original grouping on PR #396 placed a factor `|B_a|^{-2}` inside the
stable term. Identity (L-91320.9) proves that this was only a choice of product
order. The corrected grouping provides:

```text
critical output          actual Xi quotient;
stable output            fully deterministic and explicit;
zero output              all and only crossed zeros;
source output             arithmetic identification target.
```

This is the preferred ledger for `ONAE_a/PAAE_a`.
