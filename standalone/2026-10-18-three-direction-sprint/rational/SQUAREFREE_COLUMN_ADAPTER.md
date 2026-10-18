# Complete squarefree columns, with paid shared-factor and square tails

**PROPOSED exact source identities and source-qualified estimates.**
This is an adapter for the full synchronized mixed vector, not a bound
for its remaining coherent core. The original inverse second-moment
input is explicitly the pinned source's `eq:amplified-note`, with
`e(r)=max(1,(1+5r)/6)=1` for 0<=r<=1. Its full proof is imported,
as in `TRANSPOSED_GAUSS_MODE.md`.

All indices below are good integral ideals of E=Q(omega). Finite unit
and primary-ray choices are kept as finite fixed sectors. Let
`psi_u(a)=chi_a(u)^varsigma`; the common finite twist nu is written
separately. All characters have their ORIGINAL zero extension. Define

    M_u(D)=D^(-1/2)sum_d mu(d)nu(d)psi_u(d)W_M(Nd/D),
    S_u(N)=N^(-1/2)sum_n nu(n)psi_u(n)W_S(Nn/N).         (1)

The profiles are the actual common-height smooth profiles of the
detector. We assume D<=C U and N<=C sqrt(U), allowing every shortened
length below those bounds. Constants depend on the fixed compact
profile supports and have the source's fixed polynomial height cost.
Rows are the complete physical good sixth-power-free annulus Nu≈U,
with a fixed nonnegative bounded row weight. All norm statements use
this weighted row space.

## 1. Exact decomposition into squarefree product columns

For Q a good ideal, put

    B_u(A,B;Q)=(AB)^(-1/2)
       sum_(a,b squarefree, (a,b)=1, (ab,Q)=1)
          mu(a)nu(ab)psi_u(ab)W_M(Na/A)W_S(Nb/B).       (2)

The symbol B on the right denotes a length, not an ideal. The new
product ab is squarefree in EVERY column. There is an exact identity

    M_u(D)S_u(N)
      =sum_(g squarefree,h>=1)
          mu(g)nu((gh)^2)psi_u((gh)^2)/(Ng Nh)
          * B_u(D/Ng,N/(Ng (Nh)^2);g).                 (3)

Every original pair occurs exactly once: uniquely write n=h^2 s with
s squarefree, set g=gcd(d,s), and write d=g a,s=g b. Then g,a,b are
pairwise coprime squarefree ideals, while h may share ANY prime with
g,a,b. We have

    dn=(gh)^2 ab,     mu(d)=mu(g)mu(a),
    [D/Ng]*[N/(Ng (Nh)^2)]=DN/(Ng Nh)^2.

These give both (3) and its central normalization. In particular there
is NO imposed condition `(h,ab)=1`. The outside factor psi_u((gh)^2)
retains its full row-zero mask; it is not replaced by one.

Only polynomially bounded Ng,Nh occur. Hence
`sum 1/(Ng Nh)<<log(2U)^2`. A uniform full mixed norm estimate for
the COMPLETE B vectors, with their displayed masks and shortened
lengths, therefore lifts to the original all-power source with only
logarithmic norm loss. This statement uses Minkowski on the whole
vector; it does not identify or discard individual conductor sectors.

## 2. Common input masks do not cost a new power in the inverse mean

The source inverse second moment for every length A<=C U is

    ||M(A)||_row <<_epsilon U^((1+epsilon)/2)(1+T)^C0.  (4)

For a moving input mask Q of polynomial norm, its SAME bound holds
with a prescribed subpower loss. Indeed, let f_Q(r)=1 if every prime
of r divides Q, and zero otherwise. Exact local Euler multiplication
gives

    mu(n)1_((n,Q)=1)=(mu*f_Q)(n).

Thus the normalized masked polynomial is exactly

    M_(u,Q)(A)
      =sum_(r Q-smooth)nu(r)psi_u(r)/(Nr)^(1/2)
                                      * M_u(A/Nr).     (5)

The sum is finite at each supported annular scale; below a fixed
minimum scale it vanishes. The omitted infinite positive resource is

    sum_(r Q-smooth)(Nr)^(-1/2)
       =product_(p|Q)(1-(Np)^(-1/2))^(-1)
       <<_epsilon (NQ)^epsilon.                       (6)

The last bound follows prime by prime, absorbing the finitely many
small primes into its constant. Equations (4)--(6) and Minkowski pay
the mask. No missing local Euler factor is divided by a zero character
value: (5) is a coefficient convolution and remains exact when
psi_u(p)=0. The only unproved input in this step is the named original
source moment (4).

## 3. An actual bound for B and complete outer tails

Expand the coprimality in (2) by
`1_((a,b)=1)=sum_(ell|a,b)mu(ell)`. Since a is squarefree,
`mu(ell a')=mu(ell)mu(a')` when `(ell,a')=1`. The TWO Mobius factors
cancel. The exact resulting identity is

    B_u(A,B;Q)
      =sum_(ell squarefree,(ell,Q)=1)
          nu(ell^2)psi_u(ell^2)/(Nell)
          *M_(u,Qell)(A/Nell)
          *S_(u,Qell)^sf(B/Nell),                    (7)

where the last plain polynomial has squarefree coefficients mu^2 and
the same common input mask. Its pointwise trivial bound is
`|S_(u,Qell)^sf(B/Nell)|<<sqrt(B/Nell)` on nonempty scales. All
profiles remain the same fixed functions at their actual rescaled
lengths. Thus (4)--(7) give the genuine complete norm estimate

    ||B(A,B;Q)||_row^2
          <<_epsilon U^(1+epsilon) B (1+T)^C1,         (8)

because `sum_ell (Nell)^(-3/2)<infinity`. This bound is weak at
B≈sqrt(U), but pays the following full-source tails.

In (3), the part Ng>G has squared norm

    <<_epsilon U^(1+epsilon) N/G * (1+T)^C1,           (9)

and the part Nh>H has squared norm

    <<_epsilon U^(1+epsilon) N/H^2 * (1+T)^C1.         (10)

Indeed each summand's norm is at most
`U^epsilon sqrt(U N)/(Ng)^(3/2)(Nh)^2`; use the elementary ideal
tails `sum_(Ng>G)(Ng)^(-3/2)<<G^(-1/2)` and
`sum_(Nh>H)(Nh)^(-2)<<H^(-1)`, and then square. The union is paid
by the triangle inequality, with its intersection explicitly counted
at most twice. It is not an assertion of orthogonality between tails.

At D=U,N=sqrt(U), choosing G=U^(3/10), H=U^(3/20) pays this COMPLETE
outer tail at U^(6/5+epsilon). The remaining vector has Ng<=G,Nh<=H
and squarefree product columns ab. Its coefficient norm still contains
the exact harmonic outer weights and masks. A bound for that remaining
vector is OPEN; (8) alone costs U^(3/2) in its hardest g=h=1 component.

## 4. Exact shared-prime warning for the next Gauss transformation

Write the positive orientation here; the other orientation is obtained
by conjugating every character and Gauss phase together.

For any two squarefree new columns A1,A2, write
`A1=R x,A2=R y`, with R,x,y pairwise coprime and squarefree.
The primitive good ratio character is
`theta=chi_x*bar chi_y`, conductor C=xy, while the original common
R remains a zero-only row mask. Primitive CRT and fixed-ray sextic
reciprocity give

    Gamma(theta)=finite_phase*gamma_1(x)bar gamma_1(y)
       =finite_phase*gamma_1(A1)bar gamma_1(A2)
                                         *theta(R)^(-2).       (11)

Here the raw Gauss sums are normalized by the square root of their
primitive conductor. A mask-divisor b in Poisson consequently gives
the factor `theta(b)bar theta(k R^2)`, not just `bar theta(k)`.
The characters in this expression are the STRIPPED primitive chi_x
and chi_y. Replacing them by chi_(A1),chi_(A2) would spuriously
annihilate R^2 and lose the actual shared-prime contributions.

The CRT ratio factor `chi_x(y)bar chi_y(x)` is only a fixed-ray phase;
it is not an additional growing cubic obstruction. The cubic factor
inside a SINGLE gamma_1(ab) remains. On every squarefree column it
gives the exact useful transfer

    mu(a)gamma_1(ab)=mu(b)conjugate(C_(-1)(ab))*G(ab),   (12)

using the source's finite Gauss identity, with every fixed ray phase
retained. Thus the inverse sign moves from the long a index to the
short b index. Equations (11)--(12), the original physical Fourier
kernel, and its complete collision corrections must all be kept in
any use of this transfer. No uncentered positive square or averaged
label estimate is asserted to bound their remaining coherent form.

`check_column_adapter.py` independently enumerates complete finite
coefficient polynomials in a fixture ideal monoid, checking (3), (5)
and (7), their normalizations and genuine h-shared-prime cases. Four
wrong variants are rejected, including the tempting EXTRA mu(ell)
in (7), which would undo the exact sign cancellation. Its fixtures
verify the algebra for every multiplicative character by coefficient
identity; they do not prove the imported asymptotic source moment.
