# Why bounded finite-cluster stability is not a global zero-basis theorem

Round2 negative knowledge,2026-11-17. Status: elementary deductions from the classical zero-count asymptotic; no novelty claim. These deductions identify an assumption mismatch rather than an error in any cited theorem.

## Source input and exact counting convention

The Riemann–von Mangoldt asymptotic counts nontrivial zeros with multiplicity and positive ordinates:

N(T)~(T/(2pi))log T.

This classical input appears in the inspected BCF1211.5191v1 proof of Lemma3,pp.6–7, in its equivalent symmetric counting form. Its classical proof is not re-audited here. Avdonin–Ivanov math/0103160v1 assumes relatively uniform discreteness (a finite union of separated sequences) in its global Riesz-basis theorem; Theorem4 discusses a negative result when that assumption fails. Only the separately proved elementary implications below are used here; no stronger consequence is attributed to their Theorem4.

## Proposition E-DENSITY-001

Let Lambda be the multiset of positive zero ordinates gamma, or any fixed positive linear rescaling a*gamma with a>0. Then:

1. Lambda cannot be a finite union of uniformly separated sequences, with multiplicity counted.
2. Lambda cannot be covered by clusters of uniformly bounded cardinality q, each lying within a fixed radius R of a center, with all distinct centers separated by a fixed delta>0.
3. The unweighted normalized pure exponentials exp(i lambda x), indexed by Lambda on L²(0,1), have no positive uniform Riesz lower bound.

Proof of1. A sequence with gap at leastdelta has at most1+T/delta points in any positive interval of lengthT. A finite union has O(T) points. The rescaled zero count grows as a positive constant times T log T, a contradiction. Repeated ordinates must be assigned multiplicities, so they cannot evade the count.

Proof of2. Every cluster meeting[0,T] has a center in[-R,T+R]. Uniformly separated centers in that interval number O_(delta,R)(T). With at mostq members per cluster, total count is O_(q,delta,R)(T), contradicting T log T. This argument does not require the clusters to have equal size or any particular ordering.

Proof of3. If ordinates repeat, the corresponding exponentials are identical and the lower bound already fails. Otherwise, unbounded average density forces arbitrarily small gaps between two ordinates: a positive global minimum gap would imply O(T) counting. For two distinct frequencies lambda,mu,

||exp(i lambda x)-exp(i mu x)||²_(L²(0,1))
 <=|lambda-mu|² integral_0^1 x²dx=|lambda-mu|²/3.

The coefficient vector(1,-1) has squared norm2. A uniform Riesz lower boundA>0 would require2A<=|lambda-mu|²/3 for every such pair, which is impossible as gaps tend to zero.

## What this excludes and what remains possible

The round2 finite-cluster theorem fixes m and a scaled diameter bound, while the block theorem additionally requires quantitative phase separation. These assumptions cannot simply be imposed globally on the entire fixed-rescaled zero multiset. Local collision stabilization does not remove its unbounded density.

This does not rule out growing clusters with quantitatively controlled constants, weighted systems, variable-height unfolding, non-Riesz frames, or different Hilbert spaces. Those alternatives require their own theorems. In particular, a height-dependent unfolding that gives roughly constant local density is a nonlinear change of frequencies and is not the same global exponential system; existing fixed-frequency Gram bounds cannot be reused without checking the changed kernels and measure.

The necessary next arithmetic/spectral step is now concrete: if one wants to use divided differences for all zeta zeros, state how cluster size, diameter, weights, observation interval, and frame constants vary with height, and prove a summable global estimate. A fixed-q compactness argument cannot supply that estimate.
