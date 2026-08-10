# Tensor phase current collapse and the four-adic Hilbert bound

Status: **PROPOSED COMPLETE EXACT ARITHMETIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Scope: finite main-pole-killing tensor phase bank, its source reserve, channel DFT, and coefficient/mean-square bounds; no complete Weil floor and no RH claim  
Depends on: PR #325 `L-32415`; ordinary Selberg–Kummer reserve; finite Fourier orthogonality; Montgomery–Vaughan's Dirichlet-polynomial mean-value theorem

## 1. Finite main-pole source and tensor phase bank

Put

\[
a(s)=4^{1-s},\qquad L=\log4,
\]

and retain the finite Q4 main-pole source

\[
B_\sharp(s)={1-a(s)\over\zeta(s)},
\qquad
b_\sharp=(\varepsilon-4\delta_4)*\mu.
\tag{TP.1}
\]

PR #325 proves that this system has positive inverse and generalized-prime coefficients, retains every nontrivial zeta-zero pole, and has a strict quarter-balanced Selberg–Kummer reserve

\[
\mathcal R_\sharp=P_\sharp^2-S_\sharp>0.
\]

For integers `k>=1`, `M>=2`, and

\[
\boldsymbol\omega=(\omega_1,\ldots,\omega_k)\in\Omega_M^k,
\]

define

\[
F_{\boldsymbol\omega}(s)
=\prod_{\ell=1}^k(1-\omega_\ell a(s)),
\qquad
B_{\boldsymbol\omega}=F_{\boldsymbol\omega}B_\sharp.
\tag{TP.2}
\]

Every channel remains main-pole killing because the common factor `B_sharp` vanishes at `s=1`. On the critical line `|a|=2`, and independent phase averaging gives

\[
{1\over M^k}\sum_{\boldsymbol\omega}
|F_{\boldsymbol\omega}(1/2+it)|^2=5^k.
\tag{TP.3}
\]

## 2. Complete phase-separated source reserve

Let

\[
\Lambda_{\boldsymbol\omega}
=-A_{\boldsymbol\omega}'/A_{\boldsymbol\omega},
\qquad A_{\boldsymbol\omega}=B_{\boldsymbol\omega}^{-1}.
\]

Logarithmic differentiation gives

\[
\Lambda_{\boldsymbol\omega}
=\Lambda_\sharp
+L\sum_{\ell=1}^k\sum_{r\ge1}
\omega_\ell^r4^r\delta_{4^r}.
\tag{TP.4}
\]

Fix a carry endpoint `n`, put `R=floor(log_4 n)`, and assume

\[
M>2R.
\tag{TP.5}
\]

For a carry row `e=(n,j)`, set

\[
d_r(e)=L4^r\chi_{n,4^r}(j).
\]

Then independent Fourier orthogonality gives

\[
{1\over M^k}\sum_{\boldsymbol\omega}
|P_{\boldsymbol\omega}(e)|^2
=P_\sharp(e)^2+k\sum_{r=1}^{R}d_r(e)^2.
\tag{TP.6}
\]

If

\[
C_{\boldsymbol\omega}
=\Lambda_{\boldsymbol\omega}\log
 +\Lambda_{\boldsymbol\omega}*\Lambda_{\boldsymbol\omega},
\]

then every term containing a phase-dependent local factor has nonzero phase in at least one independent coordinate. The condition `M>2R` also prevents a same-coordinate local/local phase from returning to zero. Hence, through the complete endpoint,

\[
{1\over M^k}\sum_{\boldsymbol\omega}C_{\boldsymbol\omega}=C_\sharp.
\tag{TP.7}
\]

Therefore the averaged row reserve is exactly

\[
\boxed{
\mathcal R_{k,M}(e)
=\mathcal R_\sharp(e)+k\sum_{r=1}^{R}d_r(e)^2\ge0.
}
\tag{TP.8}
\]

Independent phase depth adds only positive local storage and creates no mixed Selberg debt.

## 3. Exact tensor DFT of sources and currents

For a subset `S` of `{1,...,k}`, put `r=|S|` and let `chi_S` be the corresponding product character on `Omega_M^k`. With the normalized tensor DFT,

\[
\widehat B_S
={1\over M^k}\sum_{\boldsymbol\omega}
\overline{\chi_S(\boldsymbol\omega)}B_{\boldsymbol\omega},
\]

one has exactly

\[
\widehat B_S=(-a)^rB_\sharp.
\tag{TP.9}
\]

Put

\[
q_\sharp=B_\sharp',
\qquad q_{\boldsymbol\omega}=B_{\boldsymbol\omega}'.
\]

Since `a'=-La`, differentiation gives

\[
\widehat q_S=(-a)^r(q_\sharp-rLB_\sharp).
\tag{TP.10}
\]

All DFT modes outside `{0,1}^k` vanish. Channel Parseval and `|a|^2=4` yield

\[
{1\over M^k5^k}\sum_{\boldsymbol\omega}|q_{\boldsymbol\omega}|^2
=\sum_{r=0}^k\binom kr{4^r\over5^k}
|q_\sharp-rLB_\sharp|^2.
\tag{TP.11}
\]

The weights are the law of `J ~ Binomial(k,4/5)`, so the complete bank collapses to

\[
\boxed{
{1\over M^k5^k}\sum_{\boldsymbol\omega}|q_{\boldsymbol\omega}|^2
=\left|q_\sharp-{4k\over5}LB_\sharp\right|^2
+{4k\over25}L^2|B_\sharp|^2.
}
\tag{TP.12}
\]

After atomized physical localization,

\[
\zeta B_\sharp N_\theta=(1-a)N_\theta
\]

is deterministic. Thus the tensor bank carries one genuine pole current, one deterministic linear gauge, and one deterministic variance term. Its causal current cost is quadratic, not exponential, in `k`.

## 4. Uniform coherent channel norm

Equip channel vectors with

\[
\|x\|_{\rm ch}^2={1\over M^k}
\sum_{\boldsymbol\omega}|x_{\boldsymbol\omega}|^2.
\]

For `||x||_ch=1`, synthesize

\[
H_x(a)
={1\over M^k5^{k/2}}
\sum_{\boldsymbol\omega}
\overline{x_{\boldsymbol\omega}}F_{\boldsymbol\omega}(a)
=\sum_{r=0}^kh_ra^r.
\tag{TP.13}
\]

Let `xhat_S` be the unitary tensor DFT of `x`. Then

\[
h_r={(-1)^r\over5^{k/2}}
\sum_{|S|=r}\widehat x_S.
\]

Cauchy–Schwarz and DFT Parseval give

\[
\boxed{
\|H_x\|_{\rm crit}^2
:=\sum_{r=0}^k4^r|h_r|^2\le1.
}
\tag{TP.14}
\]

This is uniform in channel count and tensor depth.

## 5. Two-layer four-adic support

The common source coefficient satisfies

\[
b_\sharp(n)=\mu(n)-4\mathbf1_{4\mid n}\mu(n/4).
\]

Its support obeys

\[
\boxed{
b_\sharp(n)\ne0\Longrightarrow v_4(n)\in\{0,1\}.}
\tag{TP.15}
\]

A squarefree integer has `v_4=0`; the second tap produces exactly `v_4=1`; every deeper layer contains a square factor and vanishes under `mu`.

Therefore the coefficients of `a^rB_sharp` lie only on the two layers

\[
v_4(n)\in\{r,r+1\}.
\tag{TP.16}
\]

At every integer, a sum `sum_r h_r a^r B_sharp` has at most two nonzero mode contributions. For

\[
\|d\|_{1/2,X}^2=\sum_{n\le X}{|d(n)|^2\over n},
\]

this bandedness and `|b_sharp(n)|<=4` give

\[
\boxed{
\|H(a)B_\sharp\|_{1/2,X}^2
\le32(1+\log X)\|H\|_{\rm crit}^2.
}
\tag{TP.17}
\]

Differentiating the Dirichlet series gives, for every integer `d>=0`,

\[
\boxed{
\|(H(a)B_\sharp)^{(d)}\|_{1/2,X}^2
\le32(1+\log X)(\log X)^{2d}
\|H\|_{\rm crit}^2.
}
\tag{TP.18}
\]

Indeed the coefficient from mode `r` and base integer `m` is a multiple of

\[
4^rh_rb_\sharp(m)\log^d(4^rm),
\]

and `4^rm<=X` bounds the logarithm by `log X`.

Combining (TP.14) and (TP.18), every coherent unit channel direction has source, current, and second-current coefficient norms bounded by fixed powers of `log X`, independently of `k`.

## 6. Montgomery–Vaughan mean-square corollary

Let `c_x^(d)(n)` be the coefficients of the `d`th derivative in (TP.18), truncated at `X`, and put

\[
D_{x,X}^{(d)}(t)
=\sum_{n\le X}{c_x^{(d)}(n)\over\sqrt n}n^{-it}.
\]

The classical Montgomery–Vaughan mean-value theorem gives

\[
\int_{-T}^{T}|D_{x,X}^{(d)}(t)|^2dt
\ll(T+X)\sum_{n\le X}{|c_x^{(d)}(n)|^2\over n}.
\]

Hence, uniformly over tensor depth, channel count, and coherent unit channel direction,

\[
\boxed{
{1\over T}\int_{-T}^{T}|D_{x,X}^{(d)}(t)|^2dt
\ll(1+X/T)(1+\log X)^{2d+1}.
}
\tag{TP.19}
\]

In the natural regime `T>=X`, the bare source, current, and second current have normalized mean square `O(log X)`, `O(log^3 X)`, and `O(log^5 X)`, respectively.

## 7. Exact remaining boundary

This theorem closes:

```text
independent phase source reserve             exact and positive;
tensor channel proliferation                 subset-DFT collapse;
causal current bank                          exact binomial law;
arbitrary coherent channel synthesis         critical norm <=1;
source/current coefficient Gram              two-layer banded;
Dirichlet mean-square cost                    polylogarithmic, uniform in k.
```

It does **not** prove the corrected Weil-kernel floor. The complete Gabor/Weil compression contains an archimedean term and a prime-shift Toeplitz operator whose worst coherent direction is not controlled merely by vertical mean square. Equivalently, the reflected left-half-plane boundary state is not the causal current Gram in (TP.12).

The remaining theorem is:

> Convert the coherent coefficient estimate (TP.19), together with the positive tensor reserve (TP.8), into a lower bound for the complete source-convolved reflected block on the Xi-cardinal or Gaussian terminal direction.

Any proof must retain the exact reflected subtraction. Replacing the complete block by its causal current Gram or by a Frobenius average is an automatic rejection.

## Exact status

```text
tensor critical frame                         PROPOSED COMPLETE EXACT
tensor phase-separated reserve                 PROPOSED COMPLETE EXACT
tensor DFT current collapse                    PROPOSED COMPLETE EXACT
binomial current/gauge law                     PROPOSED COMPLETE EXACT
coherent critical polynomial norm              PROPOSED COMPLETE EXACT
two-layer four-adic coefficient bandedness      PROPOSED COMPLETE EXACT
uniform coefficient and MV mean-square bounds   PROPOSED COMPLETE
complete corrected-kernel arithmetic floor      OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVED
```
