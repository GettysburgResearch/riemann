# Growing-shift maximal cancellation for the actual power-completed sources

Status: PROPOSED unconditional deductions with complete proofs below; not independently reviewed.
The deep bounded-function estimate is imported from Matomaki--Radziwill--Tao (MRT),
*An averaged form of Chowla's conjecture*, arXiv:1503.05121v3, Theorem 1.7 and
its displayed estimate (1.12). No ordinary-Chowla preprint, QRH, GRH, or unknown
native moment is a premise. This is a theorem over the rational integers, not
an identification with the CT theta family or with Eisenstein norm coefficients.

The contribution relative to recovered #956 is a quantitative estimate for a
GROWING set of shifts, with a maximum over all summation endpoints. It is uniform
in the unbounded power degree and powerful-prime profiles. The rate is logarithmic,
not the power saving needed to prove RH. Classical short-sum/Fourier ideas and
MRT's cancellation are credited; no global literature priority is asserted.

## 1. Main statements and exact quantifiers

Fix a finite set S of rational primes and a Dirichlet character xi modulo Q0,
with every prime divisor of Q0 included in S. For m>=2 and arbitrary |z_p|<=1,
choose ONE of the following local coefficient families outside S:

    native:       1-xi(p)x;
    coupled:      1-(1-1/p)xi(p)x-z_p p^(m/2-1)x^m;
    two-channel:  (1-xi(p)x)(1-z_p p^(m/2-1)x^m);
    geometric:    1-(1-1/p)xi(p)x/(1-z_p p^(m/2-1)x^m).       (1)

At p in S the entire factor is 1. Let F(n) be the multiplicative coefficients.
These are formal local series; no critical-line Euler-product convergence is
assumed. All shared-prime terms required by (1) remain. m is an ALGEBRAIC degree,
not an assertion about the existence of an automorphic cover.

Put e(t)=exp(2 pi i t), and, for real 10<=H<=X, write

    r(H,X)=log log(3H)/log(2H) + (log(2X))^(-1/700).          (2)

Integer X,H suffice for the correlation conclusions. Constants below may depend
on S and xi, but not on m, the z_p, H, X, or the selected family.
They are not uniform in growing ordinary Dirichlet conductors or growing S.
The supremum over profiles permits m and z to be chosen afresh at each X,H.

**Theorem A (uniform short-Fourier square bound).** For X>=H>=10,

    sup_alpha integral_R |sum_(x<n<=x+H, n<=X) F(n)e(alpha n)|^2 dx
                         <= C_(S,xi) X H^2 r(H,X).          (3)

The frequency supremum is OUTSIDE the x integral. Moving it inside is neither
claimed nor used. The source contains all integers up to X, with the literal masks.

**Theorem B (complete growing-shift correlations against an L2 test).**
Let X,H be integers with 10<=H<=X. Let G be ANY complex sequence on [1,2X]
with sum |G(n)|^2 <= A X, where A>=0. G need not be multiplicative or bounded.
Define the complete ordinary correlation prefix

    C_h(Y)=sum_(1<=n<=Y) F(n) conjugate(G(n+h)), 0<=Y<=X.     (4)

Then

    sum_(h=1)^H |C_h(X)|^2 <= C_(S,xi) A H X^2 r(H,X),       (5)
    sum_(h=1)^H max_(0<=Y<=X) |C_h(Y)|^2
                         <= C_(S,xi) A H X^2 r(H,X)^(1/2). (6)

Consequently,

    sum_(h=1)^H max_(0<=Y<=X) |C_h(Y)|
                         <= C_(S,xi) sqrt(A) H X r(H,X)^(1/4). (7)

All maxima over Y are over integer endpoints. Every term is retained; no
coprimality condition on n,n+h is inserted. There is no Mellin-twist average,
prime randomization, or logarithmic weight 1/n in (4)--(7).

Taking G to be any other family in (1), with possibly different m, S, xi and
powerful phases, is legitimate with A=2 zeta(2). Only the first source's fixed
S,xi enter the cancellation constant. The second source needs only its square
prefix bound. In particular, for EVERY H(X)->infinity with H(X)<=X, (7) is
uniformly o(HX), even if either algebraic degree tends to infinity.
A fixed h theorem is not inferred from this average.

**Corollary C (a growing band in the actual Gaussian kernel).** With two sources
F_1,F_2 as above, the kernel from #952 is

    K_D(v,w)=kappa_c/sqrt(vw) exp[-log(v/w)^2/8]
                     Phi(log D-log(vw)/2-(2c-1)),
    kappa_c=exp((2c-1)^2/2)/(2 sqrt(2pi)).                    (8)

For integer D>=H>=10 and fixed real c,

    sum_(h=1)^H |sum_(D<n<=2D) F_1(n)conjugate(F_2(n+h))K_D(n,n+h)|
                              <= C_(S_1,xi_1,c) H r(H,D)^(1/4). (9)

This is the complete n-shell and shift band specified in (9), with genuine
signed cancellation before the outer absolute value. It is NOT the whole
cumulative energy or a bound after discarding the other Gaussian shells.
At H=D^theta, 0<theta<=1, the displayed guarantee is only
O(D^theta (log D)^(-1/2800)); it is not D^epsilon for every epsilon>0.

## 2. Source decomposition and the square-integrable powerful tail

Write v(r)=product_(p|r)(1-1/p) and a=m/2-1. For all four sources, every supported
integer has a UNIQUE representation n=r d^m:

- coupled: r,d squarefree and coprime;
  coefficient mu(r)xi(r)v(r) mu(d)z(d)d^a;
- two-channel: r,d squarefree, WITHOUT coprimality;
  coefficient mu(r)xi(r) mu(d)z(d)d^a;
- geometric: r squarefree, d arbitrary, rad(d)|r;
  coefficient mu(r)xi(r)v(r) z(d)d^a;
- native: d=1 and r squarefree, coefficient mu(r)xi(r).

All parameters avoid S. The uniqueness is a valuation check: exponents are
respectively {0,1,m}, {0,1,m,m+1}, and {0,1,1+m,1+2m,...}.
It also holds at m=2. In particular shared primes in the two-channel and
geometric sources must not be removed.

Let F_R retain exactly the terms with d<=R, for integer R>=1. Since the d
supports are disjoint and |F(r d^m)|^2<=d^(m-2), elementary counting gives

    sum_(n<=T)|F(n)|^2 <= zeta(2)T,
    sum_(n<=T)|F(n)-F_R(n)|^2 <= T sum_(d>R)d^-2 <= T/R.  (10)

This is #956 Lemma 3.1, reconstructed here, not a new coefficient count.
No prime distribution input is needed. The inequality sum_(d>R)d^-2<=1/R
is used only for INTEGER R.

Each d-component can equivalently be written

    F_d(n)=gamma_d 1_(t_d|n) g_d(n/t_d).                  (11)

For coupled and two-channel t_d=d^m and gamma_d=mu(d)z(d)d^a.
For coupled, g_d=mu xi v 1_(coprime to dS); for two-channel,
g_d=mu xi 1_(coprime to S), without a d mask.
For geometric,

    t_d=d^m rad(d),
    gamma_d=mu(rad d)xi(rad d)v(rad d)z(d)d^a,
    g_d=mu xi v 1_(coprime to dS).

The native component is t_1=gamma_1=1. Components incompatible with S are zero.
All g_d are one-bounded. Crucially, for every nonzero component,

    |gamma_d|/sqrt(t_d)<=1/d,
    |gamma_d|/t_d<=1/d^2.                               (12)

The second estimate uses m>=2. These two weights serve different purposes.
Confusing the t^-1/2 energy Jacobian with the t^-1 normalized short-sum weight
would invalidate the proof.

## 3. Precisely the external cancellation input used

MRT v3 Theorem 1.7 states, for any one-bounded multiplicative b, Y>=L>=10,

    sup_alpha integral_0^Y |sum_(x<n<=x+L)b(n)e(alpha n)| dx
       <= C Y L { exp[-M(b;Y,Q)/20] + log log L/log L
                                      + (log Y)^(-1/700) },
    Q=min((log Y)^(1/125),(log L)^5).                    (13)

M is the infimum of the pretentious squared prime distance from chi(n)n^(it)
over q<=Q and |t|<=Y. Its summands use 1-Re(b(p)conjugate(chi(p)p^(it)))/p.
MRT (1.12), on printed page 6, gives for lambda, and hence for mu at primes,

    M(mu;Y,Q) >= (1/4)log log Y-C                       (14)

for large Y, uniformly for Q<=(log Y)^(1/125). We deliberately use 1/4 rather
than the sharper 1/3-epsilon there. These are established external estimates;
this note neither re-proves MRT nor uses a QRH strip instead of its inputs.

The relevant untwisted bounded cores are

    b_d(n)=mu(n)v(n)^epsilon 1_((n,d product(S))=1), epsilon=0 or 1.

At each unmasked prime their difference from mu is at most 1/p. At a masked
prime the difference is at most 1. Thus, uniformly over the testing characters,
frequencies and Y,

    M(b_d;Y,Q)>=M(mu;Y,Q)-C_S-sum_(p|d)1/p.              (15)

An elementary estimate suffices for the last sum:

    sum_(p|d)1/p <= C+log log(3d).                       (16)

For log d>=2, split at log d. Bounding the small primes by ALL integers costs
at most log log d+C. There are at most log d/log 2 prime divisors above that
threshold, whose reciprocal sum is at most 1/log 2. Bounded d is absorbed.
No short-interval prime theorem is hidden here.

The fixed xi is dealt with by its finite additive Fourier expansion modulo
Q0. The sum of the absolute Fourier coefficients is at most sqrt(Q0), by
Parseval and |xi|<=1. It costs only a fixed constant in (13), without changing
Q or moving a frequency supremum inside an integral.

## 4. Bounded cores with actual hard endpoints

For a finite sequence b supported on [1,Y], define

    V_b(L,alpha)=integral_R |sum_(x<n<=x+L)b(n)e(alpha n)|^2 dx. (17)

For g_d truncated at Y and 10<=L<=sqrt(Y), one has

    V_(g_d 1_[1,Y])(L,alpha)
      <= C_(S,xi) Y L^2 { exp[-M(b_d;Y,Q)/20]
                       + log log L/log L+(log Y)^(-1/700)+L/Y }. (18)

Proof: at most L+1 integers occur in each window, so its square is bounded
by (L+1) times its absolute value. Except on two endpoint strips of total
length at most 2L, the truncated sum agrees with the sum in (13), or is zero.
Those strips cost O(L^2) in L1. Multiply by L+1 and use (13), including the
fixed-character Fourier expansion. This proves (18).

For a longer window h<=Y partition it into J=ceil(h/sqrt(Y)) equal intervals,
each of length ell=h/J (take J=1 if h<=sqrt(Y)). Minkowski and translation
invariance of the x integration give

    V_b(h,alpha)^(1/2)<=J V_b(ell,alpha)^(1/2).           (19)

If h>sqrt(Y), ell is between sqrt(Y)/2 and sqrt(Y). Thus we never pay an
uncontrolled endpoint error H/Y when H is comparable with Y. Small Y or
ell<10 are covered by a fixed enlargement of constants.

We will apply this when

    d<=R=floor(log(2H)), t_d<=sqrt(H),
    Y=X/t_d>=sqrt(X), h=H/t_d>=sqrt(H), H<=X.            (20)

The ell in (19) is then at least H^(1/4)/2. From (14)--(16), the exponential
term in (18) is at most

    C_S (log(3R))^(1/20) (log Y)^(-1/80)
                                   <= C_S (log(2X))^(-1/700). (21)

The final comparison uses Y>=sqrt(X), R<=log(2X), and the fixed strict
exponent gap 1/80-1/700; powers of log log X are absorbed in that gap.
Also log log ell/log ell <= C log log(3H)/log(2H) and ell/Y<=Y^-1/2.
Consequently (18)--(21) give, uniformly in the dense components (20),

    V_(g_d 1_[1,Y])(h,alpha)<=C_(S,xi) Y h^2 r(H,X).     (22)

All statements here are for real window lengths, so no unpriced rounding
error occurs in the division by t_d or J.

## 5. Proof of Theorem A: dense dilations, sparse dilations, and tail

Fix R=max(1,floor(log(2H))). For a dilation component in (11), substitution
x=t_d y gives the EXACT identity

    V_(F_d 1_[1,X])(H,alpha)
       =|gamma_d|^2 t_d
          V_(g_d 1_[1,X/t_d])(H/t_d,alpha t_d).          (23)

For t_d<=sqrt(H), use (22) and then the second bound in (12). Minkowski shows
that all these components together have root norm at most

    C_(S,xi) sqrt(X)H sqrt(r(H,X)) sum_(d<=R)|gamma_d|/t_d
                  <= C_(S,xi) zeta(2) sqrt(X)H sqrt(r(H,X)). (24)

For the other retained components, t_d>sqrt(H), do NOT apply a long-interval
cancellation theorem at the possibly microscopic length H/t_d. Direct counting
instead gives

    V_(F_d 1_[1,X])(H,alpha)
       <= |gamma_d|^2 (H/t_d+1) H floor(X/t_d).          (25)

Each occupied base integer contributes over an x interval of length H.
If t_d>X the component is empty. Otherwise its normalized root bound is

    V_d^(1/2)/(sqrt(X)H)
       <= (|gamma_d|/sqrt(t_d)) sqrt(1/t_d+1/H)
       <= d^-1(H^-1/4+H^-1/2).                          (26)

Their total root cost is at most C(1+log R)H^-1/4.
This explicit sparse regime is why the final theorem is uniform even when
m grows; one cannot assume H/d^m tends to infinity for every d<=R.

Finally for the omitted sequence T=F-F_R, a window contains at most H+1
integers. Cauchy, Fubini, and (10) give

    V_(T 1_[1,X])(H,alpha)
       <=H(H+1)sum_(n<=X)|T(n)|^2 <=2XH^2/R.           (27)

The sum of (24), (26), and (27) in root norm is at most

    C sqrt(X)H [ sqrt(r)+(1+log R)H^-1/4+R^-1/2 ].       (28)

The square of the bracket is O(r(H,X)) for H>=10. This proves (3), uniformly
in m and every powerful profile. The proof uses actual support decomposition,
not boundedness incorrectly asserted for F. QED.

We need one endpoint-uniform consequence. For every integer 0<=Y<=X,

    sup_alpha V_(F 1_[1,Y])(H,alpha)<=C XH^2 r(H,X).     (29)

If Y>=sqrt(X) and H<=Y, this follows from (3). If H>Y, split H into equal
windows between Y/2 and Y and use (19); their rate is comparable to r(H,X),
since sqrt(X)<=Y<=H<=X. If Y<sqrt(X), use (10) and window Cauchy: for H<=Y
the normalized cost is O(Y/X)<=O(X^-1/2); for H>Y it is
O(Y^2/(XH))<=O(1/H). Both are O(r). Also

    V_b(2H,alpha)<=4 V_b(H,alpha)                        (30)

for every finite sequence, by splitting into two translated H-windows.
These statements do not use a maximum inside MRT's integral.

## 6. Mixed Fourier identity and proof of (5)

Extend f(n)=F(n)1_[1,Y] and g(n)=G(n)1_[1,2X] by zero on Z. For L>0 let

    S_f(x,alpha)=sum_(x<n<=x+L) f(n)e(alpha n),
    J_fg(alpha)=integral_R S_f(x,alpha)conjugate(S_g(x,alpha))dx.

Finite expansion, followed by ordinary Fourier orthogonality, gives

    J_fg(alpha)=sum_h (L-|h|)_+ C_h(Y)e(-alpha h),
    integral_0^1 |J_fg(alpha)|^2 d alpha
                    =sum_h (L-|h|)_+^2 |C_h(Y)|^2.      (31)

This is the mixed version of MRT Lemma 1.4; the elementary extension is
proved by the displayed expansion, not imported as a new theorem.
Pointwise Cauchy in x gives |J_fg|^2<=V_f V_g. Parseval and Fubini give

    integral_0^1 V_g(L,alpha)d alpha=L sum_n |g(n)|^2.   (32)

Take L=2H. For 1<=h<=H the squared weight in (31) is at least H^2.
Apply (29)--(30) to f and (32) to g. Thus, UNIFORMLY over every endpoint Y,

    sum_(h=1)^H |C_h(Y)|^2
                    <= C_(S,xi) A H X^2 r(H,X).         (33)

This proves (5) and a common-endpoint estimate. The endpoint maximum in (6)
requires a separate argument; it does not follow by interchanging max and sum.

## 7. A square-mass partition handles the endpoint maximum, including spikes

Write V=sum_(n<=X)|F(n)|^2 and W=sum_(n<=2X)|G(n)|^2. If either is zero all
claims are identities. Fix any integer J>=1. Declare an index heavy when
|F(n)|^2>V/J; there are fewer than J such indices. The other indices are light.
Greedily partition [1,X] into consecutive intervals whose LIGHT square mass
is at most 2V/J: end a bin when its light mass first reaches V/J. Every light
atom is at most V/J, so this upper bound holds and there are at most J+1 bins.
The partition and its at most J+2 endpoints may depend on F. Estimate (33)
already holds at EVERY endpoint, so this selection causes no new premise.

For an endpoint Y within one bin, split C_h(Y) into the correlation at the
preceding grid endpoint, the light part of the remaining bin, and its heavy
part. For each h, the light error is at most sqrt(2VW/J), by Cauchy; replacing
the bin by the full support in the G square sum is a legitimate upper bound.
For the heavy error use

    max_Y |sum_(heavy n<=Y)F(n)conjugate(G(n+h))|^2
                  <= J sum_(heavy n)|F(n)|^2 |G(n+h)|^2.

After summing h, each G block is at most W. Thus the heavy contribution is
at most JVW. This is essential: uniform pointwise boundedness of F is false.
Taking (a+b+c)^2<=3(a^2+b^2+c^2), summing the grid bounds (33), and using
V<=zeta(2)X, W<=AX, gives

    sum_(h=1)^H max_Y |C_h(Y)|^2
          <= C_(S,xi) A HX^2 [J r + 1/J + J/H].         (34)

If r>=1 a direct Cauchy bound proves (6). If r<1 choose an integer J
comparable with r^-1/2. Since Hr(H,X)>=1 for H>=10, every term in (34)
is O(sqrt(r)). This proves (6). Cauchy in h gives (7). QED.

Unlike an unqualified maximal Fourier estimate, this argument puts the maximum
only over the correlation's summation ENDPOINT. It does not optimize the
exponential frequency separately at each short interval. Nor does it apply
one fixed-shift result to a varying shift without uniform estimates.

## 8. Gaussian shell and the remaining RH scale

For D<n<=2D and 0<=h<=D, (8) has the form

    K_D(n,n+h)=D^-1 k_c(n/D,h/D),

where k_c and its first derivative in the first argument are bounded on
[1,2]x[0,1]. This follows directly from the smooth Gaussian/CDF formula;
all norms are bounded away from zero on this compact set. Therefore its
supremum plus total variation in n is O_c(D^-1), uniformly in h.
Partial summation and (7), with X=2D and the second sequence restricted
through 4D, prove (9). The difference of two correlation prefixes costs at
most twice their maximum; no further uniform-in-h derivative assumption is used.

For H=D^theta the second summand of r dominates eventually, so (9) gives
O(D^theta (log D)^(-1/2800)). This is genuine logarithmic cancellation in
a growing fixed-twist band. It does not give the subpower total covariance
required by #952's critical-energy criterion. Summing over O(D) shifts still
leaves a power-scale upper bound. The loss cannot be removed by calling the
terms 'almost all small', or by applying (7) separately to every individual h.

Likewise this proof does not identify rational F with the aggregated Eisenstein
norm coefficients, whose ordinary prime values include -2 at split primes.
MRT cannot be applied to that unbounded prime profile by the powerful-tail
argument above. No all-number-field improvement on proposed #959 follows.

## 9. Current-source audit and precise scope of success

The preceding 13-file mesoscopic and 11-file affine packets were already
published in #956 at 943d7714f81b97a75652ebc6e19990a88c917d4d. This pass preserves
them and adds a new packet; it does not recreate their recovery commit.

The latest #959 at 7b845294207d96b883c1fa95028663082267804f proposes the strict
11/12 all-number-field region from CT/DF/BGL. Its live proof and source map
were read for the analytic interfaces and ceiling. Its own bound

    S_theta=(1-alpha)/6-(M-1)/2, M>1, beta<=alpha,

has supremum 1/12 as M->1+ and alpha->1/2+. That is a ceiling of those
positive upper estimates, not a theorem that the true signed pairing has
such a lower bound. Improving density bins alone does not prove RH.
The current pass neither independently certifies nor strengthens #959.
Direct CT v2 and DF retrieval failed in this session, so no fresh-primary
CT/DF audit is claimed. They are not inputs to Theorems A--C.

The actual new result is (6)--(7): a complete, ordinary, endpoint-maximal,
growing-shift theorem uniform in all algebraic degrees and powerful profiles,
based on an established external short-sum estimate and a fully stated adapter.
No full proof of RH, fixed-row sextic moment hierarchy, or new zero-free
exponent has been obtained in this pass.
