# Independent weighted-Hardy reconstruction of the operator range

Reviewer:equivalences. Date:2026-11-17. I derived the coefficient normalization and Schur route independently and sent it to root before receiving li_skeptic's full proof. This note records that reconstruction; the proposed repaired classification is an elementary operator statement, not a claim about RH or historical priority. Parent adjudication is separate.

## Exact setting and result to check

Let alpha<−1,a>0, beta=alpha+2<1, delta=a+(alpha+1)/2. In the exact coefficient spaces D_gamma with norm² sum|A_n|²(n+1)^gamma, set

T_af=f'−af/(1−z):D_beta->D_alpha.

Then T_a is bounded. The proposed complete classification is:

* delta>0: bounded bijection;
* delta<0: bounded surjection with one-dimensional kernel span{(1−z)^−a};
* delta=0: injective, dense proper nonclosed range.

Restricting alpha to[−3,−2) repairs the printed Proposition5.1 by making its bounded-bijection inequality strict. It does not automatically prove the paper's later reformulation or every assertion depending on it.

## Boundedness before inversion

Differentiation mapsD_beta boundedly intoD_(beta−2), by direct index comparison of(n+1)A_(n+1). For multiplication by(1−z)^−1, normalize v_k=A_(k−1)k^(beta/2), k>=1. The positive majorant matrix is

K_(n,k)=n^(beta/2−1) k^(−beta/2) 1_(k<=n)
 =n^(−b−1/2)k^(b−1/2)1_(k<=n), b=(1−beta)/2>0.

Schur's weightp_n=n^−1/2 works: the weighted row sum is controlled by n^(−b−1/2)sum_(k<=n)k^(b−1), and the column sum by k^(b−1/2)sum_(n>=k)n^(−b−1). Both are at most fixed multiples ofp_n orp_k, respectively. Thus the multiplier andT_a are bounded. This proof works for everybeta<1 and invokes no claim from the source's disputed surjectivity argument.

## Prefix normalization and every coefficient

Write f=sumA_nz^n,g=sumG_nz^n. Put

P_n=(a+1)_n/n!, c_n=(a)_n/n!, S_n=sum_(k0..n)A_k, u_n=S_n/P_n.

The coefficient equationT_af=g is

G_n=(n+1)A_(n+1)−aS_n.

Since P_(n+1)/P_n=(n+a+1)/(n+1), it gives

u_(n+1)−u_n=G_n/[(n+1)P_(n+1)],                             (R1)

A_0=u_0,

A_n=c_nu_n+G_(n−1)/(n+a), n>=1.                            (R2)

For(R2), P_n−P_(n−1)=c_n and P_(n−1)/P_n=n/(n+a). This checks the off-by-one factors that matter in a proposed inverse. For fixeda>0, Gamma asymptotics and the finite initial segment give positive all-index bounds P_n comparable to(n+1)^a and c_n comparable to(n+1)^(a−1).

## Two signs of delta

Normalize x_k=G_(k−1)k^(alpha/2), k>=1. The direct term in(R2) maps boundedly intoD_beta because

(n+1)^(alpha+2)/(n+a)² <=C_(a,alpha)n^alpha.

For delta>0 choose

u_n=−sum_(k=n+1..infinity)G_(k−1)/(kP_k).

The sum is absolutely convergent: its normalized absolute majorant is sum|x_k|k^(−delta−1/2), with square-summable kernel for delta>0. The c_nu_n term in the domain norm is majorized by the matrix

H_(n,k)=n^(delta−1/2)k^(−delta−1/2)1_(k>=n), n,k>=1,

after replacing the output indexn byn+1, which is exactly the tail starting index. Weighted row/column Schur sums withp_n=n^−1/2 reduce to sum_(k>=n)k^(−delta−1) and sum_(n<=k)n^(delta−1). Both are bounded with fixed constants at most1+1/delta after the elementary integral comparisons. This also includes the a0=u0 functional. Hence the construction is a bounded right inverse.

For delta<0 takeu0=0 and the finite forward sums from(R1). The matrix is the reverse orientation

n^(delta−1/2)k^(−delta−1/2)1_(k<=n).

Writingb=−delta>0 turns this into the same Schur matrix used in the multiplier bound. Its row/column sums are finite with constants depending on|delta|. This gives a bounded right inverse. All constants keepa,alpha fixed; no uniformity asdelta approaches0 is inferred.

The full analytic homogeneous solution isC(1−z)^−a. Its domain norm is comparable to sum n^(2delta−1), so it belongs toD_beta exactly whendelta<0. Thusdelta>0 gives uniqueness and a bounded inverse;delta<0 gives the stated one-dimensional kernel. The disappearance of the kernel atdelta0 proves injectivity but says nothing about surjectivity, which is the source endpoint pitfall.

## Critical range, not merely an unbounded inverse

Atdelta0, truncate the exact homogeneous Taylor coefficients: f_K=sum_(n0..K)c_nz^n. Then

T_af_K=−aP_K z^K/(1−z),

||f_K||²_(D_beta) ~logK/Gamma(a)²,

||T_af_K||²_(D_alpha) ->1/[2a Gamma(a)²].

The last limit follows from2a+alpha+1=0, P_K~K^a/Gamma(a+1), and the elementary power tail. ThusT_a is not bounded below. Since it is bounded and injective, its range cannot be closed.

Its range is dense: for any polynomialq,

T_a[(1−z)q]=(1−z)q'−(a+1)q,

which is triangular on the polynomial basis with nonzero diagonal−(n+a+1). Hence every polynomial target has a polynomial preimage, and polynomials are dense inD_alpha. Nonclosedness already implies nonsurjectivity; an explicit target is also available. TakeG_(k−1)=k^a/log(k+1). Its target norm² is sum1/[k log²(k+1)], finite atdelta0. The increments in(R1) are positive and asymptotic toGamma(a+1)/(klogk), so everyu_n grows asGamma(a+1)loglogn plus a constant. Equation(R2) forces|A_n| comparable from below to n^(a−1)loglogn eventually, whose domain squared norm dominates sum(loglogn)²/n. Thus this target has no domain preimage.

The previously documented alpha−3,a1 target is the exact-logarithmic special case. Neither critical argument uses a numerical computation or any RH assumption.

## Comparison and next dependency task

Compare with `audits/adversarial_reviews/gallardo_seco_hardy_repair_skeptic_round4.md`, independently produced by li_skeptic. This note does not independently reproduce all cited classical operator literature or assert priority. The remaining paper-specific task is to trace Proposition5.1's use in Theorem5.5, distinguishing the bounded forward map from a bounded inverse and checking the auxiliary multiplier's lower-bound hypothesis.
