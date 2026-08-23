# T-104560 — Modular mixed-orbit Laguerre frontier for the fixed-order Xi cascade

Claim ID: `T-104560`  
Status: **UNCONDITIONAL SOURCE REDUCTION + ONE MIXED-MATRIX GATE**  
Created: 2026-08-23  
Depends on: `T-104540`, `T-104550`, `L-104531--L-104533`, `R-104516`  
RH status: **unproved**

## 1. The genuinely direct fixed-order conversion

Let `alpha_3` and `alpha_2` denote the fixed-order line-zero proportions in the normalization of `T-104540`.  At every simple real zero of `Xi'''`, the sign

\[
\Xi'''(t)^2-\Xi''(t)\Xi''''(t)\ge0
\]

is exactly the Rolle-generating orientation for `Xi''`.  If this sign holds on a proportion `q` of the line zeros of `Xi'''`, then

\[
\boxed{\alpha_2\ge(2q-1)\alpha_3.}
\tag{T-104560.1}
\]

In particular, pointwise positivity gives

\[
\boxed{\alpha_2\ge\alpha_3>0.9873.}
\tag{T-104560.2}
\]

Unlike the independently known `alpha_2>0.9584` row, (T-104560.2) would be a genuine use of the third-derivative hypothesis.

## 2. Fully assembled modular source

The exact Jacobi-theta identity of `L-104531` produces positive orbit sources `g_n` with

\[
u^2\Phi(u)=\sum_{n\ge1}g_n(u).
\]

The complete Laguerre profile is the all-ones quadratic form of the mixed matrix

\[
\mathbf T(t)=[\mathcal T_{mn}(t)]_{m,n\ge1}:
\]

\[
\boxed{
\Xi'''(t)^2-\Xi''(t)\Xi''''(t)
=
\sum_{m,n\ge1}\mathcal T_{mn}(t).
}
\tag{T-104560.3}
\]

All independent-frequency product terms and cross terms occur exactly once.

## 3. Exact remaining theorem

The conclusion-facing gate is

```text
MTSG104560 — mixed theta Schur/Gram theorem

For every real t, the complete mixed theta-orbit matrix has nonnegative
all-ones quadratic form.  A sufficient stronger formulation is positivity of
every finite matrix T_N(t), stable under the exponential cutoff exhaustion.
```

Then

\[
\boxed{
\mathrm{MTSG104560}
\Longrightarrow
\mathrm{LAG2XI104550}
\Longrightarrow
\alpha_2\ge\alpha_3>0.9873.
}
\tag{T-104560.4}
\]

This would be an unconditional improvement of the fixed-order `Xi''` line proportion obtained by descending Conrey's `Xi'''` theorem.

## 4. What has been removed

```text
historical alpha_3 normalization ambiguity       CLOSED
proportion-only converse Rolle                    REFUTED
orientation/count algebra                         CLOSED
Xi Fourier source                                 CLOSED
Jacobi modular source typing                      CLOSED
finite-cutoff exhaustion                          CLOSED
compact-height reduction                          CLOSED
orbitwise/diagonal shortcut                       REFUTED
```

The sole remaining issue is simultaneous mixed-orbit sign.

## 5. Two exact attack lanes

### A. Modular Gram lane

Use the even theta mother

\[
\mathcal A(u)=e^{u/2}\vartheta(e^{2u})
\]

and the identity

\[
\Phi={1\over4}(D^2-1/4)\mathcal A
\]

to integrate the complete, untruncated mixed kernel by parts before separating theta orbits.  The target is a coefficient-one Gram or Schur complement for the full matrix.

### B. Cofinal certified-margin lane

For a growing sequence `T_j`, choose `N_j` and prove directed lower margins

\[
\min_{|t|\le T_j}\Lambda_{N_j}(t)
>
C N_j^C e^{-\pi N_j^2}.
\]

The exponential tail theorem then proves the Laguerre sign cofinally.  To imply the asymptotic proportion transfer, the height sequence must cover all sufficiently large line zeros, not merely isolated compact boxes.

## 6. Boundary

```text
T104540 historical exactification              PROVED / IMPORTED
T104550 orientation bridge                     PROVED EXACT
modular theta source and mixed matrix           PROVED EXACT
exponential cutoff tail                         PROVED EXACT
MTSG104560                                      OPEN / RH-BEARING AT FIXED ORDER
alpha_2 >= alpha_3 from alpha_3                  NOT YET ESTABLISHED
Riemann Hypothesis                              UNPROVED
```
