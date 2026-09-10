# Finite nonreal defects of centered gamma approximants

Date: 2026-09-10. Status: **PROPOSED component theorems, pending independent mathematical review. RH and the vanishing-defect estimate remain OPEN.**

This continues the exact centered family of PR #855 at `0e19b74fe6dfb39bef69a5edd3f0b3098b10a6ad`. It does not change that source or the integration candidate. The new argument is not another improvement of an absolute approximation rate. It proves that the infinite spectrum at each finite stage has only finitely many nonreal exceptions, identifies their exact moment-form index, and gives a quantitative real-zero replacement whose error is controlled by one nonnegative scalar. Its vanishing for the actual arithmetic cascade is not proved.

Classical ingredients include simplex convolution, endpoint Laplace/Watson asymptotics, Hadamard products, Jensen's formula, polynomial separation and inertia. No priority is claimed for these general mechanisms or for moment formulations of RH. Full proofs of the applications and constants used below are supplied.

## 1. Exact source and an independent convergence argument

Let G_n be independent gamma variables of shape two and rate one. Set

    X_N = sum_(n=1)^N G_n/n^2,     X = sum_(n>=1) G_n/n^2,
    tau_N = 2 sum_(n>N)n^-2,       v_N = 2 sum_(n>N)n^-4.

Write f_N for the density of X_N and f for the density of X. Define

    g_N(x) = f_N(x-tau_N) 1_(x>tau_N),
    h_N(t) = sqrt(g_N(pi exp(2t)) g_N(pi exp(-2t))),
    Z_N = integral_R h_N(t)dt,
    F_N(z) = Z_N^-1 integral_R h_N(t) exp(izt)dt.       (1)

**Notation:** F_N in this packet is the parent's CENTERED Fhat_N, not its raw F_N. Let

    T_N = (1/2) log(pi/tau_N),  alpha_N=N-1/2, beta_N=N+1/2.

The support of h_N is [-T_N,T_N]; it is positive in the interior, even, and zero at both endpoints. Since 0<tau_N<=tau_1=pi^2/3-2<13/10<pi, T_N>0. F_N is real even entire, of exponential type at most T_N, F_N(0)=1, and

    F_N(iy) > 0 for EVERY real y.                      (2)

Thus there are no imaginary-axis zeros, including zero. Nonreal zeros occur in quartets {rho,bar(rho),-rho,-bar(rho)} with rho in the open first quadrant.

The classical BPY/Jacobi source identity [E1], in this scaling, is

    E[(X/pi)^(s/2)] = 2 xi(s),
    f(pi^2/x)=(x/pi)^(5/2)f(x),
    Phi(z):=Xi(z)/Xi(0)
      = integral h(t)exp(izt)dt / integral h(t)dt,
    h(t)=sqrt(f(pi exp(2t)) f(pi exp(-2t))).            (3)

Xi(z)=xi(1/2+iz); xi is the ENTIRE completion, xi(0)=xi(1)=1/2. This arithmetic identity is an explicitly imported classical theorem, not a claim about arbitrary gamma laws.

For completeness, the convergence needed below does NOT rely on the parent's infinite differential-product or its O(N^-3) expansion. Put U_N=sum_(2<=n<=N)G_n/n^2 and R_N=X-X_N. The first density f_1(x)=x exp(-x)1_(x>0) is globally Lipschitz with constant one. Independence and coupling give, at EVERY real x,

    |g_N(x)-f(x)| <= E|R_N-tau_N| <= sqrt(v_N) ->0.    (4)

Indeed apply the Lipschitz estimate to f_1(x-U_N-tau_N) and f_1(x-U_N-R_N). The limit has a positive density by this same convolution.

The complete exponential moment of U_N telescopes:

    E exp(U_N)=product_(n=2)^N (1-n^-2)^-2
              =(2N/(N+1))^2 <=4.

Consequently f_N(x)<=4x exp(-x), and for every N,t,

    h_N(t)<=4pi exp(tau_N)exp(-pi cosh(2t))
          <=64 exp(-3 cosh(2t)).                      (5)

The inequality includes the region where h_N is zero. The same bound holds for h. Equations (4),(5) and dominated convergence prove F_N->Phi locally uniformly in C and after every fixed spectral derivative, since exp(R|t|)|t|^k times (5) is integrable for every fixed R,k. **No zero-location statement or zero simplicity is used.** The parent's faster O(N^-3) rate remains a separate proposed result; this proof does not newly review it.

### A uniform normalization, growth and zero-count budget

Let V_N=U_N+tau_N. Its mean is exactly tau_1<13/10, so P(V_N<=13/5)>1/2. For 3<=x<=4 and V_N<=13/5, x-V_N lies in [2/5,4]. On that interval u exp(-u)>1/16 (check the two endpoints and the derivative; exp(4)<64). Thus g_N(x)>1/32. If |t|<=1/100, both pi exp(2t) and pi exp(-2t) lie in [3,4]. Therefore

    Z_N > 1/1600,
    h_N(t)/Z_N <=102400 exp(-3 cosh(2t)).              (6)

For r>=0 split exp(-3 cosh(2t)+r|t|) using cosh(2t)>=exp(2|t|)/2. The maximum of r|t|-(3/4)exp(2|t|) is at most (r/2)log(r+2), and

    integral_R exp(-(3/4)exp(2|t|))dt <=4/3<2.

This proves the deliberately coarse, N-INDEPENDENT entire-growth bound

    M_N(r):=max_(|z|<=r)|F_N(z)|
          <=204800 (r+2)^(r/2).                       (7)

Also, for |z|<=1,

    |F_N(z)-1| <=204800 |z|,

using |exp(izt)-1|<=|z||t|exp(|t|) and 3cosh(2t)>=2|t|. Hence no F_N has a zero with |z|<=delta:=1/409600. This is only a crude normalization guard, not a useful zero-free height for xi.

Let n_N(r) count ALL complex zeros in |z|<=r, with multiplicity. Jensen's formula at radius 2r gives, for r>=1,

    n_N(r) <=26+2r log(2r+2).                         (8)

We used log(204800)<13 and log 2>1/2. Boundary radii follow by limits. Partial summation, retaining its boundary term before dropping the favorable part, gives

    sum_(|rho|>R) mult(rho)/|rho|^2
       <=26/R^2+4[log(4R)+1]/R,  R>=1.               (9)

The same estimates hold for Phi by the locally uniform limit or the source bounds. In particular the paired inverse-square products below converge, uniformly in this zero-tail sense as N varies. A single global constant S_*<infinity bounds the sum over positive-real-part representatives of mult(rho)/|rho|^2; for example S_*=32 delta^-2+32 is sufficient by (8),(9). This constant is intentionally not practical.

## 2. GFD1: a positive simplex representation resolves the endpoints

View X_N as the sum of m=2N independent exponentials, with rate list

    lambda=(1,1,4,4,...,N^2,N^2).

A direct simplex change of variables in the convolution density gives, for x>0,

    f_N(x)=a_N x^(m-1) r_N(x),
    a_N=(N!)^4/(2N-1)!,
    r_N(x)=E exp(-x L_N),  L_N=sum_(j=1)^m lambda_j U_j, (10)

where U is uniform probability on the simplex {u_j>=0,sum u_j=1}. In particular 1<=L_N<=N^2. This r_N is normalized by r_N(0)=1, is entire, and is strictly positive on the real axis. It is completely monotone for x>=0.

For any real x and any y with |y|<pi/(N^2-1), rotate r_N(x+iy) by exp(iy(N^2+1)/2). Its real part is

    E exp(-x L_N) cos(y[L_N-(N^2+1)/2]) >0.           (11)

So r_N is zero-free in that horizontal strip. When N=1 it is exp(-x) and has no zeros anywhere. Neither f_N nor an unnormalized difference of its partial fractions is substituted for r_N in this assertion.

Equation (10) also gives the exact Taylor expansion

    r_N(x)=sum_(k>=0) (-1)^k h_k(lambda) x^k/(m)_k,    (12)

where h_k is the complete homogeneous symmetric polynomial and (m)_k the rising factorial. In particular

    r_N'(0)=-(N+1)(2N+1)/6.                           (13)

### A positive evaluation formula with its complete remainder

With B=N^2, the same simplex identity can instead be written

    r_N(x)=exp(-Bx) sum_(k>=0) h_k(B-lambda) x^k/(m)_k, x>=0.

Every coefficient here is NONNEGATIVE. Since 0<=B-L_N<=B-1, its k-th term is at most v^k/k!, where v=(B-1)x. Truncation after K is bounded, whenever v/(K+2)<1, by

    0<= r_N(x)-exp(-Bx)sum_(k=0)^K h_k(B-lambda)x^k/(m)_k
       <=exp(-Bx) [v^(K+1)/(K+1)!]/[1-v/(K+2)].

This gives an outward rational/exponential density evaluation without cancellation of the order-(2N-1) zero. The checker encloses the exponential by a rational Taylor sum with its entire geometric remainder, then cross-checks a separate partial-fraction evaluation. These are finite gamma-density values, not a certificate of a Fourier zero or of the all-N complex theorem.

The factorization (10) is useful analytically and numerically: it separates a known high-order zero from a positive, zero-free analytic factor, rather than subtracting large nearly equal exponentials near x=0.

Set tau=tau_N, T=T_N and q_+(t)=pi exp(2t)-tau, q_-(t)=pi exp(-2t)-tau. Exactly,

    q_+(t)q_-(t)=pi^2+tau^2-2pi tau cosh(2t).

The quotient by T^2-t^2 is positive on [-T,T] and has removable, nonzero values at the endpoints. Its nearest other zeros have imaginary part at least pi. Equation (11), or compactness and positivity, supplies a zero-free complex neighborhood for both r_N(q_+) and r_N(q_-). For example a sufficiently small tube width below

    min(1/8, tau/(64 pi N^2))                         (14)

keeps the arguments inside a strictly smaller strip than (11); reducing the width further if necessary avoids the removed endpoint factors. There is therefore a positive even REAL-ANALYTIC amplitude A_N near the whole interval such that

    h_N(t)=(T^2-t^2)^(N-1/2) A_N(t),  |t|<T.          (15)

Branches in a complex neighborhood are specified by continuation from positive real values. We do not assume h_N itself is analytic across either algebraic endpoint.

Let ell=pi^2/tau-tau. At the right endpoint,

    h_N(T-u)=c_N u^alpha [1+d_N u+O_N(u^2)],          (16)
    c_N=sqrt(a_N (2tau)^(2N-1) f_N(ell))>0,
    d_N=alpha -tau (N+1)(2N+1)/6
                    -(pi^2/tau) f_N'(ell)/f_N(ell),
    alpha=N-1/2.

The left endpoint has the identical expansion by evenness. To verify d_N, use q_-(T-u)=2tau u(1+u+O(u^2)), q_+(T-u)=ell-2pi^2 u/tau+O(u^2), and (13). Every constant depends on the actual gamma source and is finite.

## 3. GFD2: at each finite stage only finitely many zeros are nonreal

**Theorem.** For every fixed integer N>=1 there is a finite B_N such that EVERY zero of F_N with |z|>B_N is real and simple. For all sufficiently large integers k there is exactly one positive zero near

    x_(N,k)=(pi/T_N)[k+N/2+3/4],

and it satisfies

    rho_(N,k)=x_(N,k)+beta_N d_N/(T_N x_(N,k))
                          +O_N(x_(N,k)^-2).          (17)

There are no other sufficiently large zeros in the WHOLE complex plane, not just on a previously sampled strip. B_N, the first k, and the error constants depend on N. No evaluated cutoff, uniform bound in N, or critical-window confinement is asserted.

**Proof near the real direction.** Drop normalization, which cannot change zeros, and write I(z)=integral_-T^T h(t)exp(izt)dt. On a small upper rectangle, the branch (T^2-t^2)^alpha A_N(t) is analytic away from its two boundary endpoints. Its endpoint singularities are integrable since alpha>-1. Small endpoint arcs have vanishing integral. Deform the interval upward by a fixed permissible eta>0. The result is the upper horizontal segment plus the upward left endpoint segment minus the upward right endpoint segment.

For z=x+iy with x>=|y| and x->infinity, the horizontal integral is O_N(exp(T|y|-eta x)). On the two vertical segments use (16), with u=+iv at the left and u=-iv at the right. Their Laplace factor is exp(-zv). Taylor's remainder is O_N(v^(alpha+2)); integrating its absolute value gives O_N(x^(-alpha-3)), hence O_N(|z|^(-alpha-3)) in this sector. Extending the two leading monomial integrals to infinity introduces an exponentially small error. Exactly integrating them gives, with beta=alpha+1 and theta=Tz-pi beta/2,

    I(z)=2 c_N Gamma(beta) z^-beta
          [cos(theta)+(beta d_N/z)sin(theta)
                        +O_N(exp(T|y|)/|z|^2)].      (18)

The power z^-beta is on the right-half-plane branch. In obtaining (18), the endpoint multipliers are exp(+i pi beta/2) at the left and exp(-i pi beta/2) at the right; reversing them would give the wrong phase in (17). This is a direct endpoint Watson calculation; [E2] records the classical general mechanism.

For 1<=|y|<=x and sufficiently large x, |cos(theta)|>=sinh(T|y|), which is a fixed positive fraction of exp(T|y|). The other terms are smaller. There are no zeros there. For |y|<=1, the identity

    |cos(a+ib)|^2=cos^2 a+sinh^2 b

shows that a zero must be within O_N(1/x) of one of the real centers x_(N,k). Choose disks of radius C_N/x_(N,k), with C_N large enough. On their boundaries the cosine dominates the error in (18). Rouche's theorem gives exactly ONE zero, counting multiplicity, in each disk. The disks are invariant under conjugation and F_N is real entire, so that single zero is real and simple. Expanding (18) at its center gives (17). The same estimates exclude all points between the disks.

**Proof near the imaginary direction.** For y>=|x| and |z|->infinity use t=-T+u on the original real interval. With w=y-ix=-iz, Re w>=|w|/sqrt(2). Apply (16) near u=0, while the remaining interval is exponentially damped. Direct integration and a bounded Taylor remainder give uniformly in this sector

    I(z)=c_N Gamma(beta) exp(-izT) w^-beta
                              [1+O_N(|z|^-1)].       (19)

The leading term is nonzero. Thus no sufficiently large zeros occur in this sector. Conjugation and evenness cover the remaining directions. Combining (18),(19) proves the whole-plane theorem. QED.

**Effectivity boundary.** The proof's constants may in principle be bounded from the explicit finite density, a zero-free tube, compact Cauchy bounds and c_N>0, followed by the displayed elementary tail estimates. This packet does NOT implement an all-plane cutoff generator or a complete root census. A mere asymptotic formula on the real axis would not prove the whole-plane conclusion; (19) and the uniform sector of (18) are essential.

The asymptotic density is T_N/pi on the positive real axis with N fixed. Passing first to large spectral frequency at fixed N is not interchangeable with taking N->infinity toward xi. No limiting arithmetic zero count follows from this fixed-N asymptotic.

## 4. GFD3: finite spectral repair with a quantitative cost

Let Q_N contain one rho=a+ib, a,b>0, from each DISTINCT nonreal quartet of F_N, and let m_rho be its analytic multiplicity. Q_N is finite by GFD2. Define

    Delta_N=sum_(rho in Q_N) m_rho b^2/|rho|^4 >=0.     (20)

The choice of FIRST-quadrant representatives matters to the constants below. Equivalently this is one quarter of the sum over ALL zeros, since real zeros contribute zero. Repeated zeros are counted with their multiplicity.

Hadamard factorization, evenness, F_N(0)=1 and order at most one give

    F_N(z)=product_(Re rho>0) (1-z^2/rho^2)^m_rho.     (21)

There is no quadratic exponential and no residual linear exponential; evenness removes the latter. The sum of |rho|^-2 is finite. For each nonreal quartet replace its pair factor by

    [(1-z^2/rho^2)(1-z^2/bar(rho)^2)]^m
                      --> (1-z^2/|rho|^2)^(2m).       (22)

Call the resulting entire function L_N. Only FINITELY many factors change. The apparent divisions are removable at their exactly specified zeros. L_N is real even entire of order at most one, L_N(0)=1, and all its zeros are real: it belongs to the classical Laguerre--Polya class. No claim is made that it is the characteristic function of a positive probability law, that it has a positive Fourier density, or that its zeros can be located without computation.

For one pair, writing r=|rho|,

    (1-z^2/rho^2)(1-z^2/bar(rho)^2)
       -(1-z^2/r^2)^2 = 4b^2 z^2/r^4.                (23)

Each pair factor is bounded by exp(2R^2/r^2) on |z|<=R. Apply the identity A^m-B^m=(A-B)sum A^j B^(m-1-j), then telescope the finite set of replacements in (21). With S_N=sum_(Re rho>0)m_rho/|rho|^2<=S_*, this proves

    max_(|z|<=R)|F_N(z)-L_N(z)|
              <=4R^2 exp(R^2 S_*) Delta_N.           (24)

The bound includes all unchanged real factors and every multiplicity. The constant is coarse but uniform in N. This solves the analytic COST of the finite repair; it does not prove that its cost tends to zero.

### The defect has a source-only Jensen representation

Let

    J_N(r)=(1/(2pi)) integral_0^(2pi)
                          log|F_N(r exp(i theta))|dtheta,
    mu_(2,N)=Z_N^-1 integral t^2 h_N(t)dt.

Circular zeros cause integrable logarithmic singularities; Jensen's formula is understood by the usual limiting radii. Tonelli applies to its nonnegative zero sum. Since

    integral_a^infinity log(r/a) dr/r^3=1/(4a^2),

we obtain

    S_N=2 integral_0^infinity J_N(r) dr/r^3,
    Delta_N=(1/2)integral_0^infinity J_N(r)dr/r^3
                                      -mu_(2,N)/8.   (25)

Indeed the coefficient of z^2 in (21) is -s_1, where s_1=mu_(2,N)/2. A quartet contributes 4m b^2/|rho|^4 to S_N-s_1. These factors of two and four are checked separately by the exact polynomial controls.

Thus no list of zero locations is necessary to DEFINE the cost from the source. Formula (25) may be numerically ill-conditioned through cancellation; no certified Jensen integral or actual Delta_N value is supplied here. In particular positivity of h_N does NOT establish the upper inequality which would make (25) vanish.

## 5. GFD4: the defect limit is exactly the off-axis xi defect

Define for the actual xi function

    Delta_xi=(1/4)sum_(Phi(rho)=0)
                    mult(rho)(Im rho)^2/|rho|^4.      (26)

The series converges absolutely by (9); Phi has no imaginary-axis zeros. In standard zeta coordinates a quartet contributes

    m (beta-1/2)^2/[gamma^2+(beta-1/2)^2]^2,

using one positive ordinate and beta>1/2. All multiplicities are retained; no off-line zero is asserted to exist.

**Theorem.** Unconditionally, on the classical BPY source identification,

    lim_(N->infinity) Delta_N = Delta_xi,
    RH iff Delta_xi=0 iff Delta_N->0.                 (27)

**Proof.** On a disk whose boundary contains no Phi zero, local uniform convergence and Rouche match the total multiplicity in small disks around each limiting zero and exclude zeros in the remaining compact region. The continuous function (Im z)^2/|z|^4 is bounded there because the common disk |z|<=delta has no zeros. Consequently the finite weighted sums converge, INCLUDING clusters at multiple real zeros. They need not remain real; their contribution tends to zero as their imaginary parts shrink.

The uniform complete tail bound is, directly from (9),

    (1/4)sum_(|rho|>R) mult(rho)(Im rho)^2/|rho|^4
        <=7/R^2+[log(4R)+1]/R, R>=1.                (28)

It holds for every F_N and Phi. Let N tend to infinity on each fixed disk and then let R tend to infinity. This proves convergence of the full sums. All summands of (26) are nonnegative, and any off-real zero makes a strictly positive contribution. Thus Delta_xi=0 is exactly reality of all Xi zeros, which is RH. QED.

The sufficiency also follows constructively from (24): if Delta_N->0, the real-zero entire functions L_N converge locally uniformly to Phi. Hurwitz excludes off-real zeros. This is a different proof of the implication, not an extra accepted premise.

**The new RH-facing target is therefore the single source-specific estimate Delta_N=o(1). It is NOT proved.** Unlike demanding global real-rootedness of every finite stage, it tolerates nonreal pairs, pair collisions and multiple-zero splitting. Unlike a bounded rectangle experiment, it pays the full complex zero tail through (28). Local uniform convergence alone proves convergence to Delta_xi, not that this unknown value is zero. The radial repair has not made the arithmetic obstruction disappear.

For a finite region already known independently to contain only simple real xi zeros, Rouche and conjugation show all its corresponding sufficiently late approximant roots are EXACTLY real. For multiple real zeros the weaker weighted convergence above is the correct claim. No unbounded region is certified by that observation.

## 6. GFD5: the whole trace-Hankel form has a finite, exact negative index

This connects the gamma continuation to the earlier trace/power-sum programme, WITHOUT requiring acceptance of an operator determinant. For each fixed N, take lambda=rho^-2 over the representatives Re rho>0, with analytic multiplicity, and put

    s_m=sum mult(lambda) lambda^m,   m>=1,
    H_d=(s_(i+j+2))_(0<=i,j<d),    d>=1.             (29)

Equivalently the s_m are obtained from the actual density moments:

    log F_N(z)=-sum_(m>=1) s_m z^(2m)/m
              near z=0,
    s_m=(-1)^(m+1) kappa_(2m,N)/[2(2m-1)!].          (30)

Cumulants belong to the probability h_N/Z_N. Ordinary moment Hankels and these cumulant/power-sum Hankels are different matrices. The square in the associated form is NOT an adjoint square:

    p^T H_d p = sum mult(lambda) lambda^2 p(lambda)^2. (31)

Let q_N=|Q_N| count DISTINCT nonreal quartets, not their summed multiplicities. Then

    sup_d n_-(H_d)=q_N,
    n_-(H_d)=q_N for every sufficiently large d.      (32)

The negative index of a real symmetric matrix is its number of strictly negative eigenvalues with multiplicity. The stabilization dimension is not evaluated, and no actual centered-gamma H_d has been numerically certified here.

**Upper bound.** Each real zero gives lambda>0 and a positive square. Each conjugate pair lambda,bar(lambda) contributes

    2m Re[(lambda p(lambda))^2],

which is a real quadratic form of signature (1,1) on its two real evaluation coordinates. There are q_N such pairs. Thus no polynomial subspace has more than q_N negative directions. A repeated zero changes the positive factor m, not the dimension two of this evaluation pair.

**Lower bound with the entire positive tail retained.** All real lambda lie in one compact interval [0,A]. For each nonreal lambda_j choose real polynomials p_j,k such that

    p_j,k(lambda_l)=delta_jl i/lambda_j,
    p_j,k(bar(lambda_l))=conjugate(p_j,k(lambda_l)),
    sup_[0,A]|p_j,k| ->0.                             (33)

Here is an elementary construction, rather than an assumption of spectral completeness. Multiply by the real polynomial L_j(x)=product_(l!=j)(x-lambda_l)(x-bar(lambda_l)). Map [0,A] linearly to [-1,1]. If z_j is the image of lambda_j, choose w_j=z_j+sqrt(z_j^2-1) with |w_j|>1. Since z_j is nonreal, w_j is nonreal. The Chebyshev identity

    T_k(z_j)=(w_j^k+w_j^-k)/2

shows that the real 2-by-2 system determining a_k,b_k from

    a_k T_k(z_j)+b_k T_(k+1)(z_j)
                           =i/[lambda_j L_j(lambda_j)]

is invertible for all sufficiently large k: its determinant is asymptotic to a nonzero multiple of |w_j|^(2k) Im w_j. Its solution has |a_k|+|b_k|=O_j(|w_j|^-k). On [-1,1] each Chebyshev polynomial has modulus at most one. This proves (33) after multiplying back by L_j.

For p=sum c_j p_j,k, the nonreal contributions in (31) are exactly -2sum m_j c_j^2. The ENTIRE real-zero contribution is bounded by

    q_N (max_j sup_[0,A]|p_j,k|)^2
                  (sum_(real lambda) m lambda^2) sum c_j^2,

which tends to zero. The sum is finite by (9). Thus the span of the q_N polynomials is negative definite for sufficiently large k. They are independent by their nonreal evaluations. Taking d larger than their degrees proves the lower bound. Enlarging d cannot decrease the index, and the upper bound persists, proving (32). QED.

**Important boundary.** Shift-two Hankel positivity alone forces real spectral nodes, not their positivity: a negative real node also gives a positive square in (31). The source property F_N(iy)>0 from (2) is what excludes such nodes here. Our exact negative-real-node control explicitly preserves this distinction.

This theorem measures a finite obstruction at each gamma stage. It does NOT say q_N is uniformly bounded, tends to zero, or is controlled by a successful finite leading-principal-minor test. The weighted cost Delta_N may vanish even when q_N does not.

## 7. The attempted universal variance-flow finish fails

The preceding proof suggests trying to bound creation of negative directions directly through the parent's variance correction. We tested that attempted finish, rather than calling the correction a real-zero-preserving evolution without checking it.

Drop the positive scalar denominator and define

    (S p)(z)=1/2[(z^2+3/4-iz)p(z-4i)
                  +(z^2+3/4+iz)p(z+4i)].             (34)

S=8pi^2 D in the parent's notation. The leading move from one centered stage toward the limit has the sign I-epsilon S, up to its harmless normalization and higher-order remainder. That is an asymptotic relation, not an exact update law on arbitrary polynomials.

For the real-rooted even polynomial p(z)=(z^2-a^2)^2, direct algebra gives

    (S p)(a)=-64(a^4-29a^2/4-3).                      (35)

At a=4 this is -8768. For p_epsilon=p-epsilon S p,

    epsilon^-1 p_epsilon(4+sqrt(epsilon)w)
                    ->64w^2+8768=64(w^2+137).                   (36)

The roots of this limiting quadratic are +/-i sqrt(137), simple. Rouche on fixed small disks about them proves nonreal roots of p_epsilon near 4+/-i sqrt(137 epsilon) for every sufficiently small positive epsilon. The symmetric pair near -4 behaves likewise. Thus this leading operator is NOT a universal real-root or strip-contraction mechanism. This exact counterexample uses a changed polynomial, not xi or a claim about the actual centered gamma stage.

The remaining plausible task must exploit the INTEGER-SQUARE gamma source, not merely positivity of a convolution kernel or the form of D. A bound Delta_N<=C/N^a for ANY fixed a>0 would suffice, but no such bound has been derived. Even Delta_N=o(1), without a rate, is the exact open arithmetic target.

## 8. Exploration and what is not certified

The separate scout uses the defining centered fourth-stage integral with t=T_4 sin(theta), removing the algebraic endpoint from the real numerical integrand. Two high-precision composite Gauss grids locate an apparent simple nonreal root near

    30.44805680701155406000392
            +0.65997805037132556792757 i.             (37)

These are nondirected mpmath calculations, NOT a root-count certificate. The two grids use the same primitive backend. No actual q_4, complete fourth-stage nonreal census, Delta_4 or high-frequency B_4 is certified. This is distinct from #855's certified RAW N=4 and intermediate-time examples. The new scout suggests global real-rootedness fails even after mean-centering, but the theorem package does not use that suggestion as a premise.

One precursor scout at N=8 stopped because partial-fraction cancellation lost density positivity at insufficient precision. No N=8 conclusion is inferred. The accepted exact checker below never uses a scout root or a floating quantity.

## 9. Research handoff

The completed proposed progress is:

1. Exact simplex/endpoint structure for the unchanged centered source.
2. Whole-plane eventual simplicity and reality, so each stage has finitely many nonreal quartets.
3. A finite real-zero repair with an explicit error bound and a source-only Jensen expression for its nonnegative cost.
4. Unconditional convergence of that cost to the actual xi off-axis defect, with a uniform complete tail budget.
5. Exact finite negative index of the trace-Hankel tower, counting distinct defect quartets without a simplicity assumption.
6. A tested failure of the generic variance-operator induction.

The central estimate Delta_N->0 remains unproved. No completed RH proof is claimed. A useful next theorem would control the full Jensen surplus in (25) along this integer-square cascade, or derive a source-specific bound on weighted defect creation and escape. This is not supplied by an absolute approximation error, the finite-index theorem alone, or the replacement's real zeros by construction.

### Sources and reading scope

[P] PR #855 at `0e19b74fe6dfb39bef69a5edd3f0b3098b10a6ad`, `standalone/2026-09-10-centered-gamma-continuation/PROOF.md`, Git blob `48dae66b76c92dccdd7d18fae61c6a5e23802569`. Full supplied principal manuscript read; local bytes authenticated against that blob. The family and context are retained. No parent numerical campaign is rerun or independently accepted, and its O(N^-3) expansion is not required for (27).

[P0] PR #849 at `11a12b8ceb7db98c7961a5cebf3870b2f31dfa79`, proposal blob `c324ba15d3f7f3e073b902042ec61c685b555f53`. The supplied proposal and finite partial-fraction formula provide provenance. This continuation independently derives the endpoint structure from positive simplex convolution.

[E1] Biane--Pitman--Yor, Probability laws related to the Jacobi theta and Riemann zeta function and Brownian excursions, arXiv:math/9912170; classical gamma/xi and reciprocal source identities. https://arxiv.org/abs/math/9912170 . The abstract metadata and the exact scaling in the supplied parent were inspected this pass; the complete external probability proof was not independently re-reviewed. This is an explicit classical import.

[E2] NIST DLMF 2.4(i), complex Watson lemma and contour rotation, https://dlmf.nist.gov/2.4#i . The relevant text and displayed formulas were inspected. The two-sector endpoint proof needed here is given in Section 3, rather than treating real-axis asymptotics as a whole-plane theorem.

[E3] NIST DLMF 1.10, entire functions, products and standard complex analysis, https://dlmf.nist.gov/1.10 . Hadamard factorization, Jensen and Rouche are classical inputs. The specialized even pairing, multiplicities, normalization and tail estimates are proved above.

The trace/power-sum connection was already part of the repository and previous supplied research. No priority claim is made for its general criterion or finite-signature viewpoint. This manuscript is new proposed research, not an integration review or mathematical acceptance record.
