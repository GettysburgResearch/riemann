# L-91689 — Fixed-window root Hall has a universal one-use stability bound

Claim ID: `L-91689`  
Status: **PROVED EXACT QUANTITATIVE HALL-STABILITY THEOREM — ANALYTIC ENDPOINT ERROR STILL REQUIRES A BOUND**  
Created: 2026-08-14  
Frozen root route: PR #464 at `2eb70463f3d0ae791a9f140694d2ace7032ae864`  
Primary inputs: `L-91673`, `L-91674`  
RH status: **unproved**

## 1. Uniform unsigned score mass

On the certified root window

\[
 1\le x<c_0^{-1}<54.2192<55,
 \tag{L-91689.1}
\]

the positive score atom at a squarefree node `k<=x` is

\[
 S_x(k)=\frac{5\sqrt x}{k}-\frac3{\sqrt k}.
 \tag{L-91689.2}
\]

Since `k<=x`, this atom is positive, and

\[
 0<S_x(k)\le\frac{5\sqrt x}{k}.
 \tag{L-91689.3}
\]

The elementary rational estimates

\[
 H_{54}=\sum_{k=1}^{54}\frac1k<5,
 \qquad
 \sqrt{55}<\frac{15}{2}
 \tag{L-91689.4}
\]

give the universal bound

\[
 \boxed{
 \sum_{\substack{k\le x\\k\text{ squarefree}}}S_x(k)
 <\frac{375}{2}<188.
 }
 \tag{L-91689.5}
\]

No Möbius cancellation is used.

## 2. Typed Hall variation identity

Let `E_e` and `O_o` be the positive even and odd score masses in one root
fiber, and let `t_(o,e)` be any feasible no-upward score Hall transport. Put

\[
 r_e=E_e-\sum_o t_{o,e}\ge0.
 \tag{L-91689.6}
\]

Let `V_k` be the complete score-normalized typed atom in a normed vector space:
it may include target, every component row, the two ordinary columns used to
form each radix-four coordinate, and every finite boundary/port coordinate.
Then the signed fiber has the exact identity

\[
 \boxed{
 \sum_eE_eV_e-\sum_oO_oV_o
 =\sum_er_eV_e+
  \sum_{o,e}t_{o,e}(V_e-V_o).
 }
 \tag{L-91689.7}
\]

This is the simultaneous residual-plus-bonus decomposition underlying
`L-91673`.

If

\[
 \|V_k\|\le M
 \tag{L-91689.8}
\]

on the root window, then

\[
\begin{aligned}
 \left\|
 \sum_er_eV_e+
 \sum_{o,e}t_{o,e}(V_e-V_o)
 \right\|
 &\le M\sum_er_e+2M\sum_{o,e}t_{o,e}\\
 &=M\left(\sum_eE_e+\sum_oO_o\right).
\end{aligned}
\]

By (L-91689.5),

\[
 \boxed{
 \|\text{root Hall output}\|<188M.
 }
 \tag{L-91689.9}
\]

The same estimate controls the total variation of the residual and all Hall
bonuses before cancellation.

## 3. Stability under finite/continuum replacement

Suppose two typed atom maps `V` and `V_tilde` on the same root window obey

\[
 \sup_k\|\widetilde V_k-V_k\|\le\varepsilon.
 \tag{L-91689.10}
\]

Use the same deterministic Hall coefficients in both. Applying the preceding
variation estimate to their difference gives

\[
 \boxed{
 \|\widetilde{\mathcal H}_x-\mathcal H_x\|
 <188\varepsilon.
 }
 \tag{L-91689.11}
\]

For a positive endpoint measure `lambda`, Tonelli gives

\[
 \boxed{
 \left\|
 \int(\widetilde{\mathcal H}_x-\mathcal H_x)d\lambda
 \right\|
 <188\varepsilon\,\lambda(S).
 }
 \tag{L-91689.12}
\]

In particular, under the inherited coarse root mass bound `lambda(S)<=54`, the
complete error is less than

\[
 \boxed{10152\varepsilon.}
 \tag{L-91689.13}
\]

If `C` is any bounded linear correction/observation map, replace the right side
by `10152 ||C|| epsilon`.

## 4. Consequence for the root-score-Hall route

PR #470 correctly shows that an exact finite/continuum identification is false.
Equations (L-91689.11)--(L-91689.13) show that exact identity is not logically
necessary. A corrected proof may instead establish:

```text
one uniform atom-map approximation epsilon;
one explicit correction-operator norm;
one positive reserve larger than 10152 ||C|| epsilon;
one-use ownership of that reserve.
```

Thus the analytic review burden of PR #464 becomes a quantitative operator
estimate on the fixed compact window, rather than a new Hall theorem or an
exact continuum/finite equality.

This theorem does not supply the required epsilon, operator norm or reserve.
It gives the sharp proof interface through which those analytic estimates must
enter.

## 5. Boundary

```text
fixed-window total score mass <188          PROVED EXACTLY
simultaneous typed Hall variation bound     PROVED EXACTLY
endpoint integration stability              PROVED EXACTLY
mass-54 global multiplier 10152             PROVED EXACTLY
actual endpoint atom approximation          OPEN / ANALYTIC
one-use mismatch/collar/port reserve         OPEN / ROOT PRODUCER
root causal-envelope conclusion             CONDITIONAL
Riemann Hypothesis                          UNPROVEN
```
