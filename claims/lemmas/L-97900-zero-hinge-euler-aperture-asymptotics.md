# L-97900 — Zero-hinge Euler apertures and the exact finite-prime asymptotic

Claim ID: `L-97900`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC THEOREM**  
Created: 2026-08-18  
Frozen base: PR #591 at `5c43060fd11e6a3f5d090ee4c74e4a48ca2eb111`  
RH status: **not assumed**

## 1. Signed and unsigned finite-prime states

Let `P` be a finite squarefree product containing `P_61`. Let `K(Y)` be either

1. the logarithmic `5:3` source `Q_*(Y)` of `L-97600`, or
2. its scale-four annulus `A_*(Y)=Q_*(Y)-Q_*(Y/4)` used in `L-97400`.

Define

\[
 F_P^K(X)=\sum_{d\mid P}{\mu(d)\over\sqrt d}K(X/d),
 \qquad
 M_P^K(X)=\sum_{d\mid P}{1\over\sqrt d}K(X/d).
 \tag{L-97900.1}
\]

The first quantity is the zero-hinge signed observation of the literal
completed-parity source; the second is the corresponding unsigned source mass.
For a new prime `p` not dividing `P`, finite divisor switching gives

\[
 \boxed{F_{Pp}^K(X)=F_P^K(X)-p^{-1/2}F_P^K(X/p),}
 \tag{L-97900.2}
\]

\[
 \boxed{M_{Pp}^K(X)=M_P^K(X)+p^{-1/2}M_P^K(X/p).}
 \tag{L-97900.3}
\]

These are the scalar and mass slices of the source-faithful prime-adjoining
recurrence in `L-97700`. No child is replaced by a comparison measure.

## 2. Kernel asymptotics

The positive dictionary

\[
q_*(2)=15,\quad q_*(3)=6,\quad q_*(4)=3,
\quad q_*(m)=6\ (m\ge5)
\]

and elementary integral comparison give

\[
 Q_*(Y)=24\sqrt Y+O(\log Y).
 \tag{L-97900.4}
\]

The directed analytic theorem retained in `L-97400` gives the sharper annular
formula

\[
 A_*(Y)=12\sqrt Y+C_0+O(Y^{-3/2})
 \qquad(Y\to\infty).
 \tag{L-97900.5}
\]

Therefore, for either kernel, there is a constant `a_K>0` such that for every
fixed finite `P`,

\[
 {F_P^K(X)\over\sqrt X}
 \longrightarrow
 a_K\prod_{p\mid P}\left(1-{1\over p}\right),
 \tag{L-97900.6}
\]

\[
 {M_P^K(X)\over\sqrt X}
 \longrightarrow
 a_K\prod_{p\mid P}\left(1+{1\over p}\right).
 \tag{L-97900.7}
\]

For the annular kernel this follows directly by substituting (L-97900.5):

\[
F_P^{A_*}(X)
=12\sqrt X\prod_{p\mid P}(1-p^{-1})
+C_0\prod_{p\mid P}(1-p^{-1/2})+O_P(X^{-3/2}),
\]

and the unsigned formula has every minus replaced by plus. The logarithmic
case follows identically from (L-97900.4), with an `O_P(log X)` remainder.

Consequently

\[
 \boxed{
 {F_P^K(X)\over M_P^K(X)}
 \longrightarrow
 \kappa(P):=
 \prod_{p\mid P}{p-1\over p+1}>0.
 }
 \tag{L-97900.8}
\]

In particular `F_P^K(X)>0` for all sufficiently large `X` when `P` is fixed.

## 3. Scope

This theorem describes the exact asymptotic aperture of every finite future-prime
state. It does not prove positivity uniformly when the installed prime set grows
with `X`. That uniform moving-state problem is the remaining Bellman frontier.
