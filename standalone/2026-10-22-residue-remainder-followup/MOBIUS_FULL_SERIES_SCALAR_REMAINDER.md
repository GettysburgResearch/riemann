# A scalar Möbius bound for the full sextic contour remainder

22 October 2026. Status: proposed theorem with complete proof below;
independent review pending. Scope: one scalar pairing of the **full**
sextic Kubota series with the original pure Möbius coefficient. This is
not the primitive series with its moving coprimality restriction, an
arbitrary-coefficient operator bound, or a bound for the full inverse
moment. No smaller zero-free boundary is claimed.

The kernel calculation was checked separately by joint_continuation
from Bröker--Hoffstein's exact finite-vector functional equation. The
finite modulus extraction and completion-removal argument below are
the signed_kernel contribution. The reference-scale primitive pole
bound used below is the root/joint_continuation companion result.

## 1. Sources, coefficients, and theorem

The full series and its completion use rStation paper 10, version 2:

<https://rstation.ai/api/v1/papers/riemann_hypothesis_10/versions/2/download>.

The snapshot SHA256 is
`525c899dd4dd5cb0ed15db43f63fb6e25cc140f98358e9d41ddfe897f5a23a7a`.
The finite-vector functional equation is Bröker--Hoffstein,
<https://arxiv.org/html/1312.0568v1>, equations (3.1), (3.8)--(3.10)
and the local gamma formulas immediately following (3.10). The residue
density is rStation paper 8, version 1:

<https://rstation.ai/api/v1/papers/riemann_hypothesis_8/versions/1/download>,

snapshot SHA256
`f1f9aed624908ccb9b6842911d898916230545ff76dc123187d7eadc3558def1`,
Section 3. Its section scope is retained: the original full component
below belongs to paper 8's fixed modulo-36 section family. No density
identity for arbitrary deeper sections is assumed.

All ideals are Eisenstein ideals, represented by good primary
generators, with the sources' literal nonunit zero extensions. Write

\[
 D_\nu(n,u)=\sum_{c\ {\rm good}}
               \frac{\nu(c)g_6(n,c)}{(Nc)^u},\qquad
 Z_\nu(n,u)=\zeta_S(6u-5)D_\nu(n,u),\qquad \theta=7/6.
                                                               \tag{1}
\]

The first series is initially absolutely convergent for `Re u>3/2`.
Fix smooth annular functions `W,w`, a fixed ray character `nu_0`, a
puncture `Q` fixed during every row sum, and an optional fixed numerator
ray-sector restriction. Put

\[
 b_n=1_{(n,Q)=1}\frac{\mu(n)\nu_0(n)}{\sqrt{Nn}}W(Nn/D).
                                                               \tag{2}
\]

The Möbius coefficient restricts `n` to squarefree ideals. For
`0<eta<1/12`, define

\[
 \mathcal E_Y[F_n]=\frac1{2\pi i}\int_{(1+\eta)}
     F_n(u)\widehat w(u-1/2)Y^{u-1}\,du,
\quad
 F(Y)=\sum_n b_n\mathcal E_Y[Z_\nu(n,\cdot)],
\quad
 R(U)=\sum_n b_n\mathcal E_U[D_\nu(n,\cdot)].           \tag{3}
\]

The completed continuation makes these definitions independent of the
chosen right line within `1<Re u<7/6`; for raw `D` the Euler factor is
nonzero there. All finite ray partitions are made before taking a
character inverse moment.

**Theorem.** For every `epsilon>0`, with the stated fixed-data and smooth
seminorm dependence, and uniformly for `D,U>=1`,

\[
 \boxed{\quad
 |R(U)|^2\ll_\epsilon(UDNQ)^\epsilon
 \begin{cases}
      D^{5/6}U^{1/6},&1\le U\le\sqrt D,\\
      D^{11/12},&U\ge\sqrt D.
 \end{cases}
 \quad}                                                    \tag{4}
\]

In particular the bound at the long-column scales `sqrt(D)<U<D` saves
against `U^(1/6)D^(5/6)` for this scalar full-series remainder. The
quantity on the left of (4) is explicitly the scalar in (3); it must
not be substituted for the inverse moment itself.

We import the actual-coefficient inverse estimate, with its smooth
norm-twist and fixed-ray uniformity,

\[
 I(H,A;Q'):=\sum_{0<Nr\le H}
 \left|\sum_{(m,Q')=1}\frac{\mu(m)\xi(m)}{\sqrt{Nm}}
              V(Nm/A)\overline{\chi_m(r)}\right|^2
 \ll_\epsilon(HA NQ')^\epsilon
                    (H+H^{1/6}A^{5/6}).                \tag{5}
\]

This is the inherited unmarked inverse theorem, including its permitted
puncture. It is not an arbitrary bounded-coefficient large sieve.
All nonzero rows used below are sixth-power-free; alternatively one
may use the all-row form (5). Fixed annular changes and norm twists
carry the source's polynomial seminorm cost.

We also use the companion primitive residue pairing, proved from
paper 10, equations (7.1)--(7.3), and (5) at a freely chosen reference
row scale:

\[
 \left|\sum_m\frac{\mu(m)\xi(m)}{\sqrt{Nm}}V(Nm/A)
       1_{(m,Q')=1}\rho_{\rm prim,\nu}(mR)\right|^2
 \ll_\epsilon(A NR NQ')^\epsilon A^{2/3}(NR)^{1/3}.
                                                               \tag{6}
\]

The companion proof chooses the reference scale `T=A sqrt(NR)`;
it uses the full primitive adjoint identity and its mean remainder,
not a single primitive-inversion branch.

## 2. Full-residue pairing

On squarefree `n`, paper 8's exact residue density gives

\[
 \rho_{\rm full,\nu}(n)=\rho_{\rm prim,\nu}(n)
                    \prod_{p\mid n}(1+(Np)^{-1})
   =\rho_{\rm prim,\nu}(n)\sum_{d\mid n}(Nd)^{-1}.      \tag{7}
\]

In each divisor term put `n=dm`. The scalar outside the normalized
Möbius polynomial in `m` is `(Nd)^(-3/2)`, up to a unit factor. Its
column length is `A=D/Nd`, label is `R=d`, and puncture is `Qd`.
If `d` meets `Q` the term is zero. A numerator-sector filter becomes
another member of the same fixed family. By (6), its squared size is

\[
 \ll (DNQ)^\epsilon (Nd)^{-3}
          (D/Nd)^{2/3}(Nd)^{1/3}
       =(DNQ)^\epsilon D^{2/3}(Nd)^{-10/3}.             \tag{8}
\]

The square roots are summable over all good `d`. Thus

\[
 \left|\sum_n b_n\rho_{\rm full,\nu}(n)\right|^2
                         \ll(DNQ)^\epsilon D^{2/3}.    \tag{9}
\]

Subunit column lengths in this divisor calculation are either empty
or bounded-size annuli; replacing them by a length comparable to one
changes constants only. The completed residue is `zeta_S(2)` times
the full residue, a fixed nonzero scalar.

## 3. Finite full-modulus sums preserve the inverse coefficient

First consider a finite physical Gauss sum at scale `H`:

\[
 S(H)=H^{-1/2}\sum_n b_n\sum_c
                \frac{\nu(c)g_6(n,c)}{\sqrt{Nc}}w(Nc/H).
                                                               \tag{10}
\]

Because `n` is squarefree, the only possible nonzero local modulus
exponents are one at primes outside `n`, and two at primes dividing
`n`. Consequently each nonzero term has uniquely

\[
       n=em,\qquad c=e^2c_0,\qquad
       e,m,c_0\text{ squarefree},\qquad (em,c_0)=(e,m)=1.
                                                               \tag{11}
\]

The modulus-one case is included. At a prime dividing `e`,
`g_6(em,p^2)=Np g_2(m,p)` after the other numerator factors are
frozen. CRT therefore supplies the scalar norm `(Ne)^(3/2)` and,
as its only dependence on the free `m`, the character
`overline(chi_e(m))^2`. The remaining modulus supplies
`overline(chi_(c_0)(m))`. Squared reciprocity and a fixed ordinary
reciprocity-sector partition turn their product into

\[
                    \overline{\chi_m(c_0e^2)}.          \tag{12}
\]

Every other factor is independent of `m`, and has modulus at most
one after these explicit norm factors are extracted. The natural
zeros retain the punctures at `e,c_0,Q`. In particular, this produces
an actual Möbius inverse polynomial of column length `D/Ne`, not an
arbitrary coefficient.

The factor `(Ne)^(1/2)` from `g_6(n,c)/sqrt(Nc)` cancels the
`(Ne)^(-1/2)` from `b_(em)`. For fixed `e`, Cauchy on
`Nc_0 asy H/(Ne)^2` and the injective row map `c_0 -> c_0e^2` give

\[
                |S_e(H)|^2
                 \ll (Ne)^{-2} I(C_wH,D/Ne;Qe).         \tag{13}
\]

All these rows have exponents one or two, so (5) applies on its
sixth-power-free support. Minkowski in `e`, followed by (5), gives

\[
 |S(H)|^2\ll_\epsilon(HDNQ)^\epsilon
                         (H+H^{1/6}D^{5/6}),\quad H\ge1.
                                                               \tag{14}
\]

Indeed the square roots of the two terms of (13) involve respectively
`sqrt(H) sum_e (Ne)^(-1)` over the finite permitted range, and
`H^(1/12)D^(5/12) sum_e (Ne)^(-17/12)`. The first costs a logarithm;
the second converges. If `H` is sufficiently small, (10) is empty.
The bounded range between that cutoff and one is covered by a fixed
enlargement of the row ball.

We shall also use the version with coefficient `g_6(n,c)/Nc`, a modulus
dyad `Nc asy L`, and a smooth shared profile in `Nn/D,Nc/L`. The same
extraction gives scalar `(Ne)^(-1)` times `1/sqrt(Nc_0)` and the same
inverse row (12). Since the squared norm of `1/sqrt(Nc_0)` on its
dyad is bounded, it gives the same bound

\[
              (LDNQ)^\epsilon(L+L^{1/6}D^{5/6})          \tag{15}
\]

for that scalar dyad. This permits a common profile, not a changing
arithmetic coefficient: separate the two fixed annular norm coordinates
by Mellin/Fourier inversion. Its weighted transform norm controls the
source's polynomial norm-twist cost. Every remaining arithmetic factor
is outside the inverse polynomial or is its fixed puncture/ray character.

## 4. Completed reflection and the finite kernel

This step uses the **completed** finite vector throughout. In the
Bröker--Hoffstein variable `s=u-1`, its archimedean factor is

\[
                     G(s)=\Gamma(6s)/\Gamma(s).
\]

Reflect (3) and put `s=v-1` in the reflected series. On each of the
finitely many good-numerator local sectors, the multiplier is a finite
sum of fixed bad-prime rescalings of

\[
       \frac{G(s)}{G(-s)}T_{ij}(-s)G_f(-s)
                       \widehat w(1/2-s)(Nn/Y)^s.       \tag{16}
\]

Here `T_ij` is a finite Laurent polynomial in fixed bad-prime norm
powers. This follows analytically from BH (3.10): in an unramified
local gamma term, the possible denominator `1-xi z`, with `xi^6=1`,
is canceled by the prefactor `1-z^6`; ramified gamma terms are
monomials. It does not rely on a numerical observation about T.

The factor
`G_f(-s)=prod_(p in S)(1-(Np)^(-1-6s))^(-1)` joins the completed
`zeta_S(1+6s)` to form the full Dedekind zeta function. Its series
expansion will therefore have a completion variable `b` over all
integral ideals, including the fixed bad primes. This change is
retained.

Moving the reflected line to `Re s>1/2`, where the full Gauss series
converges absolutely, crosses its possible theta pole at `s=1/6`.
The simple zero of `1/G(-s)` cancels that pole. The remaining fixed
local factors are regular there. Consequently there is no additional
theta residue in this reflected completed identity.

After expanding the reflected zeta factor and the full Gauss series,
one obtains a fixed finite sum of expressions

\[
 \sum_n b_n\sum_{c\ {\rm good}}\sum_{b\ {\rm integral}}
       \frac{\nu_j(c)g_6(n,c)}{Nc\,Nb}
       K_j\!\left(\frac{Nc(Nb)^6Y}{Nn}\right).          \tag{17}
\]

Fixed bad-prime factors and numerator-sector indicators are suppressed
only in this displayed notation; they are retained as the fixed
rescalings and finite partitions just described. In particular the
numerator and the sextic Gauss orientation are unchanged by reflection.

The kernel is a Mellin integral of `G(s)/G(-s)` times the finite
Laurent factor and `widehat w(1/2-s)`. For every fixed Euler derivative,
every `A>0`, and every small `delta>0`, it satisfies

\[
 |(x\partial_x)^jK_j(x)|\ll
 \begin{cases}
    x^{1/6-\delta},&0<x\le1,\\
    x^{-A},&x\ge1.
 \end{cases}                                             \tag{18}
\]

For the first bound move the kernel contour to
`Re s=-1/6+delta`, before the first numerator gamma pole; for the
second move right arbitrarily. The gamma ratio has polynomial vertical
growth on each fixed line, while the Mellin transform of the smooth
annular `w` has arbitrary vertical decay. The finite Laurent factors
give only fixed rescalings. These arguments also prove the derivative
and common-profile seminorm bounds used in (15).

Put `C=D/Y`. On a modulus dyad `L`, the profile in (17) has size and
required Euler seminorms bounded by the corresponding envelope in
(18), evaluated at `L(Nb)^6/C`. Apply (15), take square roots, and sum
the dyads. Choosing the large-x decay exponent sufficiently large gives

\[
 \left|\sum_n b_n\sum_c\frac{\nu_j(c)g_6(n,c)}{Nc}
          K_j\!\left(\frac{Nc(Nb)^6Y}{Nn}\right)\right|
 \ll (CDNQNb)^\epsilon
       \left[(C/(Nb)^6)^{1/2}
             +D^{5/12}(C/(Nb)^6)^{1/12}\right].         \tag{19}
\]

For a subunit effective scale `C/(Nb)^6`, rapid large-x decay makes
the left side smaller than the stated bound; no row ball below one
is used. For scales at least one the small-x exponent in (18) makes
the dyads below that scale summable. Taking the internal subpower
smaller than the available margins preserves both summations.

Multiplying (19) by `1/Nb` and summing the completion variable is
legitimate: the two principal weights are `(Nb)^(-4)` and
`(Nb)^(-3/2)`. Thus

\[
             |F(Y)|^2\ll (YDNQ)^\epsilon
                       (C+C^{1/6}D^{5/6})
             =(YDNQ)^\epsilon(D/Y+D Y^{-1/6}).          \tag{20}
\]

More transparently, the intermediate bound is
`C+C^(1/6)D^(5/6)`. In particular,

\[
       |F(Y)|^2\ll(YDNQ)^\epsilon D Y^{-1/6},
                       \qquad Y\ge\sqrt D.             \tag{21}
\]

## 5. The original completed branch, including subunit scales

Move the original completed contour to its absolute half-plane.
The only crossed pole is theta. Grouping the coefficient index
`c b^6` gives exactly the completed finite sum minus the completed
residue:

\[
 F(Y)=\sum_{b\ {\rm good}}\frac1{Nb}S(Y/(Nb)^6)
  -\zeta_S(2)\widehat w(2/3)Y^{1/6}
                     \sum_n b_n\rho_{\rm full,\nu}(n).
                                                               \tag{22}
\]

The finite sum is actually finite because `w` is annular. Equations
(9), (14), and the convergent completion weights imply

\[
 |F(Y)|^2\ll(YDNQ)^\epsilon
       \left(Y+Y^{1/6}D^{5/6}+Y^{1/3}D^{2/3}\right)
                  \ll(YDNQ)^\epsilon Y^{1/6}D^{5/6}
                         \quad(1\le Y\le\sqrt D).     \tag{23}
\]

If `0<Y<1` is below the fixed annular support threshold, the finite
sum is empty and (22) is exactly its negative residue term. The bound
`Y^(1/3)D^(2/3)<=Y^(1/6)D^(5/6)` still holds. In the remaining bounded
range it follows by enlarging fixed constants. Consequently the
estimate in (23) holds for every `0<Y<=sqrt(D)`, with the subpower
understood as `(DNQ max(Y,Y^-1))^epsilon`; all such small losses can be
chosen before the convergent sums below.

## 6. Exact raw completion removal and the optimized split

On the original line `Re u=1+eta`, the reciprocal Euler series is
absolutely convergent. Therefore the identity

\[
             R(U)=\sum_{a\ {\rm good}}\frac{\mu(a)}{Na}
                              F(U/(Na)^6)               \tag{24}
\]

is exact. Every scale `U/(Na)^6` is retained. No raw-series contour is
shifted to the left of one, and no zero-free premise is used to remove
completion.

Suppose `U>=sqrt(D)` and put

\[
                 A=(U^2/D)^{1/12}\ge1.                 \tag{25}
\]

For `Na<=A`, apply (21). Minkowski and ideal counting give the squared
head cost

\[
 \left(\sum_{Na\le A}\frac{|F(U/(Na)^6)|}{Na}\right)^2
     \ll(UDNQ)^\epsilon D U^{-1/6}
                     \left(\sum_{Na\le A}(Na)^{-1/2}\right)^2
     \ll(UDNQ)^\epsilon D U^{-1/6}A.                   \tag{26}
\]

For `Na>A`, including all subunit scales, apply (23). The squared tail
cost is

\[
 \left(\sum_{Na>A}\frac{|F(U/(Na)^6)|}{Na}\right)^2
     \ll(UDNQ)^\epsilon D^{5/6}U^{1/6}
                     \left(\sum_{Na>A}(Na)^{-3/2}\right)^2
     \ll(UDNQ)^\epsilon D^{5/6}U^{1/6}A^{-1}.           \tag{27}
\]

With (25), both final quantities are `D^(11/12)`. This proves the
second line of (4). If `U<=sqrt(D)`, every scale in (24) is on the
original branch, and its same convergent tail estimate proves the
first line. All internal epsilon losses can be chosen sufficiently
small to give the prescribed final exponent.

## 7. Exact limit of the conclusion

The full modulus extraction (11) is part of the proof; replacing it by
a squarefree-modulus restriction would omit nonzero terms. Likewise,
the reflected completion variable in (17), the original one in (22),
and every reciprocal-completion scale in (24) remain present.

For the moving-coprimality primitive series `H_n`, local inversion
adds divisors `d|n`, changes the numerator to `n d^2`, and changes the
physical scale to `U/(Nd)^2`, together with its finite Euler
denominator. The theorem above does not silently sum those branches.
Their residue tails and some refined weighted means are controlled
in companion notes, but a complete primitive scalar extension is
not asserted in (4).

Even a primitive scalar extension would control only the pairing
with a Gauss vector. Passing to the full signed first-Poisson return
or proving a bound for the complementary operator remains an
additional theorem. Neither (4) nor the finite Gauss operator estimate
in the neighboring note establishes that missing implication.
