# Xi carrier scale: an exact mismatch window and localization firewall

Status: **exact Fourier-density and Hardy-kernel theorems; Xi narrowing is
conditional on the explicit concentration bound in `L-106502`**.

Scope: fixed positive source frequency, odd derivative order, positive even
Schwartz Fourier sources; no source-Pick congruence or zero-count estimate.
This is an earlier-work scout independent of the #763 finite-place programme.
It makes no novelty, ninety-percent, density-one, or RH claim.

Exact sources: PR #731 head `6d440eb6c82d989c046e87e13f9bdabf087f920f`,
scientific head `81d52e569cc8bb566e54043fd692fd6157406aab`. Six literal source
files are authenticated in `xi_near_adapted_scale_firewall.sources.json`.
The independent-constant-review boundary of `L-106502` is retained, not closed.

What was run: bounded exact binomial, Gaussian-moment, rational phase-window,
and rational Hardy-band controls. No Xi zeros, numerical Fourier transforms,
or special-function evaluations were computed.

Smallest remaining gap: an estimate in the **actual outer-normalized
source-Pick metric**, either exploiting signed off-band compensation or
proving an appropriate collective localization theorem. The scalar results
below do not supply that estimate.

## 1. Literal source and dimensionless variables

Retain `L-106710` with `K>=1` odd, `xi>0`, and a nonnegative even Schwartz
kernel `Phi`. Assume `L_K(xi)>0`. Write `s=xi/2`, `d=v-u`, `x=d/xi`, and

\[
 P_K(y)=\sum_{j=0}^{(K-1)/2}{K\choose2j}y^j,
 \qquad Q_K(y)=\sum_{j=0}^{(K-1)/2}{K\choose2j+1}y^j,
 \qquad R_K(x)=P_K(x^2)/Q_K(x^2).
\]

The conditional probability `mu=mu_(K,xi)` has density proportional to
`d(v^K-u^K)Phi(u)Phi(v)`. Put

\[
 m_2=\int d^2\,d\mu>0,\qquad
 p=\frac{a_{K,2/\xi}(\xi)}{(2/\xi)L_K(\xi)},\qquad
 g=\frac{\xi}{2}\frac{a_{K,0}(\xi)}{L_K(\xi)}.
\tag{1.1}
\]

Here `p` is an adapted **Fourier-density ratio**, not a physical endpoint
phase or a Pick eigenvalue. For any constant `lambda>0` define

\[
 \eta=\lambda\xi/2,\qquad
 \rho(\eta)=\frac{a_{K,\lambda}(\xi)}{\lambda L_K(\xi)}.
\]

The half-convolution and change-of-variable factors cancel in these ratios.
The variable-scale expression at `eta=1` remains a Fourier construction;
it is not substituted into the physical companion quotient.

## 2. Exact gain and sharp scale-window algebra

**Theorem XS-1.** Under these hypotheses,

\[
 \frac1K\le R_K(x)\le K,\qquad
 \frac1{2K}\le p\le\frac K2,\qquad
 g\ge\frac{\xi^2}{2K m_2},
\tag{2.1}
\]

and the entire scale dependence is exactly

\[
 \boxed{\rho(\eta)=\frac g\eta+(p-g)\eta.}
\tag{2.2}
\]

Proof. The coefficients of `K P_K-Q_K` and `K Q_K-P_K` are nonnegative:

\[
 K{K\choose2j}-{K\choose2j+1}
 ={2j(K+1)\over2j+1}{K\choose2j}\ge0,
\]

\[
 K{K\choose2j+1}-{K\choose2j}
 ={(K+1)(K-1-2j)\over2j+1}{K\choose2j}\ge0.
\]

Since `Q_K(x^2)>0`, this proves the bounds on `R_K`. Directly dividing the
source integrands gives

\[
 p=\frac12\int R_K(d/\xi)\,d\mu,
 \qquad g=\frac{\xi^2}{2}\int\frac{R_K(d/\xi)}{d^2}\,d\mu.
\tag{2.3}
\]

The apparent inverse moment is finite because it is exactly a constant
multiple of `a_(K,0)/L_K`; `mu` gives `d=0` zero mass. Cauchy--Schwarz gives
`(int d^2 dmu)(int d^(-2) dmu)>=1`, proving the lower bound on `g`.
Finally insert the literal mismatch identity
`a_lambda=(1-eta^2)a_0+lambda^2 b_K` from `L-106710`. QED.

**Theorem XS-2 (exact phase diagram).** If `g>p`, let `b=g-p>0`. Then
`rho(eta)=g/eta-b eta` is strictly decreasing on `eta>0`, vanishes at
`eta_c=sqrt(g/b)>1`, and changes from positive to negative there. For any
`M>=0`, the condition `abs(rho(eta))<=M` holds on exactly the interval

\[
 \eta_-={\sqrt{M^2+4bg}-M\over2b},\qquad
 \eta_+={\sqrt{M^2+4bg}+M\over2b}.
\]

In particular,

\[
 \boxed{\eta_+-\eta_-={M\over g-p}.}
\tag{2.4}
\]

If instead `g<=p`, the ratio is positive at every scale; the sign-transition
conclusion must not be used. These statements follow directly from (2.2).

The exact difference formula, valid whenever `g>p`, is

\[
 |\rho(\eta)-p|
 =|\eta-1|\left[g(1+1/\eta)-p\right].
\tag{2.5}
\]

Consequently `abs(rho)<=M` implies

\[
 |\eta-1|\le {M+p\over g-p}.
\tag{2.6}
\]

When `xi^2>K^2 m_2`, (2.1) supplies the explicit variance-controlled bounds

\[
 \eta_+-\eta_-\le {2KM m_2\over\xi^2-K^2m_2},
 \qquad
 |\eta-1|\le {K(2M+K)m_2\over\xi^2-K^2m_2}.
\tag{2.7}
\]

These are bounds on a **pointwise density ratio**. `M` is not a global
free-energy budget, and no comparison to the ninety-percent allowance is made.

## 3. Uniform control exists at only one source-independent scale

**Theorem XS-3.** For fixed odd `K` and fixed `xi>0`, `lambda=2/xi` is the
unique positive scale at which `abs(a_(K,lambda)/(lambda L_K))` is bounded
uniformly over positive even Schwartz sources with `L_K(xi)>0`.

The adapted bound is (2.1). For the converse, set `s=xi/2`, choose `nu>0`,
and define the source upstream by

\[
 \Phi_\nu(u)=\exp[-u^2/(4s^2\nu)].
\]

Conditioning its **unweighted** product on `u+v=xi` makes `x=d/xi` a centered
Gaussian of variance `nu`; the current measure `mu` still has its additional
`x^2 Q_K(x^2)` weight. Denote Gaussian expectation by `E_nu`. Polynomial
Gaussian moments, obtained by integration by parts, give

\[
 g_\nu={E_\nu P_K(x^2)\over2E_\nu[x^2Q_K(x^2)]},
 \qquad
 p_\nu={E_\nu[x^2P_K(x^2)]\over2E_\nu[x^2Q_K(x^2)]}.
\]

Since `E x^(2j)=(2j-1)!! nu^j`,

\[
 g_\nu={1\over2K\nu}+O(1),\qquad
 p_\nu={1\over2K}+O(\nu).
\]

For fixed `eta!=1`, therefore,

\[
 \nu\rho_\nu(\eta)\longrightarrow {1-\eta^2\over2K\eta}\ne0.
\tag{3.1}
\]

More sharply, if `eta_nu=1+c nu+o(nu)` for any fixed real `c`,

\[
 \boxed{\rho_\nu(\eta_\nu)\longrightarrow {1-2c\over2K}.}
\tag{3.2}
\]

Thus even a vanishing relative scale error can change the limiting adapted
ratio, make it zero, or reverse its sign. For `K=5` this limit is
`1/10-c/5`. This counterfamily varies the Schwartz source at one fixed
frequency; it is **not** a counterexample about the actual Xi kernel.

For checking constants, the fifth-order Gaussian formulas are exactly

\[
 g_\nu={1+10\nu+15\nu^2\over10\nu+60\nu^2+30\nu^3},\qquad
 p_\nu={1+30\nu+75\nu^2\over10+60\nu+30\nu^2}.
\]

## 4. Conditional Xi consequence: an exponentially narrow pointwise window

Assume only the `q=1` concentration assertion of `L-106502`, uniformly for
large `xi`:

\[
 m_2(\xi)\le C_K e^{-\xi}.
\tag{4.1}
\]

For fixed `K,M`, (2.7) then implies

\[
 |\rho(\eta)|\le M
 \quad\Longrightarrow\quad
 |\eta-1|=O_{K,M,C_K}(e^{-\xi}/\xi^2).
\tag{4.2}
\]

The exact accepted-scale interval has at most that order of width. Its true
width may be smaller: positive-moment concentration alone gives a lower
bound on `g`, not an upper inverse-moment bound.

More generally, along `xi -> infinity` and `eta -> 1`, (2.5) proves
`rho(eta)-p -> 0` **if and only if** `(eta-1)g -> 0`. Hence preserving the
conditional fifth ratio `1/10` requires that mismatch condition; the weaker
statement `eta -> 1` does not suffice.

For one physical constant `lambda`, put `Xi_c=2/lambda`. On the candidate
high-frequency band `[Xi_c/2,2 Xi_c]`, with `Xi_c -> infinity`, every frequency
satisfying the pointwise bound must lie within

\[
 |\xi-\Xi_c|=O(e^{-\Xi_c}/\Xi_c).
\tag{4.3}
\]

Indeed (4.2) first makes `abs(xi-Xi_c)=o(1)` uniformly on this band; replacing
`xi` by `Xi_c` in its exponential and polynomial scales then gives (4.3).
This is a necessary localization condition for **this pointwise strategy**,
not a necessary condition for every possible proof of `XICARRIERPICK106710`.

## 5. A raw Hardy node is not concentrated in that carrier band

**Theorem XS-4.** For the normalized simple-node Fourier vector used in
`L-106502`,

\[
 e_{a,y}(\xi)=\sqrt{2y}\,e^{-(y+ia)\xi},\quad \xi>0,\ y>0,
\]

and `0<A<B<infinity`,

\[
 \int_A^B|e_{a,y}(\xi)|^2d\xi=e^{-2yA}-e^{-2yB}
 \le {B-A\over eA}.
\tag{5.1}
\]

Proof. Pointwise in `xi>=A`, maximize `2y e^(-2yA)` over `y>0`; its maximum
is `1/(eA)`. Integration gives (5.1). In fact the sharp maximum mass is
`(1-A/B)(A/B)^(A/(B-A))`, by differentiating the exact difference. QED.

For a relative carrier band `Xi_c[1-epsilon,1+epsilon]`, `0<epsilon<1`, the
mass is at most `2 epsilon/[e(1-epsilon)]`, uniformly in pole location and
height. In a band of the size (4.3) it is `O(e^(-Xi_c)/Xi_c^2)`, not close to
one. Shallow Hardy kernels reach high frequencies, but are not narrowly
localized at a chosen carrier frequency.

This does not control a source-weighted or outer-normalized vector, a
nonorthogonal combination, or a confluent jet. It neither bounds the Pick
determinant nor rules out collective/signed compensation outside the band.

## 6. Exact bridge boundary and useful next target

`L-106620` controls the physical coefficient `1-lambda_j theta'(t)` on real
mesoscopic windows. That is not the spectral variable `1-lambda_j xi/2`.
The present result does not refute its logarithmic carrier-matching theorem.

The literal `T-106670` matrix is
`G_j-tau V_j^* G_j V_j`, with actual outer-normalized source values in `V_j`
and the denominator-kernel metric `G_j`. Dividing Fourier densities is not
division by the common physical outer factor and is not a congruence of this
matrix. Endpoints, confluent nodes, and the forced index from `R-106710`
remain untouched. No topological identity is being repackaged as progress.

The next proof-sized target is an **outer-retaining off-band comparison**:
express the constant/adapted mismatch as a bilinear form on the actual
denominator kernel/jet vectors and prove a signed bound after the exact
common outer normalization. Any proposed localization-based version must
first explain how its actual transformed vectors escape (5.1); raw
single-node localization cannot do so. This is an open target, not an
assumed transport theorem or a new name for a proved estimate.

The gain/phase theorem is elementary and source-uniform; the only Xi-specific
corollary is conditional on (4.1). It does not establish
`XICARRIERPICK106710`, a free-energy budget, ninety percent, density one, or RH.

## 7. Bounded replay

The producer independently checks both coefficient inequalities for odd
`K<=15`, exact Gaussian moments and phase samples, rational scale-window
identities and variance bounds, and conservative rational versions of the
Hardy-band upper bound. The general theorems are proved above, not inferred
from the corpus. Input bit sizes and polynomial orders are explicitly capped.

The six frozen source files are read from Git and checked by blob ID and
LF-normalized SHA-256. Current note, producer, tests, and manifest are
similarly bound to the fixture; typed canonical comparison rejects altered
data. Original source replays are not imported as proof-producing checkers.
All result-bearing checks survive optimized Python.

```text
python -B research/exploratory/xi_near_adapted_scale_firewall.py --check
python -B -O research/exploratory/xi_near_adapted_scale_firewall.py --check
python -B -m unittest discover -s tests -p test_xi_near_adapted_scale_firewall.py
python -B -O -m unittest discover -s tests -p test_xi_near_adapted_scale_firewall.py
```
