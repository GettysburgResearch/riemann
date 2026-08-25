# M-106080 — Superseded hostile-review contract for the minimum-owner proposal

Claim ID: `M-106080`  
Status: **SUPERSEDED BY THE COMPLETED SELF-RECONSTRUCTION AND THE `T-106081` REVIEW HANDOFF**  
Created: 2026-08-25  
Corrected: 2026-08-25  
Applies to: historical `T-106080`; binding `R-106080`; corrected `T-106081`  
Programme issues: #743, #736, #737  
RH status: **unproved**

## Binding posture

The hostile reconstruction originally demanded by this file has now been
performed internally. It found a decisive source-kernel failure and retracted
the former `T-106080` closure.

The independent reviewer must therefore begin with:

```text
claims/refutations/
  R-106080-core-only-centered-phase-packing-does-not-transport-owner-squareclasses.md

claims/theorems/
  T-106081-minimum-owner-boolean-vaughan-corrected-owner-occupancy-frontier.md

standalone/2026-08-25-t106080-self-reconstruction/
  REVIEW_SPECIFICATION.md
```

The old acceptance classification in which `T-106080` might be approved as a
complete RH proof is no longer live. Any attempt to revive it must first refute
`R-106080` by supplying a source-faithful fixed-squareclass map which preserves
the varying co-owner, physical Gram and modulus selectors.

## Results already reconstructed

```text
Boolean disjoint-support Möbius inversion             ACCEPTED EXACT
Boolean Vaughan identity                              ACCEPTED EXACT
balanced Boolean support has two literal core primes  ACCEPTED EXACT
squarefree lattice reindexing                         ACCEPTED EXACT
fixed-owner Boolean Type-I                            ACCEPTED POWER-SAVING
minimum-owner gauge                                   ACCEPTED EXACT
lambda^2 <= a and L^2 < 2B                            ACCEPTED EXACT
no-exception P <= a                                   ACCEPTED EXACT
exceptional lambda^5 < 4 sqrt(Y)                      ACCEPTED EXACT
abstract same-family identity                         ACCEPTED EXACT
```

The following former transport is rejected:

```text
complete varying-owner source
  -> fixed-squareclass c_b packet of L-102883.
```

## Current mandatory review order

1. verify the retained Boolean and minimum-owner reductions;
2. reconstruct the physical kernel on `P_i*a_i^2-P_j*a_j^2`;
3. verify the selector-tied Gram `T-106081.8`;
4. verify the corrected Cauchy coefficient
   `(rho-1)/(ell*rho)` in `T-106081.10`;
5. inspect the two sharpened sectors:
   - `MOBOSM-NE106081`, where `P_i<=a_i`;
   - `MOBOSM-EX106081`, where `lambda_i^5<4*sqrt(Y)`;
6. decide whether either sector admits a source-faithful mixed large-sieve,
   owner-conductor moment, residue-cell or renewal estimate;
7. independently verify `BSFTI106081`, the global parent-ledger Type-I
   transport;
8. retain the frozen Volterra/Mellin consumer only after the arithmetic moment
   is genuinely closed.

## Mandatory firewalls

A review fails if it:

```text
replaces P_i*a_i^2-P_j*a_j^2 by a_i^2-a_j^2;
declares different owner packets orthogonal after physical observation;
assumes the Hilbert coefficient norm which is itself the owner-occupancy target;
proves fixed-P estimates and recombines them source-blindly;
uses selected owner weights twice;
uses the first-draft coefficient (ell-1)/(ell*rho);
claims the finite replay proves MOBOSM106081;
claims T-106080 or RH is proved.
```

## Current acceptance classifications

### Corrected frontier accepted

```text
R-106080 source-kernel firewall                  valid;
T-106081 selector-tied Gram and moment           valid reduction;
MOBOSM106081                                     remains open unless separately proved;
RH                                               unproved.
```

### New arithmetic closure

A reviewer may prove `MOBOSM106081` directly or prove both sharpened sectors.
Only then, together with `BSFTI106081`, may the frozen detector composition be
invoked.

### Rejection or further correction

The reviewer must identify the first false equation or unsupported source
normalization in `R-106080` or `T-106081`, and preserve all exact reductions
which precede it.

The PR remains draft and must not be merged as an RH proof.
