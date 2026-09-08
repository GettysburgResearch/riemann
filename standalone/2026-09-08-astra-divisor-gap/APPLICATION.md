# Certified elimination, rather than another positive finite section

Status: proposed component consequences of ADG26.T1; independent review pending.
All norms below are the original inherited Hilbert norms. None is an RH proof.

## 1. The exact block now has a quantitative inverse

For the full arithmetic matrix L_N of PROOF.md, let U=h_N perpendicular and
A=L_N restricted to U. Then A>=gamma I with gamma=1/kappa(P). If b is in U,
there is a unique solution x=A^(-1)b, and

    ||x||<=kappa(P)||b||,
    <x,A x><=kappa(P)||b||^2.                         (18)

This is uniform over all coefficient signs and grows only logarithmically in
the logarithm of the largest allowed prime. It was not supplied merely by
the earlier sum-of-squares identity. The extension to a fixed-prime, unbounded
exponent reservoir is proved in Section 5 of PROOF.md.

For any trial y in U, define

    r=b-Ay,
    F(y)=2 Re<b,y>-<y,Ay>.

Completing the square gives the exact identity

    <b,A^(-1)b>-F(y)=<r,A^(-1)r>.

Thus the COMPLETE correction, not only a projected correction, obeys

    F(y) <= <b,A^(-1)b> <= F(y)+kappa(P)||r||^2.        (19)

There is no assumption that a Galerkin limit or a numerical solve converges.
The residual must be enclosed in the original metric. This is an a posteriori
certificate applicable to any chosen finite calculation.

## 2. A whole-matrix Schur lower certificate

Let B map a retained Hilbert space H0 into U (or U tensor H), and let H0 have
Hermitian operator H_0. In the block operator

    T = [[H_0, B*], [B,A]],

the exact Schur complement is S=H_0-B*A^(-1)B. Given ANY bounded proposed solve
Y:H0->U, set

    R=B-AY,
    V=Y*B+B*Y-Y*AY.

Direct multiplication proves

    B*A^(-1)B - V = R*A^(-1)R,
    H_0-V-kappa(P)R*R <= S <= H_0-V.                  (20)

This controls all retained coefficient combinations simultaneously. The
right-hand bound is an upper certificate. It becomes a genuine LOWER
certificate only after subtracting the explicit residual budget on the left.
If an additional self-adjoint perturbation of A has norm at most eta<gamma,
replace kappa by 1/(gamma-eta), and compute the residual for that actual block.
No unbounded or unchecked perturbation is covered by this statement.

Standard Schur complement algebra is not claimed new. The new input is the
explicit arithmetic coercivity constant valid on the entire eliminated block,
including arbitrary finite divisor-closed cutoffs and infinite fixed-prime
reservoirs. That is the precise downstream prerequisite supplied here.

## 3. A finite actual-source demonstration, not a synthetic Gram scan

The checker encloses one exact inverse quadratic for S={1,...,32}, P=31.
Use coordinates f(n)=sqrt(n)v_n. A rational basis for the harmonic-mean-zero
space is given by columns T_i, i=2,...,32:

    f(i)=x_i (i>=2),  f(1)=-sum_(i=2)^32 x_i/i.

Its EXACT inherited metric is

    M_(i,j)=delta_(i,j)/i+1/(ij).

Its stiffness K is the full prime-power form E_S(Tx). Every entry is a finite
linear combination of log p with rational coefficients. The target covector
b is (1,0,...,0), so b*x reads the coefficient x_2. The quantity certified is

    m_32=b^T K^(-1)b.                                 (21)

It is not a zeta value, an eigenvalue of xi, or the original prime-error K.
The rational trial y is fixed in check.py with denominator 10^8. A discarded
floating solve proposed it; all acceptance calculations are independent exact
or directed arithmetic on the fixed rational trial.

For an independent FINITE gap certificate, replace each log p in K by
(2/3)floor(log_2 p), obtaining a rational lower matrix K_-. The checker proves

    K_- - M/384 is positive definite

by all 31 exact rational LDL pivots. Since log2>2/3, the actual K>=K_-; hence
K>=M/384 without needing to accept the infinite ADG26 proof for this one
finite experiment. Directed reduced-atanh logarithms enclose every actual
entry used in F(y) and r=b-Ky. Since M>=diag(1/i),

    r^T K^(-1)r <=384 r^T M^(-1)r <=384 sum_(i=2)^32 i |r_i|^2.

This yields an enclosure for the TRUE inverse quadratic (21), not just the
trial's objective. The printed enclosure in result.json is verified against
all retained rational endpoints. There is no unknown prime tail: L_32 is a
finite object by definition, and all powers with j p^k<=32 are included.

## 4. Relation to the existing source programmes

The exact C_N here is the prime-power cusp matrix in the earlier
`divisor-cusp-pass10/PROOF.md`, at the source pinned in SOURCES.json. Its
arithmetic diagonal D_N turns the signed cross interaction into L_N.
The refined bound is

    <v,C_N v> <= <v,D_N v>
             -kappa(P)^(-1)[||v||^2-|<h_N,v>|^2/||h_N||^2].

This offers a quantitative reserve on the coefficient complement, with all
multiplicities of prime powers and all complex coefficient signs retained.
For Hilbert-valued window primitives the projection removes one entire common
function channel; it does not remove that function's internal infinite degrees
of freedom. No claim is made that the gamma term or window means equal D_N.

The separate square-grid programme leaves an accumulated discrepancy upper
bound open. Nothing proved here says that its signed increments have small
E_S, or identifies their full source with L_N. A real adapter would have to
retain its continuum, means, endpoints and metric. That adapter or an adequate
arithmetic upper bound remains a research task, not a premise for the new gap.

In particular, adding -epsilon*h_N h_N^*/||h_N||^2 leaves every complement
estimate unchanged and creates a negative direction. A positive eliminated
block cannot force the retained Schur complement to be positive. Conversely,
(20) now gives a rigorous way to CHECK such a lower bound once the actual
retained block and coupling have been constructed and bounded.

## 5. Sparse application and a deterministic convergent solve

For the complete initial interval {1,...,N}, the number of edges is

    E_N=sum_(p^k<=N) floor(N/p^k)
        <=N[3log(1+log N)+1].                         (22)

Indeed, with q=1+1/log N, positivity of the Euler logarithm gives
sum_(p<=N)1/p<=e log zeta(q)<3log(1+log N); the k>=2 part is at most
sum_(n>=2)1/[n(n-1)]=1. This uses only the decreasing-integral estimate
zeta(q)<1+1/(q-1), not PNT. The empty contributions are retained exactly.
Thus the complete form can be applied in O(N(1+log log N)) arithmetic
operations after generating the primes, with no dense matrix storage.

Let Gamma=2(log N+3) and b perpendicular to h_N. The iteration

    y_0=0,  y_(m+1)=y_m+(b-L_N y_m)/Gamma

stays in that orthogonal space in exact arithmetic. From (5), its residual is
(b-L_N y_m)=(I-L_N/Gamma)^m b and therefore

    ||b-L_N y_m|| <=exp[-m/(Gamma*kappa(P))] ||b||.     (23)

This gives a prescribed convergent solve and a certified residual budget in
(19)-(20), with O(log N log log P) iterations per fixed reduction factor.
It is an arithmetic-operation statement, not a bit-complexity theorem or a
claim about unchecked floating-point convergence. Directed enclosures of the
actual final residual can be used exactly as in Section 3. No full-size solve
was run here beyond that 31-dimensional demonstration.
