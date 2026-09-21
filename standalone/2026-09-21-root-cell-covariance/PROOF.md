# RSC26 — local isometry and full residual covariance control

**Proposed component proofs for independent review. No all-scale native coarse-energy bound, full Newton gain, or RH proof is claimed.** This additive continuation uses DCN26 at `f80aa1346bbc457d5726977c0b720162c05bb70e`. The principal change is to project the OUTPUT rather than select another sparse set of product pairs. The remaining coarse term is not discarded.

Classical ingredients are summation by parts, orthogonal projection, discrete Poincare, divisor bounds and short-prefix Dirichlet inversion. The global innovation isometry and capped completion are inherited from NIR26/PCR26. The local polarized identity and its application below are supplied in full, without a field-wide novelty claim.

## 1. An exact local physical/innovation isometry

For a real sequence a(n), put

    A(k)=sum_(n<=k)a(n),   r(k)=sum_(n<=k)a(n)/n,
    eta_k=r(k)-A(k)/(k+1),   A(0)=r(0)=eta_0=0.

Let C=[s,t] be an inclusive integer interval, ell=t-s+1, and

    w_k=1/[k(k+1)],   W_C=sum_C w_k=ell/[s(t+1)].

For positive weights define V_w(f)=sum w*f^2-(sum w*f)^2/sum w. For unit weights write V(f).

**RSC26-1.** At EVERY interval, with no arithmetic or size assumption,

    V_w(A|C) = V(r|C).                                      (1)

The equality also holds for the associated bilinear covariance by polarization.

Proof. Since eta_k-eta_(k-1)=A(k)/[k(k+1)] and r(k)=eta_k+A(k)/(k+1), direct expansion gives

    r(k)^2-A(k)^2/[k(k+1)]
      =(k+1)eta_k^2-k eta_(k-1)^2.

Summing yields

    sum_C r(k)^2-sum_C w_k A(k)^2
      =(t+1)eta_t^2-s eta_(s-1)^2.                         (2)

Two telescopes give the cell means

    u_C=sum_C w_k A(k)=eta_t-eta_(s-1),
    v_C=sum_C r(k)=(t+1)eta_t-s eta_(s-1).                 (3)

Expansion of the two squares shows

    v_C^2/ell-u_C^2/W_C=(t+1)eta_t^2-s eta_(s-1)^2.

Subtract this equality from (2). QED.

Thus the local residuals agree, NOT the uncentered full energies or their coarse pieces. For complex sequences use absolute squares and sesquilinear polarization. No endpoint or completion correction may be removed from (2).

## 2. All product pairs have an exact rational residual kernel

Keep PCR26's literal column

    K_d(k)=[H_floor(k/d)-H_k+log d]/d,   H_0=0.

Consider the arithmetic source a_d(n)=1_(d divides n)-1/d. Its ordinary and reciprocal cumulatives are

    A_d(k)=floor(k/d)-k/d=-{k/d},
    r_d(k)=[H_floor(k/d)-H_k]/d.

K_d differs from r_d by a constant, killed ONLY by subtracting its cell mean. Polarizing (1) therefore gives

    sum_C (K_d-mean_C K_d)(K_e-mean_C K_e)
      =sum_C w_k(A_d-mean_w A_d)(A_e-mean_w A_e).          (4)

The right side is a completely explicit RATIONAL fractional-part covariance. It holds for arbitrary d,e, whether near or far, squareclass-matched or unmatched, and whether or not either product is above t. For d>t the right column is -k/d, not zero.

Let P be unweighted orthogonal averaging on any partition into integer intervals; Pi is weighted averaging in the physical norm. For the finite product source z=c*c,

    ||Q||^2 = ||P Q||^2 + ||(I-P)Q||^2,
    ||(I-P)Q||^2 = sum_(d,e)z(d)z(e) Cov_C(K_d,K_e),      (5)

summed over all cells and ALL product indices. Formula (4) identifies this residual matrix with the physical residual matrix. This is a partition in observation space, NOT an absolute entrywise envelope or another partition of d,e pairs. It does not permit assigning the residual bound to the coarse matrix.

## 3. Root cells give a logarithmic worst-case residual

Fix an integer q>=1. Cells are the nonempty level sets of floor(q sqrt(k)), intersected with b<=k<b^2. Their endpoints are computed using integer squares; no floating threshold is used. The q=2,4 partitions refine q=1.

Assume |a(n)|<=1. The pairwise variance formula

    V_w(A)=(1/W_C) sum_(i<j in C) w_i w_j(A(j)-A(i))^2

and |A(j)-A(i)|<=j-i show that the largest possible residual is attained by a(n)=1 on the relevant increments. The same conclusion follows from |r(j)-r(i)|<=H_j-H_i. Consequently

    0<=V_w(A|C)=V(r|C)<=U_C,                              (6)
    U_C=ell-h-h^2/W_C,  h=H_(t+1)-H_s.

Indeed sum_C w_k*k=h and sum_C w_k*k^2=ell-h. By (1) applied to a=1, U_C is also

    U_C=sum_C H_k^2-(sum_C H_k)^2/ell.                   (7)

The two formulas are exactly equal, not alternative approximations. They are implemented separately in the two coordinate checks.

For fixed q and b tending to infinity,

    U_(b,q):=sum_cells U_C=(log b)/(3q^2)+O_q(b^(-1/2)).   (8)

Here is an elementary error justification. On a cell of length ell,

    ell(ell^2-1)/(12 t^2) <= U_C
      <= ell(ell^2-1)/(12(s+1)^2).

This follows by bounding each H_j-H_i between (j-i)/t and (j-i)/(s+1), and using sum_(i<j)(j-i)^2=ell^2(ell^2-1)/12. A complete root cell has ell=2sqrt(s)/q+O_q(1). Thus

    U_C=ell/(3q^2 s)+O_q(1/s).

The sum of 1/s over these cells between b and b^2 is O_q(b^(-1/2)); the same bound controls the error replacing sum ell/s by integral_b^(b^2) dx/x. Each of at most two clipped end cells costs O_q(b^(-1/2)). This proves (8). No prime theorem or Mobius cancellation enters.

The coefficient 1/(3q^2) is sharp for this bounded-increment class, since the ramp attains every U_C. This is a uniform bound for the fine-scale part of native M and m, not a conjectural random-sign estimate.

## 4. A full harmonic residual bound for capped sources

Let |c(n)|<=K, with finite support, and sum c(n)/n=0. Set z=c*c and Q=sum z(d)K_d. All products remain in this definition. The reciprocal moment gives sum z(d)/d=0, and therefore

    Q(k)-Q(k-1)=(1*z)(k)/k,
    |(1*z)(k)|<=K^2 tau_3(k).                            (9)

Without the moment condition there is an additional term -(sum z(d)/d)/k; it cannot be silently omitted.

On an ell-point interval, the pairwise difference formula and Cauchy give

    V(f)<= (1/2)sum_(j=1)^(ell-1) j(ell-j)|Delta f_j|^2
         <=ell^2/8 sum_internal |Delta f|^2.             (10)

For a q=1 root cell j^2<=k<(j+1)^2, ell<=2j+1, while every internal increment index k>=j^2+1. Thus ell^2/k<=5, since

    5(j^2+1)-(2j+1)^2=(j-2)^2>=0.

Apply (9)-(10) and tau_3^2<=tau_9:

    ||(I-P)Q||^2 <=(5/8)K^4 sum_(k<=B)tau_3(k)^2/k
                  <=(5/8)K^4 H_B^9.                   (11)

The divisor inequality follows by the standard matrix-of-exponents argument; sum tau_9(k)/k<=H_B^9 follows from expanding a ninefold harmonic product. Refining the partition only decreases residual energy. This is an all-scale bound for the full signed residual in (5), not its absolute off-diagonal mass. It has NO small-prime bank or quotient restriction.

### Stronger native bound, with the collar paid

For the actual Mobius prefix through Y, use PCR26's cap-three completion c. Its support L satisfies L<=Y+ceil(Y/2). Native reconstruction below b^2 gives

    (1*z)(n)=2c(n)-mu(n),   Q(k)=2m_c(k)-m(k).            (12)

Thus the increments have size at most 7/k in the collar, and at most 1/k after L. Pairwise variance gives the finite bound

    ||(I-P)Q||^2 <= U_Q:=sum_C gamma_C^2 U_C,
    gamma_C=7 if cell start<=L, and 1 otherwise.          (13)

This intentionally overpays the cell straddling L. In particular, for fixed q,

    U_Q <= (log b)/(3q^2)+16 log(3/2)/q^2
           +O_q(b^(-1/2)).                              (14)

To obtain (14), the extra factor 48 applies only up to L+O_q(sqrt(L)); use the proof of (8) on this bounded-ratio collar. The exact computable (13), not the asymptotic constant, is used in every finite certificate.

## 5. Complete endpoint certificates, not an omitted mean

For mu, retain

    E_n=sum_(k<=n) M(k)^2/[k(k+1)],
    F_n=sum_(k<=n)m(k)^2=E_n+(n+1)eta_n^2,
    A_n=E_n+2(n+1)eta_n^2,   F_n<=A_n<=2F_n.

Let B=b^2-1. Equations (3),(6) give

    A_B <= E_Y + sum_C (eta_t-eta_(s-1))^2/W_C
                 +U_(b,q)+2b^2 eta_B^2,                (15)
    F_B <= F_Y + sum_C [(t+1)eta_t-s eta_(s-1)]^2/ell
                 +U_(b,q).                            (16)

The inputs after Y are endpoint eta-values, not the measured residual or full annular energy. The last term in (15) is the actual completion cost. Dropping it is not allowed. The implementation stores M and m separately so their arithmetic can be checked; one eta-value per required boundary suffices mathematically.

For fixed q the certificate uses O(qb) cells versus Theta(b^2) output indices. This is a sparse certificate, not a claim that we computed all its arithmetic endpoints without processing the full output: this pass's verifier generates that output from the short prefix by classical Dirichlet Newton reconstruction.

## 6. A finite simultaneous gain theorem actually certified

The desired inherited candidate is

    1+A_((Y+1)^2-1) <=2(1+A_Y)^(3/2).                   (G)

This packet proves (G) for EVERY integer 1<=Y<=2047, as a finite certificate. It is not a cofinal sequence or an all-scale theorem.

The maximum endpoint is N=2048^2-1=4,194,303. The q=4 endpoint certificate (16) gives

    F_N <= V <1.858259550206,
    (1+2V)^2<32.

All authoritative comparisons use outward integer intervals, not these printed decimals. Monotonicity of F, A_n<=2F_n, and A_Y>=F_1=1 now give, simultaneously for every Y in the stated range,

    1+A_((Y+1)^2-1) <=1+2V<4sqrt(2)
                         <=2(1+A_Y)^(3/2).

In addition, each of the ten displayed stages and each q=1,2,4 passes its own full (15) gain test. The single maximum-range bound proves the intervening cutoffs; they are not interpolated from those ten examples.

## 7. What is NOT closed

Write m(k) as its coarse cell mean plus its orthogonal residual. Equation (16) isolates the remaining coarse energy exactly. It is still necessary to prove a suitable all-scale bound on

    sum_C [(t+1)eta_t-s eta_(s-1)]^2/ell.                 (17)

For example a polynomial-in-log-b bound on (17) along the square ladder, combined with (8), would give polylogarithmic F and the inherited Mellin continuation ending. NO SUCH BOUND IS ESTABLISHED. Nor is (17) asserted easier than the underlying arithmetic cancellation problem.

The known nonnative cap-three fake source gives a decisive control: its Q-energy is about 170.56 at Y=15 and 968.75 at Y=31, with respective coarse energies 167.88 and 966.13. The fine residual is only about 2.68 and 2.62. Thus a small fine residual can coexist with a large coarse component even for a balanced capped Newton source. An energy-only extrapolation is invalid.

Even on arbitrary partitions one cannot reduce the generic fine error for free. For the ramp on n indices in [X/2,X], any partition into J intervals has weighted residual at least

    [n^3/J^2-n]/[12X(X+1)].                              (18)

Proof: min w>=1/[X(X+1)]; minimizing over each cell's constant gives at least that factor times ell(ell^2-1)/12. Sum and use sum ell^3>=n^3/J^2. This shows the square-root order of the grid is natural for a uniformly small bounded-source residual. It does not preclude better source-specific compression.

The outcome is global fine-scale control, an exact local adapter between the two old metrics, and complete finite certificates. It is NOT closure of the full unbounded covariance gap. No prior canonical claim is promoted.
