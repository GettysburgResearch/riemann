# Next attack: prove the E–Widder source inequality

Status: **RESEARCH PROGRAMME; ALL COMPLETION-BEARING TARGETS BELOW ARE OPEN UNLESS MARKED AS IDENTITIES.**

The target is

\[
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \mathcal L_k(u,\log n)
 \le
 \mathcal G_k(u)
 \qquad(u>0,\ k\ge1).
 \tag{EW}
\]

The point of this note is to prevent the next pass from reverting to broad computation or merely renaming the equivalent positivity condition.  It records exact new normal forms, the first theorem-sized target and a route from that target to all orders.

## 1. Exact differential recurrence

For any smooth `q`, define

\[
 \mathcal W_k(u)=(-1)^{k-1}D^{2k-1}[u^kq(u)].
\]

Using

\[
 D^m[ug]=uD^mg+mD^{m-1}g,
\]

one obtains the exact recurrence

\[
 \boxed{
 \mathcal W_{k+1}
 =-u\mathcal W_k''-(2k+1)\mathcal W_k'.
 }
 \tag{1.1}
\]

Equivalently,

\[
 \boxed{
 \mathcal W_{k+1}
 =-u^{-2k}D\left[u^{2k+1}\mathcal W_k'\right].
 }
 \tag{1.2}
\]

This is an identity, not an RH assumption.  It holds separately for the archimedean reserve and every prime-power filter:

\[
 \mathcal G_{k+1}
 =-u\mathcal G_k''-(2k+1)\mathcal G_k',
\]

\[
 \mathcal L_{k+1}(u,\ell)
 =-u\partial_u^2\mathcal L_k(u,\ell)
 -(2k+1)\partial_u\mathcal L_k(u,\ell).
\]

Thus the all-order theorem can be phrased as a weighted flux hierarchy:

\[
 \mathcal W_{k+1}\ge0
 \iff
 D\left[u^{2k+1}\mathcal W_k'(u)\right]\le0.
\]

The first new rung is

\[
 \boxed{
 \mathcal W_2(u)
 =-D^3[u^2q(u)]
 =-u\mathcal W_1''(u)-3\mathcal W_1'(u)
 \ge0.
 }
 \tag{1.3}
\]

This is the first theorem-sized target to attack.

## 2. Lower-derivative complete-monotonicity form

Widder's full two-parameter quantities are

\[
 F_{n,k}(u)=(-1)^nD^{n+k}[u^kq(u)].
\]

For fixed `k`, define

\[
 \boxed{
 Q_k(u)=D^k[u^kq(u)].
 }
 \tag{2.1}
\]

Widder's theorem is equivalently

\[
 \boxed{
 \mathrm{RH}
 \iff
 Q_k\text{ is completely monotone for every }k\ge0.
 }
 \tag{2.2}
\]

The diagonal E–Widder functional is

\[
 \mathcal W_k=(-1)^{k-1}D^{k-1}Q_k.
\]

The `Q_k` use only `k` derivatives before the complete-monotonicity test and may be better adapted to heat/Laguerre source formulas than the direct `2k-1` derivative.

There is another exact recurrence:

\[
 \boxed{
 Q_{k+1}=uQ_k'+(k+1)Q_k.
 }
 \tag{2.3}
\]

Under RH,

\[
 Q_k(u)=2k!\sum_{\gamma>0}m_\gamma
 \frac{a_\gamma^k}{(u+a_\gamma)^{k+1}},
 \qquad a_\gamma=\gamma^2+1/4,
\]

which is manifestly completely monotone.

A viable source proof can therefore target either:

```text
all W_k >= 0;
or
all Q_k completely monotone.
```

The second is stronger term by term but has a lower-order primary derivative.

## 3. Normalized Hausdorff microscope

Define

\[
 \boxed{
 C_k(u)=
 \frac{(4u)^k}{2(2k-1)!}\mathcal W_k(u),
 \qquad k\ge1.
 }
 \tag{3.1}
\]

Under RH,

\[
 \boxed{
 C_k(u)=
 \sum_{\gamma>0}m_\gamma
 \lambda_u(a_\gamma)^k,
 }
 \tag{3.2}
\]

where

\[
 \boxed{
 \lambda_u(a)=\frac{4ua}{(u+a)^2}
 =\operatorname{sech}^2\left(\frac12\log\frac au\right)
 \in(0,1].
 }
 \tag{3.3}
\]

For fixed `u`, the finite measure

\[
 d\nu_u(\lambda)
 =\sum_{\gamma>0}m_\gamma
 \lambda_u(a_\gamma)\,
 \delta_{\lambda_u(a_\gamma)}
\]

satisfies

\[
 C_k(u)=\int_{[0,1]}\lambda^{k-1}\,d\nu_u(\lambda).
\]

Thus RH yields an invariant-coordinate Hausdorff moment sequence:

\[
 (-1)^m\Delta^mC_k(u)
 =\sum_{\gamma>0}m_\gamma
 \lambda_u(a_\gamma)^k
 [1-\lambda_u(a_\gamma)]^m
 \ge0.
 \tag{3.4}
\]

It also yields all shifted Hankel and Bernstein-cell inequalities.

This normal form supplies a spectral microscope.  Writing

\[
 v=\log(a/u),
\]

we have

\[
 \lambda_u(a)^k
 =\operatorname{sech}^{2k}(v/2)
 =\exp\left[-\frac{k}{4}v^2+O(kv^4)\right]
\]

near `v=0`.  Large Widder order localizes invariant zero mass to logarithmic width `O(k^{-1/2})` around `a=u`.

A source-side proof should seek the corresponding localization directly in the prime filters, rather than differentiating expanded formulas blindly.

## 4. Generating function in Widder order

Under RH, for fixed `u`,

\[
 \sum_{k\ge1}C_k(u)w^{k-1}
 =\sum_{\gamma>0}m_\gamma
 \frac{\lambda_u(a_\gamma)}
 {1-w\lambda_u(a_\gamma)}.
 \tag{4.1}
\]

This is a Stieltjes/Pick function of `w` on the unit disk.  An off-line invariant zero produces a complex transformed atom and should create either a nonreal pole geometry or a failed Hausdorff cell.

The generating function is useful for proof organization, but the earlier safe-line annulus firewall must be respected: no termwise Euler continuation is assumed outside its absolute domain.  The fixed-order E–Widder formula remains the safe arithmetic front door.

## 5. First target: the weighted curvature theorem

The recommended first theorem is

\[
 \boxed{
 D\left[u^3\mathcal W_1'(u)\right]\le0
 \qquad(u>0).
 }
 \tag{5.1}
\]

By (1.2), this is exactly `W_2>=0`.

The theorem should be proved in the literal form

\[
 \mathcal G_2(u)
 \ge
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \mathcal L_2(u,\log n).
 \tag{5.2}
\]

A proof of (5.1) would be the first genuinely new sign beyond the already reviewed first-order monotonicity.  It would not prove RH by itself, but it would validate the differential-recursive route and expose the exact all-order obstruction.

## 6. Source decomposition of the first target

Use

\[
 D_u=\frac1{2x}D_x,
 \qquad u=x^2-1/4.
\]

Do not expand all derivatives into a large polynomial at the outset.  Generate the filters recursively from `L_1` using (1.1), preserving:

- the common exponential `e^{-ell x}`;
- exact rational functions of `x`;
- the sign-changing polynomial in `ell`;
- the common source sum before absolute values.

The archimedean part should be put into a polygamma/Laplace integral before comparison.  The prime side should remain the complete von Mangoldt translation sum.  A termwise sign proof is neither expected nor required.

## 7. Three geometric regimes in `u`

### 7.1 Terminal Euler-safe regime

For each fixed `k`, use Stirling's expansion for the digamma term and the exponential smallness of the prime series as `s=1/2+x` tends to infinity.  The leading term of `q` is

\[
 q(u)=\frac{\log u}{4\sqrt u}
 +O(u^{-1/2}),
\]

and the leading logarithmic coefficient has the correct Widder sign.  The concrete target is an effective `U_k` such that

\[
 \mathcal W_k(u)>0
 \qquad(u\ge U_k).
\]

This should be proved analytically, not inferred from sampling.

### 7.2 Compact source regime

On `epsilon<=u<=U`, every differentiated Euler series converges uniformly and admits explicit prime-cutoff tails.  This is the right region for exact symbolic simplification, interval reconnaissance and testing candidate factorizations.

Finite verification is useful here only to discover the factorization or inequality that will later be proved uniformly.

### 7.3 Functional-equation boundary `u->0+`

At `u=0`, `xi_R` is nonzero and `q` is analytic, but the separated formula

\[
 2/u+\text{gamma term}-\text{prime term}
\]

contains a cancellation of the zeta pole.  The archimedean and prime pieces must not be bounded separately by singular absolute estimates.

Construct a pole-subtracted source identity before estimating the boundary.  Candidate coordinates include:

- the Chebyshev error measure `d psi(x)-dx`;
- a pole-subtracted logarithmic derivative;
- a compactly supported or Abel-regularized explicit-formula kernel;
- the invariant Taylor coefficients of `mathfrak X'/mathfrak X`.

The cancellation must remain exact.

## 8. Heat/Laguerre lane

The integrated safe-line work already proves that discrete Hausdorff differences are generalized-Laguerre filters of first-Hermite heat time.  The new invariant hierarchy should be connected to that basis.

Concrete target:

1. express `Q_k` or `W_k` as an integral over first-Hermite heat time;
2. identify the exact generalized-Laguerre or Bessel filter produced by the invariant derivative `D_u=(2x)^{-1}D_x`;
3. keep the complete theta/prime sum inside the integral;
4. prove a variation-diminishing or square-completion theorem for the coupled filter.

Modewise `PF_infinity` is forbidden by the positive-sum firewall.  The theorem must act on the completed sum.

## 9. Prime-shift operator lane

The operator form is

\[
 T=T_{\rm gamma}
 -\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 e^{-(\log n)A_0}.
\]

The full result is `T+T^*>=0` on the exponential core.  A source-local factorization

\[
 T+T^*=V^*V
\]

would close RH immediately.

The next finite theorem is the four-exponential Schur complement.  It must be derived inside the unquotiented gamma-plus-prime form.  Bounding the translation sum after a nonorthogonal projection would repeat the #770 error mode.

The finite theorem is reconnaissance: fixed packet size four cannot replace the all-order factorization.

## 10. Differential induction lane

The recurrence (1.2) suggests the cone

\[
 \mathcal C_k=
 \left\{
 h:\ h\ge0,
 \ D[u^{2k+1}h']\le0
 \right\}.
\]

A complete induction would prove

\[
 \mathcal W_k\in\mathcal C_k
 \quad\Longrightarrow\quad
 \mathcal W_{k+1}\ge0
\]

while also establishing the hypothesis for the next order.

The missing source theorem may be a weighted complete-monotonicity or total-positivity property of the deficit sequence, rather than a separate estimate at every `k`.

A generic positivity-preserving claim for the differential operator is false; the proof must use the literal source or an invariant cone with sufficient derivative control.

## 11. Hausdorff-cell lane

The normalized sequence `C_k(u)` suggests proving the shifted Bernstein-cell inequalities

\[
 \boxed{
 B_{N,j}(u)
 =\binom Nj(-1)^{N-j}\Delta^{N-j}C_{j+1}(u)
 \ge0,
 \qquad 0\le j\le N.
 }
 \tag{11.1}
\]

Under RH,

\[
 B_{N,j}(u)
 =\sum_{\gamma>0}m_\gamma
 \binom Nj
 \lambda_u(a_\gamma)^{j+1}
 [1-\lambda_u(a_\gamma)]^{N-j}.
\]

These are beta/Bernstein cells of the invariant spectral coordinate `lambda_u(a)`.  They sum to `C_1(u)` and localize transformed spectral distance.

The source-side question is whether the complete prime filters admit an exact beta-cell decomposition with a positive archimedean reserve.  This is the most direct bridge to the existing Hausdorff/Laguerre repository machinery.

## 12. Computation that is worth doing

Useful bounded work:

- exact recursion and simplification of `G_k` and `L_k`;
- directed evaluation on compact `(u,k)` panels;
- asymptotic saddle extraction in `k`;
- search for square completions or positive integral kernels;
- rigorous prime-cutoff remainder bounds at fixed `u>0`;
- testing the weighted flux `D[u^{2k+1}W_k']` rather than raw high derivatives;
- comparing invariant Bernstein cells with existing safe-line Laguerre cells.

Work to avoid:

- another unstructured Xi zero scan;
- sparse companion panels without a cofinal frame theorem;
- modewise total-positivity tests;
- absolute prime envelopes;
- finite-order positivity extrapolated to all order.

## 13. End-to-end completion protocol

A successful pass should aim to deliver the following chain in one argument:

```text
literal pole-subtracted gamma-plus-prime source
-> invariant heat/flux or Hausdorff decomposition
-> all-order source inequality (EW)
-> q is Stieltjes by Widder
-> invariant zeros lie on the negative real axis
-> every nontrivial zeta zero has beta=1/2
-> RH.
```

If the all-order step fails, the pass should still freeze the sharpest theorem-sized intermediate result, preferably `W_2>=0`, an effective terminal theorem, or an exact positive recursion with one clearly named source remainder.

## 14. Immediate priority

The recommended immediate order is:

1. prove the exact recurrences in a checker and in prose;
2. derive a compact pole-subtracted formula for `W_2`;
3. prove terminal positivity for `W_2`;
4. attack the remaining compact/boundary source form without quotienting;
5. identify whether the successful mechanism extends through (1.1) or through the `Q_k` complete-monotonicity hierarchy;
6. only then generalize to all `k` and close RH.

The project should treat `W_2` as a mechanism-discovery theorem, not as an endpoint substitute.
