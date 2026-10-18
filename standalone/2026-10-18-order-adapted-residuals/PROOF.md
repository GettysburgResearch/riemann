# Order-adapted signed inverse residuals

Status: PROPOSED complete deductions from the pinned large-sieve and functional-equation inputs. Independent mathematical review is required. No RH, new zero-free half-plane, uncapped inverse-L moment, or critical native-Mobius moment is proved.

## 1. What changes relative to #986

During this investigation, #986 published the same M6/R2/R4 mixed-norm mechanism and the sextic residual second mean U^(11/15+epsilon). We credit that result and its all-fixed-order envelope, rather than claiming a second discovery. This note specializes that envelope at cutoffs adapted to the requested moment, proves a general character-order specialization, and gives an exact necessary-and-sufficient test for when the envelope can save a power.

The new principal numerical statements are FULL-family residual bounds at s=3/4+it:

- with A=U^(1/5), sum_a |L_a(s)M_A(s,a)-1|^4 << U^(4/5+epsilon);
- with A=U^(19/291), sum_a |L_a(s)M_A(s,a)-1|^6 << U^(175/194+epsilon).

There is no cap and no deleted exceptional set in these sums. The mollifier length changes with the order. These statements are not upgrades of a theorem for the SAME long mollifier A=U^(3/5): #986's displayed fourth-moment bound for that different observable has exponent 6/5. The first new statement reaches the exact minimum 4/5 of the stated envelope over ALL its legal cutoffs and integer Holder parameters. This minimum is a property of these upper estimates, not an arithmetic lower bound.

## 2. Exact family and definitions

Fix n>=3, a number field F containing mu_n, admissible finite S/ray/generator data for de Faveri's family, and one fixed finite-order S-supported Hecke twist psi. All family constants depend on these fixed choices. Rows a are n-th-power-free exterior integral IDEALS, ordered by FULL ideal norm Na<=U, U>=2. Neither radical nor conductor ordering is substituted. Characters retain their literal zero values at nonunits. Distinct ideals of equal norm remain distinct.

For 1/2<sigma<1, |t|<=T0 with T0 fixed, put s=sigma+it, d=2sigma-1, and

    L_a(s)=L_F^S(s,psi chi_a),
    M_A(s,a)=sum_(Nb<=A) mu_F(b) (psi chi_a)(b) (Nb)^(-s),
    E_A(s,a)=L_a(s)M_A(s,a)-1.

Choose FIXED 0<a<=x<=1 and A=U^a, X=U^x. Here a in an exponent is a real parameter, not the ideal row. Moment orders r,p below are fixed integers, independent of U. No constants uniform as r,n grow or sigma tends to 1/2 are claimed.

The imported sieve, with BOTH indices n-th-power-free, is

    sum_(Na<=U)^flat |sum_(Nb<=V)^flat z_b chi_a(b)|^2
      << (UV)^epsilon K_n(U,V) sum_b |z_b|^2,
    K_n(U,V)=U+V+U^(1-1/n)V^(2/n)+U^(2/n)V^(1-1/n).       (LS)

Define

    k_n(v)=max(1,v,1-1/n+2v/n,2/n+(1-1/n)v), v>=0.

The exact family, LS, and the complete functional-equation interface are the ones in #984/#986. The primary de Faveri text was inspected at the theorem context and both-index definition; the isolated theorem display was missing from the parser. LS is also explicitly pinned in both repository proofs. We do not claim a new proof of that deep input.

## 3. Reconstructing the bound we use

This section records the complete scope of the inherited envelope so that the specializations cannot silently strengthen it.

**Full columns.** In an ideal norm dyad V<Nb<=2V, common coefficients of size (Nb)^(-u) times a fixed-order divisor function have squared row norm

    << (UV)^epsilon V^(1-2u) K_n(U,V).                   (3.1)

Indeed b=c e^n uniquely, with c n-free and NO condition (c,e)=1. Complete multiplicativity including zeros gives chi_a(b)=chi_a(c)1_((a,e)=1). The fixed-e coefficient square mass costs (Ne)^(-n); Minkowski and sum_e (Ne)^(-n/2+epsilon)<infinity prove (3.1). The conjugate family and positive row subsets obey the same bound. Fixed psi is part of the common column coefficient.

**Mollifier.** Raising M_A to integer power j retains its complete ordered factorization coefficient and individual caps. Its product support is Nb<=A^j. Applying (3.1), divisor bounds, and dyadic Minkowski gives

    sum_all |M_A|^(2j) << U^(m_j+epsilon),
    m_j=max(1,k_n(ja)-dja).                              (3.2)

The 1 retains the unit term. Convexity of k_n(v)-dv makes the endpoint maximum over [0,ja] valid.

**Flat cutoff and dual.** Fix a smooth V equal to one on (0,1] and zero on [2,infinity), and define P_X=sum_b (psi chi_a)(b)(Nb)^(-s)V(Nb/X). For an inducing-NONPRINCIPAL row, the complete functional equation gives L_a=P_X+R_X. For a primitive character its exact dual is

    R_X=epsilon_a Q_a^(1/2-s)
          sum_c conjugate((psi chi_a)(c))(Nc)^(s-1)
                         V_s(Nc X/Q_a).                 (3.3)

Mellin inversion of V has only its simple pole at zero. Move its line left, take that residue, and apply the full Hecke functional equation on the left line. The dual weight is the resulting Mellin integral, not a sharply truncated series. It and each required fixed logarithmic derivative are bounded at small argument and rapidly decreasing at large argument. Moving a small distance right of zero retains the small-argument residue; no gamma pole is crossed before 1-sigma. Stirling on fixed t compacts supplies integrable Mellin tails.

Divide by ACTUAL conductor dyads Q<=C U, not Q comparable with U. Localized Fourier separation of the weight in log Nc and log Q gives common coefficient arrays. Root numbers stay outside the polynomial. For a dual-column dyad C, powering to j and applying (3.1) costs

    U^epsilon Q^(-jd) C^(jd) K_n(U,C^j)
                       min(1,(C X/Q)^(-J)),             (3.4)

with arbitrarily large fixed J. For Q/X>=1, Minkowski over ALL C, including the rapid tail, gives X^(-jd)K_n(U,(Q/X)^j). For Q/X<1 all C>=1 are in the tail; choosing J>jd plus the finite sieve powers gives at most U^(1+epsilon)X^(-jd). Thus, for NONPRINCIPAL rows,

    sum |R_X|^(2j) << U^(b_j+epsilon),
    b_j=k_n(j(1-x))-jdx.                                (3.5)

The fixed omitted S-Euler factors give finite polynomial factors and a dual S-supported sum with root weight (Nc_S)^(sigma-1), which converges. Its dilation only shortens the exterior dual length. This retains all original masks and all S-supported and archimedean tails. This is the same finite-S treatment as #984 Section 4 and #986 Section 3, not a principal or reciprocal contour shift.

Inducing-principal rows are NOT included in (3.5). There are only finitely many for the stated n-free, S-supported-twist family. Pay them at the end by |E_A|^(2r)<<1+A^(r(1-d)). A principal dual includes the pole at one, and can violate (3.5).

**Main signed error.** Because A<=X, the literal coefficients through A cancel:

    P_X M_A-1=sum_(A<Nb<=2AX) (psi chi_a)(b)(Nb)^(-s) h(b),
    h(b)=sum_(e|b,Ne<=A) mu_F(e)V(Nb/(Ne X)).             (3.6)

Every divisor is present when Nb<=A and V=1. The unit is subtracted. Beyond this exact cancellation we only use |h(b)|<=C d_2(b). Raising (3.6) to integer r has support A^r<Nb<=(2AX)^r and divisor majorant d_(2r). Consequently

    sum_all |P_X M_A-1|^(2r) << U^(g_r+epsilon),
    g_r=max(k_n(ra)-dra, k_n(r(a+x))-dr(a+x)).             (3.7)

All products and common factors remain. This is not a formal multiplication of two dual characters with the wrong conjugation.

Finally, for any integer p>=2, ordinary Holder interpolation gives

    sum_nonprincipal |M_A R_X|^(2r)
     <= (sum |M_A|^(2pr))^(1/p)
        (sum |R_X|^(2r))^((p-2)/p)
        (sum |R_X|^(4r))^(1/p).                          (3.8)

At p=2 the middle factor is omitted. No statistical independence is needed. Taking fractional powers of a Dirichlet polynomial and treating them as finite character polynomials would be invalid; (3.8) does not do that.

Combining (3.2), (3.5), (3.7), (3.8), and the principal bound proves the exact envelope of #986 Theorem C:

    sum_all |E_A|^(2r) << U^(G+epsilon),
    G=max(g_r, [m_(pr)+(p-2)b_r+b_(2r)]/p, 0, ra(1-d)).   (3.9)

Every epsilon loss is selected after all fixed parameters. This finishes the inherited analytic interface used below.

## 4. Power-saving fourth and sixth residual moments

At n=6, sigma=3/4, take r=2,p=5,a=1/5,x=1/2. Formula (3.9) has

    m_10=1, b_2=2/3, b_4=1,
    g_2=max(k_6(2/5)-1/5,k_6(7/5)-7/10)=4/5,
    [m_10+3b_2+b_4]/5=4/5,
    ra(1-d)=1/5.

Therefore

    sum_all |L_a(3/4+it)M_(U^(1/5))(3/4+it,a)-1|^4
                         << U^(4/5+epsilon).             (4.1)

The twentieth mollifier moment is bounded by U because its powered column length is U^2 and its coefficient weight pays that length. The dual fourth and eighth moments cost U^(2/3) and U. Their weighted product supplies the gain; no unproved inverse moment is used.

For a sixth residual moment use r=3,p=11,a=19/291,x=293/582. All cutoffs are legal, and exact substitution gives

    m_33=209/194, b_3=159/194, b_6=285/194,
    g_3=175/194,
    [m_33+9b_3+b_6]/11=175/194,
    ra(1-d)=19/194.

Thus

    sum_all |L_a(3/4+it)M_(U^(19/291))(3/4+it,a)-1|^6
                         << U^(175/194+epsilon).         (4.2)

The high moments are FIXED (including the 66th mollifier moment). No assertion uniform in their order is necessary or made. These are direct, explicitly credited corollaries of #986's envelope at different lengths, not a separately invented analytic mechanism or an optimum claim for (4.2).

**Exact optimality of (4.1) inside (3.9).** We prove G>=4/5 for every legal a,x and integer p>=2 at n=6,d=1/2,r=2. Always g_2>=1-a. If x>=1/2, its upper endpoint is at least 1/3+2(a+x)/3 >=2/3+2a/3. If x<=1/2, use

    m_(2p)>=max(1,pa), b_2>=2-8x/3, b_4>=4-6x.

The mixed term is at least

    2-8x/3+max(1/p,a)-2x/(3p).

For t>=0, max(t,a)-(2x/3)t >= a(1-2x/3) when 0<=x<=1/2 (check t<=a and t>=a separately). Therefore the mixed term is at least 2-8x/3+a(1-2x/3), which is at least 2/3+2a/3. In BOTH x ranges,

    G>=max(1-a,2/3+2a/3)>=4/5,

the last inequality following by weights 2/5 and 3/5. The parameters of (4.1) attain it. This rules out improving this FOURTH-RESIDUAL exponent merely by retuning (3.9), not by a new arithmetic estimate.

## 5. A general character-order specialization

For every FIXED n>=6 at sigma=3/4, put

    a_n=x_n=(2n-6)/(3n-8),
    theta_n=2(n^2-2n-2)/(n(3n-8)).

Then (3.9), with r=1,p=3, proves

    sum_all |L_a(3/4+it)M_(U^a_n)(3/4+it,a)-1|^2
                              << U^(theta_n+epsilon).   (5.1)

The n=6 case is precisely #986's 11/15 and is not claimed new. To verify every n, note 3/5<=a_n<2/3. The actual active branches give

    g_1=theta_n,
    k_n(3a_n)-3a_n/2=1-(n-2)/(n(3n-8)), so m_3=1,
    b_1=1-a_n/2,
    b_2=1+3/n-a_n(1+4/n),
    (1+b_1+b_2)/3=theta_n-2(n-6)/(3n(3n-8)).

The principal cost a_n/2 is smaller. These rational identities and branch inequalities establish (5.1) for all fixed n>=6, not just a tested finite list.

The main-error estimate itself has this exact floor. Write

    l=1-1/n+(2/n-1/2)a,
    u=2/n+(1/2-1/n)(a+x),
    w=(2n-4)/(3n-8).

Both are lower bounds for the respective endpoint expressions in g_1, and

    w*l+(1-w)*u
       =theta_n+[(n-4)(n-2)/(2n(3n-8))]*(x-a)>=theta_n.

Our cutoffs attain that floor while paying the complete dual. The formal limit theta_n->2/3 changes the root-of-unity field and character order. It is NOT a zero-free boundary or an RH limit for one fixed target.

## 6. Exact line threshold of the fixed-order envelope

An all-fixed-order formula must not be mistaken for an all-order critical theorem. This section gives a precise test for the currently available envelope.

For fixed n>=3 and integer r>=1, there exist legal fixed a,x,p making (3.9) strictly less than one if and only if

    sigma > sigma_(n,r):=1/2+[k_n(r/2)-1]/r.             (6.1)

For example,

    r=1: sigma_(n,1)=1/2;
    r=2: sigma_(n,2)=1/2+1/(2n);
    r=3: sigma_(n,3)=2/3+1/(6n);
    r>=4: sigma_(n,r)=1-1/r.

These are thresholds of (3.9), NOT necessary conditions for the actual residuals or for RH.

**Necessity.** Let v0=r/2, d_*= [k_n(v0)-1]/v0, and suppose d<=d_*. Convexity gives 1+k_n(2v)>=2k_n(v). Hence m_(pr)>=1 implies the mixed term in (3.9) is at least b_r. If x<=1/2, b_r>=k_n(v0)-dv0>=1. If x>=1/2, put v=r(a+x)>=v0. The convex secant inequality k_n(v)>=k_n(v0)+d_*(v-v0) gives k_n(v)-dv>=1. This is one of the terms of g_r. Thus G>=1 for every choice.

**Sufficiency.** Suppose d>d_* and fix x=1/2. Let B=k_n(v0)-dv0<1 and C=k_n(r)-dr. Convexity gives T=1+C-2B>=0. Choose a fixed integer p>=2 with T/p<1-B. Next choose a>0 sufficiently small that pra<=1/2, a<=x, and k_n(r(a+x))-dr(a+x)<1; continuity permits this since its value at a=0 is B. Then m_(pr)=1, the mixed term is B+T/p<1, and the lower main term is 1-dra<1. Decrease a further so ra(1-d)<1. Thus G<1. Every choice is made before U tends to infinity. This proves (6.1).

At n=6 these boundaries are 1/2,7/12,25/36,3/4,4/5,... . In particular the existing envelope cannot supply a power-saving eighth residual moment at sigma=3/4. This is why (4.1)-(4.2) cannot be iterated into an RH assertion.

## 7. What the estimates actually exclude

At an actual zero of L_a(s), E_A(s,a)=-1. Every estimate above has a POSITIVE power of U on its right. It permits a fixed bad row, and many exceptional rows. None implies nonvanishing of a prescribed member. Markov does give, from (4.1),

    #{a: |E_(U^(1/5))(3/4+it,a)|>T}
                      << U^(4/5+epsilon) T^(-4), T>0.

This is a full-residual large-value count for that mollifier, not an optimized zero density. On |E_A|<=q<1, L_a and M_A are nonzero and

    |L_a^(-1)-M_A|/|L_a^(-1)|=|E_A|<=q.

The complementary inverses remain uncontrolled. No cap or exception can be silently removed from #984's negative-moment law by citing this formula.

The user asks for RH. This pass did not establish the missing principal-member estimate or a cofinal ferromagnetic realization. Its additions are order-adapted full residual estimates and exact boundaries of their method. They do not promote any prior QRH or finite Lee--Yang certificate into RH.
