# Independent reconstruction of the proposed global pair transport

Reviewer: the Eisenstein-probes sprint agent, independent of the rational
agent's construction. This is a mathematical component review, not a
repository acceptance or exact-final-commit review.

Reviewed `../rational/GLOBAL_TRANSPORT.md`, SHA256
`3b455ff7541c4fae9ed07a8f63f37a1e5e875865880128af63894c8d0beb5d94`,
and the full proof of `../reviews/TRANSPORT_KERNEL.md`, SHA256
`1adf7854b2b44a817c27feb03ad793a4f842c2088a1ace877ca30a4200efc815`.
Also reconstructed the underlying R/S_q identity and the Abel/geometric
Gram argument in rational/PROOF.md sections 1 and 6.1. Later edits are
outside this hash-specific receipt until checked again.

**Finding:** no blocking error found in the proposed component theorem.
It supplies a concrete global removal of every top-prime-pair denominator
at subpower coherent energy, in the declared pair-weighted probe class.
It does not bound the complete complementary source or improve a zeta
zero-free boundary. The following are the load-bearing checks.

1. The primary [Tolev paper](https://arxiv.org/pdf/math/0505326), version
   math/0505326v1, Theorem 3 on the third PDF page, states an actual uniform
   asymptotic for Q_l(x,h). It is not merely an existence or averaged
   result. At r=1,l_1=0 its hypotheses hold for psi(x)=(log x)^(1/2),
   h=ceil(Y^(1/5+eta)), x comparable with Y, for all sufficiently large Y.
   Its 6/pi^2 density exceeds 3/5. Applying it separately on the two
   contiguous factor intervals leaves at least H/5 common squarefree
   indices by inclusion-exclusion. No squarefree-pair correlation theorem
   is being inferred.

2. For N=pl and r=floor(sqrt N), B-N lies between r+2 and 3r+2.
   Taking k0 maximal with k0(k0+1)<=B-N makes the first gap O(sqrt Y).
   The next H indices have gap O(sqrt(Y)H), both factors <=Y in the stated
   interior range, and |a-b|<=7sqrt Y. The odd sum a+b guarantees an even
   reference product, including every shared factor.

3. Every target N is distinct. A fixed reference pair receives targets
   only in its 2G+1 integer neighborhood, each with probability <=5/H.
   This proves a fractional load O(sqrt Y) with no Hall matching input.
   Since N>=Y^2/4, its aggregate reference coefficient is O(Y^(-3/2)).
   Multiplication back by ab gives the claimed old-input weight cap.

4. An old input divisible by a prime p>Y/2 must equal p. A product of
   two old inputs divisible by distinct top primes p,l must therefore be
   exactly pl and odd. Thus no even reference product is divisible by pl.
   The retained coefficient 2/(pl) is a canonical denominator response,
   not merely the coefficient of one R-dilate. Reference products may
   have repeated factorizations; all counts are explicitly at pair level.

5. In the complete kernel, the log x and Euler constants cancel. On the
   full native physical range, only harmonic jumps j<=16 can occur.
   For each fixed x,j, every contributing distinct target lies within G
   of x/j. Summing reference probabilities rather than their multiplicity
   gives the pointwise O(G/Y^2) bound. The zero total R coefficient makes
   this an actual integer-cell step source. No individual-mode L2
   triangle bound has replaced the coherent kernel.

6. For q=r^2s and s=uvw, the reference divisibility spacings are
   A=ruw and B=rvw, so AB=q w. Counting in both orientations gives
   `2Y B0/(q w)+min(Y/A,Y/B)`. Retaining this minimum is essential.
   Since w max(u,v)>=sqrt(s), its contribution is exactly of the size
   `d_3(s)[1/q+1/(sqrt(Y)sqrt(q))]` after the pair coefficient cap.
   This includes primes shared by both references; no coprimality
   condition has been used to manufacture a saving.

7. Squaring the coefficient bound, using d_3(s)^2<=d_9(q), and summing
   d_9 by elementary divisor counting gives the complete resource
   `(Q+Q^2/Y)H_Q^8`. The Abel remainder for arbitrary fixed coefficients
   of resource B is at most O(BQ^3/K^3) in squared norm. For Q<=K this
   is absorbed by the displayed Gram estimate. Its moving native cutoff
   is handled separately on every annulus; the coefficients themselves
   stay fixed in the physical output.

8. The four annular powers are K^(rho-1), K^(3rho-2),
   Y^(-1)K^(2rho-1), Y^(-1)K^(4rho-2). The first two decrease and the
   latter two increase. On Y<=K<=O(Y^2), their total is bounded by
   `[Y^(3rho-2)+Y^(8rho-5)]` times a fixed log power. Thus the stated
   restriction rho<5/8 is exactly sufficient, including the final
   shortened annulus.

9. For the small-core sector, every squared-prime part r divides both
   distinct references, hence r<=|a-b|<=B0. Multiplication of the
   coefficient resource by the full global norm sqrt(3q)beta(q) gives
   the two complete r resources `sum beta(r)/r` and
   `Y^(-1/2)sum beta(r)`. Both are paid by expanding beta over squarefree
   divisors. The remaining s sum is bounded by d_6(s), giving precisely
   `H_S^5[sqrt(S)H_Y+S]`. This remains valid with all actual annular/core
   indicators because each individual global root norm majorizes its
   restricted norm.

10. The omitted corner contains O(Y) integer pairs. Each coefficient
    2/(pl) times its full S_(pl) norm is O(1/Y), so the coherent boundary
    cost is O(1). Top-prime-pair denominators pass every actual rough mask
    for large Y. Consequently the final subtraction removes every one
    throughout the complete native step.

One minor scope clarification was communicated to the author: the boundary
S_(pl) addition can itself be realized by the old pairs (1,1), (p,1),
(l,1), (p,l), using `S_(pl)=R(x/(pl))-R(x/p)-R(x/l)+R(x)`.
Its accumulated input weights satisfy the same O(sqrt Y) cap (indeed
smaller). The displayed initial W formula describes the interior
transport; spelling this out makes the final enlarged compensator's
pair-source status equally concrete.

The important limitation is already stated accurately by the author:
the reference redistribution can change original aggregate coefficient
zeros. It is a legal enlarged pair-weighted source, not a bounded
per-denominator multiplier of the native source. The remaining signed
complement retains the full unproved arithmetic task.

## Exact-byte refresh, 2026-10-18

The final source SHA-256 is
`8d18b680cbc1287862e004cfb2a2afb95eae99c75299852184e7409d36a7c407`.
The only addition relative to the reviewed bytes is the paragraph in
Section 8 realizing the boundary addition with `(p,l),(p,1),(l,1),(1,1)`.
I independently read that paragraph and checked the expansion and its
coefficient count: the `(1,1)` coefficient is O(1/Y), while each fixed
`(p,1)` coefficient is O(Y^(-1/2)). This is exactly the scope clarification
requested above. It does not alter the theorem, the complete boundary
root bound, or the unestimated complementary source. No new blocking
issue was found in this refresh.
