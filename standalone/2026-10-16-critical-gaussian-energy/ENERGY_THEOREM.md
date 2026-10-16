# Critical Gaussian energy: an exact signed pair kernel and a logarithmic diagonal

Status: PROPOSED component mathematics. No full arithmetic energy estimate,
new zero-free region, generalized native moment, or RH proof. Same-author
reconstruction; no independent referee or Lean build.

The preceding packet's OPEN-G2 is a scale mean-square hypothesis, whereas its
proved comparisons are pointwise scale envelopes. This note treats the energy
itself, obtains its exact pair kernel, controls its literal ideal diagonal,
and quantifies a finite truncation. These are not a proof of its off-diagonal
estimate. The elementary methods are Gaussian integration, Dirichlet
convolution, ideal counting, and Minkowski; no global novelty is claimed.

## 1. Objects, masks, and the two positive coefficient counts

Fix a number field F. Choose A_F>=1 such that the number I_F(T) of nonzero
integral ideals of norm at most T is at most A_F T, for T>=1. All constants
below retain this fixed-field dependence; uniformity in discriminants is NOT
asserted. Use the original excluded primes S, containing all primes above
2 and 3. Let m>=2 be an integer and |a_p(u)|,|b_p(u)|<=1 for every row u.
At an originally masked prime set BOTH phases to zero. Fix a nonnegative row
measure w of finite mass Z_w. It is the SAME measure at every scale.

Write q=Np and define p_m(n;u) by the formal local factors

    P_p(x)=1-(1-1/q)a_p(u)x-b_p(u)q^(m/2-1)x^m.

Thus only the exponents 0,1,m occur. Every nonzero coefficient has the UNIQUE
form n=r d^m with r,d squarefree and (r,d)=1. For that representation,

    |p_m(n;u)| <= (Nd)^(m/2-1).

Let q_m be the two-channel coefficients with local factor
(1-a_p x)(1-b_p q^(m/2-1)x^m). Its analogous representation permits (r,d)>1;
a shared prime creates exponent m+1 and is NOT deleted. The representation
is still unique. This also works at m=2. Equal-norm ideals remain distinct.

### Lemma E1 (uniform first and second coefficient masses)

For every T>=1, every m>=2 and every permitted row,

    sum_(Nn<=T) |p_m(n;u)| <= C_F T,
    sum_(Nn<=T) |p_m(n;u)|^2 <= C_F T,                 (E1)
    C_F=A_F zeta_F(2).

The same bounds hold for q_m and for the ordinary Mobius coefficients
mu_F(n)a(n;u), after increasing C_F if necessary (the displayed C_F suffices).

Proof. Drop coprimality, squarefreeness and masks from the positive count.
For power j=1 or 2, sum first over d and then over r:

    sum |p_m(n)|^j <= A_F T sum_d (Nd)^[j(m/2-1)-m].

For j=1 the exponent is -m/2-1<=-2; for j=2 it is exactly -2. This proves E1.
For q_m the same representation without coprimality proves it. For native
Mobius use |mu_F a|<=1 and I_F(T)<=A_F T. QED.

These counts preserve an upper bound uniformly over masks; they do not replace
any zero or phase in an identity. No comparison to independent physical rows
occurs. All statements about m are algebraic, NOT new metaplectic realizations.

Fix c in R and the SAME Gaussian as the source (c=5/6 in that application):

    W_c(y)=(2 sqrt(pi))^(-1)y^(-c) exp[-(log y)^2/4],
    B_m(X,u)=sum_n p_m(n;u)W_c(Nn/X).

Let C_m and A be the analogous q_m and native Mobius sums. All are absolutely
convergent and flat at X=0, uniformly in m and row, as proved in the recovered
GAUSSIAN_ADAPTER.md. In particular their energies below are finite.

Define the cumulative CRITICAL energy, with no scale supremum:

    E_F(D;w)^2 = integral_0^D ||F(X)||_(L2(w))^2 dX/X^2.  (E2)

The extra 1/X relative to dX/X is essential. This quantity is not an energy
on a changing row box H=X^h. For each chosen H the row measure must be fixed.

## 2. An exact pair kernel for the full Gaussian energy

Let Phi_N be the standard normal cumulative distribution function,
Phi_N(t)=(2pi)^(-1/2) integral_(-infinity)^t exp(-v^2/2)dv. Put

    beta=2c-1,   K_c=exp(beta^2/2)/(2 sqrt(2pi)),
    K_D(v,z)=K_c/sqrt(vz) * exp[-(log(v/z))^2/8]
             * Phi_N(log D-(log v+log z)/2-beta).       (E3)

Here v,z denote positive norms, not physical rows or spectral variables.

### Theorem E2 (exact signed energy)

For D>0,

    E_B(D;w)^2
      = sum_(n,l) K_D(Nn,Nl)
                    integral p_m(n;u) conjugate(p_m(l;u)) dw(u). (E4)

The pair sum is absolutely convergent for every finite D. It includes ALL
ideal pairs, including distinct ideals of the same norm, shared primes and
principal aliases. Each scalar K_D is positive, but the coefficient pairing
need not be. K_D is a positive-semidefinite Gram kernel; this does not make
its signed off-diagonal subtotal nonnegative.

Proof. For a finite sum expand E2. With x=log X, a=log v, b=log z, and
mu=(a+b)/2, its kernel integrand is

    (4pi)^(-1) exp[(2c-1)x-c(a+b)
                         -((x-a)^2+(x-b)^2)/4].

Complete the square. Its exponent is EXACTLY

    -(x-mu-beta)^2/2 - mu + beta^2/2 -(a-b)^2/8.

Integration from -infinity to log D gives E3, including its normal-CDF shift
and constant. To justify the infinite expansion, E1 and partial summation give

    sum_n |p_m(n;u)| |W_c(Nn/X)|
       <= C_F X integral_0^infinity y|W_c'(y)|dy.        (E5)

The Gaussian is not assumed monotone: the absolute derivative is used. The
integral is finite. The square of the right side, divided by X^2, is integrable
on (0,D), uniformly in the row; multiply by Z_w. Tonelli for the absolute
majorant and then Fubini prove E4. This also proves the unconditional bound
E_B(D;w)^2<=C_(F,c) Z_w D. QED.

This proof does NOT move a Mellin line through unknown poles. The identity is
physical Gaussian integration only.

### Corollary E3 (the literal ideal diagonal is logarithmic)

Let D>=1 and let Delta_B(D;w) be the n=l subtotal of E4. Then

    0<=Delta_B(D;w)<=C_(F,c) Z_w [1+log D],             (E6)

uniformly in m and the phases/masks. Consequently the real off-diagonal O_B
satisfies

    E_B^2=Delta_B+O_B,       O_B>=-Delta_B.              (E7)

Proof. The diagonal kernel is K_c t^(-1)Phi_N(log D-log t-beta). It is a
nonnegative decreasing function h(t) for t>=1. Use the second count E1 and
Stieltjes partial summation:

    sum_n |p_m(n)|^2 h(Nn)
       <= C_F [h(1)+integral_1^infinity h(t)dt].

After t=exp(v), the integral divided by K_c equals
integral_(-infinity)^(log D-beta) Phi_N(s)ds. For any real a this is
 a Phi_N(a)+(2pi)^(-1/2)exp(-a^2/2), at most a_++1/sqrt(2pi).
This proves E6. E7 follows from nonnegativity of the original energy. QED.

IMPORTANT: this is the IDEAL diagonal, not all equal-rational-norm pairs, and
not the principal-character tuple reference from #942. Distinct equal-norm
ideals stay in O_B. They must not be discarded or counted only once.

## 3. Direct two-way critical ENERGY transfer

Use U_m and its inverse from the recovered PROOF.md, with their nonnegative
coefficient majorants of total critical mass <=exp(5[F:Q]).

### Theorem E4

For every D>0,

    E_B(D;w)<=exp(5[F:Q]) E_C(D;w),
    E_C(D;w)<=exp(5[F:Q]) E_B(D;w).                     (E8)

For D>=2 there is C_(F,c), independent of m, phases, masks, D and w, such that

    E_B(D;w)<=C_(F,c)(1+log D/m) E_A(D;w),
    E_A(D;w)<=C_(F,c)(1+log D/m) E_B(D;w).              (E9)

No pointwise hypothesis or supremum over shorter scales appears in E8--E9.
They are finite-horizon energy comparisons on the same actual row measure.

Proof. For a dilation N>=1, substitution Y=X/N gives

    ||F(X/N)||_(L2((0,D),dX/X^2;L2(w)))
                       =N^(-1/2) E_F(D/N;w).           (E10)

Apply Minkowski to the exact Gaussian convolutions B=u_m*C and C=v_m*B.
Rowwise multiplication by a kernel coefficient is bounded by its uniform
majorant. Monotonicity E_F(D/N)<=E_F(D) and its summable mass prove E8.

For A and C the two exact convolutions have dilation (Nd)^m and coefficient
(Nd)^(m/2-1) times, respectively, mu_F(d)b(d;u) or b(d;u). After E10 their
absolute critical weight is 1/Nd in BOTH directions. Split at R=D^(1/m).
For Nd<=R use sum_(Nd<=R)1/Nd<=A_F(1+log R). This gives the claimed logarithm.
For Nd>R all shorter horizons are <1. Uniform Gaussian flatness gives

    E_F(T;w)<=C_(F,c) sqrt(Z_w) T^(3/2),  0<T<=1,

for F=A,C,B; one may use |coeff(n)|<=sqrt(Nn) and the Gaussian majorant at
weight 2 to prove this. Partial summation of I_F(t)<=A_F t implies

    D^(3/2) sum_(Nd>R)(Nd)^(-1-3m/2)<=2A_F.

Hence this tail costs only C_(F,c)sqrt(Z_w), uniformly in m.

This additive error can genuinely be absorbed. Every source has unit
coefficient one, and |coeff(n)|<=sqrt(Nn). For sufficiently small fixed X0>0,
uniformly for X in [X0/2,X0],

    sum_(n!=1)|coeff(n)| W_c(Nn/X) <= W_c(1/X)/2.

Indeed the ratio of a nonunit summand to W_c(1/X) is bounded by
(Nn)^[1/2-c+(log X)/2]; choose X0 so its ideal sum is <=1/2. Such a choice
exists since zeta_F(t)-1 tends to zero as t tends to infinity. Therefore each
energy at D>=1 is >=c_(F,c)sqrt(Z_w), with c_(F,c)>0. Absorb the tail, then
combine with E8. If Z_w=0 all inequalities are identities. QED.

The logarithmic order is a genuine limitation of a source-independent
inverse CHANNEL operator. Over Q excluding 2 and 3, in x=log X coordinates
its critical action on f is

    Vf(x)=sum_((d,6)=1) d^(-1) f(x-m log d).

On x in [0,L], take f=1_[0,L]. Then Vf(x)=x/(3m)+O(1), by elementary harmonic
sum inclusion-exclusion. If L/m tends to infinity, ||Vf||_2/||f||_2>=c L/m.
This is a test of the causal operator on arbitrary functions, NOT a lower
bound for the original Gaussian Mobius source or a refutation of RH.

## 4. A finite pair target with a controlled Gaussian tail

The identity E4 is an infinite pair sum, but it has a near-linear finite
truncation in the scale D, without assuming cancellation.

Let B_{<=T} use only ideals of norm <=T. For V>=0 and T=D exp(V), Gaussian
completion of squares gives

    W_c(e^t)<=C_c e^(-t^2/8)e^(-2t),
    C_c=exp(2(2-c)^2)/(2 sqrt(pi)).

Since all omitted terms have t=log(Nn/X)>V for 0<X<=D, and
sum |p_m(n)|/(Nn)^2<=zeta_F(3/2), using |p_m(n)|<=sqrt(Nn), one obtains the explicit safe bound

    E_(B-B_{<=T})(D;w)
       <= C_c zeta_F(3/2)/sqrt(3)
                         *sqrt(Z_w) D^(3/2) exp(-V^2/8).   (E11)

This bound is uniform in m, masks and phases. To convert it to an error in
SQUARED energies, use |E_B^2-E_{B_{<=T}}^2|<=r(2E_B+r), where r is E11 and
E_B<=C_(F,c)sqrt(Z_w D) by E5. For every fixed B0>0 choose

    V=sqrt(8(B0+3)log(2D)).

Then |E_B^2-E_{B_{<=T}}^2|<=C_(F,c,B0) Z_w D^(-B0), D>=2. In particular
T=D exp(O_(B0)(sqrt(log D)))=D^(1+o(1)). The result controls all omitted
cross terms as well as the omitted diagonal; merely deleting those cross
terms from a positive Gram matrix would not justify a truncation.

All finite norm fibers still require their complete ideal multiplicities.
The row sum, if present, retains all its original masks. For a single fixed
finite criterion one can choose B0=1 throughout, so T(D)=D exp(sqrt(32 log(2D)))
and the squared-energy error is O_(F,c)(Z_w/D).

## 5. What would finish the scalar zero-exclusion argument

For the actual principal m=6 source and w a single row of weight one, the
following assertions are equivalent as ALL-EPSILON assertions:

 (a) E_B(D)^2=O_epsilon(D^epsilon), for every epsilon>0;
 (b) integral_D^(2D)|B(X)|^2 dX/X=O_epsilon(D^(1+epsilon));
 (c) E_A(D)^2=O_epsilon(D^epsilon);
 (d) O_B(D)<=C_epsilon D^epsilon.                       (OPEN-E)

None of these arithmetic assertions has been proved here. For a<=>b use
X between D and 2D and sum the dyadic intervals in the reverse direction,
including Gaussian flatness below one. For a<=>c use E9 and absorb its fixed
logarithmic square into an arbitrarily small exponent. For a<=>d use E6--E7.
E11 permits replacing a by the explicit finite kernel energy at the prescribed
T(D), with negligible error. This is a quantified finite family of unproved
inequalities, not evidence that they hold at unbounded D.

As established in the recovered GAUSSIAN_ADAPTER.md, any of these bounds gives
holomorphy of the actual Mellin transform on Re(s)>1/2 and the identity

    zeta_F^S(s) Mellin[B](s)
       =exp((s-5/6)^2) U_6(s) E_b(6s-2).               (E12)

Here E_b(z)=product_p(1-b_p q^(-z)) is normally convergent and nonzero for
Re z>1. U_6 is nonzero on Re s>3/7. Thus the right side of E12 is nonzero for
Re s>1/2, with NO finite-order-character assumption on b. Analytic uniqueness
would exclude every target zero there. The standard functional equation then
gives critical-line confinement. For the auxiliary field in the imported
construction its stated abelian descent may be applied; no new field descent
or automorphic source theorem is asserted in this note.

A particularly concrete remaining estimate is therefore the one-sided bound
on the OFF-DIAGONAL of the finite K_D matrix in E3, with its literal Mobius
coefficients, sufficient to keep the full energy subpower. E6 pays its entire
ideal diagonal with only a logarithm; E11 pays the far Gaussian tail. The
unpaid term is a signed correlation, including nearby norms and equal-norm
aliases, not a missing absolute-convergence lemma.

## 6. A check on the attempted positive-matrix shortcut

Replacing the arithmetic coefficients by their absolute values is not harmless.
Within the permitted algebraic coefficient class, take F=Q, exclude 2 and 3,
and choose a_p=b_p=-1. Every nonzero p_m(n) is then positive. Its squarefree
part is mu(n)^2 phi(n)/n on (n,6)=1. For each delta>0,
phi(n)/n>=c_delta n^(-delta): separate a finite set of primes and use
1-1/p>=p^(-delta) on all remaining primes. The elementary squarefree count in
any fixed interval [aD,bD] on (n,6)=1 has positive linear density. Choose such
an interval on which W_c is bounded below. Hence

    B_m(D)>=c_delta D^(1-delta),
    E_B(D)^2>=c_delta D^(1-2delta),

for large D. E5 gives the matching upper exponent one. The energy diagonal
still satisfies E6. Therefore a positive Gram kernel, an O(log D) diagonal,
and bounded correction/inverse kernels do NOT imply OPEN-E for arbitrary
phases. This is a counterexample to that universal inference, NOT to the
native source a_p=1 or to RH. Its squarefree count follows from
mu(n)^2=sum_(r^2|n)mu(r), finite exclusion inclusion-exclusion, and an
absolutely convergent positive Euler density; no new prime theorem is used.

## 7. Sources and scope of the advance

- Recovered critical-power PROOF.md and GAUSSIAN_ADAPTER.md, frozen source
  packet at recovery commit bf55bad693d147747bdb8074fc555d408b60782e: definitions,
  bounded U/inverse kernels, full Gaussian interchanges and OPEN-G2. Both read
  in full and their finite checker replayed; this is not independent review.
- #949 cdb0666fc48d5166f5edd81f394b13e2001a6b5d: original normalization and
  source Mellin identity. Its theta foundation is not reproved or Lean-built.
- #951 aba76e1df38dc438b9f5c5f20b698fb26fb1716e: COUPLED_PRIME_FLOW.md read in
  full; CRITICAL_FACTOR_AND_GAUSSIAN.md read through the main Gaussian bound.
  Its one-log coefficient and pointwise-envelope costs and full two-channel
  compensation are credited. This note's addition is the actual cumulative
  L2 energy interface, explicit covariance kernel, its uniform logarithmic
  diagonal, and a finite Gaussian truncation with a squared-energy guarantee.
- #950 5a6418b021a35c95bbc2c80775353ee33506faee: overlap as described in #951
  and its PR metadata, not an imported analytic premise. No independent
  reconstruction of its geometric-source proof is claimed here.
- #942/#947: previously read principal-tuple and principal-row distinctions.
  The diagonal of E4 is explicitly a THIRD object: equality of coefficient
  IDEALS in a scalar/log-scale energy, not either of those physical-row cuts.

The reported external 31/32 theorem has not been independently rebuilt here.
The current Hexagon v1 landing record was checked on 2026-10-16 and still lists
v2 as current. No new PDF analysis, theorem-version reconciliation, or claim
of external acceptance is made in this energy note.
