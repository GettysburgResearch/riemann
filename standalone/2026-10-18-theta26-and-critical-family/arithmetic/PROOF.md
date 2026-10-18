# Actual quadratic families throughout Re s > 1/2: quantitative residual transfer and optimal local variance removal

**Status:** PROPOSED complete analytic component estimates, requiring independent
review. These estimates improve the actual-family domain and allow growing
mollifiers. They do not improve a zero-free boundary for ordinary zeta, and do
not prove RH or an individual quadratic GRH.

**Scope:** the actual primitive quadratic characters of discriminants `-8u`,
with `Q<u<=2Q`, `u` odd and squarefree; every fixed compact subset of
`1/2<Re s<1`; positive conditioning on finitely many prescribed local states;
all finite mollifier horizons; and explicit polynomially growing horizons.
Every full-product residual contains the common factor `zeta(s)`.

**New estimates relative to PR #1001:** its elementary full-L adapter required
`Re s>3/4` and fixed mollifier length. Here the quadratic large sieve supplies
an actual mean-square tail bound on every fixed line `Re s>1/2`. A quantitative
transfer theorem then permits growing mollifiers. Separately, a constructive
least-squares theorem removes the auxiliary local variance with the optimal
finite-prime multiplier, and the resulting small residual is proved for actual
quadratic fields with growing prime support. No literature-priority claim is
made for the classical large-sieve or Euler-product ingredients.

**Inputs:** Heath-Brown's quadratic large sieve; the primitive quadratic
functional equation; and the elementary squarefree character average proved
in PR #1001, restated below. No recent proposed zero-free theorem is an input.

**Smallest remaining gap for ordinary zeta:** an upper bound for the retained
rational bias, such as a complete strict-below-one bound for
`|zeta(s) M_Z(s)-1|`. The variance-removal theorem proves that the additional
quadratic fluctuation can be made small; it does not bound that bias.

## 1. Family, local law, and notation

Let

\[
\mathcal U(Q)=\{u:Q<u\le2Q,\ u\text{ odd and squarefree}\},
\quad \chi_u=\chi_{-8u},\quad N_Q=|\mathcal U(Q)|.
\]

These are primitive odd characters of conductor `q=8u`, with root number one.
Write `E_Q` for the uniform average. Then
`N_Q=(4/pi^2)Q+O(sqrt Q)`. For odd positive `n`, the elementary character
average from PR #1001 is

\[
\mathbb E_Q\chi_u(n)
=\mathbf1_{n=\square}g(n)
 +O\!\left(Q^{-1/2}n^{1/4}\log(2n)\right),
\qquad g(n)=\prod_{p\mid n}\frac p{p+1}.                 \tag{1.1}
\]

For even `n` both the actual character and the limiting variable are zero.
The proof of (1.1) expands `mu^2(u)`, applies Pólya--Vinogradov below a
square-divisor cutoff, and counts multiples above it. In the square case it
retains the coprimality mask. It requires no zero-free premise.

Let independent variables at odd primes have the distribution

\[
\Pr(X_p=0)=\frac1{p+1},\qquad
\Pr(X_p=1)=\Pr(X_p=-1)=\frac p{2(p+1)},\qquad X_2=0,
\]

and extend them completely multiplicatively to `X(n)`. Expectations without
a subscript refer to this model. Thus

\[
\mathbb E X(n)=\mathbf1_{n=\square}g(n)\quad(n\text{ odd}).
                                                               \tag{1.2}
\]

Fix a compact set `K` in `1/2<Re s<1`; put
`sigma_0=min_(s in K) Re s`, `sigma_1=max_(s in K) Re s`, and assume
`1/2<sigma_0<=sigma_1<1`. All height bounds are compact, not growing with `Q`.
At one point write

\[
\sigma=\Re s,\qquad h=\sigma-\tfrac12>0,
\qquad \lambda=\tfrac54-\sigma>0,
\qquad L=2\lambda=\tfrac52-2\sigma.                     \tag{1.3}
\]

Constants may depend on the compact set, a fixed local condition, and a
requested positive loss. No constant is uniform as `sigma_0` decreases to
`1/2` or as a local condition acquires more primes.

### Fixed local conditions are allowed

Choose finitely many odd primes `S`, and prescribe `chi_u(p)=omega_p` with
`omega_p in {0,1,-1}` for `p in S`. Let `J_u` be the indicator and let
`J(X)` be the corresponding model indicator. Their limiting probability
`pi=E J(X)` is strictly positive. Use conditional averages `E_(Q,omega)`
and `E_omega` below when desired.

Indeed the local indicators are the polynomials
`1-X_p^2` and `(X_p^2 +/- X_p)/2`. Expanding their finite product in (1.1)
gives, uniformly in odd `n`,

\[
\mathbb E_{Q,\omega}\chi_u(n)
=\mathbb E_\omega X(n)
 +O_S\!\left(Q^{-1/2}n^{1/4}\log(2n)\right),             \tag{1.4}
\]

and the conditional family has cardinality `pi N_Q+O_S(sqrt Q)`.
For sufficiently large `Q` it therefore has positive density. An arbitrary
fixed nonnegative weight on these finite local states, of positive mean,
works by the same argument. Negative weights are not used as probability
weights in the norm estimates.

## 2. The actual full-L tail estimate

### Theorem A: mean-square approximation by an ordinary initial segment

For every `1<=K<=Q`, every `s` in the fixed compact set, and every
`epsilon>0`,

\[
\boxed{
\mathbb E_{Q,\omega}\left|
 L(s,\chi_u)-\sum_{n\le K}\chi_u(n)n^{-s}
\right|^2
\ll_{\mathcal K,S,\varepsilon} Q^\varepsilon K^{1-2\sigma}.}
                                                               \tag{2.1}
\]

This is a bound for the complete analytically continued `L`-value; it has no
exceptional-character deletion. The dual functional-equation sum is included
in its proof. The estimate is also valid without local conditioning.

There is also an actual complex-compact version:

\[
\mathbb E_{Q,\omega}\sup_{s\in\mathcal K}\left|
 L(s,\chi_u)-\sum_{n\le K}\chi_u(n)n^{-s}\right|^2
\ll_{\mathcal K,S,\varepsilon}Q^\varepsilon K^{1-2\sigma_0}.
                                                               \tag{2.1a}
\]

After proving (2.1), apply the submean inequality for the holomorphic
difference on a finite disc cover of `mathcal K`, lying in a slightly larger
compact set with minimum real part `sigma_0-tau>1/2`. Tonelli bounds the
expected supremum by a fixed multiple of the integral of (2.1) over that
larger set. The factor `K^(2tau)` is at most `Q^(2tau)`; choose `tau` and
the preliminary losses after the requested `epsilon`. This proves (2.1a)
without a height discretization or an inverse-L holomorphy assumption.

### 2.1. Quadratic large sieve with all square parts retained

The imported Heath-Brown inequality, for common complex coefficients, is

\[
\sum_{\substack{u\le U\\u\text{ odd squarefree}}}
 \left|\sum_{\substack{a\le V\\a\text{ odd squarefree}}}
       c_a\left(\frac au\right)\right|^2
\ll_\varepsilon (UV)^\varepsilon(U+V)\sum_a|c_a|^2.       \tag{2.2}
\]

Quadratic reciprocity, a split into residue classes modulo four, and fixed
column signs give the same inequality with `(a/u)` replaced by `chi_u(a)`.
Positive row restrictions preserve its upper bound. The conditional
normalization only contributes a fixed factor depending on `pi`.

We need a consequence for **all** odd column integers. Let `V>=1`, let
`|c_n|<=n^(-beta)` on `V<n<=2V`, with `beta` in a fixed bounded interval,
and let row-dependent weights `W_u(n)` have uniformly bounded supremum and
total variation on that dyad. Then

\[
\mathbb E_{Q,\omega}
 \left|\sum_{V<n\le2V}c_n\chi_u(n)W_u(n)\right|^2
\ll_\varepsilon (QV)^\varepsilon(1+V/Q)V^{1-2\beta}.
                                                               \tag{2.3}
\]

Here and below a partial endpoint of a dyad is permitted. To prove (2.3),
write **uniquely**

\[
n=a b^2,\quad a\text{ odd squarefree},\quad b\text{ odd};
\qquad \chi_u(n)=\chi_u(a)\mathbf1_{(u,b)=1}.             \tag{2.4}
\]

No condition `(a,b)=1` is imposed. For each fixed `b`, the row mask in
(2.4) is retained before enlarging the row sum in the nonnegative large-sieve
upper bound.

For clarity, row-dependent smooth weights do not become common coefficients
by assertion. The maximal initial-segment form of (2.2) costs at most two
powers of `log(2V)`. For each row, decompose an initial segment into disjoint
binary intervals, use Cauchy--Schwarz, then sum the large-sieve bounds for
all binary intervals. Each coefficient appears at most `O(log(2V))` times.
Abel summation now bounds each weighted sum by its weight's supremum plus
variation times that maximal initial-segment sum.

For the fixed `b` part of (2.4), the coefficient square mass is at most

\[
\sum_{V/b^2<a\le2V/b^2}(ab^2)^{-2\beta}
\ll V^{1-2\beta}/b^2,
\]

also when `V/b^2` lies between `1/2` and `1`. Its normalized row norm is
therefore at most

\[
(QV)^\varepsilon(1+V/Q)^{1/2}V^{1/2-\beta}/b.
\]

Minkowski and `sum_(b<=sqrt(2V)) 1/b << log(2V)` prove (2.3), after
shrinking the preliminary large-sieve loss. This logarithm is the square-part
cost specific to quadratic characters. It is not replaced by a convergent
sum, and repeated primes are not discarded.

### 2.2. Exact flat-cutoff functional equation

Fix a smooth real function `V(y)` equal to one on `0<y<=1` and zero on
`y>=2`. Its Mellin transform `Vhat(w)` is meromorphic with one simple pole,
at zero, of residue one, and decays faster than any power on each fixed
vertical line. Put

\[
P_K(s,u)=\sum_n\chi_u(n)n^{-s}V(n/K).
\]

The primitive functional equation gives the **exact** identity

\[
L(s,\chi_u)-P_K(s,u)
=(q/\pi)^{1/2-s}
 \sum_{n\ge1}\chi_u(n)n^{s-1}
       W_s(\pi nK/q),\qquad q=8u,                        \tag{2.5}
\]

where, for a sufficiently negative fixed real line,

\[
W_s(y)=-\frac1{2\pi i}\int_{(-c)}
 \widehat V(w)
 \frac{\Gamma((2-s-w)/2)}{\Gamma((s+w+1)/2)}y^w\,dw.
                                                               \tag{2.6}
\]

Here is a direct derivation. Mellin inversion writes `P_K` as an integral of
`L(s+w,chi_u) K^w Vhat(w)` on `Re(s+w)>1`. Shift to `Re(s+w)<0`.
The only crossed pole is `w=0`, because these characters are nonprincipal.
Use

\[
L(s+w,\chi_u)
=(q/\pi)^{1/2-s-w}
 \frac{\Gamma((2-s-w)/2)}{\Gamma((s+w+1)/2)}
 L(1-s-w,\chi_u)
\]

on the shifted line and expand the dual series there absolutely. This proves
(2.5)--(2.6), including its sign and scale. The root number is one for this
family; no varying phase has been suppressed.

Shifting (2.6) arbitrarily far left proves arbitrary polynomial decay for
large `y`, also for a fixed number of logarithmic derivatives. For small `y`
move to a sufficiently small positive line, crossing only `w=0`; the first
possible numerator gamma pole has real part `2-sigma>1`. Thus

\[
W_s(y)=\frac{\Gamma((2-s)/2)}{\Gamma((s+1)/2)}+O(y^c)
\quad(y\longrightarrow0)
\]

for some fixed `c>0`. The logarithmic derivative is bounded as well.
All these statements are uniform on the specified compact set. The Mellin
transform's rapid decay and the gamma quotient's polynomial vertical growth
justify the contour shifts and the interchange with the dual Dirichlet
series. In particular, on a dyad `n~V`, the weights and their variation are

\[
\ll_J \min\{1,(VK/Q)^{-J}\},                            \tag{2.7}
\]

uniformly in `Q<u<=2Q`. This supplies precisely the row-dependent weights
allowed in (2.3).

### 2.3. Completing the tail estimate

The difference between `P_K` and the sharp initial segment is supported on
`K<n<=2K`. Apply (2.3) with `beta=sigma` and `K<=Q`; its row norm is
`O(Q^epsilon K^(-h))`.

For the dual in (2.5), use (2.3) with `beta=1-sigma`. A column dyad has row
norm at most

\[
Q^{-h}(QV)^\varepsilon(1+V/Q)^{1/2}V^h
     \min\{1,(VK/Q)^{-J}\}.                              \tag{2.8}
\]

Set `R=Q/K`, so `1<=R<=Q`. Minkowski over `V<=R` gives
`O(Q^epsilon Q^(-h) R^h)=O(Q^epsilon K^(-h))` since `h>0`.
The separate dual unit `n=1` has norm `O(Q^(-h))`, which fits this bound.
Every dyad `V>R` is included using (2.7). Choose `J>h+1` after fixing
the compact set and the preliminary loss; the resulting dyadic series is
geometric and has the same bound. This also covers `V>Q`, where the factor
`(1+V/Q)^(1/2)` is present. Squaring and assigning the preliminary losses
after the requested `epsilon` proves (2.1).

## 3. The limiting analytic object, with its complete square kernel

The random Euler product

\[
\mathcal L(s)=\prod_{p\text{ odd}}(1-X_pp^{-s})^{-1}
\]

exists in `L^2` locally uniformly on `Re s>1/2`. Its Dirichlet initial
segments `T_K(s,X)=sum_(n<=K) X(n)n^(-s)` obey

\[
\|\mathcal L(s)-T_K(s,X)\|_{L^2(\mathbb P_\omega)}
\ll_{\mathcal K,S} K^{1/2-\sigma}(\log(2K))^{1/2}.       \tag{3.1}
\]

For the series proof, use (1.2). On one dyad the absolute square kernel is

\[
\sum_{\substack{V<n,m\le2V\\nm=\square}}(nm)^{-\sigma}
\ll V^{1-2\sigma}\log(2V).                              \tag{3.2}
\]

Indeed `n=ra^2,m=rb^2` with common squarefree `r`; the `r`-sum after
the two short power sums is bounded by `sum_(r<=2V)1/r`. Dyadic Minkowski
proves (3.1). A fixed local condition only multiplies the unconditional
nonnegative norm bound by `1/pi`.

The Euler product is the same object. For a local factor `f_p=(1-X_p x)^(-1)`,
`x=p^(-s)`, its mean and second moment differ from one by `O(p^(-2sigma))`.
Independence and `sum_p p^(-2sigma_0)<infinity` make the finite Euler products
Cauchy in `L^2`, locally uniformly. Both the product and the series are
holomorphic with values in that Hilbert space. They agree by absolute
convergence on `Re s>1`, hence throughout `Re s>1/2` by the identity theorem.
Conditioning on finitely many local states gives the same conclusion.

The square aliases in (3.2) survive; this argument does not replace them by
an artificial diagonal `n=m`.

## 4. Quantitative transfer for every finite polynomial

Let

\[
A_u(s)=\sum_{n\le X}c_n(s)\chi_u(n),\qquad
A(s,X_\bullet)=\sum_{n\le X}c_n(s)X(n),
\]

where the coefficients are common to all rows. They may depend on `Q`.
Define their **actual** absolute masses

\[
B=\sum_{n\le X}|c_n(s)|,\qquad
D=\sum_{n\le X}n^{1/4}|c_n(s)|.                         \tag{4.1}
\]

Let `z=z(s)` be any bounded scalar on the chosen compact set. In particular,
`z(s)=zeta(s)` is allowed on a compact set avoiding its pole. Define

\[
R_Q=\mathbb E_{Q,\omega}|zL(s,\chi_u)A_u(s)-1|^2,
\quad R_\infty=\mathbb E_\omega|z\mathcal L(s)A(s,X_\bullet)-1|^2.
\]

### Theorem B: a master estimate with the complete residual

For every `1<=K<=Q`,

\[
\boxed{
|\sqrt{R_Q}-\sqrt{R_\infty}|
\ll Q^\varepsilon |z| B K^{-h}
 +Q^{-1/4}\!\left(\log(2KX)\right)^{1/2}
       \bigl(1+|z|D K^\lambda\bigr).}                   \tag{4.2}
\]

This is valid with signs, zeros at ramified primes, and all square aliases.
The comparison concerns the norm of `zLA-1`, not an uncapped reciprocal
moment. Its proof never divides by `z` or by `L`.

**Proof.** By (2.1) and (3.1), replacement of `L` and `mathcal L` by their
respective initial segments changes either residual norm by at most
`O(Q^epsilon |z| B K^(-h))`. Expand the remaining polynomial residual as
`sum_l b_l chi_u(l)`, or with `X(l)` in the model. Its support is at most
`KX`; its weighted coefficient mass is at most

\[
\sum_l l^{1/4}|b_l|
\le1+|z|D\sum_{a\le K}a^{1/4-\sigma}
\ll1+|z|D K^\lambda.                                   \tag{4.3}
\]

Using (1.4) in the exact square of this polynomial gives a difference of
squared norms at most

\[
O_S\!\left(Q^{-1/2}\log(2KX)
             (1+|z|D K^\lambda)^2\right).              \tag{4.4}
\]

For nonnegative numbers `a,b`, `|sqrt(a)-sqrt(b)|<=sqrt(|a-b|)`.
Apply this to (4.4) and add the two tail errors. This proves (4.2).

A useful squared-norm form is

\[
|R_Q-R_\infty|
\ll Q^\varepsilon(1+|z|B)|z|B K^{-h}
 +Q^{-1/2}\log(2KX)(1+|z|D K^\lambda)^2.                 \tag{4.5}
\]

To justify its first term, both actual and model `L`-values have uniformly
bounded second moments on the fixed compact set. For the actual family this
already follows from (4.2) with `A=1,z=1,K=Q^(1/3)` and the bounded model
norm. Thus both residual norms are `O(1+|z|B)`, so the difference of their
squares caused by the tail is bounded as displayed. This use of (4.2) is
not circular: (4.2) required only the tail estimate and finite character
averages, not a uniform full-L second moment bound.
More explicitly, if a replacement changes a residual norm by at most
`Delta=O(Q^epsilon |z|B K^(-h))`, the change of its squared norm is at most
`2 O(1+|z|B) Delta+Delta^2`. The last term is absorbed in the first term
of (4.5), after shrinking the preliminary loss, because `K>=1` and
`|z|B<=1+|z|B`. A uniform bound for the truncated residual is therefore not
silently assumed.

### Explicit growing triangular inverse-Dedekind mollifiers

Take

\[
M_Z(s)=\sum_{m\le Z}\mu(m)m^{-s},\qquad
\mathcal M_{u,X}(s)
=\sum_{mn\le X}\mu(m)\mu(n)\chi_u(n)(mn)^{-s}.          \tag{4.6}
\]

This is the full inverse-Dedekind coefficient truncation; its principal
inverse factor is retained. The masses in (4.1) satisfy

\[
B\ll X^{1-\sigma}\log(2X),\qquad D\ll X^{5/4-\sigma}. \tag{4.7}
\]

For the second bound, group by `n`, use
`sum_(m<=X/n)m^(-sigma)<< (X/n)^(1-sigma)`, and then sum `n^(-3/4)`.
No Möbius cancellation is assumed in these two error bounds.

Fix `eta>=0`, take `X<=Q^eta`, and use the worst real part `sigma_0`
in the following exponents. If

\[
\eta<\frac{\sigma_0-1/2}{5/2-2\sigma_0},\qquad
\delta_1=\frac{\sigma_0-1/2-\eta(5/2-2\sigma_0)}3>0,
                                                               \tag{4.8}
\]

then choosing `K=Q^((1-eta)/3)` in (4.2) gives uniformly

\[
\boxed{|\sqrt{R_Q}-\sqrt{R_\infty}|
               \ll Q^{-\delta_1+\varepsilon}.}           \tag{4.9}
\]

For an absolute squared-residual asymptotic, the sufficient range is

\[
\eta<\frac{\sigma_0-1/2}{(5-4\sigma_0)(3/2-\sigma_0)},
\quad
\delta_2=
\frac{\sigma_0-1/2-\eta(5-4\sigma_0)(3/2-\sigma_0)}
     {4-2\sigma_0}>0.                                   \tag{4.10}
\]

Choosing `K=Q^((1-eta)/(4-2sigma_0))` in (4.5) gives

\[
\boxed{R_Q=R_\infty+O(Q^{-\delta_2+\varepsilon}).}        \tag{4.11}
\]

These are direct upper-error estimates for growing actual families and
growing mollifiers. At `sigma_0=3/4`, (4.9) allows every `eta<1/4`,
and (4.11) every `eta<1/6`. At `sigma_0=5/6`, the respective ranges are
`eta<2/5` and `eta<3/10`. The endpoints are not claimed.

All losses are chosen in the correct order: fix the compact set and `eta`
strictly within its range, then fix a requested error loss; finally choose
the finitely many preliminary large-sieve losses and dual decay orders.
There is no limiting assertion with these parameters varying toward their
endpoints.

For each fixed `X`, (4.11) extends the full residual identity of PR #1001
from `Re s>3/4` to every `Re s>1/2`. Its explicit random bias--variance
formula, with all square aliases, is unchanged. With `z=zeta(s)`, a
hypothetical ordinary zeta zero still gives `R_Q=1` exactly for every
finite `Q,X`.

## 5. A constructive optimal signed local projection

This section answers whether a more elaborate signed local probe can lower
the nonnegative auxiliary variance. It can be removed asymptotically, with an
explicit optimal finite-prime multiplier. The remaining scalar is visible.

Fix `y>=3` and set

\[
P_y=\prod_{3\le p\le y}p,\qquad
E_y(s,\chi)=\prod_{3\le p\le y}(1-\chi(p)p^{-s})
 =\sum_{d\mid P_y}\mu(d)\chi(d)d^{-s}.                  \tag{5.1}
\]

This is an actual finite Dirichlet polynomial with support up to the
primorial `P_y`. In the model write

\[
\mathcal L=\mathcal L_{\le y}\,\mathcal T_y,
\qquad \mathcal T_y=\prod_{p>y}(1-X_pp^{-s})^{-1},
\qquad C_y=\mathbb E\mathcal T_y,
\quad H_y=\mathbb E|\mathcal T_y|^2.                     \tag{5.2}
\]

These expectations converge for `Re s>1/2`; `C_y` is holomorphic and
nonzero there. In particular,

\[
C_y(s)=\prod_{p>y}
 \frac{1-(1-g_p)p^{-2s}}{1-p^{-2s}},\qquad g_p=\frac p{p+1}.
                                                               \tag{5.3}
\]

Let `N` be **any** complex function of the finite local states `X_p,p<=y`
(so arbitrary signed combinations of all such probes are allowed). Impose
the explicitly chosen mean constraint

\[
\mathbb E[\mathcal L N]=m,                              \tag{5.4}
\]

where `m=m(s)` is a specified scalar, not `1/zeta(s)` obtained by division.

### Theorem C: exact optimum at fixed principal mean

Among all `N` satisfying (5.4), the complete residual is minimized by

\[
\boxed{N_*(s,X_\bullet)=\frac{m(s)}{C_y(s)}
            \prod_{3\le p\le y}(1-X_pp^{-s}).}           \tag{5.5}
\]

The minimum is

\[
\boxed{
\min_N\mathbb E|z\mathcal L N-1|^2
=|zm-1|^2+|zm|^2\left(\frac{H_y}{|C_y|^2}-1\right).}    \tag{5.6}
\]

If `z!=0`, equality characterizes (5.5) almost surely. If `z=0`, every
residual is identically one, so uniqueness is not asserted.

**Proof.** Put `A=mathcal L_(<=y) N`. Every local Euler factor is nonzero,
so this is an invertible change of finite-state variables. The independent
tail gives `E[mathcal L N]=C_y E A=m`. Direct expansion yields

\[
\mathbb E|z\mathcal L N-1|^2
=|zm-1|^2
 +|zm|^2\left(\frac{H_y}{|C_y|^2}-1\right)
 +|z|^2H_y\,\mathbb E|A-\mathbb E A|^2.                 \tag{5.7}
\]

The last term vanishes precisely when `A=m/C_y` is constant. This proves
the result. The proof optimizes over the complete finite local state space,
not only linear characters or a guessed subspace.

For an explicit tail estimate put `x=p^(-s)` and
`d_p=1-(1-g_p)x^2`. The local relative variance is

\[
v_p(s)=
\frac{g_p|x|^2(1+(1-g_p)|x|^2)}{|d_p|^2}>0.
\]

Direct evaluation on the three states gives

\[
\frac{H_y}{|C_y|^2}=\prod_{p>y}(1+v_p),\qquad
0\le\frac{H_y}{|C_y|^2}-1
\ll_{\mathcal K}\sum_{p>y}p^{-2\sigma}
\ll_{\mathcal K}y^{1-2\sigma}.                         \tag{5.8}
\]

The last bound deliberately uses only comparison with the integer sum.
No prime-number asymptotic is needed. Equations (5.5)--(5.8) prove a positive,
constructive variance-removal theorem, not merely a lower-bound obstruction.

## 6. The variance removal holds in actual growing families

The primorial support in (5.1) must be paid. The master estimate does so
through its actual coefficient masses, which are much smaller than a bound
depending only on the maximum support.

For the unnormalized `E_y`,

\[
B_y=\prod_{3\le p\le y}(1+p^{-\sigma}),\qquad
D_y=\prod_{3\le p\le y}(1+p^{1/4-\sigma}).               \tag{6.1}
\]

In particular, by comparison with integer sums,

\[
\log B_y\ll_{\mathcal K} y^{1-\sigma_0},\qquad
\log D_y\ll_{\mathcal K} y^{5/4-\sigma_0},\qquad
\log P_y\le y\log y.                                   \tag{6.2}
\]

Fix

\[
0<\nu<\frac1{5/4-\sigma_0},\qquad
y=(\log Q)^\nu.                                         \tag{6.3}
\]

Then `B_y,D_y=Q^(o(1))`, uniformly on the compact set, and
`log(2K P_y)=Q^(o(1))`. This remains true when the primorial support is
larger than every fixed power of `Q`: it is (6.1), not an unproved
small-support assumption, that enters (4.2).

Take `K=Q^(1/3)`, `A=E_y/C_y`, and any fixed bounded scalar `m(s)` in
Theorem B. The model identity (5.6) and (4.2) give

\[
\left|
 \left(\mathbb E_Q\left|
  z(s)L(s,\chi_u)\frac{m(s)E_y(s,\chi_u)}{C_y(s)}-1
                     \right|^2\right)^{1/2}
 -\left(|zm-1|^2+|zm|^2
       \bigl(H_y/|C_y|^2-1\bigr)\right)^{1/2}
\right|
\ll Q^{-(\sigma_0-1/2)/3+\varepsilon}.                 \tag{6.4}
\]

The same statement follows for a fixed local condition once `y` includes
all its primes: the remaining random tail is independent and has the same
`C_y,H_y`; the fixed-conditioned large-sieve constants are retained.

In particular, set `z=m=1`. A complete actual-family upper bound is

\[
\boxed{
\mathbb E_Q\left|
 L(s,\chi_u)\frac{E_y(s,\chi_u)}{C_y(s)}-1
                 \right|^2
\ll_{\mathcal K,\nu,\varepsilon}
 y^{1-2\sigma}+Q^{-2(\sigma_0-1/2)/3+\varepsilon}.}       \tag{6.5}
\]

All members, including any that vanish at the tested point, remain in this
average. Equation (6.5) is an auxiliary-family residual bound tending to
zero; it does not prove that every member is nonzero. A persistent individual
zero would contribute `1/N_Q`, which is compatible with the bound.

For the full common-factor detector, take `z=zeta(s)` and the specified
ordinary Möbius polynomial `m=M_Z(s)` with `Z` fixed. Then (6.4) says

\[
\lim_{Q\to\infty}
\mathbb E_Q\left|
 \zeta(s)L(s,\chi_u)M_Z(s)\frac{E_y(s,\chi_u)}{C_y(s)}-1
                 \right|^2
=|\zeta(s)M_Z(s)-1|^2.                                  \tag{6.6}
\]

This is the achieved constructive reduction of the variance. The normalizer
`1/C_y` is an explicit absolutely convergent Euler product on `Re s>1/2`.
It contains neither `1/zeta(s)` nor a reciprocal of an actual `L`-value.
It is holomorphic and nonzero there. The resulting multiplier is a finite
Dirichlet polynomial times an explicit holomorphic factor; it is not claimed
to have constant Dirichlet coefficients as a function of `s` after that
normalization.

At an ordinary zeta zero `rho`, every full residual on the left side of
(6.6) is exactly one. The right side is also one. A strict-below-one theorem
must therefore control the ordinary scalar, and none of (2.1), (4.11), or
(6.5) supplies that missing cancellation. In particular, this packet does
not claim to beat the repository's reported ordinary-zeta benchmark.

## Sources and replay

- D. R. Heath-Brown, *A mean value estimate for real character sums*,
  Acta Arithmetica 72 (1995), 235--275,
  [publisher and DOI](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/72/3/108575/a-mean-value-estimate-for-real-character-sums).
- K. Soundararajan and M. P. Young, *The second moment of quadratic twists
  of modular L-functions*, JEMS 12 (2010), 1097--1116,
  [primary paper, Theorem 2.4](https://ems.press/content/serial-article-files/31734).
  This freshly retrieved theorem gives exactly the squarefree quadratic
  large-sieve contract (2.2). No GRH-dependent theorem from that paper is used.
- PR #1001, the previous exact shared-factor packet, supplies (1.1) and the
  explicit triangular-mollifier bias--variance identity. Its weaker `3/4`
  full-L adapter remains frozen; Sections 2--4 here supply the stronger
  replacement proof without modifying that historical packet.

The accompanying finite checker tests the local least-squares identities,
the full square-part decomposition including shared primes, and the exact
parameter balances. It does not certify Heath-Brown's theorem, analytic
continuation, any infinite limit, or any zero-free region.
