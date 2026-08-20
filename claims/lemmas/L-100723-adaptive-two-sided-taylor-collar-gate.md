# L-100723 — Adaptive left/right Taylor certificates form an exact collar AND gate

Claim ID: `L-100723`  
Status: **PROVED EXACT TWO-CERTIFICATE IMPLICATION; TWO ARITHMETIC ESTIMATES OPEN**  
Created: 2026-08-21  
Depends on: `L-100720--L-100722`; audited joint min--max source on PR #695  
RH status: **not assumed**

Let

\[
H(t)=H_{p,q;\mathcal P}(t),
\qquad
\widetilde H(t)=H(t)-M_{p,q;\mathcal P}(t)
\]

be one literal double-owner cubic interval. Put

\[
\mathcal L(t)
={1\over2}\int_0^t(t-u)^2|\widetilde H'''(u)|du,
\tag{L-100723.1}
\]

\[
\mathcal R(t)
={1\over2}\int_t^\infty(u-t)^2|\widetilde H'''(u)|du.
\tag{L-100723.2}
\]

## 1. Two exact pointwise certificates

At the activation origin,

\[
H(0)=H'(0)=0,
\qquad H''(0)>0.
\]

Taylor's formula from the left gives

\[
H(t)={H''(0)\over2}t^2
+{1\over2}\int_0^t(t-u)^2\widetilde H'''(u)du,
\]

and therefore

\[
\boxed{H(t)_-\le\mathcal L(t).}
\tag{L-100723.3}
\]

The compact centered collar and its first two derivatives vanish at infinity.
Taylor's formula from the right gives

\[
\widetilde H(t)
=-{1\over2}\int_t^\infty(u-t)^2\widetilde H'''(u)du.
\]

Since the removed carrier is nonnegative,

\[
\boxed{H(t)_-\le\mathcal R(t).}
\tag{L-100723.4}
\]

Hence

\[
\boxed{H(t)_-\le\min\{\mathcal L(t),\mathcal R(t)\}.}
\tag{L-100723.5}
\]

This is the stable form of the two-sided certificate. The raw integral of
`mathcal L` over all later scales is not used; `R-100721` proves that such a
charge is false.

## 2. Adaptive source-owned partition

Define the deterministic collar regions

\[
\Omega_{\rm A}
=\{(p,q,\mathcal P,t):\mathcal L(t)\le\mathcal R(t)\},
\]

\[
\Omega_{\rm D}
=\{(p,q,\mathcal P,t):\mathcal R(t)<\mathcal L(t)\}.
\]

These regions are determined by the two exact source packets before the sign of
`H` is observed. They partition every occurrence-time pair exactly once.

For a finite labelled source let

\[
\pi_{ij}=r_ir_jL_iR_j
\]

be the audited joint min--max coefficient. Put

\[
\mathscr A_k(t)
=\sum_{i<j}\pi_{ij}
  \mathbf1_{\Omega_{\rm A}}\mathcal L_{ij}(t),
\tag{L-100723.6}
\]

\[
\mathscr D_k(t)
=\sum_{i<j}\pi_{ij}
  \mathbf1_{\Omega_{\rm D}}\mathcal R_{ij}(t).
\tag{L-100723.7}
\]

Then the joint hazard identity and (L-100723.5) give

\[
\boxed{
(F_k(t^2))_-
\le\mathscr A_k(t)+\mathscr D_k(t).
}
\tag{L-100723.8}
\]

No first-owner or largest-owner marginal is formed, and no inactive Taylor tail
is charged.

## 3. Two complementary terminal statements

Define

\[
\boxed{
\mathrm{APCC100723}(Y):
\quad
\sup_k\int_1^Y\mathscr A_k(\sqrt X){dX\over X}
=Y^{o(1)}
}
\tag{L-100723.9}
\]

and

\[
\boxed{
\mathrm{DPCC100723}(Y):
\quad
\sup_k\int_1^Y\mathscr D_k(\sqrt X){dX\over X}
=Y^{o(1)}.
}
\tag{L-100723.10}

Finite-cutoff exhaustion and the centered-cubic Mellin--Landau theorem give

\[
\boxed{
\mathrm{APCC100723}\ \wedge\ 
\mathrm{DPCC100723}
\Longrightarrow RH.
}
\tag{L-100723.11}

The two inputs are adapted to different exact structures:

```text
APCC:
  activation-origin Taylor packet;
  compensated finite reciprocal prefix;
  first-owner / endpoint-jump tools.

DPCC:
  completed deep carrier;
  future product boundary;
  PR #695 completed-minus-transition coboundary and balanced homotopy.
```

Neither estimate is asserted here. The theorem proves their typed, lossless
composition on one joint min--max ledger.
