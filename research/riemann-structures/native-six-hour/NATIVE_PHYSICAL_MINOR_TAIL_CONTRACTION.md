# A conditional fixed-minor certificate for every future physical horizon

This note designs an exact sufficient test. It records no test outcome and
does not promote bounded physical ranks to an all-horizon theorem. Its source
is the original three-prime half-source at2,3,5, its observation is the actual
1/d reduced-ratio sum, and its20 source directions are the independently
proved literal curvature space. No original Gamma matrix is needed here.

## 1. Freeze the minor before testing its future tail

Take the H900 panel in the frozen horizon discovery underlying the final
certificate `a4d610431d5edaf26b00bae903bb9111837e4c31`. Choose exactly its20
rational `physical_rank.independent_rows` and20 `pivot_coordinates`, in their
captured order. These specify20 reduced ratios and20 ambient polynomial/form
coordinates. The same choices are used at every later horizon; no later
pivoting selects a more favorable minor.

Let A_H be that20-by20 submatrix of the actual coalesced curvature rows.
At H900 its invertibility follows from the captured exact elimination and
must also be checked afresh. Since the full literal space has dimension20,
invertibility of A_H implies physical rank20. At a later horizon the chosen
minor may be singular even if other rows retain full rank; such a case is
an inconclusive outcome for this test.

## 2. Exact local formula, including the curvature factor2

For a selected reduced ratio a/b, write alpha_i=ord_(p_i)a,
beta_i=ord_(p_i)b. At an alias g with exponents k_i, put

    f_i(u)=a_(k_i+alpha_i)+b_(k_i+alpha_i)u,
    h_i(u)=a_(k_i+beta_i)+b_(k_i+beta_i)u,
    N_i(u)=f_i(u)h_i(u)=N_i0+N_i1*u+N_i2*u^2,
    D_i=f_i' h_i-f_i h_i'.                            (1)

Thus, writing local f=a+bu and h=c+du,

    N0=ac, N1=ad+bc, N2=bd, D=bc-ad.                 (2)

The coefficient of du_i wedge du_j in the literal curvature
2 d(lambda_(ga)) wedge d(lambda_(gb)) is exactly

    (D_i N_j' - N_i' D_j) product_(ell!=i,j) N_ell.  (3)

For a coordinate with polynomial powers t_i,t_j in{0,1}, its differentiated
part is respectively

    (t_i,t_j)=(0,0): D_i N_j1-N_i1 D_j,
                  (0,1): 2 D_i N_j2,
                  (1,0): -2 N_i2 D_j,
                  (1,1): 0.                         (4)

The other coordinate powers lie in{0,1,2}. Equations(3)--(4) are obtained by
expanding the two actual derivative products; they do not drop the original
factor2 or replace a source coefficient by a fitted value.

Define a nonnegative majorant w_(a/b,c)(g) by replacing each product in (4)
by its absolute product and replacing the difference in its(0,0) case by
the sum of those two absolute products. Multiply by the absolute value of
the corresponding N_ell,t_ell at every other prime. Then

    |C_(ga,gb)[c]| <= w_(a/b,c)(g).                   (5)

Each w is a sum of at most two products of **one-prime** nonnegative
sequences, with the displayed factors2 retained. The exact determinant D
is evaluated before taking its absolute value. If alpha_i=beta_i, D_i is
identically zero, and its majorant is set identically zero too.

## 3. Positive product sums with explicit geometric remainders

For any local factor L among |N0|,|N1|,|N2|,|D|, define

    S_(p,alpha,beta,L)=sum_(k>=0) L(k)/p^k.           (6)

The sums are nonnegative, so Tonelli and multiplicativity of1/g factor the
complete majorant sum into products of the local sums(6). This is only an
identity for the declared positive majorant; the signed source curvature
continues to be computed separately by (3).

Use a fixed local cutoff K=64. Compute every term through k=64 exactly as a
rational number. For e>=1, |c_e| is decreasing, where
c_e=(-1)^e binom(1/2,e). If N>=2, then for every e>=N,

    |a_e| <= |c_floor(N/2)|,
    |b_e| <= |c_floor(N/2)|.                          (7)

Indeed even a_e=c_(e/2), even b_e=|c_(e/2)|-|c_e|,
and odd a_e=0, |b_e|=|c_e|. Consequently for k>=K+1, set

    U_alpha=|c_floor((K+1+alpha)/2)|,
    U_beta =|c_floor((K+1+beta)/2)|.

The remaining local tail is bounded by

    R_L = m_L U_alpha U_beta * p^(-(K+1))/(1-1/p),    (8)

where m_N0=m_N2=1 and m_N1=m_D=2. For an identically zero D the remainder
is zero. The finite partial sum plus(8) is a fully rational upper bound
S_L^+. There is no numerical integration or floating error in it.

## 4. Subtract the same majorant on the complete known prefix

For horizon H and ratio a/b put G=floor(sqrt(H/(ab))). Enumerate every
2,3,5-supported g<=G. Compute both the signed source entry

    A_H[a/b,c]=sum_(g<=G) C_(ga,gb)[c]/g              (9)

and the positive prefix sum P_H[a/b,c]=sum_(g<=G) w_(a/b,c)(g)/g.
Replace each local S in the factored full majorant by S^+ to obtain an upper
bound U[a/b,c]. Define

    Tail_H[a/b,c]=U[a/b,c]-P_H[a/b,c].                (10)

This is nonnegative and bounds the sum of all omitted absolute source
coefficients. The subtraction uses the **same** positive majorant as U,
not the smaller signed coefficient or its absolute value. Thus cancellation
within the known prefix does not inflate the tail estimate. The only
majorization loss is on omitted aliases and the tiny univariate remainders.

For every later integer H'>=H,

    |A_(H')-A_H| <= Tail_H entrywise.                 (11)

This controls every future partial prefix, not only the infinite limit.

## 5. An exact Neumann sufficient test, not a necessary condition

If A_H is invertible, calculate its exact rational inverse and verify both
products with A_H equal the identity. If

    theta_H=max_i sum_j ( |A_H^(-1)| Tail_H )_(i,j) <1,  (12)

then ||A_H^(-1)(A_(H')-A_H)||_infinity<1 for every H'>=H. The Neumann
criterion makes A_(H') invertible for every such H'. Since the literal
source dimension is20 there, every later physical rank is exactly20.

An invertible minor with theta_H>=1 is **UNKNOWN**, not a rank failure.
A singular chosen minor is likewise UNKNOWN, not a failure of full physical
injectivity. The separate infinite-source theorem proves eventual
faithfulness without guaranteeing that these particular20 ratios remain
an invertible infinite minor, or that this sufficient norm bound succeeds.

A pass at H900 would combine with the frozen complete bounded atlas to prove
physical/literal rank equality for every horizon. A pass only at the fixed
held-out H=2^20 would prove the eventual statement with that explicit
threshold, leaving the interval901,...,2^20-1 unresolved. That gap must not
be filled by interpolation, monotonicity, or the infinite-limit theorem.
