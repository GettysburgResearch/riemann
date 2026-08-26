# T-105480 — Bounded-detector Hardy–Gram and signed near-collision geometry

Claim ID: `T-105480`

Status: **RETAINED EXACT GENERIC HILBERT COMPRESSION; OLD SOURCE-TO-RH ARROW SUPERSEDED**

Corrected: 2026-08-27

Superseded conclusion disposition: `R-105500`, `T-105500`

Let

\[
\delta_m=\Delta_2W(m)=H_K(m+)/4.
\]

For any finite coefficient sequence, weighted Cauchy gives

\[
\left(\sum_{m=M}^{2M}\frac{|\delta_m|}{m}\right)^2
\le
\left(\sum_{m=M}^{2M}\frac1m\right)
\sum_{m=M}^{2M}\frac{|\delta_m|^2}{m}.
\tag{T-105480.1}
\]

The square has the exact positive-semidefinite Gram expansion

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

The Gram vanishes unless \(1/8<n/r<8\).  Whenever the source diagonal is
subpower, the weighted square is subpower if and only if the positive part of
its signed distinct-product off-diagonal is subpower.

The source-blind linear-loss counterexample `R-105480` remains binding: no
coefficient-energy, Schur, or generic Hodge estimate proves that off-diagonal
condition.

## Corrected spectral coordinate

The historical nondecaying unregularized weight is withdrawn.  The exact
bounded-current Plancherel weight satisfies

\[
\Omega_K(t)=|\widehat K_L(\tfrac14+it)|^2
\asymp(1+t^2)^{-1}.
\]

At a fixed source,

\[
\mathrm{F1KFOURTH}_{105493}
\Longrightarrow
\mathrm{F1KASQ}_{105492}
\Longleftrightarrow
\mathrm{F1GRAM}_{105480}
\Longleftrightarrow
\mathrm{F1HCNC}_{105481}.
\tag{T-105480.3}
\]

These are Hilbert-space/source identities and implications.  They do not by
themselves identify the source with an RH detector.

## Binding source correction

The previous terminal chain ending in RH cited the withdrawn completed-source
`QPTI/BCI/HMO` bridge.  Corrected PR #719 proves `QPTI103112` false.  The
balanced coefficient \(b_U\) is distinct and is not refuted by that fixed-core
semiprime calculation, but a fresh conclusion theorem is required.

The independent native-source F1 frontier is `NATIVEF1XD105504`, whose exact
cell form is `NATIVECELL105504`.

```text
Hardy l1 from weighted square                     PROVED
continuous/discrete bounded-current L2            PROVED
positive ratio-eight Gram                         PROVED EXACT
diagonal/off-diagonal identity                    PROVED EXACT
bounded Mellin-Plancherel                         PROVED EXACT
old unregularized analytic-square L2              REFUTED / INFINITE
correct positive Omega_K                          PROVED EXACT
source-blind Gram closure                         REFUTED LINEARLY
old F1HCNC/F1GRAM -> RH arrow                      WITHDRAWN

F1KFOURTH/F1KASQ/F1HCNC on b_U                    OPEN SOURCE ESTIMATES
NATIVEF1XD105504 / NATIVECELL105504               OPEN / RH-EQUIVALENT
Riemann Hypothesis                                UNPROVED
```
