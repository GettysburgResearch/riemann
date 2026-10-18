# Native amplitude control, connected theta degree 18, and an all-order budget limit

Status: **proposed research components with written proofs and reproducible
finite certificates. RH remains open.** The mathematical review is by separate
agents and the coordinating reviewer within one AI session; it is not external
referee acceptance or a proof-assistant verification.

This packet continues [PR #974](https://github.com/GettysburgResearch/riemann/pull/974)
at `89c37b6707cb77fc5a86143ea98d8756759fdcbc`. It adds three results that change
the next research decisions. It does not propose another global zero-free
fraction. The source and overlap cutoff is 17 October 2026, 23:56 UTC; the
last inspected PR is #978. Exact source heads and review limits are in
[SOURCES.md](SOURCES.md).

| Track | Result in this packet | Remaining proof obligation |
| --- | --- | --- |
| Theta law / Lee–Yang | An actual connected 281-spin ferromagnet matches the original theta moments exactly through degree 18. | A construction reaching unbounded orders, with the required convergence; this model misses degree 20. |
| Native Newton energy | A complete range of products inside the native amplitude can be removed with a negative-power squared error. | Control of the explicit balances and the remaining high-product amplitude in terms of the old native energy. |
| Contour / character moments | An exact `100/111` floor for the specified retained-Type-II and separate-moment budget, allowing every fixed moment order and asymmetric scales. | Improve the literal Type-II sum, exploit zero-selection in a coupled estimate, or prove a signed physical estimate. |

## 1. The degree-18 finite target is now reached

[Theorem T18C](lee_yang/PROOF.md) constructs a zero-field Ising tree with
281 vertices and 280 strictly positive couplings. It has a hub, 266 leaves
in two weight groups, and a 14-spin chain. All 280 observed spins have positive
weights; the auxiliary hub has weight zero. The first chain edge has

\[
\tanh J=0.22713565209564776,
\]

an exact rational parameter. The other twelve chain edges have correlation
`1/100000000`; they remain present in the model and in every calculation.
The first two weighted chain spins have covariance strictly between `1/60`
and `17/1000`. Thus the construction retains a substantial correlation as
well as the weak edges that make the full graph connected.

Let \(T_*\) be the original theta-law variable standardized to variance one.
The theorem proves the existence of an observable \(Y\) for which

\[
\mathbb E Y^{2r}=\mathbb E T_*^{2r}\qquad(1\le r\le9).
\]

All odd moments vanish by spin-flip symmetry. Every coupling satisfies
\(10^{-9}<J_e<1/4\), and the support of \(Y\) lies in \((-10,10)\).
The finite weighted Lee–Yang theorem gives an entire characteristic function
with only real zeros. Rescaling the observable by the square root of the
original theta variance restores the unstandardized moments and leaves the
Ising couplings fixed.

The exact target is certified through a contraction on nine active weights,
with all other parameters fixed. In a rational cube of radius \(10^{-30}\),
the complete source residual after applying the exact center inverse is
less than \(2.843\times10^{-41}\), and the contraction constant is less than
\(4.312\times10^{-12}\). The proof encloses the actual theta constants,
including all integration and omitted-index tails. It therefore proves an
exact nearby root, rather than accepting a high-precision solver output.

There is also an exact independent probability-transfer calculation of the
whole 281-spin model at the rational center, through raw moment 20. It agrees with the author's
cumulant construction and is accompanied by a complete 128-configuration
small-graph enumeration. See [the graph check](check_chain_transfer.py)
and [its report](CHAIN_TRANSFER_CHECKS.json).

The next discrepancy is explicitly certified:

\[
0.450<\mathbb E Y^{20}-\mathbb E T_*^{20}<0.451.
\]

This closes the specific degree-18 target left open in #974. It does not
produce a degree-20 realization, a path from the old degree-16 root, or an
extension rule for arbitrary order. The weak edge scale and the inverse
Jacobian in this one finite construction carry no uniform-in-order claim.

## 2. Newton: a bound inside the amplitude

Put \(m(k)=\sum_{n\le k}\mu(n)/n\), \(b=Y+1\), and
\(z_Y=(\mu\mathbf1_{n\le Y})*(\mu\mathbf1_{n\le Y})\).
The strict native inverse identity reconstructs every output
\(b\le k<b^2\) from the old prefix. After subtracting the exact logarithmic
part of the harmonic kernel, retain the two finite balance coordinates

\[
M_Y=m(Y),\qquad
B_Y=1+\sum_{n\le Y}\frac{\mu(n)\log n}{n}
       -(\log Y+\gamma/2)M_Y.
\]

On each dyadic output annulus \(k\asymp X\), let
\(D=\lfloor X^\rho\rfloor\), where \(1/2<\rho<2/3\), and retain only
products \(d>D\) in the renormalized oscillatory kernel. The resulting
explicit old-prefix quadratic amplitude is denoted \(P_{Y,\rho}(k)\).
[The Newton theorem](newton/PROOF.md) proves

\[
\sum_{Y<k<(Y+1)^2}|m(k)-P_{Y,\rho}(k)|^2
 \ll_\rho Y^{-(2-3\rho)}(1+\log Y)^8.
\]

For \(\rho=5/8\), this is \(O(Y^{-1/8}(1+\log Y)^8)\).
On the last annulus, the removed product threshold is of order \(Y^{5/4}\).
In particular, all ordered pairs of old-prefix indices with one index up
to a constant times \(Y^{1/4}\) belong to that controlled sector.

The elementary pointwise harmonic bound would give squared error of size
\(D^2(1+\log D)^2/X\), which is power-small only below \(D=X^{1/2}\).
The new proof permits every fixed exponent below \(2/3\) by keeping the
complete rational-frequency covariance. Equal reduced frequencies are
grouped before applying their spacing estimate, and the sawtooth's
nonzero discrete mean is retained.

This is a bound on part of the actual amplitude. The #974 theorem bounded
variation around block means. Both results combine by contraction of
orthogonal projection: for the original coarse energy \(S_Y\) and the
filtered coarse energy \(S_Y^{\rm high}\),

\[
\big|\sqrt{S_Y}-\sqrt{S_Y^{\rm high}}\big|
 \le \sqrt{E_Y},
\]

where \(E_Y\) is the complete error above. The mixed term in energy is
not discarded. Products larger than the current output index also remain
in the renormalized formula, because they cancel part of its logarithmic
balances.

The kernel estimate works for arbitrary coefficients bounded by the divisor
function. Its gain is periodic-kernel cancellation, not a new theorem about
Möbius signs. The actual Möbius inverse identity identifies the amplitude
being approximated. A saving in the remaining high-product quadratic form
is still required for the native energy recurrence leading toward RH.

## 3. What higher moments cannot fix by themselves

[The all-order analysis](critical/ALL_ORDER_BARRIER.md) allows every fixed
numerator and mollifier moment order, every permitted detector shift,
finite norm interpolation, and asymmetric physical scales. It keeps the
same Type-II terms and the stated two-term physical norm.

At the density threshold \(\sigma=2/3\), one retained term is exactly
\(U^{5/6}\), independently of the moment orders and detector parameters.
Every complete finite threshold partition therefore has a class whose
available count exponent is at least \(\nu=5/6\) and whose contour placement
has \(x\ge2/3\).

An exact positive-weight certificate shows that all numerator norm budgets
generated by the listed estimates satisfy

\[
66e-55/p+45y\ge27.
\]

Here \(e\) is an allowed upper-budget exponent of the \(\ell^p\) norm,
including after restriction, and \(y\) is the numerator line.
For that class, its selected first-mean exponent \(m\) consequently obeys
\(66m+45y\ge82\). In the actual physical monomial this forces balanced
scale exponent \(a\ge15/37\), hence a boundary no lower than

\[
\frac56+\frac a6\ge\frac{100}{111}.
\]

At a fixed boundary, moving asymmetric scales to their balanced endpoint
only improves this class's budget. The long-support regime of the same
physical norm already costs at least \(11/12\). These observations exclude
those parameter choices as escapes from the stated floor.

This is a restriction on deductions from specified upper estimates. It
does not give an arithmetic lower bound, locate any zero, or establish an
optimal boundary for the whole repository. It also does not assert that
`100/111` is achievable after paying every other class.

The source-specific sum that needs a different treatment is explicit:

\[
c_A(\mathfrak n)=\sum_{\substack{\mathfrak d\mid\mathfrak n\\
                         N\mathfrak d\le A}}\mu_F(\mathfrak d),
\qquad
\sum_{V<N\mathfrak n\le H}
 \frac{c_A(\mathfrak n)(\psi\chi_{\mathfrak a})(\mathfrak n)}
 {(N\mathfrak n)^{2/3+it}}.
\]

Here \(A\le V\le H\le2V\), and \(\psi\) is the fixed finite twist.
The proof retains the actual prefixes, ideal columns, finite twists and
nonunit masks. A density-only escape below `9/10` would need a count exponent
strictly below `22/27` at `2/3`; the fixed `5/6` term would need a saving
greater than `1/54`. At the favorable fourth-moment line \(y=5/12\),
with the retained count exponent \(\nu=5/6\), an alternative selected
numerator saving would have to exceed `1/72`.
These are necessary costs, not sufficient new zero-free theorems.

Concurrent #976 contains overlapping full-strip numerator hierarchy work.
Its new physical-moment estimate and optimistic model use different inputs.
The selected reflected-ratio bounds in #977 and #978 use extra information
from the same zero-free rectangle and likewise leave the separate global-
moment numerator budget analyzed here. Those additions are credited and
are not contradicted by this theorem.

## Research priority after this pass

The principal signed source remains a direct proof-level target, and the
new Type-II formula gives another precise place to seek arithmetic
cancellation. The recent coupled reflected-ratio work should be assessed
with both numerator and denominator heights and every physical remainder.
Adding moment orders within the unchanged separate-estimate architecture
is no longer a promising way to seek a large further advance.

Newton now has a smaller explicit amplitude to attack. Its useful next
theorem is an energy bound on that remaining form and the two balances,
with a saving from the quadratic dependence on the old native energy.
Further compression alone would not supply it.

Lee–Yang has passed the next finite test. Its useful next theorem is a
target-reaching extension that can be iterated while retaining positivity
and convergence control. Another isolated finite order can test that
mechanism, but cannot substitute for it.

## Reproduction

From this packet directory:

```sh
python3 verify_packet.py
python3 verify_packet.py --replay
```

The first command authenticates the complete manifested payload. The
second also runs the exact all-order predicates and failing controls,
the complete declared Newton cases, the full theta-source contraction,
and the independent graph check. It uses standard Python and does not
require a numerical optimizer, network access or an external moment oracle.
See [VALIDATION.md](VALIDATION.md) and [REVIEW.md](REVIEW.md) for the distinct
roles and limits of computation and mathematical review.
