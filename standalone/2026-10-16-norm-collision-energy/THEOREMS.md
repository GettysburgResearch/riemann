# Norm collisions and an unconditional averaged critical-energy theorem

Status: PROPOSED complete mathematical arguments, not independently reviewed.
Scope: unconditional all-scale bounds for actual coefficient sums, including
all equal-rational-norm pairs and a full Mellin-twist average. These are not
conditional norm comparisons, randomized prime models, or an RH proof.
No new pointwise native moment or zero-free exponent is asserted.

## 1. Exact objects and main statements

Fix a number field F of degree d and a finite excluded-prime set S. Write

    F tensor_Q F = E_1 x ... x E_r,       r = r(F),
    Z_F,2(s) = product_(j=1)^r zeta_(E_j)(s).

The E_j are fields, with multiplicities retained. In particular r(Q)=1;
r(F)=2 for a quadratic field; and r(F)=d when F/Q is Galois. All implied
constants retain the fixed-field dependence. They are not discriminant-
uniform. This tensor square, not a hypothesis about its zeros, will determine
the logarithmic exponent. The integer r is independent of the degree m below.

For an integer m>=2, each prime ideal p of norm q, and each physical row u,
let |a_p(u)|,|b_p(u)|<=1. Original excluded or nonunit-masked primes have BOTH
values zero. Define multiplicative ideal coefficients c_m(n;u) by

    1-(1-1/q)a_p(u)x-b_p(u)q^(m/2-1)x^m.                (1)

Thus the permitted prime-ideal exponents are 0,1,m. Arbitrary correlations
between different rows and primes are allowed; no probability model for
these phases is introduced. The native coefficients mu_F(n)a(n;u), with
local factor 1-a_p(u)x, are covered separately by every upper bound below.
The geometric 1,7,13,... source of #950 is NOT (1).

Keep one nonnegative finite row measure w, of mass Z, at ALL column scales.
Set, for real c (the source uses c=5/6),

    W_c(y)=y^(-c)exp[-(log y)^2/4]/(2 sqrt(pi)),
    B_tau(X,u)=sum_n c_m(n;u)(Nn)^(i tau)W_c(Nn/X),
    Energy_tau(D)=integral_0^D integral |B_tau(X,u)|^2 dw(u) dX/X^2.

There is no truncation of the Gaussian or of the ideals. These are ideal sums,
not potentially infinite norm-only balls of elements in a positive-unit-rank
field. All tests below use D>=2. Define the rational-norm coefficients

    A(N,u)=sum_(Nn=N) c_m(n;u),
    L(N,u)=sum_(Nn=N) |c_m(n;u)|.                         (2)

Distinct ideals of the same norm MUST be summed before squaring A.
Let beta=2c-1 and k_c=exp(beta^2/2)/(2 sqrt(2pi)). Write Phi for the standard
normal CDF. The exact kernel from #952, reconstructed in Section 4, is

    K_D(v,z)=k_c (vz)^(-1/2)exp[-log(v/z)^2/8]
                       Phi(log D-log(vz)/2-beta).        (3)

### Theorem A: the full norm-collision block, not just identical ideals

For every allowed m, phases, masks, w and D,

    Delta_norm(D)=sum_N K_D(N,N) integral |A(N,u)|^2 dw(u)
       <= Delta_absnorm(D)
        :=sum_N K_D(N,N) integral L(N,u)^2 dw(u)
       <= C_(F,c) Z [log(3D)]^r.                         (4)

The last quantity is the absolute sum over ALL ordered ideal pairs of equal
rational norm. Thus even that entire off-ideal-diagonal sector is paid without
signed cancellation. The constant can be chosen independently of m>=2, S,
the masks and phases. It does depend on the fixed field.

More generally, for any symmetric graph G on the positive rational integers,
including loops, with at most Delta neighbors per vertex,

    sum_((Nn,Nl) in G) K_D(Nn,Nl)
                       integral |c_m(n;u)c_m(l;u)| dw(u)
       <= C_(F,c) Delta Z [log(3D)]^r.                    (5)

For example ALL pairs with |Nn-Nl|<=L have Delta<=2 floor(L)+1. Any bandwidth
L(D)=D^o(1) therefore costs D^o(1), uniformly in the actual row phases. This
is a bounded-degree norm-pair sector, not a bound for the complete graph.

### Theorem B: a full, unconditional Mellin-averaged critical energy

Let T>=1, tau_0 real, and g_T(t)=exp[-t^2/(2T^2)]/(sqrt(2pi)T). Then

    | integral_R g_T(tau-tau_0) Energy_tau(D) dtau
                                  -Delta_norm(D) |
       <= C_(F,c) Z (D/T) [log(3D)]^(r-1).               (6)

In particular the FULL original arithmetic source, not merely a diagonal
sector or a modified independent-prime model, satisfies

    integral_R g_T(tau-tau_0) Energy_tau(D) dtau
       <= C_(F,c) Z {[log(3D)]^r+(D/T)[log(3D)]^(r-1)}.   (7)

The estimate is uniform in the center tau_0, all m>=2 and all allowed phases.
For F=Q(omega) this is O(Z[log(3D)^2+(D/T)log(3D)]). At T>=D/log(3D) it
is a polylogarithmic bound for the full averaged energy. At T=D the error
in (6) is one logarithm smaller than the principal norm-diagonal order.
At T=D^(1+delta), delta>0, its error is O(Z D^(-delta)log(3D)^(r-1)).

This is a long vertical/Mellin-twist average. It gives no bound at the fixed
principal twist tau=0 and hence no new zeta zero-free half-plane. The long averaging
window is a genuine quantified cost, not hidden in a constant.

### Theorem C: the norm-collision logarithm is sharp

For one scalar row, take a_p=1 outside the fixed finite S and fix arbitrary
|b_p|<=1 there, with no finite-order character assumption. For each FIXED
m>=2 there is an explicit C_(F,S,m,b)>0 such that

    Delta_norm(D) ~ k_c C_(F,S,m,b) (log D)^r/Gamma(r+1). (8)

The same conclusion holds for the native ideal Mobius source, with its own
positive constant. Thus, in a quadratic field, replacing the full norm
block by the O(log D) identical-ideal diagonal misses a genuine log-squared
term. Combining (6) and (8), the same asymptotic holds for the full Gaussian
Mellin average whenever T log(3D)/D tends to infinity, including T=D. The asymptotic is for a fixed
m and fixed prime profiles; uniformity for m=m(D) is NOT asserted.

## 2. The rational-prime coefficient budget

We prove a single positive majorant for all rows and masks. For a rational
prime p with residue degrees f_1,...,f_g in F (q_i=p^f_i), let M_m(p^e) be
the coefficient of t^e in

    product_(i=1)^g [1+(1-1/q_i)t^f_i+q_i^(m/2-1)t^(m f_i)]. (9)

Extend multiplicatively to rational N. This includes all prime ideals,
even any in S; it is only an upper bound, not a change to the original sums.
It gives L(N,u)<=M_m(N) by unique ideal factorization and the triangle
inequality WITHIN each rational-norm fiber. For the native coefficients use
product_i(1+t^f_i) instead. All the following budgets hold for that variant.

Let r_p be the number of f_i=1, and let v=p^(-1/2). After dividing the e-th
coefficient in (9) by p^(e/2), each prime-ideal factor has total positive
mass 1+(1-1/q_i)q_i^(-1/2)+q_i^(-1). Its degree-one mass is
r_p(1-1/p)v. The total mass in rational exponents e>=2 is at most

    3^d v^2.                                           (10)

Indeed a degree-one ideal contributes at most 1+v+v^2; every other ideal
contributes at most 1+2v^2. Expand
(1+v+v^2)^r_p(1+2v^2)^(g-r_p), remove 1+r_p v and bound every remaining
monomial by v^2 times its coefficient, since 0<v<=1. Restoring the removed
r_p v^3 from (1-1/p)v still leaves a bound (3^g-1)v^2<=3^d v^2.
For the native variant the analogous estimate is even smaller.

Consequently, for every 0<=t<=1,

    P_(p,m)(1+t):=sum_e M_m(p^e)^2 p^(-e(1+t))
       <=1+r_p^2 p^(-1-t)+9^d p^(-2).                  (11)

This uses the SQUARE of the residual positive mass in (10); it is not the
false assertion that rational-norm coefficients themselves are bounded by
one. At t=0 the degree-one coefficient is r_p^2(1-1/p)^2/p. It follows also
that P_(p,m)(1+t)=1+r_p^2 p^(-1-t)+O_d(p^(-2)), uniformly in m and t, for the
unmasked principal source's SQUARED signed norm coefficients. Cancellation
among the higher local coefficients cannot affect its first coefficient.

## 3. Why the exponent is r(F), without a new zero-free theorem

The imported analytic number-theory facts are fixed-field ideal counting,
and the classical simple pole at 1 with positive residue and real s>1 Euler
product of each fixed Dedekind zeta function. No QRH/RH, Chebotarev error estimate,
prime-number-theorem cancellation, or Artin holomorphy is needed.

Here is the required tensor arithmetic. Separability gives
F tensor_Q F=product E_j. Outside a finite set of rational primes, reduction
is compatible with this decomposition and

    (O_F/p) tensor_Fp (O_F/p)
          =product_(i,j) [F_(p^f_i) tensor_Fp F_(p^f_j)].

A tensor factor on the right has an F_p field component if and only if
f_i=f_j=1; then it has exactly one. Equivalently,
F_(p^f) tensor F_(p^g) consists of gcd(f,g) copies of F_(p^lcm(f,g)).
Therefore the total number of degree-one primes among the E_j is r_p^2.
The local factor of Z_F,2 thus has positive coefficients and is at least
1+r_p^2 p^(-s) for real s>1. Its remaining terms are O_d(p^(-2s)) near 1.
These standard tensor/splitting facts are also proved by factoring a
separable primitive-element polynomial and applying CRT; see SOURCES.md.

Divide (11) by this local zeta factor. The quotient is at most
1+9^d/p^2 outside the finite exceptional set. At an exceptional prime the
whole critical local mass is bounded by 9^d, independently of m. Since
sum_p p^(-2)<infinity, for 0<t<=1,

    F_M(1+t):=sum_N M_m(N)^2/N^(1+t)
       <= C_F Z_F,2(1+t) <= C'_F t^(-r).               (12)

The field constants cover the compact part of 1<s<=2 as well as the pole.
This proves (12) uniformly in every m>=2. It also proves absolute convergence
of this nonnegative Dirichlet series without assuming it in the argument:
first compare finite Euler products, then use monotone convergence.

This is classical positive Euler/Rankin bookkeeping specialized to (1), not
a new general theorem about Rankin--Selberg L-functions. The useful arithmetic
improvement over the identical-ideal count is that EVERY rational-norm
collision is included and its exact pole order is identified.

### A coefficientwise refinement: one fewer logarithm in the error

The real-series bound (12) would give an extra logarithm in (6). We remove
it without a signed estimate or a uniform complex-continuation hypothesis.
At every good rational prime use a formal variable z and put

    P_p(z)=sum_e M_m(p^e)^2 p^(-e) z^e,
    V_p(z)=product_(h in tensor residue degrees)(1-p^(-h)z^h).

Thus V_p is the inverse local factor of Z_F,2 at the critical weight. Its
constant and linear coefficients are 1 and -r_p^2/p. Write
P_p=1+A z+P_2 and V_p=1-B z+V_2. The norm here is the absolute coefficient
sum of these polynomials. Section 2 and the fact that their omitted terms
have degree at least two give

    A<=d^2/p, B=r_p^2/p, |A-B|<=2d^2/p^2,
    ||P_2||<=9^d/p^2, ||V_2||<=2^(d^2)/p^2,
    ||V_p||<=2^(d^2).

Hence C_p=P_p V_p has constant coefficient one and

    ||C_p-1|| <= K_d/p^2,
    K_d=2d^2+d^4+2^(d^2)(1+d^2+9^d).                 (12a)

Indeed expand (1+A z+P_2)(1-B z+V_2); the five remaining bounds are
|A-B|, ||V_2||, AB, A||V_2||, and ||P_2||||V_p||. Notice that C_p may have a
NONZERO linear coefficient, but its critical mass is O(p^-2); deleting it
would be incorrect. For native Mobius, A=B and the same estimate holds.
At the finite exceptional primes use ||C_p||<=9^d 2^(d^2).

Returning to unweighted Dirichlet coefficients, let h_m be the exact formal
quotient of F_M by Z_F,2, and let v_m(N)=|h_m(N)|. Formula (12a) implies

    sum_N v_m(N)/N <= C_F, uniformly in m.             (12b)

Every formal coefficient identity uses only finitely many divisors, so this
requires no analytic interchange. The coefficients z_F,2(N) of Z_F,2 are
nonnegative, and F_M=h_m*z_F,2 implies

    M_m(N)^2 <= (v_m*z_F,2)(N).

Each factor field E_j has I_(E_j)(x)<=A_j x. Repeated Dirichlet convolution
and sum_(Nn<=x)1/Nn<=A_j(1+log x) therefore give

    sum_(N<=x) z_F,2(N) <= C_F x(1+log x)^(r-1).

Convolving with v_m and using (12b) proves the uniform, stronger prefix bound

    sum_(N<=x) M_m(N)^2 <= C_F x(1+log x)^(r-1), x>=1. (12c)

This is a positive arithmetic bound for complete rational-norm fibers.
It does not merely apply N^epsilon to their multiplicities. The first
coefficient matching in the tensor square is what makes (12b) summable.

## 4. Gaussian kernel, two weighted sums, and Theorem A

The unique representation n=r d^m, with r,d squarefree and (r,d)=1, gives
|c_m(n;u)|<=(Nd)^(m/2-1). Ordinary fixed-field ideal counting I_F(x)<=A_F x
then yields both

    sum_(Nn<=x)|c_m(n;u)|^j <= A_F zeta_F(2)x,  j=1,2. (13)

For j=1 the summation exponent in d is -m/2-1<=-2; for j=2 it is -2.
This is #952 Lemma E1, not claimed as new. The first bound and Gaussian
partial summation give sum_n|c_m(n;u)|W_c(Nn/X)<=C_(F,c)X. Its square is
integrable against dX/X^2 on every (0,D). Thus all following pair expansions
are absolutely convergent, including their tails at X=0 and Nn=infinity.

For finite sums put x=log X, a=log v, b=log z. The exponent in the pair
integrand equals

    -(x-(a+b)/2-beta)^2/2 -(a+b)/2+beta^2/2-(a-b)^2/8.

Integrating x from -infinity to log D gives (3). Absolute convergence just
proved passes this to the full sums. K_D is a Gram kernel, so

    0<K_D(v,z)<=sqrt(K_D(v,v)K_D(z,z)).                 (14)

Let t=1/log(3D), so 0<t<=1 and D^t<=e. For any lambda>0 and real x,
Markov's inequality for a standard normal G gives

    exp(lambda x)Phi(-x-beta)
       <=exp(-lambda beta+lambda^2/2).                 (15)

Use (15) with x=log(N/D) and lambda=t in (12) for the first of the
following TWO full-tail bounds. Use the sharper prefix (12c) for the second:

    sum_N M_m(N)^2 K_D(N,N) <= C_(F,c) [log(3D)]^r,
    sum_N N M_m(N)^2 K_D(N,N) <= C_(F,c) D[log(3D)]^(r-1). (16)

To see the second precisely, apply Stieltjes partial summation to the
decreasing weight Phi(log D-log x-beta) and the prefix (12c). After x=D e^y,
its upper bound is at most

    C_F D integral_(-log D)^infinity
               e^y (1+log D+y)^(r-1) phi(-y-beta)dy,

where phi is the standard normal density. The integral is at most
C_(F,c)(1+log D)^(r-1), by Gaussian decay. No truncation at N=D is used;
all N>D remain. Formula (4) follows from L<=M and integration in u.

For (5), put R_N=M_m(N)sqrt(K_D(N,N)). By (14) the absolute graph sum per
row is at most sum_((N,L) in G) R_N R_L. Applying 2R_N R_L<=R_N^2+R_L^2,
symmetry and the maximum degree bound gives at most Delta sum_N R_N^2.
Use (16) and multiply by Z. Loops are counted once and ordered off-diagonal
pairs twice, consistently with the original energy expansion. This proves
Theorem A with no arithmetic cancellation assumption.

## 5. A Gaussian log-frequency Schur bound: proof of Theorem B

Average the exact full pair expansion in tau. The elementary Gaussian
Fourier integral inserts

    exp[i tau_0 log(N/L)] exp[-T^2 log(N/L)^2/2].

All equal-norm pairs survive, giving Delta_norm, not the smaller ideal
diagonal. The absolute value of the remaining sum is at most

    Z sum_(N!=L) R_N R_L exp[-T^2 log(N/L)^2/2].        (17)

The required real-variable estimate is particularly simple. For every
integer N>=1, the function f(x)=exp[-T^2 log(x/N)^2/2] is increasing up to N
and decreasing thereafter. Compare each f(L), L<N, with its integral on
[L,L+1], and each L>N with its integral on [L-1,L]. Then

    sum_(L>=1,L!=N) exp[-T^2 log(L/N)^2/2]
       <= integral_0^infinity exp[-T^2 log(x/N)^2/2]dx
        = (N sqrt(2pi)/T)exp[1/(2T^2)].                (18)

Apply 2R_N R_L<=R_N^2+R_L^2 and symmetry to (17), then (18) and the second
bound in (16). Since T>=1, exp[1/(2T^2)]<=sqrt(e). This proves (6), hence
(7). It is a direct proof; no imported large-sieve or Montgomery--Vaughan
mean-value theorem is needed. Gaussian averaging and this Schur argument
are classical methods, not claimed as inventions.

## 6. Sharp asymptotics and an explicit quadratic constant

For the scalar principal source of Theorem C, rational-norm aggregation is
multiplicative. Put

    D_m(s)=sum_N |A(N)|^2/N^s,
    H_m(s)=D_m(s)/Z_F,2(s),   real s>1.

At every nonexceptional rational prime the quotient of local factors is
1+O_d(p^(-2)), uniformly for real 1<=s<=2 and m>=2, by Section 2. At a
fixed exceptional prime it is continuous and strictly positive on that
real interval. Infinite products therefore give, for each fixed m/profile,

    H_m(1):=lim_(s downarrow 1) H_m(s)>0,
    D_m(1+t) ~ C_(F,S,m,b)t^(-r),
    C_(F,S,m,b)=H_m(1) product_j Res_(s=1)zeta_(E_j)(s). (19)

This only uses a real one-sided limit, not an unjustified complex
continuation of D_m or uniform asymptotics with m growing. Finite exclusions
are retained in H_m. The native source has the same argument, because its
first rational-prime coefficient is -r_p.

For completeness the positive Tauberian implication is supplied in
TAUBERIAN.md. Applied to the measure sum_N |A(N)|^2/N delta_(log N), (19)
gives

    sum_(N<=exp L) |A(N)|^2/N
       ~ C_(F,S,m,b) L^r/Gamma(r+1).                   (20)

The same partial sums are O((1+L)^r) by (12). The smoothed sum in Delta_norm
is the expectation of that cumulative measure at L-beta-G, with G standard
normal, interpreted as zero at negative arguments. Divide by L^r and use
(20), the polynomial bound and Gaussian domination. This proves (8).

For F=Q(omega), S the primes above 2 and 3, m>=3, put alpha_p=1-1/p. At a
split rational prime p (p=1 mod 3), with its two DISTINCT ideals carrying
b_1,b_2, its squared-norm local factor at s=1 is exactly

    1+4 alpha_p^2/p+alpha_p^4/p^2+|b_1+b_2|^2/p^2
        +alpha_p^2|b_1+b_2|^2/p^3+|b_1 b_2|^2/p^4.    (21)

At an inert p (p=2 mod 3), q=p^2, it is

    1+(1-1/q)^2/q+|b_p|^2/q^2.                        (22)

Since Z_F,2=zeta_F^2, multiply (21) by (1-1/p)^4, (22) by (1-1/p^2)^2,
and include the excluded local factors, to obtain H_m(1). These local
expressions and hence the leading constant are independent of m>=3 when
the b profiles are fixed. The rate in (8) is not thereby uniform in m.
At m=2 the exponent-two channels collide, so (21) is FALSE; Section 2 and
Theorems A--C still apply with the correctly aggregated local coefficient.

For the native quadratic source the split local factor is 1+4/p+1/p^2
and the inert one is 1+1/p^2. Its constant is generally different from
(21)--(22). No claim of equality of these constants is made.

## 7. Exact progress and the remaining mathematical boundary

#952 bounded the equality-of-IDEALS diagonal by O(log D). Theorems A/C now
bound and asymptotically evaluate the larger equality-of-RATIONAL-NORMS
block: O(log(3D)^r), sharply log^2 D in the quadratic principal case. The
bounded-degree extension also pays a genuine near-norm part of the remaining
covariance. Theorem B bounds the FULL arithmetic energy after an explicitly
priced long Mellin average. None of these statements assumes the desired
native moment, the compensated injection bound, or a quasi-RH theorem.

The new upper bounds are genuine arithmetic statements, but the critical
pointwise energy at tau=0 still involves the complement of every paid norm
graph. Removing the long Mellin averaging cost is not proved. Positivity, (6), or
a small average cannot be used to extract that single deterministic member.
The signed coprime theta pairing of the recovered ramified-dilation packet
is a different source and is not identified with B by matching an Euler
factor. Its outstanding estimate remains outstanding.

There is no claimed historical priority for tensor-square Rankin counting,
Tauberian asymptotics, Gaussian averaging or Schur bounds. The proposed
contribution is their complete source-specific combination, its r(F)
exponent, uniform correction-order and mask coverage, and quantitative
full-energy statement. No independent mathematical referee has vetted it.
