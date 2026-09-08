# A uniform native annular lower bound and the exact prime-square drift

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent review required.
RH and the eventual sharp arithmetic lower bound remain unproved.
Parent: PR #803 at 8d8750e5be8e0f2920db371bf31ea93c2d0a0caf.
Local labels HT1--HT6 belong only to this packet.

The new sign is an actual bound for the parent's finite prime-power scalar,
not another criterion alone and not a new full-window PSD assertion. It holds
uniformly over a continuum of scales; the large range is NOT enumerated.
Its external finite-height input is Platt--Trudgian, Theorem 1, arXiv:
2004.09765v1, restricted to H=3*10^12. Their calculation is imported, not rerun.
No simplicity, zero table, or RH assumption above H is used. Quantitative
zero-counting constants used here are proved below, rather than imported
from a high-precision argument-bound optimization.

## 1. Keep the exact native scalar

Put

 w(u)=u/3-1/(192u^2),         1/4<u<=1,
      1/(3u^2)-u/192,         1<u<=4,
      0,                     otherwise.

The formulas agree at 1, vanish at the outside endpoints, and obey

 0<=w<=21/64,  w(1/u)=u*w(u),  integral w(u)du=45/128.       (1)

Let Lambda(p^k)=log p for every prime p and integer k>=1. For EVERY real
m>=2 define

 P(m^2)=(1/m) sum_n Lambda(n) w(n/m^2),
 D(m)=P(m^2)-45m/128+1/4,
 B(m)=192m^3 P(m^2).                                      (2)

For integer m these are exactly B_m and D_m in the parent, including its
quarter endpoint and center conventions. No integer rounding is introduced
in (2). The support is m^2/4<n<=4m^2. In particular the theorem below covers
real X=m^2, not only a finite set of square samples.

**HT1 (proved finite-height transfer).** For every real m>=2,

 D(m)>1/4 - 237/5000 - 205/(128m^5)
          -(85/64)*(37/(25*10^12))*(m+2+1/m).              (3)

Consequently

 D(m)>1/10,    2<=m<=50,000,000,000;
 D(m)>1/200,   2<=m<=100,000,000,000.                      (4)

Thus the parent's sharp lower inequality holds at every real scale
4<=X<=10^22, including every integer m from 2 to 10^11. All required prime
powers up to 4*10^22 are included mathematically; no such prime scan is run.
The margin statements are strict, with their full analytic tail included.

There is also a weaker bound at UNBOUNDED scales:

 B(m)>(135/2-1887/(5*10^12))*m^4-19m^3,    all m>=2.       (5)

It is essential not to call (5) the RH-strength bound. Its fixed positive
loss in the m^4 coefficient eventually dominates its gain in the m^3 term.
The proof of (3)--(5) occupies Sections 2--5.

## 2. The full zero representation, without assuming RH

Fix b=3/2, d=log 4, c=1/8, and retain the literal arithmetic W of the parent.
Define V(x)=(1+c^2)W(x)-cW(x-d)-cW(x+d) and

 A(z)=(1-c exp(dz))(1-c exp(-dz)).                         (6)

Let rho range over every nontrivial zero with positive ordinate, counted
with analytic multiplicity. Write z_rho=rho-1/2=alpha+i gamma. Both members
alpha+i gamma and -alpha+i gamma of an off-line reflected pair occur in
this upper-half-plane list. They are not replaced by four copies. The
classical critical strip gives |alpha|<1/2 and gamma>0.

For the entire centered completion E(r)=xi(1/2+r), evenness and its
order-one Hadamard product give, off its poles,

 H(r):=E'(r)/E(r)=sum_(gamma>0) 2r/(r^2-z_rho^2).           (7)

Pairing the opposite zeros cancels the genus-one exponential factors.
Evenness removes a linear exponential, and order one excludes a quadratic
one. The sum converges normally on compact pole-free sets since the
zero count is O(T log(T+2)). All multiplicities stay in the list.

The parent's source identity is

 Laplace W(r)=[H(r)-(r/b)H(b)]/(b^2-r^2), Re r>1/2.        (8)

The value at r=b is removable. For each summand of (7), the corresponding
term of (8) is 2r/[(b^2-z_rho^2)(r^2-z_rho^2)]. Inverting term by term gives

 W(x)=sum_(gamma>0) 2 cosh(z_rho*x)/(b^2-z_rho^2),
 V(x)=sum_(gamma>0) 2 A(z_rho)cosh(z_rho*x)/(b^2-z_rho^2). (9)

These are unconditional expressions, unlike the cosine-only version under
RH. They are absolutely and uniformly convergent on every bounded real
interval. Indeed |cosh(z_rho*x)|<=cosh(x/2) and
|b^2-z_rho^2|>=gamma^2+2. Their Laplace transforms on Re r>1/2 may be
interchanged absolutely, and uniqueness for continuous exponential-order
functions proves equality with the ARITHMETIC source (8). Thus (9) is not
a new definition using a desired real spectrum. The classical product,
(8), and the elementary uniqueness theorem are the exact inputs.

### 2.1 An arbitrary certified height

Assume only that every zero through height H>=100 is on the critical line.
Write V=V_low+V_high by that ordinate cutoff, and put

 R_H=sum_(gamma>H) 1/gamma^2.                              (10)

For low zeros the coefficients 2A(i gamma)/(b^2+gamma^2) are positive,
because A(i gamma)>=49/64. Therefore

 |V_low(x)|<=V_low(0).

For all upper zeros, independently of their location in the strip,

 |A(z_rho)|<=1+c^2+2c cosh(d/2)=85/64,
 |V_high(x)|<=(85/32) cosh(x/2) R_H.                       (11)

The actual constant C0=V(0) is NOT replaced by the low-zero sum. From
V_low(0)=C0-V_high(0), (11) proves the two-sided bound

 |V(x)|<=C0+(85/32)*(1+cosh(x/2))*R_H.                    (12)

The extra high-tail term at x=0 is necessary. Omitting it would incorrectly
promote a finite critical-line prefix to a complete spectral mass.
No individual zero below H need be computed, and no sign is assigned to
an individual unknown high zero. Equations (9)--(12) retain all of them.

## 3. A coarse counting remainder with a complete derivation

**HT2.** With N(T)=#{rho:0<Im rho<=T}, multiplicities counted, and
M(T)=T/(2pi)*log(T/(2pi e)), one has

 |N(T)-M(T)|<=20 log(T+2), T>=100.                         (13)

This deliberately loose bound avoids dependence on a sharp subconvexity
constant. We use the classical argument-principle identity
N(T)=1+theta(T)/pi+Arg_T(zeta(1/2+iT))/pi away from zero ordinates,
with theta(T)=Im log Gamma(1/4+iT/2)-(T/2)log pi. The argument is continued
from 2 along Re s=2 and then horizontally. This classical identity counts
ALL nontrivial zeros, not only those on the line.

Here is an explicit bound for its argument. Let
f_T(z)=(zeta(z+iT)+zeta(z-iT))/2 on |z-2|<=2. It is analytic there for
T>=100, is real on real z, and f_T(2)>1/3 because zeta(2)<=sum_(n=1)^5 n^-2+1/5<5/3. One
Euler--Maclaurin integration gives, for Re s>-1 away from 1,

 zeta(s)=1/(s-1)+1/2+s/12
       -s(s+1)/2 integral_1^infinity B2({u})u^(-s-2)du,
 |B2({u})|<=1/6.                                         (14)

On that disk Re(z+/-iT)>=0 and |z+/-iT|<=T+4. Thus

 |f_T(z)|<=1/(T-2)+1/2+(T+4)/12+(T+4)(T+5)/12<2T^2.

Jensen on concentric radii 3/2 and 2 gives at most

 q_T<=log(6T^2)/log(4/3)<8log T+8                         (15)

zeros in the inner disk. The elementary inequalities log(4/3)>1/4 and
log6<2 suffice. Boundary zeros are included by limiting radii. On the
horizontal path Re zeta can change sign at most q_T times. Between such
points a continuous argument varies within an interval of length pi, and
on Re s=2 zeta stays in the right half-plane. Consequently

 |Arg_T zeta(1/2+iT)|/pi<=q_T+3/2<8log T+19/2.             (16)

For completeness, on Re z>0 Euler--Maclaurin for log Gamma gives

 log Gamma(z)=(z-1/2)log z-z+(1/2)log(2pi)+R(z),
 R(z)=1/(12z)-(1/2)integral_0^infinity B2({u})/(u+z)^2 du,
 |R(z)|<=1/(12|z|)+1/(12 Re z).                          (17)

At z=1/4+iT/2 the elementary part differs in imaginary part from
(T/2)log(T/(2pi e))-pi/8 by at most 3/(16T). Thus its full error, including
R, is less than one. Inserting (16)--(17) into the counting identity gives
|N(T)-M(T)|<8log T+12<20log(T+2). Taking right limits extends this to
zero ordinates with the stated <= convention. This proves (13).

**HT3 (complete reciprocal-square tail).** For H>=100,

 R_H <= [log(H/(2pi))+1]/(2pi H)
                +[40log(H+2)+10]/H^2 =: Rbar(H).          (18)

Stieltjes integration by parts, including the lower endpoint, gives
R_H=-N(H)/H^2+2 integral_H^infinity N(t)/t^3 dt. Insert (13).
The main term integrates exactly to the first term of (18). For the error,
use log(t+2)<=log(H+2)+log(t/H) for t>=H. The endpoint error is
20log(H+2)/H^2 and the integral error is at most
20log(H+2)/H^2+10/H^2. This proves (18) also when a zero lies exactly at H.
The stricter bound with gamma^2+2 in the denominator is unnecessary.

For H=3*10^12 the outward elementary checker proves

 Rbar(H)<37/(25*10^12).                                   (19)

The actual real value of this upper-bound expression is about
1.47970363104*10^-12; this decimal is not an accepting input.

## 4. From the spectrum to the native arithmetic lower bound

The exact parent filter identity is

 V(log X)=45sqrt(X)/128-P(X)-E(X), X>=4,                   (20)
 E(X)=c S(log(X/4))+c S(log(4X))-(1+c^2)S(log X),
 S(x)=sum_(j>=1) exp(-(2j+1/2)x)/[(2j+1/2)^2-b^2].

Every prime power outside [X/4,4X] cancels, not approximately but exactly.
Each exponential in E has a positive coefficient, so E>=0. Since its
smallest gamma exponent is 5/2 and S(0)=1/6+log2/3<2/5,

 0<=E(m^2)<205/(128 m^5), m>=2.                           (21)

Indeed discard the negative term of E and use S(y)<=S(0)exp(-5y/2)
on y>=0. Then c S(0)[(4/m^2)^(5/2)+(4m^2)^(-5/2)] is bounded by (21).
The value m=2 is included; the series at zero converges absolutely.

The fixed arithmetic constant is exactly

 C0=47/64-(21/64)(gamma_E+log pi)+(115/96)log2
                           -(641/1728)log3-(65/192)log5.

Its parent derivation cancels P2 and retains both activated primes 2 and 3.
A fresh interval evaluation proves 0<C0<237/5000. The checker authenticates
the unchanged parent primitive source, re-evaluates the constant, and does
not assume a stored decimal for it.

Apply (12) at x=2log m and use cosh(log m)=(m+1/m)/2. Equations (18)--(21)
and D(m)=1/4-V(2log m)-E(m^2) prove the parameterized inequality

 D(m)>=1/4-C0-E(m^2)
                -(85/64)(m+2+1/m)Rbar(H).                (22)

Platt--Trudgian Theorem 1 proves the needed finite-height premise at
3,000,175,332,800; its restriction to H=3,000,000,000,000 is all we use.
This is the sole finite-zero-verification input. Neither their simplicity
statement nor an interval file for any specific zero is used. Combining
(19), (21), and C0<237/5000 proves (3).

## 5. Four rational endpoint budgets cover the whole continuum

The function m+2+1/m is increasing on m>=2, whereas m^-5 decreases. To prove
D>1/10 up to M_1=5*10^10, use the following two lower bounds:

 1/4-237/5000-205/(128*2^5)
                     -(85/64)R0*(4+2+1/4),
 1/4-237/5000-205/(128*4^5)
                     -(85/64)R0*(M_1+2+1/M_1),           (23)

where R0=37/(25*10^12). They cover [2,4] and [4,M_1] respectively, and
both exceed 1/10 by exact rational arithmetic.

For D>1/200 up to M_2=10^11, replace the split point 4 by 16 and the two
intervals by [2,16] and [16,M_2]. Both exact lower bounds exceed 1/200.
The smaller large-range budget exceeds 0.0060359. Nothing is sampled between
endpoints: monotonicity proves complete coverage of the intervals. This
establishes (4) without evaluating one of the huge finite arithmetic sums.

For all m>=2, multiplication of (3) by 192m^3 gives (5), since

 255R0=1887/(5*10^12),
 192*(237/5000+205/4096)+(1275/2)*R0 < 19.                (24)

The contribution (1275/2)R0 bounds 255R0(2+1/m), and (21) is bounded by
its m=2 value. This is an all-scale lower bound, but the loss in its leading
coefficient is fixed and positive. In particular it does not pay the
parent's eventual inequality at arbitrarily large m. No limiting operation
sending H to infinity is licensed by the one imported finite-height theorem.

## 6. HT4: prime squares contribute a fixed leading drift

The direct arithmetic attack must not discard prime powers. Write

 P(m^2)=P_pr(m)+P_sq(m)+P_hi(m),
 P_pr(m)=(1/m)sum_p log p*w(p/m^2),
 P_sq(m)=(1/m)sum_p log p*w(p^2/m^2),
 P_hi(m)=(1/m)sum_(p,k>=3)log p*w(p^k/m^2).               (25)

Each part is nonnegative. Let theta(y)=sum_(p<=y)log p and g(v)=w(v^2).
The ordinary, unconditional PNT, theta(y)=y+o(y), implies

 P_sq(m)->integral_(1/2)^2 g(v)dv=49/288.                 (26)

This is an application of PNT, not a new PNT proof or an effective rate.
Indeed P_sq=(1/m)integral g(v)d theta(mv), and integration by parts gives

 |P_sq(m)-49/288| <= (21/(32m))
                 sup_(m/2<=y<=2m)|theta(y)-y|.             (27)

The total variation of g is 2g(1)=21/32; its endpoints are zero. The two
halves of the integral in (26) are EACH 49/576, by integrating v^2/3-v^-4/192
on [1/2,1] and v^-4/3-v^2/192 on [1,2]. The equality also follows from the
self-reciprocity in (1). Bound (27) justifies the uniform scaled convergence.

### 6.1 The entire higher-power remainder is paid

For every real y>=1, theta(y)<3y. To see this, each prime between 2^(j-1)
and 2^j divides binomial(2^j,2^(j-1)); its logarithm is less than 2^j log2.
Sum these dyadic estimates to the least power of two >=y. The result is
less than 4y log2<3y. This elementary bound uses no PNT.

Put Y=4m^2. From (1), every term in P_hi is at most (21/(64m))*log p.
The k=3 row has total log weight <3Y^(1/3). There are at most
log Y/log2 rows with k>=4, each with total log weight <3Y^(1/4). Therefore

 0<=P_hi(m)<=(63/(64m))*[Y^(1/3)+(log Y/log2)Y^(1/4)].     (28)

This controls ALL k>=3, not only a fixed finite collection. It is
O(m^(-1/3)+m^(-1/2)log m), hence tends to zero. Under PNT, the cube row
has the more precise asymptotic

 P_hi(m) ~ (3/20)*[65/64-(2^(1/3)+2^(-1/3))/8]*m^(-1/3). (29)

For the cube row, change p=m^(2/3)v and use the same partial-summation
argument. The coefficient is (1/3)integral_(1/4)^4 w(u)u^(-2/3)du,
equal to the coefficient displayed in (29). Rows k>=4 are
O(m^-1/2 log m)=o(m^-1/3) by (28). The Mellin integral is elementary:

 J(rho)=integral_(1/4)^4 w(u)u^(rho-1)du
       =A(rho-1/2)/[b^2-(rho-1/2)^2],                    (30)

with removable values at rho=-1,2. At rho=1/3 this gives (29).
No expansion of P_sq beyond (26) is asserted. In particular, its
unconditional PNT error cannot simply be placed below the cube term.

## 7. HT5: a prime-only reformulation with the correct offset

Define

 D_pr(m)=P_pr(m)-45m/128+121/288.                          (31)

Since 121/288=1/4+49/288, (25)--(28) give

 D_pr(m)-D(m)->0.                                         (32)

The constant prime-square drift is thereby paid, rather than silently
lost by replacing Lambda with primes. The following is a correctly scoped
reformulation of the parent's theorem:

 RH iff D_pr(m)>=0 for every sufficiently large integer m. (33)

For necessity, under RH the parent gives D(m)>1/10 for every m>=2, and
(32) then gives eventual D_pr>0. For sufficiency no PNT error estimate is
needed: P_sq+P_hi>=0 implies D(m)>=D_pr(m)-49/288. Thus (31)>=0 gives a
fixed lower bound for D at every sufficiently large square sample. The
parent's unconditional square interpolation and one-sided Landau theorem
then exclude every off-line zero. These exact dependencies are not newly
proved by the finite checker. This is NOT a claim that (31)>=0 has been
established at unbounded m, nor that its eventual threshold is effective.

## 8. HT6: what the direct prime-discrepancy attack still requires

Let Epsi(y)=psi(y)-y, where psi(y)=sum_(n<=y)Lambda(n). Exact Stieltjes
integration by parts in (2), with the compact endpoints retained, gives

 D(m)=1/4-(1/m)integral_(1/4)^4 w'(u) Epsi(m^2 u)du.      (34)

There is no delta at u=1: w is continuous there, although w' jumps.
The two ordinary derivative pieces are

 w'(u)=1/3+1/(96u^3)>0,       1/4<u<1;
 w'(u)=-2/(3u^3)-1/192<0,     1<u<4.                      (35)

Thus the desired unbounded bound is the assembled SIGNED comparison
integral w'(u)Epsi(m^2u)du <= m/4, eventually. Taking absolute values
before combining the two sides loses the cancellation. The elementary
variation bound gives only

 |D(m)-1/4| <=(21/(32m))
              sup_(m^2/4<=y<=4m^2)|psi(y)-y|.             (36)

Even an RH-style pointwise O(sqrt y log^2 y) estimate inserted here gives
O(log^2 m), not a constant margin. This does not refute the scalar bound;
it identifies the waste in this particular domination. Ordinary PNT is
weaker at this absolute scale. The tail theorem (3) instead preserves the
fixed spectral mass and controls the complete unverified complement, which
is why it proves a constant margin over its finite stated range.

The attempted completion was to use (34) and the explicit prime-square
correction to propagate the lower bound. No sign/monotonicity principle
for the actual two-sided discrepancy in (34) was proved. A nonnegative
prime-power measure by itself does not give that principle; the parent's
source-preserving countermodel retains a PNT asymptotic while violating
it at large scales. The literal arithmetic premise remains OPEN.

## 9. Scope of the advance

The first new conclusion is a proved actual-scalar bound through a very
large continuum range, using one named external finite-height theorem and
a complete unconditional complement bound. It is not 10^11 separate
computations, a new zero-free region, an independent reproduction of the
external verification, or positivity of the full W form on longer windows.
The second conclusion is the exact prime-square drift and the all-exponent
higher-power estimate. It isolates the prime-only difficulty with correct
normalization but does not solve it.

The methods are classical explicit-formula transfer, Jensen/Backlund
counting, partial summation, and Chebyshev/PNT prime-power separation.
Platt--Trudgian already discuss finite-RH transfer to prime estimates. No
external novelty, optimal range, record, or effective all-scale error
exponent is claimed. Independent mathematical review remains required.
