# Validation and publication scope

## 1. Preserved conversation artifacts

The following two mounted files were supplied by the prior chat and are preserved byte-for-byte under `evidence/`:

| File | SHA-256 |
|---|---|
| mobius_packet_check.py | `d8b87123900d07c9db074f8d6c030e251b5f24eb5aab56cbc55b3850cfff81fa` |
| mobius_packet_check_results.json | `cadabefd169b0f3e61739d7d647cc647bf93f765c1adfe2dfa00b7471e79c061` |

During this publication session the checker was run with default limit 500000 and cutoff 512, once in ordinary Python and once with `-O`. Both output JSON files compared byte-for-byte equal with the supplied JSON. No assertion-removal artifact is used: the checker raises explicit exceptions on failed mathematical conditions.

These are bounded exact-rational checks of moments, Gram energies, derivative constants, finite dilations and complete finite-prefix decompositions. Floating numbers in JSON are display fields; they are not directed interval bounds. The program does not test the entire Golomb hierarchy, prove asymptotic packet coverage, or calculate infinite Gaussian energies.

Reproduce from this packet directory:

```sh
python evidence/mobius_packet_check.py --output /tmp/rhg26-packets.json
python -O evidence/mobius_packet_check.py --output /tmp/rhg26-packets-opt.json
cmp evidence/mobius_packet_check_results.json /tmp/rhg26-packets.json
cmp /tmp/rhg26-packets.json /tmp/rhg26-packets-opt.json
```

A separate small exact checker under `checks/` exercises additional finite identities and explicit failure controls. Its recorded result and source-binding receipt specify the actual execution scope. These tests do not certify the infinite analytical arguments.

## 2. Mathematical audit scope

The synthesis reconstructs proofs, corrects identified normalization errors and labels unresolved statements. It is not an external review, a formal verification, or a claim that every proposed composition has been accepted by the repository. In particular, the sparse fixed-Gaussian theorem, digit-boundary proof and exact exponent/multiplicity deductions are proposed written arguments requiring independent review.

Classical inputs are stated and attributed. Numerical values whose generating artifacts were not supplied are explicitly marked historical/unreplayed. No 10^7 Golomb computation, prime-zeta boundary search, arbitrary-height zero census or infinite determinant has been rerun for publication.

## 3. Repository and transport boundary

All publication changes are add-only under `standalone/2026-09-17-reciprocal-hierarchies-to-gaussian-energy/`, based on `f99d9e3908dde4865377c75d9ca051c1f545bf4f`. No source files on other research branches, canonical status records, workflows or main are edited.

GitHub connector reads and writes are the publication mechanism. A container attempt to retrieve a public raw file failed DNS; it is not reported as a successful local repository checkout. The supplied local artifacts and their replays were accessible independently of that failure. No whole-repository validation, Lean build, independent remote CI result or full local checkout test is claimed.

The actual PR and head SHA are supplied in the publication receipt/PR description after successful remote verification. A draft receipt or locally planned branch is not evidence of publication. The packet's file inventory and the remote changed-file list delimit what was delivered.

## 4. What no test proves

The following remain unproved regardless of successful finite checks:

- the native signed-covariance upper bound on cofinal cutoffs;
- the fixed-Gaussian subpolynomial norm estimate;
- an all-scale small residual/inter-packet budget;
- the nested Golomb infinitude and density law;
- uniform continuation of the infinite Golomb sieve through growing character moduli;
- an RH-strength generic Type-II or short-interval variance estimate.

The packet's value is a complete source-qualified research handoff, including useful component arguments and refuted shortcuts, not an RH completion.
