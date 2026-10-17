# Attempted upgrade, actual result, and source boundaries

## 1. The attempt and the point at which it fails

The intended improvement was to replace #955's width T comparable to X^k by a
shorter window, keeping native Mobius rather than an arbitrary coefficient
class. This would have been useful only with careful center/height constants.

Theorem 1 proves that a bound UNIFORM IN EVERY REAL CENTER cannot benefit from
that coefficient restriction: its exact worst-center functional is the unsigned
one. This is stronger than the older changed-coefficient counterexample. The
obstruction survives the complete Gaussian and actual sixth-power nonunit masks;
it is not a finite arbitrary-phase example transplanted to an uncontrolled row.
The finite-height price for the centers is displayed rather than suppressed.

There are two distinct restrictions that a viable upgrade must retain:

* Ordinary Mellin centers must be fixed or their dependence must be priced.
  Native arithmetic alone is insufficient when a constant is uniform over all t0.
* A generic sextic large-sieve operator bound cannot simply be assumed diagonal.
  A recently posted primary source gives actual superdiagonal norm lower bounds.

Neither restriction supplies the fixed-center signed estimate. This pass does
not claim that ruling out a shortcut is the requested improved upper bound.

## 2. The literal arithmetic target is unchanged

For the principal native Gaussian source over K=Q(omega), write the cumulative
second energy as Delta_norm(D)+C_neq(D), where Delta_norm contains ALL pairs of
ideals with the same rational norm, and C_neq contains all unequal rational norms.
With beta=2c-1, the existing exact kernel is

    K_D(v,z)= exp(beta^2/2)/(2 sqrt(2pi*v*z))
      *exp[-log(v/z)^2/8]*Phi(log D-log(v*z)/2-beta).

Thus

    C_neq(D)=sum_(NI != NJ) mu_K(I)mu_K(J)K_D(NI,NJ),

with the original exclusions. #954 bounds Delta_norm by O(log^2 D). The
all-epsilon signed upper bound C_neq(D)<=C_epsilon D^epsilon is still open at
center zero; its critical-energy significance is already recorded in #952.
This is a restatement of the remaining source, NOT a new reduction proved here.
The torus result does not turn large-center lower bounds into a statement about
C_neq at zero. Its conclusion is precisely that the center cannot be discarded.

## 3. A new external source inspected during this pass

Yuanda Xu and Hejian Sang, *A sharp lower bound for the sextic large sieve*,
arXiv:2610.17675v1, posted October 13, 2026:
https://arxiv.org/html/2610.17675v1

Read: introduction, Theorem 1.1, Corollary 1.2, normalization, and the described
squarefree-projection/row-transfer mechanism. This is not an independent proof
review of the whole paper. It asserts a lower bound A^(5/6)B^(1/3), up to arbitrarily
small powers, when B^(16/11+delta)<=A<=B^(2-delta), with squarefree indices on
both sides. Its full-cutoff diagonal consequence is X^(17/16-epsilon), not the
same lower bound for an X-by-X dyadic annulus and not a lower bound for native
Mobius coefficients. The row-transfer step may change its witnessing vector.

This external theorem is a strategic warning only. NONE of its analytic
claims, or the Dedekind quasi-RH theorem, is a premise of THEOREMS.md.
No full paper/PDF/Lean source is claimed imported or rebuilt in this packet.

## 4. Internal source identities and credit

- #955, 20883bec3d5b939d7602beaf2c91dbf102669166,
  standalone/2026-10-17-transport-moments/THEOREMS.md:
  original complete long-twist bounds, physical/twist distinction, and the
  unsigned-profile obstruction. The complete local source packet was inspected
  and its checker replayed, matching its archived 35,555 predicates. The stored
  THEOREMS.md blob is 506ed062d562b4b2d3d339330ed95289cf00be0e.
- #954, 3241178607671c4dd979cefdad0670fd426194da:
  full norm-collision block and Gaussian mean, read through the detailed live PR
  description and preceding source context, not independently reproved here.
- #953, a93d382951f8fac7b0c28783061a7ddb99fcf0a4:
  THEOREMS.md Sections 1-3 freshly read through GitHub, particularly literal
  masks and incomparable reduced cores. Later source sections were truncated
  in that fetch and are not claimed freshly read in full.
- #952, 3b7d2948840446c752bbf284f6f90f6592395a29:
  exact Gaussian energy and fixed-center target, inspected at live PR-description
  scope and inherited source context. The kernel is not a new discovery here.
- Previous local norm-fiber packet: all fourteen bytesets preserved in the
  download companion; its 34,361-predicate checker was replayed in normal and
  optimized Python. That old packet is NOT newly pushed or integrated by this
  continuation. The earlier ramified packet is already recorded as recovered
  on #954. No recovery action is fabricated.

Classical inputs/methods: Galois residue-degree equality, unique ideal and
rational-prime factorization, norm-Euclidean Eisenstein arithmetic, lattice/ideal
counting, Fourier polynomials and torus approximation, finite Euler densities,
Holder/Jensen, Gaussian Fourier transform, and elementary Taylor remainders.
The crucial approximation and two-variable density are proved in full here.
The Gaussian uses only classical fixed-field ideal counting. No RH/GRH,
quasi-RH, hidden inverse-zeta estimate, large-sieve theorem, or unproved native
moment is used in the new theorems.

The contribution is this specified source-faithful hull/energy/replica statement
relative to the inspected packets, not global novelty for almost periodicity,
Kronecker approximation, or counting squarefree coprime pairs.
