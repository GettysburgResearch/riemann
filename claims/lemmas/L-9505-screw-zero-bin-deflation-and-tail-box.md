# L-9505 — Screw zero-bin deflation and tail box

Claim ID: L-9505  
Title: Certified critical-line zero bins give Toeplitz lower blocks and a two-sided tail box  
Status: PROPOSED  
Authoring agent: `gpt56-08`  
Reviewing agents: none  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: L-9504; certified critical-line zero bins and, for the upper box, a certified zero-tail sum  
Scope: zero-deflated arithmetic-progression screw witnesses  
Related counterexample candidates: none yet

## Definitions

A **certified zero bin** is an exact rational interval on the real ordinate
axis together with a rigorously proved lower or exact count of critical-line
zeros, including multiplicity.  A **complete low-zero cover through `T`** is a
pairwise disjoint family of such bins accounting for every ordinate
`|gamma|<=T`, including both signs.  All matrix inequalities below use the
Loewner order on Hermitian matrices.

## Statement

Fix `h>0` and `n>=1`.  For real nonzero `gamma`, define

\[
 u_\gamma(h)
 =\frac{1-e^{i\gamma h}}{\gamma}
   \begin{pmatrix}
    1&e^{i\gamma h}&\cdots&e^{i(n-1)\gamma h}
   \end{pmatrix}^{T}.
\tag{L-9505.1}
\]

Under RH, `L-9504` gives

\[
 H^{(n)}(h)=\sum_\gamma u_\gamma(h)u_\gamma(h)^*.
\tag{L-9505.2}
\]

Let

\[
 I=[c-r,c+r],
 \qquad r\ge0,
 \qquad |c|>r,
\tag{L-9505.3}
\]

be an exact real interval.  Suppose exact nonnegative numbers `G` and `eta`
satisfy

\[
 \|u_c(h)\|_2\le G,
 \qquad
 \|u_\gamma(h)-u_c(h)\|_2\le\eta
 \quad(\gamma\in I).
\tag{L-9505.4}
\]

Put

\[
 \varepsilon=(2G+\eta)\eta.
\tag{L-9505.5}
\]

Then every `gamma in I` obeys the Loewner lower bound

\[
 \boxed{
 u_\gamma u_\gamma^*
 \succeq
 u_cu_c^*-\varepsilon I_n.
 }
\tag{L-9505.6}
\]

### Lower deflation from certified zero bins

Let `I_s=[c_s-r_s,c_s+r_s]` be pairwise disjoint bins.  Suppose bin `I_s`
contains at least `m_s` certified zeros of

\[
 \xi\!\left(\frac12+i\gamma\right)
\]

with real ordinates in the bin, counted with multiplicity.  Define

\[
 L_s=u_{c_s}u_{c_s}^*-\varepsilon_sI_n.
\tag{L-9505.7}
\]

Then RH implies

\[
 \boxed{
 R_{\rm low}
 :=H^{(n)}(h)-\sum_s m_sL_s
 \succeq0.
 }
\tag{L-9505.8}
\]

Consequently a frozen exact vector `v` with a directed enclosure

\[
 \sup v^*R_{\rm low}v<0
\tag{L-9505.9}
\]

is a finite RH-disproof witness.  The same is true for a negative exact trace
against any exact positive-semidefinite Gram multiplier.

### Sharper fixed-vector bin subtraction

For one frozen vector `v`, define

\[
 \ell_I(v)
 =\left(
   \max\left\{0,
    |v^*u_c|-\|v\|_2\eta
   \right\}
  \right)^2.
\tag{L-9505.10}
\]

Every `gamma in I` satisfies

\[
 |v^*u_\gamma|^2\ge\ell_I(v).
\tag{L-9505.11}
\]

Thus the weaker hypothesis that `I_s` contains at least `m_s` certified
critical-line zeros gives the scalar RH consequence

\[
 \boxed{
 v^*H^{(n)}(h)v-\sum_s m_s\ell_{I_s}(v)\ge0.
 }
\tag{L-9505.12}
\]

This fixed-vector subtraction is normally sharper than contracting the
matrix repair `epsilon I`, and its exact lower endpoints can rank which zero
bins are worth certifying first.

### Two-sided box after complete low-zero coverage

Assume more strongly that the bins contain exactly their declared
multiplicities and collectively account for every zero ordinate with
`|gamma|<=T`, including multiplicity and both signs.  Let

\[
 E=\sum_s m_s\varepsilon_s.
\tag{L-9505.13}
\]

Suppose a rigorous tail estimate proves

\[
 \sum_{|\gamma|>T}\frac1{\gamma^2}\le S_T.
\tag{L-9505.14}
\]

Then RH implies the two-sided operator box

\[
 \boxed{
 0\preceq R_{\rm low}
 \preceq (4nS_T+2E)I_n.
 }
\tag{L-9505.15}
\]

Thus either a negative Rayleigh value or an exact Rayleigh value above the
upper endpoint in (L-9505.15) contradicts RH.  The second failure mode is an
**excess-positive** witness unavailable in an undeflated PSD test.

## Constructive bin bounds

Let

\[
 a=|c|-r>0.
\]

The center norm is exactly

\[
 \|u_c(h)\|_2^2
 =\frac{4n\sin^2(ch/2)}{c^2}
 \le\frac{4n}{c^2}.
\tag{L-9505.16}
\]

For `0<=j<n`, write

\[
 u_{\gamma,j}(h)
 =\frac{e^{ijh\gamma}-e^{i(j+1)h\gamma}}{\gamma}.
\]

On `I`,

\[
 \left|\frac{d}{d\gamma}u_{\gamma,j}(h)\right|
 \le
 \frac{h(2j+1)}a+\frac2{a^2}.
\tag{L-9505.17}
\]

Therefore it is enough to certify

\[
 \boxed{
 \eta^2\ge
 r^2\sum_{j=0}^{n-1}
 \left(\frac{h(2j+1)}a+\frac2{a^2}\right)^2.
 }
\tag{L-9505.18}
\]

For a rational certificate, `h` may be replaced in (L-9505.18) by any exact
rational upper bound.  Square roots need not enter the checker: store rational
upper bounds `G` and `eta` whose squares dominate the displayed quantities.

## Proof or construction

Let

\[
 x=u_\gamma(h),
 \qquad y=u_c(h),
 \qquad \|x-y\|\le\eta,
 \qquad \|y\|\le G.
\]

For a unit vector `v`,

\[
\begin{aligned}
 \left|v^*(xx^*-yy^*)v\right|
 &=\left||v^*x|^2-|v^*y|^2\right|\\
 &\le |v^*(x-y)|\left(|v^*x|+|v^*y|\right)\\
 &\le \eta(2G+\eta)=\varepsilon.
\end{aligned}
\]

Hence

\[
 -\varepsilon I_n
 \preceq xx^*-yy^*
 \preceq\varepsilon I_n,
\tag{L-9505.19}
\]

which proves (L-9505.6).  The reverse triangle inequality also gives

\[
 |v^*u_\gamma|
 \ge |v^*u_c|-|v^*(u_\gamma-u_c)|
 \ge |v^*u_c|-\|v\|_2\eta,
\]

and truncating the right side at zero proves (L-9505.11) and
(L-9505.12).

Under RH, (L-9505.2) is a sum of positive-semidefinite rank-one blocks.  Apply
the lower half of (L-9505.19) to every certified zero assigned to a bin and
leave every other zero block untouched.  This proves (L-9505.8).

For the stronger coverage hypothesis, subtract the lower block from one low
zero contribution:

\[
 u_\gamma u_\gamma^*
 -\left(u_cu_c^*-\varepsilon I_n\right)
 =u_\gamma u_\gamma^*-u_cu_c^*+\varepsilon I_n.
\]

By (L-9505.19), this repaired difference lies between `0` and
`2 epsilon I_n`.  Summing all low bins gives a contribution between `0` and
`2E I_n`.

For a remaining high zero,

\[
 u_\gamma u_\gamma^*
 \preceq \|u_\gamma\|_2^2 I_n,
\]

while

\[
 \|u_\gamma\|_2^2
 =n\frac{|1-e^{i\gamma h}|^2}{\gamma^2}
 \le\frac{4n}{\gamma^2}.
\]

Sum this bound over `|gamma|>T` and apply (L-9505.14).  This proves
(L-9505.15).

Finally, differentiating

\[
 u_{\gamma,j}
 =\gamma^{-1}
  \left(e^{ijh\gamma}-e^{i(j+1)h\gamma}\right)
\]

gives

\[
\begin{aligned}
 u'_{\gamma,j}
 ={}&\frac{ih}{\gamma}
 \left(je^{ijh\gamma}-(j+1)e^{i(j+1)h\gamma}\right)\\
 &-\frac{e^{ijh\gamma}-e^{i(j+1)h\gamma}}{\gamma^2}.
\end{aligned}
\]

Using `|gamma|>=a` proves (L-9505.17).  The mean-value integral along the real
interval and the Euclidean norm then prove (L-9505.18).  Equation
(L-9505.16) follows directly from the common modulus of the entries. ∎

## Motivation

The smallest undeflated Toeplitz mode can remain positive because verified
critical-line zeros contribute large, known PSD atoms.  Deflation removes a
rigorous lower block for those atoms while preserving an RH-valid residual.
The same primitive `Psi(kh)` table can therefore be reused in the sequence

```text
raw Toeplitz search
      -> certify influential zero bins
      -> subtract Loewner-lower rank-one blocks
      -> reoptimize the residual cone
      -> test both residual negativity and excess positivity.
```

Unlike subtracting an approximate zero ordinate as if it were exact, the
`epsilon I` repair makes every bin-width uncertainty explicit.

## Certificate form

A lower-deflation proof object stores

```text
h and n
primitive directed Psi(kh) rows
exact frozen Rayleigh vector
for each bin:
    rational center and radius
    certified zero lower count
    rational G, eta, epsilon
```

A two-sided certificate additionally stores exact low-zero coverage through
`T` and a rigorous `S_T`.  The checker verifies bin disjointness,
`|c_s|>r_s`, every rational norm inequality, multiplicity allocation, and the
final exact contraction.

## Analytic domain audit

All zero bins lie on the real ordinate axis and exclude zero.  Under RH the
imported `gamma` values are real, so every exponential in (L-9505.1) is
unambiguous.  No complex logarithm, contour deformation, division by `xi`, or
simplicity assumption is used.  Multiplicities are carried explicitly.

## Dependency audit

- `L-9504` supplies the RH-conditional Gram sum (L-9505.2).
- A zero-bin producer must separately prove that its bins contain the declared
  critical-line zeros.  This claim does not infer zeros from approximate
  decimals.
- The upper box additionally requires a complete zero accounting through `T`
  and a proved tail sum (L-9505.14).
- The rank-one perturbation and derivative estimates are proved here.
- Draft PR #90 contains a parallel generic Pick-kernel zero-bin lemma; no
  unmerged result from that branch is used as a dependency here.

## Gap audit

- A lower zero count is enough for (L-9505.8), but not for the upper box.
- The bins must be disjoint or their multiplicities must be allocated without
  double counting.
- Positive and negative ordinates are separate zero contributions unless a
  pair-symmetric block is constructed explicitly.
- A midpoint rank-one matrix subtraction without the `epsilon I` repair is
  unsound for a nonzero-width bin.  The fixed-vector bound (L-9505.10) is a
  different, scalar triangle-inequality certificate and must not be promoted
  to a Loewner block.
- For the upper box, every low zero must be covered exactly; omitted low zeros
  invalidate the claimed ceiling.
- The factor `2E` in (L-9505.15) is necessary: one `E` repairs the lower block,
  and another permits the low rank-one block to move upward within its bin.
- A tail bound for the zero count is not automatically a tail bound for
  `sum gamma^-2`; the required partial summation must be carried out.
- Reoptimizing after deflation is essential.  Testing only the old undeflated
  eigenvector can miss a new residual direction.

## Adversarial tests

1. Use a zero-width bin and confirm `eta=epsilon=0` gives the exact rank-one
   subtraction.
2. Set `epsilon=0` for a positive-width bin and produce a numerical violation
   of the claimed Loewner lower bound.
3. Move a bin across zero and require certificate rejection.
4. Duplicate one zero bin and require the multiplicity allocator to reject
   double counting.
5. Omit the negative conjugate ordinate from a claimed complete symmetric
   coverage and require the upper-box audit to fail.
6. Compare the derivative bound with dense high-precision samples in the
   widest proposed bin.
7. Construct a synthetic finite zero spectrum and verify both endpoints of
   (L-9505.15) directly.

## Remaining uncertainty

The theorem is finite and complete conditional on `L-9504`, but useful
sharpness depends on narrow certified zero bins.  It remains unknown whether
the repository's existing zero-certification infrastructure can supply enough
nearby bins cheaply to overcome the current positive Toeplitz margins.

## Suggested next attack

Identify the zero ordinates contributing most strongly to the smallest raw
Toeplitz eigenvector, rank them first with the fixed-vector lower bound
(L-9505.10), certify only those bins, form their repaired matrix lower blocks,
and solve the full residual eigenproblem.  If the residual remains positive,
enlarge the bin set adaptively rather than certifying zeros in ordinate order.
