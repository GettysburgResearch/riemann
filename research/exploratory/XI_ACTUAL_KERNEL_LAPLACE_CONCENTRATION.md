# Actual Xi-kernel concentration and the sharp carrier boundary layer

Status: NEW ANALYTIC PROOF; EXACT-SHA INDEPENDENT REVIEW REQUESTED.

Scope: the literal real Xi Fourier source, each fixed positive odd order, and
source frequency tending to positive infinity. No physical-window transfer.

Exact sources: six Git-locked inputs in the companion source manifest; classical
theta inversion and Mellin normalization are identified below.

What was actually run: the companion checker authenticates the frozen sources
and bounded exact rational algebra. It does not certify the analytic proof.

Smallest remaining program gap: transfer to the literal outer-normalized,
nonlocal source-Pick metric remains open. RH remains unsolved.

This is a new, explicit reproof of the real concentration assertion
`L-106502.4`, with leading constants. It does not import the complex-ray
theorem proposed in `L-105413`, and does not rewrite any historical claim.
It removes the concentration dependency of the scout at
`939a24962a4c6a449c0b56e3b20f78b936f35f6c`, subject to review of this new proof.

## 1. Literal normalization: an old factor of two

Use the standard completed function and full-line Fourier convention

\[
 \xi_{\rm R}(z)=\tfrac12z(z-1)\pi^{-z/2}\Gamma(z/2)\zeta(z),\qquad
 \Xi(t)=\xi_{\rm R}(\tfrac12+it),\qquad
 \Xi(t)=\int_{\mathbb R}\Phi_\Xi(u)e^{itu}\,du.
\tag{XL1}
\]

The inverse Fourier transform is `(2 pi)^(-1) integral f(t) exp(-it u) dt`,
as in the pinned `L-106401`. The standard normalization is
[DLMF 25.4.4](https://dlmf.nist.gov/25.4.E4).

The literal expression called `Phi` in the pinned historical `L-105413` is

\[
 \phi_0(u)=\sum_{n\ge1}
 (2\pi^2n^4e^{9u/2}-3\pi n^2e^{5u/2})e^{-\pi n^2e^{2u}}.
\tag{XL2}
\]

With (XL1), the actual kernel is **`Phi_Xi = 2 phi_0`**, not `phi_0`.
Here is a direct check, rather than an appeal to a convention from memory.
Put

\[
 \psi(x)=\sum_{n\ge1}e^{-\pi n^2x},\quad
 \theta(x)=1+2\psi(x),\quad f(u)=e^{u/2}\psi(e^{2u}),\quad D=d/du.
\]

Termwise differentiation on compact real intervals gives

\[
 \phi_0=\tfrac12(D^2-\tfrac14)f.
\tag{XL3}
\]

Theta inversion is `theta(x)=x^(-1/2) theta(1/x)`; it is the specialization
of [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32) to the positive imaginary
lattice parameter. Thus `G(u)=e^(u/2) theta(e^(2u))` is even and
`phi_0=(D^2-1/4)G/4` is even. Every term of (XL2) is positive for `u>=0`;
evenness proves positivity everywhere. The bounds in Section 3 also prove
superexponential real decay at both ends.

For `Re z>1`, direct integration of the positive theta series (or absolute
convergence for complex `z`) gives

\[
 \int_{\mathbb R}f(u)e^{(z-1/2)u}\,du
 =\tfrac12\pi^{-z/2}\Gamma(z/2)\zeta(z).
\]

This is equivalently [DLMF 20.10.2](https://dlmf.nist.gov/20.10.E2) after
changing variable. Integration by parts in (XL3), twice, yields

\[
 \int_{\mathbb R}\phi_0(u)e^{(z-1/2)u}\,du
 =\tfrac14 z(z-1)\pi^{-z/2}\Gamma(z/2)\zeta(z)
 =\tfrac12\xi_{\rm R}(z).
\tag{XL4}
\]

There are no discarded boundary terms: at negative infinity theta inversion
gives `f(u)=(e^(-u/2)-e^(u/2))/2` plus a superexponentially small term, with
the same property after finitely many derivatives; multiplication by
`exp((z-1/2)u)` makes all boundary terms vanish for `Re z>1`. At positive
infinity the theta series and its derivatives decay superexponentially.
The left side of (XL4) is entire in `z` by the even real-tail bounds below;
analytic continuation proves (XL4) everywhere, in particular (XL1).

This scalar correction matters for absolute Fourier densities: passing from
`phi_0` to `Phi_Xi` multiplies every quadratic density below by four.
It does **not** change the probability measure, moments, `g`, `p`, `rho`,
or the current ratio. No frequency rescaling is involved. We use
`Phi=Phi_Xi` henceforth; all normalized conclusions also hold for `phi_0`.

## 2. Exact source objects and theorem

Fix a positive odd integer `K`; it does not grow with frequency. For `xi>0`
write

\[
 E=e^\xi,\quad u=(\xi-d)/2,\quad v=(\xi+d)/2,\quad
 H_\xi(d)=\Phi(u)\Phi(v),\quad
 W_{K,\xi}(d)=d(v^K-u^K).
\]

The binomial expansion gives the exact positive polynomial

\[
 W_{K,\xi}(d)=2^{1-K}\sum_{j=0}^{(K-1)/2}
  {K\choose2j+1}\xi^{K-2j-1}d^{2j+2}.
\tag{XL5}
\]

Define `Z=integral W H dd`, `d mu = W H dd/Z` and

\[
 P_K(y)=\sum_j{K\choose2j}y^j,\qquad
 Q_K(y)=\sum_j{K\choose2j+1}y^j,\qquad
 R_K(x)=P_K(x^2)/Q_K(x^2).
\]

The factors `du=|dd|/2` and the half-convolution in the pinned sources give

\[
 \begin{split}
 L_K(\xi)&=Z/4
 =2^{-K-1}\xi^{K-1}\int d^2Q_K(d^2/\xi^2)H_\xi(d)\,dd,\\
 a_{K,0}(\xi)&=2^{-K-1}\xi^K
                  \int P_K(d^2/\xi^2)H_\xi(d)\,dd,\\
 g_K(\xi)&=\frac\xi2\frac{a_{K,0}(\xi)}{L_K(\xi)},\qquad
 p_K(\xi)=\frac{a_{K,2/\xi}(\xi)}{(2/\xi)L_K(\xi)}
           =\tfrac12\int R_K(d/\xi)\,d\mu.
 \end{split}
\tag{XL6}
\]

For any constant companion scale `lambda>0`, evaluated at this source
frequency, put `eta=lambda xi/2`. The exact scout identity is

\[
 \rho_{K,\lambda}(\xi)
 =\frac{a_{K,\lambda}(\xi)}{\lambda L_K(\xi)}
 =\frac{g_K}{\eta}+(p_K-g_K)\eta.
\tag{XL7}
\]

**Theorem.** As `xi -> +infinity`, for each fixed positive odd `K`, each
fixed integer `q>=0`, and each fixed real `h_0>=0`,

\[
 \int |d|^{2q}e^{h_0|d|}\,d\mu_{K,\xi}(d)
 \sim\frac{(2q+1)!!}{(2\pi e^\xi)^q}.
\tag{XL8}
\]

In particular this proves the bound in `L-106502.4`, and sharpens it to

\[
 m_2\sim\frac3{2\pi}e^{-\xi},\qquad
 g_K\sim\frac\pi K\xi^2e^\xi,\qquad
 p_K=\frac1{2K}+\frac{K^2-1}{4\pi K}\frac{e^{-\xi}}{\xi^2}
              +o(e^{-\xi}/\xi^2).
\tag{XL9}
\]

At `K=1`, `p_1=1/2` exactly. For every fixed real `c`,

\[
 \eta_\xi=1+c\frac{e^{-\xi}}{\xi^2}+o(e^{-\xi}/\xi^2)
 \quad\Longrightarrow\quad
 \rho_{K,\lambda_\xi}(\xi)\longrightarrow
             \frac1{2K}-\frac{2\pi c}{K}.
\tag{XL10}
\]

Here `lambda_xi=2 eta_xi/xi` labels pointwise evaluations. It does not
replace a physical constant companion by a Fourier multiplier in any
index theorem. The analytic assertions hold for every fixed odd `K`, not
only for the bounded orders in the companion algebra checker.

## 3. A global tail bound, including the unbalanced region

For `t>=0`, let `U(t)=exp(9t/2-pi exp(2t))`. The first term of (XL2),
using `pi>3`, gives `phi_0(t)>=pi^2 U(t)`. For the upper bound,

\[
 \phi_0(t)\le2\pi^2 U(t)
 \sum_{n\ge1}n^4e^{-\pi(n^2-1)e^{2t}}.
\]

For every integer `n>=1`, `n<=2^(n-1)` and `n^2-1>=3(n-1)`. Thus the
sum is at most `1/(1-r_t)`, where
`r_t=16 exp(-3 pi exp(2t)) <16 exp(-9)<1/32`, using `e>2`. Consequently

\[
 \pi^2U(t)\le\phi_0(t)\le(64/31)\pi^2U(t)<3\pi^2U(t).
\tag{XL11}
\]

The same argument with `n>=2` bounds the relative tail by `r_t/(1-r_t)`.
In particular,

\[
 \frac{\phi_0(t)}{2\pi^2 U(t)}
 =1-\frac3{2\pi e^{2t}}+O(e^{-3\pi e^{2t}})\longrightarrow1.
\tag{XL12}
\]

The remainder is nonnegative and at most
`(512/31) exp(-3 pi exp(2t))`; this is a bound, not a fitted expansion.

For `|d|<=xi`, both arguments of `Phi` are nonnegative, and (XL11) gives

\[
 \frac{H_\xi(d)}{H_\xi(0)}
 \le9\exp\{-2\pi E(\cosh d-1)\}.
\]

For `d>=xi`, use evenness and set `a=d-xi>=0`. Now
`|u|+|v|=d` and `exp(2|u|)+exp(2|v|)=2 exp(d) cosh(xi)`. The exact identity

\[
 e^d\cosh\xi-e^\xi\cosh d=\sinh(d-\xi)
\]

shows that the same upper estimate receives only the extra factor
`exp(9a/2-2 pi sinh(a))<=1`, since `sinh(a)>=a` and `2pi>9/2`.
Reflection handles `d<=-xi`. Therefore, for all `xi>0` and real `d`,

\[
 0<\frac{H_\xi(d)}{H_\xi(0)}
 \le9e^{-2\pi E(\cosh d-1)}
 \le9e^{-\pi E d^2}.
\tag{XL13}
\]

There is no omitted exterior region or uncontrolled tail polynomial.

For completeness the normalization has an explicit lower bound, independent
of the asymptotic argument. If `xi>=1` and `|d|<=E^(-1/2)`, (XL11) also
gives

\[
 H_\xi(d)/H_\xi(0)\ge\tfrac19
 e^{-2\pi E(\cosh d-1)}\ge\tfrac19e^{-2\pi}.
\]

Here `|d|<=1`, and `cosh(d)-1<=d^2`, for example by the power series and
`cosh(1)<2`. The latter follows from `e<3` and `e^(-1)<1`.
With `kappa_K=K 2^(1-K)` and (XL5), integration over that interval yields

\[
 Z_{K,\xi}\ge\frac{2e^{-2\pi}}{27}\,
 \kappa_K\xi^{K-1}H_\xi(0)E^{-3/2}>0.
\tag{XL14}
\]

All moments and denominators used here are thus finite, and `L_K>0`.

## 4. Laplace limit and the current's extra two powers

Set `epsilon=(pi E)^(-1/2)`. For fixed real `y`, both
`(xi +/- epsilon y)/2` tend to infinity, so (XL12) gives

\[
 \frac{H_\xi(\epsilon y)}{H_\xi(0)}\longrightarrow e^{-y^2}.
\tag{XL15}
\]

Indeed the leading linear prefactors cancel in the balanced product, and
`2pi E(cosh(epsilon y)-1)->y^2`. For any fixed integer `j>=0` and fixed
`h>=0`, substitute `d=epsilon y` in
`I_j(xi;h)=integral d^(2j) exp(h|d|) H_xi(d) dd`. The global bound (XL13)
dominates the rescaled integrand by
`9 |y|^(2j) exp(-y^2+h|y|)` for `epsilon<=1`. It is integrable. Dominated
convergence proves

\[
 I_j(\xi;h)\sim H_\xi(0)\epsilon^{2j+1}\Gamma(j+\tfrac12).
\tag{XL16}
\]

This is an actual-kernel limit. A Gaussian has emerged from the proved
rescaling and global domination; it has not been substituted for the source.

In the finite polynomial (XL5), the term `j=0` dominates each moment:
relative to it every term `j>=1` is `O_K((E xi^2)^(-j))`, by (XL16).
Consequently the ratio defining (XL8) is asymptotic to

\[
 \epsilon^{2q}\frac{\Gamma(q+3/2)}{\Gamma(3/2)}
 =\frac{(2q+1)!!}{(2\pi E)^q}.
\]

The underlying *unweighted* product has second moment `1/(2pi E)`;
the literal current weight starts with `d^2`, changing it to `3/(2pi E)`.
Dropping that current weight would give the wrong gain constants if combined
with the source formulas.

## 5. Gain, adapted phase, and the sharp transition

The first two formulas of (XL6), together with (XL16), give

\[
 g_K=\frac{\xi^2}{2}
 \frac{\int P_K(d^2/\xi^2)H_\xi(d)\,dd}
      {\int d^2Q_K(d^2/\xi^2)H_\xi(d)\,dd}
 \sim\frac{\xi^2}{2K}\frac{I_0(\xi;0)}{I_1(\xi;0)}
 =\frac\pi K\xi^2E.
\tag{XL17}
\]

The displayed final equality refers to the ratio of the leading terms.
Equivalently, for every `delta>0` the gain lies between
`(1-delta) pi xi^2 E/K` and `(1+delta) pi xi^2 E/K` for all sufficiently
large `xi` (with the lower assertion relevant for `delta<1`).

For all real `x`, the coefficient inequalities give `1/K<=R_K(x)<=K`.
Expansion at zero gives

\[
 R_K(x)=\frac1K+\frac{K^2-1}{3K}x^2+O_K(x^4).
\tag{XL18}
\]

The remainder bound can be taken global: on `|x|<=1` use the rational
function with `Q_K(x^2)>=K`; on `|x|>=1` use boundedness of `R_K` and
`1+x^2<=2x^4`. Taking expectations in (XL18) yields

\[
 p_K=\frac1{2K}+\frac{K^2-1}{6K}\frac{m_2}{\xi^2}
                       +O_K(m_4/\xi^4),
\]

which proves (XL9), including the exact `K=1` case. Finally, use the exact
identity

\[
 \rho-p_K=(\eta-1)\{p_K-g_K(1+1/\eta)\}.
\tag{XL19}
\]

Combining it with (XL9) proves (XL10). For `eta=1+c e^(-xi)/xi^2`
without an additional remainder, convergence is uniform for `c` in any
fixed compact interval.

For an exact tolerance `M>=0`, eventually `g_K>p_K>0`. Then `rho` is
strictly decreasing in `eta>0`, and `|rho|<=M` is precisely the interval
with endpoints

\[
 \eta_- =\frac{\sqrt{M^2+4(g_K-p_K)g_K}-M}{2(g_K-p_K)},\quad
 \eta_+ =\frac{\sqrt{M^2+4(g_K-p_K)g_K}+M}{2(g_K-p_K)}.
\]

The unique zero is `eta_c=sqrt(g_K/(g_K-p_K))`. The asymptotics are

\[
 \begin{split}
 \eta_c&=1+\frac1{4\pi}\frac{e^{-\xi}}{\xi^2}
                         +o(e^{-\xi}/\xi^2),\\
 \eta_\pm&=1+\left(\frac1{4\pi}\mathbin{\pm}\frac{KM}{2\pi}\right)
                      \frac{e^{-\xi}}{\xi^2}+o(e^{-\xi}/\xi^2),\\
 \eta_+-\eta_-&=\frac{M}{g_K-p_K}
            \sim\frac{KM}{\pi}\frac{e^{-\xi}}{\xi^2}\quad(M>0).
 \end{split}
\tag{XL20}
\]

For `M=0` the two endpoints coincide exactly. One may obtain their
expansions directly from the displayed root formulas; no inversion of a
merely pointwise limit is needed. The common shift `1/(4pi)` is independent
of `K`, while the width depends on `K`.

## 6. The original untranslated current profile

The exact source identity in `L-106502.3` is

\[
 \frac{J_{K,h}}{hL_K}=\int\frac{\sinh(hd)}{hd}\,d\mu,\qquad
 r^\sharp_{K,h}=\frac{hL_K}{J_{K,h}}.
\]

For `0<=h<=h_0`, the Taylor remainder after `1+(hd)^2/6` is nonnegative
and bounded by a constant times `h^4d^4 exp(h_0|d|)`. Equations (XL8)--(XL9)
therefore show

\[
 \frac{J_{K,h}}{hL_K}=1+\frac{h^2}{4\pi}e^{-\xi}
                       +o(h^2e^{-\xi}),\qquad
 1-r^\sharp_{K,h}=\frac{h^2}{4\pi}e^{-\xi}
                       +o(h^2e^{-\xi}).
\tag{XL21}
\]

The remainders divided by `h^2 exp(-xi)` tend to zero uniformly for
`0<h<=h_0`, for each fixed finite `h_0>0`; at `h=0` use continuity.
Indeed the second-moment relative error is independent of `h`, the
fourth-moment contribution after division is `O(h_0^2 exp(-xi))`, and
inverting `1+O(h^2 exp(-xi))` preserves that uniformity. No causal factor
`exp(-h xi)` is introduced.

## 7. Verification and remaining boundary

The companion exact checker verifies the theta differential-operator
coefficients, the Fourier factor-of-two algebra, binomial current weights,
Gaussian moment constants, the Taylor coefficient of `R_K`, and phase
constants for `K=1,3,...,15`, `q=0,...,6`. It authenticates every pinned
repository source by commit, Git blob, and LF-normalized SHA-256; the JSON
fixture also binds this note, checker, tests, and manifest. Its arithmetic
class is exact integer/rational algebra with symbolic `pi`; it performs
no floating-point Xi evaluation, quadrature, fitted asymptotic, or directed
transcendental computation. The theorem for all fixed `K,q` is proved in
the text, not inferred from that finite panel.

Replay completed: 14 unit tests passed in normal Python and under `-O`;
the producer passed in both modes; Ruff lint and formatting checks passed.
The replay includes 224 balanced/unbalanced exact current-weight identities,
the `K=1` and `q=0` edges, factor-of-two rejection, missing-source rejection,
scope/type mutation rejection, and input/resource guards. Commands:

```text
python -m unittest discover -s tests -p test_xi_actual_kernel_laplace_concentration.py
python -O -m unittest discover -s tests -p test_xi_actual_kernel_laplace_concentration.py
python research/exploratory/xi_actual_kernel_laplace_concentration.py --check
python -O research/exploratory/xi_actual_kernel_laplace_concentration.py --check
```

External mathematical inputs are precisely the classical theta inversion
and gamma/Mellin identity cited in Section 1; their formulas are explicit.
The checker authenticates the declared external reference contract, not
remote page contents or a formal proof of those classical identities.
The only historical `L-105413` input used is its literal series (XL2).

This closes a real source-concentration calculation, not the nonlocal
geometry required by the main program. It does not identify source
frequency with the physical carrier, construct a source-Pick congruence,
transport a multiplier through an outer factor or an all-pass phase,
control collective/confluent model-space localization, or bound the
topological free energy. No ninety-percent, density-one, or RH conclusion
is claimed. No novelty claim is made for classical Laplace concentration.

The smallest analytic statement whose failure would invalidate the new
concentration result is the global product estimate (XL13) for the literal
kernel, together with the local first-orbit limit (XL12); both have explicit
proofs above, and (XL14) independently supplies the denominator lower bound.
