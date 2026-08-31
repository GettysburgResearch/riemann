# Segre recurrence, syzygy Euler sums, and specialization

Status: proposed exact algebra; classical Segre/Koszul mechanisms, not a new
automorphic family or an analytic completion. Independent frozen review pending.
Scope: finite-dimensional complex polynomial representations; formal local
series. The rank-three computations below are finite exact rational algebra.
Base: `7ee5e024e1d8c3dd187b40ea5d48f9c9ff46d95e`.

## Preregistered held-out controls

Recorded before constructing the new rank-three maps in this worktree:

1. For three rank-three factors, the degree-one Segre module has dimension
   27; the quadratic ideal has dimension 162; the actual cubic linear-syzygy
   module has dimension 1720; the cubic quadratic-dual algebra has dimension
   9019. These are distinct objects, not four descriptions of one space.
2. With A=Sym^3, B=S_(2,1), and C=Lambda^3 on a rank-three factor, the cubic
   syzygy character is the sum of all six placements of A tensor B tensor C,
   plus two copies of B tensor B tensor B, plus all three placements of
   B tensor B tensor C, plus all three placements of B tensor C tensor C.
   Its dimension is 480+1024+192+24=1720. This classical prediction is also
   obtained from Snowden's section 4.7, Figure 1, cubic part of f_3.
3. Let omega be a primitive cube root of unity and specialize the diagonal
   action to diag(1,omega,omega^2). Then h_r is 1 for 3 dividing r and zero
   otherwise, so every positive coefficient power has series 1/(1-T^3).
   For power three the universal Sym^3-denominator numerator must be
   (1-T)(1-T^3)^2, while the ambient Segre K-polynomial is (1-T^3)^8.
   The actual 1720-dimensional cubic syzygy module must have trace -8 and
   eigenvalue multiplicities (568,576,576) at (1,omega,omega^2).

These predictions will be checked against actual maps and whole characters,
not used to set their matrix ranks. A failure is a failed prediction.

### Additional analytic predictions, before the slice producer

For A=diag(t,1,t^-1), x=t+t^-1, set C_1=x, C_2=x^2-2,
C_3=x^3-3x. The cubic coefficient series is predicted to equal P_x/D_7,
where

\[
D_7=(1-T)\prod_{j=1}^3(1-C_j(x)T+T^2),\qquad
P_x=1+B T+C T^2+B T^3+T^4,
\]
\[
B=2x^2+5x+2,\qquad C=x^3+6x^2+7x+2.
\]

The reciprocal spectrum polynomial is z^2+Bz+(C-2), with discriminant
Delta=4x^4+16x^3+9x^2-8x+4. For unitary input, x in [-2,2], the defect
is pure exactly on [x_*,0], where x_* is the unique root of Delta in
(-5/3,-13/8). This statement includes multiplicities and reduction.
At the additional nonunitary controls x=-3 and x=-8, the reduced numerator
is respectively (1+T)^2 and (1-T)(1+92T+T^2), with denominator degrees
5 and 6. These are cancellations without coincident input eigenvalues.

## 1. Classical inputs and what this packet adds

The Segre ring, Koszul duality, and low-degree Segre syzygies are classical.
[Snowden, *Syzygies of Segre embeddings*](https://websites.umich.edu/~asnowden/papers/segre-111810.pdf),
section 1.1, distinguishes canonical Tor modules from choices of a minimal
resolution; Lemma 3.3 gives the additive equivariant Hilbert-series argument;
section 4.7, Figure 1 supplies the low-syzygy character prediction.
[Gorbounov--Schechtman](https://sigma-journal.com/2009/034/sigma09-034.pdf),
sections 3.4.1--3.4.5, supplies the classical Koszul--Lie formal product.

The frozen parent proves the actual sorting presentation and Koszul property.
We retain its V rather than V* convention for coordinate generators. We do
not substitute Tor over the Segre ring for Tor over its ambient polynomial
ring. The present gains are a source-specific three-object dictionary,
explicit reduction strata, a native 27-generator full-character replay, and
a rank-three self-dual slice with a rigorously delimited purity chamber.
No publication-priority or exhaustive novelty claim is made.

PR #781 was read at d4fa9dcc88beddbf0dbb978e1c64091086bd8825.
Its delta from ac1cc5eaf229087b6d805e908897c7c8c99a58b7 is graph-only.
The deformation-spectrum and codimension proofs are comparison context,
not imported theorems or machine-authenticated dependencies here. In
particular this packet reproves its own backward-continuation statements.
A spectrum constructed from polynomial roots is not thereby a natural
representation or a syzygy action. Its signs must be read from the actual
factor 1-zT+b^m T^2, whose trace is z, not -z.

## 2. Three objects, with their coefficient rings fixed

Fix n,m>=1, V=C^n, A in GL(V), and put

\[
 E=V^{\otimes m},\quad S=\operatorname{Sym}(E),\quad
 R=\bigoplus_{r\geq0}(\operatorname{Sym}^r V)^{\otimes m},\qquad
 F_A(T)=\sum_{r\geq0}h_r(A)^m T^r.
 \tag{SB1}
\]

The multiplication in R is coordinatewise multiplication. It is fixed
before any character is evaluated. The product GL(V)^m action restricts to
the diagonal GL(V); h_r(A)^m is exactly the trace on R_r. All statements
refer to formal power series and rational functions, not an all-prime product.

**Ambient syzygy Euler polynomial.** The finite minimal S-resolution gives

\[
 K_R(A,T)=\sum_{i,j}(-1)^i
   \operatorname{Tr}(A\mid\operatorname{Tor}^S_i(R,\mathbb C)_j)T^j,\qquad
 F_A(T)=\frac{K_R(A,T)}{D_E(A,T)},\quad
 D_E=\det(1-T A^{\otimes m}).
 \tag{SB2}
\]

Indeed an equivariant free term S tensor B(-j) contributes
Tr(A|B)T^j/D_E. Taking the Euler characteristic degree by degree proves
(SB2). Hilbert's syzygy theorem makes this a finite sum. The canonical
objects are the Tor modules and their actions; choosing maps and free
modules in a particular minimal resolution involves noncanonical choices.

**Universal recurrence numerator.** Set
\[
 N_0=\binom{n+m-1}{m},\qquad
 D_{\rm sym}(A,T)=\det(1-T\operatorname{Sym}^m A),\qquad
 N_{\rm univ}(A,T)=D_{\rm sym}(A,T)F_A(T).
 \tag{SB3}
\]
Theorem SB3 below proves that N_univ is a polynomial with polynomial
character coefficients, not merely a rational expression.

**Reduced numerator.** For each specific A, divide N_univ and D_sym by
their greatest common divisor g_A, normalized to constant coefficient one:
\[
 P_A=N_{\rm univ}/g_A,\qquad Q_A=D_{\rm sym}/g_A,\qquad F_A=P_A/Q_A.
 \tag{SB4}
\]
The notation N_rec means P_A only on the specified reduced stratum. It
must not mean the universal numerator before specialization.

### Theorem GLO764.SEGRE_RECURRENCE_DICTIONARY_V1

Let C=E/Sym^m V, the canonical quotient by the symmetrization summand
(characteristic zero). Then, for every A in GL(V),

\[
 \boxed{K_R(A,T)=N_{\rm univ}(A,T)\det(1-T A\mid C).}
 \tag{SB5}
\]

Proof: the equivariant splitting E=Sym^m V direct-sum C gives
D_E=D_sym det(1-TA|C). Substitute (SB2)--(SB3), initially formally, and
use the polynomial conclusion below. This is an identity of character
polynomials, with no choice of syzygy differential or spectral roots.

**Off-purity divisor corollary.** Suppose every eigenvalue of A has
absolute value R>0. Then K_R, N_univ and the true reduced numerator P_A
have the same inverse-root divisor off the circle |lambda|=R^m, including
multiplicities. In particular their purity verdicts agree, with a constant
numerator counted as vacuously pure. Indeed every inverse root of D_E,
D_sym, det(1-TA|C), and g_A has absolute value R^m. Multiplying by or
cancelling those factors cannot change an off-circle divisor. This is a
valid spectrum consequence of the syzygy Euler identity, without a finite
syzygy superdeterminant. It is not asserted for nonpure input data.

## 3. Generic denominator, exact cancellation, and specialization strata

For distinct nonzero eigenvalues alpha_1,...,alpha_n, partial fractions give

\[
 h_r(A)=\sum_{i=1}^n c_i\alpha_i^r,\qquad
 c_i=\frac{\alpha_i^{n-1}}{\prod_{j\ne i}(\alpha_i-\alpha_j)}.
 \tag{SB6}
\]
Each c_i is nonzero. Therefore
\[
 F_A(T)=\sum_{|\nu|=m}
 \frac{b_\nu}{1-\alpha^\nu T},\qquad
 b_\nu=\frac{m!}{\nu_1!\cdots\nu_n!}\prod_i c_i^{\nu_i}.
 \tag{SB7}
\]

If all N_0 monomials alpha^nu are distinct, every residue coefficient is
nonzero and the reduced denominator is exactly D_sym. These inequalities
define a nonempty Zariski-open set: independent indeterminates satisfy them.
No positivity assumption is used.

When input eigenvalues are still distinct but product eigenvalues collide,
group (SB7) by lambda=alpha^nu. The exact reduced denominator is
\[
 \boxed{Q_A(T)=\prod_{\lambda:\ B_\lambda\ne0}(1-\lambda T),\qquad
 B_\lambda=\sum_{\nu:\alpha^\nu=\lambda}b_\nu.}
 \tag{SB8}
\]
Distinct simple partial fractions are linearly independent. Thus both
product collisions AND cancellation of their summed coefficients matter.
Repeated input eigenvalues are outside formula (SB6), but not outside
(SB3)--(SB5): they use polynomial specialization, followed by actual gcd
reduction. Confluent poles can have multiplicity greater than one.

### Degree, leading coefficient, and inverse-matrix reciprocity

The canonical backwards continuation of h_r satisfies
\[
 h_{-1}=\cdots=h_{-(n-1)}=0,\quad
 h_{-n}=(-1)^{n-1}(\det A)^{-1},
\quad
 h_{-r}(A)=(-1)^{n-1}(\det A)^{-1}h_{r-n}(A^{-1})\ (r\ge n).
 \tag{SB9}
\]
For distinct roots these follow from (SB6), Lagrange interpolation and
replacing alpha_i by alpha_i^-1. Equivalently one can run the order-n
recurrence backwards, whose last coefficient is nonzero. Both sides are
rational functions of the matrix entries with powers of det(A) allowed;
hence the identities persist when eigenvalues coincide.

For any finite exponential-polynomial sequence phi(r), linearity and
applying powers of T d/dT to 1/(1-lambda T) prove
\[
 \sum_{r\ge0}\phi(r)T^r
   =-\sum_{j\ge1}\phi(-j)T^{-j}
 \quad\hbox{as the Laurent expansion at infinity}.
 \tag{SB10}
\]
This is not an equality of two convergent series in the same annulus.

Taking phi=h^m, (SB9)--(SB10) prove properness, deficit n, and
\[
 \deg N_{\rm univ}=N_0-n,\qquad
 [T^{N_0-n}]N_{\rm univ}
 =(-1)^{N_0+1+m(n-1)}(\det A)^{mN_0/n-m}.
 \tag{SB11}
\]
Here mN_0/n=binomial(n+m-1,m-1) is an integer. First prove (SB11)
generically using (SB7). Each coefficient of D_sym F_A is a polynomial
class function of A, so every coefficient above N_0-n vanishes
identically. The displayed nonzero leading coefficient persists on GL(V).
Thus N_univ is the promised universal polynomial for all A.
After reduction the exact statement is
\[
 \deg Q_A-\deg P_A=n.
 \tag{SB12}
\]
A specialization can lower both degrees while preserving this deficit.

The stronger equivariant reciprocity, valid in every rank, is
\[
 F_A(T^{-1})=(-1)^{1+m(n-1)}(\det A)^{-m}T^n F_{A^{-1}}(T).
 \tag{SB13}
\]
Multiplying by the determinant reciprocity gives
\[
 N_{\rm univ}(A,T)=
 (-1)^{N_0+1+m(n-1)}(\det A)^{mN_0/n-m}
 T^{N_0-n}N_{\rm univ}(A^{-1},T^{-1}).
 \tag{SB14}
\]
This normally compares A with A^-1, not a polynomial with itself.
A scalar palindromy law at fixed A needs an additional self-duality
relation on A. Section 7 supplies such a genuine rank-three slice.

### Finite rank strata, including confluent inputs

Put c_r=h_r(A)^m and let H(A)=(c_(i+j))_(0<=i,j<N_0).
Then
\[
 \boxed{\deg Q_A=\operatorname{rank}H(A).}
 \tag{SB15}
\]
The universal recurrence from D_sym expresses every later column of the
infinite Hankel matrix as a combination of its first N_0 columns.
It also expresses every later row as a combination of its first N_0
rows. Thus the finite displayed block has the infinite Hankel rank.
On the span of infinite columns, shifting is well-defined and invertible,
because the universal recurrence has nonzero last coefficient.
The first dependence in the Krylov sequence of columns gives its minimal
recurrence; conversely any order-d recurrence bounds the rank by d.
This proves (SB15), including repeated eigenvalues.

Consequently the locus deg Q_A<=d is cut out by the (d+1)-minors of
H(A), and exact-order strata are constructible. In an algebraic family,
the order can drop at specialization; this is not an assertion of
monotonicity along arbitrary parameter paths. Formula (SB8) describes
the simple-input strata explicitly. Syzygy module dimensions need not
change at all when this observable's recurrence order drops.

## 4. Additive Euler sum is not a superdeterminant

An alternating trace is not a superdeterminant. The latter involves all
powers of its operator through log det(1-TB)=-sum_{r>=1}Tr(B^r)T^r/r;
it does not follow from one additive Euler identity. Tor over S, Tor over
R, and the dual Lie generators also have different roles.

For n=m=2, delta=det A,
\[
 F_A(T)=\frac{1+\delta T}
 {(1-\alpha^2T)(1-\delta T)(1-\beta^2T)},\quad
 N_{\rm univ}=1+\delta T,\quad K_R=1-\delta^2T^2.
 \tag{SB16}
\]
The ambient ring has one quadratic relation of character delta^2.
Its Euler polynomial is K_R, not N_univ.

### Theorem GLO764.SEGRE_SYZYGY_SUPERDET_BOUNDARY_V1

There is no universal finite product of graded determinants of natural
representation actions (allowing virtual representations) realizing
N_univ for rank two/power three, or rank three/power three.

At A=I_2 the first numerator is 1+4T+T^2. Its roots -2+-sqrt(3)
are not roots of unity. Every finite product
prod_j det(1-T^j R_j(A))^{e_j}, e_j integers, specializes at A=I
to prod_j(1-T^j)^{e_j dim R_j}, whose zeros and poles are roots of
unity. Even inserting fixed parity signs only adds factors 1+T^j
and does not evade this obstruction.

For the rank-three cubic case,
\[
 F_{I_3}(T)=\frac{1+20T+48T^2+20T^3+T^4}{(1-T)^7},\quad
 N_{\rm univ}(I_3,T)=(1-T)^3(1+20T+48T^2+20T^3+T^4).
 \tag{SB17}
\]
The quartic equals T^2((T+T^-1)^2+20(T+T^-1)+46).
Its two z-roots are -10+-3sqrt(6), both less than -2 because 54<64.
Hence all its roots are negative real and nonunit, giving the same
contradiction. This also rules out a finite natural-syzygy determinant
interpretation of the ambient K-polynomial in these cases, since the
extra determinant in (SB5) has only unit roots at the identity.

This does NOT exclude assigning an auxiliary companion matrix to a
polynomial, a spectral multiset over an algebraic closure, or an additional
operator unrelated to the natural A-action. Such a construction requires
its own definition, functoriality and proof; it is not supplied by (SB2).
Nor does the theorem deny that a finite polynomial of virtual characters
is an additive Euler class. It forbids the stated finite multiplicative
interpretation. The parent's infinite Koszul--Lie product remains valid.

## 5. Actual rank-three quadratic/cubic maps and the complete character

The producer builds the 27 generators indexed by (i,j,k) in {0,1,2}^3.
In degree two, commutative monomials are grouped by their three coordinate
multisets. Multiplication sends every monomial in a fibre to the same
basis vector of R_2. Subtract a fixed fibre anchor from each other
monomial: these 162 independent binomials form a basis of I_2.

Multiply these actual binomials by every generator and map into
Sym^3(E). The resulting 4374 two-term columns in 3654 rows have exact
rational rank 2654, split across all 1000 product-torus weights. The
kernel is precisely Tor^S_2(R,C)_3: there are no degree-one relations,
and the ideal is generated by quadrics. It has dimension 1720.
The image fills I_3 in every weight, not only in total dimension.

A second construction takes Q=im(R_2* -> E* tensor E*), with the native
relation in each ordered-pair fibre equal to the sum of all its words.
It computes the actual quotient by Q tensor E* + E* tensor Q in tensor
degree three. There are 19683 words and 11664 columns of rank 10664;
the quotient dimension is 9019. Adding the nested odd brackets
xyz+xzy-yzx-zyx gives a rank increase of 1720, weight by weight.
The reported positive weights are those of the DUAL of this Lie module,
consistent with the parent's contravariant-generator convention.

A separate graph-incidence algorithm computes the rank of the bar map
\[
 d_3(a,b,c)=((ab),c)-(a,(bc)).
 \tag{SB18}
\]
Its graph has one connected component in each of the 1000 weights and
11664 vertices in total. Thus rank d_3=11664-1000=10664. Also d_2d_3=0
literally, and d_2 has one-dimensional image in each weight. Hence
Tor^R_2(C,C)_3=0 and dim Tor^R_3(C,C)_3=9019. The bar/dual matrices are
transposes up to signs on one summand; the algorithms (incidence versus
rational elimination) are independent rank computations, not independent
infinite proofs.

Write A_i=Sym^3(V_i), B_i=S_(2,1)(V_i), C_i=Lambda^3(V_i).
The entire 1720-dimensional character recovered from the maps is
\[
 \sum_{\text{six placements}} A_1\otimes B_2\otimes C_3
 +2B_1\otimes B_2\otimes B_3
 +\sum_{\text{three placements}} B_1\otimes B_2\otimes C_3
 +\sum_{\text{three placements}} B_1\otimes C_2\otimes C_3.
 \tag{SB19}
\]
The placement notation permutes the module types among the three factors.
Its dimension is 480+1024+192+24. The checker independently constructs
each Schur character using semistandard tableaux: for shape (2,1) the
entries satisfy a<=b and a<c. It compares all 460 nonzero weight
multiplicities, not just 1720. The central weight (012,012,012) has
syzygy multiplicity 46 and quadratic-dual multiplicity 163.

This is a classical character, newly used as an independently preregistered
27-generator replay. It neither implies that all syzygies are linear nor
identifies the finite S-resolution with the infinite R-Koszul resolution.

## 6. A complete cyclic collapse with nontrivial syzygy spectrum

Let A=diag(1,omega,omega^2), omega^3=1, omega!=1. Since
det(1-uA)=1-u^3, h_r(A) is the indicator of 3 dividing r. Thus for
EVERY positive integer m,
\[
 F_A(T)=1/(1-T^3).
 \tag{SB20}
\]
For m=3, Sym^3(A) has multiplicities (4,3,3) at (1,omega,omega^2);
A tensor A tensor A has multiplicities (9,9,9). Consequently
\[
 D_{\rm sym}=(1-T)(1-T^3)^3,\quad
 N_{\rm univ}=(1-T)(1-T^3)^2,\quad K_R=(1-T^3)^8,
\quad (P_A,Q_A)=(1,1-T^3).
 \tag{SB21}
\]
The generic order ten has dropped to three, but the 1720-dimensional
syzygy module has not vanished. Its exact eigenvalue multiplicities
computed from (SB19) are (568,576,576), and its trace is -8.

For an independent trace check, Tr(A|E)=Tr(A^2|E)=0 and Tr(A^3|E)=27,
so Tr(A|Sym^3 E)=9. The exact sequence for cubic linear syzygies gives
Tr(A|Tor^S_2(R,C)_3)=0-9+Tr(A|R_3)=-8.
Reality of this integral character makes the omega and omega^2
multiplicities equal; dimension 1720 then gives the displayed census.
This is an exact countercontrol against reading reduced numerator roots
as the eigenvalues of the actual finite syzygy modules.

## 7. Rank-three reciprocal deformation and its purity chamber

### Theorem GLO764.SEGRE_CUBIC_SELF_DUAL_SLICE_V1

Let t be any nonzero complex number, x=t+t^-1, A=diag(t,1,t^-1).
Define D_7, B, C and P_x as in the preregistration above. Then
\[
 \boxed{F_A(T)=P_x(T)/D_7(x,T),\qquad
 P_x(T)=T^2 M_x(T+T^{-1}),\quad
 M_x(z)=z^2+Bz+C-2.}
 \tag{SB22}
\]
This is an exact polynomial identity over Z[x,T] after clearing D_7.
D_7 is NOT asserted reduced at every x.
On this slice the universal degree-ten denominator satisfies
D_sym=D_7(1-T)(1-xT+T^2), so
N_univ=P_x(1-T)(1-xT+T^2). The quartic P_x is an intermediate numerator,
not another name for the universal degree-seven one.

For generic t, (SB7) groups the cubic products into t^j, -3<=j<=3,
so D_7 annihilates the series. Equations (SB9)--(SB10) give numerator
degree four. Since A is conjugate to A^-1 and det A=1, (SB13) gives
F_A(T^-1)=-T^3 F_A(T); also D_7(T^-1)=-T^-7 D_7(T). Thus P_x is
reciprocal of degree four, with constant and top coefficients one.
Writing S=sum_(j=-3)^3 t^j=x^3+x^2-2x-1,
h_1=x+1 and h_2=x(x+1), its first two numerator coefficients are
\[
 B=(x+1)^3-S=2x^2+5x+2,
\]
\[
 C=x^3(x+1)^3-S(x+1)^3+
 \frac{S^2-(x^6-5x^4+6x^2-1)}2
 =x^3+6x^2+7x+2.
 \tag{SB23}
\]
This proves (SB22) generically, and hence identically as polynomial
coefficients. It therefore includes t=+-1 by specialization.
The producer separately expands the source recurrence over Q[x], not by
interpolation, and verifies thirteen complete coefficient identities.

For unitary input |t|=1, equivalently x real in [-2,2], let x_* be
the unique root in (-5/3,-13/8) of
\[
 \Delta(x)=B^2-4(C-2)=4x^4+16x^3+9x^2-8x+4.
 \tag{SB24}
\]
Then P_x, and also the true reduced numerator P_A, has every inverse
root on the unit circle exactly when
\[
 \boxed{x_*\le x\le0.}
 \tag{SB25}
\]
Multiplicity is allowed; a constant reduced numerator satisfies the
condition vacuously. This is local purity, not an RH assertion.

Proof: factor M_x(z) over C. Each z-root contributes
1-zT+T^2; its inverse roots are unitary exactly when z is real in [-2,2].
If both z-roots lie there, then |B|<=4 and M_x(-2)>=0. But
\[
 M_x(-2)=x(x+3)(x-1),\qquad M_x(2)=(x+1)^2(x+8).
 \tag{SB26}
\]
On [-2,2] the first inequality forces x<=0 or x>=1, and x>=1 is
impossible since B>=9. On [-2,0], B lies in [-9/8,2], so the vertex
-B/2 is inside [-2,2]; both endpoint values in (SB26) are nonnegative.
The roots therefore belong to [-2,2] iff Delta>=0.

For x in [-1,0],
\[
 \Delta=(2x^2+4x-1)^2+3(1-x^2)>0.
\]
For x=y-2, 0<=y<=1,
\[
 \frac{d}{dy}\Delta(y-2)=16y^3-48y^2+18y+20
 =\sum_{j=0}^3 b_j\binom3j y^j(1-y)^{3-j},
 \quad (b_0,b_1,b_2,b_3)=(20,26,16,6).
 \tag{SB27}
\]
Thus Delta is strictly increasing on [-2,-1], with endpoint values
-8 and 9. It has a unique zero there; the exact values
Delta(-5/3)=-71/81 and Delta(-13/8)=1/1024 give the declared bracket.
This proves (SB25) for P_x. Every factor of D_7 has unit inverse roots
for unitary t, so cancelling its gcd with P_x only removes unit roots.
Therefore purity before and after reduction is equivalent here.

The chamber endpoints have different meanings: at x_* the two spectrum
points coincide, while x=0 has a spectrum point at -2. At x=-1 the
reduced numerator is constant by (SB20). At x=1 the input remains
unitary but the reduced numerator is 1+7T+T^2, which is not pure.
A fixed-matrix self-dual slice in rank three thus admits a reciprocal
deformation spectrum even though generic rank-three data need not have
scalar fixed-A palindromy. No generic-rank conclusion is smuggled in.

### Nonunitary cancellation strata without coincident input roots

For t!=0,+-1, put L=(t-1)^2(t+1). The three coefficients in (SB6) are
\[
 c_t=t^3/L,\quad c_1=-t(t+1)/L,\quad c_{t^{-1}}=1/L.
\]
The coefficients of t^{+-r} in h_r(A)^3 vanish exactly when
c_1^2+c_t c_(t^-1)=0, equivalently x=-3. The coefficient of 1^r
vanishes exactly when c_1^2+6c_t c_(t^-1)=0, equivalently x=-8.
At these x the input eigenvalues are distinct and t is not a root of
unity, so there are no additional product collisions. All other grouped
coefficients are nonzero.

At x=-3,
\[
 P_x=(1+3T+T^2)(1+T)^2.
\]
The first factor cancels the two denominator weights t,t^-1, giving
degree(Q_A)=5 and P_A=(1+T)^2.
At x=-8,
\[
 P_x=(1-T)^2(1+92T+T^2).
\]
One copy of 1-T cancels the denominator weight 1, giving degree(Q_A)=6
and P_A=(1-T)(1+92T+T^2). In both cases the deficit remains three.
This explicitly separates numerator-spectrum collision, summed-residue
cancellation, and input-eigenvalue collision.

## 8. Finite computation and acceptance boundary

The default report authenticates eight immutable current parent artifacts
at G7ee5 and the frozen preregistration note at 64c8664a2fee08ae2e249743d6f784a7bec61b83.
The latter is historical and is not required to match the now-extended
current proof. All nine source bindings include exact commit, Git blob
and LF-normalized SHA-256. The fixture seals this note, producer, tests
and manifest, and seals its payload by canonical SHA-256. Acceptance
requires typed equality with fresh recomputation, not only matching
self-reported seals.

The producer checks actual finite maps. It does not import ranks from
the Hilbert numerator. The additional scalar controls compare universal
and reduced recurrences at five rational eigenvalue panels, thirteen
rational slice parameters, the exact cyclic character, symbolic Q[x]
identities, and exact discriminant/Bernstein factorizations.
There are no floating roots, numerical period integrals or prime samples.

Public ranks are strict built-in integers in 1..3, with at most three
factors and at most 19683 cubic words, checked before allocation.
Every elimination block has at most 216 rows and 512 columns; scalar
arithmetic checks a 4096-bit numerator/denominator cap, and polynomial
operations impose degree caps. JSON and source bytes are capped at 2 MiB.
Duplicate keys, floating/nonfinite JSON values, invalid types and oversized
inputs fail closed under both normal Python and -O. Resource caps apply
to the finite checker, not to the written all-parameter theorems.
JSON nesting is separately bounded by 32 before parsing.

Run from the isolated repository root:

    python -B research/l-families/atlas/generalized/segre_recurrence_syzygy_bridge.py --check
    python -B -O research/l-families/atlas/generalized/segre_recurrence_syzygy_bridge.py --check
    python -B -m unittest tests.test_segre_recurrence_syzygy_bridge
    python -B -O -m unittest tests.test_segre_recurrence_syzygy_bridge

The smallest invalidating statements are the literal map ranks and full
character comparison in section 5, or the polynomial identity and purity
criterion in (SB22)--(SB27). A mismatch cannot be repaired by relabelling
Tor or fitting a new operator after the fact. Independent exact-SHA review
is required before integration.

This supplies no Frobenius, motive, automorphic object, global continuation,
trace-class determinant, positivity principle, or new Euler product.
The frozen global natural-boundary and completion obstructions remain
unchanged. RH and GRH remain open.
