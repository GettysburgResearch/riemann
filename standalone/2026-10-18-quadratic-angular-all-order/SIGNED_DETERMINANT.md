# The exact signs in higher native moments, and the determinant obstruction

**Scope:** identities for the ORIGINAL ideal Mobius columns, with every separate cutoff retained. These equations are not estimates for Liouville polynomial correlations. A statement that such correlations cancel at RH strength would be an unproved leap.

## 1. Exact sign factorization at EVERY moment order

Fix K imaginary quadratic, Q rationally saturated and containing all ramified rational primes, and define the native hard column

    A_l(X)=sum_(X/2<NI<=X) mu_K^S(I) Psi(I)^l .

For each integer k>=1 expand A_l(X)^k in the basis Psi(I)^l. Let

    c_(k,X)(I)= # {(I_1,...,I_k):
        I_1*...*I_k=I,
        X/2<NI_j<=X, I_j squarefree and prime to S for every j}.

These are NONNEGATIVE INTEGER counts, with all repeated primes across different columns and all separately capped factors retained. Write lambda_K(I)=(-1)^Omega_K(I), Omega_K counting prime ideals with multiplicities. Since mu_K(I_j)=(-1)^Omega_K(I_j) on each squarefree contributing column, EVERY admissible tuple has the SAME sign:

    [Psi(I)^l] A_l(X)^k = lambda_K(I) c_(k,X)(I).       (1)

This is an exact multiplicative-sign identity, not a heuristic. It includes I which is not squarefree, and it remains true if each column receives the same multiplicative norm twist (NI_j)^(it), after factoring (NI)^(it) from the coefficient. It is NOT the corresponding factorization for arbitrary polynomial phases P(NI_j), since products of those phases need not depend only on NI.

Every I has unique rational content I=(a)J, J rational-primitive. If c_(k,X)((a)J)!=0, all primes of I avoid S. Therefore (a,Q)=1, J avoids S, and

    lambda_K((a))=chi_(d_K)(a),     lambda_K((a)J)=chi_(d_K)(a)lambda_K(J).   (2)

At unramified split p, (p) is a product of TWO prime ideals, contributing (+1), and chi(p)=+1. At inert p, (p) is ONE prime ideal, contributing (-1), and chi(p)=-1. The identity remains true for ALL exponents of a; lambda((p)^e)=chi(p)^e.

Collect the angular rays:

    A_l(X)^k = sum_(J primitive) B_(k,X)(J) Psi(J)^l ,
    B_(k,X)(J)=lambda_K(J)
             sum_(a<=sqrt(X^k/NJ), (a,Q)=1)
                 chi_(d_K)(a) c_(k,X)((a)J).              (3)

All squarefree restrictions belong INSIDE c_(k,X), not in the sum over a. In particular, for k>=2 it is generally FALSE to impose (a,NJ)=1 in (3): a prime can appear in J and (a), provided its occurrences are distributed between different squarefree columns. This is a genuine distinction from the order-two (k=1) periodic ray sum of #972.

For a radial parameter t the right side gains only (NI)^(it) inside the summation, or equivalently a^(2it)(NJ)^(it); the exact signs in (2) are unchanged.

## 2. Exact angular Gram decomposition

Let phi_J=arg Psi(J). For K=Q(sqrt(-3)), class number is one and distinct rational-primitive rays have distinct phi modulo 2pi. The exact Gaussian average is

    M_(k,R)(X;l0) =
      sum_l p_R(l-l0)|A_l(X)|^(2k)
      = sum_J |B_J|^2
        + sum_(J!=J') B_J conjugate(B_J')
              exp(i*l0*(phi_J-phi_J')) Theta_R(phi_J-phi_J'). (4)

Here Theta_R is the centered-free, positive real wrapped-Gaussian kernel. Inserting (3), each off-diagonal pair is a sum of weights with literal signs
chi(a)chi(b)lambda_K(J)lambda_K(J'). The Schur estimate in PROOF.md takes absolute values of those pairs. That is precisely where the potential fixed-principal gain disappears.

For general K there are h_K ideal classes, and (4) still holds algebraically, but distinct rays in different classes are not assumed to have distinct phase. The proof instead takes classwise Gram blocks and bounds their cross-class sum by Cauchy; the distinction is explicit.

## 3. Eisenstein determinant coordinates and a polynomial Liouville sign

Specialize to K=Q(omega), omega=(-1+sqrt(-3))/2, with 3|Q. A primitive integral ideal J prime to S is principal J=(alpha) and supported only on split prime ideals, not inert or ramified ideals. Consequently

    lambda_K(J)=lambda_Z(NJ) .                             (5)

For two such ideals J=(alpha), J'=(beta), write

    gamma=alpha*conjugate(beta)=(T+h*sqrt(-3))/2,
    T,h integers of the same parity.

The ordinary trace and determinant coordinates satisfy

    T^2+3h^2=4 (NJ)(NJ') .                                 (6)

Since lambda_Z(4)=+1 and Liouville is completely multiplicative, (5)-(6) imply the EXACT sign identity

    lambda_K(J)lambda_K(J')
         =lambda_Z(T^2+3h^2).                              (7)

There is no appeal to a conjecture about primes represented by quadratic forms here; (7) is just the norm identity. For positive determinant h!=0 the angular distance is controlled by the same h, which is the geometric input to the Gaussian. Thus the signed cross terms of (4) can be reorganized by the determinant h and trace T with the arithmetic sign lambda(T^2+3h^2), multiplied by the nonnegative decomposition-count weights and the radial chi(a)chi(b) factors. Those weights CANNOT be dropped without changing the original source.

The polynomial-phase uniformity of PROOF.md is an ABSOLUTE coefficient estimate, so it does not control lambda(T^2+3h^2). Nor does the squarefree partial-sum identity of #972 automatically bound (3) for k>=2, because c_(k,X)((a)J) varies with a. Claiming otherwise would turn a weighted Liouville problem into a solved polynomial exponential-sum problem incorrectly.

A legitimate further attack must control the exact signed Gram remainder in (4), including the count weights, all rational contents, and full Gaussian tails, in a way that retains the fixed l=0 row.

## 4. The angular resolution barrier is sharp in power

For the Eisenstein field, fix k>=1 and choose 0<delta<1/2 such that (1-delta)^k>1/4. Dirichlet's prime number theorem in progression 1 mod 3 supplies asymptotically c_delta X/log X split rational primes p in ((1-delta)X,X]. Choose ONE prime ideal over each p, always using a fixed orientation convention.

Take any k distinct chosen primes and their ideal product J. It is rational-primitive, with

    X^k/4 < NJ <= X^k.

It contributes exactly k! ordered tuples to c_(k,X)(J) (one prime ideal per column); no factor (a) with a>=2 is possible in its ray while keeping product norm <=X^k, since 4 NJ>X^k. Therefore

    |B_(k,X)(J)|=k!.

The number of distinct such J is asymptotically a positive constant times (X/log X)^k, divided by k!, for fixed k. Hence the EXACT ray diagonal satisfies

    sum_J |B_(k,X)(J)|^2 >>_(k,Q) X^k/(log X)^k .         (8)

For R>=C_k X^k, the same-class Schur error in (4) is at most one-half of the ray diagonal (take C_k large enough). Thus

    sum_l p_R(l)|A_l(X)|^(2k)
              >>_(k,Q) X^k/(log X)^k .                    (9)

This lower bound uses the elementary class-number-one setting; it does not claim such a direct lower bound for arbitrary choices of class-character extensions.

So the general upper exponent X^(k+epsilon) at sufficient angular width is optimal in the exponent. The loss is not merely a lazy divisor bound.

## 5. A rigorous limit of positivity-only principal extraction

At center l0=0,

    p_R(0)^(-1) =sum_(l in Z)exp(-l^2/(2R^2)) asymptotic sqrt(2pi)R
    as R grows, and is comparable to R for all R>=1.

Since the principal term l=0 is one nonnegative summand, (15) of PROOF.md gives

    |A_0(X)|^(2k)
      <= p_R(0)^(-1) M_(k,R)(X;0)
      <<_(k,epsilon) X^(k+epsilon)(R+X^k).                (10)

The optimal bound from this inequality, over R>=1, is X^(2k+epsilon), i.e. |A_0(X)|<<X^(1+epsilon). This cannot reach the square-root criterion X^(1/2+epsilon) for ANY k, even along unbounded fixed orders. The obstacle is the X^k angular resolution cost of a product of k ideal factors, not a failure to push k high enough.

This is a limitation of THIS norm+positivity argument, **not** a no-go theorem for all moment methods or all signed projections.

The actual missing new theorem would have to exploit cancellation in (4) at the fixed principal row, or a different projection that recovers the reciprocal-zeta pole without paying the angular Gram width. The free-Mellin projection #962, the prime derivative #975/#991, and the determinant quotient #993 are distinct zero-sensitive candidates; none currently provides the required RH-strength arithmetic estimate.
