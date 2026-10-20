# Scoped component review and frozen-file manifest

Review date: 2026-10-20. Reviewer: liu_paper_audit.

## Scope and disposition

The independent analytic review of uniform_mobius_consequence.md and
hecke_small_prime_consequence.md found no material gap in their stated
implications from a common Hecke zero-free half-plane. Both retain the
imported preprint theorem as an external premise. Neither implication
improves that boundary.

The reviewer authored liu_source_audit.md, artin_chebotarev.md and
principal_factorization.md. Their hashes below identify the versions
submitted for the separate root review; this document does not relabel
author checking as independent peer review. The source audit is explicitly
limited to identification, field transfer, descent, selected scalar and
numerator checks, and proof-status accounting. It does not certify every
analytic step of Liu's 136-page paper.

### Conductor-uniform reciprocal and signed Möbius bound

The logarithm exists on the simply connected half-plane after removal
of the principal pole. On the small disk its Euler logarithm is uniformly
bounded. Borel-Carathéodory controls it on the larger disk by \(\log Q\), and
three-circles gives \((\log Q)^\theta\) with one fixed \(\theta<1\). The disks
remain a fixed positive distance from the boundary; their height shifts
are bounded. The constants therefore remain uniform in the conductor
and finite-order character for a fixed field.

The Perron coefficients are bounded uniformly by the coefficients of
\(\zeta(s)^n\). The half-integer cutoff removes proximity to an integer norm.
The stated truncation error follows by separating norms near the cutoff
from the remaining absolutely convergent series. With \(T=x^2\) and
\(e=\epsilon/(8n)\), the shifted vertical integral is
\(O(q^e x^{B+3\epsilon/4})\); horizontal pieces and truncation errors fit the
remaining margin. No unsigned ideal sum replaces the signed main object.

**Correction incorporated:** the growth statement for the normalized
principal function was initially worded for every bounded real strip.
Its rational normalizer can have a pole at \(s=-1\). The root changed the
statement to bounded real strips contained in \(\operatorname{Re}s>B\). The
corrected version is the one hashed below; the correction covers the
disks used by the proof.

### Uniform small primes and ray-class generators

The fixed annular weight has integral one, vanishes with its first
derivative at both endpoints, and has a Mellin transform decaying
quadratically in height. The completed logarithmic derivative at \(s=2\)
bounds the absolutely convergent weighted zero sum by
\(\log(DN\mathfrak f)+n\), uniformly in the field. The functional-equation
shift to \(\operatorname{Re}s=-1/2\) controls the remaining contour with the
same arithmetic quantity. The trivial-zero contribution at zero is at
most a constant times \(n\); the Mellin kernel is regular there.

The missing Euler factors cost at most
\(\omega(\mathfrak m_0)\log X\), which the displayed error absorbs. Removing
rational prime powers of exponent at least two costs \(O(n\sqrt X)\) by
the elementary Chebyshev bound, and therefore permits degree-one prime
ideals. Character projection onto a subgroup of index \(i\) gives the
main term \(X/i\); its averaged error has no further factor \(i\).
These facts justify the stated exponent \(1/(1-B)\) for detection and
for subgroup generators. The proof correctly does not assert this bound
for a prime in every prescribed ray class.

The exact transformation of the boundary polynomial and the elementary
weight identities were checked by direct arithmetic during this review.
The separate root checker provides the machine replay of those scalar
identities.

### Principal local identity checker

verify_principal_factorization.py was executed successfully using
Python's standard library. It checks six exact polynomial/exponent
identities and rejects five explicit symbolic mutations. The variables
\(v,D,R\) remain algebraically independent. In particular the angular
phase is retained, and the target character's sixth power is not
replaced by one.

This finite checker covers the displayed local algebra only. Normal
convergence, global Hecke continuation, the small-scale Mellin tail,
and the angular Möbius convolution estimates are written analytic
arguments in the companion note. The checker does not certify them,
the exceptional-theta origin of the local series, or the upstream
zero-free theorem.

## Frozen-file SHA-256 manifest

Paths are relative to the eventual standalone packet. The hashes refer
to the completed files in the shared work directory before assembly.

| File | SHA-256 |
|---|---|
| uniform_mobius_consequence.md | 955bca0d2c40f8bcf9aa929d52f5a75d5f19dfe100fa3889c91b3cc3a2dd8d86 |
| hecke_small_prime_consequence.md | 978862e9932f9dfcbbacb084f45ab30aca42ae5fa2f35dffb1c7a5093b78daa6 |
| principal_factorization.md | a30318e672f6ae7bc91defdb1ba1e23447b4d9d315cce77dbb47efb2e4d79fd0 |
| artin_chebotarev.md | 7cd0567c4106665ee4d81cc0a3a6938ac18785dd83fa1d6bba5aed86ccb8c9a9 |
| liu_source_audit.md | b8e278c1aa1f3dd85186fcf052b3f5173da16759c4959fdd94e313d01b2bff9e |
| verify_principal_factorization.py | a14d511f519c66726455dc3d91b056cf1161dabf28811c778752db26e811ff1a |
| PRINCIPAL_FACTORIZATION_CERTIFICATE.json | 97c422f5cda4d0f846b08f059baf18c3fccce72ee8c8a54a5e7dc912877168c5 |

The source PDF remains pinned to arXiv 2610.26835v1, SHA-256
5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5.
Any later changes require corresponding hash updates and review of
their mathematical scope. This is a file-level component review, not
an approval of an unseen assembled Git commit.
