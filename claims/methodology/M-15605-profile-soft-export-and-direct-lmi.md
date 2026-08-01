# M-15605 — Profile-soft packet export and direct Suzuki LMI protocol

Claim ID: `M-15605`  
Title: Proof-producing export of `P_R^soft`, complete arithmetic assembly, and PR #191 harmonic residual short  
Status: `PROPOSED PRODUCTION PROTOCOL`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: `L-15630`--`L-15632`; `T-15606`; `L-18512`

## 1. Objective

For each certified support block, emit one finite proof object whose final
quantity is

\[
 \rho_R
 =
 \left\|
 \left[
 G_{S,R}^{-1/2}
 \mathscr D_R^{\rm soft}
 G_{S,R}^{-1/2}
 \right]_{-}
 \right\|.
\]

The cofinal target is `rho_R -> 0`. No selected-zero count, principal angle, or
separate terminal/cross norm is used.

## 2. Support-block inputs

For a dyadic block `[T,2T]`, retain:

```text
exact source-frame map F_R and localized identity L_R F_R = I;
production metric G_R;
actual profile Gram D_R;
complete amplitude/support-derivative Gram K_R;
unwhitened envelope M_T with K_R <= M_T^2 G_R;
all phase, radial, endpoint and exceptional-set ledgers;
complete harmonic metric M_R and line-centered ambient floor constants;
source, normalization and code digests.
```

Compute

```text
a_T   = M_T^2 (log T)^2 / T,
tau_T = M_T / sqrt(T),
Dhat_R = D_R + tau_T G_R.
```

The block may proceed only when `a_T<1` and every directed graph/phase LMI is
strict.

## 3. Support selection before spectral splitting

Apply the complete Hilbert-valued support-average ledger in the fixed block
metric

\[
 \widehat{\mathcal G}_R=\widehat D_R\oplus M_R.
\]

Certify a positive-measure set on which

\[
 \left\|
 \widehat{\mathcal G}_R^{-1/2}
 (\mathcal H_R-\mathcal H_R^0)
 \widehat{\mathcal G}_R^{-1/2}
 \right\|
 \le\varepsilon_T,
\]

with

\[
 \varepsilon_T\le C a_T^{1/4}\log T.
\]

Select one exact or interval support from that set, avoiding every zeta-cycle
length. The soft projector is not used in this selection.

## 4. Directed soft/hard export

At the selected support, solve the generalized Hermitian problem

\[
 D_Rv=\nu G_Rv.
\]

Use two thresholds:

```text
soft-safe threshold       tau_T,
hard-safe threshold       2 tau_T.
```

Every eigenvalue interval wholly below `tau_T` is soft. Every interval wholly
above `2 tau_T` is hard. Every interval meeting the transition band is placed
in the soft packet. Thus the exported rational/interval basis `Q_S` must prove

\[
 Q_S^*D_RQ_S\preceq2\tau_TQ_S^*G_RQ_S,
\]

while the certified hard complement proves

\[
 D_R\succeq\tau_TG_R.
\]

The exporter retains:

```text
basis or Riesz-projector representation;
Gram and orthogonality intervals;
generalized spectral residuals;
transition-band disposition;
soft and hard LMI pivots.
```

No binary64 eigenvector is accepted as a proof object.

## 5. Complete actual Suzuki block

On the exported packet assemble

\[
 B_S=B_S^{\rm arch}+B_S^{\rm local}
     +B_S^{\rm prime}+B_S^{\rm polar}.
\]

Requirements:

1. enumerate every prime power in the exact support;
2. perform the terminal-prime/polar pole cancellation symbolically before
   interval contraction;
3. include all fixed-prefix and same-end terms;
4. evaluate archimedean kernels with directed tails;
5. retain the complete low--harmonic cross `Z_S` and harmonic block `C`;
6. bind an independent zero-side reconstruction for normalization only.

## 6. Line-centered comparator ledger

Construct or bound the artificial line-centered block

\[
 \mathcal H^0_S
 =
 \begin{pmatrix}B_S^0&(Z_S^0)^*\\Z_S^0&C^0\end{pmatrix}.
\]

The certificate proves

\[
 \mathcal H_S^0\succeq0,
\]

\[
 C^0\succeq h_TM,
 \qquad h_T\ge c\log T,
\]

and

\[
 B_S^0\preceq\ell_T\widehat D_S,
 \qquad \ell_T\le C\log T.
\]

It also binds the complete actual-minus-line perturbation endpoint
`epsilon_T`. Separate terminal-prime and harmonic-cross radii are diagnostics,
not the proof gate.

## 7. PR #191 harmonic trial solve

Compute a finite line-centered trial solve `X_T` and the actual residual

\[
 \mathscr R_T=Z_S-CX_T.
\]

Form

\[
\begin{aligned}
 \mathscr D_R^{\rm soft}
 ={}&B_S-Z_S^*X_T-X_T^*Z_S+X_T^*CX_T\\
 &-h_{\rm act}^{-1}
 \mathscr R_T^*M^{-1}\mathscr R_T.
\end{aligned}
\]

The line-centered solve residual, actual solve residual, interval assembly
radius, and all metric transports are preserved independently.

## 8. Final consumers

The proof object has two valid consumers.

### Analytic consumer

Apply `L-15632` and certify

\[
 \rho_R\le
 3\tau_T\left[
 \varepsilon_T\left(1+\frac{\ell_T}{h_T}\right)
 +{\varepsilon_T^2\over h_T-\varepsilon_T}
  \left(1+\sqrt{\frac{\ell_T}{h_T}}\right)^2
 \right]
 +\rho_R^{\rm solve}+\rho_R^{\rm dir}.
\]

### Direct LMI consumer

Prove directly

\[
 \mathscr D_R^{\rm soft}+\rho_RG_{S,R}\succeq0
\]

by directed LDL. The analytic bound remains an independent upper check.

## 9. Cofinal ledger

For block index `j`, retain

```text
T_j, selected R_j, a_(T_j), tau_(T_j),
soft rank, hard rank,
epsilon_j, h_j, ell_j,
line-centered residual,
harmonic residual,
directed assembly radius,
analytic rho upper,
direct LDL rho upper.
```

A valid cofinal sequence requires

```text
T_j -> infinity,
a_(T_j) -> 0,
rho_j -> 0,
all earlier radical/cross/assembly rates -> 0.
```

## 10. Fail-closed rules

- A support interval touching an exceptional length is rejected.
- An unresolved generalized eigenvalue is assigned to the soft packet.
- A missing prime-power row rejects the level.
- Pole and terminal matrices may not be bounded separately before exact
  cancellation.
- A non-strict ambient floor rejects the Schur consumer.
- A line-centered or actual harmonic residual absent from the certificate is
  treated as infinite.
- Positive finite levels are finite evidence only; the cofinal theorem needs
  an unbounded sequence.
