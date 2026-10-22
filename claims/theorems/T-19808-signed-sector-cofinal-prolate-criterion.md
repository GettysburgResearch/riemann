# T-19808 — A signed-sector `d_6` cofinal prolate theorem implies RH

Claim ID: `T-19808`  
Status: **PROPOSED CORRECTED COMPOSITION THEOREM — FOUR GLOBAL ANALYTIC INPUTS OPEN**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Dependencies: finite Rayleigh-floor transfer `T-15103`; moving-Hardy cutoff `L-16213`; pure-prolate signed hierarchy `L-19823`; corrected support adapter `L-19822`; CCM Proposition 5.7, Theorem 5.10, and Lemma 7.3  
Scope: corrected successor to reviewed `T-19807`; no present RH proof

## 1. Purpose

The reviewed proposal `T-19807` used two invalid load-bearing statements:

1. the rejected quarter-power lemma `L-19821`;
2. a complete target-complement gap at scale `d_8`, although the `-1` Fourier
   sector supplies a lower `d_6` direction.

This theorem states the exact repaired composition. The finite and limiting
logic still works after:

- replacing `L-19821` by the branchwise theorem `L-19822`;
- replacing the complete `d_8` hierarchy by a signed `d_6` hierarchy;
- normalizing the local-Weyl error relative to `log R`;
- requiring a quantitative complete source frame, not qualitative surjectivity.

## 2. Complete signed finite frame

Let

\[
 R=2\pi\lambda^2,
 \qquad
 N_\lambda=\lceil c(\log\lambda)^2\rceil,
 \qquad c>2/\pi^2,
 \tag{T-19808.1}
\]

and let `V_R` be the complete finite CCM space used by the finite real-zero
theorem. It contains both Fourier-sign sectors.

Assume there is a finite exact-radical source space

\[
 \mathcal U_R=\mathcal U_{R,+}\oplus\mathcal U_{R,-}
 \tag{T-19808.2}
\]

and an exact source synthesis

\[
 \mathscr E_R:\mathcal U_R\longrightarrow V_R
 \tag{T-19808.3}
\]

such that:

1. every source satisfies `f(0)=0` and `integral f=0`;
2. `mathscr E_R` is onto and one-to-one after the declared finite coordinate
   quotient;
3. for the ordinary finite-space metric `H_R` and the moving-Hardy coefficient
   metric `M_R`,

   \[
   \|\mathscr E_R\|+\|\mathscr E_R^{-1}\|
   \le(\log R)^{C_0},
   \tag{T-19808.4}
   \]

   and

   \[
   M_R\preceq K_RH_R,
   \qquad
   K_R\le(\log R)^{C_1}.
   \tag{T-19808.5}
   \]

The inverse bound must hold on a positive-measure subset of every sufficiently
large support block. Merely avoiding the countable exact zeta-cycle set is not
sufficient.

## 3. Exact omitted-tail and Weil forms

Let

\[
 D_R\succeq0
\]

be the complete arithmetic omitted-tail Gram in the exact source coordinates,
and let

\[
 A_R
\]

be the exact finite localized Weil form in the same coordinates. The global
radical identity supplies the equality between the localized source form and the
omitted-tail zero-side form.

Let `p_R` be an `H_R`-normalized, inversion-even repaired target. Put

\[
 \mu_D(R)=\langle D_Rp_R,p_R\rangle.
 \tag{T-19808.6}
\]

## 4. Signed arithmetic-tail hierarchy

Assume constants `C_4,c_6>0` exist such that

\[
 \boxed{
 \mu_D(R)\le C_4d_4(R),}
 \tag{T-19808.7}
\]

and, on the complete `H_R`-orthogonal target complement,

\[
 \boxed{
 D_R-\mu_D(R)H_R
 \succeq c_6d_6(R)H_R.}
 \tag{T-19808.8}
\]

The pure prolate model satisfies first scales `d_4,d_6` by `L-19823`. A
proof-grade arithmetic route to (T-19808.8) may split the two Fourier-sign
sectors and prove

```text
+1 target complement: scale d_8,
-1 sector:            scale d_6,
complete constrained Schur floor: scale d_6.
```

That arithmetic transfer is a hypothesis of this theorem, not an established
result.

The fixed-mode Fuchs hierarchy gives

\[
 {d_4(R)\over d_6(R)}\longrightarrow0.
 \tag{T-19808.9}
\]

## 5. Correct relative local-Weyl estimate

Assume that on a positive-measure set of supports in every sufficiently large
dyadic block,

\[
 A_R=(\log R)D_R+E_R
 \tag{T-19808.10}
\]

and define the dimensionless relative error

\[
 \boxed{
 \eta_R
 :={
 \|D_R^{-1/2}E_RD_R^{-1/2}\|_{\rm op}
 \over\log R}.}
 \tag{T-19808.11}
\]

Require

\[
 \eta_R\longrightarrow0.
 \tag{T-19808.12}
\]

This corrects `T-19807.12`, which omitted the division by `log R` while using
`epsilon_R` as a relative error in its next display.

Equivalently,

\[
 \boxed{
 (1-\eta_R)(\log R)D_R
 \preceq A_R\preceq
 (1+\eta_R)(\log R)D_R.}
 \tag{T-19808.13}
\]

A proposed route to (T-19808.12) is:

1. the line-centered Selberg/Stieltjes estimate;
2. the branchwise support average `L-19822` for horizontal displacement;
3. a complete collective endpoint and infinite-alias operator ledger;
4. the quantitative signed source-frame theorem of Section 2.

## 6. Finite floor and complete gap

For all sufficiently large `R`, `eta_R<1`, so (T-19808.13) and `D_R>=0` give

\[
 A_R\succeq0.
 \tag{T-19808.14}
\]

Thus a rigorous global lower floor is

\[
 L_R=0.
 \tag{T-19808.15}
\]

The target Rayleigh quotient obeys

\[
 \mu_A(R)
 \le(1+\eta_R)(\log R)C_4d_4(R).
 \tag{T-19808.16}
\]

For every `x perpendicular_(H_R) p_R`, (T-19808.8) and (T-19808.13) give

\[
\begin{aligned}
 \langle A_Rx,x\rangle-\mu_A(R)\langle H_Rx,x\rangle
 \ge(\log R)\bigl[&
 (1-\eta_R)c_6d_6(R)\\
 &-2\eta_RC_4d_4(R)
 \bigr]\langle H_Rx,x\rangle.
\end{aligned}
 \tag{T-19808.17}
\]

Define

\[
 g_R=(\log R)
 \left[(1-\eta_R)c_6d_6(R)
       -2\eta_RC_4d_4(R)\right].
 \tag{T-19808.18}
\]

Then `g_R>0` eventually and

\[
 \boxed{
 {\mu_A(R)-L_R\over g_R}
 \le
 {(1+\eta_R)C_4d_4(R)
  \over
  (1-\eta_R)c_6d_6(R)-2\eta_RC_4d_4(R)}
 \longrightarrow0.}
 \tag{T-19808.19}
\]

This is the corrected `d_4/d_6` ratio.

## 7. Moving-Hardy ground-line transfer

From (T-19808.5), the ordinary complement floor (T-19808.17) implies the
moving-Hardy coercivity

\[
 A_R-\mu_A(R)H_R
 \succeq {g_R\over K_R}M_R
 \tag{T-19808.20}
\]

on the target complement.

Let `t_R` be the moving-Hardy target projection tail. Assume

\[
 t_R\longrightarrow0
 \tag{T-19808.21}
\]

and that the projected target norm remains bounded above and below. The
Rayleigh-floor estimate then gives a target-to-ground error bounded by

\[
 t_R+C
 \sqrt{K_R{\mu_A(R)-L_R\over g_R}}.
 \tag{T-19808.22}
\]

Because `K_R` is polylogarithmic while the fixed-mode ratio `d_4/d_6` decays by
a positive power of `lambda`, (T-19808.19) implies

\[
 K_R{\mu_A(R)-L_R\over g_R}\longrightarrow0.
 \tag{T-19808.23}
\]

Hence the exact finite ground line is simple, has the parity of the inversion-even
target, and converges projectively to that target in the moving Hardy norm.

The quadratic-log cutoff `L-16213` supplies (T-19808.21) once the exact source
normalization and signed-frame adapter are established.

## 8. Cofinal support selection

Suppose the quantitative frame bound, signed hierarchy, branchwise
support-average estimates, endpoint/alias ledgers, and relative local-Weyl bound
hold simultaneously outside bad-support sets whose total relative measure tends
to zero in every dyadic block.

Then one may select

\[
 R_j\in[T_j,2T_j],
 \qquad T_j\to\infty,
\]

outside all bad sets and all exact zeta-cycle supports. The quantitative frame
bound must already hold on the selected positive-measure set; deleting only the
exact singular points does not create it.

## 9. CCM and Hurwitz conclusion

At the selected supports, let `xi_j` be the exact finite simple-even ground
states. The preceding sections yield nonzero real scalars `c_j` such that

\[
 \|c_j\xi_j-k_{\lambda_j}\|_{\lambda_j,\tau_j}
 \longrightarrow0,
 \qquad
 \tau_j\nearrow1/2.
 \tag{T-19808.24}
\]

CCM Proposition 5.7 and Theorem 5.10 imply that every finite transform has only
real zeros. CCM Lemma 7.3 and the Hardy-strip estimate give local-uniform
convergence to `Xi`. Hurwitz then excludes every nonreal centered zero of `Xi`.

Therefore the hypotheses of Sections 2--5 imply

\[
 \boxed{\mathrm{RH}.}
 \tag{T-19808.25}
\]

## 10. Exact unresolved theorem list

The conditional composition is now repaired, but its global hypotheses are not
proved. A full proof requires all four of the following.

1. **Quantitative signed source frame.** Both Fourier-sign sectors map onto the
   complete finite CCM space with polylogarithmic right-inverse norm on a
   positive-measure support set.
2. **Signed arithmetic-tail hierarchy.** The actual omitted-tail form has target
   scale `d_4` and complete complement scale `d_6` in one common metric.
3. **Complete holomorphic branch/alias theorem.** The shrinking-strip WKB/Airy
   decomposition, one support derivative, and collective endpoint/infinite-alias
   bounds hold uniformly on the growing packet.
4. **Full relative local-Weyl theorem.** Equation (T-19808.12) holds at one
   support in every sufficiently large block.

None is a routine checker consequence. Until all four are proved:

```text
corrected prolate route: SERIOUS CONDITIONAL PATH
accepted proof of RH:    NO
status:                  GAPS/BLOCKED
```
