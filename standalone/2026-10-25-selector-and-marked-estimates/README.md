# Second attack: finite selectors and uniform marked estimates

Date: 25 October 2026.

Status: exploratory research packet containing proved component arguments,
explicit source-dependent estimates, independent agent reviews, and finite
diagnostics. **No smaller zero-free half-plane is established.** The all-scale
arithmetic or spectral estimate that would move the boundary remains open.

This is an additive continuation of PR #1021's first mathematical packet at
`742e952be4ef7843de86ea12678c0bdd3d3579c3`. It preserves that packet and its
reviews. The changes below close two specific gaps in its proposed routes,
prove an actual fractional coefficient window, and establish a sharp
parameter/error tradeoff for growing integer marks.

## What actually advanced

| Direction | Completed result in this pass | Remaining estimate |
|---|---|---|
| Marked squarefree count | Exact matching of the complete principal term to a specified prime-power model; an exact reciprocal-moment cancellation removes the earlier hyperbola exponent loss | A power improvement for the resulting signed prime-error convolution |
| Growing integer marks | A uniform positive theorem for `K <= (log X)^theta`, with a matching exponent obstruction when `theta > 1/2` | A genuinely noninteger or marked-derivative bound; the growing integer shortcut does not provide it |
| Fractional native mean | The desired native envelope holds uniformly on an explicitly quantified power-thin interval near `z=1` | A much wider interval or a new signed mean; the proved width is insufficient for continuation to `z=-1` |
| Spectral selection | Positive tight legal selectors imply RH without identifying an entire limit with Xi; exact finite even matrices suffice on an explicit cofinal schedule | An all-scale lower bound for those matrices, or existence of globally nonnegative tight finite selectors |

The most useful new target is the finite even-matrix problem in Section 1.
It keeps every prime power and both pole terms, gives an explicit matrix
size, and removes both a separate odd-sector requirement and a separate
continuum-legality requirement from that formulation. Those reductions are
proved; the matrix hypothesis is not.

## 1. A finite matrix target that really detects zeros

Let `Q_k` be the exact compression of the complete semilocal Weil form to
the even functions

\[
E_k=\operatorname{span}\{1,\cos(\pi x/k),\ldots,
                 \cos(N_k\pi x/k)\},\qquad N_k=\lceil k^3\rceil,
\]

on `[-k,k]`, with zero extension. It includes all prime powers up to
`exp(2k)`, the complete archimedean term, and both pole terms. Write
`lambda_k=min spec(Q_k)` in the inherited `L2` normalization.

Fix `eta >= 0`. The new consumer proves

\[
\boxed{\quad
\lambda_k\ge-C_\varepsilon e^{(2\eta+\varepsilon)k}
\ \text{for every }\varepsilon>0\text{ and all large }k
\quad\Longrightarrow\quad
\zeta(s)\ne0\quad(\Re s>\tfrac12+\eta).
\quad}
\]

In particular, a lower bound of size `-exp((1/2+epsilon)k)` would give
`Re s>3/4`; a subexponential negative lower bound would imply RH. The
known elementary estimate of size `-O(k exp(k))` only recovers the trivial
strip. A finite list of matrix minima cannot establish the displayed
all-scale hypothesis.

The proof has two substantive steps. Symmetric separated bumps turn an
even-sector lower bound into a one-sided bound on a smoothed Weil
distribution. Adding a positive exponential and using the elementary
Landau theorem for nonnegative Laplace transforms detects the exact poles
at `rho-1/2`; zeta has no real nontrivial zeros that could account for a
rightmost real singularity. Compact Gevrey bumps then approximate those
tests in the prescribed finite spaces. Their Fourier tail beats the full
`O(k exp(k))` prime/pole operator loss. Endpoint jumps are controlled in
the actual logarithmic form domain.

There is also a selection version. Choose shifts `kappa_k<lambda_k` and
normalize

\[
f_k=\frac{(Q_k-\kappa_k)^{-1}1}
             {\int_{-k}^k (Q_k-\kappa_k)^{-1}1}.
\]

If these physical trigonometric polynomials are nonnegative on their
whole intervals and their mass-one measures are uniformly tight, then
`kappa_k -> 0` and RH follows. Uniformly bounded second moments suffice
for tightness. The proof compares the exact finite variational equation
with projected theta and broad theta-convolution test vectors whose
complete-source residuals tend to zero in sup norm.

This is a concrete reduction of the first packet's variance-selector
problem: positive variance-matched finite selectors on the cofinal
schedule would be enough. A separate identification of a limiting
entire function with Xi is unnecessary under these hypotheses. The
unresolved requirement is their existence and global physical sign.
Adding positivity and variance constraints to an unrelated minimization
does not automatically produce the unconstrained resolvent equation
required here.

Full proofs:
[spectral growth and tight selectors](spectral/SPECTRAL_GROWTH_AND_TIGHT_POSITIVE_SELECTION.md)
and [even finite-matrix consumer](spectral/EVEN_FINITE_SELECTOR_CONSUMER.md).

### What the selector computations establish

Eight finite cases were completed using the authenticated PR #1017
matrix source. At half-width `a=1.3`, the target variance lies outside
the tested endpoint bracket at 16 modes and inside it at 32 modes. At
`a=1.8`, 32 modes again miss that bracket. The bracketed cases have
positive sampled physical densities. A failed endpoint bracket does not
prove nonexistence of other roots, and sign samples do not prove global
nonnegativity.

The selected shift at `a=1.3`, 32 modes is approximately
`-8.9350e-46`. Its small size is not a continuum lower bound. These runs
use ordinary arbitrary precision and quadrature, without outward error
bounds. The [diagnostic report](spectral/NUMERICAL_SELECTOR_DIAGNOSTICS.md)
records all cases, the complete prime-power lists, the two parity minima,
the numerical settings, and the limitations. They are not executions of
every member of the cofinal schedule above.

## 2. The marked remainder now has a completely matched main term

For a fixed nonzero smooth profile supported in `(1,2)`, set

\[
S_W(Y)=\sum_n\mu^2(n)W(n/Y),\qquad
c_W=\widehat W(1)/\zeta(2),\qquad E_W(Y)=S_W(Y)-c_WY.
\]

Let

\[
J(u)=\sum_{p^j\le u}\frac1j,\qquad
J_0(u)=\int_1^u\frac{1-v^{-1}}{\log v}\,dv,\qquad R=J-J_0.
\]

The fixed target is the signed discrepancy

\[
\Delta_W(X)=\int S_W(X/u)\,dR(u).
\]

The new matching theorem proves, for `1/2<c<b<1`,

\[
A_\omega(X)-C_{\omega,b}(X)
=\Delta_W(X)+\int_c^b
       \frac{\zeta(v)}{\zeta(2v)}\widehat W(v)X^v\,dv
       +O(X^c),
\]

with the exact principal term and branch convention of the first packet.
The displayed real integral is `O(X^b/log X)`. All higher prime powers
are included. This closes the earlier main-term matching gap, including
its cutoff contribution.

Under a stated prime-error bound `R(u)=O(u^beta)`, `1/2<beta<1`, one has
the exact reciprocal moment and its consequence

\[
\int_1^\infty\frac{dR(u)}u=0,
\qquad
\Delta_W(X)=\int_1^\infty E_W(X/u)\,dR(u)=O(X^\beta).
\]

This improves the first pass's separate-bound exponent `(1+beta)/2`
back to `beta`. It does not improve the input exponent `beta` itself.
The surviving hard range is `u` comparable to `X`, where the squarefree
kernel has bounded scale. The proof also identifies the local logarithmic
suppression at a zero and explains why it leaves the power `X^(Re rho)`.

See [the complete matching proof](marked/MATCHED_PRIME_SQUAREFREE_REMAINDER.md).

## 3. Growing integer marks: a positive theorem and a matching limitation

For the explicit smooth profile in the proof, put

\[
A_K(X)=\sum_n\mu^2(n)K^{\omega(n)}W(n/X),\qquad
C_K(X)=\operatorname{Res}_{s=1}
       \bigl(\widehat W(s)\zeta(s)^K H_K(s)X^s\bigr),
\]

where `K` is a positive integer and
`H_K(s)=product_p (1+K p^(-s))(1-p^(-s))^K`. The full pole polynomial
is retained.

For every fixed `0<theta<1` and `epsilon>0`, the new uniform theorem gives

\[
\boxed{\quad A_K(X)-C_K(X)
 =O_{\theta,\varepsilon,W}
  (X^{\max(1/2,\theta)+\varepsilon}),\qquad
  K\le(\log X)^\theta.\quad}
\]

The proof tracks both the Euler correction, of logarithmic size
`O(K^(1/sigma)/log K)`, and the uniform Mellin integral, whose remaining
cost is `exp(O(K log K))`. Its smoothing and contour estimates are proved
in the note.

For `theta>1/2`, a uniform scalar error `O(X^b)` on that range necessarily
has `b>=theta`. The lower argument exhibits actual continued-Euler-product
growth at heights tending to zero, so it cannot be repaired by stronger
high-frequency smoothing. It also rules out every fixed `b<1` on the
larger range `K<=log X/loglog X`, even after the complete pole subtraction.

The factorial in a high-order local Hankel coefficient is retained:
`N!/(log X)^N` is still a subpower factor when `N` is of order
`log X/loglog X`. Suppressing that factorial would give a false power
saving. These are results about scalar integer counts, not lower bounds
for a different native character mean.

Proofs: [uniform positive theorem](marked/GEVREY_INTEGER_WINDOW.md) and
[arithmetic resonance and limitation](marked/GROWING_INTEGER_RESONANCE.md).

## 4. The fractional native mean has a proved, but too narrow, interval

Use the first packet's actual sixth-power-free physical row family and
its normalized vector with coefficient `mu^2(n) z^omega(n)`. Write its
squared row norm as `M_z(U,D)`. Under the pinned ordinary endpoint and
full arbitrary-coefficient sieve inputs, the new estimate is

\[
\sqrt{M_z}\le\sqrt{M_1}
 +C_\varepsilon(UD)^\varepsilon(1-z)(1+\log\log D)
  \sqrt{U+D+U^{5/6}D^{1/3}+U^{1/3}D^{5/6}},
\]

with the profile seminorm, fixed ray data, common puncture and height
costs specified in the proof, for `0 <= z <= 1`. It comes from the actual coefficient
energy and the Hilbert-space triangle inequality.

For the native target `U+U^(1/6) D^(4/5)`, this proves a uniform window
`1-U^(-kappa)<=z<=1` with:

| Lengths | `kappa` |
|---|---:|
| `D=U` | `1/12` |
| `D=U^(25/24)` | `29/288` |
| `D=U^(3/2)` | `13/120` |

The same power-thin scale works in a complex disk around one. It is an
actual noninteger estimate. Its width is nevertheless too small for the
generic coefficient-continuation bound to have subpower cost. The much
wider proposed scale `1/loglog D` remains open.

A companion theorem, conditional on a fixed zero-free half-plane, shows
that a polynomial-height norm twist cannot approximate the negative
prime phase even in harmonic mean square. The narrow-prime-band attempt
requires new arithmetic support and product-moment control. The
shifted-prime paper examined in this pass supplies neither that native
embedding nor a fixed-power estimate for this problem.

Proofs: [fractional window](fractional/UNIFORM_FRACTIONAL_WINDOW.md) and
[norm-twist/band analysis](fractional/NORM_TWIST_AND_BAND_TRANSFER.md).

## 5. Review, computation, and source boundaries

The three researchers cross-reviewed one another's complete analytic
notes and bound their reports to exact SHA-256 hashes. The root agent
also read the load-bearing proofs. This is independent agent scrutiny,
not external peer review or formal verification. The imported ordinary
and arbitrary-coefficient moment frameworks retain their original scope.

The exact marked-convolution checker verifies 2,048 coefficient identities,
340 retained prime powers, and 17 finite smoothing identities. Removing
the required prime-power corrections creates 418 failures, beginning at
`n=4`. The root reproduced the normal and optimized outputs byte for
byte. This tests the finite identities, not the contour or asymptotic
estimates.

The root independently reconstructed the PR #1017 source archive from
its pinned Git objects and matched the copied matrix source byte for byte.
It repeated the `a=0.4`, 16-mode selector at higher precision and quadrature
order. The stored matrix values, selector coefficients, shift, variance
and sampled signs agree at their reported digits; the floating-point
linear-system residual changes with precision, as expected. This replay
uses the same matrix implementation and is not an interval certificate.

See [sources](SOURCES.md), the review reports under `reviews/`, and
[the root replay receipt](reviews/ROOT_REPLAY.json). The copied
`spectral/source/NUMERICS.md` is an unchanged provenance document from the
older source package; its old reproduction commands refer to that full
archived package. Use this packet's diagnostic report to reproduce the
new selector runs.

## Next mathematical work

The spectral route now calls for a source-specific proof of the finite
matrix lower bound, or a proof that the exact finite legal selectors
exist with global sign and tightness. A finite positive computation or
the theta residual alone does not establish either statement.

The arithmetic route now calls for cancellation in the fully matched
`Delta_W` or in the actual signed fractional convolution. Increasing
integer mark orders, a single norm twist, and a power-thin continuity
interval have quantified limits. A new prime/same-prime-count mean or a
faithful native-kernel root-averaging theorem would address the missing
arithmetic gain; no such theorem is asserted here.

These are the precise surviving tasks. The packet adds completed
components and removes identified intermediate gaps while keeping the
zero-free claim at its established scope.
