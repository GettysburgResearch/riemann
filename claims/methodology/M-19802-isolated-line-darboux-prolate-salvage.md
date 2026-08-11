# M-19802 — Corrected isolated-line/positive-completion salvage

Claim ID: `M-19802`  
Title: Separate arithmetic isolation and Hardy convergence from the exact positive CCM completion  
Status: **CORRECTED AFTER R-19848 — TWO OBLIGATIONS CLOSED, ONE POSITIVE-COMPLETION GATE OPEN**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-11; corrected 2026-08-11  
Depends on: `L-19862`, `L-19867`, `L-19868`, `R-19848`, and the finite CCM/Caratheodory--Fejer theorem  
Nonclaim: RH is not proved

## 1. Correction to the first version

The first version proposed that a simple isolated even **interior** eigenline of
the finite localized Weil matrix might inherit the CCM real-zero conclusion.
`R-19848` gives an exact `3 x 3` counterexample inside the CCM divided-difference
matrix class:

```text
spectrum                  -1, 0, 3
simple even target        eigenvalue 0
orthogonal singular moat  1
target residual            0
transform numerator        z^2+1.
```

Thus perfect two-sided isolation does not imply real zeros.

The first version also allowed a Darboux step of the form

\[
 \widehat\xi^{\,D}=P\widehat\xi
\]

with `P` real-rooted.  This cannot remove any nonreal zero of `hat xi`; it only
adds zeros.  That proposed escape is withdrawn.

## 2. What is now proved

### 2.1 Exact arithmetic isolated line

The exterior-cardinal residual Gram of `L-19862` has block form

\[
 D=\begin{pmatrix}m&b^*\\b&C\end{pmatrix},
 \qquad C\succeq I.
\]

With the exact metric `G=diag(1,C)`, `L-19867` proves

\[
 \|Dw\|_{G^{-1}}\ge\|w\|_G
 \qquad(w\perp p)
\]

and

\[
 \|Dp\|_{G^{-1}}^2\le m+m^2.
\]

Since `m<=C_B exp(-BL)` at any prescribed exponential rate on a suitable
cofinal cutoff, the two-sided moat is exactly `g=1` and `b/g->0`.  The resulting
generalized ground line converges exponentially to the Xi target.

### 2.2 Complete target-side moving-Hardy rate

`L-19868` proves, on one explicit quadratic-log schedule,

\[
 \|\iota_L\widetilde\xi_L-r_\Xi\|_{\tau_L}
 =O(e^{-cL}),
 \qquad
 \tau_L\uparrow1/2.
\]

Its ledger retains:

```text
exterior support tail;
all periodization copies / aliases;
exact endpoint matching after periodization;
finite Fourier cutoff;
normalization;
isolated-line displacement;
per-level directed interval radius.
```

The transforms therefore converge locally uniformly to a nonzero multiple of
`Xi` on every closed substrip.

## 3. The one surviving theorem

The remaining problem is not an abstract non-ground spectral theorem.  It is the
construction, for the **specific convergent line** `xi_j`, of an independent
positive CCM/Loewner completion.

Let

\[
 D_{0,j}=\operatorname{diag}(-N_j,\ldots,N_j),
 \qquad
 \eta_j=(1,\ldots,1)^T
\]

in the audited uncentered convention.  The required finite object is a real
parity-invariant matrix `Q_j` such that

\[
 \boxed{
 Q_j\succeq0,
 \qquad
 \ker Q_j=\mathbb C\xi_j,}
\tag{M-19802.1}
\]

and

\[
 \boxed{
 [D_{0,j},Q_j]
 =|\beta_j\rangle\langle\eta_j|
  -|\eta_j\rangle\langle\beta_j|.}
\tag{M-19802.2}
\]

Equivalently, in matrix entries,

\[
 (Q_j)_{kk}=a_{j,k},
 \qquad
 (Q_j)_{k\ell}
 ={b_{j,k}-b_{j,\ell}\over k-\ell}
 \quad(k\ne\ell),
\tag{M-19802.3}
\]

with the usual parity conditions.

If (M-19802.1)--(M-19802.3) are proved, the finite CCM theorem gives that the
Fourier transform of `xi_j` has only real zeros.  Combining this with
`L-19868` and Hurwitz proves RH.

This completion does not require `xi_j` to be the ground line of the localized
Weil matrix.  But positivity is now displayed openly in `Q_j`; it is not
silently inferred from isolation in another matrix.

## 4. Exact finite LMI form

For a fixed nonzero real vector `xi` with all coordinates retained, the
commutator relation and kernel condition are finite linear equations in the
real variables

\[
 a_k,\ b_k.
\]

Thus the remaining theorem is a concrete semidefinite feasibility problem:

\[
 \boxed{
 \text{find }(a,b)
 \text{ satisfying (M-19802.3), }Q(a,b)\xi=0,
 \text{ and }Q(a,b)|_{\xi^\perp}\succ0.}
\tag{M-19802.4}
\]

A directed certificate consists of exact rational/dyadic enclosures for `xi`,
a rational nullspace parameterization of the linear equations, and an outward
LDL proof on the complement.  The residual-Gram moat of `L-19867` is useful as
a conditioning model, but it does not itself prove that the LMI slice
(M-19802.4) intersects the positive cone.

## 5. Why the gate is conclusion-producing

The counterexample `R-19848` proves that the positive-completion cone can be
empty even when the target is perfectly isolated in another exact CCM matrix.
Conversely, the finite CCM theorem shows that any point of the cone proves the
finite real-zero statement.

Therefore the positivity of (M-19802.4) is precisely the missing real-zero
content.  It may be attacked through:

```text
an arithmetic Loewner/Pick representation;
a source-bound positive moment measure;
a total-positive or canonical-system factorization;
a rank-changing Darboux construction with an explicit no-cancellation proof.
```

A real-rooted multiplier alone is ruled out.

## 6. Correct conditional completion

The following chain is now fully rigorous as a conditional theorem:

\[
\begin{aligned}
&\text{positive CCM completion (M-19802.1)--(M-19802.3)}\\
&\quad\Longrightarrow
\text{every finite }\widehat\xi_j\text{ is real-rooted}\\
&\quad\Longrightarrow
\widehat\xi_j\to C\Xi\text{ locally uniformly by L-19868}\\
&\quad\Longrightarrow
\Xi\text{ has no nonreal zero by Hurwitz}\\
&\quad\Longrightarrow \mathrm{RH}.
\end{aligned}
\tag{M-19802.5}
\]

The first arrow is the sole open arrow.

## 7. Status boundary

```text
positive residual-Gram isolated line          PROVED (L-19867)
complete target-side moving-Hardy rate         PROVED (L-19868)
arbitrary isolated interior CCM real-zero      FALSE (R-19848)
real-rooted multiplicative Darboux repair       FALSE AS A REPAIR (R-19848)
positive CCM completion for the convergent line OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVED
```
