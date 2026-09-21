# NCL29: all-denominator angular control and the near-zero remainder

**Status: proposed component proofs; independent mathematical review required.**
**No full composite-covariance bound, new zero-free region, or RH proof.**
Date: 20 September 2026. Continuation of #904 at
`879497b4f11be2618c448efc1fa93f69b4022e4c`.

This pass changes the partition, not the arithmetic sequence. It proves a
polylogarithmic budget for the combined rational Fourier modes at ALL
available denominators outside a prescribed small angular neighborhood of
zero. All pure prime-power denominators can also be paid in full. The remaining
near-zero band at denominators with at least TWO distinct primes is not
estimated here. The new bound is valid for bounded sources generally; native inversion is used to identify
scale-local Newton outputs with the actual Mobius sequence, not to claim
that the generic estimate has solved the arithmetic cancellation problem.

The NCG28 denominator-window theorem remains unchanged. The result here is
not an estimate for its entire moving high-composite component. Different
short prefixes are used on different observation blocks, and each tail map
is applied BEFORE restriction to its block. The comparison is exact at the
level of the full native output, not term-by-term between the two partitions.

## 1. Finite source and notation

Write e(t)=exp(2*pi*i*t). Dirichlet convolution is denoted by *. For a real
source c supported on 1,...,L, suppose |c(n)|<=K and

    sum c(n)/n = 0.

Define

    z=c*c,  U_d=sum_(d|n)c(n)/n,
    B_q=sum_(q|d)z(d)/d,             1<=q<=L^2.

Thus B_1=0; all quantities are finite rationals when c is rational. A
superscript square denotes an ordinary square unless convolution is explicit.
Put H_0=0, H_n=sum_(j=1)^n 1/j and

    T_d(k)=(d-1)/2-(k mod d),
    R_q(k)=sum_(d|q)mu(q/d)T_d(k),   q>=2.

Finite Fourier inversion gives

    R_q(k)=sum_(1<=a<q,(a,q)=1) e(ak/q)/(1-e(-a/q)).          (1.1)

This follows by differencing T_d, whose nonconstant Fourier coefficients
are 1/(1-e(-a/d)), and applying divisor inversion to isolate reduced fractions.
The constant Fourier coefficient of T_d is zero. The full cumulative Newton
output v=2c-1*z is

    V(k)=2 A_c(k)+(sum c(n))^2/2-sum_(q>=2) B_q R_q(k).     (1.2)

Indeed sum_(q|d,q>=2)R_q=T_d, and floor(k/d)=(k+T_d(k)-(d-1)/2)/d.
Reciprocal balance kills k sum z(d)/d. The remaining constant is exactly
(sum c)^2/2, since sum z(d)/d=0. It is not discarded in physical space.

For a periodic bounded function P define its complete tail transform by

    (TP)(k)=P(k)/(k+1)-sum_(j>k)P(j)/[j(j+1)].              (1.3)

For any b>=1, direct expansion and completion in weighted ell2 prove

    sum_(k>=b)|TP(k)|^2
      =sum_(j>=b)|P(j)|^2/[j(j+1)]
       -b |sum_(j>=b)P(j)/[j(j+1)]|^2.                    (1.4)

The same identity holds for complex P, using Hermitian products. For finite
P, diagonal coefficients are 1/[j(j+1)]-b/[j^2(j+1)^2], and the polarized
coefficient for i<j is -b/[i(i+1)j(j+1)]. Truncation in the weighted norm,
followed by Cauchy--Schwarz for the tail functional, proves (1.4) in general.
In particular T is a contraction and annihilates constants. This is the
NCG28 elementary tail identity, rederived here, not a new Hardy theorem.

For 0<alpha<1 define the centered single-frequency mode

    Z_alpha(k)=sum_(n=1)^k e(alpha*n)/n + log(1-e(alpha)).   (1.5)

The logarithm is the radial limit from |z|<1 of log(1-z), with its branch
fixed there. Differentiating the power series gives sum z^n/n=-log(1-z).
Bounded geometric partial sums and summation by parts give convergence at
e(alpha), so (1.5) equals minus the COMPLETE harmonic exponential tail.
Another summation by parts gives

    T[e(alpha*k)/(1-e(-alpha))]=Z_alpha(k).               (1.6)

Conjugate frequencies make (1.5) real after pairing; the paired constant is
2 log(2 sin(pi*alpha)) for 0<alpha<1/2. At alpha=1/2 the self-conjugate
constant is log 2 and is counted once.

Summing (1.5) over all reduced a/q gives the previous Ramanujan harmonic
mode Z_q(k)=sum_(d|q)mu(q/d)H_floor(k/d)+Lambda(q). The full logarithmic
constant cancels because

    sum_(q>=2)B_q Lambda(q)=sum_d z(d)log(d)/d=0.           (1.7)

This cancellation is asserted only for the FULL source, not for an angular
piece. Consequently the reciprocal Newton output is exactly

    m_v(k)=2m_c(k)-sum_(q>=2)sum_((a,q)=1) B_q Z_(a/q)(k).
                                                                  (1.8)
No observation or source tail has been omitted in these identities.

## 2. NCL29-1: a global denominator moment with a modest explicit constant

For every finite source with |c(n)|<=K, even without reciprocal balance,

    sum_(q<=L^2) q |B_q|^2
       <= 1024 K^4 H_L^4 H_(L^2)^4.                       (2.1)

This is a GENERIC bounded-source estimate. It does not use RH, PNT,
independent random signs, or the native inverse identities.

First |U_d|<=K H_L/d. The exact prime-exponent threshold identity

    1_(i+j>=a) = sum_(u=0)^a 1_(i>=u)1_(j>=a-u)
                -sum_(u=1)^a 1_(i>=u)1_(j>=a+1-u)

is checked by counting the allowed u. Multiplying over p^a||q and applying
the bound for U_d to every resulting product gives

    |B_q|<= K^2 H_L^2 A(q)/q,
    A(q)=product_(p^a||q)(a+1+a/p).                        (2.2)

Overlapping divisibility conditions and every prime power are present. The
alternative exact formula

    B_q=sum_(d|q)sum_(h|q/d)mu(h) U_(dh) U_(q/d)

follows by partitioning the first source index according to its gcd with q.
Neither formula makes B_q multiplicative or fixes its sign.

Let d_4 count ordered four-factor decompositions. Since
(a+1)^2<=binom(a+3,3), we have

    A(q)^2<=d_4(q) product_(p|q)(1+1/p)^2.

Write g(p)=2/p+1/p^2, extend g multiplicatively to squarefree numbers, and
set it to zero on nonsquarefree numbers. Expanding the product, using
submultiplicativity d_4(dm)<=d_4(d)d_4(m), and summing positive terms gives

    sum_(q<=Q) A(q)^2/q
      <= H_Q^4 sum_(d squarefree) d_4(d)g(d)/d
      = H_Q^4 product_p(1+8/p^2+4/p^3)
      < 1024 H_Q^4.                                      (2.3)

Here sum_(m<=Q)d_4(m)/m<=H_Q^4, by opening all four factors. For the FULL
infinite product, p>=2 gives

    1+8/p^2+4/p^3 <= 1+10/p^2 <= (1-p^-2)^(-10).

The absolutely convergent Euler product is therefore at most zeta(2)^10<2^10;
zeta(2)<2 follows from the integral test. This pays every omitted prime and
does not attach a numerical oracle to the constant. Submultiplicativity of
d_4 follows by splitting each distribution of the prime exponents of dm
between those of d and m, which gives a surjection from pairs of distributions.
Equations (2.2)-(2.3) prove (2.1).

The exact weighted denominator moment, not a pointwise assertion about
signs of composite amplitudes, is the useful quantity in the next estimate.

## 3. NCL29-2: all denominators away from zero frequency

Fix 0<eta<=1/2. Let A be ANY set of reduced fractions a/q with
2<=q<=L^2 and

    ||a/q||=min(a/q,1-a/q)>=eta.

A need not contain every admissible fraction. For real-valued components
assume it is closed under conjugation a -> q-a. Put

    P_A(k)=sum_(a/q in A) B_q e(ak/q)/(1-e(-a/q)),
    W_A=T P_A.

For every integer X>=1,

    sum_(k>=X)|W_A(k)|^2
    <= [2/X+4L^4 H_(L^4)/(3X^2)]
       *256 K^4 eta^-1 H_L^4 H_(L^2)^4.                  (3.1)

In particular, if L^2<=8X, then

    sum_(k>=X)|W_A(k)|^2
       <= 2^21 K^4 eta^-1 H_L^9.                         (3.2)

This controls the COMBINED function, all cross-denominator and
cross-numerator covariance, and its ENTIRE future. Taking A to contain
only composite denominators, or only large composites, is permitted.
It is not a complete-period average or an assertion of orthogonality.

### Fourier coefficient mass

Using sin(pi*t)>=2t for 0<=t<=1/2, we obtain

    sum_(1<=a<q,||a/q||>=eta) |1-e(-a/q)|^-2 <= q/(4eta).
                                                                  (3.3)
Indeed, pair a with q-a, put A0=ceil(eta*q), and bound by
(q^2/8) sum_(a>=A0)a^-2 <=q^2/(4A0)<=q/(4eta).
The even-q central term can safely be counted twice for this upper bound.
Dropping the coprimality condition only enlarges the positive sum.
Therefore the total squared Fourier coefficient mass is at most the last
factor of (3.1), by (2.1).

### Complete covariance bound

Distinct reduced fractions of denominator at most Q=L^2 are separated on
the circle by at least Q^-2. For N consecutive integers, geometric summation
and the Schur row bound give

    sum_block |sum_alpha a_alpha e(alpha*k)|^2
       <= [N+Q^2 H_(Q^2)] sum_alpha |a_alpha|^2.           (3.4)

To verify the entire off-diagonal budget, order neighboring frequencies in
each direction from a fixed alpha. The j-th neighbor has circular distance
at least j/Q^2 until distance 1/2; the geometric sum has magnitude at most
1/(2||alpha-beta||). Both directions cost at most Q^2 H_(Q^2).
This is the elementary logarithmic-loss additive large sieve used in NCG28,
not a quadratic-character theorem. Summing (3.4) over [2^jX,2^(j+1)X),
with the upper physical weight (2^jX)^-2, yields the bracket in (3.1).
Apply (1.4). Every future block is included.

Finally H_(L^2)<=2H_L, H_(L^4)<=4H_L, and L^4/X^2<=64 when L^2<=8X.
The bracket in (3.1) is then at most 344H_L. Multiplying 344 by 256*16
is below 2^21, proving the conservative constant in (3.2).

The eta^-1 factor is real. Letting eta approach zero without paying this
factor is NOT justified. In particular setting eta~1/L^2 introduces a
power loss; the all-mode problem has not been solved by (3.2).

## 3a. NCL29-2b: every prime-power denominator is affordable in full

Pure prime powers need not be left inside the near-zero remainder. For

    P_pp(k)=sum_(p prime,a>=1,p^a<=L^2) B_(p^a) R_(p^a)(k),
    W_pp=T P_pp,

we have, whenever L^2<=8X,

    sum_(k>=X)|W_pp(k)|^2 <= 2^12 K^4 H_L^8.              (3.5)

This includes ALL primes, prime squares and higher powers, every reduced
numerator, their complete mutual covariance, and the entire observation tail.
It is not a claim that B_(p^a) is negative or that prime powers suffice as
an approximation basis in the separate Nyman--Beurling programme.

For a=1, reciprocal balance gives B_p=-U_p^2 and |R_p|<p/2. Consequently
the sum of the pointwise absolute prime contributions is at most
K^2 H_L^3/2. For a>=2, (2.2) gives

    |B_(p^a)| <= K^2 H_L^2(2a+1)/p^a,
    R_(p^a)=T_(p^a)-T_(p^(a-1)),  |R_(p^a)|<p^a.

Put A=floor(log_2(L^2)). Since p^a<=L^2, each exponent a>=2 has at most
L^(2/a)<=L possible primes, even after enlarging to all positive integers.
Thus

    sum_(a=2)^A (2a+1) #{p:p^a<=L^2} <= L(A+1)^2.

Also A+1<=4H_L for L>=2. Combining all prime powers yields

    |P_pp(k)| <= 17 K^2 L H_L^4  for EVERY k.

The complete physical tail has weight sum 1/X. Its energy is at most
289 K^4 L^2 H_L^8/X <=2312 K^4 H_L^8 <2^12 K^4 H_L^8.
Apply the exact contraction (1.4). No period averaging is used.

For this COMPLETE prime-power sector, the logarithmic constants cancel
prime by prime: sum_(a>=1)B_(p^a)=0. Hence W_pp has an exact rational
harmonic-number evaluation when c is rational. The far and near angular
parts of mixed-prime denominators still require their centering constants.

## 4. NCL29-3: exact scale-local assembly for the native square step

Let Y>=7, b=Y+1, B=b^2-1 and

    m(k)=sum_(n<=k)mu(n)/n,     F_Y=sum_(k<=Y)m(k)^2.

For j=0,...,J-1, where J=ceil(log_2 b), set

    X_j=b*2^j,   M_j=min(2X_j-1,B),   y_j=floor(sqrt(M_j)). (4.1)

These disjoint integer blocks cover EVERY k=b,...,B. We have y_j<=Y,
M_j<(y_j+1)^2, and 2y_j<=X_j, since X_j>=8 and y_j<sqrt(2X_j).

For each block use its OWN canonical capped completion c^(y_j). Retain
mu(n) for n<=y_j, then subtract the reciprocal residual by coefficients
of magnitude at most 3 until its reciprocal sum is zero. The elementary
bound |m(y)|<=1 follows from sum mu(n)floor(y/n)=1. The available correction
through y+ceil(y/2) is at least one, so its support L_j<=2y_j and its cap
is three. These are the PCR26 construction and bounds; no future Mobius
value is used to define these sources.

For each fixed source, e_j=delta-1*c^(y_j) vanishes below y_j+1 and

    mu-(2c^(y_j)-1*c^(y_j)*c^(y_j))=mu*e_j*e_j.

Thus its entire Newton coefficient prefix through M_j is exactly native.
Also m_(c^(y_j))(k)=0 on its assigned block, since L_j<=X_j. Formula (1.8)
therefore gives, for ALL k in that block,

    m(k)=-W_pp^(j)(k)-W_far^(j)(k)-W_near^(j)(k),           (4.2)

where W_pp contains every pure prime-power denominator, W_far uses
||a/q||>=eta at denominators with at least two distinct primes, and W_near
uses 0<||a/q||<eta at those same mixed-prime denominators. Together EVERY
q<=L_j^2 is included. The distinction is ANGULAR, not a bound on q.
All three are full tail transforms for a frozen source and mask before any
restriction to the assigned block. Constants inside each angular component
in (1.5) must be retained.

Define the piecewise functions F_pp(k)=W_pp^(j)(k), F_far(k)=W_far^(j)(k),
and F_near(k)=W_near^(j)(k) on their respective blocks. (These symbols denote
components, not the scalar energy F_Y.) Then

    F_B-F_Y=||F_pp+F_far+F_near||_[b,B]^2,
    D_far:=||F_far||_[b,B]^2
       <= 81*2^21 * J * eta^-1 * H_(2Y)^9,
    D_pp:=||F_pp||_[b,B]^2 <=81*2^12*J*H_(2Y)^8.          (4.3)

Here L_j^2<=4y_j^2<8X_j, so (3.2) applies, and the disjoint blocks cost
only their number J. In particular eta=1/(2J) gives D_far=O(log^11(2Y)),
with an absolute explicit constant. This bound is independent of F_Y.
ALL mixed-prime high-denominator modes satisfying the angular restriction
are included, while pure prime powers are already included at every angle.

Put G=F_pp+F_far and D_good=||G||^2<=2D_pp+2D_far. The exact three-channel
identity has THREE mixed terms, not an assumption about their signs. A valid
upper inequality is

    F_B<=F_Y+2D_good+2||F_near||_[b,B]^2.                 (4.4)

### No hidden commutation or completion cost

The short source changes between blocks. We do NOT apply T to a piecewise
stitched physical source and assert it equals the piecewise W functions.
Such an operation would create additional future-boundary terms. Instead,
(1.8) is applied separately to each complete fixed-source output, where it
is valid at every assigned integer. Restriction occurs last. This is why
(4.2) is exact without deleting a transition term.

Likewise this does not assert a componentwise identity with NCG28's moving
high-composite W_high. That older decomposition used one c^(Y) on the
entire square step. The two FULL sums agree with m, but their summands need
not agree. The old activation correction remains correct and unchanged.

## 5. What this proves about the remaining difficulty

The theorem is an affirmative bound, but its bounded-source nature is also
an important limitation. The expensive part has NOT been proved small;
it is the explicit signed near-zero rational-frequency band at mixed-prime
denominators in (4.2).
At eta=1/(2J), an estimate

    ||F_near||_[b,B]^2 <= C(1+log Y)^A(1+F_Y)^p,  p<2,    (5.1)

on the prescribed square ladder would combine with (4.4) to give the desired
subquadratic scale recurrence. The inherited logarithmic iteration would
then give F_X=X^o(1), and E_X<=F_X plus dyadic Cauchy--Schwarz would make
integral M(x)x^(-s-1)dx holomorphic for Re(s)>1/2. On Re(s)>1 it equals
1/(s*zeta(s)); the identity theorem and the functional equation imply RH.

**No estimate (5.1) is supplied.** This conditional ending is not a new RH
criterion counted as independent progress. The new estimate is (3.1)-(4.3).

More generally eta may be any prescribed eta_Y in (0,1/2] with
eta_Y^-1=Y^o(1). Then D_good=Y^o(1). For example
eta_Y=2^(-ceil(sqrt(J))) has that property. If the actual increment
F_B-F_Y>=Y^epsilon along any sequence for fixed epsilon>0, then (4.2)-(4.3)
and the reverse triangle inequality force

    ||F_near||_[b,B] / sqrt(F_B-F_Y) -> 1,
    ||G||_[b,B] / sqrt(F_B-F_Y) -> 0.                 (5.2)

Thus any power-sized growth must be carried by that shrinking band.
These are additive Fourier frequencies on the INTEGER OBSERVATION INDEX.
This is NOT a statement that zeros of zeta have small imaginary parts.

The finite data below show that this remaining band can already contain most
of the energy. Denominator coverage is not energy coverage, and neither is
a percentage of progress toward RH.

## 6. Exact low-frequency formula and a falsifier for dropping constants

For a conjugation-invariant selected set, evaluation can avoid complex
logarithm choices entirely:

    W_A(k)=sum_(a/q in A) B_q[
              sum_(n=1)^k cos(2*pi*a*n/q)/n
              + log(2 sin(pi*a/q))].                    (6.1)

This retains the full harmonic tail by the exact identity (1.5), rather
than truncating a slowly convergent infinite series numerically.

For c=delta_1-2delta_2, the only nonzero amplitudes are B_2=-1 and B_4=1.
With eta=1/3, the far component contains alpha=1/2 and has logarithmic
constant -log 2. The near component contains alpha=1/4,3/4 and has constant
+log 2. They cancel in the full source, NOT in either piece. Discarding
those constants changes the values and energies; the checker rejects it.

A second control keeps native low/far covariance of either sign. No
frequency sign, sign of B_q, or pointwise sign of a mode licenses deletion
of that cross term.

## 6a. The unbounded remainder still has an exact short-source bilinear form

The unresolved band is not an arbitrary collection of Fourier coefficients.
For each integer d and fixed eta, let

    K_(eta,d)(k)=sum Z_(j/d)(k),

where the sum is over 1<=j<d with ||j/d||<eta and with
q=d/gcd(j,d) having at least two distinct prime factors. Then on a fixed
source block the exact remaining function is

    W_near(k)=sum_(r,s<=L) c(r)c(s)/(rs) K_(eta,rs)(k).     (6.2)

To prove (6.2), substitute B_q=sum_(q|d)z(d)/d and interchange FINITE sums.
The reduced fractions a/q with q|d correspond bijectively to j/d, with
q=d/gcd(j,d). Uncoalescing z(d) gives the displayed short-source bilinear
form. It is checked by two exact rational frequency dictionaries in the tests.

Every K includes the entire logarithmic centering in (1.5). With NO angular
or denominator-type restriction, its full version telescopes exactly to

    K_full,d(k)=H_floor(k/d)-H_k+log d.                  (6.3)

Indeed sum_(j=1)^(d-1)e(j*n/d)=d*1_(d|n)-1, and the root-of-unity product
product_(j=1)^(d-1)(1-e(j/d))=d supplies the total real logarithmic constant.
The masked version does not inherit either cancellation term by term.

Equivalently the cosine part of the unfiltered near-angle kernel is a
short Dirichlet kernel: for A=ceil(eta*d)-1,

    sum_(j near) cos(2*pi*j*n/d)=2 sum_(j=1)^A cos(2*pi*j*n/d),

with the prime-power reduced fractions then removed exactly. The hard work
is to use the ACTUAL c(r)c(s), including its native divisor-inverse relations,
in this masked bilinear kernel before squaring. Absolute-value summation or
allowing arbitrary bounded coefficients does not supply the missing gain.
Equation (6.2) is an exact execution target, not advertised as a new upper
estimate. It prevents the near-zero remainder from being detached from its
source or mistaken for a freely optimizable spectral vector.

## 7. Evidence and review boundary

The executable companion uses exact Fraction/integer source and divisor
algebra and outward fixed-point sine/cosine/logarithm bounds. It checks all
native Newton coefficients through the endpoint of every declared block
against separately computed Mobius values. An independent gcd-threshold
formula checks the spectral amplitudes. Small full-frequency calculations
check (4.2) with both angular pieces computed directly. Larger declared
panels may calculate the near piece by exact complementary algebra; the
report distinguishes that from a second independent spectral evaluation.

No finite experiment proves the infinite estimates. The written proofs,
operator-domain/tail identities, exponent/cutoff quantifiers, and coefficient
majorant require mathematical review. No original-research priority is claimed
for classical divisor, Fourier, Hardy, or large-sieve tools or for the specific
combination before a fuller literature audit.

See VALIDATION.md for commands actually executed, bounded domains, negative
controls and publication limitations. Prior NCG28/DSE27/RCB26/NSR26 campaigns,
a whole-repository validator, Lean and external referee review are not implied
by this packet's tests.
