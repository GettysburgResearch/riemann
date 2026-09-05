# Route 3, pass 2: a noncompact Hardy model with complete finite-witness capture

Status: PROPOSED THEOREMS, complete proofs supplied; independent review required.
Scope: the full Riemann zero divisor with multiplicities, a source-defined trace-class self-adjoint operator, exact Cauchy/Blaschke screening, and quantitative finite-height plus finite-time capture. No positivity theorem or RH proof is claimed.
Parent: PR #793 at 7275b956b278051504da4befeb3b37924f83fd58. Its compact-band Hilbert surplus and screening counterexamples remain valid and unchanged.
Smallest open step: prove positivity of the specific gamma-plus-prime-source operator below. Cofinal capture is no longer a separate assumption for THIS new noncompact model.

This is a change of test metric, not a free improvement of the compact-support pair-correlation theorem. Standard Hardy/Blaschke and Weil/Suzuki mechanisms are credited. No new external priority or pair-correlation input is asserted.

## C1. Definitions, all zeros, and trace-class convergence

Let Z be the distinct zeros of Xi(z)=xi(1/2+iz), with multiplicities m_z. Write z=gamma+i y. Unconditionally |y|<h=1/2, Z is invariant under z->bar z and z->-z, and

    N_*(T):=sum_(z: |Re z|<=T)m_z <= C_0 T log(eT),  T>=T_0,

for some constants C_0>0,T_0>=1. Only this coarse classical zero-count upper bound is needed; no RH, zero simplicity, spacing, or finite verification is imported.

Fix a>h and b>h, once and for all. On L2(0,infty), with inner product linear in the second entry, define

    h_z(t)=sqrt(2a) exp(-a t+i z t)/(b-i z),
    T_(a,b)=sum_(z in Z) m_z |h_z><h_(bar z)|.

The series converges in trace norm. Indeed

    ||h_z||^2 = a/[(a+y)((b+y)^2+gamma^2)],
    ||h_z|| ||h_(bar z)||
      = a/[sqrt(a^2-y^2)
           sqrt(((b+y)^2+gamma^2)((b-y)^2+gamma^2))]
      <= c_a/gamma^2  (gamma!=0),
    c_a=a/sqrt(a^2-h^2).

The finitely many low zeros cause no problem since a,b>h. For T>=T_0,

    S_2(T):=sum_(|gamma|>T)m_z/gamma^2
       <= 2 C_0(log T+2)/T,
    ||T_(a,b)-T_(a,b;T)||_1 <= R(T):=c_a S_2(T).

Here T_(a,b;T) retains every zero with |gamma|<=T. The S_2 bound follows from Stieltjes integration by parts and N_*. Conjugation pairs the summands with their adjoints, so the limit is self-adjoint. Multiple zeros appear only as positive scalar weights, not as duplicate independent vectors.

## C2. The operator has an independent safe arithmetic source

Define the continuous even real function

    W_b(x)=sum_z m_z exp(i z x)/(b^2+z^2).

The sum is absolutely locally uniformly convergent. The integral kernel of T_(a,b) is

    2a exp(-a(t+u)) W_b(t-u).

Although the zero sum is useful for analysis, W_b can instead be specified from safe arithmetic data. Put

    L(r)=xi'/xi(1/2+r),   r>1/2.

The even canonical product for Xi gives sum_z m_z/(r^2+z^2)=L(r)/r, and therefore, for r>1/2, r!=b,

    integral_0^infty exp(-r x) W_b(x)dx
       = [L(r)-(r/b)L(b)]/(b^2-r^2).                 (C2)

The apparent singularity at r=b is removable. To check the constants, average exp(izx) with exp(-izx), integrate to r/(r^2+z^2), and use partial fractions. The sum is over BOTH signs of the zeros; inserting an extra factor two would be wrong.

Every L(r) on this safe real axis has the prime-defined expression

    L(r)=1/(r+1/2)+1/(r-1/2)-(log pi)/2
          +(1/2) digamma((r+1/2)/2)
          -sum_(n>=2) Lambda(n)n^(-r-1/2).

The prime series converges absolutely. The convergent series gives |W_b(x)|<=C_b exp(h|x|). Formula (C2), evenness, and uniqueness of the Laplace transform in this continuous exponential-growth class specify W_b without choosing a desired zero set or inner product. Existence follows from the usual unconditional xi theory and the convergent zero representation just proved. This is a source-defined resolvent coordinate in the classical Weil/Suzuki setting, not a claim of a new positivity mechanism.

## C3. Exact finite Cauchy screening

For each zero let p_z=a+i bar z in the open right half-plane and s_z=1/(b-i z). Then h_z=s_z sqrt(2a) exp(-bar(p_z)t). The Gram entry is

    <h_z,h_w> = conjugate(s_z)s_w 2a/(p_z+conjugate(p_w)).

Choose a hypothetical nonreal pair z_+=gamma+i y, z_-=bar(z_+), y>0, of common multiplicity m. Let S be any finite set of other DISTINCT zero locations, and P_S the orthogonal projection off the span of their h_z. Define the finite Blaschke product

    B_S(p)=product_(z in S) (p-p_z)/(p+conjugate(p_z)).

Multiplying factors by unimodular constants does not affect the following formula. For i,j in {+,-}, the residual Gram is exactly

    G_S(i,j)=<P_S h_(z_i),P_S h_(z_j)>
       =conjugate(s_(z_i))s_(z_j)
          2a B_S(p_(z_i))conjugate(B_S(p_(z_j)))
            /(p_(z_i)+conjugate(p_(z_j))).           (C3)

### Proof

Under the Laplace isometry L2(0,infty)->H2(Re p>0), exp(-bar p t) is the reproducing kernel k_p. Vanishing at the points p_z is the closed subspace B_S H2. Multiplication by B_S is isometric, and projection of k_p onto B_S H2 is conjugate(B_S(p)) B_S k_p. Taking inner products yields C3. Alternatively, the same finite identity follows by the Cauchy determinant/Schur-complement formula; the checker reconstructs it in that independent way. QED.

In particular,

    det G_S = |s_+ s_- B_S(p_+)B_S(p_-)|^2
                         y^2/(a^2-y^2) >0.         (C4)

Neither equal ordinates nor arbitrarily close distinct neighbors break the strict inequality. They can make its value small; no uniform spacing bound is claimed.

## C4. The full infinite background does not erase this pair

Let S grow through all other distinct zero locations. Since Re p_z is between a-h and a+h and N_*(T)=O(T log T),

    sum_z Re p_z/(1+|p_z|^2)<infty.

Thus the normalized products define a Blaschke product B_infty, nonzero at both omitted target points. Projection onto the orthogonal complement of the closed background span has residual Gram G_infty given by C3 with B_infty. In particular det G_infty>0.

For completeness, the scalar tail modulus can be bounded without a spacing assumption. For a fixed target p, write

    |(p-p_z)/(p+bar p_z)|^2=1-x_z,
    x_z=4 Re p Re p_z/|p+bar p_z|^2.

If T>=2|Im p| and T^2>=32 Re p(a+h), then for |Re z|>T,

    0<=x_z<=16 Re p(a+h)/(Re z)^2<=1/2,
    -log|B_(tail,T)(p)|^2
       <=32 Re p(a+h) S_2(T).

The remote zero tail changes the fixed target product by at most an explicit O(log T/T) logarithmic amount. Nearby zeros still enter through their exact finite product. This proves survival for each fixed target, NOT a lower bound uniform over all possible target locations and configurations.

## C5. An explicit negative witness, without eigensolvers

Let S_T contain all other distinct zeros with |gamma|<=T, with T large enough to contain the target pair. Write G_T=G_(S_T), v=(1,-1)^t, and let V_T have columns P_(S_T)h_+, P_(S_T)h_-. Put

    q_T=V_T G_T^(-1)v,
    d_T=2m/(v^*G_T^(-1)v)>0.

Every background summand of T_(a,b;T) vanishes on q_T. The two target evaluations are +1 and -1, so

    <q_T,T_(a,b;T) q_T> = -2m,
    ||q_T||^2=v^*G_T^(-1)v.

Hence its exact Rayleigh quotient is -d_T. C4 gives G_T->G_infty>0 and therefore d_T->d_infty>0. Since R(T)->0, eventually

    R(T)<d_T,

and the same finite-combination vector has a strictly negative quadratic value for the FULL operator. The threshold depends on the target and the finite product; it is not asserted uniform or computable without the corresponding data.

This closes finite-height capture for the new operator. It is not a new zero-free theorem.

## C6. Finite-time capture and the leakage budget

Let P_L be multiplication by 1_[0,L]. Directly from each rank-one summand,

    ||T_(a,b)-P_L T_(a,b)P_L||_1
       <=2 M exp(-(a-h)L),
    M=sum_z m_z ||h_z|| ||h_(bar z)||<infty.

Indeed the discarded tail of h_z has norm exp(-(a+y)L)||h_z||, and the two rank-one differences are bounded by the sum of the two tail factors.

The total M can be bounded by the finite sum M_T plus R(T). Consequently the finite conditions

    G_T>0,
    R(T)+2(M_T+R(T))exp(-(a-h)L)<d_T              (C6)

guarantee that P_L q_T is a compactly supported negative test vector for the full arithmetic kernel. To see this, compare the quadratic form of P_L T P_L on q_T with that of T_T; the operator-norm error is at most the left side of the second inequality. A negative value also proves P_L q_T is nonzero.

Every hypothetical off-line pair admits some finite T,L satisfying C6. This is a complete finite-height AND finite-time capture theorem at the stated source, with all omitted-zero and time-tail terms present.

There is no contradiction with the pass-1 compact-band screening theorem. Projection off an infinite real background in a fixed compact interval may annihilate the raw horizontal residual. Here one annihilates only a finite background, controls the remaining weighted operator tail, and then pays time truncation. Approximate cancellation with a strict budget is not exact projection off an infinite span. The logarithmic-density zero tail and the rational resolvent weights are essential.

## C7. Exact positivity endpoint, and what has not been proved

For these fixed a,b>1/2,

    T_(a,b)>=0  iff RH.

Under RH every z is real, h_(bar z)=h_z, and the trace-norm sum consists of positive rank-one operators. Conversely C5 or C6 gives a negative direction from any nonreal zero. Repeated real zeros remain harmless positive weights.

This equivalence is in the established Weil/Hardy positivity family. The contributions of this pass are the explicitly source-normalized trace-class model, the exact conditioned pair Gram, its cofinal survival, and the finite error budget C6. Positivity of T_(a,b) has NOT been proved. No compact-support BGST/Lamzouri estimate is imported into this noncompact metric without a new adapter.

The next arithmetic task can now be stated without an unspecified frame or capture hypothesis: prove nonnegativity of

    integral_0^infty integral_0^infty
       conjugate(f(t)) 2a exp(-a(t+u)) W_b(t-u) f(u) du dt

for every compactly supported L2 test f, using the exact gamma-plus-prime source C2. Every off-line zero would be caught by one such finite test, including an isolated finite exception.
