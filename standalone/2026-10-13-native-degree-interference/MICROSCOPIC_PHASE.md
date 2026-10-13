# Microscopic prime-phase rigidity: a uniform imaginary-part detector

Status: PROPOSED component proof; independent mathematical review required.
The original native moment, a new zero-free boundary, and RH are not proved.
The all-scale lower theorem below concerns a changed prime phase, not the
Möbius endpoint. Its matching upper statement is a stability/transfer theorem,
not an unconditional upper bound for that endpoint.

Scope: K=Q(sqrt(-3)), fixed excluded prime ideals S containing those above 2
and 3, one fixed nonzero nonnegative W in C_c^infinity((0,infinity)), fixed
moment order k and fixed h>0. The lower theorem uses the TRIVIAL fixed Hecke
twist. The elementary stability theorem permits every fixed unitary twist and
all literal row zeros and further column exclusions.

Sources: the classical fixed-field zero-free strip, polynomial bounds for its
Euler logarithm, the prime ideal theorem, Cauchy's estimate, and the Hankel
formula for reciprocal Gamma. The necessary smoothed parameter-uniform
Selberg--Delange calculation is reconstructed in Section 2. See SOURCES.md
for primary references and the distinction from earlier scalar-deformation
obstructions in PRs #933/#935. No October 2026 quasi-RH or large-sieve input.

## 1. The question left by the finite degree experiment

Put omega_K(n)=#{prime ideals dividing n}. For a real theta define

 A_theta(D,u) = sum_{(n,S)=1} mu_K(n) exp(i theta omega_K(n))
                         chi_n(u) W(Nn/D).                    (1.1)

Only squarefree n contribute; chi_n is extended by ZERO at nonunits.
A_0 is the literal native sum. In the unsigned degree polynomial used by
DEGREE_GEOMETRY.md, this is the evaluation z=-exp(i theta), not z=exp(i theta).

A finite window can have a lower moment away from z=-1. It is tempting to
average over nearby phases and hope to exploit a smoother coefficient family.
The following theorem prices how close those phases have to be. Crucially its
error is proportional to theta, rather than a fixed additive logarithmic error.
It is therefore valid for phases that shrink as a negative power of D, or faster.

Let L=log D, ell=log L, and

 Z_S(s)=product_{p not in S}(1-(Np)^(-s))^(-1),
 kappa_S=Res_{s=1} Z_S(s)>0,
 c_W=(integral_0^infinity W(t)dt)/kappa_S>0.

### Theorem 1.1 (uniform microscopic imaginary term)

There are constants c_*>0, C and D_0, depending only on K,S,W, such that
for D>=D_0 and 0<|theta|<=c_*/log log D,

 Im A_theta(D,1)
   = c_W theta D/(log D)^2
       + O( |theta| D/(log D)^2
                       [1/log D+|theta| log log D] ).         (1.2)

The implicit constant is C and is independent of how theta approaches zero.
In particular c_* can be chosen so that

 |Im A_theta(D,1)| >= (c_W/2)|theta|D/(log D)^2.               (1.3)

More generally (1.2) gives a relative asymptotic whenever
|theta| log log D -> 0. No small bound for the real native value A_0 is used
in taking this imaginary part.

## 2. Smoothed Selberg--Delange calculation with its analytic remainder

Introduce a COMPLEX parameter w in |w-1|<=1/4, and write

 S_D(w)=sum_{(n,S)=1} mu_K(n) w^{omega_K(n)} W(Nn/D).

At each D this is a finite polynomial with real coefficients. For Re s>1,

 F(s,w)=sum_n mu_K(n)w^{omega_K(n)}(Nn)^(-s)
       =Z_S(s)^(-w) E(s,w),
 E(s,w)=product_{p not in S} (1-w q^(-s))/(1-q^(-s))^w,
 q=Np.                                                       (2.1)

The local logarithm in E has no linear term and is O(q^(-2 Re s)), uniformly
in w on the displayed disk. All allowed prime norms are at least seven.
Thus E and its logarithm are holomorphic on Re s>1/2 near the contours below,
with uniform bounds on Re s>=3/4; E(s,1)=1. This is an absolutely convergent
Euler correction, not an assertion that the original series converges there.

The classical fixed-field analytic input used for Z_S is the following:
a fixed c>0 can be chosen so that Z_S has no zeros in
Re s>=1-c/log(3+|Im s|), apart from its pole at one. On a slightly narrower
slit strip its Euler logarithm, continued from Re s>1, has at most logarithmic
size away from the pole. In particular Z_S(s)^(-w), for w in the fixed disk,
has a fixed polynomial bound in 3+|Im s| and in |s-1|^(-1).
These are standard fixed-field consequences of zeta/Dirichlet L theory:
zeta_K(s)=zeta(s)L(s,chi_{-3}); any fixed real exceptional zero can be excluded
by reducing c, using nonvanishing at one. No varying field or modulus is used.
These classical inputs are not inferred from the numerical census.

Write near s=1, with v=s-1,

 Z_S(1+v)=kappa_S v^(-1) Z_0(v),   Z_0(0)=1,
 H(v,w)=W_hat(1+v) kappa_S^(-w) Z_0(v)^(-w) E(1+v,w).

Here H is jointly holomorphic in a fixed product neighborhood and real on
real v,w. Define H_j(w)=[v^j]H(v,w). In particular

 H_0(1)=c_W.                                                 (2.2)

We claim the following precise finite expansion, uniformly on |w-1|<=1/4:

 S_D(w)=D sum_{j=0}^2 H_j(w)
                   L^(-w-j-1)/Gamma(-w-j) + R_D(w),
 |R_D(w)| <= C_W D L^(-19/4).                               (2.3)

The remainder is holomorphic in w on the interior of that disk and respects
complex conjugation. Its derivative on |w-1|<=1/8 satisfies

 |R_D'(w)| <= C_W D L^(-19/4).                               (2.4)

Here is the contour proof, supplied to fix the smoothing and uniformity.
Mellin inversion on Re s=1+1/L is justified by absolute convergence and
W_hat(s)'s arbitrary polynomial vertical decay. Truncate at T=exp(a sqrt L),
where the fixed a>0 is sufficiently small. Shift to Re s=1-rho with
rho=c'/log(3+T), circling the slit from 1-rho to 1. The left line and both
horizontal segments cost O(D exp(-c'' sqrt L)): choose a so that the factor
D^(-rho) defeats the fixed polynomial growth in T, and use sufficiently
many integrations by parts in W_hat for the horizontal pieces and original
vertical tails. These choices are uniform in w on the fixed disk. Logarithmic
factors near s=1 are absorbed in the same exponentially small bound.

On the two lips of the slit the integrand is
D exp(Lv) v^w H(v,w). Replace H by H_0+H_1 v+H_2 v^2. The remainder is bounded
by C|v|^3 uniformly, giving

 C D integral_0^rho exp(-Lx) x^(Re w+3) dx
       <= C D L^(-Re w-4) <= C D L^(-19/4).

The small circular endpoint contribution tends to zero because Re w>=3/4.
Each retained term can be extended to the full Hankel contour at an
exponentially small cost. The identity

 (1/(2pi i)) integral_Hankel exp(Lv)v^(w+j)dv
       = L^(-w-j-1)/Gamma(-w-j)

follows by subtracting the two lips and using the Gamma reflection formula;
it is also valid when -w-j is a nonpositive integer, where its value is zero.
This proves (2.3). Since both the original polynomial and the retained terms
are holomorphic in w, R_D is holomorphic. Cauchy's estimate on an intermediate
disk proves (2.4). This is a bound for the ANALYTIC remainder, not a formal
differentiation of an unspecified O-term.

### Proof of Theorem 1.1

Put w=exp(i theta). The reciprocal-Gamma recurrence gives the exact identity

 1/Gamma(-w)=w(w-1)/Gamma(2-w).

Therefore g(w):=H_0(w)/Gamma(-w) has g(1)=0 and g'(1)=c_W. Consequently,
for |theta| log L bounded by a sufficiently small fixed constant,

 Im [ L^(-w-1)g(w) ]
   = L^(-2) [ c_W theta+O(theta^2(1+log L)) ].               (2.5)

This follows from w-1=i theta+O(theta^2), the bounded second derivative of
g near one, and exp(-(w-1)log L)=1+O(|w-1|log L). For j=1,2, the same
recurrence gives

 1/Gamma(-w-j)=(-1)^j (w-1)w(w+1)...(w+j)/Gamma(2-w).

Thus those two terms vanish at w=1 and have total absolute size
O(|theta| D/L^3), including their bounded L^(-w+1) factors.
Finally R_D(conjugate w)=conjugate(R_D(w)); the vertical segment from w to
conjugate w is inside |w-1|<=1/8. Equation (2.4) gives

 |Im R_D(w)| <= |Im w| sup |R_D'| <= C |theta| D L^(-19/4).

Apply this to (2.3) and use A_theta(D,1)=S_D(exp(i theta)). This proves
(1.2). Choosing c_* and then D_0 so that the relative error is at most 1/2
proves (1.3). QED.

This also recovers the classical tangent asymptotic
sum mu_K(n)omega_K(n)W(Nn/D)=c_W D/(log D)^2+O(D/(log D)^3).
Its asymptotic nature does not require that the finite sums have this sign
at the small scales in the census.

## 3. Genuine sixth-power copies: a lower moment at the actual height

### Theorem 3.1

For every fixed k>=1 and h>0, and uniformly throughout the theta range of
Theorem 1.1, for all sufficiently large D,

 M_{2k,theta}(D,D^h)
 :=sum_{0<Nu<=D^h}|A_theta(D,u)|^(2k)
 >= c_{k,h,S,W} |theta|^(2k) D^(2k+h/6)/(log D)^(4k+1).
                                                                  (3.1)

All physical rows are retained on the left. A positive subfamily supplies
the lower bound; this is not a lower bound for an individually signed tuple
sector. The theorem is for the phase-modified coefficients in (1.1).

Proof. Set Y=D^(h/6). For each prime ideal r outside S with Y/2<Nr<=Y,
choose a generator r and use the literal element row u=r^6. Distinct prime
ideals give distinct rows and Nu<=D^h. The character value is exactly
chi_n(r^6)=1_{(n,r)=1}. Using |sin(theta j)|<=|theta|j and
omega(n)<=C log D on the fixed column support gives

 |Im A_theta(D,r^6)-Im A_theta(D,1)|
   <= C |theta| log D (D/Nr+1).                              (3.2)

The difference is identically zero when Nr>bD, where b is the column support
cap. Thus (3.2), divided by |theta|D/(log D)^2, tends to zero uniformly in
all copying primes and ALL nonzero theta in the stated range. For h>0 fixed,
(log D)^3(D^(-h/6)+D^(-1)) -> 0. Theorem 1.1 therefore supplies a lower
bound c|theta|D/(log D)^2 on every one of these rows.

The classical prime ideal theorem in this one fixed field supplies at least
c_h D^(h/6)/log D copying ideals. Sum their positive 2k-th powers to obtain
(3.1). This argument does not claim a prime theorem for a moving ray class,
forget a nonunit zero, or change the physical row box. QED.

### Corollary 3.2 (a polynomial angular resolution barrier)

Let theta=D^(-a), a>0 fixed. A diagonal upper bound
M_{2k,theta}<<D^(h+k+epsilon) for every epsilon>0 is impossible when

 a < a_crit(k,h) := 1/2 - 5h/(12k).                          (3.3)

Indeed the lower power excess over HD^k in (3.1) is

 e_lower= k-2ka-5h/6 = 2k(a_crit-a)>0.                       (3.4)

The logarithmic denominator cannot pay a positive power. In particular,
for k=2, h=21/20, one has a_crit=9/32. At theta=D^(-1/4),

 M_{4,theta}(D,D^(21/20))
       >= c H D^(2+1/8)/(log D)^9.                          (3.5)

These are bounds for CHANGED coefficients. Theta=0 is expressly excluded.
Neither (3.3) nor (3.5) refutes the native fourth moment.

## 4. Elementary positive result: exactly priced phase stability

Let w_H(u)>=0 be any finite row measure of total mass Z. Let nu be any unitary
multiplicative column twist; let additional column exclusions be arbitrary.
Let pi_D be any probability distribution on real phases with finite p-th
absolute moment, p>=1. Use A_theta with these phases and data. Then

 | ||A_theta||_{L^p(w_H times pi_D)}-||A_0||_{L^p(w_H)} |
 <= C_W Z^(1/p) D log log(3D)
                    (integral |theta|^p d pi_D)^(1/p).     (4.1)

Proof. Pointwise |exp(i theta omega(n))-1|<=|theta|omega(n). Hence
|A_theta-A_0|<=C_W |theta| sum_{Nn<=bD} omega(n).
Opening omega, ideal counting, and Chebyshev's prime-ideal estimate give

 sum_{Nn<=bD} omega(n)
 <= C D sum_{Np<=bD}(Np)^(-1)
 <= C D log log(3D).

Dropping squarefreeness only enlarges this bound; all masks and phases have
modulus at most one. Integrate the pointwise difference in the product measure
and use the two directions of the triangle inequality. The constant is
independent of p, H, the row support, and the additional exclusions. QED.

If pi_D is supported in |theta|<=D^(-1/2)(log D)^B for fixed B, then for
each fixed k the averaged 2k-th moment has diagonal size with an arbitrary
D^epsilon allowance IF AND ONLY IF the native 2k-th moment does. This holds
at the same physical height; when used at shorter column scales, replace D
by that actual column scale. The comparison creates no new analytic input.

Conversely, suppose pi_D is uniform on [-delta_D,delta_D], with
0<delta_D<=c_*/log log D. Integrating (3.1) gives

 integral M_{2k,theta}(D,D^h) d pi_D(theta)
 >= c delta_D^(2k) D^(2k+h/6)/(log D)^(4k+1).                (4.2)

For delta_D=D^(-a), every fixed a<1/2 therefore fails for a cofinal family
with h_k=o(k) (even allowing excesses e_k=o(k)): choose a sufficiently
large fixed k so 2k(1/2-a)-5h_k/6-e_k>0, then let D grow.
At a>=1/2, (4.1) instead transfers, but does not prove, the native hierarchy.
Thus the exponent 1/2 is a sharp boundary at this COFINAL phase-averaging
scope. No sharp fixed-k sufficiency at a_crit(k,h), no sharp logarithmic
endpoint, and no unproved growing-order uniformity are claimed.

## 5. What the attempted continuation achieved

The exact degree census shows large cancellations between prime degrees and
rules out a finite global/local minimum principle at the Möbius phase.
Theorem 3.1 shows why averaging over even polynomially shrinking phases can
still reintroduce the coherent obstruction; fixed noninteger deformation
arguments alone did not price this microscopic range. Equation (4.1) supplies
a positive, mask-preserving comparison at the square-root resolution scale.

This does NOT bound the native large-singleton covariance. At the resolution
where the phase average is controllably equivalent, it is still as hard as
the original moment. A proof must use the exact signed endpoint, or estimate
a nearby average at that actual scale without treating the changed prime
coefficients as an arbitrary unitary class.
