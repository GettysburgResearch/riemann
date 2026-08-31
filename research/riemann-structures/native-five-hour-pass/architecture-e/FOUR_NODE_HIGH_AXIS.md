# Effective four-node positivity on the whole high safe axis

Status: PROPOSED theorem; final independent review pending. Bounded exact
replay and17 controls pass in ordinary and optimized Python.
Scope: literal completed Riemann xi, at most four nodes, every node at least
256, with arbitrary separation and all confluent limits. RH remains open.
What was run: the preregistered rational source-algebra replay, not numerical
Xi sampling. The theorem and domains were written before that acquisition.
Smallest remaining gap: independent verification of the finite-space bounds
below; the region containing a node below256 is not covered.

## 1. Source, normalization, and statement

Use the standard completion

    xi(s) = s(s-1) pi^(-s/2) Gamma(s/2) zeta(s) / 2,
    Y(x) = xi(1/2+x),       F(x) = Y'(x)/Y(x),
    H(x,y) = (F(x)+F(y))/(x+y),       C(x,y)=1/(x+y).

The safe real axis is x>1/2. The Euler product makes Y nonzero there;
F is holomorphic on Re x>1/2. This proof uses no zero census or RH premise.
The centered notation in the integrated packet is Xi(x)=Y(x), whereas
Fourier-coordinate Xi is X(z)=xi(1/2+iz); hence Y(x)=X(ix) by reflection.
These coordinate conventions must not be interchanged in derivative signs.

**Theorem E4.** For1<=n<=4 and arbitrary real x_1,...,x_n>=256,

    [H(x_i,x_j)] >= (1/4)[C(x_i,x_j)]                         (E4.1)

in the Hermitian positive-semidefinite order. Distinct-node matrices are
positive definite. More strongly, (E4.1) holds after Newton divided-difference
congruence and extends to arbitrary partial or full confluence, counting
total jet dimension rather than just the number of distinct node values.

For four distinct nodes put H_3=[H(x_i,x_j)]_(i,j<=3),
h=(H(x_i,x_4))_(i<=3), and

    S_4 = H(x_4,x_4)-h* H_3^(-1) h.

Then

    S_4 >= 1/(8x_4) product_(i=1)^3 ((x_4-x_i)/(x_4+x_i))^2. (E4.2)

If the fourth Newton row is divided by product_(i<4)(x_4-x_i),
its Schur residual obeys the nonvanishing bound

    S_4^Newton >= 1/[8x_4 product_(i<4)(x_4+x_i)^2].           (E4.3)

This extends continuously to repeated nodes. At complete confluence x,
the lower bound is1/(512x^7), using derivatives divided by their factorials.
No finite sample is used to establish these universal quantifiers.

## 2. Exact finite source space, including collisions

For a list of positive nodes with repetitions, let E be the span of
t^k exp(-xt) for each distinct x and0<=k<its multiplicity, in L2(0,infinity).
Its dimension is the list length n. The operator A=-d/dt leaves E invariant.
There is no assumed closed operator F(A_0) on the ambient infinite space.
Only ordinary finite-dimensional holomorphic functional calculus on E is
used; its eigenvalues lie in Re x>1/2.

For j=1,...,n define a real function phi_j by its Laplace transform

    L phi_j(z) = sqrt(2x_j)/(z+x_j)
                 product_(k<j) (z-x_k)/(z+x_k).               (E4.4)

These functions form an orthonormal basis of E. Here is a direct proof.
Each factor (z-x_k)/(z+x_k) has modulus1 on the imaginary axis, so Laplace
Plancherel gives norm1. The numerator zeros at preceding nodes, with their
multiplicities, make phi_j orthogonal to all preceding exponential jets:
inner products with t^k exp(-xt) are signed derivatives of L phi_j at x.
Partial fractions show phi_j belongs to the first j-node jet space.
The leading z^(-1) coefficient also gives phi_j(0)=sqrt(2x_j).

In this basis A is the upper triangular matrix

    A_ii=x_i,       A_ij=2sqrt(x_i x_j) for i<j,       A_ij=0 for i>j. (E4.5)

Indeed nested spaces are invariant and the new quotient eigenvalue is x_j.
Integration by parts gives A+A*=bb*, b_i=sqrt(2x_i), fixing every upper entry.
In particular Re A>=0, even though its smallest numerical real part is zero
when n>1. Coincident eigenvalues cause no singularity in (E4.4)--(E4.5).

For an ordinary packet g=sum c_i exp(-x_i t), direct integration gives

    2 Re <F(A)g,g> = sum_(i,j) c_i conjugate(c_j) H(x_i,x_j),
    ||g||^2       = sum_(i,j) c_i conjugate(c_j) C(x_i,x_j).   (E4.6)

For jets differentiate these identities in the node variables, with the
same factorial normalization on both sides. It is therefore enough to prove
Re F(A)>=1/8 on every E of dimension at most4 with minimum node R>=256.

## 3. Resolvent and logarithmic term without spacing loss

For real t with no denominator zero, direct upper-triangular inversion gives

    [(A+t)^(-1)]_ii=1/(x_i+t),
    [(A+t)^(-1)]_ij=-2sqrt(x_i x_j)/[(x_i+t)(x_j+t)]
                     product_(i<k<j) (t-x_k)/(t+x_k), i<j.   (E4.7)

Induction on j-i proves the formula; alternatively substitute it into both
matrix products. It is an identity, not an asymptotic resolvent expansion.

For c>=0 the principal logarithm has diagonal log(x_i+c) and off-diagonal
entries minus the integral from0 to infinity of [(A+c+t)^(-1)]_ij.
Every intermediate product has absolute value<=1. Thus

    |[log(A+c)]_ij|
       <=2sqrt(x_i x_j) integral_0^infinity
                         dt/[(t+x_i+c)(t+x_j+c)] <=2.         (E4.8)

The last inequality follows from the logarithmic mean exceeding the
geometric mean: sqrt(ab) log(b/a)/(b-a)<=1. At a=b use the continuous limit.
For a proof set b/a=r^2 and integrate
d/dr[r-r^(-1)-2log r]=(r-1)^2/r^2>=0 for r>=1.

Each row of Re log(A+c) has at most n-1 off-diagonal entries of modulus<=1.
Consequently

    Re[ (1/2)log((A+c)/(2pi)) ]
       >= [(1/2)log((R+c)/(2pi))-(n-1)/2] I.                 (E4.9)

This is uniform for arbitrarily large node ratios and for colliding nodes.
It is not obtained from a minimum separation or a Vandermonde condition number.

## 4. Literal Euler-prime and digamma decomposition

Logarithmic differentiation of the stated completion, with c=1/2, gives

    F(x)=1/(x-c)+1/(x+c)-(log pi)/2
          +(1/2)psi((x+c)/2)-sum_(m>=2) Lambda(m)m^(-x-c).

The prime-power coefficient is the literal von Mangoldt value Lambda(p^k)=log p,
and is zero otherwise. It is not replaced in this identity by all integers.
The classical digamma integral yields

    q(t)=1/(1-exp(-t))-1/t,       0<q(t)<1 for t>0,
    F(A)=(1/2)log((A+c)/(2pi))+(A-c)^(-1)+(A+c)^(-1)
          -integral_0^infinity q(2t) exp(-ct) exp(-tA) dt
          -sum_(m>=2) Lambda(m)/sqrt(m) exp[-(log m)A].        (E4.10)

The bounds on q follow from1-exp(-t)<t and exp(t)-1>t. The integral is the
exact gamma remainder, not a fitted expansion. The final terms are the exact
right shifts g(t)->g(t+log m) on E. Formula (E4.10) is also the literal source
decomposition of the Schur residual: substitute its minimizing packet
g=sum_(i<=3)(-H_3^(-1)h)_i exp(-x_i t)+exp(-x_4 t) into (E4.6).

We now bound the remainders uniformly; only at this bounding stage is the
prime-power sum majorized by an all-integer series.

### Rational terms

Since Re A>=0, Re(A+c)^(-1)>=0. Put R_-=(A-c)^(-1). The exact identity

    Re R_-=R_-* (Re A-cI) R_- >= -c R_-*R_-                 (E4.11)

is essential: a positive scalar rational function need not have a positive
real part on this nonnormal matrix. For x_i>=R>c set

    Q=(R+c)/(R-c),
    J_n(R)=1/(R-c)+2R/(R-c)^2 sum_(j=0)^(n-2) Q^j.

The empty sum is0. Formula (E4.7) bounds both absolute row and column sums of
R_- by J_n(R), hence ||R_-||<=J_n(R). For n<=4,R>=256,

    J_n(R)<=J_4(256)<1/32.                                  (E4.12)

All factors used in this majorant decrease with R, so checking R256 suffices.

### Gamma remainder

For i<j expand [exp(-tA)]_ij over increasing paths
i=i_0<i_1<...<i_k=j by finite upper-triangular Duhamel expansion. A path is
(-1)^k product A_(i_l,i_(l+1)) times the convolution of the k+1 functions
exp(-x_(i_l)t). This is a finite identity, valid also at repeated eigenvalues.
Its weighted absolute integral is bounded by the same product divided by
product(x_(i_l)+c). Summing all subsets of intermediate indices gives

    integral_0^infinity exp(-ct)|[exp(-tA)]_ij|dt
       <=2sqrt(x_i x_j)/[(x_i+c)(x_j+c)]
                        product_(i<k<j)(1+2x_k/(x_k+c))
       <=2*3^(j-i-1)/(R+c).                                (E4.13)

For diagonal entries the bound is1/(R+c). Since0<q(2t)<1, both absolute
row and column sums of the gamma remainder are at most

    [1+2 sum_(j=0)^(n-2)3^j]/(R+c)=3^(n-1)/(R+c).

Its operator norm is therefore at most27/(R+c) for n<=4. This bound retains
all signs in (E4.10); no positivity of the gamma matrix is assumed.

### Prime remainder

The inverse Laplace form of (E4.4) is the convolution of sqrt(2x_j)exp(-x_j t)
with the j-1 signed measures delta_0-2x_k exp(-x_k t)dt. For a=R/2, weighted
Young's inequality gives

    ||exp(at)phi_j||_2 <=sqrt(2)*5^(j-1),
    ||exp(at)g||_2 <=[2 sum_(j=0)^(n-1)25^j]^(1/2)||g||_2.

For n<=4 the square bracket is32552<181^2. Thus every right shift on E obeys

    ||exp(-tA)||<=181 exp(-Rt/2).                            (E4.14)

This estimate, though deliberately loose, is independent of node separation.
At R>=256, using Lambda(m)<=log m<=m gives

    ||prime remainder||
       <=181 sum_(m>=2) Lambda(m)m^(-(R+1)/2)
       <=181 sum_(m>=2)m^(-127)
       <=181[2^(-127)+2^(-126)/126] <2^(-118)<1/1024.         (E4.15)

The integral test proves the penultimate bound. The absolute operator series
therefore converges on this finite space; no global bounded shift series is
being asserted.

## 5. Exact numerical constants and proof of the theorem

All numerical comparisons reduce to rational arithmetic. The classical bound
pi<22/7 follows by integrating the positive function
x^4(1-x)^4/(1+x^2) on(0,1), whose integral is22/7-pi. The positive exponential
Taylor series at7/2 through degree16, with geometric tail beginning at17,
gives exp(7/2)<34. Finally3591/88>34. Hence

    (R+1/2)/(2pi) >=(256+1/2)/(2pi)>3591/88>exp(7/2),
    (1/2)log((R+1/2)/(2pi))-3/2 >1/4.

Combining (E4.9)--(E4.15), without dropping either negative source remainder,

    Re F(A) > [1/4-27/256-1/2048-1/1024] I
            =293/2048 I >1/8 I.                            (E4.16)

Equation (E4.6) proves (E4.1). The same operator proof applies directly to
every repeated-node exponential-jet space, so no ill-conditioned limiting
matrix estimate is needed to establish confluence.

For completeness, Schur complements are minima of quadratic forms with the
last coefficient fixed to1. Minimizing (E4.1) yields
S_4>=Cauchy_Schur/4. The exact Cauchy determinant gives
Cauchy_Schur=(2x_4)^(-1)product_(i<4)((x_4-x_i)/(x_4+x_i))^2.
Newton congruence divides this by product_(i<4)(x_4-x_i)^2; its continuous
limit is the Gram determinant ratio of the exponential jets. This proves
(E4.2)--(E4.3), including partial and full collisions.

## 6. Provenance and limits

The integrated order-three statement is
`research/integrated/xi_pick/ORDER_THREE_CANONICAL.md`, at the starting head
`9421846721cd788ab01615c8b6d459d9de849df7`. Its source manifest also records
older fixed-order high-axis asymptotics. They are prior work, not new results
of this packet. The present claimed addition is an explicit R256, all-node-
ratio, confluent four-packet coercivity bound with the literal gamma and Euler
remainders paid. It does not close the complete four-node safe-axis problem.

The exact PR765 source boundary is
`8f01064df805624c045877655893c324a220975d`, companion/cancellation source
`research/exploratory/XI_COMPANION_GENERIC_PARAMETER_COPRIMALITY.md`, blob
`797f7b581580ad5a441c7702015c64a53eca6f4d`.
The PR783 index boundary is
`9497db89e34669e2167c632c918c491bf6ee73ab`,
`research/exploratory/prs-765-766-770-781-proof-review/GENERALIZED_SCHUR_ZERO_INDEX.md`,
blob `5e120b6bae9d65e5a90c63716f1c1382839bb3bf`.
Neither theorem is used to infer a new zero count here.

Classical analytic inputs are the standard completion
<https://dlmf.nist.gov/25.4.E4>, the Euler product and its absolutely convergent
logarithmic derivative on Re s>1, and the digamma integral
<https://dlmf.nist.gov/5.9.E13>. Laplace Plancherel, finite matrix calculus,
Young's inequality and Cauchy determinants are used with proofs or exact
reductions stated above. The exponential orthogonalization is classical
Malmquist-system algebra; no external novelty or priority claim is made.

The bounded exact replay checks rational constants, source identities and
finite algebra controls. It cannot by itself certify the analytic integral
identities, all-node estimates, or the theorem's universal quantifiers.
