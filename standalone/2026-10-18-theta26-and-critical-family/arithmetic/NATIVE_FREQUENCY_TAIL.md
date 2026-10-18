# A proved high-frequency removal for the complete native Newton amplitude

**Status:** PROPOSED complete deduction from the exact native transform and
classical published zeta estimates. The conclusion is a bound for a retained
frequency sector, not a new zero-free strip or a subquadratic recurrence.

**Scope:** ordinary rational Möbius, the literal old prefix at every integer
`Y>=2`, the complete strict square step, and every real Mellin frequency.
Physical restriction is performed after frequency decomposition and is paid
by the `L^2` contraction property. The two operations are not interchanged.

**What is proved:** all input frequencies `|t|>Y^(84/71)` have subpower total
squared norm, uniformly in `Y`. A classical twelfth-moment argument separately
gives the cutoff `Y^(6/5)`. The newly reported twelfth-moment refinement gives
a slightly smaller cutoff than `6/5`, but it is still weaker here than the
published pointwise exponent. None of these numbers is a zeta zero boundary.

## 1. Exact source and spectral normalization

Keep the native definitions from PR #994 at commit
`c93ca65a510b6acaf167f929b9bf7e67d742b05a`:

\[
g_Y(n)=\mu(n)\mathbf1_{n\le Y},\qquad z_Y=g_Y*g_Y,
\qquad G_Y(s)=\sum_{n\le Y}\mu(n)n^{-s},
\]

\[
R(x)=H_{\lfloor x\rfloor}-\log x-\gamma,
\qquad Z_Y(x)=\sum_{d\le Y^2}\frac{z_Y(d)}d R(x/d).
\]

All products `d<=Y^2`, including `d>x`, occur. Let

\[
a_Y(u)=e^{u/2}Z_Y(e^u),\qquad
\Phi_Y(t)=\frac{\zeta(1/2+it)G_Y(1/2+it)^2}{-1/2+it}.
                                                               \tag{1.1}
\]

The Fourier convention is `ahat(t)=int a(u) exp(-itu)du`. The exact native
Mellin identity is

\[
\widehat a_Y(t)=\Phi_Y(t).                              \tag{1.2}
\]

For completeness, `f(u)=e^(u/2)R(e^u)` is in `L^1 cap L^2`, and
`fhat(t)=zeta(1/2+it)/(-1/2+it)`. In `a_Y`, the term with `d` is
`z_Y(d)d^(-1/2) f(u-log d)`, whose Fourier multiplier is
`z_Y(d)d^(-1/2-it)`. Summing these finite terms gives `G_Y(1/2+it)^2`.
This explains both the power of `d` and the Fourier sign in (1.2).

Define the complete input tail

\[
\mathcal H(Y,T)=\int_{|t|>T}|\Phi_Y(t)|^2\,dt,
\qquad T\ge1.                                          \tag{1.3}
\]

No assumption about the zero set of zeta occurs in this definition.

## 2. Elementary full moments of the finite Möbius polynomial

For each fixed integer `j>=1`,

\[
\int_T^{2T}|G_Y(1/2+it)|^{2j}\,dt
\ll_j (T+Y^j)(\log(2Y))^{j^2+1}.                       \tag{2.1}
\]

Here is an elementary derivation sufficient for the powers used below.
Expand `G_Y(s)^j=sum_(n<=Y^j)b_j(n)n^(-s)`. The coefficients retain every
ordered `j`-tuple and every individual prefix cap; `|b_j(n)|<=d_j(n)`.
The time-integral Gram matrix of the frequencies `log n` has diagonal `T`.
Its off-diagonal entries have absolute value at most
`2/|log(n/m)|<=2Y^j/|n-m|`. Schur's row bound is consequently
`O(T+Y^j log(2Y))`. It remains to bound

\[
\sum_{n\le Y^j}\frac{d_j(n)^2}{n}
\le\sum_{n\le Y^j}\frac{d_{j^2}(n)}n
\ll_j(\log(2Y))^{j^2}.                                 \tag{2.2}
\]

The local inequality `d_j(p^k)^2<=d_(j^2)(p^k)` follows by counting
nonnegative `j` by `j` integer matrices of total sum `k`: every pair of
row and column compositions has at least one such matrix. Multiplicativity
gives the first inequality in (2.2), and expanding the divisor function into
`j^2` factors gives the harmonic-sum bound. This proves (2.1).

## 3. A tail bound from a pointwise subconvexity exponent

Assume the named direct bound

\[
|\zeta(1/2+it)|\ll_\varepsilon (1+|t|)^{\theta+\varepsilon},
\qquad 0\le\theta<1/2.                                 \tag{3.1}
\]

Apply (2.1) with `j=2` on each dyad `U<|t|<=2U`. Since
`|-1/2+it|^(-2)<=U^(-2)` there,

\[
\int_{U<|t|\le2U}|\Phi_Y(t)|^2\,dt
\ll_\varepsilon (YU)^\varepsilon
              U^{-2+2\theta}(U+Y^2).                  \tag{3.2}
\]

Choose the preliminary loss less than `1-2theta`. Each of the two terms
is then a convergent geometric series over `U=2^jT`, giving

\[
\boxed{\mathcal H(Y,T)
\ll_\varepsilon (YT)^\varepsilon
            T^{-2+2\theta}(T+Y^2).}                    \tag{3.3}
\]

Bourgain's published Theorem 5 gives `theta=13/84`. Its primary
`arXiv:1408.5794v2` PDF was freshly checked, including the exponent in
Theorem 5; the older abstract in some search indexes still shows `53/342`.
Thus

\[
\mathcal H(Y,T)
\ll_\varepsilon (YT)^\varepsilon T^{-71/42}(T+Y^2).
                                                               \tag{3.4}
\]

At `T=Y^(84/71)`, the term `Y^2 T^(-71/42)` is exactly one, while
`T^(-29/42)` decays. After assigning the preliminary loss,

\[
\boxed{\mathcal H(Y,Y^{84/71})\ll_\varepsilon Y^\varepsilon
\quad\text{for every }\varepsilon>0.}                  \tag{3.5}
\]

This is an actual full-frequency upper estimate for the exact Möbius input.
It does not use any bound on a reciprocal zeta value.

## 4. Independent twelfth-moment bound and the recent refinement

The classical Heath-Brown twelfth moment gives

\[
\int_U^{2U}|\zeta(1/2+it)|^{12}\,dt
\ll_\varepsilon U^{2+\varepsilon}.                      \tag{4.1}
\]

Hölder with exponents `6` and `6/5`, followed by interpolation of the
`24/5` moment of `G_Y` between its fourth and sixth moments, yields

\[
\begin{aligned}
\int_U^{2U}|\Phi_Y(t)|^2\,dt
&\ll U^{-2}
 \left(\int_U^{2U}|\zeta|^{12}\right)^{1/6}
 \left(\int_U^{2U}|G_Y|^{24/5}\right)^{5/6}\\
&\ll_\varepsilon (YU)^\varepsilon U^{-5/3}
                       (U+Y^2)^{1/2}(U+Y^3)^{1/3}.
\end{aligned}                                          \tag{4.2}
\]

The interpolation is exact: the fourth- and sixth-moment integrals have
powers `3/5` and `2/5` before raising to `5/6`, and therefore powers
`1/2` and `1/3` afterward. No noninteger Dirichlet-polynomial expansion
is used. On doubling `U`, the last two factors grow by at most `2^(5/6)`,
so summing the decaying dyads proves

\[
\boxed{\mathcal H(Y,T)
\ll_\varepsilon (YT)^\varepsilon T^{-5/3}
                        (T+Y^2)^{1/2}(T+Y^3)^{1/3}.}   \tag{4.3}
\]

In particular, `H(Y,Y^(6/5))<<_epsilon Y^epsilon`.

For the optional recent input, de Faveri--Pandey,
`arXiv:2610.01035v1`, Theorem 10.1, states precisely

\[
\int_0^U|\zeta(1/2+it)|^{12}\,dt
\ll_\varepsilon U^{2-\delta_{12}+\varepsilon},
\qquad \delta_{12}=\frac{520}{445121}.                  \tag{4.4}
\]

This primary theorem and its normalization were freshly retrieved. Taking
it as an imported result replaces `-5/3` in (4.3) by
`-5/3-delta_12/6`, and gives the sufficient cutoff exponent

\[
\frac{12}{10+\delta_{12}}
=\frac{890242}{741955}\approx1.199859829774.
\]

This is a source-qualified optional refinement of (4.3), not a new proof of
(4.4). It does not improve the stronger cutoff `84/71≈1.183098591549`
already obtained in (3.5). The recent square-root-phase theorem is not
silently applied to the native `G_Y` polynomial: its explicit phase and
coefficient hypotheses would require a separate transformation.

## 5. Restricting to the exact native square step

Set `b=Y+1`, define `m(x)=sum_(n<=x)mu(n)/n`, and put
`F_N=sum_(k<=N)|m(k)|^2`. The native Newton identity is exact for
`b<=x<b^2`:

\[
m(x)=A_Y(x)-Z_Y(x),\qquad
A_Y(x)=2M_YB_Y+M_Y^2\log(Y^2/x),                         \tag{5.1}
\]

\[
M_Y=m(Y),\qquad
B_Y=1+\sum_{n\le Y}\frac{\mu(n)\log n}{n}
                 -(\log Y+\gamma/2)M_Y.
\]

It holds throughout each real unit cell, not only at its left endpoint:
both sides use the same floor cutoffs in the finite harmonic sums. At the
strict endpoint `b^2`, the first possible Newton coefficient defect occurs;
that endpoint is excluded.

For every native reciprocal crossing, `|M_Y|<=1/Y`. The elementary identity

\[
B_Y=(\gamma/2)M_Y+
       \sum_{n\le Y}\frac{\mu(n)}n R(Y/n)
\]

and `|R(t)|<=1/t` for `t>=1` give `|B_Y|<=1+(gamma/2)|M_Y|`.
Consequently

\[
\|A_Y\|_{L^2([b,b^2),dx)}\ll1                          \tag{5.2}
\]

at those crossings. The constant component uses the interval length
`O(Y^2)`, and `int_b^(b^2) log^2(Y^2/x) dx=O(Y^2)` handles the second
component. The cofinality of these literal crossings is the classical
Landau argument supplied in the frozen native source; no gap estimate
between crossings is needed here.

In the logarithmic coordinate let

\[
W_Y(u)=\mathbf1_{[\log b,2\log b)}(u),\qquad
a_{Y,\le T}=\mathcal F^{-1}
        [\mathbf1_{|t|\le T}\Phi_Y(t)],
\quad a_{Y,>T}=a_Y-a_{Y,\le T}.                         \tag{5.3}
\]

These inverse transforms are interpreted in `L^2`. Multiplication by the
physical indicator is a contraction, so Plancherel gives

\[
\|W_Ya_{Y,>T}\|_2^2
\le\|a_{Y,>T}\|_2^2=\frac1{2\pi}\mathcal H(Y,T).       \tag{5.4}
\]

In contrast, the restricted low-frequency component has Fourier transform
`(2pi)^(-1) What_Y * [1_(|t|<=T) Phi_Y]`. Its frequency support is not
claimed to stay inside `[-T,T]` after this physical multiplication.

Change variables `x=e^u` in (5.1). The native step norm equals
`sqrt(F_(b^2-1)-F_Y)`, exactly, because `m(x)` is constant on the same unit
cells. Combining (5.1)--(5.4) with the reverse triangle inequality gives

\[
\boxed{
\left|\sqrt{F_{b^2-1}-F_Y}-\|W_Ya_{Y,\le T}\|_2\right|
\ll1+\sqrt{\mathcal H(Y,T)}.}                           \tag{5.5}
\]

At `T=Y^(84/71)` the right side is `O_epsilon(Y^epsilon)` for every
`epsilon>0`. Thus the high-frequency sector has been fully paid, coherently,
on the original output. Mixed terms are handled by this root-norm estimate;
none is erased from the energy.

## 6. The attempted positive-power contraction

The remaining object in (5.5) is the actual signed, physically restricted
low-frequency input. It still includes all frequencies in every fixed
compact interval. The frequency-tail bound does not control this component.

For example, partial summation gives at a native crossing

\[
G_Y(s)=Y^{1-s}m(Y)+(s-1)\int_1^Y m(x)x^{-s}\,dx,
\]

and on `Re s=1/2`, for bounded `t`, Cauchy--Schwarz gives only

\[
|G_Y(1/2+it)|
\ll (1+|t|)\sqrt{1+F_Y}\,(\log(2Y))^{1/2}.             \tag{6.1}
\]

Squaring the native spectral amplitude uses the fourth power of `G_Y`.
Even on a fixed compact frequency interval, inserting (6.1) therefore costs
`O((1+F_Y)^2 log^2(2Y))`. Direct zeta moments at large height do not
replace this quadratic power by `p<2` on that interval. This calculation
identifies a failed estimate; it is not an impossibility theorem for a
more arithmetic or correlated treatment of the low-frequency component.

An improvement of the ordinary boundary still requires a complete estimate
for `||W_Y a_(Y,<=Y^(84/71))||_2^2` with a genuinely better power of the
old native energy, and with any scale penalty explicitly paid. No such
positive-power contraction has been proved in this packet. The actual
advance here is (3.5) and its complete native consumer (5.5).

## Primary references

- [Frozen native Newton source, PR #994](https://github.com/GettysburgResearch/riemann/blob/c93ca65a510b6acaf167f929b9bf7e67d742b05a/standalone/2026-10-18-theta20-and-native-cancellation/native/PROOF.md),
  especially its exact square-step identity and Section 7 Mellin transform.
- J. Bourgain, *Decoupling, exponential sums and the Riemann zeta function*,
  [arXiv:1408.5794v2, Theorem 5](https://arxiv.org/pdf/1408.5794v2),
  published in JAMS 30 (2017), 205--224. This supplies the direct exponent
  `13/84`, not any reciprocal or zero-free assertion.
- D. R. Heath-Brown, *The twelfth power moment of the Riemann-function*,
  Quart. J. Math. 29 (1978), 443--462,
  [DOI](https://doi.org/10.1093/qmath/29.4.443).
  Its classical moment contract is also explicitly stated in the next
  primary paper's introduction.
- A. de Faveri and M. Pandey, *The sixth moment of the Riemann zeta function*,
  [arXiv:2610.01035v1, Theorem 10.1](https://arxiv.org/html/2610.01035v1#S10),
  for the optional recent twelfth-moment refinement only.
