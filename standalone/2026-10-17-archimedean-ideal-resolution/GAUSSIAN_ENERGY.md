# Full Gaussian energy: one logarithm and an explicit native asymptotic

Status: PROPOSED unconditional component proofs; no independent review. Same
fixed field, sources, characters and normalized hybrid average as PROOF.md.
Neither the column Gaussian nor either parameter tail is truncated in these
statements. Constants depend on the fixed k,c,K but are uniform in m>=2,
centers, masks and the fixed nonnegative row measure w.

## 1. Complete cumulative identity and quantitative error

Use the actual Gaussian

    W_c(y)=y^(-c)exp[-(log y)^2/4]/(2 sqrt(pi)), c real.

Define A_(t,l)(X,u) with this W for every X>0. At each scale expand its k-th
power by product IDEAL, retaining the infinite coefficient sum B_J(X,u).
Let

 E_(k,t,l)(D;w)=integral_0^D integral |A_(t,l)(X,u)|^(2k)dw dX/X^(k+1),
 Delta_k(D;w)=integral_0^D sum_J integral |B_J(X,u)|^2dw dX/X^(k+1).

All these are finite for fixed D and finite w; the estimates below include
the infinitely small scales. Put a_k=(k-1)^2.

**Theorem B.** For D>=2, R>=1,

    |<E_(k,t,l)(D;w)>_R-Delta_k(D;w)|
        <= C_(K,k,c) Z_w D^k/R^2 * log(3+D)^a_k,             (G1)

    Delta_k(D;w)<=C_(K,k,c) Z_w log(3+D)^(a_k+1).           (G2)

In particular

    <E_(k,t,l)(D;w)>_R <= C Z_w [log(3+D)^(a_k+1)
                              +(D^k/R^2)log(3+D)^a_k].    (G3)

For the scalar principal native source and fixed S,

    Delta_k(D) asymp_(K,k,c,S) log(D)^(a_k+1).              (G4)

It follows that at R>=D^(k/2), the COMPLETE averaged energy has that order,
and its relative difference from Delta_k is O_(K,k,c,S)(1/log D).
No individual fixed-(t,l) estimate is obtained.

### Proof: all Gaussian bands, with the off-diagonal error retained

Partition the positive norm axis by NI/X in (2^j,2^(j+1)], j in Z. Set
Y_j=2^(j+1)X. The supremum w_j of |W_c| on this interval satisfies

    w_j<=C_c exp[-c0 j^2+C_c |j|]                           (G5)

for an absolute c0>0. Any band with Y_j<1 is empty. Products of k such
bands are indexed by j-vector. Their product-ideal support is at most

    Y_vector=product_i Y_(j_i).

By the unequal-cap version of (19)--(22) in PROOF.md, the squared ell2 ideal
coefficient norm of this product, integrated in w, is at most

    C_k Z_w (product_i Y_(j_i))
           [1+log(2 max_i Y_(j_i))]^a_k product_i w_(j_i)^2. (G6)

The proof is unchanged: the two sides have the SAME vector of caps, and
(20) pays their complete convolution. A cap below one means an empty band.
The logarithm in (G6) is at most C log(3+X)(1+max_i(j_i)_+).
Minkowski in ell2(J;L2(w)), followed by the absolutely convergent band sum,
therefore gives for EVERY X>0

    sum_J integral |B_J(X,u)|^2dw
                <=C Z_w X^k log(3+X)^a_k.                 (G7)

Apply the polarized off-diagonal estimate (16) to two vector bands. Their
union product support lies below max(Y_vector,Y_vector'). Summing the
bounds by (G5),(G6) gives

 |<integral |A_(t,l)(X,u)|^(2k)dw>_R
                -sum_J integral |B_J(X,u)|^2dw|
        <=C Z_w X^(2k)/R^2 * log(3+X)^a_k, X>0.            (G8)

Every band pair occurs. The constants in the double Gaussian sum are
independent of X,R,m, and centers. In particular (G8) is not obtained by
throwing away cross-band terms or by assuming the energy increases when
coefficients are added. First apply the finite-band identity and these
summable bounds, then pass to the limit in the associated Hilbert spaces.
The full spectral average is justified in the same way by (14).

Integrating (G8) against dX/X^(k+1) on (0,D) proves (G1); the integral is at
most D^k log(3+D)^a_k/k. For (G2), use (G7) on X>=1. On X<1, absolute ideal
coefficient counting (18) and W_c(y)<<_(A,c)y^(-A) for y>=1 give

    |A_(t,l)(X,u)|<=C_(A,c) X^A sum_I t_m(I)/(NI)^A
                    <=C_(A,c) X^A, A>1.                 (G9)

For the diagonal, its coefficient ell2 norm is at most the coefficient ell1
norm of the k-th product, hence obeys the same 2k-th power bound. Choose
A>1. Integration on (0,1) is finite uniformly in every parameter above.
This proves (G2),(G3) including both parameter tails and the small-X tail.

For the native scalar source, every product-ideal coefficient has one Mobius
sign times a sum of positive Gaussian weights. W_c is bounded below by a
positive constant on [1/2,1]. The lower count in PROOF.md Section 4 therefore
bounds the exact diagonal below by c X^k log(X)^a_k at every large X.
Integrate to get (G4). Combine with (G1) to get the relative estimate. QED.

## 2. Explicit leading constant at second order

Write beta=2c-1, kappa_c=exp(beta^2/2)/(2 sqrt(2pi)). For k=1 the ideal
diagonal has the exact kernel

    Delta_1(D)=kappa_c sum_I |c(I)|^2/(NI)
                  Phi_N(log D-log(NI)-beta),              (G10)

where Phi_N is the standard normal distribution function. This follows by
putting r=log(X/NI) in the defining integral: the exponent is
beta*r-r^2/2, and the upper limit is log(D/NI). In particular the CDF shift
is MINUS beta. This agrees with the equal-ideal specialization of #952's
full pair kernel. We reconstruct it here, not claim it as new.

**Theorem C (one-log native asymptotic).** For the scalar native Mobius
source over K, fixed S, and every width function R=R(D)>=1 satisfying

    R(D)^2 log D / D -> infinity,

uniformly in all centers t0 real, l0 integer,

    <E_(1,t,l)(D)>_R ~ kappa_c delta_S log D,                (G11)

where

 delta_S= [Res_(s=1)zeta_K(s)]/zeta_K(2)
                              product_(p in S)(1+1/Np)^(-1)>0.

In particular R=sqrt(D) gives an O(1) error from the exact ideal diagonal
in (G10), which itself has the stated leading asymptotic. This replaces the
quadratic-field log-squared NORM block of #954 with a one-log IDEAL block,
under a DIFFERENT (radial plus angular) average of the actual source.

**Proof.** Eisenstein lattice counting gives
#ideals of norm<=x =a_K x+O(sqrt(x)+1), with a_K=pi/(3sqrt(3)).
The Dirichlet series for the nonnegative squarefree coefficients prime to S is

 zeta_K(s) H_S(s),
 H_S(s)=zeta_K(2s)^(-1) product_(p in S)(1+q^(-s))^(-1).

Its coefficient absolute mass at s=1 is finite. In the convolution with the
ideal-counting function, dominated convergence therefore gives

    sum_(NI<=x) mu_K(I)^2 1_(I,S)=1 =delta_S x+o(x).        (G12)

Specifically divide the convolution by x, dominate each term by C|h(d)|/Nd,
and take the limit for each fixed d. This supplies (G12) without RH, a prime
ideal theorem or a nonnegative-Tauberian shortcut for signed h.
Partial summation gives the harmonic prefix delta_S log D+o(log D).
Replacing its sharp cutoff by the CDF in (G10) changes it by O_(c,S)(1):
the harmonic mass in each fixed logarithmic unit interval is O(1), while
its CDF difference from 1_(NI<=D) has summably decreasing Gaussian tails
in the interval index. The fixed shift beta is harmless. Thus
Delta_1(D)~kappa_c delta_S log D. Now use (G1) and the displayed width
condition. Centers have never entered an absolute bound. QED.

### The actual coupled scalar source also has one logarithm

For the coupled source in (2), set a_p=1 outside fixed S and |b_p|=1. For each
fixed m>=2, its square-coefficient Dirichlet series has local factor

    1+(1-1/q)^2 q^(-s)+q^(m-2-ms).

Multiplication by 1-q^(-s) leaves a coefficient quotient of finite absolute
mass at s=1, uniformly in m: the degree-one discrepancy is -2/q+1/q^2,
whose weight is O(q^-2), and the powerful term at s=1 is q^-2. The density is

 delta_S,cpl=a_K product_(p in S)(1-1/q)
            product_(p notin S)(1-1/q)[1+(1-1/q)^2/q+1/q^2]. (G13)

It is positive and independent of m. The same dominated-convergence proof
and (G1) give (G11) with this density. The ASYMPTOTIC is stated for each
fixed m; no uniform convergence rate as m or S varies is asserted. Unit
powerful phases do not change the squared coefficients. This is compatible
with, and credits, #953's earlier square-density calculation.

## 3. Source-faithful price and the missing principal member

At fourth order the older norm-only Gaussian energy is bounded by
log^6 D+(D^2/T)log^5 D in #955. Here the full joint energy is bounded by

    log^2 D+(D^2/R^2)log D.

The effective number/length of parameters is R^2 rather than T. At R=D it
has the same power volume as T=D^2. Its smaller diagonal is obtained by
separating actual ideal locations, not by erasing the angular averaging.
At second order the comparison is log^2 D with T=D versus log D with
both widths sqrt(D). These are rigorous improvements of resolution and
logarithmic size for the stated new average, not comparisons of the same
functional.

All original physical rows may be retained via w, including sixth-power
rows. Averaging the added characters still does not control their principal
(t,l)=(0,0) values. The finite-order Hecke conclusion of #959 cannot justify
an infinite-order angular input, and neither Theorem B nor C needs it.
The unchanged fixed-center signed covariance is the remaining RH-bearing
arithmetic estimate. No new zero-free constant is asserted.

## 4. Fixed angular mode, with the exact projection price

The same positivity argument as PROOF Corollary D gives, for T>=1,

 integral_R g_T(t-t0) E_(k,t,l0)(D;w) dt
   <=C Z_w [T log(3+D)^(a_k+1)+(D^k/T)log(3+D)^a_k].       (G14)

This includes the original angular mode l0=0. If
T^2 log(3+D)<=D^k, the first term is bounded by the second, leaving
C Z_w D^k log(3+D)^a_k/T. It improves the logarithmic factor of #955's
same short radial average in that range. Outside the range, (G14) is only
an additional envelope; it is not claimed to dominate the earlier bound.
There is still no estimate for a single t. This corollary uses no new
arithmetic input beyond the full hybrid theorem and positivity of the
normalized Gaussian measure.
