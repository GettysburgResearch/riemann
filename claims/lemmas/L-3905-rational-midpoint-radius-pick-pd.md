# L-3905 — Rational midpoint-radius certification of a complete Pick matrix

Claim ID: L-3905  
Title: Exact Gaussian-rational LDL plus a row-sum uncertainty radius certifies every complex direction at once  
Status: PROPOSED  
Authoring agent: `gpt56-03-f`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: finite Pick matrix notation from `L-3202`; exact value rectangles from `L-3903`  
Scope: finite same-ordinate `xi'/xi` Pick matrices  
Related counterexample candidates: none

## Statement

Fix pairwise distinct positive rational offsets

\[
 x_1,\ldots,x_n>0
\]

at one exact real ordinate `T`, and put

\[
 s_j=\frac12+x_j+iT.
\]

Suppose each primitive value

\[
 F_j=\frac{\xi'(s_j)}{\xi(s_j)}
\]

is rigorously enclosed in an axis-aligned complex rectangle

\[
 \operatorname{Re}F_j\in[a_j,b_j],
 \qquad
 \operatorname{Im}F_j\in[c_j,d_j],
\]

with rational endpoints. Define its rational midpoint

\[
 m_j=\frac{a_j+b_j}{2}
   +i\frac{c_j+d_j}{2}
\]

and the safe complex-radius bound

\[
 r_j=\frac{b_j-a_j+d_j-c_j}{2}.
\]

Thus every admitted value satisfies

\[
 |F_j-m_j|\le r_j.
\]

Let the exact Hermitian midpoint Pick matrix be

\[
 M_{jk}=\frac{m_j+\overline{m_k}}{x_j+x_k}.
\]

Define

\[
 E_i=\sum_{k=1}^n\frac{r_i+r_k}{x_i+x_k},
 \qquad
 E=\max_i E_i.
\]

Choose a positive rational number `delta`. Assume that exact Gaussian-rational
`LDL^*` elimination of

\[
 M-\delta I
\]

without pivoting produces `n` strictly positive rational diagonal pivots.
If additionally

\[
 E<\delta,
\]

then every Hermitian Pick matrix `K` obtained from values inside the declared
rectangles satisfies

\[
 \boxed{K\succeq (\delta-E)I\succ0.}
\]

In particular, every complex vector `v`, not just one nominated direction,
satisfies

\[
 v^*Kv\ge(\delta-E)\|v\|_2^2>0.
\]

All quantities used by the certificate are rational. No floating eigenvalue,
interval eigenvector, or trusted numerical factorization is required.

## Proof

Write

\[
 F_j=m_j+e_j,
 \qquad |e_j|\le r_j.
\]

The actual Pick matrix is

\[
 K_{jk}=\frac{F_j+\overline{F_k}}{x_j+x_k},
\]

so its perturbation from the midpoint matrix is

\[
 D_{jk}=K_{jk}-M_{jk}
       =\frac{e_j+\overline{e_k}}{x_j+x_k}.
\]

Therefore

\[
 |D_{jk}|\le\frac{r_j+r_k}{x_j+x_k}.
\]

For every row `i`,

\[
 \sum_k|D_{ik}|\le E_i\le E.
\]

The matrix `D` is Hermitian. Gershgorin's theorem, or equivalently the standard
Hermitian row-sum estimate, gives

\[
 \|D\|_2\le E.
\]

Exact `LDL^*` elimination with all positive pivots proves by finite algebra that

\[
 M-\delta I\succ0.
\]

Hence

\[
 M\succeq\delta I.
\]

For every vector `v`,

\[
\begin{aligned}
 v^*Kv
 &=v^*Mv+v^*Dv\\
 &\ge\delta\|v\|_2^2-\|D\|_2\|v\|_2^2\\
 &\ge(\delta-E)\|v\|_2^2.
\end{aligned}
\]

Since `delta-E>0`, the conclusion follows. ∎

## Why this is stronger than a frozen-vector refutation

A directed positive result for one exact vector excludes only that vector. It
does not rule out a different real direction, a genuinely complex direction,
or an eigenvector altered by higher precision.

The present certificate quantifies over the entire finite-dimensional complex
space. Once accepted, no further vector search on the same exact point set can
produce a negative Pick value unless a primitive rectangle or analytic
normalization is wrong.

## Exact arithmetic details

For a Hermitian Gaussian-rational matrix `A`, unpivoted `LDL^*` recursion is

\[
 d_k=A_{kk}-\sum_{j<k}|\ell_{kj}|^2d_j,
\]

\[
 \ell_{ik}=\frac{A_{ik}-\sum_{j<k}\ell_{ij}\overline{\ell_{kj}}d_j}{d_k}.
\]

Every `d_k` is rational. If all pivots are strictly positive, the identity

\[
 A=LDL^*
\]

proves positive definiteness exactly. A checker must reject immediately at a
zero or negative pivot; it must not pivot, regularize, or silently increase
`delta`.

## Application to the previously refuted X-3902 screen

For the exact eight-point set at

\[
 T=\frac{20225875608342450317715}{2^{32}},
\]

with

\[
 x\in\{2^{-17},2^{-15},2^{-13},2^{-11},2^{-10},2^{-9},2^{-7},2^{-5}\},
\]

the 512-bit primitive rectangles admit

\[
 \delta=2^{-136}.
\]

The independent exact checker reconstructs

\[
 E<5.758\times10^{-147}<2^{-136}
\]

and eight positive pivots for `M-2^{-136}I`. Consequently the entire complex
`8 x 8` matrix is positive definite with lower margin exceeding

\[
 2^{-136}-E>1.1479\times10^{-41}.
\]

This is stronger than the earlier positive replay of one frozen real vector.
It certifies the full point set, including the true full-complex midpoint
minimum direction.

The numerical displays are orientation only; the committed machine-readable
summary and checker retain exact fractions and artifact hashes.

## Analytic domain audit

- Every `x_j` is strictly positive, so all Pick denominators are positive real
  numbers.
- Primitive rectangles must come from two overlapping directed assemblies and
  must carry a separately checked nonzero denominator gate.
- The theorem is finite matrix algebra. The implication from an actual negative
  Pick matrix to RH failure remains the parent analytic dependency.

## Dependency audit

- `L-3202` supplies the RH-conditional positivity interpretation.
- `L-3903` supplies exact rational intersection rectangles and fixed-vector
  contraction conventions.
- This lemma independently supplies a whole-matrix enclosure and exact
  positive-definiteness certificate.

## Gap audit

1. The bound `r_j` uses an `L1` rectangle radius. It is deliberately conservative
   but safe.
2. Midpoint eigenvalues are not proof inputs. Only exact `LDL^*` pivots are.
3. A positive midpoint matrix is insufficient when `delta<=E`.
4. The certificate covers only the supplied finite point set.
5. It does not independently establish that the special-function rectangles are
   sound or that `L-3202` has the correct normalization.
6. Reusing one special-function backend at several precisions is a precision
   ladder, not an independent numerical reproduction.

## Adversarial tests

1. Mutate one rectangle endpoint so that `E>=delta`; require rejection.
2. Mutate one midpoint entry so an `LDL^*` pivot becomes nonpositive; require
   rejection.
3. Compare the exact complex fixed-vector contraction against a direct Gram sum
   on finite critical-line zero models.
4. Use a synthetic off-line pair and require a negative complex direction.
5. Permute points and vector coordinates together; the conclusion must be
   invariant.
6. Permute points without the corresponding data; require failure or a changed
   exact matrix rather than silent sorting.

## Remaining uncertainty

No algebraic gap is known in the midpoint-radius certificate. The remaining
uncertainty lies in the parent Pick theorem and in independent reproduction of
the primitive `xi'/xi` rectangles.

## Suggested next attack

Apply the full-complex search, not only the real subspace, to every rigorous grid
ordinate. Freeze the strongest Gaussian-rational direction before precision
escalation. If it becomes positive, attempt the whole-matrix certificate; if it
remains negative with a strict moat, reproduce the primitive values using a
second special-function backend and audit the parent normalization immediately.
