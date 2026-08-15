# L-93252 — First-Hermite and centered Q4 reduce to one-dimensional prime-block coherence

Claim ID: `L-93252`  
Status: **PROPOSED COMPLETE EXACT REDUCTION ON FROZEN INPUTS — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: `L-93240`, `L-93241`, `L-93250`, `T-93251`; PR #474 `L-93015` at `0a7e95a6d22f4bed9bbfa4e04b632b2c5827b53b`  
Scope: exact scalar prime-block decompositions and diagonal bounds; no decorrelation theorem and no RH conclusion beyond the conditional consequences stated

## 1. Cubic Q4 prime blocks

Use the exact prime-base source components of PR #483:

\[
\begin{aligned}
 c_{\circ,p}(m)
={}&(\log p)\sum_{k\ge1}\mathbf1_{m=p^k}
 -4(\log p)\sum_{k\ge1}\mathbf1_{m=4p^k}\\
&+3(\log4)\mathbf1_{p=2}
  \sum_{r\ge1}\mathbf1_{m=4^r}.
\end{aligned}
\tag{L-93252.1}
\]

Define the scalar block

\[
 Z_{p,N}
 =\sum_{m\le N}c_{\circ,p}(m)K(m/N),
\tag{L-93252.2}
\]

where \(K\) is the cubic kernel of `L-93250`. Then exactly

\[
 \boxed{
 \mathcal A_\circ(N)=\sum_{p\le N}Z_{p,N}.
 }
\tag{L-93252.3}
\]

Let

\[
 A_{p,N}=\sum_{m\le N}|c_{\circ,p}(m)|.
\]

The frozen tower accounting of `L-93015` gives

\[
 \sum_pA_{p,N}\le10N,
 \qquad
 \max_pA_{p,N}\le8\log(2N),
 \qquad
 \sum_pA_{p,N}^2\le80N\log(2N).
\tag{L-93252.4}
\]

Since \(\|K\|_\infty^2=1/972\), the complete same-prime scalar diagonal obeys

\[
 \boxed{
 D_{\rm cub}(N)
 :=\sum_p|Z_{p,N}|^2
 \le {20\over243}N\log(2N).
 }
\tag{L-93252.5}
\]

This pays every power, contracted appearance, and four-adic correction of one prime before any cross-prime estimate.

## 2. Cubic coherence inverse theorem

When \(\mathcal A_\circ(N)\ne0\), put

\[
 \eta_N={\mathcal A_\circ(N)\over|\mathcal A_\circ(N)|},
 \qquad
 a_{p,N}=
 \left[\Re(\overline{\eta_N}Z_{p,N})\right]_+.
\tag{L-93252.6}
\]

Applying `L-93240` in the one-dimensional complex Hilbert space gives

\[
 \sum_pa_{p,N}\ge|\mathcal A_\circ(N)|,
 \qquad
 \sum_pa_{p,N}^2\le D_{\rm cub}(N),
\tag{L-93252.7}
\]

and therefore

\[
 \boxed{
 \#\{p:a_{p,N}>0\}
 \ge
 {243\over20}
 {|\mathcal A_\circ(N)|^2\over N\log(2N)}.
 }
\tag{L-93252.8}
\]

If \(J_N\) is a smallest set carrying half of the positive projection, then

\[
 \boxed{
 |J_N|
 \ge
 {243\over80}
 {|\mathcal A_\circ(N)|^2\over N\log(2N)}.
 }
\tag{L-93252.9}
\]

Subject to an off-line zero \(\rho\) of real part \(\beta>1/2\), `T-93251` implies, for every admissible \(\varepsilon\),

\[
 \limsup_{N\to\infty}
 {\#\{p:a_{p,N}>0\}\log(2N)
  \over N^{2\beta-1-2\varepsilon}}
 =\infty.
\tag{L-93252.10}
\]

Thus the centered Q4 route no longer requires a row-space direction or a separate endpoint mean: one explicit cubic scalar forces one-dimensional coherent participation of many distinct prime towers.

## 3. Frozen First-Hermite comparison

For the truncated First-Hermite prime polynomial, PR #483 writes

\[
 S_{q,a}(t)=\sum_pY_{p,q,a}(t)
\tag{L-93252.11}
\]

with one block containing every power of the same prime, and proves

\[
 D_{\rm heat}(q,a,t)
 :=\sum_p|Y_{p,q,a}(t)|^2
 \le V(q)+1152
 \ll q+1.
\tag{L-93252.12}
\]

On the frozen PR #392 negative-centre threshold,

\[
 \mathcal M(q,t)<0
 \Longrightarrow
 |S_{q,a}(t)|\gg\log T,
\tag{L-93252.13}
\]

so

\[
 \boxed{
 { |S_{q,a}(t)|^2\over D_{\rm heat}(q,a,t)}
 \gg {\log^2T\over q+1}.
 }
\tag{L-93252.14}
\]

The same Hilbert lemma then forces

\[
 \gg{\log^2T\over q+1}
\]

distinct prime blocks into one half-space.

## 4. Common projective obstruction

Both neglected routes now have the exact form

\[
 \boxed{
 \text{arithmetic scalar }V=\sum_pv_p,
 \qquad
 \text{safe same-prime budget }D=\sum_p|v_p|^2,
 \qquad
 \kappa={|V|^2\over D}.
 }
\tag{L-93252.15}
\]

The First-Hermite violation forces large \(\kappa\) at one carrier; an off-line zero forces unbounded polynomial \(\kappa\) along the cubic Q4 endpoint sequence. The final theorem in either lane must therefore use arithmetic geometry beyond the diagonal and cardinality:

```text
First-Hermite block:
    Gaussian log-prime weight and multiplicative carrier phase;

centered-Q4 block:
    fixed cubic scale weight and the exact factor-four source;

common missing input:
    deterministic distinct-prime decorrelation in the relevant geometry.
```

## 5. Proof boundary

Established:

1. exact scalar Q4 prime-block decomposition;
2. logarithmic complete-tower diagonal (L-93252.5);
3. scalar coherence and half-carrier bounds;
4. the common projective normal form with the frozen heat route.

Open:

1. a deterministic upper bound for the cubic coherence ratio;
2. one-carrier exclusion in the First-Hermite geometry;
3. RH.
