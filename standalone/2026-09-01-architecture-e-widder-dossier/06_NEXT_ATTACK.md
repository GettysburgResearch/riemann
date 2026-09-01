# Next attack: pass from the finite-height Widder cone to all orders

Status: **RESEARCH PROGRAMME; THE E–WIDDER SOURCE INEQUALITY IS PROVED THROUGH ORDER `4.71*10^12`; ITS UNBOUNDED-ORDER FORM AND RH REMAIN OPEN.**

The target is

\[
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \mathcal L_k(u,\log n)
 \le
 \mathcal G_k(u)
 \qquad(u>0,\ k\ge1).
 \tag{EW}
\]

[`08_FINITE_HEIGHT_WIDDER_CONE.md`](08_FINITE_HEIGHT_WIDDER_CONE.md) proves `(EW)` for every `u>0` and every

\[
 1\le k\le4{,}710{,}000{,}000{,}000.
\]

The previous plan treated `W_2>=0` as the first new sign.  That frontier is obsolete: the complete diagonal hierarchy is now paid through more than four trillion orders, and a matching finite rectangle of the full Widder cone is paid as well.

The remaining problem is qualitative rather than merely quantitative.  One needs a **height-free mechanism** preventing phase rotation of hypothetical off-line invariant zero atoms at unbounded Widder order.

## 1. Exact differential recurrence

For any smooth `q`, define

\[
 \mathcal W_k(u)=(-1)^{k-1}D^{2k-1}[u^kq(u)].
\]

Using

\[
 D^m[ug]=uD^mg+mD^{m-1}g,
\]

one obtains

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

This identity holds separately for the archimedean reserve, every prime-power filter and their complete deficit.

A successful induction must prove not only `W_k>=0` but a source-specific derivative cone strong enough to make

\[
 D[u^{2k+1}W_k']\le0
\]

at the next order.  The differential operator is not positivity preserving on a generic cone.

## 2. Full Widder and lower-derivative coordinates

Define

\[
 F_{n,k}(u)=(-1)^nD^{n+k}[u^kq(u)]
\]

and

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

The exact recurrence

\[
 \boxed{
 Q_{k+1}=uQ_k'+(k+1)Q_k
 }
 \tag{2.3}
\]

may be better suited to a heat or source-flow proof because it takes only one new derivative at each stage.

The finite-height theorem already proves

\[
 F_{n,k}(u)>0
\]

through the complete region

\[
 \max\{k,n+1\}\le4{,}710{,}000{,}000{,}000.
\]

Any inductive theorem must genuinely escape this finite rectangle rather than reprove low orders.

## 3. Exact invariant-atom obstruction

Without assuming RH, the genus-zero product gives

\[
 F_{n,k}(u)
 =2(n+k)!\sum_a
 \frac{a^k}{(u+a)^{n+k+1}},
 \qquad
 a=-\rho(\rho-1).
 \tag{3.1}
\]

For an off-line zero `rho=beta+i gamma`, write

\[
 a=A+iB,
 \qquad
 A=\gamma^2+\beta(1-\beta),
 \qquad
 B=-\gamma(2\beta-1).
\]

Then

\[
 |\arg a|<\arctan(1/|\gamma|).
\]

If

\[
 \theta=\arg a,
 \qquad
 \phi=\arg(u+a),
\]

the phase of the atom in (3.1) is

\[
 \Psi_{n,k}=k\theta-(n+k+1)\phi
\]

and obeys

\[
 |\Psi_{n,k}|\le\max\{k,n+1\}|\theta|.
 \tag{3.2}
\]

This is the exact reason a finite verified height buys a finite Widder cone.  It also identifies what an all-order proof must defeat: when `k` becomes comparable to a hypothetical zero height, the atom can rotate through a right angle.

The one-way localization theorem is

\[
 \boxed{
 \mathcal W_k(u)<0
 \Longrightarrow
 \text{an off-line zero below height }
 \cot\left(\frac\pi{2k}\right).
 }
 \tag{3.3}
\]

Thus a proof at order `k` only needs arithmetic information through height approximately `2k/pi`, but the all-order theorem requires a uniform mechanism as that height grows.

## 4. Normalized Hausdorff microscope

Define

\[
 \boxed{
 C_k(u)=
 \frac{(4u)^k}{2(2k-1)!}\mathcal W_k(u).
 }
 \tag{4.1}
\]

Under RH,

\[
 C_k(u)=
 \sum_{\gamma>0}m_\gamma
 \lambda_u(a_\gamma)^k,
 \qquad
 \lambda_u(a)=\frac{4ua}{(u+a)^2}.
 \tag{4.2}
\]

For positive real `a`,

\[
 \lambda_u(a)
 =\operatorname{sech}^2\left(\frac12\log\frac au\right)
 \in(0,1].
\]

Large order localizes invariant spectral mass to logarithmic width

\[
 O(k^{-1/2})
\]

around `a=u`.  In the false-RH geometry, the same microscope sees complex atoms with a phase amplified by `k`.

A source proof should therefore seek a **localized reserve theorem at scale `u~gamma^2`**, not a global absolute tail bound.  Low fixed critical zeros cannot dominate a hypothetical high off-line atom after localization.

## 5. The new primary target: localized source reserve

The useful next theorem is not the literal order

\[
 4{,}710{,}000{,}000{,}001.
\]

It is an all-scale statement that acts before Widder order is chosen.

### Localized E-reserve theorem `LER`

Construct, from the pole-subtracted gamma-plus-prime source, a positive measure or positive quadratic form `R_u` such that for every `k>=1`

\[
 \boxed{
 C_k(u)
 =\int_{[0,1]}\lambda^{k-1}\,dR_u(\lambda),
 \qquad R_u\ge0.
 }
 \tag{LER}
\]

A source-local construction of `R_u` closes all Hausdorff differences, all `W_k`, the Stieltjes theorem and RH at once.

This is stronger than merely estimating each derivative, but it is exactly adapted to the normalized microscope.  An arbitrary measure obtained from the zeros would be tautological; `R_u` must be built from theta, gamma and prime labels before zero information is used.

Equivalent acceptable targets are:

```text
source-local Stieltjes measure for q;
source-local Gram factorization of A_Phi;
source-local factorization T+T*=V*V;
positive Bernstein-cell decomposition of every C_k(u).
```

## 6. Bernstein-cell formulation

For `N>=0` and `0<=j<=N`, define

\[
 \boxed{
 B_{N,j}(u)
 =\binom Nj(-1)^{N-j}\Delta^{N-j}C_{j+1}(u).
 }
 \tag{6.1}
\]

Under RH,

\[
 B_{N,j}(u)
 =\sum_{\gamma>0}m_\gamma
 \binom Nj
 \lambda_u(a_\gamma)^{j+1}
 [1-\lambda_u(a_\gamma)]^{N-j}
 \ge0.
 \tag{6.2}
\]

The cells sum to `C_1(u)` and resolve the invariant spectral distance from `a=u`.  The source-side goal is an exact beta-cell decomposition in which the complete prime sum remains assembled before absolute values.

The existing safe-line Laguerre/Hausdorff transforms should be compared with these invariant cells.  A successful intertwiner between the two cell systems would be a plausible route to `LER`.

## 7. Heat/Laguerre lane

Use

\[
 D_u=\frac1{2x}D_x,
 \qquad u=x^2-1/4.
\]

Seek an exact representation of `Q_k`, `W_k` or `B_(N,j)` as an integral over first-Hermite heat time.  The desired theorem must:

1. identify the generalized-Laguerre/Bessel filter generated by invariant differentiation;
2. keep the completed theta or prime sum inside the integral;
3. preserve the pole cancellation at `u=0`;
4. produce a square, variation-diminishing operator or positive beta-cell measure for the complete coupled source.

Modewise `PF_infinity` remains forbidden: positive sums of totally-positive atoms need not be totally positive.

## 8. Prime-shift operator lane

On the exponential core,

\[
 T=T_{\rm gamma}
 -\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 e^{-(\log n)A_0}.
\]

The all-order theorem is

\[
 T+T^*\succeq0.
\]

A source-local factorization

\[
 T+T^*=V^*V
\]

would close RH immediately.  Every prime translation, gamma term and boundary term must remain in one quadratic form.  Quotienting or norm-bounding the prime shifts separately repeats the source-loss barriers of PR #770.

Finite four-exponential Schur complements remain useful reconnaissance, but no fixed packet size can replace the all-order factorization.

## 9. Zero-orbit compensation lane

The invariant atom formula suggests a conditional analytic target:

\[
 \sum_{\text{off-line pairs}}
 \left[
 \Re\frac{a^k}{(u+a)^{2k}}
 \right]_{-}
 \le
 \sum_{\text{critical atoms}}
 \frac{a^k}{(u+a)^{2k}}.
 \tag{9.1}
\]

Proving (9.1) from independent information about local critical-line density, zero-free regions and multiplicity would also establish `W_k>=0`.

However, global positive-proportion theorems are not automatically enough: the microscope localizes to a narrow logarithmic height window and a negative off-line pair can have phase close to `pi`.  Any compensation theorem must be local at the `O(k^(-1/2))` invariant scale and retain multiplicity.

This lane is secondary to a source-local factorization because it risks rebuilding RH through zero statistics.

## 10. Three `u` regimes

### 10.1 Functional-equation boundary `u->0+`

The separated formula

\[
 2/u+\text{gamma term}-\text{prime term}
\]

contains exact pole cancellation.  Construct a pole-subtracted source identity before estimating.  Bounding the two singular pieces separately is forbidden.

### 10.2 Compact Euler-safe regime

On `epsilon<=u<=U`, every differentiated Euler series converges uniformly and admits directed prime-cutoff tails.  Use this only to test or certify a proposed factorization, not to extrapolate finite order.

### 10.3 Large `u`

For each fixed `k`, Stirling and prime exponential decay give terminal positivity.  This is now far weaker than the global finite-height theorem and does not address the joint regime `k~sqrt(u)` where hypothetical high zeros are detected.

The real asymptotic problem is a two-parameter saddle in `(u,k)` with `u` of order `k^2`.

## 11. Differential-induction lane

The recurrence (1.2) suggests a source-dependent cone

\[
 \mathcal C_k=
 \{h:\ h\ge0,\ D[u^{2k+1}h']\le0\}.
\]

A full induction must propagate enough derivative information to place `W_(k+1)` in the next cone.  A generic positivity claim is false.  The candidate cone must be justified by the literal theta/prime source or by a positive integral representation.

The finite-height theorem can serve as an enormous base case, but a finite base case does not by itself help an induction whose propagation theorem is missing.

## 12. Computation worth doing

Useful work:

- exact recursive generation of `G_k`, `L_k` and invariant Bernstein cells;
- asymptotic analysis in the joint scaling `u~k^2`;
- search for a heat-time intertwiner between safe-line Laguerre cells and invariant cells;
- exact symbolic testing of candidate source Gram factorizations;
- directed compact checks only after a uniform identity is proposed;
- local zero-orbit phase studies to calibrate the reserve required by (9.1).

Work to avoid:

- raw derivatives at order `4.71*10^12+1`;
- another broad zero scan;
- modewise positivity;
- absolute prime envelopes;
- sparse finite packets promoted to all order;
- treating the finite-height theorem as an all-order argument.

## 13. End-to-end completion protocol

A successful continuation must deliver

```text
literal pole-subtracted gamma-plus-prime source
-> source-local invariant measure / Gram / Bernstein cells
-> all-order (EW)
-> q is Stieltjes by Widder
-> invariant zeros lie on the negative real axis
-> every nontrivial zeta zero has beta=1/2
-> RH.
```

The present checkpoint has completed the finite-height part:

```text
published RH verification through 3*10^12
-> exact invariant angular theorem
-> full Widder cone through 4.71*10^12
-> strict (EW) through 4.71*10^12.
```

The next pass should attack `LER`, not a low-order scalar inequality.
