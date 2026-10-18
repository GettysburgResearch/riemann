# A signed quadratic-sieve bound for the complete cube-tilted family

Status: **PROPOSED component theorem using the pinned reflection interface.**
This is a new upper estimate for the exact arithmetic deformation in
CUBE_TILT.md, with an explicit loss. It does not preserve the original CT
exponent and does not establish a new zero-free region.

Fix the same field and complete native source. All constants may depend
on the fixed field, local classes and profiles. The imported ingredients
are the original exact reflected expansion with its two Euler derivatives,
the quadratic ideal large sieve, and its summable higher-power majorants,
as stated in the pinned CT `prop:reflection`, `eq:separated-reflection`,
`eq:quadratic-sieve`, `eq:beta`, and `prop:moment`. The original OpenAI
source is commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a,
[04-reflection.tex](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/04-reflection.tex).
No stronger sieve or random-phase assertion is imported.

## 1. The arithmetic quadratic convolution lemma, with every shared prime

Let rows d be squarefree exterior ideals with Nd<=D. Let n range over
ALL exterior ideals in [N,2N), and let c be squarefree with Nc in [C,2C).
For arbitrary coefficients |a(n)|<=1/N and |b(c)|<=1/sqrt(C),

    sum_d^flat |sum_(n~N,c~C)^flat a(n)b(c) chi_d(nc)^3|^2
            <<_epsilon (NCD)^epsilon [D/N+C].          (1)

The flat condition in the inner sum applies only to c, not n. Fixed row
unit phases and arbitrary fixed masks may be inserted whenever they
separate after the decompositions below. In particular masks at primes
shared with n or c are retained by the original zero extension.

Here is the full squarefree-core proof, rather than a sieve applied to a
non-squarefree column. Write uniquely n=a^2 b with b squarefree; a,b may
share primes. Put e=gcd(b,c), b=e b1,c=e c1. Then e,b1,c1 are pairwise
coprime squarefree ideals, while a may meet any of them. The character is

    chi_d(nc)^3=chi_d(b1c1)^3 1_((ae,d)=1).             (2)

Thus its core l=b1c1 is squarefree, of norm O(NC/((Na)^2(Ne)^2)). The
row mask in (2) must be retained when applying the sieve. For fixed a,e,
there are O(NC/((Na)^2(Ne)^2)) pairs b1,c1 before coprime restrictions.
Each coefficient has modulus <=1/(N sqrt(C)). A divisor Cauchy inequality
for the possible factorizations of l therefore bounds the complete column
square mass by

    (NC)^epsilon/[N (Na)^2(Ne)^2].                     (3)

The quadratic sieve gives row square norm at most

    (NCD)^epsilon [D/(N(Na)^2(Ne)^2)
                                      +C/((Na)^4(Ne)^4)]. (4)

Minkowski over a,e now costs only the products of harmonic ideal sums in
the first square root, and convergent inverse-square sums in the second.
The fixed-field count I(X)<<X bounds these harmonic sums by logarithms.
Absorb their fixed powers in epsilon, proving (1). This proof includes
all n powers and all n,c shared primes; discarding those populations
would give an unjustified cheaper column.

The corresponding single-filter estimate is

    sum_d^flat |sum_(n~N) a(n)chi_d(n)^3|^2
                    <<_epsilon (ND)^epsilon[D/N+1].   (5)

It follows by the same n=a^2b decomposition without e,c. All additional
row masks (a,d)=1 remain. Arbitrary common row multipliers of modulus at
most one may be inserted after each frozen native coefficient.

## 2. Smooth profiles do not erase the quadratic correlation

On fixed dyads a reflected profile has the form

    Phi(v0 exp(x)),
    x=log(Nc/C)-3log(Nn/N)-2log(Nd/D).

The x range is one fixed compact interval. Multiply by a fixed smooth
cutoff equal to one there. Two integrations by parts bound the L1 norm
of its Fourier transform by

    O_A(min(v0^alpha,v0^(-A))), some fixed alpha>0.      (6)

This uses exactly the source's two controlled Euler derivatives. Fourier
inversion separates c,n,d by the factors (Nc/C)^(it), (Nn/N)^(-3it) and
(Nd/D)^(-2it), each of modulus one. The new polynomial remains the actual
quadratic kernel chi_d(nc)^3. Minkowski for the Fourier integral, followed
by (1), is legitimate with the full envelope (6). No uncontrolled sharp
norm-coupled cutoff is inserted.

For the primal Gaussian profile P_G(Nc (Nk)^3 (Nn)^3/Z), use the identical
one-variable argument in log(Nn/N), freezing the native c,k first. All
Gaussian Euler derivatives have rapidly decreasing envelopes. Their
complete coefficient-weighted Fourier L1 sum is

    sum_(c squarefree,k) 1/(sqrt(Nc) Nk)
            ||Gaussian profile for c,k||_Fourier L1
                   <<_epsilon z^(1/2+epsilon),
    z=Z/N^3.                                          (7)

For z>=1 this is partial summation of the fixed-field ideal count in c,
followed by sum_k(Nk)^(-5/2-3epsilon)<infinity. For z<1 use Gaussian
flatness with any fixed power to obtain the stronger O_A(z^A).
Both Gaussian tails and every cube k remain in (7).

## 3. The actual filter, before either Cauchy loss

Use the exact coefficients c_v(n) of CUBE_TILT.md, satisfying |c_v(n)|<=1/Nn,
and define its full dyadic piece

    S_N(m;Z)=sum_(N<=Nn<2N) c_v(n)chi_n(m)^3 B_m(Z/(Nn)^3). (8)

Fix a row-unit class and write mR=h d, h powerful, d squarefree, (h,d)=1.
Let P<=Nh<2P, D<=Nd<2D. Allowed-generator reciprocity, including shared
zeros, gives

    chi_n(m)^3=chi_n(h epsilon)^3 chi_d(n)^3,            (9)

where epsilon ranges over the fixed finite row-unit classes. The first
factor is a column coefficient of modulus at most one, retaining the
primes shared by n and h. The d-character combines with the original
reflected chi_d(c)^3 to give the kernel in (1).

The complete reflected estimate, using (1),(6), is

    sum_(m in the P,D dyad)|S_N(m;Z)|^2
       <<_epsilon Z^epsilon P^(1/2)
                       [D/N+(D^2P/Z)N^3].             (10)

The algebra of the extra N is worth checking: the effective original
reflected c length at input Z/(Nn)^3 is C approximately (D^2P/Z)N^3.
The combined quadratic core nc increases the sieve column length by N,
but its complete coefficient square mass saves exactly 1/N. Their product
is C, rather than C/N. Thus the binding dual-column cost is not removed.

Here is the full resource for summing the frozen higher-power factors and
reflected cube k. Write a_f for the active frozen ideal. Its effective
column length is

    C_eff=D^2 (Nf)^2 N^3/[Z Na_f (Nk)^3].

The sqrt(C_eff) term, including the original factor beta(a_f)/Nk, has
resource

    sqrt(D^2(Nf)^2 N^3/Z)
                   *beta(a_f)/(sqrt(Na_f)(Nk)^(5/2)).

Its complete k sum is zeta_F^S(5/2), and its a_f sum is the source's
E_f(1/2). The sqrt(D/N) term uses E_f(0), a retained harmonic k sum and
the logarithmic number of c dyads. Choose the common cutoff
R0=Z^delta (D^2P/Z) N^3, independent of the individual filter n on its
dyad. The original rapidly decreasing reflected tail uses exactly the
same beta majorants; summing |c_v(n)| on this dyad costs O(1) by (8) and
ideal counting. Thus no uncharged polynomial N factor is introduced in
the tail. All row masks remain, the f sum is P^epsilon, and the same
P^(1/2) powerful-ideal count applies. The harmless powers of N,D,P can
be absorbed in Z^epsilon on fixed polynomial ranges. For an effective
C below one, the rapid large-v0 profile envelope gives the same bound.
This checks the complete imported interface, not one favorable frozen sector.

There is a better estimate for long filters. In the ORIGINAL native
expansion, freeze c,k. Its entire character chi_(c k^3)(m) is now a common
row multiplier of modulus <=1 in (5). No coprimality with the filter n
is imposed. Use (5), the Gaussian separation and the full coefficient
sum (7), then sum the powerful h population. This gives

    sum_(m in the P,D dyad)|S_N(m;Z)|^2
       <<_epsilon Z^epsilon P^(1/2)(D/N+1) Z/N^3.       (11)

For Z/N^3<1 its right side may be replaced by any higher Gaussian power.
Unlike absolute filter summation, (10)--(11) use the signed quadratic
correlation with the row before taking a norm. They are valid for the
actual c_v, not a synthetic replacement asserted to equal it.

## 4. Complete filtered moment and the resulting exponent

Combining (10)--(11), summing the dyadic filter by Minkowski, and absorbing
its logarithmic number of pieces gives

    sum_(m in the P,D dyad)|B_(m,v)(Z)|^2
       <<_epsilon Z^epsilon P^(1/2)
          [D+D sqrt(P)+D^(11/7)P^(4/7)Z^(-1/7)].        (12)

To verify the exponent, put L=D^2P/Z. The elementary inequalities

    min(LN^3,DZ/N^4)<=L^(4/7)(DZ)^(3/7),
    min(LN^3,Z/N^3)<=sqrt(LZ)

give the last two terms in (12). The first is D/N<=D. Constants two in
splitting D Z/N^4+Z/N^3 are harmless. The first balance occurs at
N^7=Z^2/(DP), when that scale is in range.

The infinite filter tail is paid explicitly. Uniformly in m, the original
native sum obeys |B_m(z)|<<_A z^A for 0<z<=1. For N0=Z^(1/3+delta),
|c_v(n)|<=1/Nn and ideal counting therefore give

    sum_(Nn>N0)|c_v(n) B_m(Z/(Nn)^3)|
                           <<_A Z^A N0^(-3A)=Z^(-3A delta). (13)

The row population is polynomial in Z. Choosing A after delta makes
the full omitted row square norm smaller than any required negative power.
Thus (12) does not omit a nontrivial long-filter sector.

For the ORIGINAL balanced row set at Nm approximately Z^M, fixed M>1,
PD<<Z^M. Precisely, rows are elements in one fixed compact-shape annular
box R intersect ell_(Z^M) K, with the finite unit/class slices of the
source, or their bounded-multiplicity representatives modulo Gamma.
They are not all generators of every ideal in a norm annulus: that would
include infinitely many S-units. Since

    P^(1/2)D<=Z^M,
    P D<=Z^M,
    D^(11/7)P^(15/14)<= (PD)^(11/7),

summing the P,D dyads in (12) proves the full bound

    sum_m |B_(m,v)(Z)|^2
             <<_epsilon Z^((11M-1)/7+epsilon), M>1.    (14)

All constants can be chosen uniformly for v>=0 in the filter coefficient
bounds, while the physical arithmetic definition remains fixed v. The
original native moment is Z^(2M-1+epsilon). For 1<M<2, (14) loses the
explicit power Z^((6-3M)/7), which is smaller than the naive absolute
filter loss but still positive.

For M>2 the raw exponent in (14) is better than 2M-1; this does not rescue
the physical comparison. Here is the full scale calculation, without
silently restricting the optimization to 1<M<2.

There is also a better envelope for long row boxes. Summing (11) alone
over every N>=1 gives Z^(1+epsilon)P^(1/2)(D+1). Since PD<<Z^M,
the full moment is at most Z^(M+1+epsilon). Thus (14) may be strengthened to

    sum_m |B_(m,v)(Z)|^2 <<_epsilon Z^(E(M)+epsilon),
    E(M)=min((11M-1)/7,M+1).                             (14a)

The crossover is exactly M=2. This uses the same complete tail (13).

## 5. All positive physical scales still give no critical-strip boundary

Write X=Z^a,Y=Z^b with a,b>0 and M=a+b>1. The original additive large sieve
has square mass O(1/min(X,Y)): before simplification it is
(XY)^(-1)(XY+Y^2)Y^(-1). Consequently (14) gives physical upper exponent

    U_hyb=(11M-1)/14-min(a,b)/2.                        (15)

The actual principal residue has Mellin shift b_a=5/6-a/3, independently
of b. Even if every other Poisson term were completely controlled, this
upper exponent could at best continue the principal target to

    B_hyb=5/6-a/3+(11M-1)/14-min(a,b)/2.                (16)

For b<=a this equals 16/21+19a/42+2b/7. For b>=a it equals
16/21+11M/14-5a/6. At fixed M both expressions are minimized at a=b=M/2,
giving the exact optimistic minimum

    B_hyb,min(M)=16/21+31M/84>95/84>1, M>1.             (17)

Thus the estimate proves no nontrivial zero-free boundary anywhere in the
critical strip, including when M>2 improves the raw long-row moment. This
conclusion already follows from the upper/principal exponents; imposing
the additional legal Poisson contours cannot improve that optimistic
minimum. The shift of the angular factor in CUBE_TILT.md acts on this SAME
principal Mellin variable s, not on an auxiliary z or a rescaled ordinate.
Native H was already nonzero for Re s>2/3, below the current ordinary-zeta
benchmark, so cleaning H is not itself the present strip bottleneck.

Using the stronger envelope (14a) does not change that conclusion. At fixed
M the minimum is again a=b=M/2, and the optimistic boundary becomes

    16/21+31M/84,  1<M<=2;
    4/3+M/12,     M>=2.                               (18)

Both expressions exceed one. Equation (18), rather than an extrapolation
of the short-row estimate, is the best boundary delivered by these two
proved moment bounds over every allowed M>1.

The value of (14) is an explicit paid bound and a remaining signed task:
improve the ACTUAL collapsed nc coefficient beyond the general quadratic
sieve's dual-column term. A claimed gain from an arbitrary denominator
contraction or from removing only a radial pole would not do that.
