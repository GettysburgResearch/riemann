# L-90010 — Centered scale-two odd-source curvature and exact compact-current two-tap routing

Claim ID: `L-90010` (provisional range; allocate before integration)  
Status: **PROPOSED COMPLETE EXACT/COFINAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Date: 2026-08-09  
Depends on: PR #346 `L-34404` odd-prime asymptotics; `R-90009` corrected odd-source carry; elementary Stirling/Kummer identities  
Scope: repairs and refines the odd-source relative state. It does not prove an upper/dissipative law, SHARP, WSTS, or RH.

## 1. Definitions

Retain the odd Euler source
\[
B_{\rm odd}(s)=\prod_{p\ {m odd}}(1-p^{-s})
\]
with coefficient sequence `b_odd`, inverse `A_odd`, odd generalized-prime sequence
\[
\Lambda_{\rm odd}(n)=\Lambda(n)\mathbf1_{2\nmid n},
\]
and Selberg sequence
\[
C_{\rm odd}=\Lambda_{\rm odd}\log+
\Lambda_{\rm odd}*\Lambda_{\rm odd}.
\]
For a nontrivial integer row `e=(n,j)`, `k=n-j`, put
\[
O(e)=\mathcal L_e(\Lambda_{\rm odd})
=\log\operatorname{odd}\binom nj,
\]
\[
S(e)=\mathcal L_e(C_{\rm odd}),
\qquad
R(e)=O(e)^2-S(e).
\tag{L-90010.1}
\]
Let
\[
q_{\rm odd}=b_{\rm odd}*\Lambda_{\rm odd}=-b_{\rm odd}\log,
\qquad
Q(e)=\mathcal L_e(q_{\rm odd}).
\tag{L-90010.2}
\]
The scale-two increments are
\[
\boxed{
\Delta_2R(e)=R(2e)-4R(e),
\qquad
I_2(e)=Q(2e)-Q(e).
}
\tag{L-90010.3}
\]
Here `2e=(2n,2j)`.

## 2. The corrected bare source naturally selects scale two

By `R-90009`,
\[
(\varepsilon-\delta_2)*b_{\rm odd}=\mu
\tag{L-90010.4}
\]
and for every nontrivial row
\[
\mathcal L_{2e}(\mu)=-1.
\tag{L-90010.5}
\]
Thus scale two is the unique first dyadic step at which the odd source difference becomes the ordinary Möbius source with a **constant**, row-independent carry charge.

This is stronger than the false scale-four invariance used in the original `L-34406`: there is no logarithmic bare state to transport after the one-unit centering below.

## 3. The odd reserve creates a critical moat at every doubling

Fix
\[
0<\eta<1/2,
\qquad
\eta n\le j\le(1-\eta)n,
\]
and write
\[
\alpha=j/n,
\qquad
H(\alpha)=-\alpha\log\alpha-(1-\alpha)\log(1-\alpha),
\]
\[
h_\eta=\min_{\eta\le\alpha\le1-\eta}H(\alpha)>0.
\]
PR #346 `L-34404` proves uniformly on the fixed balanced cone
\[
O(e)=nH(\alpha)+O_\eta(\log(2n)),
\tag{L-90010.6}
\]
\[
S(e)=2nH(\alpha)\log n+nK(\alpha)
+O_\eta(\log^2(2n)),
\tag{L-90010.7}
\]
for one bounded continuous `K`.

At the doubled row,
\[
S(2e)-4S(e)
=-4nH(\alpha)\log n
+4nH(\alpha)\log2
-2nK(\alpha)
+O_\eta(\log^2(2n)).
\tag{L-90010.8}
\]
Hence, cofinally and uniformly,
\[
\boxed{
S(2e)-4S(e)
\le-2h_\eta n\log n.
}
\tag{L-90010.9}
\]

Now put
\[
E_2(e)=O(2e)-2O(e).
\tag{L-90010.10}
\]
Kummer/Legendre gives the exact valuation invariance
\[
\boxed{
v_2\binom{2n}{2j}=v_2\binom nj,}
\tag{L-90010.11}
\]
because binary doubling shifts every digit without changing its digit sum. Therefore, with `v=v_2 binom(n,j)`,
\[
\boxed{
E_2(e)
=\log\frac{\binom{2n}{2j}}{\binom nj^2}
+v\log2.
}
\tag{L-90010.12}
\]
Uniform Stirling on the balanced cone yields
\[
\log\frac{\binom{2n}{2j}}{\binom nj^2}
=\frac12\log n+O_\eta(1).
\tag{L-90010.13}
\]
Since `v>=0`,
\[
\boxed{E_2(e)\ge0}
\tag{L-90010.14}
\]
cofinally and uniformly. Also `E_2=O_\eta(log n)` because `v=O(log n)`.

Using
\[
O(2e)=2O(e)+E_2(e),
\]
one gets the exact expansion
\[
\boxed{
\Delta_2R(e)
=E_2(e)\bigl(4O(e)+E_2(e)\bigr)
-\bigl[S(2e)-4S(e)\bigr].
}
\tag{L-90010.15}
\]
Since `O>=0`, (L-90010.9) and (L-90010.14) give
\[
\boxed{
\Delta_2R(e)
\ge2h_\eta n\log n
}
\tag{L-90010.16}
\]
cofinally. The same estimates give the matching upper bound
\[
\boxed{
\Delta_2R(e)=O_\eta(n\log n).
}
\tag{L-90010.17}
\]
Thus
\[
\boxed{
\Delta_2R(e)=\Theta_\eta(n\log n).
}
\tag{L-90010.18}
\]
The critical odd-prime moat is therefore already created at **each doubling**, not only after a scale-four jump.

As a consistency identity,
\[
\boxed{
\Delta_4R(e)
=\Delta_2R(2e)+4\Delta_2R(e).
}
\tag{L-90010.19}
\]
So the scale-four moat of `L-34404` decomposes exactly into two scale-two moats.

## 4. A correctly centered cross-free scale-two vector curvature

Define the positive odd Jordan deformation
\[
J_\tau(s)=\frac{A_{\rm odd}(s-\tau)}{A_{\rm odd}(s)},
\qquad
K_\tau=b_{\rm odd}*J_\tau.
\tag{L-90010.20}
\]
For one row put
\[
F_e(\tau)=1+\mathcal L_e(J_\tau)
\]
and define the relative scalar coordinate
\[
\boxed{
H_e^{(2)}(\tau)
=\frac{F_{2e}(\tau)}{F_e(2\tau)}.
}
\tag{L-90010.21}
\]
Exactly as in the scale-four Jordan calculation,
\[
H_e^{(2)}(0)=1,
\]
\[
(H_e^{(2)})'(0)=E_2(e),
\]
and
\[
\boxed{
-\bigl(\log H_e^{(2)}\bigr)''(0)=\Delta_2R(e).
}
\tag{L-90010.22}
\]

For the source leg use the **centered** coordinate forced by (L-90010.5):
\[
\boxed{
G_e^{(2)}(\tau)
=1+
\mathcal L_{2e}\bigl((\varepsilon-\delta_2)*K_\tau\bigr).
}
\tag{L-90010.23}
\]
Then
\[
\boxed{G_e^{(2)}(0)=0}
\tag{L-90010.24}
\]
exactly, while
\[
\boxed{(G_e^{(2)})'(0)=I_2(e).}
\tag{L-90010.25}
\]
The second derivative is the corresponding source-difference second current but its value drops out of the curvature because the zeroth coordinate is zero.

Put
\[
W_e^{(2)}(\tau)=\bigl(H_e^{(2)}(\tau),G_e^{(2)}(\tau)\bigr).
\]
For
\[
\mathfrak C(W)=\|W'(0)\|^2-
\operatorname{Re}\langle W(0),W''(0)\rangle,
\]
(L-90010.22)--(L-90010.25) give the exact identity
\[
\boxed{
\mathfrak C(W_e^{(2)})
=\Delta_2R(e)+|I_2(e)|^2.
}
\tag{L-90010.26}
\]
Thus the repaired odd-source state is cross-free already at scale two and contains the genuine current innovation with coefficient one.

Positivity of (L-90010.26) is **not** an upper bound for `I_2`; no RH conclusion is inferred.

## 5. Exact compact Q4 current routing through two scale-two innovations

Now write
\[
z=2^{-s},
\qquad
T(z)=(1-z)(1-4z^2)=1-z-4z^2+4z^3.
\tag{L-90010.27}
\]
The compact Q4 source of PR #346 factors as
\[
\boxed{B_\circ(s)=T(z)B_{\rm odd}(s).}
\tag{L-90010.28}
\]
Hence its current is
\[
q_\circ=T(z)q_{\rm odd}+T'(s)b_{\rm odd},
\tag{L-90010.29}
\]
with
\[
\boxed{
T'(s)=(\log2)(z+8z^2-12z^3).
}
\tag{L-90010.30}
\]

Fix a fully aligned dyadic chain
\[
e_r=(2^rn,2^rj),
\qquad r\ge0,
\]
and write
\[
Q_r=Q(e_r),
\qquad
Y_r=Y_{\rm odd}(e_r),
\qquad
I_r=Q_r-Q_{r-1}\quad(r\ge1).
\tag{L-90010.31}
\]
The exact delay identity
\[
\mathcal L_{e_r}(\delta_{2^a}*f)
=\mathcal L_{e_{r-a}}(f)
\qquad(r\ge a)
\tag{L-90010.32}
\]
gives, for `r>=3`,
\[
\mathcal L_{e_r}(Tq_{\rm odd})
=Q_r-Q_{r-1}-4Q_{r-2}+4Q_{r-3}
=I_r-4I_{r-2}.
\tag{L-90010.33}
\]
By the corrected scaling law `R-90009`,
\[
Y_{r-a}=Y_r+a.
\tag{L-90010.34}
\]
Therefore the derivative gauge in (L-90010.30) is
\[
\begin{aligned}
\mathcal L_{e_r}(T'b_{\rm odd})
&=(\log2)(Y_{r-1}+8Y_{r-2}-12Y_{r-3})\\
&=-(\log2)(3Y_r+19).
\end{aligned}
\tag{L-90010.35}
\]
Combining (L-90010.29), (L-90010.33), and (L-90010.35),
\[
\boxed{
Q_\circ(e_r)
=I_r-4I_{r-2}-(\log2)(3Y_r+19),
\qquad r\ge3.
}
\tag{L-90010.36}
\]
This is an exact finite two-tap routing of the RH-sensitive compact current through **two scale-two odd innovations separated by one scale-four delay**, plus a completely explicit bare charge.

Since (R-90009.6) gives `Y_r=O(log(2^rn))`, the last term is deterministic logarithmic forcing.

At critical square-root normalization, let
\[
N_r=2^rn,
\qquad
u_r=\frac{I_r}{\sqrt{N_r}},
\qquad
c_r=\frac{Q_\circ(e_r)}{\sqrt{N_r}}.
\]
Then (L-90010.36) becomes
\[
\boxed{
c_r
=\nu_r-2\nu_{r-2}
-\frac{(\log2)(3Y_r+19)}{\sqrt{N_r}}.
}
\tag{L-90010.37}
\]
The forcing is `O(log N_r/sqrt(N_r))`. The delayed coefficient `2` is exactly critical: its square `4` matches the factor-four scale loss across two doublings. Thus (L-90010.37) is a **neutral two-step recurrence target**, not a strict contraction.

## 6. What this changes in the Q4 frontier

The corrected route now has the following architecture:

```text
fresh deterministic storage at every doubling:
    Delta_2 R_odd = Theta_eta(n log n);

source-complete centered state:
    C(W_e^(2)) = Delta_2 R_odd + |I_2|^2;

compact RH-sensitive current:
    normalized q_circ = current scale-two innovation
                        - 2 * two-step-delayed scale-two innovation
                        + vanishing deterministic forcing.
```

This is finer than the previous scale-four formulation. It removes the false bare-charge invariance and replaces it with a constant Möbius centering. It also exposes the exact **neutral coefficient** which any conclusion-producing Hermitian ledger must handle.

What remains is still RH-bearing: one needs an **upper/dissipative law** for the same centered scale-two curvature state, or a lossless two-state colligation which turns the neutral combination in (L-90010.37) into current output plus delayed storage without double spending.

A generic Cauchy bound on `|nu_r-2nu_{r-2}|^2` is not sufficient and would destroy the coefficient-one scale balance.

## 7. Boundary

Closed here, subject to independent review:

1. exact scale-two odd-source centering by ordinary Möbius;
2. exact binary-valuation invariance under row doubling;
3. cofinal `Delta_2R_odd=Theta_eta(n log n)`;
4. exact decomposition of the old scale-four moat into two scale-two moats;
5. cross-free centered vector curvature `Delta_2R_odd+|I_2|^2`;
6. exact compact-current routing (L-90010.36);
7. critical normalized neutral recurrence form (L-90010.37).

Still open:

1. an upper/fixed-delay law for the centered scale-two curvature;
2. a lossless/dissipative two-state realization of the neutral innovation pair;
3. subpower global current energy;
4. RH.