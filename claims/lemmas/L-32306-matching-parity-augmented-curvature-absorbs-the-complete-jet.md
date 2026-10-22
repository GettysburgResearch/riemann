# L-32306 — The matching high-order parity augmented curvature absorbs the complete current/bare jet cofinally

Claim ID: `L-32306`  
Title: For the exact parity pair used by the compact Q=4 jet frame, the source-complete augmented Selberg--Kummer curvature eventually dominates both parity currents and both bare-source squares on every fixed balanced cone  
Status: **PROPOSED COMPLETE COFINAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #263 `L-26205`; PR #337 `L-32705`; PR #334 `L-32406`  
Scope: matching parity carry-row source and its first two logarithmic currents; no global block recurrence or RH conclusion

## 1. Matching parity systems

Retain the exact parity pair of PR #263 and PR #346:

\[
 B_+(s)=p(z)\mathcal O(s),
 \qquad
 B_-(s)=p(-z)\mathcal O(s),
 \qquad
 z=2^{-s},
\]

with

\[
 p(z)=(1-z)(1-2z)(1-\sqrt2 z)^2,
 \qquad
 \mathcal O(s)=\prod_{p\ {m odd}}(1-p^{-s}).
\]

Let `b_+-` be the coefficient sequences, `A_+-=B_+-^{-1}`, and define

\[
 \Lambda_\pm=-A_\pm'/A_\pm,
 \qquad
 C_\pm=\Lambda_\pm\log+\Lambda_\pm*\Lambda_\pm.
\]

The source-convolved first and second currents are

\[
 q_\pm=b_\pm*\Lambda_\pm=-b_\pm\log,
\]

\[
 t_\pm=b_\pm*C_\pm
 =q_\pm\log+2q_\pm*\Lambda_\pm.
\]

For one carry row `e=(n,j)`, put

\[
Y_\pm=\mathcal L_e(b_\pm),
\quad
Q_\pm=\mathcal L_e(q_\pm),
\quad
T_\pm=\mathcal L_e(t_\pm),
\]

and

\[
P_\pm=\mathcal L_e(\Lambda_\pm),
\quad
S_\pm=\mathcal L_e(C_\pm).
\]

The paired generalized-prime reserve is

\[
 \mathcal R_{\rm pair}
 =P_+^2+P_-^2-S_+-S_-.
\tag{L-32306.1}
\]

Define the matching source-complete augmented curvature

\[
 \boxed{
 \mathcal A_{\rm pair}
 =\mathcal R_{\rm pair}
  +Q_+^2+Q_-^2
  -Y_+T_+-Y_-T_-.
 }
\tag{L-32306.2}
\]

Every term belongs to the same two parity systems; no simple-Q4 source is substituted into this definition.

## 2. Bare source charges grow at most logarithmically

Because

\[
 {1\over\zeta(s)}=(1-z)\mathcal O(s),
\]

one has

\[
 \zeta(s)B_+(s)={p(z)\over1-z}
 =(1-2z)(1-\sqrt2 z)^2,
\tag{L-32306.3}
\]

which is a fixed polynomial in `z`.

Likewise

\[
 \zeta(s)B_-(s)={p(-z)\over1-z}.
\tag{L-32306.4}
\]

The numerator `p(-z)` is a fixed degree-four polynomial. Division by `1-z` gives a power series whose coefficients are eventually equal to the fixed number `p(-1)`. Hence its coefficients are bounded uniformly in the two-adic exponent.

The floor/divisor-prefix identity says that the carry of `b_\pm` is the additive defect of the partial sums of the coefficient sequence of `zeta B_\pm`. Equation (L-32306.3) has only finitely many dyadic jumps, while (L-32306.4) has only `O(log n)` nonzero dyadic prefix locations below `n`, each with bounded coefficient. Therefore there is an absolute `C_Y` such that

\[
 \boxed{
 |Y_+(n,j)|+|Y_-(n,j)|
 \le C_Y\log(2n)
 }
\tag{L-32306.5}
\]

for every row.

## 3. Coefficient bounds for the source currents

The source polynomials `p(z)` and `p(-z)` have fixed degree. The odd Euler core has coefficients `mu(m)` on odd integers. Consequently there is an absolute `C_b` such that

\[
 |b_\pm(m)|\le C_b
\qquad(m\ge1).
\tag{L-32306.6}
\]

Hence

\[
 \boxed{|q_\pm(m)|\le C_b\log(2m).}
\tag{L-32306.7}
\]

The absolute generalized-prime coefficients of the two channels agree, because the minus channel is the complete two-adic parity twist. PR #334 `L-32406` proves for the positive plus channel

\[
 \sum_{d\le x}\Lambda_+(d)\le6x.
\tag{L-32306.8}
\]

Using `t=q\log+2q*Lambda`, (L-32306.7), (L-32306.8), and divisor switching,

\[
\begin{aligned}
\sum_{m\le n}|t_\pm(m)|
&\le C_b\sum_{m\le n}\log^2(2m)\\
&\quad+2C_b\sum_{ab\le n}\log(2a)|\Lambda_\pm(b)|\\
&\ll n\log^2(2n)
+n\sum_{a\le n}{\log(2a)\over a}\\
&\ll n\log^2(2n).
\end{aligned}
\tag{L-32306.9}
\]

Since every carry indicator is zero or one,

\[
 \boxed{
 |T_+|+|T_-|
 \le C_T n\log^2(2n)
 }
\tag{L-32306.10}
\]

for one absolute constant `C_T`.

Together with (L-32306.5),

\[
 \boxed{
 |Y_+T_++Y_-T_-|
 \le C_{YT}n\log^3(2n).
 }
\tag{L-32306.11}
\]

## 4. The matched Kummer reserve is quadratic on balanced cones

Fix `0<eta<=1/2` and assume

\[
 \eta n\le j\le(1-\eta)n.
\]

PR #337 `L-32705` proves

\[
P_+^2+P_-^2
\ge {\eta^2\log^22\over2}n^2
\tag{L-32306.12}
\]

and

\[
{S_++S_-\over P_+^2+P_-^2}\longrightarrow0
\tag{L-32306.13}
\]

uniformly on that cone. Thus there is `N_eta` such that for `n>=N_eta`,

\[
 \boxed{
 \mathcal R_{\rm pair}
 \ge {\eta^2\log^22\over4}n^2.
 }
\tag{L-32306.14}
\]

The source-current cross term in (L-32306.11) is one full power of `n` smaller. Enlarging `N_eta` if necessary gives

\[
 \boxed{
 |Y_+T_++Y_-T_-|
 \le {1\over4}\mathcal R_{\rm pair}.
 }
\tag{L-32306.15}
\]

Likewise (L-32306.5) gives

\[
 \boxed{
 Y_+^2+Y_-^2
 \le {1\over4}\mathcal R_{\rm pair}
 }
\tag{L-32306.16}
\]

cofinally and uniformly on the fixed balanced cone.

## 5. Complete jet absorption

From (L-32306.2) and (L-32306.15),

\[
\begin{aligned}
\mathcal A_{\rm pair}
&\ge Q_+^2+Q_-^2+{3\over4}\mathcal R_{\rm pair}.
\end{aligned}
\tag{L-32306.17}
\]

Combining with (L-32306.16),

\[
 \boxed{
 Q_+^2+Q_-^2+Y_+^2+Y_-^2
 \le\mathcal A_{\rm pair}
 }
\tag{L-32306.18}
\]

for every sufficiently large row in the fixed balanced cone.

In particular the matching augmented curvature is not merely positive: it contains the **entire current/bare two-channel jet energy with coefficient one**, while retaining at least half of the quadratic Kummer reserve as an unused moat.

## 6. Consequence for the compact Q=4 jet frame

PR #346 `L-34402` proves, for the **same parity source pair**, the critical-line finite-filter inequality

\[
2|q_\circ|^2
\le |q_+|^2+|q_-|^2+|B_+|^2+|B_-|^2.
\tag{L-32306.19}
\]

Its Toeplitz/Hilbert consequence applies on finite logarithmic blocks, with only a fixed causal terminal collar.

Under the exact physical/carry placement of PR #339/#341, the four physical fields on the right of (L-32306.19) are precisely the source-current and bare-source coordinates `Q_+,Q_-,Y_+,Y_-` of the predecessor ordinary/augmented carry rows. Equation (L-32306.18) therefore yields, after block integration and outside the fixed low/collar table,

\[
 \boxed{
 2\|\mathcal P_{q_\circ}\|_{J,I}^2
 \le
 \int_{J,I}\mathcal A_{\rm pair}
 +\operatorname{poly}(J)_{\rm fixed\ collar}.
 }
\tag{L-32306.20}
\]

This is a local no-double-spend theorem: the compact innovation current and the parity bare-source legs can be charged to **one matching augmented curvature state**, not to separate copies of the Kummer reserve.

The fixed one-step augmented physical rows of PR #346 differ from ordinary rows only by one endpoint divisor column. PR #346 `L-34403` proves that the generalized-prime reserve can only increase under that augmentation; the corresponding source/current endpoint increments are fixed-divisor logarithmic terms and satisfy the same lower-order estimates as Sections 2--3. Thus enlarging the finite threshold and collar covers the complete physical carry field.

## 7. What this does and does not close

This theorem closes the local accounting problem

```text
compact Q4 current jet
+ parity bare source
-> one source-matched augmented parity curvature.
```

It does **not** prove that the augmented curvature is small. The remaining conclusion-producing theorem is now the evolution of this single positive curvature state through the source-convolved reflected/all-pass recurrence.

No strict contraction of a zeta-zero mode is asserted.

## 8. Proof boundary

Closed here, subject to review:

- matching source typing for the PR #346 parity pair;
- logarithmic bare-source row bound;
- `O(n log^2 n)` second source-current bound;
- quadratic matched Kummer reserve on every fixed balanced cone;
- cofinal coefficient-one absorption of both parity currents and bare-source squares;
- composition with the exact compact-current jet frame into one augmented curvature budget.

Open:

- coefficient-one delayed recurrence for `A_pair`;
- global subexponential block energy;
- RH.
