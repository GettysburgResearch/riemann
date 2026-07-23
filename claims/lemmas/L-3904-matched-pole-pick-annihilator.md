# L-3904 — Matched-pole barycentric Pick annihilators

Claim ID: L-3904  
Title: An exact rational Pick vector can annihilate the positive rank-one part of a modeled off-line zero pair  
Status: PROPOSED  
Authoring agent: `gpt56-02-e`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: `D-3201`; `L-3202`; the same-ordinate zero-pair calculation used by `L-3901` and `L-3902`  
Scope: exact fixed-vector `xi'/xi` Pick certificates at one ordinate  
Related counterexample candidates: none

## Statement

Fix an integer `n>=2`, distinct positive rational nodes

\[
 x_1,\ldots,x_n>0,
\]

and a positive rational model parameter `d` with `x_i^2 != d` for every `i`.
Put

\[
 P(z)=\prod_{i=1}^n(z-x_i),
 \qquad
 w_i=\frac1{P'(x_i)}
     =\frac1{\prod_{j\ne i}(x_i-x_j)},
\]

\[
 \alpha_i(d)=\frac{x_i}{x_i^2-d},
 \qquad
 S_0=\sum_iw_i\alpha_i(d),
 \qquad
 S_1=\sum_iw_ix_i\alpha_i(d),
\]

and

\[
 D(d)=\prod_i(x_i^2-d).
\]

Define the exact rational vector

\[
 c_i=D(d)w_i\bigl(S_1-S_0x_i\bigr).
 \tag{1}
\]

For a fixed real ordinate `T`, let

\[
 s_i=\frac12+x_i+iT
\]

and let `K=K(T;x_1,...,x_n)` be the real same-height Pick matrix

\[
 K_{ij}=
 \frac{F(s_i)+\overline{F(s_j)}}{x_i+x_j},
 \qquad
 F=\frac{\xi'}\xi,
 \tag{2}
\]

in the normalization of `D-3201`.

Then the following hold.

### 1. RH positivity and exact contraction

If RH holds, then

\[
 c^{\mathsf T}Kc\ge0.
 \tag{3}
\]

For real `c`, the quadratic form is the exact real linear functional

\[
 c^{\mathsf T}Kc
 =\sum_{i=1}^n q_i\operatorname{Re}F(s_i),
 \qquad
 q_i=2c_i\sum_{j=1}^n\frac{c_j}{x_i+x_j}.
 \tag{4}
\]

Thus an outward interval for the right side of (4) with negative upper endpoint is a finite RH-disproof witness, subject to the parent normalization and zero-resolvent audit.

### 2. Moment cancellation

The vector (1) satisfies

\[
 \sum_i c_ix_i^k=0
 \qquad(0\le k\le n-3),
 \tag{5}
\]

with the range empty when `n=2`.

### 3. Exact annihilation of a modeled pair

The same vector satisfies

\[
 \sum_i c_i\frac{x_i}{x_i^2-d}=0,
 \qquad
 \sum_i c_i\frac1{x_i^2-d}=-1.
 \tag{6}
\]

Suppose a zero orbit contains, with multiplicity `m>=1`, the same-ordinate pair

\[
 \rho_+=\frac12+\delta+i\gamma,
 \qquad
 \rho_-=\frac12-\delta+i\gamma,
 \qquad
 \delta^2=d,
\]

and evaluate at `T=gamma`. Its contribution to (2) is

\[
 K^{(d)}_{ij}
 =2m\frac{x_ix_j-d}
 {(x_i^2-d)(x_j^2-d)}
 =2m\left(\alpha_i(d)\alpha_j(d)
           -d\beta_i(d)\beta_j(d)\right),
 \tag{7}
\]

where `beta_i(d)=1/(x_i^2-d)`. Consequently

\[
 c^{\mathsf T}K^{(d)}c=-2md.
 \tag{8}
\]

The positive rank-one component is annihilated exactly, while the negative rank-one component has a fixed rational value. Multiplying `c` by a nonzero rational or integer scale preserves the sign.

### 4. Exact mismatch polynomial

For a possible actual squared displacement `q>0`, define

\[
 D_q=\prod_i(x_i^2-q),
\]

\[
 U(q)=\sum_i c_ix_i\prod_{j\ne i}(x_j^2-q),
 \qquad
 V(q)=\sum_i c_i\prod_{j\ne i}(x_j^2-q).
 \tag{9}
\]

Away from the node squares, the actual pair contribution is exactly

\[
 c^{\mathsf T}K^{(q)}c
 =2m\frac{U(q)^2-qV(q)^2}{D_q^2}.
 \tag{10}
\]

At the model point,

\[
 U(d)=0,
 \qquad
 V(d)=-D(d),
 \qquad
 U(d)^2-dV(d)^2=-dD(d)^2<0.
 \tag{11}
\]

Therefore the matched pair remains negative on a nonempty open interval of model mismatch. Because every quantity in (9) is a rational polynomial, a proposed interval can be checked by exact rational root isolation or a directed interval evaluation.

### 5. Suppression of distant critical-line zeros

Let

\[
 R=\max_i x_i,
 \qquad
 C=\sum_i|c_i|.
\]

For a critical-line zero with ordinate offset `y=T-gamma` and `|y|>R`, its Gram amplitude satisfies

\[
 \left|\sum_i\frac{c_i}{x_i+iy}\right|
 \le
 \frac{CR^{n-2}}
 {|y|^{n-1}(1-R/|y|)}.
 \tag{12}
\]

Thus its nonnegative Pick contribution is bounded by the square of (12), namely `O(|y|^(-2n+2))`. The construction spends one interpolation degree on exact pole matching and uses the remaining degrees to suppress distant critical-line background.

## Motivation

`L-3901` gives a model-free product localizer whose off-line sign is controlled by how many horizontal nodes lie below the hidden displacement. `L-3902` gives two sign-complete two-point channels. The present construction is complementary: after a reconnaissance model proposes a squared displacement `d`, it produces one exact rational vector that removes the modeled pair's positive component algebraically.

This matters for proof-grade search because:

1. no interval eigenvector is required;
2. the vector and contraction coefficients are exact rationals;
3. the target-pair value is exactly `-2md` under the model;
4. model mismatch has a finite polynomial certificate;
5. additional nodes suppress remote critical-line background.

The model is only a proposal parameter. A negative fitted or modeled value is never a certificate. The final object is the direct outward interval for (4).

## Proof

### RH positivity

Under RH, `L-3202` gives the zero-resolvent Gram representation

\[
 K_{ij}
 =\sum_\gamma
 \frac1{x_i+i(T-\gamma)}
 \frac1{x_j-i(T-\gamma)}.
\]

Hence, for every real or complex fixed vector,

\[
 c^*Kc
 =\sum_\gamma
 \left|\sum_i\frac{c_i}{x_i+i(T-\gamma)}\right|^2
 \ge0.
\]

For real `c`, direct contraction of (2) gives (4).

### Barycentric moment identities

The standard partial-fraction identity

\[
 \frac1{P(z)}=\sum_i\frac{w_i}{z-x_i}
\]

implies

\[
 \sum_iw_ix_i^k=0
 \qquad(0\le k\le n-2).
 \tag{13}
\]

For `0<=k<=n-3`, substitute (1):

\[
 \sum_ic_ix_i^k
 =D(d)\left(
 S_1\sum_iw_ix_i^k
 -S_0\sum_iw_ix_i^{k+1}
 \right)=0,
\]

which proves (5).

Also,

\[
 \sum_ic_i\alpha_i(d)
 =D(d)(S_1S_0-S_0S_1)=0.
\]

It remains to compute the beta overlap.

Put

\[
 T_0=\sum_i\frac{w_i}{x_i^2-d}.
\]

Because `sum_i w_i=0`,

\[
 S_1=\sum_iw_i\frac{x_i^2}{x_i^2-d}=dT_0.
\]

Moreover `S_0=sum_i w_i x_i/(x_i^2-d)`. Therefore

\[
 \sum_i\frac{c_i}{x_i^2-d}
 =D(d)(dT_0^2-S_0^2).
 \tag{14}
\]

Work temporarily in the quadratic extension containing `r` with `r^2=d`. From the partial-fraction identity,

\[
 T_0=\frac1{2r}
 \left(\frac1{P(-r)}-\frac1{P(r)}\right),
\]

\[
 S_0=-\frac12
 \left(\frac1{P(r)}+\frac1{P(-r)}\right).
\]

Thus

\[
 dT_0^2-S_0^2=-\frac1{P(r)P(-r)}.
\]

But each factor satisfies

\[
 (r-x_i)(-r-x_i)=x_i^2-d,
\]

so `P(r)P(-r)=D(d)`. Equation (14) is therefore `-1`, proving (6). The result lies in the ground rational field, so the temporary quadratic extension introduces no branch or irrational input into the certificate.

### Pair matrix

At `T=gamma`, the pair contributes to `F(s_i)`

\[
 m\left(\frac1{x_i-\delta}+\frac1{x_i+\delta}\right)
 =\frac{2mx_i}{x_i^2-d}.
\]

Substitution into (2) gives

\[
 K^{(d)}_{ij}
 =\frac{2m}{x_i+x_j}
 \left(\frac{x_i}{x_i^2-d}
       +\frac{x_j}{x_j^2-d}\right),
\]

which simplifies to (7). Equations (6) and (7) yield (8).

### Mismatch polynomial

For actual squared displacement `q`, the two overlaps are

\[
 \sum_i c_i\frac{x_i}{x_i^2-q}=\frac{U(q)}{D_q},
 \qquad
 \sum_i c_i\frac1{x_i^2-q}=\frac{V(q)}{D_q}.
\]

Substitution into the rank-two form proves (10). Equation (6) gives (11), and continuity of the polynomial numerator gives the open negative mismatch interval.

### Distant-zero bound

For `|y|>R`, expand absolutely:

\[
 \frac1{x_i+iy}
 =\sum_{k=0}^\infty
 \frac{(-x_i)^k}{(iy)^{k+1}}.
\]

By (5), all terms through `k=n-3` cancel. Taking absolute values from `k=n-2` onward gives

\[
 \left|\sum_i\frac{c_i}{x_i+iy}\right|
 \le
 \sum_i|c_i|
 \sum_{k=n-2}^\infty\frac{x_i^k}{|y|^{k+1}}
 \le
 \frac{CR^{n-2}}{|y|^{n-1}(1-R/|y|)},
\]

which proves (12).

## Analytic and domain audit

- Every certificate node lies strictly in `Re(s)>1/2`.
- The modeled `d` is a positive rational search parameter and must avoid every node square.
- The final evaluator must prove every sampled `xi` or `zeta` denominator excludes zero.
- The algebraic vector construction uses only rational arithmetic.
- The temporary symbol `r^2=d` appears only inside a proof of a rational identity.
- No zero location, multiplicity, or modeled displacement is assumed in the final sign check.

## Dependency audit

- `D-3201` fixes `xi`, `F`, and the corrected completion convention.
- `L-3202` supplies the conditional Pick Gram representation.
- Standard functional-equation and conjugation symmetries supply the same-ordinate reflected zero.
- The pair calculation is independently reproduced above.

No dependency is promoted by this lemma.

## Gap audit

1. The exact negative in (8) belongs to the modeled pair component, not automatically to the complete Riemann `xi` function.
2. Other zeros and completion terms are already part of the actual `F` evaluations; they must not be dropped or approximated by a fitted background.
3. A model parameter selected from the same noisy data is proposal-only. The final vector must be frozen before directed evaluation.
4. Large rational coefficients can amplify pointwise ball widths. The exact coefficients in (4) must be published with an `L1` uncertainty budget.
5. A negative ordinary midpoint, eigenvalue, or modeled pair score is not a candidate.
6. The mismatch polynomial controls only the isolated target-pair contribution; it is not a bound for the complete background.
7. Passing any finite collection of matched filters is not evidence for RH.

## Adversarial tests

1. Verify (5)--(8) exactly for node counts `2` through `6` using `Fraction` arithmetic.
2. Compare (10) with direct rank-two contraction at a mismatched rational displacement.
3. Check an exact open negative mismatch interval around the model point.
4. Evaluate finite critical-line zero models and require every complete Pick quadratic form to remain nonnegative.
5. Mutate one node, model parameter, or vector coefficient and require at least one exact identity to fail.
6. Reject duplicate, nonpositive, or pole-touching nodes rather than silently perturbing them.
7. Widen actual `F` rectangles through zero and require the certificate checker to become unresolved.

## Remaining uncertainty

The algebraic identities are complete-looking and have exact finite regression tests. Their practical detection power for Riemann `xi` depends on model nomination, coefficient conditioning, and rigorous high-height special-function evaluation. No actual matched-filter negative has been found.

## Suggested next attack

Add a `matched-pole-real-pick` producer mode to the active Arb branch PR #56. Its `L-3903` exact-contraction checker already accepts the resulting rational vector, so the proof path requires no new trusted matrix code:

1. nominate a rational `d` from scalar/two-channel reconnaissance;
2. build (1) exactly and record the moment, alpha, and beta identities;
3. compute the exact coefficients (4) and their error amplification;
4. evaluate all points in one shared Arb batch;
5. freeze only intervals with a negative upper endpoint;
6. independently reproduce any survivor before allocating a candidate ID.
