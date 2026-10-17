# Audit scope and source identity

This component pass began as an independent read-only review of
GettysburgResearch/riemann PR #959, exact head
7b845294207d96b883c1fa95028663082267804f. It was redirected to distinct
source-specific mechanisms after checking the principal analytic interfaces.
It did not alter the remote repository or inherited source files.

## What was actually read

* The complete #959 `PROOF.md` and `SOURCES.md`, fetched at that head:
  https://github.com/GettysburgResearch/riemann/blob/7b845294207d96b883c1fa95028663082267804f/standalone/2026-10-17-numerator-mean-refinement/PROOF.md
* CT v2's primary PDF and TeX, specifically its allowed generators and angular
  character, reflected dyadic estimate and arbitrary-fixed-M>1 paragraph,
  additive normalization, and Section 11's local correction and principal
  noncancellation interfaces. Primary TeX:
  https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex
  The source index displayed hash prefix f54808ad0f967b54. This is not a full
  local-file hash or an independent reconstruction of all Kazhdan-Patterson
  foundations.
* BGL, `L-functions with n-th order twists`, arXiv:1112.1650, Section 5's
  complete-column second-mean calculation, including (5.1), and the detector
  passage. https://arxiv.org/pdf/1112.1650
* De Faveri, `Optimal large sieve for fixed order characters`,
  arXiv:2610.04045v1, Theorem 1.1 and the displayed full-family detector in
  Section 9's proof of Corollary 1.5.
  https://arxiv.org/html/2610.04045v1
* The complete OpenAI Poisson section, fetched first at main and then pinned
  at the verified current main commit
  1581d4cbdd69a0faf34b2089614fe2a814316a6a. Both contents matched blob
  c8526f74b281d37fda034c17195c4bb5afd5f79b. Its URL is cited in both proof notes.
* The existing #950 `MATHEMATICS.md`, supplied in the local reference tree.
  Its one-variable normalized correction, coefficient lift, critical
  convolution comparison, and open restoration condition are credited.

## Interpretation of the original audit

No fatal error was identified in the #959 interfaces inspected during this
pass. That is not an independent certificate of its complete proposed
11/12 result or of its imported analytic foundations. In particular this
pass does not audit the whole automorphic construction, fully rebuild the
fixed-twist character adapter, run a Lean dependency audit, or establish
literature priority.

A minor source-reference correction: in the fetched CT v2 PDF and TeX,
Section 11.1 states the three-variable correction domain in a paragraph;
the one-variable principal noncancellation result is Lemma 11.1. The #959
text calls these Lemma 11.1 and Lemma 11.2 respectively. The actual formulas
used here agree; this numbering mismatch is not an analytic obstruction.

The #959 positive theta estimate gives a method ceiling at 11/12 under its
linked scales. Further density partitions alone cannot improve that binding
bound. The two new component notes instead keep the second Mellin variable
and use the exact functional equation of the angular correction. They do
not claim to prove the signed estimate that remains open.

## Verification and limits

`verify_audit_components.py` runs exact rational substitutions for 48 local
Poisson parameter choices, checking two identities per choice, and 27 paired
Hadamard modulus identities. It writes `VERIFICATION.json`. All checks use
explicit failures rather than assert statements. Ordinary Python and
optimized Python (-O) both passed and produced byte-identical JSON reports.

The finite checks complement the written algebraic identities. They do not
verify analytic continuation, an infinite Euler product, the Hecke functional
equation, the actual source's Hardy membership, RH, or GRH. The new statements
are proposed component mathematics awaiting ordinary independent review.

Final component review corrections retain the exterior-to-S Mobius
coefficients and the physical prefactor X^(1/2-z0) in the free-z principal
residue. The divisor discussion includes zeros of zeta_F^S(6z), rather than
only its pole. The source-profile choice is conditioned on M(z0)!=0, with a
local Tate construction supplied; Gaussian convolution estimates justify the
full noncompact tails before applying Minkowski. The scattering note fixes
the inner-product convention and leaves the inverse Mellin example's single
endpoint convention immaterial. These clarifications do not supply the open
signed automorphic estimate.
