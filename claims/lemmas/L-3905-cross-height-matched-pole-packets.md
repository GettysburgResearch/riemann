# L-3905 — Cross-height complex matched-pole Pick packets

Claim ID: L-3905  
Title: Complex barycentric Pick packets use vertical phase coherence while annihilating a modeled off-line zero pair  
Status: PROPOSED  
Authoring agent: `gpt56-04-d`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: D-3201; L-3202; exact Gaussian-rational arithmetic  
Scope: arbitrary-height finite Pick matrices for `F=xi'/xi` in `Re(s)>1/2`  
Related counterexample candidates: none

## Statement

Fix an integer `n>=2`, a rational model ordinate `Gamma`, distinct Gaussian-rational nodes

\[
 z_j=x_j+i y_j\in\mathbf Q(i),\qquad x_j>0,
 \qquad 1\le j\le n,
\]

and a positive rational model parameter `d` such that `z_j^2 != d` for every `j`. Put

\[
 s_j=\frac12+z_j+i\Gamma,
 \qquad
 P(z)=\prod_{j=1}^n(z-z_j),
 \qquad
 w_j=\frac1{P'(z_j)}.
\]

Define

\[
 \alpha_j(d)=\frac{z_j}{z_j^2-d},
 \qquad
 \beta_j(d)=\frac1{z_j^2-d},
\]

\[
 S_0=\sum_jw_j\alpha_j(d),
 \qquad
 S_1=\sum_jw_jz_j\alpha_j(d),
 \qquad
 D(d)=\prod_j(z_j^2-d),
\]

and

\[
 \lambda_j=D(d)w_j(S_1-S_0z_j),
 \qquad
 c_j=\overline{\lambda_j}.
 \tag{1}
\]

All quantities in (1) lie exactly in `Q(i)`.

Let

\[
 F(s)=\frac{\xi'(s)}{\xi(s)}
\]

and form the arbitrary-height Pick matrix

\[
 K_{jk}=
 \frac{F(s_j)+\overline{F(s_k)}}
 {s_j+\overline{s_k}-1}.
 \tag{2}
\]

Then the following assertions hold.

### A. RH-valid finite witness

If RH holds, `K` is positive semidefinite by L-3202, hence

\[
 c^*Kc\ge0.
 \tag{3}
\]

Consequently an exact Gaussian-rational vector and directed primitive `F(s_j)` rectangles that imply

\[
 c^*Kc<0
\]

form a finite RH-disproof witness, subject to the D-3201/L-3202 normalization and primitive-value gates.

### B. Exact arbitrary-height contraction

For any exact complex vector `c`, define

\[
 a_j=\overline{c_j}
 \sum_{k=1}^n
 \frac{c_k}{s_j+\overline{s_k}-1}.
 \tag{4}
\]

Then

\[
 \boxed{
 c^*Kc=2\operatorname{Re}\sum_{j=1}^na_jF(s_j).}
 \tag{5}
\]

Thus the exact checker needs each primitive complex rectangle only once. Writing `a_j=A_j+iB_j` and `F(s_j)=U_j+iV_j`, the checked real functional is

\[
 2\sum_j(A_jU_j-B_jV_j).
 \tag{6}
\]

Unlike every same-height real-vector contraction previously used in X-3902/X-3903, (6) retains the imaginary parts of `F` and the vertical phase information between different ordinates.

### C. Moment cancellation

The vector (1) satisfies

\[
 \sum_j\lambda_jz_j^k=0
 \qquad(0\le k\le n-3),
 \tag{7}
\]

with an empty range when `n=2`.

### D. Exact modeled-pair annihilation

The same vector satisfies

\[
 \sum_j\lambda_j\alpha_j(d)=0,
 \qquad
 \sum_j\lambda_j\beta_j(d)=-1.
 \tag{8}
\]

Suppose a zero orbit contains, with multiplicity `m>=1`, the same-ordinate reflected pair

\[
 \rho_+=\frac12+\delta+i\Gamma,
 \qquad
 \rho_-=\frac12-\delta+i\Gamma,
 \qquad
 \delta^2=d.
\]

Its contribution to (2) is the Hermitian rank-two matrix

\[
 K^{(d)}_{jk}
 =2m\left(
 \alpha_j(d)\overline{\alpha_k(d)}
 -d\,\beta_j(d)\overline{\beta_k(d)}
 \right).
 \tag{9}
\]

Therefore

\[
 \boxed{c^*K^{(d)}c=-2md.}
 \tag{10}
\]

The positive rank-one component is annihilated exactly, while the negative component is normalized to one.

### E. Two-parameter mismatch formula

Let an actual pair have horizontal displacement squared `q>0` and ordinate `Gamma+epsilon`. Put

\[
 z_j(\epsilon)=z_j-i\epsilon,
\]

\[
 A(q,\epsilon)=
 \sum_j\lambda_j
 \frac{z_j(\epsilon)}{z_j(\epsilon)^2-q},
 \qquad
 B(q,\epsilon)=
 \sum_j\lambda_j
 \frac1{z_j(\epsilon)^2-q}.
\]

Away from poles, its exact contribution is

\[
 c^*K^{(q,\epsilon)}c
 =2m\left(|A(q,\epsilon)|^2-q|B(q,\epsilon)|^2\right).
 \tag{11}
\]

At the model point `(q,epsilon)=(d,0)`, equation (8) gives `A=0`, `B=-1`, and (11) equals `-2md`. Hence the isolated pair remains negative on a nonempty open neighborhood in both horizontal displacement and ordinate. For rational `q,epsilon`, every quantity in (11) is Gaussian rational and can be checked exactly.

### F. Suppression of distant critical-line zeros

Let

\[
 R=\max_j|z_j|,
 \qquad
 C=\sum_j|\lambda_j|.
\]

For a critical-line zero with ordinate offset `Y=Gamma-gamma` and `|Y|>R`, its Gram amplitude satisfies

\[
 \left|
 \sum_j\frac{\lambda_j}{z_j+iY}
 \right|
 \le
 \frac{CR^{n-2}}
 {|Y|^{n-1}(1-R/|Y|)}.
 \tag{12}
\]

Thus the nonnegative background contribution of that zero is `O(|Y|^{-2n+2})`. Vertical node freedom can improve modeled-pair localization and primitive-rectangle conditioning without sacrificing the exact moment suppression inherited from L-3904.

## Proof

### Exact contraction

Expand the quadratic form from (2):

\[
 c^*Kc=
 \sum_{j,k}\overline{c_j}c_k
 \frac{F(s_j)}{s_j+\overline{s_k}-1}
 +
 \sum_{j,k}\overline{c_j}c_k
 \frac{\overline{F(s_k)}}{s_j+\overline{s_k}-1}.
\]

The second double sum is the complex conjugate of the first after interchanging `j` and `k`. Grouping the first sum by `j` proves (4)--(5). Expanding the real part proves (6).

### Barycentric identities over `Q(i)`

The partial-fraction identity

\[
 \frac1{P(z)}=\sum_j\frac{w_j}{z-z_j}
\]

holds over every characteristic-zero field, hence over `Q(i)`. Comparing the expansion at infinity gives

\[
 \sum_jw_jz_j^k=0
 \qquad(0\le k\le n-2).
 \tag{13}
\]

Substituting (1) into the left side of (7) and using (13) at powers `k` and `k+1` proves the moment cancellation.

The alpha overlap vanishes immediately:

\[
 \sum_j\lambda_j\alpha_j
 =D(S_1S_0-S_0S_1)=0.
\]

For the beta overlap, work temporarily in a quadratic extension containing a symbol `r` with `r^2=d`. Put

\[
 T_0=\sum_j\frac{w_j}{z_j^2-d}.
\]

As in L-3904,

\[
 S_1=dT_0,
\]

and partial fractions at `r` and `-r` give

\[
 T_0=\frac1{2r}
 \left(\frac1{P(-r)}-\frac1{P(r)}\right),
\]

\[
 S_0=-\frac12
 \left(\frac1{P(r)}+\frac1{P(-r)}\right).
\]

Therefore

\[
 dT_0^2-S_0^2=-\frac1{P(r)P(-r)}.
\]

But

\[
 P(r)P(-r)=\prod_j(r-z_j)(-r-z_j)
 =\prod_j(z_j^2-d)=D(d).
\]

It follows that

\[
 \sum_j\lambda_j\beta_j
 =D(d)(dT_0^2-S_0^2)=-1,
\]

proving (8). The final identity lies in `Q(i)` and does not require choosing a numerical square root of `d`.

### Pair matrix

Relative to the model ordinate, the two zero coordinates are `+delta` and `-delta`. Their contribution to `F(s_j)` is

\[
 \frac1{z_j-\delta}+rac1{z_j+\delta}
 =\frac{2z_j}{z_j^2-d}.
\]

Substitution into the shifted Pick denominator `z_j+conj(z_k)` gives

\[
 \frac{2}{z_j+\overline{z_k}}
 \left(
 \frac{z_j}{z_j^2-d}
 +\frac{\overline{z_k}}{\overline{z_k}^2-d}
 \right)
 =2\frac{z_j\overline{z_k}-d}
 {(z_j^2-d)(\overline{z_k}^2-d)},
\]

which is (9). Contracting (9) and applying (8) proves (10). Replacing `z_j` by `z_j-i epsilon` and `d` by `q` proves (11).

### Distant-zero suppression

For `|Y|>R`, expand absolutely:

\[
 \frac1{z_j+iY}
 =\sum_{k=0}^{\infty}
 \frac{(-z_j)^k}{(iY)^{k+1}}.
\]

Equation (7) cancels every term through `k=n-3`. Bounding the remaining geometric tail gives (12).

## Why this is a genuinely new search direction

The rigorous X-3902 and X-3903 scans used one common ordinate and real vectors. Their exact contractions consequently depend only on `Re F(s_j)`. L-3905 permits:

- arbitrary exact ordinates;
- exact complex vectors;
- exact use of both `Re F` and `Im F`;
- target packets whose vertical offsets are comparable to the modeled horizontal displacement;
- the same modeled-pair value `-2md` as L-3904;
- stronger proposal conditioning in finite exact proxy searches.

This does not assert that a particular packet is negative for Riemann `xi`; the complete direct interval alone decides.

## Analytic and domain audit

- Every sample has `x_j>0`, so every Pick denominator has positive real part.
- Nodes, center, model parameter, and vector are exact rationals or Gaussian rationals.
- The final checker evaluates no zero model and assumes no zero location.
- Every primitive `xi` or `zeta` denominator ball must exclude zero before contraction.
- A negative modeled-pair score is proposal metadata only.
- Equation (11) controls only the isolated pair component, not the complete zero background.

## Dependency audit

- D-3201 fixes the completed-`xi` logarithmic derivative and shifted half-plane.
- L-3202 supplies arbitrary-point Pick positivity under RH.
- L-3905 supplies the exact vector, contraction, and modeled-pair algebra.
- PR #56/X-3902 supplies primitive directed `F(s)` rectangles and two-assembly gates.

No dependency is promoted by this lemma.

## Gap audit

1. A direct negative interval still requires independent special-function reproduction.
2. Reusing one Arb primitive table for many adaptively selected vectors is mathematically safe, but selection does not make the producer independent.
3. Large Gaussian-rational coefficients can amplify both real and imaginary rectangle widths.
4. The target pair may be vertically or horizontally mismatched; only the complete direct contraction is decisive.
5. Passing a finite packet family says nothing universal about RH.
6. The D-3201/L-3202 canonical-product normalization remains `PROPOSED` pending independent review.

## Adversarial tests

1. Verify (7)--(10) exactly over `Fraction` pairs for dimensions two through six.
2. Compare (5) with direct matrix contraction for arbitrary synthetic complex primitive values.
3. Require a finite critical-line zero model to give a nonnegative direct packet value.
4. Require the exact modeled off-line pair to give `-2d`.
5. Mutate one point ordinate, vector coefficient, or model center and require the identity checker to reject.
6. Widen a primitive rectangle through zero and require an unresolved rather than negative verdict.
7. Check that the same-height real-node specialization agrees with L-3904.

## Suggested next attack

Evaluate exact three- and five-node vertical packets at the optimized and earlier carrier basins with Arb at two precisions. Rank only complete normalized direct intervals. If all fixed model packets remain positive, use their common primitive table to nominate exact Gaussian-dyadic minimum-eigenvector packets, then replay those vectors unchanged at higher precision.