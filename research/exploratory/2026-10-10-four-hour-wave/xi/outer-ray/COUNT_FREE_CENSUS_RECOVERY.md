# Recover a complete simple census from finite signs and one complete moment

Status: proposed source-qualified analytic theorem and directed finite guards.
Scope: actual Xi, complete classical strip and even product, authenticated
finite Hardy-Z sign changes, and a native degree-six logarithmic jet. The
recovered census does not require a historical finite zero-count contract.
Exact dependencies: the positive theta source and complete product in
[THEOREM.md](THEOREM.md), imported primitive sign facts from
[NATIVE_SLAB_CERTIFICATE.md](NATIVE_SLAB_CERTIFICATE.md) and
[REFINED_PREFIX_MOMENTS.md](REFINED_PREFIX_MOMENTS.md), and the finite-census
column theorem in [CENSUS_FULL_COLUMN_SECTOR.md](CENSUS_FULL_COLUMN_SECTOR.md).
What was actually run: the separate checker recomputes the native degree-six
Gamma/zeta jet and all finite inverse-sixth-power interval terms, checks the
strict seed `Xi(0)>99/200`, and tests exact rational exclusion guards. It
imports the already replayed sign facts and calls no complete-count routine.
Smallest remaining gap: independent exact-source review and replay of these
new guards. None of this is a global real-zero assertion or an RH proof.

## 1. A source zero-free disk supplies a global positive angular sector

Write `F(z)=Xi(z)=xi(1/2+iz)` in its exact positive even theta form

\[
 F(z)=\int_0^\infty\cos(zu)\,d\mu(u),\qquad d\mu\ge0,
 \quad f(y)=F(-iy)=\int_0^\infty\cosh(yu)\,d\mu(u).
\tag{CF1}
\]

For every complex `z`, absolute termwise expansion of the cosine gives
`|cos(zu)-1|<=cosh(|z|u)-1`. Hence throughout `|z|<=B`,

\[
 |F(z)-F(0)|\le f(B)-F(0).
\tag{CF2}
\]

The exact classical value `zeta(6)=pi^6/945`, the Gamma recurrence, and the
functional equation give

\[
 f(11/2)=\xi(6)=2\pi^3/63.
\tag{CF3}
\]

The elementary bound `pi<22/7` can be proved directly from
`22/7-pi=integral_0^1 x^4(1-x)^4/(1+x^2) dx>0`. The directed native seed
and the strict rational comparison therefore give

\[
 F(0)>99/200,\qquad
 (22/7)^3/63<99/200,\qquad f(11/2)<2F(0).
\tag{CF4}
\]

By (CF2), `|F(z)-F(0)|<F(0)` on the whole closed disk of radius `11/2`.
Thus `F` has no zero there; the triangle inequality itself suffices, or one
may apply Rouche to the constant `F(0)` on its boundary.

The classical complete strip `|Im rho|<=A=1/2` consequently implies

\[
 |\operatorname{Re}\rho|>\sqrt{(11/2)^2-(1/2)^2}
 =\sqrt{30}>5
\tag{CF5}
\]

for every actual source zero, without using a zero census or zero count.

## 2. Select one occurrence from each strict sign change

Suppose finitely many pairwise disjoint positive real intervals `I_j` each
have authenticated strict opposite actual Hardy-Z endpoint signs. Each has
at least one real Xi zero `gamma_j`; select **one occurrence** of one such
zero from each interval. Initial uniqueness, simplicity, completeness and a
zero-count theorem are not hypotheses. Disjointness makes the selected
positive zeros distinct. Evenness removes their reflected negative
occurrences as well. If a selected zero has multiplicity greater than one,
all additional occurrences remain in the residual source.

The complete even genus-zero-in-`z^2` product from THEOREM.md gives

\[
 T=-3[z^6]\log\frac{F(z)}{F(0)}-\sum_j\gamma_j^{-6}
   =\sum_{\substack{\text{remaining}\operatorname{Re}\rho>0}}
      m_\rho\rho^{-6}.
\tag{CF6}
\]

After selection, `m_rho` denotes the remaining nonnegative integer
multiplicity. The complete sum is absolutely convergent. For nonreal roots,
retain both conjugates in the positive half-plane. The residual is real;
no unknown zero or unselected multiplicity is discarded.

By (CF5), every remaining positive-half-plane root has argument of absolute
value less than `atan(1/10)`. Put

\[
 c=\cos(6\arctan(1/10))
  =\frac{5^6-15\cdot5^4/4+15\cdot5^2/16-1/64}{(25+1/4)^3}>0.
\tag{CF7}
\]

The angle `6 atan(1/10)<3/5<pi/2` is acute, so cosine decreases on the
relevant interval. Each individual root therefore satisfies
`Re(rho^-6)>=c |rho|^-6`. Conjugate grouping and absolute convergence give

\[
 T\ge c\sum_{\text{remaining}\operatorname{Re}\rho>0}
       m_\rho |\rho|^{-6}\ge0.
\tag{CF8}
\]

This positivity uses the complete global zero-free disk and strip. It does
not assume that the unselected roots lie beyond 8192, or beyond any of the
finite sign intervals.

## 3. Exact exclusion guard forces completeness and simplicity

Let a directed native coefficient and finite interval calculation enclose
the expression in (CF6), for all allowed selected `gamma_j`, by a real
interval with upper endpoint `U`. For a fixed positive height `H`, suppose

\[
 U(H^2+1/4)^3<c.
\tag{CF9}
\]

If any remaining positive-half-plane zero had `Re rho<=H`, the strip would
give `|rho|^2<=H^2+1/4`. Its remaining multiplicity is at least one, so the
single root already contributes at least `c/(H^2+1/4)^3` to (CF8), while
all other contributions remain nonnegative. This contradicts (CF9).
A nonreal zero has its conjugate also remaining; using just one occurrence
is a valid weaker lower bound.

Consequently every actual zero with `|Re rho|<=H` is one of the selected
real zeros or its reflection. Each selected zero there is simple: any
additional occurrence at the same point would be a prohibited remaining
zero. Thus the finite sign list restricted to that height is a complete
simple real census. If no retained interval meets the boundary `H`, the
list of intervals wholly below `H` identifies this census without any
boundary ambiguity. A zero exactly at the boundary would also have been
excluded as an unselected zero, so the conclusion includes that boundary.

## 4. Native source binding and two fixed consequences

The selected list uses the 8049 original disjoint sign-change intervals
below 8192. For the first 111 intervals, use the strictly nested refined
intervals of width `2^-80`; for the remaining 7938, use the original width
`2^-24`. Strict signs on the original list were independently replayed in
the earlier native packet; the refined 222 endpoint signs were independently
replayed in the prefix packet. **Only those primitive sign facts are
imported.** The earlier packets also compute a complete count and infer
uniqueness, but neither assertion is used in (CF1)--(CF9).

`check_count_free_census.py` evaluates
`s(s-1)/2*pi^(-s/2)*Gamma(s/2)*zeta(s)` at `s=1/2+iz` through degree six
at 224 bits. It forms the logarithmic jet of `F/F(0)`, encloses every finite
inverse sixth power over its full selected-root interval, and recomputes
`T` directly. It uses no midpoint root, no assumed finite completeness, and
no call to `zeta_nzeros`. The seed, rational `pi` comparison, angular
constant, interval geometry, and exclusion guards are explicit strict tests.
The receipt hashes the displayed direct source list and native binaries;
it explicitly records the imported sign facts and the unused count claims.
The infinite product and positive theta identities remain mathematical
dependencies rather than finite-checker authenticated theorems.

The fixed guards are tested for `H=2048` and `H=2240`. No selected interval
meets either boundary. Their exact rational accepted receipts, rather than
rounded numerical estimates, determine the claims. Applying the already
proved finite-census column theorem then gives, for either accepted height,

\[
\begin{gathered}
 0\le r\le2H-3,\qquad\lambda>0,\qquad
 |T_0|<H-(r+2)/2,\qquad y\ge0,\\
 E_r=\Xi^{(r)}-i\lambda\Xi^{(r+1)},\qquad
 E_r(T_0-iy)\ne0,\quad E'_r(T_0-iy)\ne0,\quad
 \operatorname{Re}\frac{iE_r(T_0-iy)}{E'_r(T_0-iy)}>0.
\tag{CF10}
\end{gathered}
\]

For `H=2048` this covers `r=0,...,4093`; for `H=2240`, `r=0,...,4477`.
The height, derivative order and horizontal range remain finite. The
historical zero-count contract and published large zero verification are
absent from this proof's load-bearing hypotheses. The actual-source strip,
complete product, authenticated finite signs and directed native jet remain
explicit dependencies.

Reproduce the finite guard packet without overwriting its receipt:

```bash
source /workspace/.riemann-tools/activate.sh
python research/exploratory/2026-10-10-four-hour-wave/xi/outer-ray/check_count_free_census.py --output /tmp/count-free-census-replay.json
```

Optimized Python uses the same explicit acceptance branches and the same
native arithmetic backend; it is no independent arithmetic implementation.
