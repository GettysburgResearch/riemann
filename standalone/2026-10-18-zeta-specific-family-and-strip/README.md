# Ordinary-zeta families and strip-confined theta models

**Status: proposed component mathematics and explicitly labelled numerical
exploration. No new zeta zero-free boundary or RH proof is claimed.**

This packet pursues two changes of target: vary actual quadratic fields while
retaining ordinary zeta as a common factor, and allow correlated finite theta
models to have zeros in a controlled horizontal strip. Both developments are
specific enough to expose the next missing estimate or construction.

The packet is stacked on PR [#994](https://github.com/GettysburgResearch/riemann/pull/994),
at `c93ca65a510b6acaf167f929b9bf7e67d742b05a`. Its only executable inherited
proof dependency is that packet's exact theta primitive and source reconstruction.
The degree-20 continuation separately states the proposed theorem T20D as a
premise; its 305-spin root is not newly certified here.

## What this adds

| Result | Scope | What remains open |
|---|---|---|
| The mean of full inverse quadratic Dedekind coefficients is rational Möbius | Actual fields; every finite arithmetic horizon; explicit conductor error | A better bound for the retained signed mean |
| Complete critical-energy capture and signed-mean capture | Equivalent to ordinary RH with explicit polynomial conductor schedules | The all-horizon subpower upper bound |
| Full-product residual equals explicit squared bias plus nonnegative variance | Random Euler model for `Re s>1/2`; actual-family limit for fixed mollifier and `Re s>3/4` | A complete residual strictly below one in a new region |
| An explicit causal correction removes the square-alias bias | Bounded invertible cutoff operator; no rational zeta inverse in its coefficients | It does not remove the ordinary Möbius cancellation problem |
| Elementary cosine products cannot converge to the theta function on the whole plane | Unconditional deduction from Li--Radziwill's progression nonvanishing theorem | Other correlated model classes are not excluded |
| Ferromagnets with bounded external fields have a strip and a uniform entire-growth bound | All finite graphs, nonnegative couplings and observable weights | Cofinal moment matching with fixed bounds |
| An 18-spin example matches theta moments 2 and 4 and has nonreal zeros | Directed primitive reconstruction and complete finite enumeration | No higher matched order is asserted for this example |
| Continuations of the existing degree-20 model | A source-qualified local theorem; separate numerical experiments | A certified degree-22 model and an unbounded construction |

Start with [the shared-family proof](shared/PROOF.md) and
[the strip-model proof](strip/PROOF.md). The independent mathematical reviews,
finite arithmetic contracts and exact replay boundaries are in
[VALIDATION.md](VALIDATION.md).

## 1. Assessment of the current repository

The recent work has become more useful where it keeps an exact source and
identifies a complete remaining error. In particular, #994's native argument
removes small reduced denominators from every old product, pays square
denominators and a growing small-core sector, and leaves one specified rough-core
amplitude. Its theta construction reaches a concrete finite order. Those are
separate advances; the missing rough-core estimate and the unbounded theta
construction still need proofs.

The newer family results also have distinct quantifiers. A residual sum with a
positive power of family size can accommodate one exceptional member. A
capped reciprocal law at fixed moment order does not give an uncapped bound
for a prescribed member. A fixed quadratic Dedekind-RH criterion concerns both
ordinary zeta and the extra Dirichlet factor. None of these distinctions is
removed by improving finite numerical agreement.

The source and scope audit is in
[FIELD_SPECIALIZATION_AND_PROBE_AUDIT.md](audit/FIELD_SPECIALIZATION_AND_PROBE_AUDIT.md),
with an [observed repository snapshot](audit/REPOSITORY_SNAPSHOT.json).
It records the exact heads of #977, #986, #989, #994, #996, #998 and #1000.
Main was observed at `f99d9e3908dde4865377c75d9ca051c1f545bf4f`; these later
research heads were open proposals, not integrated acceptance.

### The ordinary-zeta benchmark

Liu's [current v2](https://arxiv.org/html/2610.12234v2) reports

\[
B_{\rm current}=\frac{18x+7}{18x+9}
=0.874957019420098946\ldots,
\qquad 1188x^3-2160x^2+171x+190=0,
\quad 0.38858<x<0.38859.
\]

The value `(1507-2 sqrt(921))/1653=0.874957069799...` quoted in the research
prompt is an intermediate bound retained in that version. Both are smaller
than #977's proposed all-field `271/300=0.903333...`. This is a comparison of
the stated targets. The imported papers' full analytic proofs and Lean builds
were not reconstructed in this work, and this packet does not depend on their
new zero-free conclusions.

### Dropping all number fields

For an ordinary-zeta programme, demanding every number field can impose an
unnecessary target. But fixing a small discriminant only improves constants
unless some binding scale-dependent estimate changes. Even one fixed quadratic
field still carries an additional Dirichlet-RH requirement if the goal is RH
for its whole Dedekind zeta function.

The two selected routes avoid that stronger conclusion from the beginning.
One averages actual fields to recover rational Möbius. The other works with
the original rational theta function and relaxes the location of finite-model
zeros. The audit also gives a precise limit on the proposed probe alternative:
profiles that only multiply one common principal factor cannot alter that
factor while retaining it. For genuinely different nuisance signatures, the
target projection must be nonzero and quantitatively well conditioned.

## 2. Shared-zeta quadratic families: what the average really contains

Let `u` run through odd squarefree integers in `(Q,2Q]`, let
`d_u=-8u`, and write

\[
F_u(s)=\zeta(s)L(s,\chi_{-8u}),\qquad
a_u=\mu*(\mu\chi_{-8u}),\qquad A_u(x)=\sum_{n\le x}a_u(n).
\]

Every hypothetical ordinary zeta zero is a zero of every `F_u`. No member has
been divided by the common zeta factor. With `M(x)=sum_{n<=x} mu(n)` and
`g(m)=product_{p|m} p/(p+1)`, the full finite-horizon limits are

\[
\lim_{Q\to\infty}\mathbb E_Q A_u(x)=M(x),
\]

\[
\lim_{Q\to\infty}\mathbb E_Q[A_u(x)A_u(y)]
=\sum_{\substack{m\le\min(x,y)\\m\text{ odd squarefree}}}
g(m)M(x/m)M(y/m).
\]

In the second display the index is over **positive odd squarefree** integers.
Prime 2 is always ramified in this actual family; all odd ramification remains
in the factors `g(m)`.

The proof gives quantitative errors, not just a limiting probability model.
For the critical energy

\[
E_{1/2}(B;T)=\int_1^T |B(x)|^2\frac{dx}{x^2},
\]

the mean of the individual field energies contains the ordinary energy with
coefficient one and is at most `(1+log T)` times it, up to
`O(Q^(-1/2) T^(3/2) log T)`. Taking `Q(T)>=T^(3+delta)` makes this error vanish.
Thus a subpower bound for that moving family is equivalent to the ordinary
critical-energy criterion, without requiring RH for each auxiliary factor.

Preserving the signs longer improves the sampling cost. If the field sources
are averaged **before squaring**, then

\[
E_{1/2}(\mathbb E_Q A_u-M;T)
\ll Q^{-1}T^{3/2}(\log(2T))^2.
\]

Now `Q(T)>=T^(3/2+delta)` suffices. The same family is fixed throughout each
integral, so this is control of the whole trajectory up to `T`, not a different
field choice at each evaluation point. A subpower upper bound for the signed
mean is still unproved.

### The residual has square aliases and positive variance

For the triangular inverse mollifier

\[
\mathcal M_{u,X}(s)=\sum_{mn\le X}\mu(m)\mu(n)\chi_{-8u}(n)(mn)^{-s},
\]

the full-product residual is exactly one at every common zeta zero. However,
even its first moment cannot be calculated by treating all character indices
as independent signs: squares and ramified primes survive.

The proof derives the complete limiting expression as an explicitly filtered
rational bias plus a sum of nonnegative orthogonal variance components. It
constructs a bounded invertible causal filter in the cutoff variable and an
explicit corrected mollifier whose first moment after multiplication by the
auxiliary L-factor is exactly `M_X(s)`.
The corrected coefficients are holomorphic on `Re s>1/2` and contain no
`1/zeta(s)`; they are not asserted to be constant coefficients of a Dirichlet
polynomial. The common-zero detector is preserved.

The probabilistic identities hold on `Re s>1/2`. A separate proof using an
approximate functional equation and weighted quadratic-character averages
establishes the **actual quadratic-family full-residual limit for each fixed
X on `Re s>3/4`**, away from the zeta pole. All conductor-dependent weights and
the dual sum are paid. This is an averaging domain, not a zero-free region.

The decomposition shows exactly where a gain must occur: the full bias and
variance must jointly give a residual strictly below one. Increasing the
family size removes a finite averaging error; it does not remove the retained
ordinary Möbius problem. See [shared/README.md](shared/README.md).

## 3. Strip models: an obstruction and a replacement

Write `F_theta(z)=xi(1/2+iz)/xi(1/2)`. A horizontal Fourier zero band
`|Im z|<=b` corresponds to the ordinary zeta strip
`1/2-b<=Re s<=1/2+b`. All bands here use this original coordinate. Standardizing
the theta variance changes the Fourier scale and must change the band too.

### The elementary product idea has a rigorous obstruction

Finite products of

\[
\frac{a+\cos(wz)}{a+1},\qquad a\ge0,\quad w>0,
\]

even multiplied by independent Gaussian factors, cannot converge locally
uniformly on the whole plane to `F_theta`. This statement permits arbitrary
factor counts, parameters and band widths.

The reason is structural. A zero approaching one known real theta zero must
come from an elementary factor. Positivity on the imaginary axis prevents
that factor's frequency from escaping to infinity; its zero also prevents
the frequency from collapsing to zero. A limiting factor would contribute
an entire arithmetic progression of real zeros to theta, contradicting
[Li--Radziwill, Theorem 4](https://arxiv.org/pdf/1208.2684).
This does not preclude useful finite moment matches, nor arbitrary correlated
Lee--Yang factors. It rules out the proposed independent elementary factors
as a complete approximation mechanism.

There is also a separate compactness warning with an exact example: take
`a=cosh(bw)` and let `w` grow. Every zero remains on `|Im z|=b` and every fixed
positive moment tends to zero, yet values at `iR` diverge when `R>b`.
A strip alone does not turn moment convergence into complex convergence.

### Correlated external-field ferromagnets supply the missing growth bound

Consider a finite ferromagnet with `J_ij>=0`, observable
`Y=sum_i w_i sigma_i`, `w_i>=0`, real external fields `h_i`, and characteristic
function `phi_h`. Define `V0=E_0 Y^2` in the **same graph at zero field**.
Theorems S3--S4 prove

\[
|h_i|\le b w_i\quad\Longrightarrow\quad
\phi_h(z)\ne0\ \text{when }|\Im z|>b,
\qquad
|\phi_h(z)|\le
\exp\!\left(\frac{V_0}{2}(b+|\Im z|)^2\right).
\]

The zero exclusion follows from the classical multivariate Lee--Yang theorem.
The new argument in this packet combines the zero-field product bound,
nonnegative spin correlations and a comparison of partition functions to get
the displayed entire-growth envelope. A graph involution that preserves the
couplings and observable weights while reversing the fields supplies an
exactly symmetric observable law.

Consequently, arbitrarily high theta moment matches within this class, with
the same `b` and a uniform bound on `V0`, converge locally uniformly on the
whole plane. Hurwitz transfers the zero band. At `b=1/3` the resulting target
would be `Re rho<=5/6`. The arbitrarily high-order construction is still the
missing premise. A finite matched model also has an explicit complex-disk
error bound, with the theta function itself supplying the target-side growth
term; the proof does not assume that theta is already Lee--Yang.

### A nonempty enlarged class, and a tested continuation

The 18-spin example has 16 independent symmetric spins and one ferromagnetic
dimer with opposite fields. Exact algebra matches the original theta moments
2 and 4. A fresh directed theta-source replay proves positive weights, field
cap below `1/3`, reference variance below `1/20`, and genuinely nonreal Fourier
zeros at heights strictly between `0.30` and `0.31`.
This is a low-order demonstration of the enlarged class, not an improvement
on #994's finite degree-20 result.

Assuming #994's proposed T20D theorem and its invertible active Jacobian,
opposite sufficiently small fields on two identical leaves can be retuned to
preserve the first 20 moments by the implicit-function theorem. Separately,
the [numerical exploration](strip/EXPERIMENT.md) tests finite continuations
toward the physical band `1/3`, recording the degree-22 discrepancy and any
failed continuation. Those ordinary high-precision computations are not
directed root certificates or cofinal existence proofs.

## 4. Reproduction and next mathematical targets

From the repository root:

```sh
python standalone/2026-10-18-zeta-specific-family-and-strip/verify_packet.py --replay
```

This authenticates the manifest, runs the two finite checkers with optimized
Python, and checks that the generated artifacts reproduce their committed
hashes. The scientific proofs and the empirical higher-order experiments have
separate scopes, documented in [VALIDATION.md](VALIDATION.md).

The next targets are concrete. For the shared family, estimate the complete
signed mean or the complete bias-plus-variance residual with growing horizon;
the finite-X actual-family limit alone cannot be interchanged with an
uncontrolled growing mollifier. For the strip class, build a graph architecture
with effective field freedom on the important observable components, then
certify a higher-order root and eventually prove cofinal feasibility with a
uniform reference variance. A new graph and a new signed estimate are
mathematical work; a denser ladder of the same finite checks does not replace
either.
