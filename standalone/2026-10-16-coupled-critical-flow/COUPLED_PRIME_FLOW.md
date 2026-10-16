# The coupled arithmetic source has an exact two-channel positive-compensation flow

**Status:** proposed component proofs. The terminal signed inequality in Section 5 is OPEN; no RH or native moment theorem is asserted. The calculation implements an arithmetic and Gaussian-source adapter, not a newly proved theta transformation or an extension of the upstream moment estimate to arbitrary coefficients.

**Sources:** the coupled degree-6 coefficient from #948 and #949; the classical Mammen law and Peano identity as used in #946, `c90818b3a671bb3d124019f3be93a439697deab1`, MATHEMATICS.md Sections 1--6. The latter identity and its positivity are credited. What is supplied here is its exact application to the non-squarefree weighted 0/1/m source, the two shortened scales with a common remaining cofactor, a uniform-in-m reference bound, and a convergent infinite-prime realization for the actual Gaussian detector.

## 1. Prime occupancy, not the exponent of a prime

Use the notation of CRITICAL_FACTOR_AND_GAUSSIAN.md. Fix a nonnegative finite row measure w(u), of mass Z_w. For each row, the allowed local coefficients are

    1,  -(1-1/q)a_p(u) at p,  -b_p(u)q^(m/2-1) at p^m.   (1)

All other positive prime exponents have coefficient zero. Both a_p and b_p are zero at an excluded/nonunit prime. For the standard character family a_p(u)=xi_u(p), b_p(u)=eta_p xi_u(p)^m. Equal-norm conjugate prime ideals remain different coordinates.

Take either a fixed bounded compact test W on (0,infinity), or the exact Gaussian w_(5/6) from the companion note. For D>=3 freeze all primes of norm <=y=(log D)^2 at multiplier 1, and assign each remaining prime an independent real multiplier Z_p with the Mammen law below. Define

    P_m(D,u;Z)=sum_n c_m,u(n) W(Nn/D)
                    product_(p|n,Np>y) Z_p.              (2)

A prime occurring to exponent m contributes ONE Z_p, not Z_p^m. This is the key adapter. The two occupied local coefficients in (1) use the same multiplier. Restoring Z_p=1 everywhere recovers the exact coupled source B_m, not a changed squarefree phase family.

It would be wrong to give the two branches independent random variables. It would also be wrong to use Z_p^m for the powerful branch and then apply a multilinear singleton identity. Both substitutions change the reference and the compensation.

For compact W only finitely many coordinates occur. For the Gaussian, (2) is absolutely convergent for every multiplier realization: |Z_p|<2, |c_m,u(n)|<=(Nn)^(1/2), and 2^omega(n)<=Nn. The resulting deterministic coefficient majorant is (Nn)^(3/2), while the Gaussian decays faster than every power at infinity. The bound is uniform in the row and in which coordinates have already been restored.

## 2. The classical local identity, with its actual sign

Put phi=(1+sqrt(5))/2. The Mammen law assigns phi probability (1-1/sqrt(5))/2 and 1-phi probability (1+1/sqrt(5))/2. Its moments satisfy

    m_0=1, m_1=0, m_2=m_3=1, m_4=2,
    m_j=m_(j-1)+m_(j-2),   0<=m_j<=phi^j for j>=2.         (3)

For U,V in C and k>=2 define

    R_k(U,V)=E|U+ZV|^(2k)-|U+V|^(2k)
                      +2k|U|^(2k-2)Re(U conjugate(V)).   (4)

The #946 Peano calculation gives

    R_k(U,V)>=c_k |V|^(2k)>=0,
    c_k=((2k)(2k-1)(2k-2)(2k-3)/24)(8/75)^(k-2).          (5)

Here is the relevant proof, to keep the interface auditable. The linear functional E g(Z)-g(1)+g'(0) annihilates degrees <=3 and equals integral K(t)g''''(t)dt, where a=1-phi, b=phi, p=P(Z=b), q=P(Z=a), and

    6K(t)=p(b-t)_+^3+q(a-t)_+^3-(1-t)_+^3+3(-t)_+^2.

It is nonnegative: on [a,0] it equals q(t-a)^3; on [0,1] it equals p(b-t)^3-(1-t)^3>=0, using pb^3>1; on [1,b] it equals p(b-t)^3. Its moments are integral K=1/24, integral tK=1/60, integral t^2K=1/90. Thus 24K(t)dt has variance 8/75. For V!=0, writing U/V=x+iy, the fourth derivative of |V|^(2k)((x+t)^2+y^2)^k is nonnegative and is at least (2k)_4 |V|^(2k)(x+t)^(2k-4). Jensen under 24K gives (5). V=0 is immediate. This is the prior local argument, not a new positivity principle for an arithmetic remainder.

At order four it gives the exact identity

    |U+V|^4=E|U+ZV|^4+4|U|^2 Re(U conjugate(V))-|V|^4.    (6)

The injection in (6) is signed. Neither the individual step nor the full native singleton covariance is asserted positive or negative.

## 3. The positive starting reference is bounded for every fixed order

Let

    G_(k,m)(D,w)=sum_u w(u) E|P_m(D,u;Z)|^(2k).            (7)

### Theorem 5

For every fixed k>=1 and epsilon>0,

    G_(k,m)(D,w) <= C_(F,k,W,epsilon) Z_w D^(k+epsilon),    (8)

uniformly in m>=2, phases, masks, exclusions, and the row measure. This applies to both tests specified in Section 1, including the full Gaussian.

For the fixed Gaussian, or a fixed normalized compact test, there is also C_(F,W), independent of m,k,D and the row, such that for sufficiently large D and all 1<=k<=log D,

    (E|P_m(D,u;Z)|^(2k))^(1/(2k))
      <= D^[1/2+log log log D/(2 log log D)+C_(F,W)/log log D]. (9)

These are reference bounds, not bounds for B_m(D,u)=P_m(D,u;1).

**Proof.** Expand a finite ideal truncation first. If p occupies j of the 2k slots, its expectation is m_j. The exponents within those occupied slots can be 1 or m. All m_j are nonnegative, so after taking coefficient absolute values a local norm majorant at sigma=1/2+delta is built from

    r_p=(1-1/q)q^(-sigma)+q^(m/2-1-m sigma)
         <=2q^(-sigma),                                 (10)

since 1+m delta>=1/2+delta. The test satisfies |W(t)|<=C_(W,sigma)t^(-sigma) for all t>0. For sigma in a fixed compact interval containing 1/2 the constants can be chosen bounded; this includes the Gaussian.

The complete positive Euler bound is therefore

    E|P_m|^(2k) <= C_(W,sigma)^(2k) D^(2k sigma)
          product_(q<=y)(1+r_p)^(2k)
          product_(q>y) sum_(j=0)^(2k) binom(2k,j)m_j r_p^j. (11)

The rough factors have no linear term and are 1+O_k(q^(-2sigma)), uniformly in m. Their product converges for every fixed sigma>1/2. The frozen-prime logarithm is at most C_k sum_(q<=y)q^(-sigma)=o(log D) at y=(log D)^2. The fixed-field prime-ideal count, or even its coarser comparison with integers, suffices. Taking 2k delta smaller than epsilon proves (8).

For the uniform statement put L=log D, v=log L, delta=log(v)/(2v). For k<=L and q>L^2, 2k phi r_p<=4phi/v<=1 once v is sufficiently large. Then the logarithm of each rough factor is at most C k^2 q^(-2sigma), by the exponential-series estimate and (3). Chebyshev's prime bound, with at most [F:Q] primes above each rational prime, and partial summation give

    sum_(q<=L^2)q^(-1/2)<=C_F L/v,
    sum_(q>L^2)q^(-1-2delta)<=C_F/(v log v).

The latter also follows by enlarging primes to ideals and using I_F(t)<=A_F t. Hence the logarithm of (11) is at most

    kL+2k delta L+C_F kL/v+C_F k^2/(v log v)+O_W(k).

Divide by 2k and use k<=L to prove (9).

For the Gaussian, the finite truncations converge in every L^(2k) by the deterministic absolute majorant in Section 1. Fatou, or dominated convergence, transfers (11) to the full sum. No compact substitute, row truncation, or unproved same-height test adapter is used. Summation over the nonnegative row weights proves (8). QED.

## 4. Exact restoration and the two shortened scales

Fix any ordering of the finitely many active primes for a compact test. For the Gaussian use any enumeration of all active prime ideals, for example increasing norm with a fixed tie-break. At step j all previous multipliers are 1 and all later multipliers retain their law. Let B_m^(p) denote the remaining source with p completely excluded, with exactly that remaining multiplier configuration. Splitting on occupancy at p gives

    P=U_(j,u)+Z_p V_(j,u),
    U_(j,u)=B_m^(p)(D,u),
    V_(j,u)=V_(j,u)^1+V_(j,u)^m,
    V_(j,u)^1=-(1-1/q)a_p(u) B_m^(p)(D/q,u),
    V_(j,u)^m=-b_p(u)q^(m/2-1) B_m^(p)(D/q^m,u).           (12)

This follows directly from (1), with no theta input. The two branches use the SAME cofactor function at different scales and the SAME physical row. Both require p not to divide the cofactor. That exclusion is correct for the occupied-prime expansion (1); it is distinct from the unrestricted convolution in the companion note.

In the ordinary sextic family the second branch is

    -eta_p q^2 xi_u(p)^6 B_6^(p)(D/q^6,u).                 (13)

If p divides u, both branches vanish, including the neutral sixth-power branch. Replacing xi_u(p)^6 by one on all rows is invalid.

Define, with conditional expectation over the later coordinates,

    I_(k,m)=2k sum_j sum_u w(u)
                  E[|U_j|^(2k-2)Re(U_j conjugate(V_j))],
    D_(k,m)=sum_j sum_u w(u) E R_k(U_j,V_j).               (14)

### Theorem 6

For the actual coupled moment,

    M_(2k,m)(D,w)=G_(k,m)(D,w)+I_(k,m)(D,w)-D_(k,m)(D,w), (15)
    D_(k,m)>=c_k sum_(j,u) w(u) E|V_j|^(2k)>=0.            (16)

At k=2,

    D_(2,m)=sum_(j,u)w(u) E|V_j^1+V_j^m|^4.              (17)

The cross terms INSIDE (17) must remain. In general (17) is neither the sum of the separate channel energies nor the compensation for two independent multipliers.

**Proof.** For each conditional multilinear polynomial apply (4) and telescope its change when Z_p is restored to 1. This proves (15)--(17) immediately for a compact test.

For the Gaussian, the same argument has no unproved infinite-prime exchange. Put

    M_0(D)=sum_n (Nn)^(3/2)|W(Nn/D)|,
    M_1(D)=sum_n omega(n)(Nn)^(3/2)|W(Nn/D)|.

Both are finite. Uniformly in all configurations, |U_j|<=M_0 and |V_j|<=M_p, where sum_p M_p<=M_1. Each injection is bounded by 2k M_0^(2k-1)M_p. Since R_k is a fixed polynomial in U,V and their conjugates and vanishes at V=0, it is bounded in absolute value by C_k M_0^(2k-1)M_p on this domain. Thus the sums in (14) converge absolutely, even after the row sum of finite mass. Finite restorations converge to B_m(D,u) by coefficientwise stabilization and deterministic domination by M_0. Passing to the limit in the telescoping identity proves the full Gaussian statement. These convergence estimates are deliberately crude; they establish existence, not the critical arithmetic bound. QED.

## 5. One exact remaining inequality, including a scalar full-proof target

The reference (8) is already diagonal-sized. The missing all-row assertion is

    I_(k,m)-D_(k,m) <= C_epsilon Z_w D^(k+e_k+epsilon).     (OPEN-C)

At m=6 the exact coefficients and scales are (12)--(13), not an arbitrary bounded array. Supplying (OPEN-C) at all required shorter scales with the SAME row measure permits the companion critical comparison to return to native moments. The predecessor field/extraction hypotheses, if used, retain their own test, twist and height quantifiers.

There is a smaller direct scalar target for the Dedekind detector. Take a single principal row of weight one, the actual theta b-profile, m=6, the exact Gaussian, and k=2. Then

    I_(2,6)(D)-D_(2,6)(D) <= C_epsilon D^(2+epsilon)        (OPEN-S)

for every epsilon>0 would give |B_(6,1)(D)|<=C_epsilon D^(1/2+epsilon). By the exact Mellin identification in the companion note, this would exclude all zeros of the target Dedekind zeta function in Re(s)>1/2 and allow the stated abelian descent. This is a sufficient full-proof route at the scalar source, without a replica-density or row-height loss. It is not a proof of (OPEN-S).

Conversely, the same scalar critical bound implies the upper bound (OPEN-S), since I-D=M_4-G<=M_4. Thus the new flow makes the missing estimate explicit; it does not weaken it into an automatically true positivity statement.

## 6. The direct bound attempted here and why it does not close

For a finite collection of steps, Holder gives at order four

    |I_(2,m)| <= 4 (sum_(j,u) w E|U_j|^4)^(3/4)
                         (sum_(j,u) w E|V_j|^4)^(1/4).    (18)

The second factor is the proved compensation energy. Young's inequality then bounds I-D by a constant times the first, UNKNOWN quantity. It is not bounded by the initial G: U_j already contains restored prime coordinates, and repeated steps also enlarge this sum. In an infinite Gaussian flow the unweighted sum of U_j energies need not even be finite, while the original weighted injection does converge. Thus (18) is only a finite-cutoff diagnostic, not an accepted estimate at the endpoint.

Likewise, applying the upstream Hecke/theta moment theorem separately to the Mammen-deformed intermediate coefficients is unjustified. The multipliers are not unitary Hecke character values and alter the prime coefficient. The rigidity and freezing obstructions from #941/#943 still apply to such a shortcut.

The arithmetic question now has a precise coupled form: bound the TOTAL signed injection using the full compensation (17), while keeping both prime and sixth-power cofactor scales. The direct Cauchy/Holder/Young attack in (18) has not bounded it. No full native moment or new zero-free exponent is promoted.
