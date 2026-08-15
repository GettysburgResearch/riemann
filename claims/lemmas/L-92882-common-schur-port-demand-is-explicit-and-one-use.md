# L-92882 — The common Schur-port demand is explicit and one use

Claim ID: `L-92882`
Status: **PROVED POSITIVE-SEMIDEFINITE AGGREGATION ON THE FROZEN P61/67 PORT INPUT**
Created: 2026-08-15
Primary inputs: `L-91320`, `L-91725`, `L-91842`
RH status: **unproved**

## 1. Branch demand and available port

For each actual rough branch `b` with rough prime `p_b>=67`, let

\[
\tau_{p_b}=p_b^{-1/2}(1-p_b^{-1/2}).
\]

Let `V_b>=0` be its diagonal projective variance and let

\[
M_b=
\begin{pmatrix}
V_b&B_b\\
B_b&V_b
\end{pmatrix}
\]

be the available two-channel endpoint port. The frozen `P_61/67` Schur estimate gives

\[
M_b\succeq\frac19V_bI_2.
\]

Since `p_b>=67`,

\[
\tau_{p_b}<\frac19.
\]

Therefore the complete branch correction demand

\[
D_b=\tau_{p_b}V_bI_2
\]

satisfies

\[
\boxed{D_b\preceq M_b.}
\tag{L-92882.1}
\]

## 2. Aggregate post-Hall demand

Let `beta_X(b)>=0` be the actual post-Hall, post-thinning branch weight. Define

\[
D_X^{\rm port}
=
\int\sum_b\beta_X(b)D_b,
\]

\[
P_X^{\rm port}
=
\int\sum_b\beta_X(b)M_b.
\]

Positive integration of (L-92882.1) gives

\[
\boxed{
D_X^{\rm port}\preceq P_X^{\rm port}.
}
\tag{L-92882.2}
\]

This instantiates the complete demand; it is not an abstract statement with an unnamed `D_s`.

## 3. Ownership and native cost

The aggregate port is current-owned and source-disjoint from every recursive child. It is a direct boundary summand and has zero ordinary/detail response, hence zero `Y_4` pairing.

The preferred PR #488 one-shot route specializes both demand and port to zero. The present theorem is the independent portful cross-check.

## 4. Boundary

```text
branch demand                               explicit
branch PSD domination                       exact on frozen P61/67 reserve
aggregate demand                            explicit positive integral
one aggregate owner                         exact
recursive child port copy                   absent
Y4 cost in direct-sum model                 zero
PR #488 one-shot port                       identically zero
Riemann Hypothesis                          unproved
```
