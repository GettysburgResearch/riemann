# A hybrid bound for the complete low-cubic-core dual sector

**PROPOSED source-qualified component estimate.** This
concerns the exact squarefree-column source in
`SQUAREFREE_COLUMN_ADAPTER.md`. Every shared COLUMN prime, every physical
sixth-free row and every introduced collision correction is included.
It does not yet combine the outer all-power components of that adapter,
or estimate the complementary dual frequencies. No zeta improvement is
claimed.

All ideals below are good Eisenstein ideals, with fixed primary/ray
conventions, except the primitive dual frequencies whose bad-prime
parts are explicitly included below. The imports are primitive planar Poisson, the quadratic
ideal large sieve on squarefree rows and columns, and the cubic ideal
large sieve on squarefree rows and columns. The latter two have their
usual divisor-subpower losses. The complete input and zero conventions
are those already reconstructed in the column adapter and
`POWERFUL_GAUSS_PROJECTION.md`.

The precise primary sieve pins are Goldmakher--Louvel,
[arXiv:1112.1642v1](https://arxiv.org/pdf/1112.1642v1), Definition 1.1
and Theorem 1.4 (PDF pages 1--2), with its Corollary 1.5 for the cubic
power of a sextic Hecke family; and Blomer--Goldmakher--Louvel,
[arXiv:1112.1650v1](https://arxiv.org/pdf/1112.1650v1), Theorem 1.3
at order three. In the fixed primary convention the quadratic family
verification is exactly the one in the pinned original source's
`eq:quadratic-sieve` and following paragraph: subdivide into its finite
primary square classes, use the primitive inducing characters, and
retain the original zero extensions. The fixed bad-prime adjustments
change only finitely many classes. Primitive planar Poisson is the
same GL1 formula pinned in BGL Lemma 2.2. Masks below enter its bounded
column coefficients or its positive row restrictions; they do not
change the fixed family in these theorems.

## 1. Exact source and the selected dual sector

Put L=DN, with D,N in fixed polynomial ranges relative to U and at least
a fixed positive constant. Consider the actual squarefree-column vector

    F_u=sum_A beta_A chi_A(u),
    beta_A=L^(-1/2) nu(A)
       sum_(ab=A,a,b squarefree,(a,b)=1,(ab,Q)=1)
                         mu(a)W_M(Na/D)W_S(Nb/N).         (1)

Its columns A are squarefree and have norm comparable to L. All common
height factors and fixed ray components may be included in the smooth
profiles. A fixed original row mask (u,Q)=1 is permitted and retained.
The moment is on ALL original sixth-free physical rows Nu comparable
to U, in their compact shape/ray classes, with a fixed smooth weight.

Open the moment, write A1=R x,A2=R y with R their full gcd, and retain
(x,y)=1 and (xy,RQ)=1. The pair character is primitive on C=xy, with
the zero-only row mask RQ. The C=1 diagonal is paid separately at
O(U^(1+epsilon)). Here and below the coefficient divisor bounds can
absorb fixed powers of logarithms.

Expand sixth-freeness EXACTLY by
`1_sixth-free(u)=sum_(d^6|u)mu(d)`. Its original column zero extension
imposes (d,A1A2)=1. Expand the remaining row mask by b|RQ. Primitive
Poisson then has prefactor and dual norm scale, on the R dyad,

    U/[(Nd)^6 Nb M],  M=L/NR,
    H=M^2 (Nd)^6 Nb/U.                                 (2)

All these d and b are retained. Its primitive Gauss factor is, in each
fixed ray sector, gamma_1(x) times conjugate(gamma_1(y)), up to separated
unit factors. The ratio CRT phase is fixed-ray; the within-column cubic
CRT phase remains. Equivalently, expressing these Gauss factors using
the ORIGINAL columns requires the correction theta(R)^(-2). Using x,y
directly as here retains that correction without a spurious zero at R.

For each nonzero dual ideal h uniquely write

    h=j^3 v,   v cubefree.                              (3)

Let P_(<=V) be the COMPLETE signed Poisson contribution with Nv<=V,
summed over every R,d,b, every such v,j, all original source columns,
and all profile tails. It is not a subset selected from a positive
square. Assume V>=1 and polynomially bounded.

The proposed estimate is

    |P_(<=V)| <<_epsilon (UDNQV)^epsilon
       { U^(2/3)V^(2/3)
          +U^(5/6)[D^(1/3)+N^(1/3)+(DN)^(1/6)]V^(5/6) }.
                                                               (4)

It is uniform under the original common smooth parameters, with their
fixed seminorm/height factors. At D=U,N=sqrt(U), this becomes

    |P_(<=V)| << U^(7/6+epsilon)V^(5/6+epsilon)
                         +U^(2/3+epsilon)V^(2/3+epsilon). (5)

In particular V=U^(1/25) fits U^(6/5+epsilon). The complete Nv>V
signed term remains OPEN.

## 2. Two coefficient resources, including every shared divisor

Remove (x,y)=1 by its EXACT finite Mobius projector. For a fixed
projector k, write x=k c1,y=k c2. The displayed Poisson expression is
extended algebraically before projecting; its artificial pairs are
not asserted to have that primitive conductor. The projector returns
exactly the original coprime pairs. Squarefreeness retains (k,ci)=1.
The common k character gives only its original zero mask on h.

The new column length is M/Nk. For every fixed row twist, input mask,
norm/angle Fourier mode and fixed R,k, the coefficient vector has

    A_(Rk):=sum_c |coefficient_c|^2
                  <<_epsilon (LNRNk)^epsilon/(NR Nk).    (6)

Indeed |beta_A|<=tau(A)/sqrt(L), and there are O(L/(NR Nk)) available
columns. The shifted input masks only remove terms from this estimate.

There is also a POINTWISE Gauss-projection estimate for this actual
factorized coefficient, uniformly in every multiplicative row twist
and every input coprimality mask:

    |sum_c coefficient_c gamma_1(c)chi_c(z)|^2
       <<_epsilon (LNRNkNz)^epsilon/(NR Nk) * C_(Rk),
    C_n=sum_(n_a n_b=n, n_a<=C D,n_b<=C N)
           [D/Nn_a+N/Nn_b+(L/Nn)^(2/3)].                 (7)

The letter C in the cutoffs denotes fixed support constants. To prove
(7), allocate each prime of Rk to its unique one of the two coprime
original input factors. Write a=n_a a',b=n_b b'. The outside
normalization is 1/sqrt(N(Rk)). The remaining lengths are D/Nn_a,
N/Nn_b. Multiplicativity and sextic reciprocity turn gamma_1(a'b')
into gamma_1(a')gamma_1(b')chi_(a')(b')^2, up to separated fixed phases.
Its cubic symbol already vanishes at shared nonunits. Cubic large
sieve and Cauchy give precisely the bracket in (7). All moving
characters and masks separate into the two factors, so they remain
bounded coefficients. Cauchy over the divisor-many allocations proves
(7). This is a factorized-source estimate, not an arbitrary-column
operator estimate.

## 3. The all-power j issue and the necessary hybrid estimate

For fixed v,d,b,R, h=j^3v has Nj on the scale J=(H/Nv)^(1/3).
The character in j is quadratic, but j is NOT squarefree. Applying a
squarefree quadratic sieve directly to it would be false. Write

    j=t^2 r,   r squarefree.

The t,r may share primes. Its character equals the quadratic character
of r times the original column mask (column,t)=1. That mask is kept.
At each fixed t, quadratic large sieve and (6) give

    << [J/(Nt)^2+M/Nk] A_(Rk).

Pointwise (7), followed by counting all r on that dyad, gives instead

    << J/(Nt)^2 * B_(Rk),
    B_(Rk)=(NR Nk)^(-1+epsilon) C_(Rk).

Taking the better bound and summing ALL square indices uses the
elementary ideal-count inequality

    sum_t min(X,Y/(Nt)^2) << sqrt(XY),   X,Y>0.

The result is

    << J A_(Rk)+sqrt((M/Nk) J A_(Rk) B_(Rk)).            (8)

This includes the square replicas r=1. Their Gauss projection is paid
by (7); they were not discarded or assigned artificial cancellation.

## 4. Complete R,k,d,b,v resource

Multiply the first term of (8) by (2). Up to subpowers its resource is

    U^(2/3)L^(-1/3)
       (Nd)^(-4)(Nb)^(-2/3)(NR)^(-2/3)(Nk)^(-1)(Nv)^(-1/3).

The k sum is harmonic; the R sum through O(L) costs L^(1/3+epsilon).
The d sum converges, the b divisor sum costs (RQ)^epsilon, and the
v sum through V costs V^(2/3+epsilon). This gives the first term of (4).

The second term of (8) has resource

    U^(5/6)L^(-1/6)
       (Nd)^(-5)(Nb)^(-5/6)(NR)^(-5/6)(Nk)^(-3/2)
                                    (Nv)^(-1/6)sqrt(C_(Rk)). (9)

Set n=Rk. Its divisor weight is
`(Nn)^(-5/6)(Nk)^(-2/3)`, so summing all k|n costs a subpower.
Use sqrt(sum positive terms)<=sum sqrt(terms), then sum all actual
input allocations. The remaining complete resource is at most

    sqrt(D) sum_(n_a<=C D)(Nn_a)^(-4/3)
                sum_(n_b<=C N)(Nn_b)^(-5/6)
     +sqrt(N) sum_(n_b<=C N)(Nn_b)^(-4/3)
                sum_(n_a<=C D)(Nn_a)^(-5/6)
     +L^(1/3) sum_n tau(n)(Nn)^(-7/6)

    <<_epsilon (DN)^epsilon
                   [sqrt(D)N^(1/6)+sqrt(N)D^(1/6)+L^(1/3)].

The d series in (9) converges, every b divisor is included, and the
v sum costs V^(5/6+epsilon). Multiplying by L^(-1/6) proves the second
term of (4).

The algebraic coprimality extension includes the formal pair x=y=1.
It is subtracted explicitly from the nonprincipal sector. Its nonzero
Poisson-frequency contribution costs O(U^(1/6+epsilon)): the smooth
lattice bound cancels its Poisson prefactor, there are O(U^(1/6))
sixth-power sieve indices, and sum_R |beta_R|^2 is a subpower.
This is absorbed by (4). The true principal diagonal was already paid
separately at U. No artificial collision has been silently kept as a
lower bound or dropped as zero.

## 5. Profiles, tails and present limit

On every dyad the primitive Fourier kernel has rapid decay outside
the scale (2). Mellin separation of its norm ratios, and angular Fourier
separation for a nonradial physical profile, have finite weighted L1
cost at fixed seminorm orders. After the k-projector the kernel still
uses the ORIGINAL x,y norms, with x=k c1,y=k c2. Its ratios Nx/M and
Ny/M lie in the SAME fixed compact annuli as before that projector;
the new coefficient lengths are M/Nk. Separating those original
ratios therefore inserts bounded norm powers into BOTH coefficients
at their shortened lengths. Likewise the angular ratios have fixed
seminorm control. No primitive kernel for an artificial pair is
substituted, and there is no uncharged norm- or angle-profile loss.
Cauchy separates the two conjugate
coefficient modes before (6)--(8). Their phases are bounded and their
source-factor profiles retain the same complete resources. Summing
the rapidly decreasing dyads gives the H powers used above; if H/Nv<1,
all nonzero j are in that same rapidly decreasing tail. Thus no
uncontrolled short-frequency or large-frequency range is omitted.

Primitive dual frequencies can include primes of the fixed bad set S
and the fixed trace-dual lattice denominators. Clear the fixed
denominators first, which changes only fixed norm/ray constants. In
h=j^3v write j=j_S j_good and v=v_S v_good. The cubefree v_S has only
finitely many patterns. Each j_S is S-smooth, contributes a bounded
multiplicative column twist, and replaces J by J/Nj_S. The resources
in (8) are proportional to J and J^(1/2); their complete j_S sums
are bounded by the convergent finite-prime geometric series at
exponents one and one half. The bilinear mixed term, when used, has
J^(3/4) and the same argument at exponent three quarters. This retains
EVERY bad-prime frequency and all fixed dual-lattice/ray classes.

The result applies to one COMPLETE squarefree-column source (1), not
merely a pairwise-coprime slice of its expanded moment. It includes
all shared-column R and all collision/projector terms. Combining the
outer g,h decomposition of the original all-power vector still needs
an explicit bilinear cross-component version: a signed dual-sector
projection does not automatically commute with its outer Minkowski
norm bound. Nor has the complete Nv>V sector been bounded. These
remaining requirements prevent (4) from being a full mixed-mean or
zero-free theorem.
