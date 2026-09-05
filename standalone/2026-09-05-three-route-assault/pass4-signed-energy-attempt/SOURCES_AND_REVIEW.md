# Exact sources, proof audit, and failed closure

## Repository sources inspected

- PR #793 at bfb66e07f7e38306dbcb916911332a591efce917: live metadata and
  comments were fetched. The supplied pass3 archive was extracted locally.
  Its R2_MOBIUS_LAGUERRE.md is the retained definition of a_n, its diagonal,
  and the exact squarefree-sign countercontrol. The other route notes
  remain background, not newly independently accepted proofs.
- PR #790 at bce97be9727dea9968db7517738edc966d2cc86b:
  standalone/2026-09-05-astra-theta-count-closure/heat-hankel-pass5/PROOF.md;
  Git blob caf9753e5c3e3bb918289da0f4e92ae7c6441f6c. The displayed source
  budget, trace-class construction, full-background interpolation and
  dyadic approximation sections were read. The source-budget argument
  needed here is reproduced in PROOF.md, including the stronger use of
  both members of a hypothetical nonreal invariant pair.
- AGENTS.md at the exact #793 parent was read; Git blob
  be9b5255e6108096450bfd63d8f04a7e9cec580a.

The source budget is classical invariant-product algebra. This pass does
not depend on accepting the full negative-index or dyadic-capture claims
of #790; those remain cross-programme context. Their code was not rerun.

## External primary references checked

- NIST Digital Library of Mathematical Functions, equation 18.18.27:
  https://dlmf.nist.gov/18.18.E27
  The Hille--Hardy Poisson kernel, specialized to Laguerre parameter zero.
  The formula is imported, not claimed new. Its finite coefficient algebra
  is checked in verify.py.
- NIST DLMF, equation 10.32.1:
  https://dlmf.nist.gov/10.32.E1
  The elementary cosine-integral representation of I_0. The estimates
  actually used are derived in PROOF.md rather than imported as an
  unverified asymptotic formula.

The Hardy weighted disk-automorphism identity is standard. Its precise
Jacobian, the source normalization, and the meromorphic/Taylor distinction
are proved in the text. The needed positive Tauberian argument is also
proved there using moments of finite measures and polynomial approximation.
The elementary squarefree-density estimate is fully reproduced.

General background search also located Suzuki's 2023 screw-function paper
and the 2026 abstract 'Weil's quadratic form via the screw function'. No
new theorem or proof from the latter is used. Neither a PDF audit nor a
full reading of that paper is claimed. No external priority claim is made
for the new source-specialized consequences without a literature audit.

## Proof review priorities

1. Norm identity: treat each side as a Taylor/H2 norm, not the integral of
   meromorphic values around a circle enclosing a pole. Finiteness in either
   direction has to give a holomorphic continuation before applying the
   unitary disk-change formula.
2. Quartet factor: the source H counts all upper-half-plane rho with
   multiplicity; an off-line quartet yields TWO conjugate invariant A's.
3. Source radius: beta is in the open critical strip. The resulting
   317/325 is a fixed squared radius below one, not an all-radius estimate.
4. Diagonal: the k=1 atom contributes exactly one to the Abel limit. It
   cannot be replaced by the squarefree density approximation.
5. Counting error: E_q(1)=0 is used near x=1. A global O(sqrt x) bound alone
   would not make the boundary-layer error vanish.
6. Abel to partial sums: positivity is available for Delta_n. It is not
   asserted for a_n or signed off-diagonal terms. No quantitative partial-
   sum remainder is claimed from the Abel remainder alone.
7. The same-diagonal countercontrol has a different source. It refutes a
   sign-blind comparison, not the assertion about the literal Mobius signs.

## Source-H rational enclosure

The executable uses H_n-log(n+1)<gamma_E<H_n-log n with n=512. These
inequalities follow by comparing each logarithmic increment with its
endpoint reciprocals. Rational atanh series enclose logarithms; Machin's
arctangent identity and alternating-series remainders enclose pi.
No floating-point value or predecessor PASS record participates in the
acceptance test 0<H<1/40. Displayed decimal endpoints are rounded outwards
with integer floor/ceiling, not ordinary decimal formatting.

## Execution scope

RESULTS.json is freshly reconstructed and compared byte for byte. The
706 finite controls are bounded algebra, including Hille--Hardy coefficient
identities, rational disk maps and pole thresholds, and finite squarefree
local-factor inversion. The separate H certificate is not counted again
as hundreds of additional tests. Ten unit/rejection tests cover invalid
inputs, a changed stored result and boolean/integer aliases.

These executions do not machine-prove the infinite analytic arguments.
No actual high-degree signed Mobius energy was computed; no prime/zero
census, directed integral, Lean build, remote CI or predecessor broad suite
was run. VALIDATION.json records the commands and exit/output hashes.

## Remote boundary

The GitHub tools exposed in this pass support repository reads, but no
create/update operation was discovered for publishing commits. Provider
search confirmed the GitHub plugin is installed. The direct Git check
failed with 'Could not resolve host: github.com'. No remote mutation is
claimed, and no new head SHA or commit is invented. The add-only patch is
bound to the fetched #793 base. Applying it to another head requires the
usual diff/conflict review; it must not overwrite parallel work.

## Scientific disposition

An RH completion was attempted and was not obtained. The signed norm is
proved finite only in the displayed fixed range. The diagonal asymptotic
and norm identity are complete proposed component proofs. Infinite safe-
point derivative data do not by themselves bound the required square sum.
The specific remaining all-radius finiteness is not discharged, and the
other routes retain their all-order positivity questions.
