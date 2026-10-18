# Global removal of the top-prime-pair sector by actual old-pair transport

Status: **PROPOSED component theorem, requiring independent mathematical
review. No estimate for the complete reweighted remainder, improved zeta
boundary or RH is asserted.**

This construction acts on the actual nonzero ordered Mobius input pairs.
It is an enlarged PAIR-WEIGHTED probe class, not a denominator contraction
`omega_q C_Y(q)`. It can create a nonzero coefficient where the original
aggregate `z_Y(d)` or `C_Y(q)` vanished. All such compensating coefficients
are explicit and retained. Every input is still <=Y; all products,
shared primes, prime powers and native output/mask conventions remain.

Use the fixed source, R, S_q, C_Y, annuli and norm of `PROOF.md` Section 1.
Write beta(q)=product_(p|q)(1+p^-1/2), H_T=sum_(n<=T)1/n.

## 1. The component theorem and its exact target response

Fix 0<eta<1/20 and 1/2<rho<5/8. Let S(Y)>=1 satisfy log S=o(log Y).
For all sufficiently large integers Y there is an explicitly defined
rational pair-weighted source

    W_Y(x)=sum_(a,b<=Y) w_Y(a,b)mu(a)mu(b)/(ab) R(x/(ab)),
    w_Y(a,b)=w_Y(b,a), |w_Y(a,b)|<=C_eta sqrt(Y),                   (1)

whose complete reduced-denominator expansion is

    W_Y(x)=sum_(q>=2) C'_Y(q)S_q(x), q<=Y^2, q cubefree.

Its q=1 coefficient is exactly zero. For every distinct pair of primes
p,l in (Y/2,Y], except a boundary sector dealt with separately below,

                         C'_Y(pl)=2/(pl).                        (2)

Take its EXACT native rough restriction

    W_Y^rough(k)=sum_(q>Q_j,core(q)>S)C'_Y(q)S_q(k), k in I_j.

Then, with delta_rho=min(2-3rho,5-8rho)>0,

    ||W_Y^rough||_2
      <<_(eta,rho) Y^(-3/10+eta)
          +Y^(-delta_rho/2)(1+log Y)^C
          +H_S^5[sqrt(S)H_Y+S].                                  (3)

Here and below C is an absolute fixed logarithmic exponent; it may be
taken larger without affecting a stated power. In particular the complete
coherent energy is O_epsilon(Y^epsilon) for every epsilon>0 on any fixed
subpower schedule S. No native sign-crossing hypothesis is required.

The omitted boundary top-prime-pair sector has global root norm O(1).
Add it to W_Y^rough. The resulting complete-mask compensator has the
same subpower energy and coefficient 2/(pl) on EVERY top-prime pair.
Subtracting it from the full unweighted native rough source removes all
those denominators throughout the ENTIRE strict native square step.
The changed complementary source remains explicit and unestimated.

The construction is not a proof of a full rough-core contraction. Its
substantive conclusion is a global, target-preserving removal of an actual
sector whose independently selected energy is >>Y^2/log(Y)^4.

## 2. Legal squarefree reference pairs near every interior top product

The only non-elementary new input is the following uniform classical
short-interval squarefree count. Tolev, Theorem 3 at r=1,l_1=0, implies

    sum_(x<n<=x+H)mu(n)^2=(6/pi^2+o(1))H                          (4)

uniformly for x in [Y/3,Y] and H=ceil(Y^(1/5+eta)). Primary source:
[D. I. Tolev, arXiv:math/0505326v1, Theorem 3, page 3 of the PDF]
(https://arxiv.org/pdf/math/0505326).
Its hypotheses hold by choosing, for example, psi(x)=(log x)^(1/2).
The required H lower bound is a constant times x^(1/5)(log x)^(3/2),
which our fixed positive eta exceeds uniformly in that location range.
Thus each such interval contains at least 3H/5 squarefree integers for
large Y. We use this density, not merely existence of one squarefree.

Let N=pl for distinct primes p,l in (Y/2,Y]. Distinct unordered prime
pairs give distinct N. Treat first the interior products

    N<=Y^2-20Y^(3/2).

Put r=floor(sqrt(N)), B=(r+1)(r+2), and let k0 be the largest integer
with k0(k0+1)<=B-N. Since r+2<=B-N<=3r+2, k0<=2sqrt(Y).
For each k=k0,...,k0+H-1 set

    a=r+1-k, b=r+2+k, M=ab=B-k(k+1).                              (5)

For large Y, H<=sqrt(Y), r<=Y-10sqrt(Y), and consequently

    Y/3<=a<b<=Y, a+b=2r+3 is odd,
    |a-b|<=7sqrt(Y), |M-N|<=G:=ceil(8sqrt(Y)H).                   (6)

The a-values and b-values each run through an integer interval of length
H at locations comparable with Y. By (4), each has at least 3H/5
squarefree values. Pigeonhole on the SAME k-set gives at least H/5
values of k for which both a and b are squarefree. No correlation or
conditioned-parity theorem is assumed. Their fixed odd sum automatically
makes one factor even, so M is even. Let G_N be this complete good set,
g_N=|G_N|, and put probability 1/g_N on each corresponding reference pair.
All shared a,b primes are allowed; mu(a)mu(b) is always nonzero.

## 3. Diffuse transport, controlled old-input weights, and target retention

For all interior products define the full finite source

    W_Y(x)=sum_N (2/N) [R(x/N)
                    -(1/g_N)sum_((a,b) in G_N) R(x/(ab))].        (7)

Every target has total reference probability one, so the sum of all
R-dilate coefficients is exactly zero. Hence no q=1 R term remains.
The canonical expansion follows from finite Mobius inversion
R(x/d)=sum_(q|d)S_q(x), with S_1=R.

For any fixed reference pair (a,b), each target attached to it lies
within G of the integer ab. There are at most 2G+1 distinct targets,
and g_N>=H/5. Its total reference probability load is therefore

    sum_(N:(a,b) in G_N)1/g_N <=5(2G+1)/H <<sqrt(Y).              (8)

This is a deterministic fractional assignment; no matching theorem,
random choice or unverified load distribution is needed. The coefficient
of R(x/(ab)), counted per unordered reference pair, has magnitude at
most C Y^(-3/2), since every N>=Y^2/4. The equivalent actual ordered
input weight is

    w_Y(a,b)=-mu(a)mu(b)ab sum_(N:(a,b) in G_N)1/(N g_N).

At each target pair w_Y(p,l)=1. Reference pairs have even product,
so they are disjoint from these target pairs. Formula (8) proves (1).
If distinct reference pairs have the same product, their coefficients
are added; the subsequent counts remain at the pair level and include
every one of these contributions.

Every old input <=Y divisible by a top prime p>Y/2 is exactly p.
Thus an old product divisible by distinct top primes p,l can only come
from the pair {p,l}; its product is odd. No even reference old product
can be divisible by pl. Consequently its canonical S_(pl) coefficient
in (7) is exactly 2/(pl), proving (2). Merely requiring M!=pl would
not suffice; it is divisibility by pl that has been excluded.

## 4. The complete full-kernel bound, including every harmonic jump

The elementary pointwise lemma is proved separately in
`../reviews/TRANSPORT_KERNEL.md`. Applied to the distinct targets N
and their probability references (6), it gives, throughout 0<x<=2Y^2,

    |W_Y(x)|<=120(G+1)/Y^2,
    ||W_Y||_L2(0,2Y^2)^2<=28800(G+1)^2/Y^2
                              <<Y^(-3/5+2eta).                   (9)

For clarity, its key fact is exact: Euler's constant and log x cancel,
and each remaining harmonic jump at index j is possible only when
|N-x/j|<=G. On this physical window j<=16. At each fixed x,j there
are at most 2G+2 distinct integer targets, irrespective of reference
loads. The logarithmic difference costs the same G/Y^2. Nothing about
an individual R-dilate L2 triangle bound is used in (9).

The entire strict native step is contained in this physical range.
Since (7) has integral dilations and zero total R coefficient, it is a
step function on integer cells. The discrete native norm is exactly
the norm of its complete constant extension.

## 5. A full coefficient resource from the near-balanced reference strip

This is the step that permits the actual denominator/core projections.
Pointwise control of (7) alone would not control either projection.

Write a cubefree q=r^2s, r,s coprime squarefree. In every contributing
reference pair a,b, r divides both a and b. Since a,b are squarefree,
each prime of s divides only a, only b, or both. Partition s=uvw into
these three pairwise-coprime squarefree parts. Then

    ruw divides a, rvw divides b, |a-b|<=B0:=ceil(7sqrt(Y)).

Dropping additional coprimality and squarefree conditions only increases
the NONNEGATIVE count. Counting a first and then b in its strip, or
vice versa, bounds the number of such pairs by

    2YB0/(r^2 s w)+min(Y/(ruw),Y/(rvw))
      =2YB0/(q w)+Y/[r w max(u,v)].                               (10)

The crucial boundary factor must be retained. Since
w max(u,v)>=sqrt(uvw)=sqrt(s), and there are 3^omega(s)=d_3(s)
partitions, multiplying (10) by the per-pair coefficient C Y^(-3/2)
proves

    |C'_(r^2s),reference|
       <=C d_3(s)[1/(r^2s)+1/(sqrt(Y)r sqrt(s))].                 (11)

It would be too expensive to replace max(u,v) by 1 when paying all low
denominators. This estimate retains the full shared-prime population.

The target part has nonzero coefficients only at q=1, a top prime, or
a distinct top-prime product. For a top prime its coefficient is at most
(2/p)sum_(l in P1)1/l<=4/p; for q=pl it is at most 2/q. Thus for
every q>=2, including all products above the output point,

    |q C'_Y(q)|<=C d_3(s)[1+sqrt(q/Y)].                            (12)

At a prime to exponent one, d_3(s)^2=9=d_9(p); at exponent two the
factor is 1<=d_9(p^2). Hence d_3(s)^2<=d_9(q), and elementary ideal-free
divisor summation yields the COMPLETE resource

    sum_(2<=q<=Q)q^2|C'_Y(q)|^2
          <=C (Q+Q^2/Y)H_Q^8.                                    (13)

No cancellation of aggregate z_Y(d), no randomness and no contraction
bound relative to original C_Y(q) has been assumed in (10)--(13).

## 6. Pay every native low-denominator annulus

The Abel/geometric Gram argument of `PROOF.md` (6.1)--(6.2) has the
following resource form for ANY fixed coefficients b_q, 2<=q<=Q<=K:

    sum_(K<=k<2K)|sum_q b_q S_q(k)|^2
       <=C(1+log Q)(1/K+Q^2/K^2)sum_q q^2|b_q|^2.                (14)

The leading term uses reduced-frequency spacing Q^-2 and
sum_(a modq)^*|1-e(a/q)|^-2<=q^2/4. The full Abel remainder has squared
norm at most C B Q^3/K^3, B=sum q^2|b_q|^2; since Q<=K this is paid
by C B Q^2/K^2. Thus (14) also pays the complete reciprocal tail and
all prime-power centerings. No output-dependent coefficient is inserted:
the transport is fixed once Y is fixed.

Combining (13)--(14), with the actual Q_j=floor(X_j^rho), bounds each
native annulus by a fixed logarithmic power times

    X_j^(rho-1)+X_j^(3rho-2)
       +Y^-1 X_j^(2rho-1)+Y^-1 X_j^(4rho-2).                      (15)

For Y+1<=X_j<(Y+1)^2, sum the first two decreasing geometric terms
from their lower endpoint and the last two increasing terms from their
upper endpoint. The full low-denominator energy, including a shortened
last annulus, is

    <<_rho [Y^(3rho-2)+Y^(8rho-5)](1+log Y)^C
    <<_rho Y^(-delta_rho)(1+log Y)^C.                              (16)

This decays for the stated 1/2<rho<5/8. At rho=13/24 one may take
delta_rho=3/8. In particular the large input multiplier O(sqrt(Y))
does not cause a hidden loss: its crude cap is replaced by the proved
near-balanced coefficient resource (13).

## 7. Pay the complete small-core sector coherently

Assume S<Y/3, as holds eventually for a subpower schedule. The target
products contribute no q>=2 with core(q)<=S. For references, r divides
gcd(a,b) and a!=b, so r<=|a-b|<=B0. Use (11) and the full global norm

    ||S_q||_L2(0,infinity)<=sqrt(3q)beta(q).

Even after inserting the arbitrary actual indicator q>Q_j on each
annulus, Minkowski therefore bounds the small-core root cost by

    C sum_(s<=S)^flat d_3(s)beta(s)
       [s^-1/2 sum_(r<=B0)beta(r)/r
                          +Y^-1/2 sum_(r<=B0)beta(r)].            (17)

Every r is retained; dropping the coprimality with s only enlarges this
positive resource. Expanding beta(r) over its squarefree divisors gives

    sum_(r<=R)beta(r)<=zeta(3/2)R,
    sum_(r<=R)beta(r)/r<=zeta(3/2)H_R.

For squarefree s, d_3(s)beta(s)<=d_6(s), including p=2. Partial summation
of sum_(s<=S)d_6(s)<=S H_S^5 now proves

    (17)<=C H_S^5[sqrt(S)H_Y+S].                                  (18)

This is subpower on every fixed subpower schedule. Thus squares, shared
prime squares and every small squarefree core have all been paid, rather
than dropped to gain the target exponent.

## 8. Boundary targets and the exact remaining problem

For N=pl>Y^2-20Y^(3/2), both primes exceed Y-20sqrt(Y). There are O(Y)
unordered integer pairs in that corner. Each actual coefficient is 2/N,
and ||S_N||_2<=sqrt(3N)beta(N)=O(Y), so the COMPLETE coherent boundary
sector has global root norm O(1). This remains true under all actual
annular/core indicators by the same individual root triangle bound.

If one wants the final boundary addition itself in the ordered-pair form
(1), expand S_(pl)=R(x/(pl))-R(x/p)-R(x/l)+R(x). These use the legal
old pairs (p,l),(p,1),(l,1),(1,1), all with nonzero Mobius values.
Their aggregated weights are bounded (the (1,1) coefficient is O(1/Y)
and each (p,1) weight is O(Y^-1/2)); this preserves the O(sqrt(Y)) cap.

Take the rough projection of (7), add this actual boundary sector, and
subtract the result from the original full rough source. At every retained
top-prime-pair denominator the coefficient changes from 2/(pl) to zero.
All other coefficients, including any newly introduced ones, remain in
the explicitly defined complement. Combining (9), (16), (18) and the
boundary O(1) proves (3) and the theorem's final complete compensation.

The new complement is supported on the same old-product range and the
same cubefree denominator class. It is not promised to have bounded
denominator multipliers relative to the original source: pair-level
weights were used, and original aggregate zeros need not be preserved.
The unestimated remainder still contains the full zeta-sensitive
arithmetic problem. The result establishes a concrete global sector
removal and a stronger coefficient resource for its legal pair deformation;
it does not estimate that complete remainder by fiat.
