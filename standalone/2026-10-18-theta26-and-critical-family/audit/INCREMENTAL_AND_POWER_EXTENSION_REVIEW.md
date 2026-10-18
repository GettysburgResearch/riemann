# Independent review of incremental endpoints and power-sum extensions

Reviewer: `/root/field_audit`, independently of the parameter search and
authoring agent. Review date: 2026-10-18.

**Verdict: PASS at the exact identities below.** The two directed endpoint
certificates establish the stated finite existence results. The companion's
moving-anchor identities, quantitative extension lemma, collision coordinates,
strip-preserving normality barrier, and conditional all-order consumers pass
analytic review. No substantive mathematical defect was found.

The certified results are endpoints with 84 factors matching through order 24
and 104 factors matching through order 26. The numerical producer follows a
64/order-22 to 84/order-24 to 104/order-26 chain. Its paths are not certified:
the exact roots supplied by the endpoint certificates are not asserted to be
connected by those same numerical trajectories. Neither two successful
extension steps nor the conditional consumers establish cofinal feasibility,
RH, or a new zero-free strip.

This is an independent agent review within the research session, not an
external referee report, a formal proof-assistant check, or a second
implementation of transcendental interval arithmetic.

## 1. Exact reviewed identity

Paths are relative to this research packet. SHA-256 hashes:

| File | SHA-256 |
|---|---|
| `theta/PROOF_INCREMENTAL.md` | `194e14b421df650d44daab6b1cf9a099ef5383f1f654b1d029652a12896ca148` |
| `theta/check_incremental.py` | `c3ad5b30c43707248499eca83c32e9c4ffe8449ceb4aac7a994f81e3d9d0f10d` |
| `theta/incremental_parameters.json` | `b124d0b05780c57c3f753732e02b7b6a21ada63170c3f6f3961fa9c74551bc77` |
| `theta/incremental_certificate.json` | `8e90e9b681e5e12015eb9d5edaec4957c1e1fd0d36dcd3eae5b6543622ec5599` |
| `theta/extension/POWER_SUM_EXTENSION.md` | `73367329eb9389cd33686b1fc25738945e14319998140838c8ba408f9ea96f9f` |
| `theta/extension/check_power_extension.py` | `8bd2281586a80f3171aabd63d2da7cd516f1f9433e84ee6ba5c77f73553cbb75` |
| `theta/extension/power_extension_certificate.json` | `8e34bd2ab464adf01fc5ca3f42d412df0ab0c84382d628b570921c77a0d50697` |

The following shared mathematical dependencies are also bound:

| Dependency | SHA-256 |
|---|---|
| `theta/check_gaussian.py` | `711f4edc1bbb262001dd87c0cf60396d5e194b32c47c42f9d7a76ee4239012aa` |
| `theta/source26.py` | `2e609acb85dc39b4a3571cb91e20f2e00dabec5ea36c1de9a50dcbcea280d7ec` |
| `theta/theta26_source.json` | `c171903e4f60c189a929ccfcce36f7db034508e9ca10c85ed766338625558dcf` |
| Inherited `pr886_primitive.py` | `2eba75b7fc82617342c20f6a06270462b6d82f1e7162f66847c029e7e5a9fa55` |

The primitive's authenticated Git blob is
`c32015f110d10186538ffabcb4689ba5bbc060d0`. Its source is the pinned prior
theta packet at commit `c93ca65a510b6acaf167f929b9bf7e67d742b05a`.

The complete-source reconstruction and generic checker have a separate
independent review in [THETA_GAUSSIAN_AUDIT.md](THETA_GAUSSIAN_AUDIT.md).
This incremental review read that audit and inspected `check_model` directly.
It authenticated and used the same complete source during its own endpoint
replays; it did not repeat the full integration or claim a new arithmetic
backend. Changes to a bound mathematical file require a new review identity.

## 2. Endpoint equations, complete domains, and positivity

For a variance-one target `H`, the logarithmic coefficient calculation gives

\[
\sum_j b_j^r=(-1)^{r+1}\frac{r\kappa_{2r}}{(2r)!},
\qquad 2\le r\le M,
\qquad a=\frac12-\sum_j b_j.
\]

Thus these equations match all Taylor coefficients through degree `2M`.
The constant, quadratic, and odd coefficients are already exact. The new
models retain 20 identical fixed final nodes. The wrapper explicitly checks
their equality and requires every active coordinate to be an old node.
The generic checker additionally checks valid distinct active indices,
complete model dimensions, and a positive exact rational cube radius.

For the 84-node endpoint, the 11 active indices agree with the proof. For the
104-node endpoint, the 12 active indices agree with the proof. All inactive
nodes, including each endpoint's cloud of 20 equal nodes, stay fixed at their
exact rational centers. Directed rational coercion enlarges the active cube
outward; it does not turn a center calculation into a whole-cube claim.

Every node occurs in each power sum. Every active derivative occurs in the
whole-cube Jacobian. The actual theta target is enclosed by the authenticated
complete moment source and the directed cumulant calculation. The preconditioner
is a specified rational matrix whose action is recomputed by the checker;
the numerical QR and Newton procedures used to produce it are not acceptance
premises.

The exact bounds verify

\[
\|Rf(y_0)\|_\infty\le\beta,\qquad
\sup_B\|I-RDf(y)\|_\infty\le L<1,
\qquad \beta+L\rho<\rho,
\qquad \rho=10^{-50}.
\]

Consequently `y-Rf(y)` contracts the full closed cube strictly into itself.
The same derivative bound makes `R Df(y_0)` invertible, hence makes the square
matrix `R` invertible. Its fixed point therefore solves the actual equations.
Uniqueness is restricted to that active cube with the remaining nodes fixed.

I separately checked that the proof's displayed decimal bounds are upward
bounds for the exact receipt:

| Endpoint | Bound for beta | Bound for L |
|---|---:|---:|
| 84 nodes / order 24 | `4.499e-90` | `1.749e-36` |
| 104 nodes / order 26 | `1.231e-87` | `9.236e-35` |

Both complete cubes have strictly positive nodes and Gaussian parameter.
Their smallest nodes exceed `0.0002990` and `0.0002826`, respectively;
their Gaussian parameters exceed `0.0652` and `0.0577`. These weaker decimal
bounds summarize strict directed inequalities, not numerical tolerances used
by the accepting code.

The only zeros are the real points `+/-1/sqrt(b_j)`, with multiplicities.
The identity `a+sum b_j=1/2` gives the whole-plane envelope
`exp(abs(z)^2/2)`. The polynomial degrees are 168 and 208; 24 and 26 are the
matched Taylor orders. The physical approximants are `P(sqrt(v_theta) z)`.
None of these conclusions needs a positive inverse Fourier density.

## 3. Producer provenance and what it does not establish

The selected parameter records bind the two curated producer files:

| Producer record | SHA-256 |
|---|---|
| `theta/extension/power_extension_candidates.json` | `45ef1c6cfc0db513b1d5be9246494aaa99695d66219257a7486d0252cf6e024f` |
| `theta/extension/power_extension26_candidates.json` | `726bdf8fdb387322bc72fee372716406b7cc81581389c454b482424574b2cce6` |

The first selected record declares a 64-node, order-22 input, 20 added equal
nodes, an 84-node order-24 endpoint, and 35 anchor changes. The second
curated file identifies the first file as its input and declares an 84-node,
order-24 starting point, 20 added equal nodes, a 104-node order-26 endpoint,
and 20 anchor changes. This supports the stated provenance as a two-step
numerical construction, rather than two separately initialized endpoint fits.

The proof correctly says that the second search starts from the numerical
84-node center. A nearby exact order-24 solution is not silently substituted
for that input. I did not certify the paths, rerun their numerical optimizers,
or review the unused 88-, 96-, or 148-node alternatives as existence proofs.
None of their residuals is used in the two endpoint acceptance checks.

## 4. Moving anchors and the quantitative extension lemma

The Jacobian of powers 2 through `m+1` in `m` distinct positive anchors is
a nonzero diagonal multiple of a Vandermonde matrix. The implicit-function
initialization at cloud node zero is therefore valid. Differentiating the
constraints and applying Lagrange interpolation gives exactly

\[
\beta_i'(x)=-\frac{Lx}{\beta_i(x)}\ell_i(x).
\]

The interpolation error for the next monomial gives the claimed next-power
derivative, and the interpolation identity for the reciprocal anchor gives
the Gaussian-reserve derivative:

\[
A'(x)=L(m+2)x\prod_i(x-\beta_i(x)),\qquad
a'(x)=-L\prod_i(1-x/\beta_i(x)).
\]

In the stated region `0<x<min beta_i`, these have the claimed parity sign,
reserve bounds, and ratio. Multiplicity `L` remains an integer; the flow
does not introduce fractional powers into a finite entire product.

The sufficient radius estimate correctly controls the whole chart. The
chosen delta box keeps all old anchors positive and pairwise separated.
For `x<=tau`, the interpolation numerators and denominators give precisely
the bounds `K_i` in (P15). Integrating the resulting derivative bound rules
out a first exit from the box. The vector field remains smooth on a compact
neighborhood, so no other finite-time continuation failure occurs before
tau. The lower bound on each factor `beta_i-x` gives (P17). Strict
monotonicity then proves the unique filling of every deficit in (P18).

These are conditional acceptance tests for a chosen starting model and chart.
Failure of the inequalities proves neither nonexistence nor inability of
another choice of anchors to continue. The proof keeps this distinction.

## 5. Collision coordinates and the physical strip budget

The pair power formula for `b_+/-=u+/-sqrt(d)` is a real polynomial in `(u,d)`
for every integer power. At `d=0`, dividing rows by their power indices and
performing the stated column subtraction gives the standard confluent
Vandermonde matrix. Its complete prefactor is
`2u^2 product(r) product(gamma_j)`, and the remaining differences are those
in (P21). The determinant is nonzero under the stated separation hypotheses.
This supplies an analytic local chart through the collision. The next-power
formula extends by its polynomial identity and continuity.

For a conjugate pair, the exact inverse-square zero calculation gives

\[
|\Im z_{\rm std}|^2=\frac{|b|-\Re b}{2|b|^2},\qquad
|\Im z_{\rm phys}|^2=\frac{|b|-\Re b}{2v|b|^2}.
\]

The direction of the variance rescaling is correct. Squaring the alternative
strip inequality is legitimate because its right side is positive when
`u>0`. The pair's absolute-square excess over its signed second power is
exactly four times the square of its imaginary part.

Summing these excesses gives (P25) with the stated constant `4 sqrt(2)`.
Starting from real nodes fixes the initial value `T=q`. The strict inequality
at a proposed barrier `R` prevents a first crossing by continuity. It remains
valid when zero nodes are added or the same pair is described in different
collision coordinates, provided `T` stays continuous.

The directed source bounds and exact rational arithmetic verify the theta
barrier `R=7/400` for physical half-width `1/3`. The resulting quartic
whole-plane envelope is correct. It is conditional on a continuous path
that preserves the strip and the second power; the barrier does not construct
such a path or imply that the numerical paths preserve it exactly.

## 6. The all-order consumers and finite positivity limitation

The canonical-factor inequality (P5) is valid for every complex argument,
including its zero. It gives the quartic envelope from `sum |b_j|^2`, without
requiring the Gaussian coefficient to remain positive. For real positive
nodes that sum is the already matched `q_2`. Cofinal exact matching therefore
gives normality, coefficient identification, and whole-plane local uniform
convergence. Hurwitz supplies real-zero confinement. The complex-pair version
uses the same argument once the independent path/barrier hypotheses supply
a common bound and strip. Neither is a cofinal construction theorem.

I independently fetched the cited primary paper
[Zagorodnyuk, Theorem 2](https://nyjm.albany.edu/j/2012/18-27p.pdf), on printed
page 485. Its scalar specialization supplies a Stieltjes measure under both
families of positive-semidefinite Hankel conditions, including degenerate
cases. This imported moment-existence theorem is used with the right
quantifier: every finite matrix order, not a bounded set of checked orders.

For the entire even target, `H(z)=F(z^2)` defines an entire `F` with `F(0)=1`.
The logarithmic-derivative coefficients have an exponential Cauchy bound.
Positivity of the representing measure therefore forces compact support.
The resulting integral expression for `-F'/F` is holomorphic on the stated
slit domain and agrees there by meromorphic identity. An off-slit zero of `F`
would produce a pole, which is impossible. The zero-support case is also
handled. This proves the conditional Stieltjes consumer without asserting
that a fractional finite product is entire.

The positive-weight counterexample is correct. Its displayed moments follow
from half the uniform probability law on the given interval, and violate
the necessary unit-node inequality `p_3<=p_2^(3/2)`. All finite Hankel
quadratic forms remain strictly positive because the density is positive on
an interval. The weight-nullspace argument also allows either sign of the
next-power change while fixing the older powers. Thus finite positivity
alone does not supply either a unit-multiplicity representation or the
particular sign needed by the one-sided root-flow lemma.

The historical Grommer discussion and equal-weight quadrature comparison are
context, not additional imported existence premises. The separate weighted
canonical note has its own review; this review does not replace it.

## 7. Independent ordinary and optimized replays

From the research packet root I ran both checkers in ordinary and optimized
Python, directing output to separate audit files:

```text
python theta/check_incremental.py --source /path/to/pinned/theta --output audit/incremental_replay.json
python -O theta/check_incremental.py --source /path/to/pinned/theta --output audit/incremental_optimized_replay.json
python theta/extension/check_power_extension.py --output audit/power_extension_replay.json
python -O theta/extension/check_power_extension.py --output audit/power_extension_optimized_replay.json
```

Both incremental receipts are byte-for-byte identical to the shipped receipt
at `8e90e9b681e5e12015eb9d5edaec4957c1e1fd0d36dcd3eae5b6543622ec5599`.
Both final power-extension receipts are byte-for-byte identical to the shipped
receipt at `8e34bd2ab464adf01fc5ca3f42d412df0ab0c84382d628b570921c77a0d50697`.
An earlier power replay preceded the final experiment-prose freeze and
differed only in its embedded proof hash; the final replays resolve that
provenance difference. No source or mathematical file was changed by this
review.

The power checker covers 24 explicit rational charts (`m=1,...,12` and
`L=1,4`), 11 confluent determinant fixtures, complete pair powers through
degree 26 for positive, zero, and negative collision coordinates, the
physical-strip conversion, the finite positivity counterexample, and the
strict rational theta barrier. Its polynomial interpolation fixtures check
complete polynomial identities on those charts, rather than sampling values
of the interpolation variable. The general theorems still rest on the
analytic and algebraic proofs reviewed above.

Both checkers use explicit exception guards that remain active with `-O`.
The new endpoint wrapper introduces no numerical optimizer dependency into
acceptance. The exact power checker uses rational arithmetic and its pinned
source bounds; it does not claim to certify a theta endpoint or cofinal
feasibility. The distinction between these two finite-check scopes is correct.

The positive verdict applies to the finite endpoints, stated component
deductions, and exact receipts at the bound identities. It does not certify
the search trajectories, promote the imported moment theorem to a new result,
or supply the missing all-order feasibility argument.
