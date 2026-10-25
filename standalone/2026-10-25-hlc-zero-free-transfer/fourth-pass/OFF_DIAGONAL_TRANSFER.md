# The thin band's exact determinant and affine prime correlation

**Status: exact finite identities, an elementary resonant-locus bound,
and a precise unproved HLC transfer hypothesis.** This note does not
deduce that hypothesis from the supplied HLC paper.

The new target is the actual narrow primal band from Section 8 of
`MIDDLE_JOINT.md`. Unlike the earlier full-native affine reformulation,
the determinant coordinates here keep its two short/long Möbius factors,
ordinary factors, anisotropic scale ranges and complete sixth-power
resonance. The goal is to specify exactly what an extension of the HLC
mechanism would have to estimate.

## 1. The actual coefficient and its elementary diagonal

Work over $E=\mathbb Q(\omega)$ and $\mathcal O_E=\mathbb Z[\omega]$,
using the pinned source's primary generators outside the fixed bad-prime
set $S$. Products of these chosen primary generators represent the ideal
products. Additive identities below are identities between those
generators, not additions of ideals.

Retain the original sixth-power-free physical rows $Nu\asymp U$,
finite-order fixed ray twists, either sextic orientation, common natural
puncture, and actual natural zeros. Thus $\psi_u$ is completely
multiplicative with its zero extension. Let $w(u)$ be the original
bounded nonnegative row weight, or weight one on a source-compatible
buffered class. The elementary identities do not require any zero-free
premise.

Put $D=U^r$, $29/25\le r\le117/100$, and use

$$
 y_1=U^{1/250},\qquad y_2=2D/U^{1/250},\qquad
 A(m)=\sum_{ab=m}\mu_E(a)\mu_E(b)w_0(Na/y_1)w_0(Nb/y_2),
$$
$$
 \Xi(m)=\chi_0(Nm/U^{773/1000})
                         -\chi_0(Nm/U^{147/200}).            \tag{1}
$$

The fixed real cutoffs take values in $[0,1]$, equal one on $[0,1]$
and vanish on $[2,\infty)$, as in the preceding note. The thin band is

$$
 B_u=-D^{-1/2}\sum_{m,c}A(m)\Xi(m)\psi_u(mc)V(NmNc/D).
 \tag{2}
$$

Define the actual full-column coefficient

$$
                     \lambda(n)=\sum_{m\mid n}A(m)\Xi(m).
 \tag{3}
$$

It is real for the stated real cutoffs, but need not have one sign and
is not the original Möbius coefficient. The exact collection is
$B_u=-D^{-1/2}\sum_n\lambda(n)\psi_u(n)V(Nn/D)$.
Divisor bounds give $|\lambda(n)|\le d_{E,3}(n)\ll_\epsilon
(Nn)^\epsilon$. In particular the complete pair diagonal has size

$$
 \Delta=D^{-1}\sum_n |\lambda(n)V(Nn/D)|^2
                                 \sum_u w(u)|\psi_u(n)|^2
                          \ll_\epsilon U D^\epsilon.        \tag{4}
$$

The full mean will be denoted $J=\sum_u w(u)|B_u|^2$.

### The whole sixth-power-resonant locus also has row-volume size

Write an ideal uniquely as $n=a t^6$, with a sixth-power-free. Let
$\operatorname{core}_6(n)=a$. The part of the expanded mean with
$\operatorname{core}_6(n_1)=\operatorname{core}_6(n_2)$ is

$$
 \mathcal R=D^{-1}\sum_u w(u)
   \sum_a\left|\sum_{\operatorname{core}_6(n)=a}
                       \lambda(n)\psi_u(n)V(Nn/D)\right|^2.
 \tag{5}
$$

Thus $\mathcal R\ge0$, with all natural zeros retained. This includes
non-equal column pairs. For completeness, elementary lattice counting
in $\mathcal O_E$ gives $I_E(X):=\#\{a:Na\le X\}\le C_E X$
for $X\ge1$; restriction away from S can only reduce this count.
For a fixed core a with $Na\le2D$, the number of t with
$N(at^6)\in(D,2D)$ is at most $C_E(2D/Na)^{1/6}$.
Consequently the number of such pairs is

$$
 \ll D^{1/3}\sum_{Na\le2D}(Na)^{-1/3}\ll D.
$$

Here the sum may be enlarged to all ideals, and partial summation gives
$\sum_{Na\le X}(Na)^{-1/3}
=X^{-1/3}I_E(X)+(1/3)\int_1^X I_E(t)t^{-4/3}\,dt
\ll X^{2/3}$. The physical row count is $O(U)$ by the same ideal
counting; the stated bounded weight does not change it. Coefficients,
profiles and the bound $|\psi_u(n)|\le1$ therefore give

$$
                       0\le\mathcal R\ll_\epsilon U D^\epsilon.
 \tag{6}
$$

No equality of the natural characters with the character of the core is
used: multiplying by a sixth power can introduce additional zeros.
Boundedness of the actual phases is enough. Consequently a proposed
HLC estimate may remove this complete resonant locus explicitly at the
cost (6), instead of mistaking every nonzero determinant for a
nonprincipal row character.

## 2. Exact determinant coordinates over the Eisenstein lattice

Expand (2) against its conjugate. For $n_1=m_1c_1$ and $n_2=m_2c_2$,
put

$$
                  P=(m_1,c_2),\qquad Q=(m_2,c_1)
                              \quad\text{in }\mathcal O_E^2.
$$

Then

$$
              \det(P,Q)=m_1c_1-m_2c_2=n_1-n_2=:h.          \tag{7}
$$

Both n-generators are primary, so $h\in3\mathcal O_E$. Off the
genuine pair diagonal, $h\ne0$. Since $Nn_i\in(D,2D)$,

$$
                              Nh\le8D.                     \tag{8}
$$

This is a two-dimensional lattice shift family with $O(D)$ possible
shifts; h is not a fixed rational integer such as two. The thin band
has

$$
 U^{.735}<Nm_i<2U^{.773},\qquad
                   Nc_i\asymp D/Nm_i.                     \tag{9}
$$

Thus the complex magnitudes of the two coordinates have scales near
$U^{.375}$ and $U^{.21}$. The exact boxes are anisotropic, with ordinary
norm exponents in $[.387,.435]+O(1/\log U)$.

The row phase separates correctly between these determinant endpoints:

$$
 \psi_u(m_1c_1)\overline{\psi_u(m_2c_2)}
  =\{\psi_u(P_1)\overline{\psi_u(P_2)}\}
     \overline{\{\psi_u(Q_1)\overline{\psi_u(Q_2)}\}}.
 \tag{10}
$$

The actual endpoint coefficients are $A(P_1)\Xi(P_1)$ and
$A(Q_1)\Xi(Q_1)$, with the two cross-product profiles still present.
Equation (10) retains the conjugation and all zeros; it does not replace
the row kernel by an unsigned determinant count.

### Primitive vectors require two actual gcd factors

P and Q need not be primitive. Write

$$
 g=(P_1,P_2),\quad l=(Q_1,Q_2),\quad P=gP_0,
 \quad Q=lQ_0,
$$

using the primary generators of the gcd ideals. The quotient vectors
$P_0,Q_0$ are primitive and

$$
                         h=gl\det(P_0,Q_0).                \tag{11}
$$

The natural character factor is exactly

$$
 1_{(gl,P_u)=1}\,
 \psi_u(P_{0,1}Q_{0,2})
                 \overline{\psi_u(Q_{0,1}P_{0,2})},         \tag{12}
$$

where $P_u$ contains the primitive conductor and every deleted natural
prime. The coefficients become $A(gP_{0,1})\Xi(gP_{0,1})$ and
$A(lQ_{0,1})\Xi(lQ_{0,1})$. The profiles acquire the actual product
$N(gl)$ in their arguments. This is a discrete bijection, with no
extra scalar Jacobian. The overall $D^{-1}$ of the squared mean stays
unchanged. A rational primitive-vector operator cannot be substituted
before these gcd factors, masks and profile scales are treated.

## 3. Extracting a prime from the long Möbius factor

The prime extraction can be placed on the long inverse factor rather
than on the collected coefficient $\lambda$, which is not Möbius.
Expand $m_i=a_i b_i$ in (1). On the thin support,

$$
                         Nb_i\gg U^{.731}>1.                \tag{13}
$$

In fact $Nb_i\le Nm_i<2U^{.773}<y_2$ throughout the stated r
interval once U is sufficiently large. Both long cutoffs
$w_0(Nb_i/y_2)$ are therefore identically one on this particular
band. They are retained in (16) to exhibit its exact origin. Thus the
only inverse-coefficient cutoff that varies here is the genuinely
short cutoff on $a_i$.

Use the exact prime-only identity

$$
 \mu_E(b)\log Nb
  =-\sum_{\substack{dp=b\\p\ {m prime}\\(d,p)=1}}
                                      \mu_E(d)\log Np.     \tag{14}
$$

It is valid also for nonsquarefree b: the right side vanishes because
either the selected prime repeats or the remaining Möbius factor is
zero. The coprimality condition is essential.

Apply (14) to $b_1=dp$ only. Put

$$
                 A_0=a_1dc_1,\qquad B_0=a_2c_2.
$$

The nonzero determinant relation becomes the precise affine equation

$$
                        A_0p-B_0b_2=h.                     \tag{15}
$$

Equivalently, the prime satisfies $A_0p\equiv h\pmod{B_0}$ and
the resulting quotient $(A_0p-h)/B_0$ is the admissible primary
generator b_2. No assumption that $A_0,B_0$ are coprime is made.
Solvability and all common factors remain in the condition (15).

For compact notation define the complete common weight

$$
 \begin{split}
 \mathcal W_U(a_1,dp,c_1,a_2,b_2,c_2)
 ={}&w_0(Na_1/y_1)w_0(Ndp/y_2)
       w_0(Na_2/y_1)w_0(Nb_2/y_2)\\
 &\cdot\Xi(a_1dp)\Xi(a_2b_2)
       V(N(A_0p)/D)\overline{V(N(B_0b_2)/D)}
       \frac{\log U}{\log(NdNp)}.
 \end{split}                                               \tag{16}
$$

The logarithmic quotient has uniformly bounded fixed logarithmic
derivatives on the actual support (13). All cutoffs, including both
short-factor cutoffs, remain in this weight.

Define the following **complete signed** sum, with all ideal variables
outside S and with their primary generators used in (15):

$$
 \begin{split}
 \mathcal T_U={}&\sum_u w(u)
 \sum_{a_1,a_2,d,c_1,c_2}
       \mu_E(a_1)\mu_E(a_2)\mu_E(d)
 \sum_{\substack{0\ne h\in3\mathcal O_E}}
 \sum_{\substack{p\ {m prime},\ (d,p)=1\\
              b_2\ {m admissible},\ A_0p-B_0b_2=h}}
       (\log Np)\mu_E(b_2)\\
 &\hspace{6mm}\cdot
       \psi_u(A_0)\overline{\psi_u(B_0)}
       \psi_u(p)\overline{\psi_u(b_2)}
       \mathcal W_U(a_1,dp,c_1,a_2,b_2,c_2).
 \end{split}                                               \tag{17}
$$

The profile supports make the sum finite. All source natural zeros
remain in the displayed characters. In particular a common prime of
$A_0B_0$ and the row or deleted support forces the correct zero,
rather than a change to a primitive character with different zeros.

Expanding the square, separating $n_1=n_2$, and applying (14) proves
the exact identity

$$
 \boxed{\qquad J=\Delta-\frac{\mathcal T_U}{D\log U}.
 \qquad}                                                   \tag{18}
$$

The whole sum $\mathcal T_U$ is real by (18), although its individual
affine summands may be complex. The part with equal sixth-power-free
cores can alternatively be removed using (5)--(6): its absolute
contribution to $\mathcal T_U$ is at most
$D\log U\cdot U D^\epsilon$.

## 4. A precise sufficient HLC extension

Here is one concrete sufficient hypothesis for the final localized
consumer. It is stronger than the minimal spike-count hypothesis, but
it is stated on an explicit prime--Möbius object with the correct signs.

**Open affine HLC input for the thin band.** For all the original
compatible critical classes, common profiles and licensed heights,
uniformly for $29/25\le r\le117/100$, the exact aggregate (17)
satisfies

$$
 \boxed{\quad
 \mathcal T_U\ge
 -C_\epsilon D\log U\,
     U^{(1+5r)/6-1/1000+\epsilon}
                         (1+|t|)^A p_J(W)^2 .\quad}         \tag{HLC-thin}
$$

A two-sided estimate of the corresponding size is stronger than
necessary. The natural resonant part just bounded is already below
this budget. The hypothesis is for the entire signed outer sum;
independent absolute estimates for each h, row, slope or gcd are not
silently assumed to imply it.

By (4) and (18), (HLC-thin) gives
$J\ll U^{(1+5r)/6-1/1000+\epsilon}$ with the same uniformity.
The row-volume diagonal is absorbed because the displayed exponent
is strictly greater than one on this r interval. Chebyshev at the
actual buffered threshold then supplies the thin-band witness count
of `DETECTOR_LOCALIZATION.md`. Its already certified conditional
consumer would give $\operatorname{Re}s>0.8748856$ in the stated
imported Eisenstein framework and inherited base-change scope.
**The new hypothesis (HLC-thin) is not proved here.**

### What the extension must cover

The exact differences from the source scalar HLC statement are now
quantified, rather than described as an unspecified analogy.

| Interface | Actual requirement in (15)--(17) |
|---|---|
| Field and geometry | Prime ideals and Möbius ideals of $\mathcal O_E$, primitive vectors in $\mathcal O_E^2$ after (11), and anisotropic complex boxes (9) |
| Additive shift | The complete signed lattice family $0\ne h\in3\mathcal O_E$, $Nh\le8D$; after primitive reduction the determinant is $h/(gl)$ when integral |
| Affine coefficients | $A_0=a_1dc_1$, $B_0=a_2c_2$, with the exact congruence and all gcds retained; $NA_0\asymp D/Np$ and $NB_0\ll U^{.439}$ |
| Character twists | The original conjugate pair $\psi_u(p)\overline{\psi_u(b_2)}$, outer phases $\psi_u(A_0)\overline{\psi_u(B_0)}$, conductor norm $O(U)$ and the prescribed growing natural deletion radical |
| Endpoint coefficients | Both remaining Möbius signs, the short factors $a_i\ll U^{.004}$, the long factors $b_i\gg U^{.731}$, and the actual smooth cutoffs in (16) |
| Rate and aggregation | The fixed-power aggregate budget (HLC-thin), in the physical row measure, with uniform finite profile and height orders |

For example, a field-level determinant replacement would need additive
characters of the two-dimensional torus dual to $\mathcal O_E$, not
only a single rational circle. At an inert rational prime the residue
field has cardinality $p^2$, so its projective-line count is $p^2+1$;
one cannot retain a factor $1/(p+1)$ from the rational local model.
The complete finite-field bridge identities can be formulated over
either residue field, but completion of these weighted integer-lattice
paths and the actual major-arc subtraction remain additional work.

Likewise, the fixed nonzero rational shift in the supplied paper is
not (15). Even a theorem uniform for each fixed h separately must be
summed with the signs and normalization of (17) before it can be used
here. This formulation preserves the possibility of coherent HLC
cancellation; it does not lose it by first imposing absolute values on
the polynomially many shifts.

The source paper's qualitative conclusion or fixed logarithmic error
does not itself establish (HLC-thin). The earlier transfer audit already
records that general rate distinction. The specific advance here is
the exact narrow-band determinant geometry, its primitive gcd ledger,
the complete resonant-locus bound and the precise remaining signed
affine input.

## 5. Verification boundary

`check_off_diagonal_transfer.py` checks the finite coefficient
collection, determinant and primitive-gcd identities over actual
Eisenstein primary ideals, natural sextic phases with a nontrivial
puncture, and the prime-extracted mean identity. A positive completely
additive prime weight replaces logarithms in its exact rational check;
the prime-only identity holds for every such additive weight.

The exact replay includes both sextic orientations, non-squarefree
physical rows, repeated primes shared by the two inverse factors,
and nontrivial endpoint contents. It checks 2,760 prime-extracted
summands, 2,256 determinant/content cases, 36,096 natural phase cases,
169 sixth-core factorizations and 3,376 resonant pair cases, including
1,408 unequal pairs. Negative controls expose missing short Möbius
signs, conjugation, repeated-prime allocations, the content mask,
the determinant content factor, the prime-extraction sign and the
incorrect removal of natural zeros from a sixth power.

These checks do not establish an asymptotic HLC bound, the original
paper's theorem, or the new affine hypothesis. The analytic implication
remains explicitly conditional.
