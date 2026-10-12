# Pricing a common inverse/plain witness estimate

Status: exact conditional reduction and a complete scalar certificate; the new mixed moment is unproved.
Scope: the September 30 physical Hecke rows, with their original masks and common frequency. The conditional boundary is Re(s)>0.874956. RH remains open.
What ran: frozen-source inspection, exact rational Bernstein checks on the full exponent rectangle, and normal/optimized Python receipt comparison. No imported analytic proof or mixed-moment theorem was rebuilt.
Smallest new gap: prove J1 below for the actual arithmetic rows, including its smooth-profile and height uniformity.

## 1. Sources, prior work and the joint object

Use S, L and their frozen commits exactly as in `KAPPA_EXTENSION_CONDITIONAL.md`, Section 1. S's SHA-256 is `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`. We use the original kappa=3/4 and c=2/9 throughout; the new conditional reduction does not need the enlarged kappa range.

Repository PR #910, commit `670a76c1a3a8f325c43c1755b1cfc24d313a3e3c`, `UPSTREAM_HEIGHT_AND_MOMENTS.md`, Section 6.6 already proposes a common-frequency mixed moment of diagonal row size U. Its Sections 6 and 8 explain why marginal moments and an arbitrary-coefficient substitution do not prove it. The joint-moment direction is therefore prior work. This note adds an exact bottleneck configuration, a weaker length-priced hypothesis, a numerical conditional consequence with a full-domain certificate, and a coefficient-energy obstruction to a particular proposed proof shortcut.

The exact source is S, `prop:detector-witness`, lines 4510–4685. With D=U^r and N=U^m, its separated polynomials are

    M_r = D^(-1/2) sum_l mu(l) psi_u(l) F_M(q_l/D),
    S_m = N^(-1/2) sum_k       psi_u(k) F_S(q_k/N),

where both profiles contain the SAME real power and pure frequency:

    F_M(x)=W_1(x)V_le(Dx/D_*) x^(-sigma-i omega),
    F_S(y)=W_2(y)             y^(-sigma-i omega),
    omega=gamma-nu.

The product cutoff is separated by one Fourier variable nu, not independent heights for the two factors. Each presentation uses a fixed label in Theta times {+1,-1}; the inducing character varies with u. Keep every zero extension, sixth-power-free physical-row condition, nonprincipal exclusion and fixed finite ray convention of S. No new prime slots are inserted in the proposed mixed moment.

For any detector cutoff t in [1,3/2], the same row supplies

    r<=t+o(1),  r+m>=t-o(1),
    0<=m<=1/2+O(epsilon),
    |M_r S_m|^2 >= U^(delta(r+m)-epsilon),

where delta=2a-1. Sigma, the dyad, presentation and omega can all be selected separately by the row. They must be paid for by the input and its maximalization; a fixed common height across rows would be insufficient.

## 2. A weaker length-priced analytic target

**J1 (open arithmetic hypothesis).** Fix the finite arithmetic data, compact annular supports and every epsilon>0. There are finite seminorm and height orders J,A and uniform constants such that for the full eligible physical rows q_u asymptotic to U, each fixed presentation label, and the exact inverse/plain profile class above,

    sum_u |M_r(u;sigma,omega) S_m(u;sigma,omega)|^2
       << U^[1+lambda (r+m-1)_+ + epsilon] (1+|omega|)^A,
    lambda=49/100.

Require uniformity on the slightly padded compact set

    1/2-eta<=r<=1+eta,  -eta<=m<=1/2+eta,
    1-eta<=r+m<=3/2+2eta,

for every sufficiently small fixed eta>0; scales below one are treated with the original bounded-scale convention. A factor U^(C eta) is allowed, with an absolute C, since eta is chosen last inside the positive exponent reserve. Sigma ranges over the fixed detector strip. Constants may depend on fixed target ray data, eta and epsilon, but not on U, the row, dyadic length, sigma or omega. No arbitrary row-dependent coefficient is permitted.

The statement includes the same bound for the finitely many logarithmic profile derivatives needed to maximalize sigma and omega. Differentiating omega inserts log(q_l/D) and log(q_k/N), which are bounded on their annuli; differentiating sigma does likewise. These remain declared smooth profiles with the original inverse cutoff. A two-variable Sobolev bound on the compact sigma interval and |omega|<=C T_1, summed over rows before taking suprema, then gives the same U exponent times a finite power of (1+T_1). Dyadic and finite-presentation selection costs only U^epsilon. This is how J1 permits the source's independently selected row heights. Assuming only one fixed-height numerical instance would not suffice.

J1 is weaker than PR #910's U^(1+epsilon) target for r+m>1. It still needs arithmetic correlation between the inverse and plain factors. Neither the separate inverse second moment nor the plain fourth moment supplies it.

## 3. Freeze the actual obstruction

At L's original sharp scalar configuration, let w=sqrt(921). Then

    delta_c=(49-w)/48,
    x_c=1/2,
    t_c=(333+37w)/1295,
    r_c=(11+4w)/185,
    m_c=(256+9w)/1295,
    z_I=(87-2w)/185,  z_P=2 z_I/7.

Thus approximately

    delta_c=.3885837123,  t_c=1.1242280517,
    r_c=.7156320392,  m_c=.4085960126,
    z_I=.1421839804, z_P=.0406239944, R_c=2/3.

The same-character product spike has exponent delta_c t_c=.4368567098. To improve its row count below 2/3 at this PARTICULAR pair, a joint moment exponent below 1.1035233765 suffices. Marginal interpolation gives only the smaller of 1+delta_c m_c and 1+delta_c r_c/2, approximately 1.1390414772. This calculation quantifies the missing correlation at the old worst configuration, without assuming the detector must choose this pair at every cutoff.

For the universal t=1 detector used next, the critical length-price slope is

    lambda_* = 3 delta_c - 2/3 = .4990844701... .

A slope strictly below lambda_* beats the old worst row count. A local gain alone would not certify the entire exponent rectangle. Section 5 checks that complete requirement for lambda=.49.

## 4. Conditional physical row count

Choose the existing detector cutoff t=1. For r>=1+O(epsilon), S's no-slot inverse amplification has count exponent

    1-alpha+(alpha-delta)r,
    alpha=5/6,

and r<=1+o(1) makes this at most 1-delta+O(epsilon). If m>=1/2-O(epsilon), the existing no-slot plain fourth moment gives the same count exponent. These inputs have no selected-prime supply hypothesis (S, `eq:no-slot-inverse-count`, lines 15282–15314, and lines 15438–15445).

In the remaining case r<=1+O(epsilon), m<=1/2+O(epsilon), write T=r+m. The detector gives 1-O(epsilon)<=T<=3/2+O(epsilon). Markov applied to the maximalized J1 and the SAME product spike gives

    R <= 1+lambda(T-1)-delta T+O(epsilon+eta+tau A).

The maximum of this affine function on [1,3/2] is

    R_J(delta)=1-delta+(lambda-delta)_+/2.

The no-slot edge branches have exponent 1-delta and obey the same bound. Therefore J1 implies this uniform physical-row count, with all masks retained. Positivity of the summed squared modulus allows restriction to a zero bin without assuming cancellation between rows. It does not justify a stronger U^(1-sigma) moment on a bin.

Use this count for large delta and keep L's original compensated count for small delta. For c=2/9 and x=q/delta in [0,1/2], define

    A_x=2-4cx, D_x=3-x-4cx, P_x=A_x(1-x),
    J=(alpha-delta)D_x+delta P_x,
    R_c=1-delta+(alpha-delta)delta P_x/(2J).

The physical bin can use either detector bound, so R<=min(R_c,R_J) up to the same arbitrarily small losses. The two detectors may choose different dyads; the bound is on the original bin cardinality and does not require identical selected dyads for both estimates.

## 5. Exact full-domain certificate and continuation

Set

    B=218739/250000=.874956,
    ell=31283/187500=4(11/12-B),
    b=1542571/12500000,
    h=(1+b+3ell)/2,
    C0=-1/4+b/6+5ell/4,
    delta_0=191/500=.382.

The high-bin excess exponent is the unchanged source expression

    E(R)=C0+(1/2+ell)delta+ell x delta-h(1-R).

For 0<=delta<=delta_0 use R_c. With v=1/2-x, the rational polynomial Q=2J[-E(R_c)] has bidegree (2,3). `check_joint_witness.py` covers the full rectangle delta in [0,191/500], v in [0,1/2] by 32 times 16 closed cells and computes every tensor Bernstein coefficient exactly. All 6144 coefficients are positive, with minimum

    415930007/63281250000000.

Since 0<J<=5/2, the uniform reserve is

    -E(R_c)>=415930007/316406250000000 > 1.31e-6.

For delta>=delta_0, use R_J and the worst x=1/2. On delta_0<=delta<=lambda,

    E(R_J)<=C0+h lambda/2
                 +delta[1/2+3ell/2-3h/2].

Its slope is exactly -1/4-3(b+ell)/4<0; its value at delta_0 is less than -0.0006033. For delta>=lambda,

    E(R_J)<=C0-b delta/2,

also decreasing and continuous at lambda. This proves strict uniform negativity on every delta in [0,alpha], x in [0,1/2]. The checker also verifies the twenty retained low, intermediate, small-row, principal, Euler-domain and prime-supply gates. It checks B below the rationally isolated L boundary. These checks cover the continuous exponent domain, not merely its old critical point.

Conditional on J1 and the imported analytic framework, apply the previously reviewed low/Euler/continuation adapters of PR #910 and L, as recorded in `KAPPA_EXTENSION_CONDITIONAL.md`, Sections 4–5. They apply to these lengths because all their general gates pass. Retain the changed signal exponent

    C(s)=s-(4+b)/6.

Fix all dyadic, profile, arithmetic and finite internal orders first. The uniform reserve above permits epsilon and eta to be chosen small, then the auxiliary tau to absorb J1's finite height cost. Choose the external transform tail order last. Family-uniform exponents, with constants and eventual thresholds depending on the fixed target, then meet the original continuation criterion. Under these explicit hypotheses the finite-order Hecke and Dirichlet families have no zero in Re(s)>B, allowing the principal pole at one.

This is a priced conditional deduction, not a proof of J1, a new independently established zero-free theorem, or RH. Its new open analytic input is stronger than every mixed bound extracted here from the existing marginal estimates.

## 6. Why a truncated convolution has no coefficient-energy saving

The exact product, before row averaging, has convolution coefficient

    c(n)=sum_{lk=n} mu(l) W_M(q_l/D) W_S(q_k/N).

The common real power and height multiply this by a scalar depending only on q_n/(DN); they do not create cancellation between divisors of n. The global identity mu*1=1 applies to all divisors at all lengths. It does not apply to these separate annular blocks.

For a nondegenerate profile family with fixed positive lower bounds on interior subannuli, take distinct prime ideals p of norm asymptotic to D and q of norm asymptotic to N, with r>m>0. In n=pq, the only eligible inverse divisor is p: the other three divisors have wrong sizes. Thus |c(pq)| is bounded below. The prime-ideal theorem in any fixed admissible ray class yields

    sum_n |c(n)|^2 >= DN/[log D log N] * constant
                  = U^(r+m-o(1)).

At the frozen critical dyad r_c<t_c, the detector's extra inverse cutoff is identically one on a smaller interior support once U is large. Fixed nonzero ray weights and a common polynomial-size deleted radical leave sufficiently many primes: the radical removes O(log U) primes, while each positive-length annulus has a power-sized prime count. A profile that vanishes identically is of course excluded from this nondegenerate example.

The obstruction remains with actual disjoint prime slots. If their total log-length z satisfies z<r-m and each slot length is below m, take n=pq times one prime from each slot. Omitting p makes the inverse norm at most U^(m+z)<U^r, and attaching any slot prime to p makes it too large, leaving exactly the intended allocation in a fixed interior support. Therefore the unnormalized coefficient energy is at least U^(r+m+z-o(1)). At the old crossing both z_I and z_P satisfy these conditions: r-m-z_I=(5r-2t-1)/2>=2/37, and z_I<=7/37<m. Fixed disjoint supports prevent permutations of slots. The natural zeros and complete sixth-power product collisions must still be retained in any actual moment expansion.

This rules out a power-saving coefficient-norm proof based only on the formal mu*1 cancellation for the annular product. It is NOT a lower bound for the full character moment, and says nothing about the existence of a bad zero bin. Off-diagonal character correlations can still give J1. That arithmetic cancellation is the substantive remaining target.
