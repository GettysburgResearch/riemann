# Finite-group sources, scalar resonances, and an S4 global completion

This theorem explains the grading natural boundary using the actual
finite-cover fibres, before any irreducible-character decomposition.
It allows scalar kernels in the input representations; their extra
resonances add positive leading terms. The explicit S4 source then
provides a second global family, with a sixth-order grading singularity
instead of the fourth-order S3 one.

The cohomological imports are the finite-cover trace formula, purity
and duality for smooth proper curves, as in the frozen
[S4 source](../global-s4-resolvent/S4_RESOLVENT_AND_RAMIFIED_FROBENIUS.md)
and [S3 completion](GLOBAL_COHOMOLOGICAL_COMPLETION.md). This is a
source-specific construction and an analytic boundary theorem, not a
new proof of finite-field RH, and no external priority is claimed.

## 1. General theorem and the actual inertia averages

Let Z -> P1 over F_Q be a finite Galois cover with Z smooth, proper
and geometrically connected, and with constant deck group G. Let V,W
be nonzero finite-dimensional characteristic-zero representations of
G, of dimensions r,s. Fix their finite-group invariant Hermitian
norms after complex realization. Define the actual graded source

    R_n=Sym^n(V) tensor Sym^n(W),
    d_n=binom(n+r-1,r-1) binom(n+s-1,s-1),
    D=r+s-1,   C=binom(D-1,r-1).

The rational character series F_g(z)=sum_n tr(g|R_n)z^n satisfy

    F_e(z) ~ C/(1-z)^D       as z -> 1.                 (1.1)

At a rational base point over F_{Q^m}, let I be its geometric inertia
subgroup and let g represent the Frobenius coset in its normalizer.
The complete, extended local trace is

    tr(Fr|R_n^I)=|I|^{-1} sum_{i in I} tr(gi|R_n).       (1.2)

This is an average over full source representations, not a replacement
of the source by the invariant input spaces. Formula (1.2) remains
valid with finite wild inertia because the coefficient characteristic
is zero; no wild-conductor formula is needed here.

Summing (1.2) over all Q^m+1 base points gives nonnegative rational
weights w_m(g), after harmless choices of coset representatives, with

    sum_g w_m(g)=Q^m+1,
    sum_g w_m(g)F_g(z) = total graded Frobenius trace,
    w_m(e)=#Z(F_{Q^m})/|G|.                            (1.3)

For the last identity, each geometric fibre is G/I. Because the deck
group is constant, Frobenius commutes with its transitive G action.
It fixes a point precisely when its normalizer coset is trivial; in
that case it fixes all |G|/|I| points. The identity contribution to
(1.2) is then 1/|I|, and otherwise zero. Summing proves (1.3).
The weights themselves can depend on conjugacy choices, but their
class-function sums and the identity coefficient do not.

## 2. The cohomological determinant and its Euler grading

Decompose R_n into its genuine finite-group multiplicity spaces.
There are finitely many irreducibles and finitely many corresponding
cohomology spaces H^i(P1,j_*rho). Fix the associated-sheaf and deck
action conventions consistently: these are
(H^i(Z) tensor rho)^G, equivalently the rho-dual multiplicity spaces
in H^i(Z). A general irreducible rho is not silently identified with
its dual. Finite-group invariant cohomology supplies this realization.
Choose a
complex realization and fixed norms on these finite spaces. Form
their multiplicity-space Hilbert sums and the operators K_i(z) whose
grade-n blocks are z^n Frobenius.

All multiplicities are bounded by d_n and grow at most polynomially.
Thus K_i(z) belongs to every Schatten class S_p, p>0, for |z|<1.
The ordinary cohomological Fredholm ratio

    L_G(z,T)=det(1-TK_1(z))
                /[det(1-TK_0(z))det(1-TK_2(z))]        (2.1)

is jointly meromorphic for |z|<1 and all complex T. This statement
uses the Hilbert sum of finite-source cohomology, and does not assert
that infinite sheaf completion commutes with taking cohomology.

For |T|<1/Q the actual closed-point Euler logarithm converges and is

    log L_G(z,T)=sum_{m>=1} T^m/m sum_g w_m(g)F_g(z^m). (2.2)

The closed-point grade in the local Euler factor is z^{n deg v}.
Absolute convergence follows from the polynomial dimensions, the
bound Q^m+1 for the total local averaging mass, and |z|<1. This also
fixes the logarithm by its value zero at T=0. No formal Euler product
is being substituted for an operator determinant.

## 3. Exact maximal-pole criterion and scalar resonances

Every g has finite order. If an eigenvalue lambda on V has
multiplicity a, the corresponding partial fraction of
det(1-u g|V)^{-1} contributes a polynomial in n of degree at most
a-1 times lambda^n. The analogous assertion holds for W. Multiplying
these coefficient formulas shows that every pole of F_g has order
at most

    max_eigen_mult(g|V)+max_eigen_mult(g|W)-1.          (3.1)

Thus a pole can have the full order D only if g is scalar on both
inputs. Conversely, if g|V=a_g I and g|W=b_g I, then

    F_g(z)=F_e(lambda_g z),    lambda_g=a_g b_g,         (3.2)

so it has a full-order pole at lambda_g z=1. Let H be this subgroup
of elements scalar on both inputs; lambda:H->C^* is a finite-order
character. Elements outside H have pole order at most D-1.

Fix real 0<T<1/Q and a root of unity zeta. Combining (1.1)--(3.2),
the radial limit is the nonnegative real number

    lim_{r->1-}(1-r)^D log L_G(r*zeta,T)
      = C sum_{m>=1} T^m/m^{D+1}
             sum_{g in H: lambda_g*zeta^m=1} w_m(g).   (3.3)

There is no omitted complex phase: in a resonant term
lambda_g*(r*zeta)^m=r^m, so its leading coefficient is C/m^D.
For dominated convergence, unitarity gives |F_g(r*zeta)|<=F_e(r),
and positivity of d_n gives F_e(r^m)<=F_e(r). The function
(1-r)^D F_e(r) is bounded on 0<=r<1. Equation (1.3) therefore gives
a summable majorant proportional to (Q^m+1)T^m/m. Each nonresonant
or lower-order term has scaled limit zero.

The limit in (3.3) is strictly positive. If zeta has order h and
Z has a closed point of degree ell, take m=lcm(ell,h). Then
w_m(1_G)>0, the identity lies in H, and its term is resonant. Such a
closed point exists because Z is a nonempty finite-type scheme over
a finite field. This does not assume that Z has a rational point
over every small extension.

Consequently the modulus of (2.1) grows faster than any finite-order
pole at every root of unity. Density proves a meromorphic natural
boundary |z|=1 for every fixed real 0<T<1/Q. This is not asserted
for arbitrary complex T. The argument works even when scalar kernels
are present, but the extra positive resonances in (3.3) must then
be retained.

If the identity is the only element scalar on both inputs, and zeta
has exact order h, the particularly simple formula is

    limit = (C/|G|) sum_{h divides m} #Z(F_{Q^m})
                                      T^m/m^{D+1}.    (3.4)

A faithful permutation input W guarantees this hypothesis: a
permutation matrix can be scalar only when it is the identity.

## 4. The actual S4 family and all its graded constituents

Use the frozen Bring-quartic S4 cover Z of genus nineteen, with
source E:y^2=x^4+b x+c -> P1_u, u=y, and hypotheses
p>3, b nonzero, 256c^3-27b^4 nonzero. Let V=std_3 and W=perm_4,
the actual augmentation and permutation representations of this
cover. The order of classes below is identity, transposition,
double transposition, three-cycle and four-cycle.

Their full graded character series are

    F_e=(1+6z+3z^2)/(1-z)^6,
    F_s=(1+2z+4z^2+4z^3+z^4)/(1-z^2)^4,
    F_d=(1+z^2)/(1-z^2)^3,
    F_c=1/(1-z^3)^2,
    F_q=1/(1-z^4).                                    (4.1)

These identities come directly from the input source: if the cycle
lengths of g in perm_4 are l_i, its symmetric-power series is
prod_i(1-u^{l_i})^{-1}. If h_n is its coefficient, the std_3
coefficient is h_n-h_{n-1}, and the R_n trace is
h_n(h_n-h_{n-1}). For a transposition the even/odd h_n are
(k+1)^2 and (k+1)(k+2), giving the displayed F_s. For a double
transposition only even grades survive, with trace (k+1)^2; the
three-cycle and four-cycle formulas follow immediately. The identity
case is the usual rank-(3,4) Segre series, or follows by the same
coefficient computation.

Let chi_rho be the frozen S4 character table and sizes (1,6,3,8,6).
The actual multiplicity generating series are

    A_rho(z)=(1/24) sum_classes size(g)chi_rho(g)F_g(z). (4.2)

Denote their coefficients by m_{rho,n}, with rho ordered
1, sign, two, std, tw=sign tensor std. The frozen geometric source
constructs the four nontrivial Frobenius polynomials P_D,P_R,P_E,P_tw,
of degrees 4,2,2,8 respectively. Its full normalized regular-source
polynomial is P_Z=P_D P_R^2 P_E^3 P_tw^3 of degree 38. Thus

    L(R_n,T)=Z(P1,T)^{m_1,n} P_D(T)^{m_sign,n}
               P_R(T)^{m_two,n} P_E(T)^{m_std,n}
               P_tw(T)^{m_tw,n}.                      (4.3)

The multiplicity space for tw cohomology has dimension eight;
its full tw-isotypic space in H^1(Z) has dimension 24. The
distinction is preserved in (4.3).

All ramified graded stalks use whole-series coset averages. At a
finite transposition branch they are (F_e+F_s)/2 if chi(-2)=+1,
and (F_s+F_d)/2 otherwise. At infinity they are (F_e+F_d)/2 if
Q=1 modulo 4, and F_s otherwise. The latter follows because both
elements of the nonsplit infinity coset are transpositions. These
are full graded Frobenius traces, not merely invariant dimensions.

Here d_n=binom(n+2,2)binom(n+3,3)~n^5/12, D=6 and C=10.
The faithful permutation input makes identity the unique full-order
class. Therefore (3.4) becomes

    lim_{r->1-}(1-r)^6 log L_S4(r*zeta,T)
      = (5/12) sum_{h divides m} #Z(F_{Q^m})T^m/m^7>0. (4.4)

The actual infinity fibre of Z has twelve rational points whenever
the field is 1 modulo 4, so #Z(F_{Q^{2h}})>=12 and the right side
is at least 5*T^{2h}/(2h)^7. No fitted eigenvalues or hypothetical
cover enter this bound.

## 5. Finite duality records its divergent source exponents

For this self-dual real S4 source set

    kappa_n = 2m_sign,n + m_two,n + m_std,n
                        + 4m_tw,n - m_1,n,
    K_N=sum_{n=0}^N kappa_n,
    W_N=sum_{n=0}^N n*kappa_n.

Finite-source Poincare duality gives the actual finite-grade product

    L_{S4,N}(z,T)=Q^{K_N}T^{2K_N}z^{2W_N}
                         L_{S4,N}(1/z,1/(QT)).        (5.1)

This includes kappa_0=-1 from Z(P1). Because all nonidentity
characters in (4.1) have coefficient growth O(n^3), (4.2) gives
m_{rho,n}=dim(rho)d_n/24+O(n^3). Hence

    kappa_n=(3/4)d_n+O(n^3)~n^5/16,
    K_N~N^6/96,       W_N~N^7/112.                    (5.2)

The native finite functional-equation prefactor consequently has
divergent exponents in the ordinary infinite limit, and z and 1/z
have disjoint strict trace-class domains. This records the precise
failure of a direct finite-prefactor limit. It does not rule out
every possible regularized pairing or alternative infinite completion.

## 6. An actual scalar-kernel control

The extra terms in (3.3) are necessary even for a genus-zero source.
Take the ramified C2 cover P1_v -> P1_u, u=v^2, and inputs V=1,
W=sign, both of rank one. Here R_n=sign^n and
F_e(z)=1/(1-z), F_s(z)=1/(1+z). The complete inertia averages give
w_m(e)=w_m(s)=(Q^m+1)/2, so the global graded trace is
(Q^m+1)/(1-z^2). Equivalently its determinant is
product_{k>=0} Z(P1,Tz^{2k}).

At zeta=-1, the identity is resonant for even m and the nonidentity
scalar is resonant for odd m. The actual scaled logarithm constant is

    (1/2) sum_{m>=1} (Q^m+1)T^m/m^2.

Keeping only the identity would omit every odd term, already missing
the positive contribution (Q+1)T/2. This is an actual ramified-source
counterexample to applying (3.4) without its scalar hypothesis, not
a hypothetical character-table example.

## 7. Replay scope and bounds

The new replay reconstructs the input symmetric powers from cycle
lengths and checks (4.1), all five multiplicity sequences, the
ramified series and source conductor dimensions. It authenticates
the frozen S4 producer, proof and full artifact. The earlier large-
extension reconstruction of P_tw is reused as a frozen source
result; this replay independently recounts only extension degrees
one and two, with maximum field size 49. It does not advertise
those repeated counts as a new degree-eight reconstruction.

Let Z_m be computed from the frozen four cohomology polynomials.
The primitive degree-one and degree-two normalized fibres check it.
For 0<T<1/Q the boundary constant tail after m=M is at most

    20 (QT)^{M+1}/[(M+1)^7(1-QT)],                    (7.1)

using Z_m<=24(Q^m+1). At real z=r or z=-r the scaled finite
logarithm has tail at most

    20 (QT)^{M+1}/[(M+1)(1-QT)],                      (7.2)

since (1-r)^6 F_e(r)<=10 and Q^m+1<=2Q^m. These conservative
rational bounds certify source constant and radial comparisons;
finite root-order lists do not replace the general density proof.
