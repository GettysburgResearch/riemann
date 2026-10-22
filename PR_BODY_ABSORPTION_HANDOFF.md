## Final analytic handoff - the exact absorption debt

T-105113 through T-105116 reduce the remaining cofinal second-carrier gate
to one explicit inequality:

\[
\limsup_{n\to\infty}
\frac{\mathfrak a_{2,n}e^{\mathcal X_{2,n}^*}\mathscr S_{2,n}}
{2\pi N_n}\le\nu.
\]

Here (\mathfrak a_{2,n}) is the authenticated anchor ratio,
(\mathcal X_{2,n}^*) is the optimally allocated Cartan exponent, and
(\mathscr S_{2,n}) is the smaller of the restricted-safe-set selector
mean and the actual outer-norm/perimeter bound.  A separate signed input
(A_n\ge\mu N_n(1+o(1))) yields strict coherence only if
(\mu^2/\nu>1/2).

Under two-sided generic loads (G_j\asymp X\log X), middle radius
(r_2\asymp X), and fixed shell width, the exact T-105116 optimizer still
costs (\Theta(X(\log X)^2)).  Radius retuning alone therefore cannot
close the generic equal-disk route.  Xi anchors/growth, actual manifests,
actual selector loads, absorption, signed positivity, RCMV104530, and RH
remain open.

Cross-program bridge: unmerged PR #720, claim L-104513, proves that every
(t)-plane Xi derivative is nonzero for (|\Im z|>1/2), so (a=-i) is a
common anchor candidate.  Import it only after restoring the omitted
origin-multiplicity term (q/z) in its canonical-product log derivative;
the term has the correct negative imaginary sign.  PR #720's L-104531
positive theta-orbit formula is the concrete source for the still-missing
fixed-order complex-disk growth corollary.

After correcting the factor-two mismatch between PR #720's L-104528 and
L-104531 kernel normalizations, the explicit candidate import is

\[
|\Xi_t^{(m)}(z)|
\le4\pi^2m!\zeta(3/2)\pi^{-q/2}\Gamma(q/2),
\qquad q=|\Im z|+11/2,
\]

and positive cosh/sinh pairing gives
(i^{-m}\Xi_t^{(m)}(-iy)>0).  This would close the common anchor and
fixed-order (O_m(Y\log Y)) growth inputs once the unmerged source blobs
and corrected corollary are frozen on the branch.

The lightweight regression ledger in
`experiments/X-105116-xi-kernel-normalization-audit` locks the corrected
factor (4), (q=|\Im z|+11/2), the (\zeta(3/2)) threshold, source provenance,
and both anchor parities.  It passes 11/11 focused tests in normal and
optimized Python with digest
`38a85d503250264cb8ca16583e1f5c813c8879ec03874d3556cf6a141ad61a67`.
It imports no source claim and leaves the Xi-growth, RCMV104530, and RH
flags explicitly open.

The audit also finds that PR #716 L-104504 uses the same half-normalized
kernel, so downstream PR #724 needs the same canonical replacement
(\Phi_{\rm std}=2\Phi_0).  Its normalized saddle/zero/PSD/orientation results
are scale-invariant, but raw Xi amplitudes require a factor (2) and its exact
Laguerre-defect and squared-norm identities require a factor (4).  This is a
normalization repair requirement, not a refutation of those invariant signs.
The same inherited linear-amplitude repair reaches PRs #725/#726/#728, while
their normalized residue/coherence conclusions remain unchanged.  PR #728's
gamma-based axis anchor is unaffected and complementary, but it supplies no
complex-disk growth envelope; none of the downstream packets imports H.9.
