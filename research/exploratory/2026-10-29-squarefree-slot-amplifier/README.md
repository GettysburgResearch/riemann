# Removing collisions from a spiked prime-slot amplifier

Status: elementary exact lemma and proposed research interface; no new zero-free theorem. Novelty has not been established. Scope is fixed-degree physical prime-slot polynomials; this is not an improved sextic large-sieve or selected-norm estimate.

## Lemma

Let `P>=2`, and let `Q= sum_{i in I} a_i z_i`, where the finite index set has `#I <= C P`, `|a_i| <= C P^(-1/2)`, and `|z_i|<=1`. Let

```
E_k = sum_{(i_1,...,i_k) in I^k, all distinct} product_{j=1}^k a_(i_j) z_(i_j)
```

be the ordered distinct-index part of `Q^k`. For each fixed integer `k>=2`, if `|Q|>=P^g` for a fixed `g>0`, then

```
E_k = Q^k * (1 + O_{C,k}(P^(-2g))).
```

The statement is complex-valued and holds uniformly in the choices of `z_i`, including zeros. Hence for sufficiently large `P`, `|E_k| >= |Q|^k/2`. Degree `k=1` is exact.

## Proof

Write `b_i=a_i z_i` and `S_j=sum_i b_i^j`. Then `S_1=Q`, while for every `j>=2`,

```
|S_j| <= C^(j+1) P^(1-j/2) <= C^(j+1).
```

The partition-lattice inclusion–exclusion identity is

```
E_k = sum_{pi partition of {1,...,k}} mu(pi) * product_{B in pi} S_|B|,
mu(pi) = product_{B in pi} (-1)^(|B|-1) (|B|-1)!.
```

The discrete partition into `k` singleton blocks contributes `Q^k`. Every other partition has at most `k-2` singleton blocks; each remaining factor is bounded by a constant depending only on `C,k`. Since `|Q|>=P^g>=1`, the sum of all remaining finitely many terms has magnitude `O_{C,k}(|Q|^(k-2))`. Divide by `|Q|^k` to get the displayed relative error. No sign, phase, coprimality, or distribution assumption is used.

## Application interface

In PR94's physical setup the normalized prime slot is a finite sum with one term per prime ideal in a fixed annulus, coefficient size `O(P^-1/2)` up to bounded profile and norm-power factors, and a zero-extended residue character value of modulus at most one. An amplitude bin with `|Q| >= P^g` and fixed `g>0` therefore admits replacement of any *fixed* slot power by its ordered pairwise-distinct prime sum without losing the spike, after increasing the fixed lower threshold. For a finite system of slots with disjoint original prime supports, do this independently in each slot; products remain squarefree across slots. The degree, number of slots and positive spike margins must be fixed before the large parameter grows. If their bounds or the minimum spike margin are allowed to vary, the implicit constant and threshold above require new control.

A source application must preserve all original character twists and masks, common profile and height uniformity, and the order in which the finite slot system and losses are chosen. A bound on the resulting squarefree tensor amplifier is not proved here. In particular Xu's reported lower bound for a sextic matrix with squarefree indices means that squarefree support alone does not defeat the large-sieve obstruction. The prospective target is a stronger estimate that uses the actual tensor structure *and* its correlation with selected physical rows, rather than merely replacing arbitrary coefficients by arbitrary squarefree coefficients.
