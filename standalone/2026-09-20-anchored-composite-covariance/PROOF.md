# ACC29: zero-anchored composite covariance

20 September 2026. **PROPOSED component proofs; independent mathematical review required. No RH proof or complete native covariance bound.**

This packet records the preceding in-chat pass, rather than only its last formula. It is additive on #904 at `879497b4f11be2618c448efc1fa93f69b4022e4c` (NCG28). Earlier references were #904 at `4e8dea7004874d1a9c679b58db1dca1fbb539388`, #848 at `7de75c02417d5d8db7eafb1ceba364380e72d16a`, and #903 at `36ffd15df96866a3f1c4f306000dd4a4dbf4153b`. No canonical status, trusted formal source, or predecessor is changed.

## 1. Motivation and coordinates

The question was whether the recent physical Newton/Fourier work could yield an actual bound on composite covariance, without assuming prime/composite orthogonality or dropping the compensating zero mode. These coordinates differ from RCB26's centered harmonic rough-parity blocks. The bounds below concern selected functions summed BEFORE squaring, including all internal covariance and the whole physical tail.

Let c be a finite real source supported in [1,L], L>=2, with |c(n)|<=K and sum c(n)/n=0. Set

    z=c*c, v=2c-1*z, A_c(k)=sum_(n<=k)c(n), V(k)=sum_(n<=k)v(n),
    S=sum c(n), U_d=sum_(d|n)c(n)/n,
    B_q=sum_(q|n)z(n)/n,
    T_d(k)=(d-1)/2-(k mod d),
    R_q(k)=sum_(d|q)mu(q/d)T_d(k), q>=2,
    r_q(k)=R_q(k)-R_q(0),
    ||f||_ph^2=sum_(k>=1)f(k)^2/[k(k+1)], H_L=sum_(n<=L)1/n.

All coefficient sums are finite; B_q=0 for q>L^2. Dirichlet convolution is ordinary, not additive.

## 2. Exact zero anchoring

R_q(0)=phi(q)/2. Since sum_(q|n)phi(q)=n,

    sum_(q>=2)B_q phi(q)=sum_n z(n)(n-1)/n=S^2.

Here sum z(n)/n=(sum c(n)/n)^2=0. DSE27's identity therefore becomes

    V(k)=2A_c(k)-sum_(q>=2)B_q r_q(k).                  (A1)

Equivalently r_q(k)=-sum_(d|q)mu(q/d)(k mod d); inserting the divisor sum directly proves (A1) from V=2A_c-sum z(d)floor(k/d). No zero mode is discarded.

For a prime power,

    r_(p^h)(k)=-p^(h-1)*(floor(k/p^(h-1)) mod p),
    |r_(p^h)(k)|<=min(k,p^h).                          (A2)

The unanchored p^2 mode starts at (p^2-p)/2, whereas its anchored version is zero until k=p. Thus large unanchored offsets can require cancellations which (A1) has already performed exactly.

## 3. Entire prime-power sector

Put U_j=U_(p^j) and U_0=0. Partitioning one convolution factor by its p-adic valuation gives

    B_(p^h)=sum_(j=1)^(h-1)U_j U_(h-j)
                -sum_(j=1)^h U_j U_(h+1-j).           (A3)

One derivation uses exact valuation layers U_j-U_(j+1), and thresholds in the second factor; the terms involving U_0 vanish by balance. In particular B_p=-U_p^2 and B_(p^2)=U_p^2-2U_p U_(p^2). Since |U_j|<=KH_L/p^j,

    |B_(p^h)|<=K^2 H_L^2[(h-1)/p^h+h/p^(h+1)]
                 <=2h K^2 H_L^2/p^h, h>=2.           (A4)

For primes, ||r_p||_ph^2<=2p, so Minkowski and sum_(n>=2)n^(-3/2)<=2 give

    ||sum_p B_p r_p||_ph^2<=8K^4 H_L^4.               (A5)

For higher powers, A(t)=sum_(p^h<=t,h>=2)h<=64 sqrt(t). Indeed squares cost at most 2sqrt(t), and h>=3 cost at most t^(1/3)(log_2 t)^2; the ratio of this expression to sqrt(t) is bounded by 144 exp(-2)/(log 2)^2<41. Restricting to p^h<=L^2 preserves this bound and also gives A(t)<=64L. Partial integration gives

    sum_(p^h<=L^2,h>=2)h min(1,k/p^h)<=128sqrt(k),

and the same sum is at most 64L for k>=L^2. Equations (A2)-(A4), then the physical weight, yield a constant times K^4 H_L^4(1+log L) for this whole sector. Combining with (A5),

    ||sum_(q=p^h<=L^2)B_q r_q||_ph^2 << K^4 H_L^5.    (A6)

All prime-power cross terms are included. The constant is absolute; no prime distribution theorem is needed.

## 4. General sparse-denominator lemma

For every q>=2,

    |B_q|<=K^2 H_L^2 tau(q)/q,
    |r_q(k)|<=2^omega(q)min(k,q).                      (A7)

For the first estimate, partition r by g=gcd(r,q). Divisibility q|rs forces q/g|s; dropping the gcd restriction costs at most KH_L/g times KH_L/(q/g) per divisor g. The second estimate follows from the nonzero terms in the divisor expansion of r_q.

For D subset [2,L^2], define

    A_D(t)=sum_(q in D,q<=t)tau(q)2^omega(q).

Suppose A_D(t)<=D0 sqrt(t) for all t>=1. Then

    |sum_(q in D)B_q r_q(k)|
      <=K^2 H_L^2 k integral_k^infty A_D(t)/t^2 dt
      <=2D0 K^2 H_L^2 sqrt(k).

For k>=L^2 use A_D(L^2)<=D0 L instead. Split the physical norm at L^2, use sum_(k<L^2)1/(k+1)<=2log L, and sum_(k>=L^2)1/[k(k+1)]=1/L^2. Thus

    ||sum_(q in D)B_q r_q||_ph^2
      <=D0^2 K^4 H_L^4(1+8log L).                    (A8)

This holds for EVERY subset dominated by the counting bound, not merely a complete structured family. It is a bound on the combined function, not a covariance diagonal.

## 5. Powerful denominators and a growing prime bank

An integer is powerful when each prime exponent is at least two. Every powerful q is uniquely a^2 b^3 with b squarefree. Submultiplicativity and the prime-power inequality

    2(2e+1)<=binom(e+5,5), e>=1,

give tau(q)2^omega(q)<=d_6(a)8^omega(b). Since sum_(a<=X)d_6(a)<=X H_floor(X)^5,

    A_powerful(t)<=sqrt(t) H_L^5
          *sum_(b squarefree)8^omega(b)/b^(3/2)
       <=3^8 sqrt(t)H_L^5.                            (A9)

For t>L^2, use the count at L^2. The Euler sum is at most zeta(3/2)^8<=3^8. Therefore

    ||sum_(q powerful,2<=q<=L^2)B_q r_q||_ph^2
       <=3^16 K^4 H_L^14(1+8log L).                   (A10)

For a finite prime bank S, admit q when every exponent-one prime belongs to S. Such q uniquely equals s*a with s a squarefree divisor of product_(p in S)p, a powerful, and gcd(s,a)=1. The weighted counting bound gains only

    Pi_S=product_(p in S)(1+4/sqrt(p)).

Hence every subset of this enlarged family satisfies

    ||sum B_q r_q||_ph^2
       <=3^16 K^4 H_L^14 Pi_S^2(1+8log L).             (A11)

Taking S={p:p<=y} with y=(log L)^2 yields L^o(1). To justify the little-o explicitly, the elementary Chebyshev bound pi(t)<<t/log t, split into dyadic intervals (with the initial range separated), gives sum_(p<=y)p^(-1/2)<<sqrt(y)/log y. Thus log Pi_S=O(log L/log log L). RCB26 contains the same elementary prime-sum ingredient; no PNT is used. Small L can be absorbed into an absolute constant.

Combining this family with the entire prime sector leaves only composite q with at least two distinct prime factors and some exponent-one prime p>y. It does not assert that these remaining modes are small or approximately independent.

## 6. Native completion, tail transport, and the actual remaining target

For the actual source preserve mu(n) through Y, then successively take a correction of sign opposite the reciprocal residual and magnitude at most 3 until it is zero. The inherited PCR26 proof, rederived in NCG28, gives L<=2Y and

    J(c)=sum_(k>=1)m_c(k)^2<=2F_Y,
    m_c(k)=sum_(n<=k)c(n)/n, F_Y=sum_(k<=Y)m(k)^2.

The innovation isometry gives ||A_c||_ph^2=J(c). Native Newton reproduction holds strictly below (Y+1)^2. For b=Y+1, B=b^2-1, and a partition into paid fixed anchored modes G and the remaining anchored modes R,

    sqrt(F_B)<=||V||_ph<=2sqrt(2F_Y)+||G||_ph+||R||_ph. (A12)

This is a sufficient full-norm route, not a claim that controlling the entire artificial Newton future is necessary.

NCG28 supplies the sharper exact adapter

    (TP)(k)=P(k)/(k+1)-sum_(j>k)P(j)/[j(j+1)],
    sum_(k>=b)(TP)(k)^2
      =sum_(j>=b)P(j)^2/[j(j+1)]
          -b*(sum_(j>=b)P(j)/[j(j+1)])^2.              (A13)

In particular T is a contraction and annihilates a constant sequence. Therefore

    T r_q=T R_q                                             (A14)

for each fixed denominator. Anchoring changes a physical upper bound, NOT the actual fixed-sector innovation component. The paid families in (A6),(A11) have subpower transformed energy too.

NCG28's low/moving window bound can be applied to the complement of this FIXED paid family because its finite-block estimate permits arbitrary subsets. Keep that window in NCG28's ORIGINAL unanchored coordinates and keep all its future-activation corrections. Switching an activated raw R_q to r_q is not free: the masked constant is no longer constant and T need not annihilate it. With this convention the two packets are compatible, not duplicate decompositions silently combined. The open target is the RESTRICTED transformed high-composite complement on b<=k<=B, with exponent below two in F_Y and allowable losses.

## 7. Signed prime towers and squarefree mixed squares

For q>1, gcd(p,q)=1, j>=1,

    r_(p^j q)(k)=p^j r_q(floor(k/p^j))
                    -p^(j-1)r_q(floor(k/p^(j-1))).    (A15)

This follows by writing k mod(p^j d)=p^j(floor(k/p^j) mod d)+(k mod p^j); the residue terms independent of d cancel. With B above support equal to zero, finite summation by parts gives

    sum_(j>=0)B_(p^j q)r_(p^j q)(k)
       =sum_(j>=0)p^j[B_(p^j q)-B_(p^(j+1)q)]
                            r_q(floor(k/p^j)),         (A16)
    B_(p^j q)-B_(p^(j+1)q)
       =sum_(q|n,v_p(n)=j)z(n)/n.

Do not sum independent pivot decompositions on top of one another: use one pivot or a disjoint recursive hierarchy.

For the UNCOMPLETED truncated Mobius prefix define

    C_q(X,Z)=sum_(r<=X,s<=Z,p does not divide rs,q|rs)mu(r)mu(s)/(rs).

Only valuation layers j=0,1,2 occur, so the right side of (A16) is exactly

    C_q(Y,Y)r_q(k)
      -2C_q(Y,Y/p)r_q(floor(k/p))
      +C_q(Y/p,Y/p)r_q(floor(k/p^2)).                  (A17)

Floors in the real cutoffs are understood. The different cutoffs cannot be replaced by one common coefficient. For completed sources (A16), not the three-layer simplification, retains every completion contribution.

For squarefree q and a_d=sum_(n<=L,gcd(n,d)=1)c(n)/n, inclusion-exclusion gives

    B_q=sum_(d|q)mu(d)a_d^2.                           (A18)

Thus for distinct primes p,r, using balance,

    B_(pr)=(U_p+U_r-U_(pr))^2-U_p^2-U_r^2.            (A19)

There is no forced sign. On the native prefix U_d=mu(d)m_d(Y/d)/d for squarefree d, plus the ACTUAL completion tail; m_d is the reciprocal Mobius sum excluding primes dividing d. This makes the coupled mixed-cutoff objects an arithmetic continuation target, not a generic random-vector assertion.

## 8. Validation and preserved prior diagnostics

`python verify.py` and `python -O verify.py` are the replay commands. The new checker uses exact Fraction/integer arithmetic: 81 balanced sources; zero-mode cancellation; full anchored output; valuation amplitudes; squarefree identities; tower telescoping; kernel bounds; native coefficients through the strict Newton endpoint for Y=3,7,15,31,63,95; and a dilation cell identity. Y=95 has TWO completion coefficients, ending at L=97. The fresh report records 96,190 exact comparisons. An exception, not an optimizable Python assert, implements each test.

The preceding chat reported 70,212 comparisons from a different, unrecovered implementation and floating annular energies:

|Y|raw prime-square|anchored prime-square|anchored all prime powers|
|--:|--:|--:|--:|
|15|0.018773|0.031678|0.055310|
|63|0.146952|0.027090|0.029890|
|255|0.527508|0.020008|0.020794|
|1023|1.594395|0.013608|0.013942|

These historical rounded diagnostics are preserved for completeness, NOT claimed as newly reproduced or interval-certified. Anchoring need not reduce every sector norm. No asymptotic claim is inferred from this table.

No full checkout was available: direct Git failed DNS resolution; the authenticated connector supports additive publication. No whole-repository validator, remote CI, Lean build, independent review or full predecessor campaign was run. Same-author finite checks cannot certify an infinite analytic proof.

## 9. Attribution and status

Short-source Newton/Mertens inversion is classical: M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Mobius function*, arXiv:1807.05890 (2018), https://arxiv.org/abs/1807.05890, abstract checked this pass. Finite Ramanujan expansions, Euler-factor deletion, divisor counting and weighted Hardy/innovation algebra are classical tools. This packet claims a proposed component composition, not externally established novelty. The exact assumptions and proof of every new estimate used here are given above.

Established in manuscript: (A1)-(A19), under their stated hypotheses. Finite-replayed: identities and native examples in verify.py. Not established: a bound for the remaining rough high-composite native covariance, a uniform Newton scale gain, RH, or any percentage of RH.
