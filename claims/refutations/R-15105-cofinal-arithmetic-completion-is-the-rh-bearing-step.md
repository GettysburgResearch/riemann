# R-15105 — Cofinal arithmetic completion is the RH-bearing step, not a remaining soft estimate

Claim ID: `R-15105`  
Status: **PROVED SCOPE/OBSTRUCTION THEOREM**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: `T-15104`, `L-15108`, `L-15111`, `L-15114`; Rouché/Hurwitz; the off-line cardinal identity of PR #179  
Scope: the exact logical status of the requested cofinal residue-line and relative-LMI statements  
Related counterexample candidates: none

## 1. Statement

Let `F_j` be any sequence of real entire finite CvS transforms satisfying

\[
 F_j\longrightarrow\Xi
 \tag{R-15105.1}
\]

locally uniformly on the open centered critical strip

\[
 |\operatorname{Im}z|<\frac12.
\]

Let `p_j` be their finite target vectors and let `T_j(c)` be the complete
arithmetic target-pinned scalar line.

Then the following cofinal assertion

\[
 \boxed{
 \exists\text{ an unbounded retained sequence and }c_j\in\mathbb R
 \text{ such that }
 T_j(c_j)\succeq0,
 \quad
 \ker T_j(c_j)=\mathbb Rp_j}
 \tag{R-15105.2}
\]

implies RH.

In the simple-real-root regime, (R-15105.2) is exactly

\[
 \boxed{
 \mu_j^*=\sup_c\min_k w_{j,k}(c)>0}
 \tag{R-15105.3}
\]

at every retained level.  Equivalently it is the existence of the strict
relative Loewner sandwiches or of a nonempty exact Bézoutian threshold
interval.

Consequently the requested cofinal positivity is **not** a technical lemma left
after the finite algebra.  It is the substantive RH-bearing arithmetic theorem.

## 2. Direct proof by an off-line zero

Assume RH is false.  Let

\[
 z_0\notin\mathbb R,
 \qquad
 |\operatorname{Im}z_0|<\frac12,
 \qquad
 \Xi(z_0)=0.
\]

Choose a closed disk `D` centered at `z_0`, compactly contained in the strip,
disjoint from the real axis, and with boundary containing no zero of `Xi`.
Put

\[
 m_D=\min_{z\in\partial D}|\Xi(z)|>0.
\]

Local uniform convergence gives, for all sufficiently large `j`,

\[
 \sup_{z\in\partial D}|F_j(z)-\Xi(z)|<m_D.
\]

Rouché's theorem therefore gives at least one zero of `F_j` inside `D`.
That zero is nonreal.

But a positive semidefinite special matrix with one-dimensional even kernel
`Rp_j` makes every zero of `F_j` real by the finite Connes--van Suijlekom
theorem.  Hence, for every sufficiently large `j`,

\[
 \boxed{
 \nexists c\in\mathbb R:
 T_j(c)\succeq0,
 \quad
 \ker T_j(c)=\mathbb Rp_j.}
 \tag{R-15105.4}
\]

This proves the contrapositive of (R-15105.2).

In particular, when the target polynomial is simple and real-rooted enough for
the residue coordinates to be defined, false RH forces the exact line/orthant
intersection to fail eventually:

\[
 \boxed{\mu_j^*\le0}
 \tag{R-15105.5}
\]

on every sufficiently large retained level.  More commonly the target
polynomial itself has already acquired nonreal roots, in which case the
positive-residue coordinate system is unavailable because canonical positivity
has failed first.

## 3. Relative-LMI form

Suppose rational data `0<ell_j<u_j` and a canonical matrix `Q_j^can` obeyed

\[
 T_j(c_j)-\ell_jQ_j^{\rm can}\succ0,
 \qquad
 u_jQ_j^{\rm can}-T_j(c_j)\succ0
 \tag{R-15105.6}
\]

on `p_j^perp`.

Adding the two inequalities makes `Q_j^can` positive on `p_j^perp`; the first
then makes `T_j(c_j)` positive there.  Thus (R-15105.6) implies
(R-15105.2) and is likewise impossible eventually under false RH.

No uniform lower margin is required for this implication.  Even margins tending
to zero prove RH if they remain strict at every retained level.

## 4. Exact off-line cardinal mechanism

The Rouché proof gives the cleanest logical obstruction.  The zero-side Weil
form identifies its mechanism.

For a centered off-line zero `omega` of multiplicity `m`, let `k_omega` and
`k_conj(omega)` be the normalized Xi-cardinal vectors.  Their polarized Weil
block is

\[
 m\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Hence

\[
 h_\omega=k_\omega-k_{\overline\omega}
\]

satisfies

\[
 \boxed{Q_W(h_\omega,h_\omega)=-2m.}
 \tag{R-15105.7}
\]

At every real critical-line zero `gamma`,

\[
 \widehat h_\omega(\gamma)=0.
\]

Therefore every finite positive frame assembled solely from certified
critical-line zeros is blind to the exact negative direction (R-15105.7).
The complete prime-side residual must carry it.  This is why the final
one-sided residual LMI of `L-15126` is the load-bearing arithmetic statement.

If a complete finite-section hierarchy captures `h_omega` in the relevant
Hardy/form topology, then any proposed selected-line-frame decomposition must
fail one of its strict gates:

- the selected-frame floor collapses along the captured cardinal direction;
- the target-evaluation residual fails to be negligible;
- or the complete residual develops a negative generalized eigenvalue large
  enough to close the moat.

This trichotomy is not a numerical pathology.  It is the finite shadow of the
exact value `-2m`.

## 5. Consequence for permissible inputs

The following inputs do not by themselves exclude the off-line cardinal block
and therefore cannot prove (R-15105.2):

1. local-uniform convergence of the targets;
2. smooth-window or Hermite-tail decay;
3. an arbitrarily large finite set of certified critical-line zeros;
4. a positive proportion of zeros on the line;
5. phase avoidance for each frozen finite zero set;
6. phase-blind prime-number-theorem or absolute-value bounds;
7. positive canonical matrices at finitely many levels;
8. a finite empirical trend in the scalar thresholds.

A successful proof must control the **complete signed arithmetic residual** or
an exactly equivalent prime/zero object strongly enough to rule out
(R-15105.7).  PR #177's centered terminal-prime matrix and PR #179's off-line
cardinal defect are two representations of this same obstruction.

## 6. Exact status of the converse

The theorem proves

\[
 \text{cofinal arithmetic completion}\Longrightarrow\mathrm{RH}.
\]

It does **not** prove that RH implies the specific natural smooth-window
arithmetic completion.  That converse requires an additional stability theorem
for this particular finite approximation and scalar source line.  Thus the
requested statement may be strictly stronger than RH for the prescribed target
family.

For arbitrary special completions, by contrast, the cofinal existence problem
is the Laguerre--Pólya real-rooted approximation reformulation already recorded
in PR #173.  The fixed arithmetic line is narrower.

## 7. Gap audit

1. This file does not prove RH and does not prove the requested cofinal
   existence.
2. The off-line cardinal identity is exact; transferring its fixed negative
   value to a particular finite hierarchy requires the declared form-density
   and tail gates.
3. A failed sufficient residual estimate is not proof that the exact arithmetic
   line fails at that finite level; exact complement `LDL^T` remains decisive.
4. The point of the theorem is to prevent the cofinal gate from being presented
   as a routine consequence of estimates compatible with false RH.
