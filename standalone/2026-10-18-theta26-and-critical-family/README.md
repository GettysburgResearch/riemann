# Theta approximants through order 26 and actual quadratic families above the critical line

**Proposed research components with complete proofs, directed finite
certificates, and separate mathematical reviews. No new global zeta
zero-free boundary or RH resolution is established.**

This continuation specializes the target to ordinary zeta. It develops two
main routes: construction of functions that retain global control of their
zeros, and quantitative estimates for actual quadratic fields sharing the
ordinary zeta factor. A third component allows controlled negative Ising
couplings. The work includes successful finite constructions and a precise
counterexample to one insufficient arithmetic strategy.

The packet is stacked on frozen PR #1001 at
`f6beb3774ae7ff5eca4cb046786eae10e4f88abc`. Its source dependencies include
PR #994 at `c93ca65a510b6acaf167f929b9bf7e67d742b05a`. Earlier packets remain
historical dependencies; their mathematical status is not promoted here.

## What was achieved

| Route | Established component | Remaining condition for a zeta conclusion |
|---|---|---|
| Real-zero entire functions | Complete-source, directed existence certificates matching the actual theta Taylor coefficients through orders 22, 24, and 26. | A construction at unbounded matched orders. |
| Incremental root construction | Exact moving-root identities, a quantitative extension lemma, and a nonsingular chart through a pair collision. Separate directed certificates establish the 84-factor order-24 and 104-factor order-26 endpoints discovered by two successive extensions. | Control of a continuing sequence, not merely the finite endpoints. |
| Positive weighted moments | A complete half-plane convergence theorem permits arbitrary positive weights, unbounded node supports, and any real Gaussian parameter. | Positive weighted feasibility for the actual theta cumulants at unbounded orders. |
| Actual quadratic fields | A full-L mean-square tail estimate throughout every fixed compact subset of `1/2<Re(s)<1`, growing-mollifier residual transfer, and constructive removal of auxiliary local variance. | A strict bound on the retained ordinary scalar `abs(zeta(s)*M(s)-1)`. |
| Rational Newton input | The complete frequency tail above `Y^(84/71)` has subpower squared norm, with an exact consumer on the strict physical square step. | An arithmetic upper bound for the retained lower frequencies. |
| Controlled negative Ising interactions | Explicit local budgets imply a global Fourier zero strip, with a positive-reference growth bound and a continuous variance barrier. | Cofinal theta matching within the prescribed strip budget. |

The finite Taylor orders above are not polynomial degrees or verified zero
heights. The original models use 64, 128, and 128 quadratic factors, so their
polynomial factors have degrees 128, 256, and 256.

## 1. A concrete advance in the theta construction

Let

\[
 F_\theta(z)=\frac{\xi(1/2+iz)}{\xi(1/2)},\qquad
 v_\theta=0.04620998623083794\ldots,
 \qquad H(z)=F_\theta(z/\sqrt{v_\theta}).
\]

The target H has variance one. The directed certificates prove existence of

\[
 P(z)=e^{-az^2}\prod_{j=1}^{N}(1-b_jz^2),\qquad
 b_j>0,\quad a>0,\quad a+\sum_jb_j=\tfrac12,
\]

with `P-H=O(z^(2M+2))` for `M=11,12,13`. All zeros are real because each
factor has exactly the roots `+/-1/sqrt(b_j)`. This is a global zero
statement for each finite approximant, supplied by its construction.

| Matched Taylor order | Quadratic factors | Full-cube contraction upper bound |
|---|---:|---:|
| 22 | 64 | `2.320e-38` |
| 24 | 128 | `5.857e-37` |
| 26 | 128 | `8.859e-35` |

The proof uses a closed rational parameter cube of radius `10^-50` and
directed arithmetic on the entire cube. Every target moment comes from a
fresh integration of the complete theta density: 512 fractional bits,
Taylor degree 220, 162 cells, eleven explicit theta indices, and complete
time, index, and Taylor remainders. Numerical zeta-zero entries were used
only to initialize the search; the checker does not load or trust them.

Read [the finite existence proof](theta/PROOF_GAUSSIAN.md),
[the complete source proof](theta/SOURCE26.md), and
[the independent review](audit/THETA_GAUSSIAN_AUDIT.md).
The more economical endpoints found by actual incremental searches are
documented separately in [PROOF_INCREMENTAL.md](theta/PROOF_INCREMENTAL.md).
Their endpoint certificates do not certify every intermediate point of the
numerical paths.

| Successive discovery step | New endpoint | Directed contraction upper bound |
|---|---|---:|
| Add 20 factors to the 64-factor order-22 model | 84 factors, order 24 | `1.749e-36` |
| Add 20 factors to that order-24 model | 104 factors, order 26 | `9.236e-35` |

In each endpoint certificate, the 20 newly appended equal factors remain
fixed while selected old coordinates vary in the full rational cube.

### Two unnecessary restrictions can be removed

Canonical factors give the identity and inequality

\[
 P(z)=e^{-z^2/2}\prod_j[(1-b_jz^2)e^{b_jz^2}],\qquad
 |(1-w)e^w|\le e^{|w|^2/2}.
\]

For real nodes, matching the fourth coefficient already fixes
`sum b_j^2=Q_2`, so

\[
 |P(z)|\le\exp\left(\frac{|z|^2}{2}
                         +\frac{Q_2|z|^4}{2}\right).
\]

This bound is uniform in the number of factors and the sign or size of a.
Thus the all-order consumer does not require a positive Gaussian reserve
or a positive inverse Fourier density.

A stronger [weighted half-plane theorem](theta/WEIGHTED_CANONICAL.md)
also removes integer multiplicities. It suffices, for unbounded M, to find
finite positive weights and nodes satisfying

\[
 \sum_j\lambda_{M,j}b_{M,j}^{\,r}=Q_r,
 \qquad 2\le r\le M,
 \qquad
 Q_r=\frac{(-1)^{r+1}r\kappa_{2r}(T/\sqrt{v_\theta})}{(2r)!}.
\]

Fractional canonical factors are holomorphic and nonvanishing on each
open half-plane. The same quartic bound gives normality there, and a
global logarithm remainder identifies the limit on a small imaginary
interval even when supports are unbounded. Hurwitz then supplies the
conditional RH implication. The proof explicitly handles the real
boundary branch points; it does not call those fractional products entire.

This turns the remaining construction into a positive weighted moment
problem. All-order feasibility remains unproved. The related classical
Stieltjes/Hankel criterion and the limitations of finite positivity tests
are recorded in the extension proof, without a priority claim.

### Extending a model and passing a collision

The [power-sum extension proof](theta/extension/POWER_SUM_EXTENSION.md)
adds L equal roots x and retunes m selected old nodes beta_i while
preserving the old matched powers. Its exact next-power derivative is

\[
 A'(x)=L(m+2)x\prod_{i=1}^m(x-\beta_i(x)).
\]

The proof gives a positive, explicit continuation radius and guaranteed
gain for any specified separated chart. It also replaces a colliding pair
by its elementary symmetric coordinates, where the Jacobian becomes a
nonsingular confluent Vandermonde matrix. Continuing into a conjugate pair
has an exact physical Fourier-strip cost.

For paths from real-node models that retain the physical strip
`abs(Im z)<=1/3`, preserve the fourth coefficient, and keep all other
real nodes positive, a simple barrier gives

\[
 \sum_j|b_j|^2<\frac7{400}.
\]

This automatically supplies a common quartic growth envelope along such
paths. An unbounded sequence of exact theta matches satisfying these
conditions would imply the boundary 5/6. Neither the barrier nor the
finite experiments establishes that sequence.

## 2. Quantitative estimates for the actual shared-factor family

Use every primitive quadratic character of discriminant `-8u`, with u
odd and squarefree in `(Q,2Q]`. On each fixed complex compact set in
`1/2<Re(s)<1`, the [arithmetic proof](arithmetic/PROOF.md) establishes

\[
 \mathbb E_Q\left|L(s,\chi_{-8u})-
                  \sum_{n\le K}\chi_{-8u}(n)n^{-s}\right|^2
 \ll_\varepsilon Q^\varepsilon K^{1-2\Re s},
 \qquad 1\le K\le Q.
\]

The proof uses Heath-Brown's quadratic large sieve and an exact
flat-cutoff functional equation. It retains all square parts, their
ramification masks, the full dual sum, and row-dependent weights. No
exceptional member is removed. Fixed local sign and ramification
conditions of positive density are also permitted.

The earlier actual full-L adapter applied above `3/4` for fixed mollifier
length. The new estimate reaches every fixed real part above `1/2` and
pays explicit growing lengths. For triangular inverse-Dedekind mollifiers
of horizon `X<=Q^eta`, sufficient strict ranges include:

| Real part | Root-residual comparison | Absolute squared-residual comparison |
|---|---:|---:|
| `3/4` | `eta<1/4` | `eta<1/6` |
| `5/6` | `eta<2/5` | `eta<3/10` |

These fractions are domains and length exponents for family estimates;
they are not zero-free regions.

An exact finite-state least-squares calculation optimizes over every
function of finitely many local quadratic states with a prescribed mean.
Its explicit finite Euler inverse removes the auxiliary variance. The
estimate transfers to actual families with a growing prime cutoff
`y=(log Q)^nu`, where `0<nu<1/(5/4-sigma_0)` and sigma_0 is the minimum
real part of the fixed compact set. In particular, `nu=1` is permitted
throughout the stated domain. The proof pays coefficient masses even when
the primorial support is very large. The normalized full-product residual
has the limit

\[
 \lim_{Q\to\infty}\mathbb E_Q
 \left|\zeta(s)L(s,\chi_{-8u})M_Z(s)
          \frac{\prod_{3\le p\le y}(1-\chi_{-8u}(p)p^{-s})}{C_y(s)}-1\right|^2
       =|\zeta(s)M_Z(s)-1|^2,
\]

where Z is fixed and C_y is an explicit nonzero absolutely convergent
auxiliary Euler product. It contains no inverse zeta factor. At a
hypothetical zeta zero, both sides remain exactly one. This is a proved
removal of auxiliary fluctuation, with the ordinary arithmetic gap still
visible. See [the arithmetic review](audit/ARITHMETIC_AUDIT.md).

## 3. A paid frequency sector and a sharper account of what it cannot do

For the literal rational Möbius prefix,
`G_Y(s)=sum_(n<=Y) mu(n)n^(-s)`, the
[native frequency-tail proof](arithmetic/NATIVE_FREQUENCY_TAIL.md) gives

\[
 \int_{|t|>T}\left|
 \frac{\zeta(1/2+it)G_Y(1/2+it)^2}{-1/2+it}
 \right|^2dt
 \ll_\varepsilon (YT)^\varepsilon T^{-71/42}(T+Y^2).
\]

Thus the complete input tail above `Y^(84/71)` has subpower squared norm.
The proof transfers this bound to the strict physical square step by
Plancherel and a root-norm comparison, retaining every mixed term.
Frequency projection and physical restriction are applied in their
correct order.

The [low-frequency attack](arithmetic/LOW_FREQUENCY_ATTACK.md) proves
that certain further spectral information is still insufficient. It
constructs bounded squarefree-supported coefficients, with first
coefficient one and both smooth balance coordinates exactly zero, whose
old energy is comparable to `Y^kappa` but whose retained output energy
is comparable to `Y^(2*kappa)`. The result retains the actual zeta
multiplier and the full physical window, for every growing frequency
cutoff. A causal `n=1` impulse explicitly preserves a nonzero component.

These constructed coefficients do not obey Möbius inversion. The result
therefore identifies the arithmetic condition that the next successful
estimate must exploit; it does not rule out a contraction for the actual
Möbius source. In particular, the suggested exponents `p=3/2, a=1/3`
cannot follow from just the larger coefficient class used by that proof.
See [its independent review](audit/LOW_FREQUENCY_AUDIT.md).

## 4. Negative Ising couplings with a paid global strip

The [negative-coupling theorem](analytic/NEGATIVE_COUPLING_STRIP.md)
allows arbitrary finite graphs with real couplings. For every negative
edge e={i,j}, allocate nonnegative endpoint costs alpha_(e,i), alpha_(e,j)
satisfying

\[
 \tanh\alpha_{e,i}\tanh\alpha_{e,j}\ge\tanh|J_e|,
 \qquad
 |h_i|+\sum_{e\ni i,\ J_e<0}\alpha_{e,i}\le b w_i.
\]

Then every zero of the complete weighted Fourier partition function is
in `abs(Im z)<=b`. An elementary disk version of the classical
Asano--Ruelle contraction is proved directly, and full incidence
contraction recovers every physical spin configuration.

The same budget controls the cost of all negative interactions relative
to the graph with negative edges removed and fields set to zero. If its
observable variance is V_+, the actual second moment satisfies
`v>=V_+ exp(-b^2 V_+)`, together with an explicit entire growth bound.
At physical b=1/3, a continuous fixed-theta-variance path from a
ferromagnet cannot cross `V_+=0.04646`. This permits negative couplings
without inserting an unproved compactness assumption. No theta-matching
negative-coupling model or cofinal construction is certified here.

## Research assessment

Ordinary zeta should remain the target. Requiring a theorem for every
number field adds obligations; even RH for one quadratic Dedekind zeta
also asks for RH of its nonprincipal Dirichlet factor. The entire-function
route here directly targets ordinary xi, and the arithmetic route uses
auxiliary fields while retaining the rational source explicitly.

The important remaining task in either route is an upper estimate or
an unbounded construction. A new family identity, a finite moment fit,
a better condition number, or an improved frequency cutoff is valuable
only with its precise consumer and remaining condition stated. This
packet makes progress on those consumers and on actual finite existence,
and records where a promising generic estimate fails.

Concurrent PR #1002 at `1319373815ee408146705b25a426fba6b22ed755` was
observed during final preparation. Its overview records complementary
paired probes, an adaptive core allowance, strip compactness, and a
determinant comparison. Those proposals are not inputs to this packet.
The present complete full-L estimates, frequency-tail consumer,
low-frequency counterexample, directed theta certificates, and relaxed
canonical-factor consumers have their own proofs and source identities.

## Reproduction and review

From a checkout containing the pinned dependency packet:

```bash
python standalone/2026-10-18-theta26-and-critical-family/verify_packet.py --replay
```

The verifier checks the complete manifest and reproduces all declared
finite receipts in ordinary and optimized Python, including a fresh
complete theta integration. It uses temporary outputs and leaves the
frozen receipt files intact. The accepting checkers use the Python
standard library; exploratory parameter searches may use NumPy and SciPy.

The independent reviews are by separate research agents in the same
session, not external human referees or a formal proof assistant. The
directed interval backend is inherited and authenticated; replay with
that backend is not a second arithmetic implementation. See
[VALIDATION.md](VALIDATION.md) for exact proof, source, replay, and
publication boundaries.
