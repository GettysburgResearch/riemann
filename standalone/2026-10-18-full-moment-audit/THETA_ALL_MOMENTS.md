# Full even moments of the actual reflected theta rows

Status: PROPOSED complete deduction from the explicitly adopted CT reflection
and quadratic-family large sieve. Independent mathematical review required.
No RH, GRH, inverse-L moment, or signed native-covariance hypothesis is used.
The analytic inputs are named below; they are not proved by the finite checker.
All integer orders k are FIXED. Constants may depend on k and every requested
loss/decay exponent. This is not uniformity for k=k(N).

## 1. Objects and theorem

Use the exact CT field F containing mu_12, its admissible fixed finite S,
R=O_(F,S), Gamma=(R*)^6, allowed generators, original profiles and theta row
B_m(Z). The notation is the recovered short-support packet, source subtree
`a80cb7e2404e0f6835c47017597b6acbeb9cb264`, REFLECTED_MOMENT.md. Its full
text was read. The CT primary body was not freshly obtained in this pass.
The source interface is adopted at that pinned scope, not inferred from a
PR title or from CT's long-support corollary.

For a fixed compact B inside F_S^times, let M(N)=R intersect ell_N B, N>=2,
where ell_N has module N. These are finite balanced element sets, not all
norm-bounded elements in a field with infinite units. No row m=0 occurs.
For m in this set write uniquely

    mR=h d,   h powerful, d squarefree, (h,d)=1,

and put q_a=N a for exterior integral ideals. Bounded generator multiplicity
in M(N), and the finite S-type list, are kept throughout. Deleting a subset
of rows in the positive moment is permitted; no signed physical sum is
replaced by a different source.

**Theorem T (every fixed even order, complete reflected tails).** For any
integer k>=1, epsilon>0 and A>0, the original rows satisfy, for P,D,Z>=1
with Z>=2 and q_h~P, q_d~D,

    sum_m |B_m(Z)|^(2k)
      << (PD)^epsilon P^(1/2) [D+(D^2 P/Z)^k]
                                    min(1,(D^2 P/Z)^A).       (T1)

Dyadic endpoints differing by fixed constants only change the implied
constant. In particular, for N,Z>=2,

    sum_(m in M(N)) |B_m(Z)|^(2k)
      << N^epsilon [N+(N^2/Z)^k] min(1,(N^2/Z)^A).             (T2)

The weaker form without the final minimum is often more convenient. Every
original squarefree c, cube n, ramified auxiliary ideal, common-prime zero,
local class and Gaussian/profile tail is included. For k=1 this recovers
(and at very short support sharpens) the earlier two-term estimate. It is
not an assertion about the native inverse-L/Mobius moment.

A useful range consequence is

    sum_(m in M(N)) |B_m(Z)|^(2k) << N^(1+epsilon)
    whenever Z >= N^(2-1/k).                                (T3)

At fourth order and N=Z^(2/3), (T2) gives O(Z^(2/3+epsilon)), versus the
O(Z^(1+epsilon)) bound obtained from the old second moment and the direct
pointwise estimate. The exponent approaching 1/2 in the equivalent support
condition N<=Z^(k/(2k-1)) is a PHYSICAL SUPPORT exponent, not a zero location.
No zeta zero-free line is asserted by (T3).

## 2. The exact imported reflection and quadratic estimate

For each h, f|rad(h), a supported on f, n an exterior ideal, and one of the
fixed finite local classes, the separated reflection is a sum of terms

    omega(h,f,a,n) rho(d) / q_n
      * sum_(c squarefree) lambda(c)/sqrt(q_c) chi_d(c)^3
             Phi(Z q_a q_c q_n^3/(q_d^2 q_f^2)).              (R)

The original restrictions (d,h n)=1, (c n,f)=1, and the literal quadratic
zero when (c,d)>1 are retained. There is no condition (c,n)=1. The factors
rho and lambda have modulus at most one. The exterior coefficient is
bounded by the product beta_f(a). These are CT Proposition 8.3, its separated
reflection and local beta formulas as transcribed in the pinned packet.
For j=0,1,2 and every L>0,

    |(x d/dx)^j Phi(x)| <<_(j,L) min(x^(1/8),x^(-L)).         (R-P)

The exact positive local majorant, for a prime norm q, is

    beta(0)=1,
    beta(1+3j)=q^(-j)  (j>=0),
    beta(3j)=q^(1/2-j) (j>=1),
    beta(2+3j)=0.                                           (R-B)

The needed quadratic-family theorem, after CT's fixed finite subdivision,
is Goldmakher--Louvel:

    sum_(d squarefree,q_d<=D)
      |sum_(c squarefree,q_c<=C) z_c chi_d(c)^3|^2
      <<_eta (CD)^eta (C+D) sum_c |z_c|^2.                  (Q2)

The family is quadratic because chi_d(c)^3 has order dividing two. Its
character at a nonunit remains zero. We do not replace (Q2) by an assumed
diagonal sextic sieve. The field constants and family-identification
obligations are the same as in the inherited second-moment proof.

Elementary inputs: I_F(x)<<F x; harmonic ideal sums are O(1+log x); the
number of powerful ideals <=x is O_F(sqrt x). The latter follows by writing
a powerful ideal uniquely as a0^2 b0^3 with b0 squarefree and summing
(Nb0)^(-3/2); a0,b0 need not be coprime. Ratios of generators in a fixed
compact shape belong to a fixed compact set of S-units, hence give only
bounded multiplicity. None of these counting statements needs zero exclusion.

## 3. A high-moment quadratic-polynomial lemma with every square retained

Let c run over ANY squarefree ideals in C<=q_c<2C, C>=1, with coefficients
|z_c|<=q_c^(-1/2). For the quadratic family in (Q2), put

    P_d=sum_c z_c chi_d(c)^3.

For each fixed k and eta>0,

    sum_(d squarefree,q_d<=2D) |P_d|^(2k)
           <<_(k,eta) (CD)^eta (D+C^k).                    (Qk)

Proof: expand P_d^k exactly. Its product-ideal coefficient b(v) is a sum
over all ORDERED k-tuples and obeys |b(v)|<=d_k(v)/sqrt(q_v), with q_v<=(2C)^k.
There is no coprimality between tuple entries, and distinct ideals of the
same rational norm remain distinct indices. The elementary ideal divisor
bound d_k(v)<<_(k,delta,F) q_v^delta follows prime by prime; fixed k is crucial.

Write each product ideal uniquely as v=e r^2, e squarefree. Shared primes
between e and r are allowed. The exact character identity is

    chi_d(e r^2)^3=chi_d(e)^3 1_((d,r)=1).                  (SQ)

This holds also at nonunits. In particular, e=1 does NOT erase a nonunit
zero at r. Fix r, apply (Q2) to the e-polynomial, and drop only its positive
row restriction after taking the square. By ideal counting its coefficient
square mass is

    sum_e |b(e r^2)|^2
      << C^delta (q_r)^(-2+delta),                        (S1)

 after renaming the arbitrarily small delta; harmonic logarithms are absorbed.
More explicitly one can first use d_k(v)^2<=O(q_v^delta), q_v<=(2C)^k,
then sum 1/q_e, retaining the prefactor q_r^-2. Apply Minkowski to the
finite r-sum in the row l^2 norm. The root bound is at most

    C^delta D^delta sum_(q_r<=(2C)^(k/2))
       q_r^(-1+delta) [sqrt(D)+(2C)^(k/2)/q_r]
      << C^O_k(delta) D^delta [sqrt(D)+C^(k/2)].           (S2)

The first sum is at most a logarithm or arbitrarily small C power; the
second is summable after choosing delta<1. Squaring and taking preliminary
losses small proves (Qk). This is the ordinary powering/large-sieve argument,
not a claim of new priority for quadratic high-moment methods. Its relevance
is that it applies to the EXACT reflected c family before the infinite
auxiliary sums. QED.

## 4. Localized profiles at all effective lengths

Fix h,f,a,n and let

    L=D^2 q_f^2/(Z q_a q_n^3)>0.

For q_c~C and q_d~D, the profile in (R) has argument
(C/L) exp(log(q_c/C)-2log(q_d/D)). Choose a fixed smooth cutoff equal to
one on the compact range of the logarithmic difference. By (R-P), two
integrations by parts show that the absolute Fourier norm of the localized
profile is at most

    O_J(min((C/L)^(1/8),(C/L)^(-J))).                     (F1)

Fourier separation multiplies c and d by unit-modulus norm phases. These
are common column phases and harmless row factors; (Qk) remains valid.
Minkowski in l^(2k)(d) and (Qk) therefore bound a full c block by

    (CD)^delta [D^(1/(2k))+C^(1/2)]
                   min((C/L)^(1/8),(C/L)^(-J)).          (F2)

Choose J>1/2+delta. Sum ALL dyadic C>=1. For L>=1 the low and high blocks
are convergent geometric sums, giving

    << D^delta [D^(1/(2k)) L^delta+L^(1/2+delta)].       (F3)

For L<1, every C block is on the decaying side, and the bound is instead

    << D^(delta+1/(2k)) L^J.                            (F4)

The term C=1 is kept. Subunit effective length is not called an empty
reflected sum. These estimates require only the same two profile derivatives
as the second-moment argument; k affects constants and divisor losses.

## 5. Infinite cube and ramified tails before summing powerful rows

Set R_a=D^2 q_f^2/(Z q_a), so L=R_a/q_n^3. Include the exterior factor 1/q_n.
If R_a>=1, split q_n at R_a^(1/3). Summing (F3) in the lower range uses

    sum_n q_n^(-1-3delta)<infinity,
    sum_n q_n^(-5/2-3delta)<infinity.

It gives D^delta[D^(1/(2k)) R_a^delta+R_a^(1/2+delta)]. For the upper range,
(F4) and ideal counting give

    sum_(q_n>R_a^(1/3)) q_n^(-1-3J) << R_a^(-J),

so the full upper tail costs at most D^(delta+1/(2k)), already covered.
If R_a<1, (F4) applies to EVERY n and yields

    << D^(delta+1/(2k)) R_a^J.                           (F5)

Now sum the ramified a and f branches, not before this convergent n analysis.
The exact local generating function and its mass are

    sum_j beta(j)t^j=1+(t+q^(-1/2)t^3)/(1-q^(-1)t^3),
    sum_j beta(j)=1+1/(1-q^(-1/2))<5  (q>=2).

Thus sum_(f|rad h) sum_a beta_f(a)<=6^omega(h)<<_(epsilon,k) q_h^epsilon.
Here and below the preliminary exponent is chosen small relative to 2k;
we do not assume a bound uniform in k. Also q_f^2<=q_h<2P. Put R0=D^2 P/Z.
Using q_a>=1 in (F3)-(F5), one obtains for EACH fixed h

    ||B_(h d)(Z)||_(2k,d)
      << (PD)^delta [D^(1/(2k))+R0^(1/2)] min(1,R0^J),   (F6)

with any desired J, after adjusting the profile decay and constants. Fixed
factors of two in R0 are absorbed in the implied constant, including when
the two regimes meet. Because Z>=2, all harmless factors (1+R0)^delta are
at most fixed powers of PD, independent of how large Z becomes.

There are O(P^(1/2)) h in the dyad. Their rows are disjoint, so their 2k-th
powers SUM rather than using another Minkowski loss across h. Raise (F6)
to the 2k-th power, use (x+y)^(2k)<=2^(2k-1)(x^(2k)+y^(2k)), choose the
profile decay to make 2kJ at least the requested A, and rename losses.
This proves (T1). All operations can first be made with finite truncations;
the displayed summable norm majorants, together with the adopted absolutely
convergent reflection, justify passing to the original full source.

On M(N), PD is within fixed multiples of N. The two contributions obey

    P^(1/2)D << N P^(-1/2),
    P^(1/2)(D^2P/Z)^k << (N^2/Z)^k P^(1/2-k).

Both dyadic P sums converge geometrically for k>=1. Additional bounded
norm bins and logarithms are harmless. Since R0<<N^2/Z, the subunit decay
also passes to the global bound, with its fixed constants retained. This
proves (T2), and (T3) follows by (N^2/Z)^k<=N. QED.

## 6. Pointwise comparison and a restricted-family corollary

The direct pointwise bound used in the fourth-order benchmark is also a
consequence of (R). Ideal counting gives the absolute c sum at most
O(sqrt(L)) for every L>0: split at L when L>=1, and use profile decay
with exponent greater than1/2 when L<1. Summing the exterior n then costs
sum_n q_n^(-5/2), and the ramified positive mass costs only q_h^epsilon.
Since q_f<=sqrt(q_h), this proves

    |B_m(Z)| << (NmR)^epsilon (NmR)/sqrt(Z q_h)
             <= (NmR)^epsilon (NmR)/sqrt(Z).

Combining its (2k-2)-th power with the inherited second moment gives the
naive bound (N^2/Z)^(k-1)(N+N^2/Z), up to N^epsilon. For k=2 and
N=Z^(2/3), that is Z^(1+epsilon), whereas (T2) is Z^(2/3+epsilon).
This is a real improvement for the complete fourth THETA moment.

For original rows with q_h>=P0>=1, (T1) also gives

    sum_high |B_m(Z)|^(2k)
      << N^epsilon [N P0^(-1/2)
                  +(N^2/Z)^k P0^(1/2-k)].                (Hk)

For k=1 this is the high-powerful mechanism in #961. It does not estimate
the complementary low-powerful SIGNED pairing. No arbitrary deletion of
terms inside B_m has occurred in this corollary.

## 7. What has not followed

This is an all-even-moment theorem for B_m, the reflected THETA row. The
principal inverse-zeta detector arises only after pairing with the additive
factor and a Poisson projection. B_m is not a pointwise invertible Euler
completion of the native Mobius row. No such adapter is supplied by (R).
CRITICAL_TARGET.md computes the price of the available Holder pairings and
states the unproved native moment separately. There is no new all-field
zero-free fraction or claim that the critical line has been reached here.
