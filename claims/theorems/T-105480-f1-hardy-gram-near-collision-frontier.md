# T-105480 — Corrected F1 Hardy–Gram and signed near-collision frontier

Claim ID: `T-105480`

Status: **MAJOR UNCONDITIONAL HILBERT COMPRESSION; ONE SIGNED OFF-DIAGONAL ESTIMATE OPEN**

Corrected: 2026-08-26

Let

\[
\delta_m=\Delta_2W(m)=H_K(m+)/4.
\]

Define

```text
F1GRAM105480:
  sum_(M<=m<=2M) |delta_m|^2/m = M^(o(1)).
```

Weighted Cauchy gives

\[
\mathrm{F1GRAM}_{105480}
\Longrightarrow
\mathrm{F1HARDY}_{105470}.
\tag{T-105480.1}
\]

The continuous logarithmic \(L^2\) norm of the bounded current is uniformly
equivalent to this discrete square modulo the subpower endpoint-jump square.

## Exact positive Gram

\[
\sum_{m=M}^{2M}\frac{|\delta_m|^2}{m}
=
\sum_{n,r}a_n\overline{a_r}G_M(n,r),
\]

where

\[
G_M(n,r)
=
\frac1{16}\sum_{m=M}^{2M}
\frac{K_L(m/n)K_L(m/r)}m.
\tag{T-105480.2}
\]

The Gram is positive semidefinite and vanishes unless \(1/8<n/r<8\).
Its diagonal is subpower. Therefore, for

\[
\mathcal N_M
=
\sum_{n\ne r}a_n\overline{a_r}G_M(n,r),
\]

\[
\boxed{
\mathrm{F1HCNC}_{105481}:
\quad(\mathcal N_M)_+=M^{o(1)}
}
\]

is equivalent to `F1GRAM105480`.

The source-blind linear-loss counterexample `R-105480` remains binding.

## Corrected spectral coordinate

Historical `L-105483` used a nondecaying unregularized weight and is withdrawn.
The correct bounded-current weight is

\[
\Omega_K(t)=|\widehat K_L(\tfrac14+it)|^2
\asymp(1+t^2)^{-1}.
\]

`L-105492--L-105493` prove

\[
\boxed{
\mathrm{F1KFOURTH}_{105493}
\Longrightarrow
\mathrm{F1KASQ}_{105492}
\Longleftrightarrow
\mathrm{F1GRAM}_{105480}
\Longleftrightarrow
\mathrm{F1HCNC}_{105481}.
}
\tag{T-105480.3}
\]

The old IDs `F1ASQ2_105483` and `F1FOURTH105483` are retired.

## Current chain

\[
\boxed{
\mathrm{F1HCNC}_{105481}
\Longleftrightarrow
\mathrm{F1GRAM}_{105480}
\Longrightarrow
\mathrm{F1HARDY}_{105470}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-105480.4}
\]

Reflection variation is a separate stronger sufficient entry through the
stable bridge of `T-105490`; it is not equivalent to the bounded Gram.

```text
Hardy l1 from weighted square                     PROVED
continuous/discrete bounded-current L2            PROVED
positive ratio-eight Gram                         PROVED EXACT
diagonal Gram                                     PROVED SUBPOWER
Gram = positive signed off-diagonal               PROVED EXACT
bounded Mellin-Plancherel                         PROVED EXACT
old unregularized analytic-square L2              REFUTED / INFINITE
correct positive Omega_K                          PROVED EXACT
correct Beta fourth moment -> F1 Gram              PROVED
source-blind Gram closure                         REFUTED LINEARLY

F1KFOURTH105493 / F1KASQ105492                    OPEN / RH-BEARING
F1HCNC105481 / F1GRAM105480                       OPEN / RH-BEARING
F1HARDY105470                                     OPEN / RH-BEARING
Riemann Hypothesis                                UNPROVED
```
