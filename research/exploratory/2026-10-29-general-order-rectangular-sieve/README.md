# A proposed conjugate-pair rectangular sieve at order n

**Status:** Source-dependent proof blueprint, not a new zero-free theorem. The argument replays [De Faveri Proposition 8.1](https://arxiv.org/abs/2610.04045v1) with a different order and imports his finite-ray reciprocity, root-number splitting, Poisson and tail estimates, together with Theorem 1.1 and Lemma 6.1. The source explicitly states Proposition 8.1 only for n=3; the extension below is not a verbatim source theorem. Full independent review of the replay, particularly its uniformity and all masks, is required. No priority claim is made.

Fix n≥3 and K containing μ_n, with the source's fixed bad set S and n-th-order family. For A,B,Q≥1 put M=min(A,B), N=max(A,B). The proposed estimate is

    Σ_{a≈A,b≈B} |Σ_{q≈Q, q squarefree} λ_q χ_q(a b^(n−1))|²
      ≪_ε (ABQ)^ε [ AB + M^(1−1/n)N^(1/n) Q
                              + M^(1/n)N^(1−1/n) Q^(2/n)] Σ_q|λ_q|².   (1)

All ideals are good; q coefficients are arbitrary and the source zero masks are retained. The dyadic notation and constants are those of the source. At n=3 this is exactly Proposition 8.1. The squarefree restriction on q is essential to the following short root-number separation; no extension to arbitrary q is claimed.

## Source replay and the additional term

Because χ_q has order dividing n with the zero extension,

    χ_q(a b^(n−1))=χ_q(a) overline(χ_q(b)).

Interchanging A and B and conjugating the entire coefficient vector λ leaves the squared sum unchanged, including collisions; the coefficient norm is unchanged. Thus the operator-norm bound is symmetric, and we may take A≤B. The opening, gcd decomposition, finite ray-class partition and diagonal `≪(ABQ)^ε AB` are the same as De Faveri §8. His Lemma 3.3 is stated for general n: after the q-indices are made coprime and lie in one fixed ray class, it gives the product-character root number as an η times β_q1 conjugate(β_q2), multiplied by factors involving their sharp parts. The q-indices here are squarefree, so the sharp parts are units, and η depends only on the fixed class. The root number therefore separates exactly as in the cubic proof. The Poisson-transformed q-character again appears at the product a·e; the exponent n−1 has been used only to obtain the conjugate on b.

At the point corresponding to source (8.3), the unrestricted-good-row, n-power-free-column sieve from [the general-order corollary](../2026-10-29-general-field-collapsed-sieve/README.md) supplies

    L₂(X,Y) ≪ (XY)^ε [ X + X^(1/n)Y
                          + X^(1−1/n)Y^(2/n)
                          + X^(2/n)Y^(1−1/n) ].             (2)

This is also obtainable from De Faveri Theorem 1.1 and Lemma 6.1. It is essential that q is squarefree: (2) may enlarge that inner support to n-th-power-free ideals, but does not discard its original zero masks.

The source's dual scale is `X≈A Q² R/(B D²)`, `Y≈Q/D`, and its outer prefactor is `BD/(QR)`, with `1≪R≪D≪Q`. Inserting the four terms of (2), and using D,R≥1 exactly as in the source's divisor summation, yields the off-diagonal upper bound

    AQ + A^(1/n) B^(1−1/n) Q^(2/n)
       + A^(1−1/n) B^(1/n) Q
       + A^(2/n) B^(1−2/n) Q^(3/n),                         (3)

apart from the permitted small powers. The first term is dominated by the third because A≤B. The last term requires a genuine case split: its ratio to the second term is `(AQ/B)^(1/n)`, and its ratio to the third is `(B/(AQ))^((n−3)/n)`. Hence it is at most the second if Q≤B/A, and at most the third if Q≥B/A. This proves the algebraic reduction from (3) to (1), **provided** all source Poisson, sector, mask, tail and summation steps transfer as described. At n=3 the last two terms coincide.

## Balanced boxes and the conditional detector consequence

Put U=AB, A≤B, A=U^γ with 0≤γ≤1/2 and Q=U^r. With a normalized squarefree Möbius coefficient vector, (1) would give inverse second-moment exponent

    E_(n,γ)(r)=max{1, r+[1+(n−2)γ]/n,
                       2r/n+[(n−1)−(n−2)γ]/n}.

For every r≥1/2, both nontrivial affine terms are at most `1/2+r`: the second by γ≤1/2, and the third because `1−1/n+2r/n≤1/2+r`. Thus the fixed-type t=1 saturated-detector argument in [the cubic note](../2026-10-29-cubic-conductor-detector/README.md), if replayed with the n-th-order family and this estimate, would give the same conductor-ordered density exponent `5/2−2σ` for `3/4<σ<1` at a sufficiently small polynomial height.

That density statement concerns only the restricted conjugate-pair subfamily g=a b^(n−1), with a,b squarefree and coprime; for n>3 it does not cover all n-th-power-free indices. A fixed unitary twist is allowed only after its coefficient, conductor, and detector profile uniformity are verified as in the cubic case. Prime-label characters give a family-size lower bound, but no individual zero-free half-plane follows. The rectangular extension, the detector transfer, and novelty relative to other fixed-order density work all remain unverified.
