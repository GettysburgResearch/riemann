# The ratio-sixteen beta Gram form localizes to high primitive rays

Status: **exact primitive-ray disintegration, fixed-ray asymptotic, and
high-height RH localization theorem; no estimate for the residual
high-height sector and no proof of RH or GRH**

Bounded exact replay:
[`ffps_boundary_field_primitive_ray_localization.py`](ffps_boundary_field_primitive_ray_localization.py).
Canonical summary:
[`ffps_boundary_field_primitive_ray_localization.json`](ffps_boundary_field_primitive_ray_localization.json).

Frozen source: the corrected compact boundary-field near-correlation theorem
at `756660350`.  Its Markdown, producer, JSON, test, and imported beta
boundary theorem are pinned by the replay.

## 0. Outcome

Let

\[
 \beta=(\delta_1-\delta_{67})*\mu,
 \qquad
 (c_0,c_1,c_2)=(1,-2,1),
\tag{0.1}
\]

so that, away from `67`, a nonzero beta coefficient is squarefree, while

\[
 \beta(67^r d)=c_r\mu(d)
 \quad(0\le r\le2,\ 67\nmid d).
\tag{0.2}
\]

Write `R` for the compact autocorrelation in the frozen ratio-sixteen Gram
criterion.  For a reduced ordered ratio `a/b`, put

\[
 a=67^\alpha a_0,
 \qquad
 b=67^\gamma b_0,
 \qquad
 \min(\alpha,\gamma)=0.
\tag{0.3}
\]

An **admissible beta ray** has `alpha,gamma in {0,1,2}`, squarefree
`a_0,b_0`, and `gcd(67a_0,b_0)=gcd(a_0,67b_0)=1`.  Define

\[
 W_q(Y)=
 \sum_{\substack{d\le Y\\ d\text{ squarefree}\\(d,q)=1}}{1\over d},
 \qquad
 C(q)={1\over\zeta(2)}\prod_{p\mid q}\left(1+{1\over p}\right)^{-1}.
\tag{0.4}
\]

Then the complete contribution of that one ordered ray is exactly

\[
\boxed{
\begin{aligned}
 \mathcal Q_{a,b}(X)
 &:=\sum_{\substack{m,n\le X\\m/n=a/b}}
 {\beta(m)\beta(n)\over\sqrt{mn}}
 \mathcal R\!\left(\log{m\over n}\right)\\
 &= {\mathcal R(\log(a/b))\mu(a_0)\mu(b_0)
       \over 67^{(\alpha+\gamma)/2}\sqrt{a_0b_0}}
 \sum_{r=0}^{2-\max(\alpha,\gamma)}
 {c_{r+\alpha}c_{r+\gamma}\over67^r}
 W_{67a_0b_0}\!\left(
 {X\over67^r\max(a,b)}
 \right).
\end{aligned}}
\tag{0.5}
\]

Every nonzero pair occurs on exactly one such ray.  For each fixed ray,

\[
 \mathcal Q_{a,b}(X)=A_{a,b}\log X+O_{a,b,\mathcal R}(1),
\tag{0.6}
\]

with an explicit coefficient below.  Thus fixed rational slopes can carry
unavoidable logarithmic resonances, but every one is already subpower.

More strongly, let `Q_<=H(X)` be the off-diagonal Gram contribution from
pairs whose reduced ratio has height

\[
 h(m,n)=\max\left({m\over(m,n)},{n\over(m,n)}\right)\le H(X).
\tag{0.7}
\]

Uniformly for `1<=H<=X`,

\[
 \boxed{
 |\mathcal Q_{\le H}(X)|
 \le 16\|\mathcal R\|_\infty H(1+\log X).}
\tag{0.8}
\]

Consequently, for every prescribed `H(X)=X^{o(1)}` with `H(X)>=1`,

\[
\boxed{
 \mathrm{RH}
 \Longleftrightarrow
 |\mathcal Q_{>H(X)}(X)|=X^{o(1)}.}
\tag{0.9}
\]

On the residual support, compact ratio-sixteen geometry forces

\[
 \min\left({m\over(m,n)},{n\over(m,n)}\right)>{H(X)\over16},
 \qquad
 (m,n)<{X\over H(X)}.
\tag{0.10}
\]

Thus all fixed, polylogarithmic, or even
`exp(sqrt(log X))` primitive rays are unconditionally harmless.  The
RH-bearing cancellation is confined to balanced coprime numerator and
denominator cores of genuinely growing height.  This localizes the open
estimate; it does not prove it.

## 1. Exact source arithmetic and ray disintegration

The beta Dirichlet series has local factors

\[
 \sum_{k\ge0}\beta(p^k)z^k=
 \begin{cases}
 1-z,&p\ne67,\\
 (1-z)^2=1-2z+z^2,&p=67.
 \end{cases}
\tag{1.1}
\]

Hence `|beta(n)|<=2`, and a nonzero coefficient has exponent at most one
away from `67` and at most two at `67`.

Fix a reduced admissible ratio (0.3).  Every pair on this ray is uniquely

\[
 m=67^rda,
 \qquad
 n=67^rdb,
 \qquad
 0\le r\le2-\max(\alpha,\gamma),
\tag{1.2}
\]

where `d` is squarefree and coprime to `67a_0b_0`.  Conversely, every row in
(1.2) has nonzero beta coefficients.  The source product and normalization
are

\[
 {\beta(m)\beta(n)\over\sqrt{mn}}
 ={\mu(a_0)\mu(b_0)\over
   67^{(\alpha+\gamma)/2}\sqrt{a_0b_0}}
 {c_{r+\alpha}c_{r+\gamma}\over67^r d}.
\tag{1.3}
\]

The prefix conditions are equivalent to

\[
 d\le {X\over67^r\max(a,b)},
\tag{1.4}
\]

while the Gram kernel is constant on the ray.  Summing (1.3) proves (0.5).
No absolute value, collapsed `67` label, or asymptotic argument enters this
identity.

## 2. Every fixed ray is an explicit logarithmic resonance

For fixed squarefree `q`, elementary squarefree harmonic summation gives

\[
 W_q(Y)=C(q)\log Y+O_q(1).
\tag{2.1}
\]

For example, insert
`mu^2(d)=sum_(k^2|d) mu(k)` and use the ordinary harmonic estimate in the
remaining variable; the omitted primes give exactly the finite Euler factor
in (0.4).

Combining (0.5) and (2.1) gives (0.6), with

\[
\boxed{
 A_{a,b}=
 {\mathcal R(\log(a/b))\mu(a_0)\mu(b_0)C(67a_0b_0)
  \over67^{(\alpha+\gamma)/2}\sqrt{a_0b_0}}
 S_{\alpha,\gamma},}
\tag{2.2}
\]

where

\[
 S_{\alpha,\gamma}
 =\sum_{r=0}^{2-\max(\alpha,\gamma)}
 {c_{r+\alpha}c_{r+\gamma}\over67^r}.
\tag{2.3}
\]

The exceptional local cases are

\[
\begin{array}{c|c}
 (\alpha,\gamma)&S_{\alpha,\gamma}\\ \hline
 (0,0)&1+4/67+1/67^2,\\
 (1,0),(0,1)&-2-2/67,\\
 (2,0),(0,2)&1.
\end{array}
\tag{2.4}
\]

None vanishes.  Thus a fixed admissible ray has a nonzero logarithmic main
term whenever `R(log(a/b))` is nonzero.  In particular, removing only the
literal diagonal does not remove all deterministic logarithmic pieces.
This is harmless for a subpower criterion, but it is load-bearing for any
attempt to claim that the residual is purely fluctuating.

As a concrete source resonance, the reduced ray `2/1` contains the pairs
`(2d,d)` with `d` odd.  Since `beta(2d)=-beta(d)`, its two orientations
contribute exactly

\[
 -\sqrt2\,\mathcal R(\log2)
 \sum_{\substack{d\le X/2\\d\text{ odd}}}{\beta(d)^2\over d}.
\tag{2.5}
\]

This is logarithmic, not a new RH obstruction.

## 3. Uniform low-height control

For any reduced `a/b`, write `m=ga,n=gb`.  Without using cancellation,

\[
 \left|{\beta(ga)\beta(gb)\over g\sqrt{ab}}
 \mathcal R(\log(a/b))\right|
 \le {4\|\mathcal R\|_\infty\over g\sqrt{ab}}.
\tag{3.1}
\]

The prefix restricts `g<=X/max(a,b)`, so the radial harmonic sum is at most
`1+log X`.  Finally,

\[
 \sum_{a,b\le H}{1\over\sqrt{ab}}
 =\left(\sum_{a\le H}a^{-1/2}\right)^2
 \le4H.
\tag{3.2}
\]

Dropping coprimality, source support, the off-diagonal restriction, and the
ratio band can only enlarge this absolute majorant.  Equations (3.1)--(3.2)
prove (0.8).

If `H(X)=X^{o(1)}`, then the right side of (0.8) is `X^{o(1)}`.  The frozen
near-correlation theorem gives

\[
 \mathrm{RH}\Longleftrightarrow|\mathcal O(X)|=X^{o(1)},
\tag{3.3}
\]

where `O` is the whole signed off-diagonal form.  Since
`O=Q_<=H+Q_>H`, adding or subtracting (0.8) proves (0.9), with both
directions and with the displayed quantifier on `H`.

On `Q_>H`, put `h=max(a,b)>H`.  Ratio-sixteen support gives
`min(a,b)>=h/16>H/16`, and `m=ga,n=gb<=X` gives `g<=X/h<X/H`.
This proves (0.10).

## 4. Radial/projector Euler factors

There is an exact Euler-factor interpretation, but it must be kept to its
domain of absolute convergence.  For `s=sigma+it` with `sigma>1`,

\[
 B(s)=\sum_{n\ge1}{\beta(n)\over n^s}
 ={1-67^{-s}\over\zeta(s)}.
\tag{4.1}
\]

At an ordinary prime, put `x=p^-s` and `y=p^-bar(s)`.  The two-copy local
factor splits as

\[
 (1-x)(1-y)
 =(1+xy)\left(1-{x+y\over1+xy}\right).
\tag{4.2}
\]

The first factor records equal prime incidence in the common radial
variable; the second records primitive one-sided incidence.  At `67`, the
corresponding split is

\[
 (1-x)^2(1-y)^2
 =(1+4xy+x^2y^2)
 { (1-x)^2(1-y)^2\over1+4xy+x^2y^2}.
\tag{4.3}
\]

Therefore

\[
 |B(s)|^2=\mathcal C_{\rm rad}(\sigma)
          \mathcal P_{\rm prim}(s),
\tag{4.4}
\]

where both Euler products converge absolutely for `sigma>1`, and

\[
\boxed{
 \mathcal C_{\rm rad}(\sigma)
 ={\zeta(2\sigma)\over\zeta(4\sigma)}
 {1+4q+q^2\over1+q},
 \qquad q=67^{-2\sigma}.}
\tag{4.5}
\]

At `sigma=1/2+epsilon`, the meromorphic expression on the right has radial
growth

\[
 \mathcal C_{\rm rad}(1/2+\varepsilon)
 \sim {1\over2\varepsilon}
 {2379\over2278\zeta(2)}.
\tag{4.6}
\]

This is the same common-factor logarithm seen in (2.1) and the frozen
diagonal calculation.  Equations (4.2)--(4.6) do **not** assert convergence
of the separated primitive Euler product at `sigma=1/2`.  Finite-prime local
factorizations remain exact there, but controlling their limit is precisely
part of the missing high-height arithmetic.

## 5. Proof and scope ledger

| statement | grade |
|---|---|
| exact beta ray disintegration (0.5) | **PROVED EXACT** |
| fixed-ray asymptotic and all `67` radial cases | **PROVED EXACT / STANDARD HARMONIC SUMMATION** |
| uniform low-height bound (0.8) | **PROVED UNCONDITIONALLY** |
| high-height RH equivalence (0.9) | **PROVED EXACT FROM THE FROZEN CRITERION** |
| residual balanced-core geometry (0.10) | **PROVED EXACT** |
| radial/projector factors for `Re(s)>1` | **PROVED EXACT** |
| critical-line convergence of the separated factors | **NOT CLAIMED** |
| subpower estimate for the residual high-height sector | **OPEN; EQUIVALENT TO RH** |
| RH or GRH | **NOT PROVED** |

The theorem says where the RH-strength aggregate begins.  It does not turn
an individual logarithmic resonance into evidence for or against RH, and it
does not license termwise cancellation of an infinite ray expansion.

## 6. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_boundary_field_primitive_ray_localization.py --check
python -B -O research/l-families/atlas/function_field/ffps_boundary_field_primitive_ray_localization.py --check
python -B -m unittest tests.test_ffps_boundary_field_primitive_ray_localization
python -B -O -m unittest tests.test_ffps_boundary_field_primitive_ray_localization
```

The replay pins every imported source blob; checks the beta local factors;
verifies the exact ray formula against direct source pairs including all
five exceptional `67` directions; checks the exceptional radial sums and
Euler-factor algebra; and enforces the scope/resource guards.  It enumerates
no zeta zero, finite field, curve, conductor family, or `L`-function.
