# Hard opposite-boundary forcing cannot satisfy the exterior growth budget

**Status: PROPOSED complete analytic obstruction.** This excludes a broad
repair of the cofinal domain-wall construction, including arbitrary
ferromagnetic interior graphs, replicated endpoint gadgets, and an
additional antiferromagnetic closing bond charged by the stated budget.
It does not exclude every correlated-field construction.

## 1. General two-endpoint setup

Let`mu_0` be any finite zero-field ferromagnetic Ising law on any graph,
with couplings`J_e>=0`. Choose distinct endpoints`u,v`, assign them
positive observable weights`B_u,B_v`, and assign every remaining observed
spin a nonnegative weight. Let

\[
 Y=B_u\sigma_u+B_v\sigma_v+Y_{\rm int}.
\]

Modify the law only by opposite endpoint fields and an optional negative
endpoint bond:

\[
 d\mu_{H,K}\ \propto\
 e^{H(\sigma_u-\sigma_v)-K\sigma_u\sigma_v}\,d\mu_0,
 \qquad H,K\ge0. \tag{1}
\]

The positive interior graph is unrestricted. All its edges, sizes,
observable weights and strengths may vary with the approximation index.

For every`R>0`,

\[
 \boxed{E_{H,K}e^{RY}\ge\frac14
         e^{R(B_u+B_v)-2(H+K)}.} \tag{2}
\]

In particular, if the forcing resource obeys

\[
 H+K\le b\min(B_u,B_v), \tag{3}
\]

then

\[
 E_{H,K}e^{RY}\ge\frac14e^{(R-b)(B_u+B_v)}. \tag{4}
\]

For any fixed`R>b`, a common budget`E exp(RY)<=M` therefore imposes the
quantitative caps

\[
 B_u+B_v\le\frac{\log(4M)}{R-b},\qquad
 H+K\le\frac{b\log(4M)}{2(R-b)}. \tag{5}
\]

Hard forcing with`H+K` tending to infinity is impossible under that
budget. This conclusion pays no entropy factor for the number of
interior spins.

## 2. Proof without an unproved correlation estimate

Zero-field spin reversal and the nonnegative high-temperature expansion
give`c=E_0 sigma_u sigma_v>=0`, and

\[
 P_0(\sigma_u=\sigma_v=+1)=\frac{1+c}4\ge\frac14.
\]

The needed nonnegative correlations follow directly by expanding every
edge factor as`cosh(J_e)(1+sigma_i sigma_j tanh(J_e))`: correlations are
ratios of sums of nonnegative edge-product terms with prescribed odd
boundary.

The density multiplier in (1) is at most`exp(2H+K)` for every spin
configuration, and equals`exp(-K)` on the`++` endpoint sector. Therefore

\[
 P_{H,K}(++)\ge\frac14e^{-2H-2K}. \tag{6}
\]

Conditional on the endpoints being`++`, the interior law in (1) is the
same as the corresponding conditional law under`mu_0`. For every
interior vertex`i`, spin reversal gives

\[
 E_0(\sigma_i\mid++)
 =\frac{E_0\sigma_i\sigma_u+E_0\sigma_i\sigma_v}{1+c}\ge0.
\]

Consequently `E(Y_int|++)>=0`. Jensen's inequality yields
`E(exp(RY_int)|++)>=1`. Multiplying by the endpoint contribution and (6)
proves (2). Condition (3) implies
`2(H+K)<=b(B_u+B_v)`, proving (4), and taking logarithms proves (5).

## 3. Consequences for the two proposed boundary repairs

For pure opposite real fields, put`K=0`. The finite field/weight band
from #1001 requires`H<=b min(B_u,B_v)`, exactly the hypothesis above.
Making the boundary fields grow, or distributing the same hard forcing
over ferromagnetically locked copies with the same aggregate observable
weights, cannot provide a bounded exterior exponential moment. In a
literal locked-copy limit the aggregate pair falls under (1); any finite
gadget that retains the same conditional-sector bounds has the same
obstruction. No claim about an arbitrary unconstrained gadget is made.

For a negative closing bond of strength`-K`, the proposed signed-edge
band budget charges

\[
 C(K)=\operatorname{atanh}\sqrt{\tanh K}.
\]

Since`sqrt(tanh K)>=tanh K`, monotonicity of`atanh` gives`C(K)>=K`.
Thus a resource constraint
`H+C(K)<=b min(B_u,B_v)` implies (3). Even if that signed-edge band
theorem is used as an input, a hard antiferromagnetic endpoint bond does
not repair the missing exterior exponential-moment estimate.
The obstruction (2) itself does not require any signed-edge zero theorem.

The domain-wall construction in COFINAL_WALL_CONSTRUCTION.md has`K=0`,
`H=2L` and`B_u=B_v=H/b`. Its sharper all-positive-state estimate retains
an additional factor`exp(2L+RA)`; the general bound here already proves
failure for every`R>b`, independently of its chosen interior architecture.

## 4. Remaining scope

A possible growth-controlled cofinal construction must avoid hard
opposite-boundary forcing of this form. A distributed field pattern that
changes the interior conditional law is outside this theorem, as are
architectures with no growing endpoint forcing. Their moment and growth
estimates still need an actual proof. This obstruction identifies a
concrete failure of a universal encoding strategy; it does not establish
an improved zero-free region.
