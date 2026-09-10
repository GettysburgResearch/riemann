# BHH26: eventual critical-line zeros at every finite branching depth

Date: 2026-09-10. **PROPOSED complete component proofs; independent analytic
review required. RH and cofinal confinement in the remaining bounded windows
are NOT proved.** No numerical zero is an input to these theorems.

This continues the prescribed Gamma(5/2, rate 5/2) Brownian branching orbit in
PR #857, frozen at `3f1984867d23b588d09c88a892882411724b174b`. The source,
reflection and normalization are unchanged. This is NOT a claim that its
entire approximants have only critical-line zeros in the whole plane.

The result is positive and all-depth: for EACH finite depth n, an explicit
rationally computable T_n excludes all off-central critical-strip zeros above
T_n, and all remaining high critical-line zeros are simple. The finite interval
below T_n is NOT covered. T_n grows rapidly with depth; interchanging the two
quantifiers would be invalid and would manufacture an RH proof.

## 1. Source, exact factorization and statement

Put k=5/2. Use independent copies in the recursion

    X_0 ~ Gamma(k, rate k),
    X_(n+1) = (X_n+X_n')/U^2,   U ~ Uniform[1,2].                 (1)

The SAME independent U divides both children. Set c_base=pi/15 and

    M_n(s)=E[(pi/6)(X_n+X_n')]^(s/2),
    H_n(s)=[M_n(s)+M_n(1-s)]/[2(1+M_n(1))].                     (2)

Powers use the real logarithm on positive variables. The denominator is a
strictly positive real number.

For a_n=k*2^n define Z_0=1 and, independently,

    B_n ~ Beta(a_n,a_n),
    C_n=B_n Z_n+(1-B_n)Z_n',    Z_(n+1)=C_n/U^2.                 (3)

Gamma--beta change of variables proves

    X_n = G_n Z_n,  G_n ~ Gamma(a_n, rate k), G_n independent of Z_n;
    X_n+X_n' = Ghat_n C_n, Ghat_n ~ Gamma(2a_n, rate k);
    4^-n <= Z_n,C_n <=1.                                      (4)

Indeed G+G' is independent of G/(G+G') for two equal-rate gamma variables;
those variables have the stated gamma and beta laws. Induction then proves
(4), including all dependence conventions. Thus, with A_n=2a_n=5*2^n,

    M_n(s)=c_base^(s/2) Gamma(A_n+s/2) E[C_n^(s/2)]/Gamma(A_n).     (5)

The right side is holomorphic on the closed critical strip and on a larger
open neighborhood. The gamma-free entire representative from #857 is

    E_n(s)=Gamma(A_n+1/4)^2 H_n(s)
                    /[Gamma(A_n+s/2)Gamma(A_n+(1-s)/2)].       (6)

The expression is interpreted through the explicit sum of reciprocal-gamma
terms, so it is entire. Its multiplier is nowhere zero on 0<=Re s<=1; hence
it has exactly the same zeros as H_n there, with multiplicity.

### BHH1: explicit eventual confinement

The rational recurrence in Section 5 defines an integer T_n for EVERY n>=0.
For that integer,

    H_n(s)=0, 0<=Re s<=1, |Im s|>=T_n
        ==> Re s=1/2 and the zero is simple.                  (7)

The same assertion holds for E_n. In particular every fixed iterate has only
FINITELY MANY off-central zeros in the closed critical strip. The construction
actually proves a strictly positive horizontal log-modulus-ratio derivative
above T_n, not just a sampled zero count.

Some deliberately conservative cutoffs are

    T_0=320,
    T_1=279109,
    T_2=1788260812445057,
    T_3=3097471590717602242860533234898291413963.               (8)

They are arithmetic outputs of the proof's norm majorants, NOT heights of
numerically verified zero censuses. The old negative derivative at depth one
and height 23 is below T_1 and is fully compatible with this theorem.

### BHH2: complete high-height counting law for a fixed iterate

Let N_n(R) count zeros of H_n in 0<Re s<1, 0<Im s<=R, with multiplicity.
For each FIXED n,

    N_n(R) = [R/(2pi)] log[pi R/(30 e 4^n)] + O_n(1),
                                                     R -> infinity. (9)

The same law holds if only critical-line zeros are counted, since the others
are finite. The O_n constant, gamma parameters and onset are depth-dependent.
This is a zero-count theorem for finite approximants, not the Riemann--von
Mangoldt formula for xi and not a claim that its errors are uniform in n.

## 2. Distributional derivatives retain the complete mixing law

Measures in this section are finite signed real Borel measures on R. Their
norm ||rho|| is total variation. A density h belongs to BV if its extension
by zero has finite distributional derivative Dh; write V(h)=||Dh|| and
L(h)=integral |h|. All supports lie inside a fixed positive compact interval
at a given depth. Distributional derivatives and convolutions can therefore
be tested against compactly supported smooth functions without endpoint-at-zero
or infinity ambiguities. S_b denotes pushforward under x -> b x.

### 2.1 Beta averaging squares the diagonal atoms

Suppose d>=0 is an integer, mu is a compactly supported probability measure,
and

    D^d mu = c eta,
    eta = sum_i r_i delta_(x_i) + h(x)dx,
    c>0, h in BV, x_i distinct and positive.                    (10)

Let B~Beta(a,a), a>d+1, and let Y=BZ+(1-B)Z' for independent copies of mu.
Put

    p=a-d>1,
    kappa=B(p,p)/B(a,a).

Differentiation under the beta integral and the scaling identity
D^d(S_b mu)=b^-d S_b(D^d mu) give the EXACT measure identity

    D^(2d) Law(Y) = kappa c^2 sigma,
    sigma=integral_0^1 (S_b eta * S_(1-b) eta) beta_(p,p)(b)db. (11)

The integral exists in total variation: before normalization its majorant is
c^2||eta||^2 b^(a-d-1)(1-b)^(a-d-1)/B(a,a), which is integrable.
The derivative is split d times onto EACH independent child, not 2d times
onto an undeclared singular factor.

In (11), matching atoms x_i=x_j remain at x_i for EVERY b. Distinct atoms
produce x_j+b(x_i-x_j), a nondegenerate affine beta distribution. Every term
containing a density is absolutely continuous. Consequently

    sigma = sum_i r_i^2 delta_(x_i) + g(x)dx,  g in BV.        (12)

This squares the SIGNED atom coefficients; the diagonal masses in (12) are
positive. All mixed terms remain in the signed density g. They are not set
to zero or asserted positive.

Here are explicit sufficient norm bounds. Let

    A=sum_i |r_i|, L>=L(h), V>=V(h),
    Q=(A+L)^2,
    G=Q-sum_i r_i^2,
    W=2p sum_(i!=j)|r_i r_j|/|x_i-x_j|
             +[(2p-1)/(p-1)](2A+L)V.                         (13)

Then ||sigma||<=Q, L(g)<=G, V(g)<=W.

For the variation estimate, the symmetric beta density has maximum at 1/2,
and that maximum is at most p. In fact

 B(p,p) >= 2*(1/2)^(p-1) integral_0^(1/2) x^(p-1)dx
          = 2^(2-2p)/p.

It vanishes at both endpoints because p>1. Its total variation is therefore
at most 2p. The off-diagonal affine beta terms give the first term in W.
For a scaled density, V(b^-1 h(./b))=b^-1 V(h). Convolution with a measure
costs its total variation; integration uses

    E_(Beta(p,p))(1/B)=(2p-1)/(p-1).

The two atom/density terms and one density/density term give the second term
in W. These arguments include endpoint variation of every zero-extended
function and all mixed pair terms.

### 2.2 The common uniform scale turns atoms into a finite difference

Let sigma be any finite signed measure supported in [b,1], b>0, and m>=0.
Define Omega_m sigma = integral_1^2 u^(2m) S_(u^-2) sigma du. It has density

 J_m(x)=integral [t^(m+1/2)/(2 x^(m+3/2))]
                     1_(t/4<x<t) sigma(dt).                   (14)

This follows by the substitution u=sqrt(t/x), including its Jacobian.
Endpoint values of a density do not matter; all derivative atoms do.
For one atom at t, the distributional derivative of its contribution is

 (4^(m+1)/t)delta_(t/4) - (1/(2t))delta_t
                   -(m+3/2) J_m(x)/x dx.                    (15)

Hence (14) is BV, and

    L(J_m)<=4^m ||sigma||,
    V(J_m)<=2*4^(m+1)||sigma||/b.                             (16)

The latter counts the lower jump, the full monotone decline and the upper
jump; for a single positive atom their total is twice the lower endpoint.
For sigma=sum s_i delta_(x_i)+g dx, the non-atomic part of 2D(Omega_m sigma)
is exactly

 h_new(x)=-(2m+3)J_m(x)/x
              +2*4^(m+1)g(4x)/x-g(x)/x.                    (17)

It is BV. Equation (15), not a formula without the common-U boundary terms,
determines its atomic part.

For use below, put Q>=||sigma||, G>=L(g), W>=V(g),
J=4^m Q and VJ=2*4^(m+1)Q/b. Then explicit bounds for (17) are

 L_new=(2m+3)(4/b)J +(2*4^(m+1)+1)G/b,
 V_new=(2m+3)[(4/b)VJ+(16/b^2)J]
          +2*4^(m+1)[(4/b)W+(4/b^2)G]+W/b+G/b^2.          (18)

For example, variation of J_m/x is at most (4/b)V(J_m)+(16/b^2)L(J_m).
For g(4x)/x use (4/b)V(g)+(4/b^2)L(g). This proves every term of (18).
No smoothness of an unexpanded probability density is assumed.

## 3. The all-depth atomic polynomial and its zero bound

Put

    d_n=2^n-1, x_j=4^-j,
    p_n=a_n-d_n=(3/2)2^n+1,
    kappa_n=B(p_n,p_n)/B(a_n,a_n),
    c_0=1, c_(n+1)=kappa_n c_n^2/2.                         (19)

In this section the c_n are positive derivative normalizations, not the
fixed Mellin scale c_base=pi/15 in (5).
To avoid any numeric ambiguity, the checker calls them derivative_scale.

Define an INTEGER triangular array

    u_(0,0)=1,
    u_(n+1,j)=u_(n,j)^2-2u_(n,j-1)^2,                     (20)

where entries outside 0<=j<=n are zero. The first rows are

    [1]
    [1,-2]
    [1,2,-8]
    [1,2,56,-128]
    [1,2,3128,10112,-32768].                              (21)

The complete derivative measure of Z_n has the representation

 D^(d_n) Law(Z_n)=c_n [sum_(j=0)^n r_(n,j)delta_(x_j)+h_n dx],
 r_(n,j)=(-1)^(d_n)u_(n,j)x_j^(-d_n),  h_n in BV.          (22)

At depth zero, d_0=0 and h_0=0. Apply (11) with a=a_n,d=d_n, so p_n>1 at
EVERY stage. Then apply (14)--(17) with m=2d_n. Since d_(n+1)=2d_n+1,
this proves the regularity and support claims in (22) by induction.

For clarity, the upper endpoint in (15), after division by c_(n+1), gives
-r_(n,j)^2/x_j. The lower endpoint from x_(j-1) gives
2*4^(2d_n+1)r_(n,j-1)^2/x_(j-1). Reweighting by x_j^(d_(n+1))
leaves precisely minus [u_(n,j)^2-2u_(n,j-1)^2], proving (20).
This calculation retains the shared interior knots 1/4,1/16,...; it is not
an endpoint-only approximation of the complete source.

Define the positive-coefficient polynomial

    P_n(z)=sum_(j=0)^n u_(n,j)^2 z^j.                       (23)

### BHH3: all zeros of P_n lie in |z|<=1/4

For n>=1, u_(n,j)>0 for j<n, the last entry is negative, and

    |u_(n,j)|>=2|u_(n,j-1)|, 1<=j<=n;
    u_(n,0)=1, |u_(n,n)|=2^(2^n-1).                       (24)

These statements follow inductively from (20). For an interior new entry,
u_j^2-2u_(j-1)^2 >=2u_(j-1)^2, while the preceding new entry is at most
u_(j-1)^2. The terminal magnitude is 2u_n^2, at least twice the preceding
new value. The first row starts the induction.

Thus the coefficients of P_n grow by at least a factor four. Here is the
needed Enestrom--Kakeya argument in full. Write P_n(z)=sum A_j z^j and
b_j=A_j/4^j; then b_j are positive nondecreasing. If |w|>1 and
sum b_j w^j=0, multiplication by 1-w would imply

 b_n |w|^(n+1)
 <= b_0+sum_(j=1)^n (b_j-b_(j-1))|w|^j
 <= b_n |w|^n,

a contradiction. Since P_n(w/4)=sum b_j w^j, every root has modulus at most
1/4. This proves the classical root-bound mechanism at its needed scope;
the source-specific input is (20), not an assumed polynomial stability.

Consequently, for 0<=Re s<=1,

    |P_n(2^-s)| >= L_n:=4^(d_n-n)>0,
    |d/ds log P_n(2^-s)| <=2n log2.                       (25)

For n=0 both statements hold with L_0=1 and derivative zero. To see (25),
factor P_n(z)=u_(n,n)^2 product(z-z_j). Here |2^-s|>=1/2 and |z_j|<=1/4,
so each factor is at least 1/4 and each logarithmic term has magnitude at
most 2log2. In particular P_n(2^-s) can have zeros only in Re s>=2.
Those are zeros of the LEADING FACTOR, not an assertion about all actual M_n
zeros at finite height.

## 4. Exact Mellin splitting and complete high-frequency remainder

Let g_n be the BV remainder in the NORMALIZED pair measure (12) applied to
eta_n in (22). Thus

 D^(2d_n) Law(C_n)
 =kappa_n c_n^2 [sum_j r_(n,j)^2 delta_(x_j)+g_n(x)dx].    (26)

Set m=2d_n, p=s/2. Testing this distribution against x^(p+m), with a smooth
cutoff equal to one on the entire positive support, yields

 E C_n^p = [kappa_n c_n^2/(p+1)_m]
                 [P_n(4^-p)+R_n(s)],
 R_n(s)=integral_(4^-n)^1 x^(p+m)g_n(x)dx.               (27)

Here (p+1)_m=(p+1)...(p+m), and an empty product is one. The derivative order
m is EVEN, so no minus sign is lost. This equality holds off the removable
exceptions p=-1,...,-m, and in particular throughout the critical strip.
All off-diagonal and continuous terms remain inside R_n.

Combining with (5) gives the exact factorization

 M_n(s)=G_n(s)[P_n(2^-s)+R_n(s)],
 G_n(s)=(pi/15)^(s/2) Gamma(A_n+s/2) kappa_n c_n^2
                       /[Gamma(A_n)(1+s/2)_(2d_n)].     (28)

The prefactor has no zero or pole on 0<=Re s<=1.

Suppose L(g_n)<=G and V(g_n)<=W. For x=e^v,

 R_n(s)=integral_(-n log4)^0 exp(itv/2)
                        exp((sigma/2+m+1)v)g_n(e^v)dv.

The zero-extended real amplitude has total variation at most

    C=W+(m+3/2)G.

This follows by composing with the monotone exponential map and the BV
product rule; x^(sigma/2+m)<=1 on the support. Multiplication by v/2, needed
for d/ds, gives variation at most n C+G/2, because log2<1.
Integration by parts against the finite distributional derivative therefore
proves the COMPLETE estimates

    |R_n(s)| <= E0/|t|,  |R_n'(s)| <= E1/|t|,
    E0=2C, E1=2nC+G,   0<=sigma<=1, t!=0.              (29)

All support endpoints and BV jumps are paid in these norms. There is no
oscillatory tail, high-frequency sampling, or zero-conditioned contour in
(29). At n=0 the remainder is identically zero.

## 5. A wholly rational recipe for the all-depth thresholds

The bounds in this section intentionally trade sharpness for a transparent
finite recurrence. They need neither the actual density g_n nor its numerical
integration. All variables below except the explicit beta integrals are
rational, and those integrals enter only through (13).

Initialize l_0=v_0=0 and u_0=[1]. At stage n set

 d=2^n-1, m=2d, b=4^-n, p=(3/2)2^n+1,
 x_j=4^-j, r_j=(-1)^d u_j 4^(jd), A=sum |r_j|,
 Q=(A+l_n)^2,
 G=Q-sum r_j^2,
 W=2p sum_(i!=j)|r_i r_j|/|x_i-x_j|
                      +[(2p-1)/(p-1)](2A+l_n)v_n,
 C=W+(m+3/2)G, E0=2C, E1=2nC+G,
 L_n=4^(d-n).                                           (30)

Define

 B_n=2m+1+4(E1+2nE0)/L_n,
 T_n=ceil max{2,2E0/L_n,B_n,320*16^n}.                   (31)

Next put J=4^m Q, VJ=2*4^(m+1)Q/b and update

 l_(n+1)=(2m+3)(4/b)J+(2*4^(m+1)+1)G/b,
 v_(n+1)=(2m+3)[(4/b)VJ+(16/b^2)J]
                 +2*4^(m+1)[(4/b)W+(4/b^2)G]+W/b+G/b^2, (32)

alongside the integer recurrence (20). Section 2 proves inductively that
l_n and v_n majorize L(h_n), V(h_n). Hence (30) majorizes the actual pair
remainder in (27). The construction is finite for every n. No asymptotic
runtime, practical large-n feasibility or small cutoff is claimed.

### Proof that T_n works

For |t|>=T_n, (25),(29) give |R_n|<=|P_n|/2, so M_n is nonzero on the entire
horizontal strip segment 0<=sigma<=1 at this height. Moreover

 |(P_n+R_n)'/(P_n+R_n)-P_n'/P_n|
       <=2(E1+2nE0)/(L_n |t|).                           (33)

The prime symbol in this formula differentiates s, including 2^-s.
For Re z>=A_n, the classical digamma integral gives

 |psi(z)-log z+1/(2z)| <=1/(12 A_n^2).                    (34)

For completeness its remainder is the integral of e^-zt times
(1/2)coth(t/2)-1/t, which lies between 0 and t/12 for positive t. This
proves (34) by absolute integration; no RH or numerical gamma oracle enters.
At z=A_n+s/2 it follows that

 Re psi(z)>=log(|t|/2)-1/|t|-1/(12A_n^2).

Each reciprocal (s/2+j)^-1 has modulus at most 2/|t|. Logarithmically
differentiating the gamma prefactor (28), using (25),(33), and adding the
reflected contribution therefore gives

 D_n(sigma,t):=d/dsigma log |M_n(sigma+it)/M_n(1-sigma-it)|
 >= log(pi |t|/30)-4n log2-1/(12A_n^2)-B_n/|t|.          (35)

All denominators are already known nonzero. By (31), B_n/|t|<=1 and
|t|>=10*2^(4n+5). Since pi>3 and log2>2/3,

    D_n(sigma,t)>5log2-1-1/(12A_n^2)>2.                  (36)

The elementary inequality log2>2/3 follows from the first term of its
positive atanh series. This proves a uniform strict sign at every height
above the EXPLICIT T_n.

At sigma=1/2 the modulus ratio equals one by conjugation. Strict increase
makes it different from one on either side. A zero of the reflected sum
would require the ratio to be -1, of modulus one. Thus H_n has no off-central
zero at these heights.

On the line s=1/2+it choose a continuous argument theta_n(t) of the nonzero
M_n. Its derivative is Re(M_n'/M_n)=D_n(1/2,t)/2>1.
A zero of H_n is Re M_n=0. There M_n is nonzero and the argument crosses an
odd multiple of pi/2 strictly, so the derivative of H_n is nonzero. This
proves simplicity and completes BHH1, including negative heights by reality.
No statement about zeros BELOW T_n was used or proved.

## 6. The entire high-height counting law

Use the locally chosen log Gamma continued along the positive-height line.
The classical fixed-shift Stirling expansion gives, for fixed n,

 arg Gamma(A_n+1/4+it/2)
    =(t/2)log(t/2)-t/2+(A_n-1/4)pi/2+O_n(1/t).

The argument of (1+s/2)_(2d_n) is 2d_n*pi/2+O_n(1/t).
For z=2^(-1/2-it), factor

    P_n(z)=u_(n,n)^2 z^n product_j(1-z_j/z).

All |z_j/z|<=sqrt(2)/4<1. Each final factor has a globally continuous bounded
logarithm on this parametrized circle. Thus an unwrapped argument satisfies

    arg P_n(2^(-1/2-it))=-nt log2+O_n(1).

Equation (29), the nonzero lower bound (25) and the principal logarithm near
one add only O_n(1/t) for R_n. Therefore

    theta_n(t)=(t/2)log[pi t/(30 e 4^n)]+O_n(1).           (37)

By (36) it is strictly increasing above T_n. The real zeros of H_n occur
exactly at theta_n=(j+1/2)pi, and each is simple. Counting these crossings
proves (9); all lower zeros contribute a fixed n-dependent integer. This
also proves there are infinitely many critical-line zeros of each finite
iterate, without confusing them with zeros of xi.

## 7. Why this is a component theorem, not the requested RH conclusion

PR #857 supplies entire E_n with E_n -> xi locally uniformly on C. It uses
the contraction and the classical BPY source identity, not the present
high-height theorem. The new theorem controls the OPPOSITE end of the zero
problem from an expanding compact exhaustion: its good region is |Im s|>=T_n.
The open windows |Im s|<T_n become larger, not smaller, with the displayed
norm bounds. Hence no interchange of n->infinity and t->infinity is allowed.

A sufficient remaining assertion is zero confinement in the bounded windows
0<Re s<1, |Im s|<T_n for an unbounded sequence of n, or any separate cofinal
expanding-window theorem from the parent. Neither has been established here.
A fixed low numerical panel, a controlled polynomial P_n, and the finite
number of possible exceptions cannot rule out those exceptions.

The old negative D_1(23) remains unchanged: (36) starts only at 279109.
Our theorem does not falsely revive the rejected all-height monotone-phase
induction. It proves where the same mechanism DOES eventually work, using
new complete derivative-measure information.

Non-directed first-/second-depth root scouting motivated the endpoint analysis.
No such root value is accepted in this packet, and no new actual-xi evaluation
or zero census was performed. The bounded checker verifies recurrences and
finite distributional identities; it is not a machine proof of BV regularity,
gamma asymptotics, or BHH1 at infinitely many depths.

## 8. Attribution and review boundary

Gamma--beta algebra, distributional integration by parts, BV Fourier decay,
Enestrom--Kakeya, Stirling/digamma asymptotics and Hurwitz are classical. The
proofs above reconstruct the mechanisms except the standard gamma expansion
used only in the counting law. DLMF 5.9, 5.11 and 5.12 are primary definitions
and reference inputs. BPY's 1999/2001 source identity is needed for the eventual
conditional RH consumer, not for the high-height finite-depth theorem itself.

The source-specific contribution proposed here is the exact signed atomic
recursion (20), its preservation with a COMPLETE BV remainder, and the
resulting explicit all-depth high-height confinement and count. No exhaustive
literature-priority or independent-acceptance claim is made.

Review Sections 2--5 first: scaling powers, diagonal versus mixed beta atoms,
BV norms under scaling, shared-U endpoint factors, the normalized moment
identity (27), s versus p derivatives, the threshold constants, and the order
of quantifiers. Review must not replace the missing bounded-window theorem.
