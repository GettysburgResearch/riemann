# T-19807 — Whole-matrix diagonal lower envelope

Claim ID: `T-19807`  
Title: A vanishing lower bound for rapidly densifying finite Weil matrices proves RH without a ground-state or ambient-complement theorem  
Status: `PROPOSED — COMPLETE FINITE-TO-GLOBAL THEOREM; SOURCE-PROFILE LMI INTERFACES EXPLICIT`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: Weil's positivity criterion; the exact finite CCM/Weil matrix normalization; `L-19818`, `L-19819` for the proposed source-frame producer  
Scope: global positive attack on RH

## 1. Strategic change

Most positive routes in the repository try to prove one of the following at each
support:

1. convergence of a finite ground state to a prolate target;
2. a lower bound for the complete infinite localized operator;
3. positivity of a finite low block plus a separate infinite-complement floor.

None is necessary for a diagonal proof of global Weil positivity.

It is enough to construct finite Fourier spaces whose union is dense in a Weil
form core and prove that the **whole finite matrix** has a lower bound tending to
zero.  No finite eigenvector must be identified, and no omitted complement at a
fixed support must be bounded.

## 2. Finite diagonal spaces

Let

\[
 I_j=[-L_j/2,L_j/2],
 \qquad L_j\longrightarrow\infty,
 \tag{T-19807.1}
\]

and let

\[
 V_j=\operatorname{span}
 \left\{
 {1\over\sqrt{L_j}}e^{2\pi ikt/L_j}:|k|\leq N_j
 \right\}
 \subset L^2(I_j).
 \tag{T-19807.2}
\]

Every vector is extended by zero outside `I_j`.  Put

\[
 H_j={2\pi N_j\over L_j}
 \tag{T-19807.3}
\]

for the largest Fourier frequency.

Let `Q_W` denote the exact global Weil quadratic form in the repository's fixed
logarithmic convention.  Let `A_j` and `G_j` be its exact matrix and the ordinary
`L^2` Gram on `V_j`:

\[
 c^*A_jc=Q_W(v_c),
 \qquad
 c^*G_jc=\|v_c\|_2^2.
 \tag{T-19807.4}
\]

## 3. Main finite-to-global theorem

Assume

\[
 \boxed{
 A_j\succeq-\rho_jG_j,
 \qquad
 \rho_j\longrightarrow0.
 }
 \tag{T-19807.5}
\]

Assume furthermore that the bandwidth is chosen so that the finite Fourier
projections are dense in one compact Gevrey Weil core.  A sufficient explicit
schedule is

\[
 \boxed{
 H_j=\exp(L_j^\theta),
 \qquad 0<\theta<\frac12.
 }
 \tag{T-19807.6}
\]

Then the Riemann hypothesis is true.

## 4. Gevrey diagonal approximation

Fix `s>1`.  Let `G_c^s(\mathbb R)` be the compactly supported Gevrey class on the
real logarithmic line.  For

\[
 f\in G_c^s(\mathbb R)
\]

there are constants `C,c>0` such that

\[
 |\widehat f(\xi)|\leq C e^{-c|\xi|^{1/s}}.
 \tag{T-19807.7}
\]

Take `j` so large that the support of `f` lies in the middle third of `I_j`, and
let `P_jf` be its Fourier-series projection onto `V_j`.  Since the periodic
copies of `f` are disjoint, the complete periodic Fourier series equals `f` on
`I_j`.  Truncating at `H_j` gives, for every fixed derivative order `m`,

\[
 \boxed{
 \|P_jf-f\|_{W^{m,\infty}(I_j)}
 \leq C_{f,m}
 e^{-c_fH_j^{1/s}}.
 }
 \tag{T-19807.8}
\]

The same estimate holds for every endpoint jet of `P_jf`, because `f` vanishes
on a neighborhood of the endpoints.

With (T-19807.6),

\[
 e^{-c_fH_j^{1/s}}
 =\exp\{-c_f e^{L_j^\theta/s}\},
 \tag{T-19807.9}
\]

which beats `e^{-CL_j}` for every fixed `C`.

## 5. Continuity of the Weil form along the diagonal

A crude support-dependent explicit-formula bound is sufficient.  There are a
fixed integer `m` and constants `C_1,C_2` such that, for functions supported in
`I_L`,

\[
 \boxed{
 |Q_W(f,g)|
 \leq
 C_1e^{C_2L}
 \|f\|_{W^{m,\infty}}
 \|g\|_{W^{m,\infty}}.
 }
 \tag{T-19807.10}
\]

One proof separates the standard explicit formula into:

1. the logarithmic/archimedean distribution, controlled by finitely many
   Sobolev or variation seminorms;
2. the finite prime-translation family, whose absolute coefficient sum is at
   most exponential in the support radius;
3. the scalar and endpoint terms.

The elementary bound

\[
 \sum_{n\leq e^{2L}}{\Lambda(n)\over\sqrt n}
 \leq CLe^L
 \tag{T-19807.11}
\]

is already more than enough.  No prime cancellation enters this density step.

Equations (T-19807.8)--(T-19807.10) imply

\[
 \boxed{
 Q_W(P_jf)\longrightarrow Q_W(f),
 \qquad
 \|P_jf\|_2\longrightarrow\|f\|_2.
 }
 \tag{T-19807.12}
\]

The zero extensions of `P_jf` may have tiny endpoint jumps; their complete
variation and every fixed endpoint jet are bounded by the right side of
(T-19807.8), so the same estimate covers those jumps.

## 6. Proof of RH

By (T-19807.5),

\[
 Q_W(P_jf)
 \geq-\rho_j\|P_jf\|_2^2.
 \tag{T-19807.13}
\]

Taking the limit and using (T-19807.12) gives

\[
 Q_W(f)\geq0
 \qquad(f\in G_c^s).
 \tag{T-19807.14}
\]

Compact Gevrey functions are dense in the ordinary compact smooth Weil test
space in every fixed finite collection of test-function seminorms.  The Weil
distribution is continuous on that test space.  Therefore

\[
 Q_W(f)\geq0
\]

for every admissible Weil test function.  Weil's criterion gives RH. QED.

## 7. Why this theorem is globally weaker than the previous positive gates

The theorem does **not** require:

- a simple or even finite ground state;
- convergence of any eigenvector;
- a Hurwitz limit of finite characteristic functions;
- a lower bound for the infinite localized complement at the same support;
- positivity of every finite matrix;
- a deterministic support formula.

The finite matrices may have negative eigenvalues at every level, provided their
lowest generalized eigenvalue is bounded below by `-rho_j` with `rho_j->0`.

A conforming finite matrix normally gives only an upper Ritz bound for an
ambient localized ground value.  That objection is irrelevant here: the matrix
is used as a diagonal form core, not as a lower approximation to one fixed
ambient operator.

## 8. One source-profile LMI that produces the finite lower bound

Let

\[
 R_j=e^{L_j}.
\]

Suppose the complete finite space `V_j` has an exact source frame and a positive
profile Gram `D_j`.  Choose `tau_j>0` and put

\[
 \widehat D_j=D_j+\tau_jG_j.
 \tag{T-19807.15}
\]

Let `A_j^0` be the line-centered zero comparator.  Assume the two-sided
source-profile estimates

\[
 \boxed{
 A_j^0
 \succeq
 [\log R_j-C_0-\alpha_j]D_j
 -\alpha_j\tau_jG_j,
 }
 \tag{T-19807.16}
\]

and

\[
 \boxed{
 -\delta_j\widehat D_j
 \preceq A_j-A_j^0
 \preceq\delta_j\widehat D_j.
 }
 \tag{T-19807.17}
\]

If

\[
 \alpha_j+\delta_j=o(\log R_j)
 \tag{T-19807.18}
\]

and

\[
 \boxed{
 (\alpha_j+\delta_j)\tau_j\longrightarrow0,
 }
 \tag{T-19807.19}
\]

then, for all sufficiently large `j`, the coefficient of `D_j` in the lower
bound is nonnegative and

\[
 \boxed{
 A_j\succeq-\rho_jG_j,
 \qquad
 \rho_j=(\alpha_j+\delta_j)\tau_j\longrightarrow0.
 }
 \tag{T-19807.20}
\]

Therefore (T-19807.16)--(T-19807.19) imply RH by the main theorem.

This is a whole-matrix theorem.  There is no hard/soft spectral split and no
harmonic Schur block unless those are useful internally for producing the LMI.

## 9. Rate supplied by the smooth complete frame

Use the source frame of `L-19819`.  Let its unwhitened graph envelope be

\[
 {\mathfrak M}_R=R^{1/4+o(1)}
 \tag{T-19807.21}
\]

and choose

\[
 \boxed{
 \tau_R={{\mathfrak M}_R\over\sqrt R}
 =R^{-1/4+o(1)}.
 }
 \tag{T-19807.22}
\]

Then the regularized **vector-profile** envelope is

\[
 \boxed{
 M_R^{\rm vec}
 =\left({{\mathfrak M}_R^2\over\tau_R}\right)^{1/2}
 =R^{3/8+o(1)}.
 }
 \tag{T-19807.23}
\]

The source dimension is

\[
 d_R=R^{o(1)}.
 \tag{T-19807.24}
\]

Assume the line-centered profile family satisfies the natural Bessel upper
bound

\[
 E_R\ll R\log R
 \tag{T-19807.25}
\]

in the same regularized metric.  Applying the rank-one theorem `L-19818` to the
complete reflected/off-line cross block gives

\[
 {1\over R}\int_R^{2R}
 \|A_s-A_s^0\|_{\widehat D_s}^2ds
 \leq
 R^{-1/4+o(1)}.
 \tag{T-19807.26}
\]

Hence every sufficiently large support block contains a point for which

\[
 \boxed{
 \delta_R=R^{-1/8+o(1)}.
 }
 \tag{T-19807.27}
\]

At that point,

\[
 \delta_R\tau_R=R^{-3/8+o(1)}\longrightarrow0.
 \tag{T-19807.28}
\]

The ordinary line-centered counting, endpoint, Airy, and Poisson errors may be
placed in `alpha_R`.  The dimension-free local-Weyl and endpoint ledgers target

\[
 \alpha_R=o(\log R),
 \qquad
 \alpha_R\tau_R\to0.
 \tag{T-19807.29}
\]

Thus the power budget has a large reserve: the complete smooth frame is
compatible with a whole-matrix lower envelope once the source-specific
Bessel/local-Weyl identities are established.

## 10. Exact remaining source-specific interfaces

The global reduction leaves three concrete interfaces.

### A. Finite matrix/source identity

Prove in one immutable normalization that the periodized smooth cardinal source
frame of `L-19819` produces the exact finite CCM/Weil matrix and its zero-side
profile matrix, including every restriction/periodization and endpoint term.

### B. Line-centered Bessel local-Weyl estimate

Prove (T-19807.16) and (T-19807.25) for the complete `R^(o(1))` source frame.
This is a positive zero-count/profile estimate; it contains no off-line sign.

### C. Complete phase ledger

Show that every term in `A-A^0` is either:

1. a rank-one oscillatory phase family covered by `L-19818`;
2. an Airy/fold window of vanishing total budget;
3. an explicitly bounded endpoint/Poisson remainder included in `alpha_R`.

These are source/normalization/oscillatory-analysis statements.  They are not a
new scalar criterion equivalent to RH and do not ask for a priori positivity of
the actual matrix.

## 11. Serious resolution path

If interfaces A--C are verified, equations

\[
 A_j\succeq-\rho_jG_j,
 \qquad \rho_j\to0
\]

hold on a rapidly densifying diagonal.  Sections 3--6 then give global Weil
positivity and RH.

This is a serious full-problem route because it removes the previously separate
obligations of ground-state identification, complete ambient complement
coercivity, visible-block positivity, and soft-sector sign.  All finite
directions are treated together, and the final global passage is direct.

## 12. Proof boundary

- The finite-to-global lower-envelope theorem and its Gevrey density proof are
  complete.
- The algebraic implication (T-19807.16)--(T-19807.20) is exact.
- `L-19818` supplies the new rank-one support-average estimate, and `L-19819`
  supplies a sufficiently dense exact smooth source frame.
- Interfaces A--C have not yet been independently established in one production
  normalization.  Therefore this file is a full resolution proposal, not a
  claimed proof of RH.
