# Frozen dependencies and scope

## Repository component

- PR [#905](https://github.com/GettysburgResearch/riemann/pull/905).
- Exact source commit: `0f82df3bf1d0bc669a1bbca09f8404b77c6fecde`.
- Load-bearing file:
  [NRC32 PROOF.md](https://github.com/GettysburgResearch/riemann/blob/0f82df3bf1d0bc669a1bbca09f8404b77c6fecde/standalone/2026-09-21-native-covariance-compression/PROOF.md).
- Imported repository components: finite Newton source identity through
  the strict square endpoint; exact harmonic block means; orthogonal
  finite-window variance decomposition; deterministic increment bound.
  These elementary parts are reproduced in the new proof.
- Preserved limit: the native coarse-covariance upper bound is open.

For the optional conditional interpretation in Section 7, the earlier
square-ladder bootstrap is also recorded in PR
[#848](https://github.com/GettysburgResearch/riemann/pull/848), exact head
`7de75c02417d5d8db7eafb1ceba364380e72d16a`,
[BNR26 PROOF.md](https://github.com/GettysburgResearch/riemann/blob/7de75c02417d5d8db7eafb1ceba364380e72d16a/standalone/2026-09-10-astra-balanced-newton/PROOF.md).
That conditional bootstrap is not used to prove the new unconditional
compression theorem, and its distinct state normalization is not silently
identified with the reciprocal energy in this packet.

## Primary analytic source

K. Matomaki, M. Radziwill, X. Shao, T. Tao and J. Teravainen,
*Higher uniformity of arithmetic functions in short intervals II.
Almost all intervals*, arXiv:2411.05770v2, 23 January 2026,
Theorem 3.1(i), specialized to the ordinary Mobius function and `T=0`.

- [Version-pinned primary text](https://arxiv.org/html/2411.05770v2).
- [Journal record](https://doi.org/10.1007/s00222-026-01408-6),
  *Inventiones Mathematicae* 244 (2026), 967--1091.
- Required range: `X^(1/3+epsilon) <= H <= X`, with fixed `epsilon>0`.
- Required content: arbitrary fixed inverse-logarithmic bounds for maximal
  sums over arithmetic progressions, outside an exceptional set of
  proportion bounded by an arbitrary fixed inverse logarithm.
- Native specialization: integer windows at `T=0`; contiguous prefix
  intervals are allowed progressions; the complete second moment over
  starts follows by paying the exceptional set with the trivial bound.
- The new proof only invokes this estimate in annuli with left endpoint
  `X >= (Y+1)^(3/2)`. The preceding annuli are paid by elementary variation.
- No numerical threshold or effective constant is derived in this packet.

## Independence and compatibility

This packet does not rely on PRs #962--965, on a Dedekind inverse
coefficient analogue of the rational Mobius theorem, on source completion,
or on an infinite Mellin projection. It neither changes nor supersedes
the distinct prime-memory, prime-detector, Eisenstein, or theta identities
in those packets.

The new theorem is an application of the above imported analytic result
to the native Newton resolution problem. It is not a new short-interval
Mobius cancellation theorem or a priority claim about that input.
