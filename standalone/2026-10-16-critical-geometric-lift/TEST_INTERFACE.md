# Closing the compact-test to Gaussian interface

Status: PROPOSED analytic adapter, not a proof of its arithmetic hypothesis.
This is a source-specific application of the classical uniform boundedness
principle (Banach--Steinhaus/Baire) and a dyadic partition of unity. No claim
of novelty for either principle. The proof makes the missing seminorm issue
in #948 explicit and resolves it under the all-compact-test hypothesis.

## Theorem

Let a(n) be coefficients indexed by ideals of one fixed number field, with
sum_n |a(n)|(Nn)^(-c)<infinity for some c>0. Define

    A_W(X)=sum_n a(n)W(Nn/X).

Fix beta>=0. Suppose for EVERY W in C_c^infinity(0,infinity) there is C_W
such that |A_W(X)|<=C_W X^beta for all X>=1. Then, for

    w(t)=(1/(2sqrt(pi)))t^(-5/6)exp(-(log t)^2/4),
    A_w(Z)=sum_n a(n)w(Nn/Z),

one has |A_w(Z)|<=C Z^beta for Z>=1. The source is unchanged. A separate
constant may be chosen for each beta; hence hypotheses with beta=1/2+epsilon
for every positive epsilon give the corresponding Gaussian estimates.

## Proof

Fix the Frechet space E of smooth functions supported in [1/2,2], with
seminorms ||W||_N=max_(j<=N) sup_t |W^(j)(t)|. For each X>=1,
L_X(W)=X^(-beta)A_W(X) is a continuous linear functional (a finite sum).
The hypothesis says p(W)=sup_X |L_X(W)|<infinity for every W in E.
The closed sets {p(W)<=n}, n=1,2,..., cover E. Baire's theorem gives one
with nonempty interior. Subtracting two elements of a smaller neighborhood
in that set bounds p on a neighborhood of zero; rescaling gives

    |A_W(X)|<=C X^beta ||W||_N                            (1)

for some finite N and C, uniformly in X>=1 and W in E. This is the usual
uniform-boundedness proof, not differentiation of an unspecified O constant.
For 1/2<=X<=1 there are only finitely many possible coefficient indices,
so enlarging C extends (1). For X<1/2 the sum vanishes. Thus (1) holds for
all X>0.

Choose smooth rho supported in [1/2,2], such that
sum_(j in Z) rho(2^(-j)t)=1 for t>0. Such a partition follows by dividing
one positive annular bump by its locally finite dyadic sum. Set

    W_j(t)=rho(t)w(2^j t),  X_j=2^j Z.

Then A_w(Z)=sum_j A_(W_j)(X_j). Every fixed finite seminorm satisfies

    ||W_j||_N <= C_N exp(-c j^2+C_N |j|),                 (2)

because log t is bounded on the annulus, while differentiating w(2^j t)
only produces polynomial factors in j and bounded powers of t^(-1).
Equations (1)-(2) give a summable bound

    sum_j |A_(W_j)(2^j Z)|
        <=C Z^beta sum_j 2^(j beta)exp(-c j^2+C_N|j|).

The rearrangement is justified by the assumed absolutely convergent
Dirichlet series and the Gaussian decay at both ends. This proves the theorem.

## Application and exact boundary

For the coefficients c_eta of MATHEMATICS.md, the required Dirichlet series
is absolutely convergent for every c>1 by (5)-(6). Their Dirichlet series is
Hhat/(C_S zeta_F^S); the Mellin transform of w supplies the Gaussian factor.
Consequently an all-compact-test scalar bound yields
OPEN-G in PRE_POISSON.md with no extra hypothesis about uniform test
seminorms. It is enough to know each fixed compact test separately.

The same argument applies to Banach-valued sums if the pointwise boundedness
hypothesis is supplied for their norms: apply Baire to the continuous
seminorms. It does NOT turn H=X^h information into a same-height family for
all shorter X. That independent arithmetic quantifier remains required.
Neither the all-test scalar bound nor the full moment estimate producing it
is proved here. The gain is a completed analytic adapter, not an exponent.
