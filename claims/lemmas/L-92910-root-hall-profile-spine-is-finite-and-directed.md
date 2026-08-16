# L-92910 — The factor-67 root Hall/profile source is a finite directed theorem

Claim ID: `L-92910`  
Status: **PROPOSED COMPLETE DIRECTED/EXACT RECONSTRUCTION — INDEPENDENT REVIEW REQUIRED**  
RH status: **unproved**

## 1. Complete root domain

For integer \(X\), put
\[
K=\left\lfloor X/67\right\rfloor+1.
\]
Every retained endpoint coordinate \(s\ge K\) has \(x=X/s<67\). Hence every squarefree source node \(k\le x\) divides \(P_{61}\), and the only possible component rows are \(2\le j\le66\).

Define
\[
T_x(k)=\frac{4\sqrt{x/k}-3}{\sqrt k},\quad
S_x(k)=\frac{5\sqrt{x/k}-3}{\sqrt k},\quad
A_{x,j}(k)=\frac{Q_{x/k}(j)}{\sqrt k}.
\]

## 2. Hall prefixes

For each active odd Möbius threshold \(t<67\), put
\[
A_t=\sum_{n\le t}\frac{\mu(n)}n,
\qquad B_t=\sum_{n\le t}\frac{\mu(n)}{\sqrt n}.
\]
The no-upward target prefix is
\[
H_t(x)=4\sqrt x\,A_t-3B_t.
\]
On \(t\le x<67\), this is affine in \(\sqrt x\). Its minimum is at \(x=t\) when \(A_t\ge0\), and at \(x\uparrow67\) when \(A_t<0\). Directed algebraic evaluation of all 22 active thresholds gives
\[
\boxed{H_t(x)>7/20.}
\]
The deterministic left-greedy Hall algorithm therefore produces one Borel nonnegative transport \(t_x(o,e)\), supported on \(e\le o\), exhausting every odd target and using at most every even target.

## 3. The same flow controls score

The ratio
\[
f(z)=\frac{5z-3}{4z-3}
\]
satisfies \(f'(z)=-3/(4z-3)^2<0\). Since an allowed edge has \(e\le o\), the same target flow is score-superordinate. No second Hall selection is made.

## 4. The same flow controls every row

For each declared row define
\[
R_j(Y)=\frac{Q_Y(j)}{4\sqrt Y-3}.
\]
On the compact causal domain \(j\le Y<67\), the activation-cell formula for \(Q_Y(j)\) is explicit. Differentiating on each cell and checking both one-sided activation values gives
\[
\boxed{R_j'(Y)\ge0\qquad(2\le j\le66).}
\]
The companion replay recomputes every activation cell with directed algebraic/logarithmic intervals; it does not extrapolate a grid. Hence \(e\le o\) implies \(R_j(x/e)\ge R_j(x/o)\), and the same Hall flow gives
\[
B_{x,j}=\sum_{o,e}t_x(o,e)\bigl[R_j(x/e)-R_j(x/o)\bigr]\ge0.
\]
Consequently
\[
\sum_k\mu(k)A_{x,j}(k)
=
\sum_{\mu(e)=1}\nu_x(e)A_{x,j}(e)+B_{x,j}
\]
simultaneously in every row, while target is exact and score favorable.

## 5. Quantifiers

The proof covers every real \(1\le x<67\), every active squarefree source node, every active odd threshold, and every declared row \(2\le j\le66\). Values at the finitely many activation knots are assigned one-sidedly and are irrelevant to endpoint integration.
