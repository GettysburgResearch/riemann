# L-32315 — The matching parity augmented curvature is one four-state Jordan path over a common odd carrier

Claim ID: `L-32315`

Status: **PROPOSED COMPLETE EXACT STATE-COMPRESSION LEMMA — INDEPENDENT REVIEW REQUIRED**

Created: 2026-08-09

Dependencies: `L-32306`; PR #334 `L-32404`; elementary Euler-factor algebra

Scope: exact state realization of the matching parity augmented curvature and exact common-odd-carrier factorization.  It does not prove the missing dissipative recurrence or RH.

## 1. Matching parity systems

Retain

\[
B_+(s)=p(z)\mathcal O(s),
\qquad
B_-(s)=p(-z)\mathcal O(s),
\qquad z=2^{-s},
\]

with

\[
p(z)=(1-z)(1-2z)(1-\sqrt2 z)^2,
\]

and

\[
\mathcal O(s)=\prod_{p\ {m odd}}(1-p^{-s}).
\]

Let

\[
A_\pm=B_\pm^{-1}.
\]

For `tau>=0` define the complete parity Jordan deformations

\[
\boxed{
J_{\pm,\tau}(s)
=\frac{A_\pm(s-\tau)}{A_\pm(s)}.
}
\tag{L-32315.1}
\]

PR #334 proves coefficientwise positivity and identifies the first two jets with the parity generalized-prime/Selberg sequences.

Define the source-convolved paths

\[
\boxed{
K_{\pm,\tau}=b_\pm*J_{\pm,\tau}.
}
\tag{L-32315.2}
\]

## 2. One four-component row path

For one carry row `e=(n,j)`, put

\[
F_{\pm,e}(\tau)
=1+\mathcal L_e(J_{\pm,\tau}),
\]

and

\[
G_{\pm,e}(\tau)
=\mathcal L_e(K_{\pm,\tau}).
\]

The first three jets are exactly

\[
F_{\pm,e}(0)=1,
\quad
F_{\pm,e}'(0)=P_\pm,
\quad
F_{\pm,e}''(0)=S_\pm,
\tag{L-32315.3}
\]

and

\[
G_{\pm,e}(0)=Y_\pm,
\quad
G_{\pm,e}'(0)=Q_\pm,
\quad
G_{\pm,e}''(0)=T_\pm.
\tag{L-32315.4}
\]

Define the four-component path

\[
\boxed{
V_e(\tau)
=
\bigl(
F_{+,e}(\tau),
F_{-,e}(\tau),
G_{+,e}(\tau),
G_{-,e}(\tau)
\bigr).
}
\tag{L-32315.5}
\]

For any Hilbert-valued twice differentiable path use

\[
\mathfrak C(V)
=\|V'(0)\|^2
-\operatorname{Re}\langle V(0),V''(0)\rangle.
\tag{L-32315.6}
\]

Substitution of (L-32315.3)--(L-32315.4) gives

\[
\boxed{
\begin{aligned}
\mathfrak C(V_e)
={}&P_+^2+P_-^2-S_+-S_-\\
&+Q_+^2+Q_-^2-Y_+T_+-Y_-T_-\\
={}&\mathcal A_{\rm pair}(e).
\end{aligned}}
\tag{L-32315.7}
\]

Thus the matching augmented curvature of `L-32306` is not a ledger assembled from unrelated estimates: it is exactly the curvature of one explicit four-state Jordan path.

## 3. Exact common odd-prime carrier

Put

\[
A_{\rm odd}(s)=\mathcal O(s)^{-1}
\]

and define

\[
\boxed{
J_{{\rm odd},\tau}(s)
=\frac{A_{\rm odd}(s-\tau)}{A_{\rm odd}(s)}.
}
\tag{L-32315.8}
\]

Since

\[
A_\pm(s)=\frac{A_{\rm odd}(s)}{p(\pm z)},
\]

and

\[
2^{-(s-\tau)}=2^\tau z,
\]

one gets the exact multiplier factorization

\[
\boxed{
J_{\pm,\tau}(s)
=J_{{\rm odd},\tau}(s)
\frac{p(\pm z)}{p(\pm2^\tau z)}.
}
\tag{L-32315.9}
\]

Thus all odd-prime arithmetic is common to the two parity channels.  The entire distinction between `+` and `-` is one explicit rational 2-adic factor of fixed degree.

## 4. Source-convolved factorization

Define the odd source-convolved path

\[
K_{{\rm odd},\tau}(s)
=\mathcal O(s)J_{{\rm odd},\tau}(s).
\tag{L-32315.10}
\]

Because

\[
B_\pm(s)=p(\pm z)\mathcal O(s),
\]

multiplying (L-32315.9) by `B_+-` gives

\[
\boxed{
K_{\pm,\tau}(s)
=K_{{\rm odd},\tau}(s)
\frac{p(\pm z)^2}{p(\pm2^\tau z)}.
}
\tag{L-32315.11}
\]

Hence both source legs are also one common odd-prime path with fixed-complexity rational two-adic dressing.

Equations (L-32315.9) and (L-32315.11) are identities of Dirichlet multipliers; coefficientwise they are interpreted through the corresponding finite local Euler expansions.

## 5. Consequence for the closing recurrence

The current live composition already proves:

```text
compact Q4 current
 -> exact parity two-jet frame       PR #346 L-34402;

parity current+bare jet
 -> one A_pair curvature state       L-32306;

A_pair
 = curvature of V_e                  this lemma;

all parity arithmetic
 = one odd carrier + finite 2-adic state this lemma;

all extra compact first/second-jet gauges
 = strict predecessor states         PR #346 L-34405.
```

Therefore the remaining dissipative theorem can be posed on a fixed-complexity state:

> propagate the four-state path `V_e` (equivalently the common odd carrier plus its finite 2-adic dressing) through one logarithmic scale step, and prove that its curvature has only a coefficient-one predecessor return plus nonnegative dissipation and polynomial collars.

No growing packet order, arbitrary source frame, or unidentified current-space map remains in this formulation.

This is a state reduction, not a proof of the recurrence.  In particular positivity of `A_pair` does not itself supply an upper bound for its later value.

## 6. Relation to the cross-free odd relative state

PR #346 `L-34406` proves that the aligned odd-source relative path has curvature

\[
\Delta_4R_{\rm odd}+|I_{\rm odd}|^2
\]

with its bare/second-current cross identically zero.  Equations (L-32315.9)--(L-32315.11) show precisely how the matching parity state is obtained from that odd carrier by finite two-adic dressing.

This nominates a concrete next theorem:

```text
cross-free odd relative curvature
+ finite rational two-adic dressing
-> matching parity curvature recurrence.
```

The two-adic part is fixed complexity and should be audited as finite Hermitian state-space algebra; all nonlocal arithmetic remains confined to the one odd carrier.

## 7. Proof boundary

Closed exactly:

1. four-component Jordan realization of `A_pair`;
2. exact identification `C(V)=A_pair`;
3. common odd-prime Jordan carrier;
4. fixed-degree rational 2-adic factorization of both parity Jordan legs;
5. fixed-degree rational 2-adic factorization of both source-convolved legs;
6. a finite-state formulation of the remaining recurrence.

Still open:

1. the finite Hermitian dissipative law under the two-adic dressing;
2. coefficient-one delayed recurrence for `A_pair`;
3. global subexponential energy;
4. RH.
