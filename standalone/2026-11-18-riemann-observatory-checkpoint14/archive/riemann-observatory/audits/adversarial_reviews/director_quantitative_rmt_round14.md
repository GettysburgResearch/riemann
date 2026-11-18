# Finite positivity witnesses and positive exact determinant approximations

18 November 2026. The director read both complete derivations, the independent functional-analytic and Hermite reviews, and the third quantitative adjudication. The following are accepted scoped deductions. Their mechanisms are classical Jacobi, Gaussian orthogonal polynomials, compact-operator compression and Fourier estimates. Publication novelty has not been established. None extends the separate RH-conditional arithmetic window rb<1/2.

## A quantitative finite witness for every fixed rank

Use the fixed-rank formal cosine continuation

```text
M(z)=exp((J−1)H z+H z²/4) P_J(z)=sum mu_k z^k/k!,
H=log(b/a), d=b−a, 0<a<b<1, J a fixed positive integer.
```

The previously adjudicated determinant construction supplies a real zero 0<t_*≤1/d. Let R=2/d and take B≥1 with |M(z)|≤B on |z|=R. Define

```text
L=ceil(log_2(8B(B+1))), p_±(x)=sum_(j=0)^L (±t_* x/2)^j/j!.
```

The formal two-by-two moment matrix on p_+,p_- has strictly negative determinant. In particular the Hankel matrix (mu_(i+j)) for 0≤i,j≤L is not positive semidefinite and some polynomial of degree at most L has negative formal square expectation. It uses moments through degree 2L, not L.

Proof: Cauchy's coefficient bound gives |mu_k|/k!≤BR^(−k). The total-degree tail in each product is at most B sum_(m>L)(t_*/R)^m≤B2^(−L). Its limiting matrix has entries 0,1,1,M(−t_*), with determinant −1. At this error the diagonal product has magnitude at most 1/8 and the off-diagonal square at least (7/8)². This handles a zero that merely touches the real axis as well as a sign crossing. The explicit polynomial selection for a zero, positive or negative first diagonal is in the source derivation.

A sufficient fully explicit majorant is

```text
D=(2J−1) 16^(2J−2) (2J−1)! exp(1+R d exp(b)),
B=J! D^J exp((J−1)H R+H R²/4).
```

This follows by majorizing each shifted Legendre profile coefficient, then each oriented entry by (2J−1)16^(2J−2)(1+p+q)^(2J−1), and using the positive compound-Poisson monomial moments on the circle of radius R. The two jump intensities each have factor R/2; their combined exponential moment is bounded by exp(1+R d exp(b)). The bound is deliberately conservative and applies also to J=1,2 with t_*=1/d.

## At rank one the least order is known exactly

Let sigma²=H/2 and J=1. Then M(z)=exp(sigma²z²/2)(1−dz) is the moment function of the signed Gaussian density modifier 1−d x/sigma². In the normalized probabilists' Hermite basis, the degree-L moment form is congruent to

```text
I−(d/sigma²) T_L,
(T_L)_(k−1,k)=(T_L)_(k,k−1)=sigma sqrt(k), 1≤k≤L.
```

Thus it is positive semidefinite exactly when the largest zero of He_(L+1) is at most sigma/d. Equality gives a singular positive semidefinite form. The least negative witness order is the first strict crossing. In particular it exceeds sigma²/(4d²) and is at most floor(sigma²/d²)+1.

The last floor(sqrt(L)) vertices of the Jacobi matrix, tested with a positive sine vector, give lambda_max/sigma≥2sqrt(L)−O(1); the truncated weighted-shift norm gives the reverse leading bound. Consequently the least order is sigma²/(4d²)+O(sigma/d) as sigma/d→infinity. For a=b/2 and b→0 this is (log 2)/(2b²)+O(1/b). The first raw-moment crossing occurs around 1/b. A raw-moment discrepancy therefore need not cause a Hankel failure at a comparable order. This is useful negative knowledge about finite tests of the formal continuation, not an obstruction to the true intrinsic law.

[Complete witness derivation](geometry102_finite_hankel_bound.md) · [Independent strict-threshold check](weighted106_hankel_rankone_review.md) · [Third independent bounds and indices](uniform110_rmt_quantitative_adjudication.md). The optional sharper remainder in the third review is not needed for these claims.

The director independently replayed the exact rational certificate for the standardized function exp(z²/2)(1−z/2). All principal minors through order two are nonnegative, and q(x)=2x³+9x²+6x−3 gives formal square expectation −30. The equality fixture with standardized tilt 1/sqrt(3) is calculated after the exact rescaling y=sqrt(3)x: its order-two form is singular positive semidefinite, y²+3y is null, and y³+4y²+12y has square expectation −27. These finite fixtures confirm the strict inequality in the Hermite criterion. [Code](../../experiments/code/geometry111_rankone_hankel_certificate.py) · [Exact receipt](../../experiments/results/geometry111_rankone_hankel_certificate.json).

## The exact Petrov tail quotient has a positive finite representation

Use the already source-matched notation: N≥2, J≥1 fixed, m=N−1, n=m+J, X=T((1−w)^J)|_(P_m), F_+=−sum w^k/(2k), F_−=F_+(w^(−1)), H_N=sum 1/k and phi=exp(z(F_++F_−)). All sums are over the nonempty finite band unless stated otherwise. Let A_n=P_nT(phi)|_(P_n), and U orthonormal columns for the complement of X in P_n. For real z, put

```text
K=H(phi_−/phi_+) H(phi_−/phi_+)*, A=I−K,
C=T(phi_−)X, V=(range C)^perp,
L=P_nT(phi_+)|_(P_n), M=U*L^(−*)L^(−1)U.
```

The upper triangular factor preserves P_n, so V=Q_n H direct-sum W with dim W=J. Block elimination shows that L_obl/L_n is the determinant of the J-dimensional Schur complement S of A across Q_n within V. More explicitly,

```text
S=M^(−1/2)(U* A_n^(−1)U)M^(−1/2),
det Gamma(z)/det Gamma(0)=det M.
```

The source's optional fixed-tail chart need not be invertible. These identities require no such chart. They follow from the actual finite support, Jacobi on LL*, and the triangularly compressed Wiener–Hopf identity, with P_n A^(−1)P_n=L^(−1) A_n L^(−*).

For real z the common lower bound for A and its compressions is delta=exp(−2|z|H_N), and delta I≤S≤I. Compression eigenvalue monotonicity and the full Hardy determinant give the stronger determinant bounds

```text
exp(−H_N z²/4) ≤ L_obl/L_n ≤1,
exp(−J|z|H_N) ≤ det M ≤ exp(J|z|H_N),
exp(−J|z|H_N) ≤ det(U* A_n^(−1) U) ≤ exp(J|z|H_N).
```

They are uniform in N on compact real z intervals at fixed positive band. At a positive formal zero z_*, the exact mass-removed complementary determinant has liminf at least exp(−2J H z_*)>0. No emerging exact small eigenvalue is responsible for the zero of the extrapolated polynomial.

## A true-cutoff continuum Gram and a factorial approximation

For z≥0 let p,q be independent compound-Poisson totals with intensity z dx/(2x) on [a,b], and u_j(t)=sqrt(2j+1)P_j(2t−1). The normalized finite Gram converges entrywise to

```text
exp(−H_N z) M_ij  →
E[1_(max(p,q)≤1) integral_(max(p,q))^1 u_i(t−p)u_j(t−q) dt].
```

The true interval shrinks continuously at its boundary. This justifies weak convergence of the shift laws and uniform polynomial Riemann sums. For p,q≤1, the difference from the transposed oriented formal kernel is the ordinary interval [max(0,q−p),q] after changing variables. Its length is min(p,q). Pure-sign terms agree in the coefficient window, while mixed terms already differ at degree two. Large shifts require the cutoff and cannot be recovered by continuing the oriented polynomial.

There is also a uniform explicit approximation of the infinite tail factors. Let k_* be the largest band index, take M_cut≥n Hardy modes, |z|≤Z real, and h=H(phi_−/phi_+). The Hilbert–Schmidt tail satisfies

```text
||h−P_(M_cut) h P_(M_cut)||_2
 ≤ |z| sqrt(H_N/2)
   sum_(s≥floor(M_cut/k_*)) (|z| H_N)^s/s!.
```

The weighted Fourier convolution norm proves this bound: the first omitted Hankel index is M_cut+1, so at least floor(M_cut/k_*)+1 Laurent factors are needed. Schatten Hölder bounds the induced trace-norm error for K. Interpolating the positive compressed determinants bounds each log-determinant error by delta^(−1) times that trace-norm error; the quotient costs at most twice this. Thus a prescribed number of bandwidth blocks gives factorial convergence uniformly in N on real compact intervals. The empty-band case is handled directly by K=0 and tail determinants one; k_* is not defined or used there.

These are controlled finite approximations to the exact factors. A routine evaluation of a formal polynomial is not a substitute. All source hypotheses and the real/complex distinction remain those of the [Round 13 source matching](director_petrov_round13.md).

[Exact Schur and truncation derivation](analytic102_petrov_positive_tail_reduction.md) · [Independent factor-order and cutoff check](geometry102_petrov_tail_qa.md) · [Third quantitative review](uniform110_rmt_quantitative_adjudication.md).
