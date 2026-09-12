# HBR28 — hyperbolic renormalization, its full analytic spectrum, and an arithmetic-shift bridge

Date: 2026-09-12. Status: **PROPOSED component proofs awaiting independent mathematical review. RH is not proved.**

This continues the objects of BRN26/#846 and BRN27/#856 but does not reuse their numerical certificates as premises. In particular the failed BRN26 phase condition is not revived. The goal of this attack was to replace a guessed individual companion by control of the entire renormalization operator and a solvable positive comparison. The operator can indeed be solved at the level of its analytic spectrum. The comparison can indeed be evaluated as finite combinations of shifted xi functions. Neither operation proves the needed complex-zero sign; precise failures and the remaining issue are stated below.

The statements concern analytic functions of the **Laplace variable** t unless an explicit Mellin transformation is made. They do not identify the spectrum of a positive operator with the zero locations of xi. All series tails needed for the analytic-spectrum statement are retained. A Schauder eigenbasis on a fixed Banach space is NOT asserted.

## 1. Source and independent preliminary bounds

Let independent mean-one exponentials E_j define

    X=(6/pi^2) sum_(j>=1) E_j/j^2,
    L(t)=E exp(-tX)=sqrt(6t)/sinh(sqrt(6t)), L(0)=1.

The series is positive, converges almost surely and in L1, and E X=1. The Laplace identity follows from the classical sinh product. Square roots in this identity cancel; L is a meromorphic function of t. The classical Brownian/xi identity credited to Biane–Pitman–Yor, in this normalization, is

    xi(2q)=(1/2)(pi/6)^q E(X+X')^q.                 (1)

Here xi is the ENTIRE completion, including xi(0)=xi(1)=1/2, and X' is independent. Both sides of (1) are entire in q. This identity is classical, not new here. Its exact normalization can also be derived directly: for Re q<0, the negative-moment Laplace integral and csch(r)^2=4 sum_(n>=1)n exp(-2nr) give

    E(X+X')^q=2*24^q Gamma(2-2q)zeta(1-2q)/Gamma(-q).

Indeed substitute r=sqrt(6t) into the integral for L(t)^2. The exponential series is absolutely integrable in this range. Multiplication by (1/2)(pi/6)^q, gamma duplication, and xi(s)=xi(1-s) give (1). All positive and negative moments exist (the positive exponential-moment and inverse-moment arguments are given below), so the identity extends to every q. The classical sinh product, gamma identities and xi functional equation are the imported special-function inputs. No zero geometry is imported.

For complex z put

    a_z = integral_1^2 u^(-2z)du
        = (1-2^(1-2z))/(2z-1),
    a_(1/2)=log 2.                                  (2)

Thus a_z is ENTIRE, a_m>0 for nonnegative integers m, and a_m strictly decreases. The source fixed-point identity is

    L(t)=integral_1^2 L(t/u^2)^2 du.                 (3)

For positive t set r=sqrt(6t), substitute v=r/u, and integrate csch(v)^2 to obtain r[coth(r/2)-coth r]=r/sinh r. Analytic continuation gives (3) on its common domain.

For integer m>=1, let V_m have density u^(-2m)/a_m on [1,2]. With all factors independent set

    W_m=sum_(j>=1) (product_(i<=j) V_(m,i)^(-2)) X_j,
    C_m=W_m+X_0,  P_m(t)=E exp(-tW_m),
    D_m(t)=t^m P_m(t).

Write b_(m,n)=a_(m+n)/a_m. The affine recursion is W_m = V_m^(-2)(W_m'+X'), so E W_m=b_(m,1)/(1-b_(m,1))<infinity. Positive-series monotone convergence proves existence. For x_n=E X^n/n!, Jensen applied to the convex combination X=sum_j [6/(pi^2 j^2)] E_j gives x_n<=1. The moment recursion is

    p_0=1,
    p_n=[b_(m,n)/(1-b_(m,n))] sum_(j=0)^(n-1) p_j x_(n-j),
    p_n=E W_m^n/n!.                                 (4)

To justify its use without presupposing moments, apply the recursion and induction first to finite perpetuity sums, then pass by monotone convergence. Since 2m a_m>=1 and n>=1,

    b_(m,n)<=1/[a_m(2m+2n-1)]<=2m/(n+2m).

The first inequality can be strict; the coarse weak inequalities suffice. Induction in (4), using the hockey-stick binomial identity, gives

    p_n <= binomial(n+2m-1,2m-1),
    E exp(vW_m)<=(1-v)^(-2m), 0<=v<1.               (5)

Thus P_m belongs to every analytic Wiener algebra of radius R<1. Also W_m>=X_1/4 and C_m>=X_0. The exponential decay of L(t) in sqrt(t), via the negative-moment Laplace integral, gives every negative moment of X, W_m and C_m. Their Mellin transforms are entire, by domination on compact exponent sets.

The smoothing linearization is

    (T f)(t)=2 integral_1^2 L(t/u^2) f(t/u^2)du.       (6)

The affine equation for P_m gives, for all t>=0 and then analytically,

    T D_m = 2a_m D_m.                               (7)

These are perturbation eigenvalues, not zeta-zero parameters.

## 2. HBR28-1: exact hyperbolic normal form and inverse

For positive t put

    r=sqrt(6t), x=tanh(r/2),
    h(x)=tanh((atanh x)/2)=x/(1+sqrt(1-x^2)).

If f(r^2/6)=r g(x), direct substitutions v=r/u and y=tanh(v/2) in (6) give

    (T f)(r^2/6)=r (A g)(x),
    (A g)(x)=2 integral_(h(x))^x g(y)dy/y.           (8)

This is exact on 0<x<1 for continuous g on the integration interval. It also holds as an analytic-germ identity. Mass-preserving analytic perturbations f(0)=0 correspond to odd analytic germs g at zero, because r=2atanh x and f(r^2/6)/r is odd and vanishes at zero.

Let N=x d/dx and C_h g=g composed with h. On these odd germs define

    N^(-1)g(x)=integral_0^x g(y)dy/y.

Then

    A=2(I-C_h)N^(-1).                              (9)

Furthermore h^j(x)=tanh(2^(-j)atanh x). The geometric shrinking at zero proves local convergence of sum_(j>=0) g(h^j(x)), uniformly on a sufficiently small complex disk and on every compact subinterval of (0,1). Consequently the inverse on analytic germs is

    A^(-1)g = (1/2)N sum_(j>=0) g composed with h^j. (10)

Derivatives converge on a smaller complex disk, by Cauchy estimates. Formula (10) is not asserted bounded on an unspecified global space.

An equivalent inverse, with a particularly simple norm contract, exists in the original coordinate. Write D=t d/dt and Sg(t)=2g(t/4). On the radius-R analytic Wiener algebra with g(0)=0, ||S||<=1/2. Coefficient integration in (6) gives

    T=2 diag(a_n) M_L,
    T^(-1)g = [1/(2L(t))](2D-1) sum_(j>=0)2^j g(t/4^j).     (11)

The order of multiplication and differentiation in (11) matters. The inverse is unbounded: its domain consists of g for which the displayed differentiated series belongs to the algebra. In particular g with sum n|g_n|R^n<infinity belongs to that domain. The geometric sum has a norm remainder <=2^(-J)||g|| after terms j=0,...,J. This remainder is for the undifferentiated sum; no derivative estimate is inferred without the stated stronger domain.

## 3. HBR28-2: full analytic spectrum, simplicity and a complete resolvent tail

Fix 0<R<1. Let A_R be the complex Banach space

    f(t)=sum_(n>=1) f_n t^n,
    ||f||_R=sum_(n>=1)|f_n|R^n<infinity.

It is a closed codimension-one subspace of the unital analytic Wiener algebra. Since ||L||_R=E exp(RX)<=1/(1-R), (6) defines a bounded operator on A_R. In coefficients,

    (Tf)_n=2a_n sum_(j=1)^n l_(n-j)f_j,             (12)

where L(t)=sum l_n t^n. Diagonal multiplication by a_n tends to zero in operator norm after finite output truncation. Therefore T is COMPACT.

**The full spectrum is exactly**

    spectrum_(A_R)(T) = {0} union {2a_m:m>=1}.       (13)

Every nonzero eigenvalue is algebraically simple, with eigenvector D_m. Zero is not an eigenvalue; T has dense, nonclosed range. The same proof gives the cut m>=k on the invariant subspace f_1=...=f_(k-1)=0.

Here is a constructive proof including the whole infinite complement. Let P_N select degrees 1,...,N, and Q_N=I-P_N. Lower triangularity implies P_N T Q_N=0 and

    T = [ T_N   0 ; B_N   C_N ],
    ||C_N|| <= ||Q_N T|| <= q_N(R):=2a_(N+1)/(1-R). (14)

For any complex lambda!=0 choose N large enough that q_N(R)<|lambda|. The tail inverse exists by a norm-convergent Neumann series. If lambda is not any diagonal value 2a_1,...,2a_N, then

    g_head=(lambda I-T_N)^(-1) f_head,
    g_tail=(lambda I-C_N)^(-1)(f_tail+B_N g_head),   (15)

and ||(lambda I-C_N)^(-1)|| <=1/(|lambda|-q_N(R)). Truncating its series after powers 0,...,J leaves operator-norm error at most

    q_N(R)^(J+1)/[|lambda|^(J+1)(|lambda|-q_N(R))]. (16)

This proves that no additional nonzero spectrum is missed. Equation (7) supplies every claimed eigenvalue. For algebraic multiplicity, choose N>=m and q_N(R)<2a_m. The tail block is invertible at 2a_m; the finite triangular block has distinct diagonal values and hence algebraic multiplicity one. Solving the block equations, or using the corresponding block resolvent contour, preserves this multiplicity. This argument controls generalized eigenvectors too.

Finally M_L is invertible on the unital algebra: 1/L=sinh(sqrt(6t))/sqrt(6t) is entire and has finite absolute coefficient norm at R. Diagonal multiplication by a_n is injective and has dense range containing the finite polynomials. Thus T is injective with dense range. A compact injective operator on this infinite-dimensional Banach space cannot be onto with a bounded inverse, so the range is not closed and 0 is in the spectrum.

**Scope distinction.** This improves finite-jet diagonalization to a genuine infinite-dimensional spectral theorem on a NAMED space, with a resolvent error bound. It does not prove convergence of an unrestricted eigenfunction expansion, a bounded self-adjointizing metric, or any statement about the locations of xi zeros. The eigenvalues in (13) are explicitly 1,7/12,31/80,..., not reciprocal squares of xi zeros.

**Universality of the nonzero list.** The same nonzero spectrum and algebraic simplicity hold if L is replaced by ANY analytic Wiener function ell with ell(0)=1 and finite radius-R norm. Indeed the same triangular formula holds and its tail is bounded by 2a_(N+1)||ell||_R. The finite block has the same distinct diagonal values; lifting each of its eigenvectors through the invertible tail constructs the corresponding full eigenvector. This does not need a positive perpetuity or invertibility of ell. The dense-range claim above still uses the specific invertibility of L and is not included in this generalization. Thus positive perturbation eigenvalues alone cannot distinguish the theta source from other normalized analytic sources. The source-specific content must enter through the hyperbolic and Mellin identities, not through this universal eigenvalue list.

## 4. HBR28-3: the whole bounded-dilation Mellin factor

Independence in W_m=V_m^(-2)C_m' gives, for EVERY complex q,

    E W_m^(q-m) = [a_q/a_m] E C_m^(q-m).             (17)

All moments on both sides exist; real logarithms define positive-variable powers. The equality first follows absolutely from independence and then is an entire identity. Thus the left side has the forced zeros

    q=1/2 + i*pi*k/log 2,  k in Z\{0}.              (18)

They are zeros of a Mellin transform of W_m, NOT asserted zeros of xi. It is safest to use the division-free identity (17): the quotient by a_q has removable singularities because it equals the entire right-hand source.

For

    G_m(2q)=(1/2)(pi/6)^q (-1)^m q(q-1)...(q-m+1) E C_m^(q-m), (19)

one also has, initially Re q<m,

    G_m(2q) = (pi/6)^q/[2 Gamma(-q)]
                     integral_0^infinity t^(m-q-1)L(t)P_m(t)dt.       (20)

This is obtained from the standard negative-moment Laplace formula and
(-1)^m q(q-1)...(q-m+1)=Gamma(m-q)/Gamma(-q). It extends through the removable integer values by (19). The m-dependence cannot be discarded from the integration weight in (20).

At m=0, W_0=X and C_0=X+X' give the classical dyadic completion E X^q=a_q E(X+X')^q. Equation (17) is its exact counterpart for every integer perturbation mode. It accounts for the ENTIRE dyadic factor rather than deleting its visible zeros without verifying the division.

## 5. HBR28-4: a solvable Pareto comparison, and the exact cost of the cutoff

For m>=1 replace V_m by a Pareto variable Vtilde_m with density

    (2m-1)u^(-2m), u>=1.

Define Wtilde_m and Ctilde_m=Wtilde_m+X_0 by the same positive perpetuity. The mean contraction is E Vtilde_m^(-2)=(2m-1)/(2m+1), and

    E Wtilde_m=m-1/2.

Positive moments follow by the same finite-series induction. Ctilde_m>=X_0 gives all its inverse moments. Wtilde_m itself does NOT have all inverse moments; none are assumed.

Its Laplace transform is explicitly

    Ptilde_m(t)=[2 tanh(r/2)/r]^(2m-1), r=sqrt(6t). (21)

To prove this independently, the affine equation on [1,infinity) implies

    2t Ptilde_m'(t)=(2m-1)(L(t)-1)Ptilde_m(t), Ptilde_m(0)=1.

Indeed substitute v=t/u^2 and differentiate the integral; the lower endpoint is zero. Integration uses

    integral_0^t [L(v)-1]dv/v =2log[2tanh(r/2)/r],

which proves (21). The affine contraction in L1 identifies the positive-series solution uniquely.

Put epsilon_m=2^(1-2m). The bounded V_m is exactly the conditional law of Vtilde_m given Vtilde_m<=2. Quantile coupling gives V_m<=Vtilde_m, and coupling every factor and X_j yields

    W_m>=Wtilde_m almost surely.

The optimal W1 distance is therefore their mean difference, which is EXACTLY

    delta_m = 3 epsilon_m(4m^2-1)/[16-(12m+10)epsilon_m].             (22)

The denominator is positive for every m>=1. This follows either from the mean contraction or directly: at m=1 it is 5; thereafter the subtracted term decreases. In particular delta_m=O(m^2 4^(-m)). No unbounded perpetuity tail is omitted in this coupling.

For every complex t in Re t>=0,

    |P_m(t)-Ptilde_m(t)| <= |t| delta_m.             (23)

The estimate follows by integrating the derivative of exp(-tu) along the interval between the coupled nonnegative variables. On the real positive axis,

    0<=Ptilde_m(t)-P_m(t)<=t delta_m.                (24)

**The limitation is essential.** The Mellin functional in (20) contains t^(m-q-1). A small right-half-plane Laplace error is not automatically a small companion error. The literal bound obtained from (23) is, for sigma=Re q<m+1, with the reciprocal gamma interpreted by its entire continuation,

    |G_m(2q)-Gtilde_m(2q)|
      <= (pi/6)^sigma delta_m/[2|Gamma(-q)|]
                         integral_0^infinity t^(m-sigma)L(t)dt,    (25)

where Gtilde is (19) with Ctilde. The integral is exactly

    4 Gamma(2m-2sigma+3)
       (1-2^(-(2m-2sigma+3))) zeta(2m-2sigma+3)
                          /6^(m-sigma+1).            (26)

The wider range in (25) requires cancellation, not separate extension of its two Mellin integrals: P_m(t)-Ptilde_m(t)=O(t) at zero. Thus the integral of t^(m-q-1)L(t)[P_m(t)-Ptilde_m(t)] is holomorphic for Re q<m+1, agrees with the entire companion difference on Re q<m, and extends it by the identity theorem. Equation (23) then proves (25) on the stated wider range. The positive odd-integer series used for (26) is absolutely convergent there. The factorial growth in (26) can overwhelm delta_m. We do not infer vanishing Mellin error, relative error near zeros, or phase preservation from (23).

### Exact survival-factor representation of the omitted cutoff

There is a stronger whole-source identity than the W1 estimate. Put c=2m-1, epsilon=epsilon_m and H_m=L P_m. Differentiating the ORIGINAL bounded-dilation affine integral gives

    2t P_m'(t)+c P_m(t)
                  =a_m^(-1)[H_m(t)-epsilon H_m(t/4)].             (26a)

This retains the complete delayed term. Comparing it with the Pareto differential equation and using c a_m=1-epsilon yields

    d/dt [P_m(t)/Ptilde_m(t)]
       = epsilon/[2a_m t Ptilde_m(t)] [H_m(t)-H_m(t/4)].           (26b)

For every t>0 the right side is strictly negative, since H_m is the Laplace transform of the strictly positive C_m. The ratio tends to one at zero. It tends to ZERO at infinity: P_m(t)<=L(t/4) decays exponentially in sqrt(t), while Ptilde_m(t) is asymptotic to a positive constant times t^(-m+1/2), by (21).

Consequently the explicitly defined function

    w_m(t)=epsilon/[2a_m t Ptilde_m(t)] [H_m(t/4)-H_m(t)], t>0,   (26c)

is a positive probability density on (0,infinity), including its WHOLE tail, and

    P_m(t)=Ptilde_m(t) Pr(T_m>t),
    Pr(T_m>t)=integral_t^infinity w_m(u)du,
    integral_0^infinity [H_m(t/4)-H_m(t)]/[t Ptilde_m(t)]dt
                                                        =2a_m/epsilon. (26d)

Here T_m denotes a new positive random variable with this prescribed density; it is unrelated to the operator T. In particular no zero locations enter its definition. At the origin w_m(0+)=delta_m, by differentiating the ratio or using the exact means. The factor is a survival function, NOT an asserted completely monotone function or zero-preserving multiplier.

For Re q<m, absolute Fubini applied to (20) now gives the exact native-to-comparison relation

    G_m(2q)=(pi/6)^q/[2 Gamma(-q)]
       E [integral_0^(T_m) t^(m-q-1)L(t)Ptilde_m(t)dt].           (26e)

This is a positive mixture of truncated Mellin integrals, not a truncation of the source to finitely many perpetuity levels. Its positive mixing density and normalization have been proved from the literal source. It still does not yield complex-zero control: positive mixtures do not generally preserve real Fourier zeros. For example the mixture (2+cos z)/3 of 1 and cos z has nonreal zeros, although each component has only real zeros or no zeros. No general mixture-preservation assumption is used here.

## 6. HBR28-5: the comparison is an exact finite arithmetic-shift hierarchy

The comparison is not merely a heuristic leading law. Its entire companions can be written explicitly in terms of shifted xi.

Let, for k>=1,

    product_(ell=1)^(k-1)(v^2-ell^2)=sum_(j=0)^(k-1)d_(k,j) v^(2j),
    B_(m,j)=sum_(k=j+1)^m binomial(m-1,k-1)
                            2^(2k)d_(k,j)/(2k-1)! .              (27)

Define the entire coefficient

    R_j(s)=pi^(-j) [s/(s+2j)] ((3-s-2j)/2)_j
                           [2^(-s)-2^(2j)],                     (28)

where the rising product is 1 when j=0. At j=0 cancel s/s and set R_0(s)=2^(-s)-1. For j>=1 the apparent singularity at s=-2j is removable because the bracket vanishes there. Then

    Gtilde_m(s)=(2/3)^m/4 sum_(j=0)^(m-1) B_(m,j) R_j(s) xi(s+2j). (29)

The identity is an ENTIRE identity in s. Its diagonal B_(m,m-1)=2^(2m)/(2m-1)! is nonzero, so for every finite depth the comparison hierarchy is an invertible triangular combination of the prescribed arithmetic-shift functions R_j(s)xi(s+2j). This is a finite algebraic span statement, not infinite spectral completeness.

**Proof with all normalizations.** Substituting r=sqrt(6t), then a=r/2, into (20) and (21) gives, for Re q<m,

    Gtilde_m(2q)=(2/3)^m (pi/4)^q/Gamma(-q)
          integral_0^infinity a^(1-2q) tanh(a)^(2m-2) sech(a)^2 da. (30)

Expand tanh^(2m-2) sech^2 as sum_(k=1)^m (-1)^(k-1) binomial(m-1,k-1) sech^(2k). For sufficiently large Re z,

    integral_0^infinity a^(z-1) sech(a)^(2k) da
       =Gamma(z) 2^(2k-z)(-1)^(k-1)/(2k-1)!
                            sum_j d_(k,j) eta(z-2j-1),           (31)

where eta(w)=(1-2^(1-w))zeta(w). To verify (31), expand
sech^(2k)a=2^(2k)sum_(n>=k)(-1)^(n-k)binomial(n+k-1,2k-1)e^(-2na)
and use binomial(n+k-1,2k-1)=n product_(ell=1)^(k-1)(n^2-ell^2)/(2k-1)!. The polynomial vanishes at the missing n<k, so extending the sum to n=1 introduces no terms. Taking Re z>2k makes all termwise integrations absolutely convergent. Therefore (30) first equals

    (2/3)^m pi^q Gamma(2-2q)/[4 Gamma(-q)]
                             sum_j B_(m,j) eta(1-2q-2j).

Apply the gamma duplication formula and xi's functional equation. With s=2q, the individual identity is

    pi^(s/2) Gamma(2-s) eta(1-s-2j)/Gamma(-s/2)
                                      = R_j(s)xi(s+2j).

It initially holds away from the displayed gamma singularities; cancellation and (28) extend it. This proves (29) on a nonempty left half-plane, and then everywhere by the identity theorem and the entire positive-law definition (19). No inference about zeros of an individual shifted factor is needed.

### The first closed comparison is not a new zero-excluding companion

Equation (29) at m=1 is particularly revealing:

    Gtilde_1(s)=(2/3)(2^(-s)-1)xi(s).                (32)

For A(z)=Xi(z), its odd reflected companion is EXACTLY

    Btilde_1(z)=-(2/(3sqrt(2))) sin(z log 2) A(z),
    Im[A(z) conjugate(Btilde_1(z))]
       =(2/(3sqrt(2))) |A(z)|^2 cos((Re z)log 2)sinh((Im z)log 2). (33)

Thus every xi zero is a common zero, and even away from them the phase orientation changes sign across vertical bands. Any open band with cos((Re z)log 2)<0 contains points at which A is nonzero, since an entire nonzero function cannot vanish on an open set. Hence this candidate cannot satisfy a positive all-band phase condition. This refutation is an exact identity, not a numerical zero claim.

For m>=2, (29) reveals why one should compare this hierarchy with the shifted-xi variance corrections in #855 and the explicit dyadic factors in #859/#860. Those are relationships of representations, not transfers of an unproved sign.

## 7. HBR28-6: the native hyperbolic kernel is TP2 but not TP3

The real kernel of (8), with integration measure dy, is

    K(x,y)=(2/y) 1_(h(x)<y<x), 0<x,y<1.              (34)

It is totally nonnegative of order two: for x_1<x_2 and y_1<y_2, a negative 2-by-2 determinant would require both off-diagonal entries positive and at least one diagonal zero. But y_2<x_1 and y_1>h(x_2), together with the increasing h, force both diagonal entries positive. All possible binary 2-by-2 determinants are therefore nonnegative, and the positive column weights preserve their sign.

It is NOT totally nonnegative of order three, even for the literal unmodified source operator. Take

    (x_1,x_2,x_3)=(4/5,15/17,12/13),
    (h(x_1),h(x_2),h(x_3))=(1/2,3/5,2/3),
    (y_1,y_2,y_3)=(5/8,3/4,5/6).

All inequalities are strict. The indicator matrix is

    [1 1 0; 1 1 1; 0 1 1],

with determinant -1; after the column weights in (34),

    det[K(x_i,y_j)] = -512/25.                     (35)

This exact rational counterexample rules out the naive attempt to get a full variation-diminishing theorem by declaring the positive renormalization kernel totally positive. It does not refute any source-specific invariant subcone or a different representation, and does not concern a zero of xi.

## 8. End-to-end disposition of this attack

The intended chain was: literal Brownian source -> complete renormalization analysis -> solvable positive comparison or variation diminution -> complex-zero control -> RH.

The first two links are supplied here at their stated domains, including the full compact spectrum and resolvent tail. The solvable comparison is also explicit, and its relation to shifted arithmetic functions is exact. The putative zero-control links do not follow: the native kernel fails TP3, the first closed comparison has both shared zeros and sign reversals, and the exponentially small W1/Laplace comparison does not imply a small high-order Mellin defect. These are specific failures, not a refusal to pursue the problem.

The revised substantive task is to control the literal survival mixture (26e), or a source-specific signed combination of the actual D_m, with a norm or sign identity that controls (20) on the full critical band. Formula (26c) identifies the full cutoff law and (26d) its exact normalization; neither replaces that complex-phase estimate. Any successful claim must supply a strict zero-exclusion or an all-order positive form, including common-zero handling and the full Mellin tails. Positivity of the perturbation eigenvalues in (13) cannot stand in for that argument. The gamma weighted-defect criterion in #862 remains a possible consumer only if a genuine source-preserving sign/defect estimate is proved. This manuscript does not prove such an estimate or give a completed RH proof.

## 9. Attribution and review boundary

The fixed Brownian source, its Mellin identification with xi, gamma duplication, eta's dyadic factor, and the functional equation are classical. The positive perpetuity modes and finite-jet observation were already in #856. This packet's proposed contributions are the precise hyperbolic operator normal form, the named-space spectral/resolvent completion, the full cutoff comparison and survival-factor law, the explicit arithmetic-shift hierarchy in this normalization, and the native TP3 obstruction. No priority claim is made beyond the present repository contribution; a literature-wide originality audit was not performed.

Review equations (8)–(16), the entire-source division in (17), the domain distinction in (25), and all constants in (27)–(33). The exact checker verifies finite rational identities and counterexamples; it is not a formal proof of the infinite analytic arguments. `SOURCES.json` and `VALIDATION.md` specify the files actually inspected and the executed tests.
