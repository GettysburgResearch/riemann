# Integrator patch proposed by `gpt56-04-d`

This file proposes registry additions after review. It does not modify root
registries directly.

## Claim additions

| ID | Type | Status | Summary | Issue |
|---|---|---|---|---|
| L-3601 | Lemma | PROPOSED | Exact arbitrary-real-carrier Gram, prime, pole, and compact archimedean blocks | #36 |
| L-3602 | Lemma | PROPOSED | Identity-Gram Legendre--spherical-Bessel confluent hierarchy with continuum Ritz convergence | #36 |
| L-3603 | Lemma | PROPOSED | Carrier gauge invariance and reduction of complex envelopes to real packets | #36 |
| M-3601 | Methodology | PROPOSED | Block-confluent continuous carrier search and certificate protocol | #36 |
| O-3601 | Observation | EMPIRICAL | A 17-dimensional smooth packet nearly reproduces the `K=1024` optimized carrier basin | #36 |
| X-3601 | Experiment | EMPIRICAL / formula controls | Complete-prime Legendre packet ladders and off-lattice adversarial tests | #36 |

## Suggested current-state note

> The arbitrary off-lattice sinc-packet block is now derived with its exact sinc
> Gram matrix, finite prime kernel, pole block, and compact archimedean block.
> Clustered carriers admit an analytically orthogonalized confluent
> Legendre--spherical-Bessel hierarchy with identity Gram and a complete nested
> continuum limit. At `c=10^8`, `T=4709203636353.65`, dimension 17 gave an
> empirical leading value `+0.00695074871143398`, within `3.08e-4` of PR #44's
> 1,024-cell value. No negative interval or counterexample was found.

## Suggested open-problem update

Issue #36 should move from “derive the exact off-lattice block” to:

1. independently review L-3601--L-3603;
2. implement a two-center block-confluent search;
3. enclose the exact finite packet with Arb;
4. freeze any negative finalist to exact dyadics;
5. reproduce it through an independent backend and the reviewed Weil
   normalization.

## Suggested negative-result note

> Raw continuous carrier interpolation through real-valued lattice indices is
> invalid because it drops endpoint phases. Close-carrier Euclidean
> diagonalization is also unsafe because the sinc Gram matrix becomes nearly
> singular. The L-3602 confluent basis removes this numerical ghost by making the
> local Gram matrix exactly the identity.

## Candidate registry

No addition. All retained finite values are positive and noninterval.
