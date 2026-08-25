# Minimum-owner Boolean Vaughan closure proposal

Date: 2026-08-25  
Execution PR: #751  
Programmes: #743, #736, #737  
Parent: PR #719 at `60285de21fafdd1b3c185ddd19b57191a41c08dd`  
Status: **full proof proposal; independent hostile review required**

## New mechanism

The prior scale-matched character coordinate left power-sized coherent owner
families in one residue cell.  The new proposal changes the owner/Vaughan gauge
before that collapse.

1. Work in the literal squarefree Euler algebra using disjoint-support Boolean
   convolution.
2. Apply an exact Boolean Vaughan identity.  Its balanced row contains two
   distinct core-prime labels; its zero-moment Type-I row remains power-small.
3. On each horizon, include the unique uncompletable label if present and use
   the smallest available label as the other owner; otherwise choose the two
   smallest labels.
4. The smaller owner `lambda` then obeys `lambda^2<=a` on every balanced core.
5. After dyadic projection `B<=a<2B`, `L<=lambda<2L`, every block satisfies
   `L^2<2B`.
6. The existing coherent centered double-phase theorem therefore closes every
   balanced block; the former short-core range is empty in this gauge.

The proposed chain is

```text
Boolean squarefree Vaughan
AND
minimum-owner horizon gauge
AND
parent coherent centered phase packing
 -> derivative negative mass is subpower
 -> fixed Volterra/Mellin consumer
 -> RH.
```

## Binding review points

The finite algebra and range implication are exact.  The extraordinary claim
stands or falls at two source transports:

```text
Boolean squarefree Type-I
  -> the parent globally closed Type-I Hilbert row;

minimum-owner Boolean balanced source
  -> the literal owner-weight allocation in parent L-102883/T-102890.
```

`M-106080` requires a reviewer to identify the first failed equation or source
normalization if rejecting the proposal.  No canonical RH status is changed
before that review.

## Replay

```text
PASS_X_106080_MINIMUM_OWNER_BOOLEAN_VAUGHAN
checks=34250
sha256=86bb5ac732d2548679b16000a61c1fa40d961c962bde5d44edf9d39c110f98df
```

The replay certifies finite Boolean convolution, owner selection, dyadic range,
centered same-family kernels, squarefree reindexing and clean phase fixtures.
It does not certify the two analytic source transports, the Mellin consumer or
RH.