# Domain completion: a finite Toeplitz hierarchy and a controlled source cutoff

Status: PROPOSED COMPONENT PROOFS; the all-rank completion estimate is OPEN.
Conventions and actual d_b,N_a,V_a are those of CONSTRUCTION.md.
All quantities below use the original L2(0,infinity) metric.

## 1. One prescribed finite hierarchy

Fix eta>0. Let phi_j=R_eta^j d_b, 0<=j<=N, and define the Hermitian Gram

    (G_N)_(j,k)=integral conjugate(phi_j(t))phi_k(t)dt.

Since R_eta has unimodular multiplier, G_N is Toeplitz:

    (G_N)_(j,k)=(1/(2pi))integral |D_b(iy)|^2
                                  r_eta(iy)^(k-j)dy.  (D1)

The entries are real for this real source (pair y with -y). Every finite
G_N is strictly positive definite: a nonzero polynomial in r_eta cannot
vanish on a positive-measure part of the boundary, while D_b is nonzero a.e.
This positivity is unconditional and by itself says NOTHING about RH.
The corresponding output Gram from R_eta^j n_a is exactly the same matrix.

Set u_eta(t)=sqrt(2eta)exp(-eta t), of norm one. Reproduction gives

    <phi_j,u_eta>=sqrt(2eta)D_b(eta)  if j=0,
                 0                  if j>0.           (D2)

Consequently the squared least-squares error is exactly

    eps_N(b;eta)=dist(u_eta,span(phi_0,...,phi_N))^2
       =1-2eta D_b(eta)^2 (G_N^{-1})_(0,0)
       =1-2eta D_b(eta)^2 Delta_(N-1)/Delta_N,         (D3)

where Delta_N=det G_N and Delta_(-1)=1. The cofactor formula uses the
Toeplitz property; it is not an approximation to the inverse. These errors
are nonnegative and decrease with N.

## 2. The exact missing limit

CONSTRUCTION identifies the closed source space as B_b H2. The orthogonal
projection of the Hardy reproducing kernel at eta onto that subspace has
squared norm |B_b(eta)|^2/(2eta). One can verify this directly: M_B is an
isometry and M_B^*k_eta=conjugate(B(eta))k_eta. Therefore

    lim_(N->infinity) eps_N(b;eta)=1-|B_b(eta)|^2.     (D4)

It follows, without an inverse-stability assumption, that

    eps_N(b;eta)->0
        iff zeta has no zero in Re w>b.              (D5)

For the predetermined sequence b_j=1/2+2^(-j-2), proving this limit for
every j would exclude every zero right of 1/2. Functional-equation reflection
then gives RH. Conversely RH makes every D_b outer and proves all these
limits by the Hardy cyclicity theorem. This is a Nyman--Beurling/Szego-type
criterion in explicit factorial-source coordinates, NOT a proof of the limit.

There is also a SINGLE-source version: the construction of d_b and its
inner-factor analysis remain valid at b=1/2. Thus eps_N(1/2;eta)->0 for one
fixed eta>0 is equivalent to RH. This does not use the degenerate a=0 Xi
quotient as a detector; it uses cyclicity of the source D_(1/2), whose
interior zeros are exactly the right-of-line zeta zeros.

An actual zero lambda=rho-b with Re lambda>0 gives for every N

    eps_N >= 1-| (eta-lambda)/(eta+conjugate(lambda)) |^2
           =4eta Re lambda/|eta+conjugate(lambda)|^2. (D6)

For multiplicity m use 1-|b_lambda(eta)|^(2m), and for any finite collection
use the product of these moduli. This follows either from the inner divisor
or direct evaluation orthogonality. It contains no simplicity hypothesis.
A small finite error bounds possible zeros in a bounded region; it is not
zero error and cannot exclude arbitrary heights.

## 3. Integer cutoff error: uniform in filter order

Let d_b^T=d_b 1_[0,T]. The elementary bound g<=1+t yields

    ||d_b-d_b^T||_2 <= e_T,
    e_T^2=exp(-2bT)[(1+T)^2/(2b)+(1+T)/(2b^2)+1/(4b^3)].
                                                        (D7)

Apply the same R_eta filters to d_b^T and let G_N^T be their Gram. Since
every power of R_eta is an isometry, every Gram-entry error is at most
2U_b e_T. Hence

    ||G_N-G_N^T||_op <=2(N+1)U_b e_T.                (D8)

At T_N=(2/b)log(N+2), this is O_b(log(N+2)/(N+2)). The largest integer needed
to define d_b^T is at most (N+2)^(2/b). Thus the source cutoff can grow
polynomially in rank; no prime/zero census defines these matrices.
This estimates arithmetic truncation error, NOT the conditioning of G_N.

In particular one must not pass (D8) through G_N^{-1} without a separate
smallest-eigenvalue bound. A safe alternative is to evaluate a proposed
coefficient vector c directly. Put V_N c=sum c_j phi_j and V_N^T similarly.
Then

    ||u_eta-V_N c||_2
      <=||u_eta-V_N^T c||_2+sqrt(N+1)e_T||c||_2.      (D9)

This displays the coefficient cost that cannot be discarded. Neither (D8)
nor (D9) currently proves eps_N->0.

### Exact finite-entry prescription

The stable filter has the finite impulse formula

    R_eta^j=I+sum_(k=1)^j binom(j,k)(-2eta)^k
                      [t^(k-1)exp(-eta t)/(k-1)!]*.

On [log n,log(n+1)) the source is exp(-bt)(n+log(n!)-nt).
All truncated entries in (D1) are therefore finite integrals of polynomial
exponentials over explicitly known logarithmic cells. Endpoints and initial
filter states must be propagated; setting filter tails to zero is NOT the
prescription. Equivalently use Toeplitz entries <d_b^T,R_eta^j d_b^T>, for
which the first factor already vanishes beyond T. The accompanying directed
source checker implements the N=0 case, not a high-rank matrix campaign.

## 4. A fully explicit positive-source obstruction to a false completion

The following is a SYNTHETIC CONTROL, not zeta and not an Euler product:

    d(t)=exp(-t)(2t-1)^2 >=0,
    n(t)=exp(-t)(1+2t^2) >0.

Their transforms are

    D(z)=(z^2-2z+5)/(z+1)^3,
    N(z)=(z^2+2z+5)/(z+1)^3.                          (D10)

Both functions are causal and in L1 intersection L2. Their boundary moduli
are equal. Thus the full isometric construction (C12) applies to them too.
The input has zeros at 1+/-2i; the output is outer. The source inner factor is

    B(z)=(z^2-2z+5)/(z^2+2z+5).

At eta=1, B(1)=1/2 and Theta(1)=N(1)/D(1)=2. Hence

    lim eps_N=3/4,   K_Theta(1,1)=-3/2.             (D11)

For eta=1 the exact Toeplitz matrix is especially transparent: main diagonal
9/2, adjacent diagonals -3, second diagonals 1, others zero. It is the Gram
of the disk polynomial (1-2w+2w^2)/sqrt(2) and all its shifts, so every finite
matrix is strictly positive. Here D(1)=1/2 and eps_N=1-(1/2)(G_N^-1)_(0,0).
The first errors are eps_0=8/9, eps_1=4/5, and all converge to 3/4, not zero.
The disk roots have modulus sqrt(1/2)<3/4. On |w|=1, factoring the quadratic
therefore gives |1-2w+2w^2|>1/8, so every G_N is in fact bounded below by
(1/128)I, uniformly in rank. Its operator norm is at most 25/2 by its row
sums. Even this uniform coercivity does not make the domain complete.

This example has TWO positive causal sources, equal norms and all equal
polarized shift Grams. It shows that these properties, even together, do not
establish cyclicity or critical Schur positivity. It is not a refutation of
cyclicity of the actual factorial source.

## 5. Where the literal arithmetic reappears in an inverse construction

For Re(z+b)>1, exact Dirichlet inversion gives

    1/D_b(z)=[(z+b)^2/(z+b-1)]sum_n mu(n)n^(-b-z).

The retarded inverse distribution is locally finite and explicit:

    ell_b=sum_n mu(n)n^(-b)
        [delta'_(log n)+(b+1)delta_(log n)
                  +1_(t>=log n)exp((1-b)(t-log n))].  (D12)

Indeed w^2/(w-1)=w+1+1/(w-1). Formal convolution d_b*ell_b=delta_0 is
legitimate in the algebra of causal distributions (finitely many atoms on
compact intervals; the remaining causal densities have exponential order).
It does not imply that ell_b is a bounded operator in H.

For the target exp(-t), its regular part contains exactly

    exp((1-b)t)/(2-b) sum_(n<=exp t) mu(n)/n
     -(1-b)^2 exp(-t)/(2-b) sum_(n<=exp t)mu(n)n^(1-b),

in addition to sum mu(n)n^(-b)delta_(log n). This follows from the rational
identity

    (z+b)^2/[(z+b-1)(z+1)]
      =1+1/[(2-b)(z+b-1)]-(1-b)^2/[(2-b)(z+1)].       (D13)

Thus the inverse is not a positive synthesis and not an L2 vector. Its
finite truncations need real cancellation estimates before they can prove
(D5). The standard mu*zeta coefficient identity alone supplies no such norm.

## 6. Status

The causal map and its norm on its domain are supplied, and its finite input
Gram has a complete tail estimate. The source-domain limit (D5), or a direct
full-domain contractivity estimate for k_a, remains open. Positive definite
finite Gram matrices, formal convolution inversion, and a small-time bound
are each insufficient. No limit is justified by a finite numerical trend.
