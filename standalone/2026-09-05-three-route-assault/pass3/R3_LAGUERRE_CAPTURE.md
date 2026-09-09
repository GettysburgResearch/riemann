# Route 3: a fixed, source-defined Laguerre matrix with quantitative global capture

Status: PROPOSED COMPLETE PROOFS; independent mathematical review required. Arithmetic positivity and RH remain unproved.
Sources: the trace-class Hardy operator in PR #793/pass2, standard Laguerre/Hardy analysis, and the all-rank versus coefficient distinction in #785/#792.
Scope: a=1, b=3/2, all zero multiplicities, a predetermined orthonormal basis. No zero list is needed to DEFINE the finite matrices. Coarse zero-count constants occur only in the convergence proof.

## G1. Freeze the operator and the basis

Retain the parent continuous even real function W(x)=W_(3/2)(x), and put

    (Tf)(t)=integral_0^infinity 2 exp(-(t+u)) W(t-u) f(u)du.

The parent proves T is self-adjoint and trace class, and T>=0 iff RH. Its safe source is

    F(r)=integral_0^infinity e^(-rx)W(x)dx
         =[L(r)-(2r/3)L(3/2)]/(9/4-r^2),
    L(r)=xi'/xi(1/2+r), r>1/2,                             (G1)

with the removable value at r=3/2. L(r) is the explicit gamma-plus-absolutely-convergent-prime expression in the parent. This is NOT a new positivity theorem.

Use the fixed orthonormal Laguerre basis

    ell_n(t)=sqrt(2)e^-t L_n(2t), n>=0,
    Q_N=projection onto ell_0,...,ell_(N-1),
    A_N=[<ell_m,T ell_n>]_(0<=m,n<N).

Unlike the target-dependent Blaschke witness in pass2, these matrices and their ordering are fixed before any hypothetical zero is specified.

## G2. Rank-two displacement: the full matrix comes from one safe scalar germ

Put c(z)=F(2/(1-z))=sum c_n z^n. Its argument has Re r>1 on the disk, so all c_n are derivatives of safe arithmetic data. The full bivariate generating identity is

    sum_(m,n>=0) A_(mn) z^m w^n
          =2[c(z)+c(w)]/(2-z-w).                          (G2)

The variable w here is a formal second variable, not an implicit complex conjugation. For a Hermitian-kernel interpretation substitute w=bar v. All coefficients are real and A is symmetric.

Proof. The basis generating function is sqrt(2)/(1-z) times exp(-(1+z)t/(1-z)). Multiplication by the damping e^-t changes the Laplace rate to r(z)=2/(1-z). Split the double integral into t>=u and u>=t. For Re r,Re s>1/2,

    double_integral exp(-rt-su) W(t-u)dtdu=[F(r)+F(s)]/(r+s).

The prefactor simplifies exactly to G2. All interchanges are justified initially on a small closed bidisk by the parent growth |W(x)|<=C exp(|x|/2), then throughout their analytic domain.

Coefficient comparison gives the exact recurrence

    2A_(mn)-A_(m-1,n)-A_(m,n-1)
       =2[c_m 1_(n=0)+c_n 1_(m=0)],                       (G3)

with negative indices zero. In particular A_00=2c_0, not c_0. This is a rank-two displacement/Lyapunov equation; it is not a rank-two bound on A itself. A_N requires only c_0,...,c_(N-1). Safe values occur at s=2 and s=5/2 and derivatives at the latter, with convergent prime-power log moments.

## G3. Exact tail of every zero feature in this basis

For a Xi zero z=gamma+iy, |y|<1/2, retain

    h_z(t)=sqrt(2)exp(-t+izt)/(3/2-iz).

The standard Laguerre Laplace integral gives

    <ell_n,h_z>= d_z alpha_z^n,
    d_z=2/[(3/2-iz)(2-iz)], alpha_z=(-iz)/(2-iz).             (G4)

Moreover

    ||(I-Q_N)h_z||=||h_z|| |alpha_z|^N,
    |alpha_z|^2=(gamma^2+y^2)/(gamma^2+(2+y)^2)<1,
    |alpha_z|^N<=exp(-N/(gamma^2+25/4)).                    (G5)

The last inequality uses 1-|alpha_z|^2=4(1+y)/(gamma^2+(2+y)^2)>=2/(gamma^2+25/4). It holds also for the conjugate feature. Trace-class summation of the two rank-one projection errors yields

    ||T-Q_N TQ_N||_1
      <=sum_z m_z ||h_z|| ||h_barz||
                  (|alpha_z|^N+|alpha_barz|^N).            (G6)

This bound retains ALL zeros and multiplicities; a finite checked prefix is not silently used as the entire operator.

## G4. Uniform trace-norm convergence rate without RH or spacing

Fix C_0,T_0 such that the classical count satisfies

    N_*(U):=sum_(|Re z|<=U) m_z <=C_0 U log(eU), U>=T_0.

Increase T_0 to at least 5/2. Let c_*=2/sqrt(3) and

    M_0=8 C_0 T_0 log(eT_0),
    kappa=sqrt(1-2/(T_0^2+25/4))<1.

For N>=T_0^2 the following explicit bound holds:

    ||T-Q_N TQ_N||_1 <= epsilon_N,
    epsilon_N=2M_0 kappa^N
       +[24 c_* C_0 log(e sqrt(N))+16 c_* C_0 log2]/sqrt(N).
                                                                  (G7)

In particular epsilon_N=O(log(N+2)/sqrt(N)), unconditionally. Constants are explicit in the stated coarse count bound; no numerical values for C_0,T_0 or a new effective zero-height theorem are claimed.

Proof. For |gamma|<=T_0, each feature norm product is at most 8, and G5 is at most kappa^N (directly from the preceding bound on alpha^2). This gives the first term. For |gamma|>T_0,

    ||h_z|| ||h_barz||<=c_*/gamma^2,
    |alpha_z|^N<=exp(-N/(2gamma^2)).

Write Y=sqrt(N). On high dyadic shells [2^kY,2^(k+1)Y], k>=0, omit the exponential and bound the sum by

    (2C_0/Y)2^-k[log(eY)+(k+1)log2].

Summation gives [4C_0 log(eY)+8C_0 log2]/Y. On lower shells (Y/2^(k+1),Y/2^k], intersected with |gamma|>T_0, use the exponential factor exp(-4^k/2) and obtain at most

    (4C_0/Y)log(eY) 2^k exp(-4^k/2).

Only shells whose upper endpoint exceeds T_0 are needed, so the count estimate is always applied in its valid range. The sum over k is less than 2: for k>=1 use 4^k/2>=2k and e^2>4. Multiplying the total by 2c_* as in G6 proves G7. QED.

## G5. Source-only finite witness and quantitative error transfer

A_N is now computable from safe arithmetic jets via G2--G3, without acquiring any hypothetical target or zero census. Let lambda_min(A_N) denote its smallest eigenvalue. Then

    lambda_min(T)>=min(0,lambda_min(A_N))-epsilon_N.         (G8)

If A_N has a negative direction, the same finite Laguerre combination is already a negative direction of T: compression is exact, so no omitted-mode correction is needed for that implication. Conversely every negative direction of T is detected by A_N for all sufficiently large N, by G7. More quantitatively, if <v,Tv> <=-d for a unit v and epsilon_N<d, then Q_N T Q_N has a negative direction.

For an approximate arithmetic matrix Atilde_N with ||A_N-Atilde_N||<=delta_N,

    lambda_min(T)>=min(0,lambda_min(Atilde_N)-delta_N)-epsilon_N.

A strictly negative eigenvalue of Atilde_N below -delta_N certifies negativity of the exact A_N. The comparison keeps arithmetic truncation error delta_N separate from basis truncation epsilon_N.

Thus any source proof of A_N>=-eta_N I along an unbounded sequence N, with eta_N->0, would prove T>=0 and RH. This is an OPEN arithmetic premise, not a consequence of G7. A generic trace-norm bound never determines the sign.

## G6. The convergence order is optimal for this basis under RH

Conditional on RH, positivity gives the exact lost trace

    Tr(T)-Tr(Q_N TQ_N)
       =sum_gamma m_gamma/(9/4+gamma^2)
                         (gamma^2/(gamma^2+4))^N
       ~ log N/[8 sqrt(pi N)],                             (G9)

where gamma ranges over BOTH signs, with multiplicity. Hence ||T-Q_NTQ_N||_1 cannot be o(log N/sqrt(N)) in that case.

To obtain the leading constant, use N_*(U)~(U/pi)log U and scale gamma=sqrt(N)x. The scaled counting measures divided by sqrt(N)log N converge on each compact subinterval of (0,infinity) to dx/(2pi). Also

    N/(9/4+Nx^2) * (Nx^2/(Nx^2+4))^N -> x^-2 exp(-4/x^2).

The same high/low dyadic bounds as G4 uniformly dominate the tails after dividing by log N/sqrt N, so compact convergence extends to the whole integral. Finally integral_0^infinity x^-2 exp(-4/x^2)dx=sqrt(pi)/4. The product of the two constants is 1/(8sqrt(pi)). This uses the classical leading zero-count law; it is not a numerical fit.

## G7. What the attempted positivity proof does not obtain

The displacement equation G3 has a rank-two RIGHT-HAND SIDE, but that side need not be positive. Replacing it by an absolute or positive envelope changes the actual operator. Safe-axis analyticity of c and trace-norm convergence of A_N hold even in synthetic off-line configurations. Neither gives A_N>=0.

The advance is a fixed, source-only and quantitatively convergent matrix interface, replacing the target-dependent geometric witness as the practical object to attack. It does not identify T's Fredholm determinant with Route 1's invariant xi determinant. It also does not import compact-band BGST estimates into this new metric. The all-N arithmetic sign remains the one missing step.

## G8. A literal trace-family bridge to Route 1

For the family T_b with a=1 and any b>1/2, trace-class summation gives

    Tr T_b=W_b(0)=L(b)/b=2 (d/dv)log F_invariant(v),
    v=b^2-1/4.                                           (G12)

Thus at b=3/2, the actual moments certified in R1_MOMENTS.md satisfy

    p_(j+1)=[(-d/dv)^j Tr T_(sqrt(v+1/4))]_(v=2)/(2j!).    (G13)

The derivative exchange follows locally from the rational resolvent weights and the summable zero tail; the independent safe source G1 gives the same derivatives. Equivalently both sides follow from the invariant chain rule. This is an exact common SOURCE, not an assertion that T_(3/2)'s eigenvalues are the reciprocal xi zeros. In particular det(I+uT_(3/2)) is not identified with f(u); positivity of a scalar trace or of finitely many trace moments is not operator positivity.
