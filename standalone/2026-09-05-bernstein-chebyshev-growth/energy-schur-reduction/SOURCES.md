# Sources, scope, and independent-review boundary

## Verified remote starting point

PR #792 in GettysburgResearch/riemann was read at the live head
`ddeca90f7aa6facd77841d38207aabe38d7a8f53`. The commit message is
`research(astra): explicit finite-window coercivity for PR792`.
The published PROOF.md has 13,270 bytes and Git blob
`35d8d38a77bee896b0b2e729b095ccdef5d7a50f`, matching the prior supplied proof.
This verifies that the mathematical packet landed. It does not claim that
all ancillary files match a prior local archive or have been re-reviewed.
The PR body's then-current summary described the preceding separated-window
layer; the actual commit and file content, not that older body, establish
publication of finite-window-coercivity.

## Mathematical inputs

1. `finite-window-coercivity/PROOF.md` at the live head above: exact positive
   subspace and q(v,v)>=(3/4)||phi_v'||^2. Read in full. The present proof
   replaces its unresolved formal-inverse step, not its remaining sign.
2. `local-window-positivity/PROOF.md` at
   `2c3184545bafb4f5d873d2fa0ffc2c335a25d048`, blob
   `8d7120ef2edc0ac033a4814eb61917652fc57ba8`: full finite-window formula,
   exact tail retention, gamma source at zero. Read in full.
3. `cross-route-hardy-laguerre/BRIDGE.md` at
   `39c13367f4b3956631ea1e00fac6c3005fc32057`, blob
   `81d7d5db7a25f5875a08c10235fdb514d67cc744`: bounded/trace-class source
   and the original d_n trace endpoint. Read in the preceding work and
   authenticated again here.
4. `separated-window-gluing/PROOF.md` at the current live head was read for
   overlap. Its six-window sign is NOT imported into an all-window claim.

The checker authenticates the three literal parent proof blobs before any
finite replay. It does not certify those analytic proofs or their publication
review status. No other agent's sign claim is imported as established RH.

## Primary literature consulted in this pass

- J. Friedrich, M. Guenther, L. Klotz, *A generalized Schur complement for
  non-negative operators on linear space*, arXiv:1708.01545 (2017), later
  Banach J. Math. Anal. 12 (2018), 617--633.
  https://arxiv.org/abs/1708.01545
  The abstract and bibliographic information were retrieved. The full paper
  was not independently audited. It is prior-art context, not an imported
  lemma: the Riesz, infimum, and index arguments are proved here.
- Masatoshi Suzuki, *Weil's quadratic form via the screw function*,
  arXiv:2606.09096v2 (2026), introduction and main-result discussion.
  https://arxiv.org/html/2606.09096v2
  Relevant context is the localized Weil form and the finite-codimension
  results attributed to Yoshida. Suzuki's unbounded operator is not silently
  identified with the compact damped operator used in this PR.
- NIST DLMF 5.7, digamma series.
  https://dlmf.nist.gov/5.7
  Relevant to the parent source. No new special-function identity is claimed.

Generalized Schur/shorted forms, Riesz representation, Galerkin orthogonality,
Sobolev integration by parts, and inertia principles are classical. No
external novelty or priority claim is made. The source-specific new step is
energy continuity from W^(1,1), followed by the explicit residual enclosure.

## What would finish and what was not finished

The effective matrix S_L is now well-defined without an L2 inverse. Its sign
for actual xi at all lengths has not been proved. No finite-dimensional
positive sign is asserted by the floating reconnaissance. A correct arithmetic
lower certificate remains to be constructed, together with an all-length
argument for RH. No independent referee review has occurred in this pass.
