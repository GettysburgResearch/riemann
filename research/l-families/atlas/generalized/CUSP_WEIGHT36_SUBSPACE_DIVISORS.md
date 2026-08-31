# Actual weight-36 subspaces: Hecke planes are not pole-protected

Status: proposed theorem, independent exact-source review required.
Scope: the actual fixed space `S_36(SL_2(Z))`, and every fixed complex subspace
of dimension one or two. This is not a growing-weight conclusion, a numerical
zero census, or an RH statement. Authoring base:
`ec5bdd9b02ea68bddfcf34ac40a85d283faf64cf` (weight-24 FI source).

Arithmetic class: **MIXED: EXACT_RATIONAL / CERTIFIED_INTEGER_COVERAGE**;
rounding: **none**. The finite controls use integer/rational polynomials and
Gaussian-rational matrices, with no floating eigenvalues or divisor samples.
The analytic lifting, common-prime value theorem, Nullstellensatz and contour
arguments are not machine-certified numerical outputs.

## 1. The theorem and the actual quotient

Let `f_1,f_2,f_3` be the real, first-q-coefficient-one simultaneous Hecke
eigenforms in `S_36`, ordered by their eigenvalues at two. Use the same literal
completed Eisenstein series as FI, with `-I` included in `Gamma_infinity`,
the full fundamental domain, and `dmu=dx dy/y^2`:

\[
 I_s(u,v)=\int_{\mathcal F} y^{36}\overline{u(z)}v(z)E^*(z,s)d\mu.
                                                               \tag{SD1}
\]

For a fixed `j`-dimensional complex subspace `W`, `j=1,2`, choose an
orthonormal coefficient matrix `V` in this fixed eigenbasis (`V^*V=1_j`).
This is Euclidean coordinate normalization, not Petersson normalization.
Complete it to a unitary coefficient basis of the full space, and put

\[
 Q_W(s)=\frac{\det I_s|_{(f_1,f_2,f_3)}}{
                  \det I_s|_{\operatorname{columns}(V)}}.
                                                               \tag{SD2}
\]

The same numerator results in the completed unitary basis. Other fixed
nonzero quotient coordinates change SD2 only by a positive nonzero constant;
the divisor depends only on `W`. In particular the canonical first-q-coefficient
hyperplane is included. The empty and full subspaces are excluded.

**Theorem SD.** Among all these proper nonzero subspaces, precisely the three
one-dimensional Hecke eigenlines have quotients with no poles on `Re s>1`.
For every other fixed `W` there is `eta_W>0` such that every fixed substrip
`1<sigma_1<sigma_2<=1+eta_W` contains at least `c_W T` distinct genuine poles
of `Q_W` at heights `0<Im s<=T`, for all sufficiently large `T`.

Every fixed `W`, including the three eigenlines, has the analogous lower
bound for distinct genuine zeros in each sufficiently near-one fixed substrip.
The constants and onset may depend on `W` and the strip. No effective width,
onset, location, multiplicity or simplicity claim is made.

In particular **every two-dimensional subspace has infinitely many genuine
poles**, including each plane spanned by two Hecke eigenforms. Thus being
Hecke-stable is not sufficient for pole protection. The fixed dimension here
does not contradict or extend the separate large-weight low-rank concentration
theorem: its limiting parameter and its near-`s=1` chamber are different.

## 2. Preregistered native arithmetic and all seven analytic inputs

The canonical Miller basis is the row-echelon basis obtained from
`Delta E4^6, Delta^2 E4^3, Delta^3`, with first three q coefficients the
identity. The alternative `Delta E6^4, Delta^2 E6^2, Delta^3` construction
gives the same basis. The frozen HC producer supplies both primitive routes
at its declared `q^18` cap; that cap was not enlarged. In this basis,

\[
 T_2=\begin{pmatrix}
 0&1&0\\
 34416831456&194184&-72\\
 5681332472832&-197264484&-54528
 \end{pmatrix},
\]

\[
 T_3=\begin{pmatrix}
 0&0&1\\
 5681332472832&-197264484&-54528\\
 113919917500913904&-228302364672&92389176
 \end{pmatrix}.                                        \tag{SD3}
\]

The matrices commute, and their complete checked action within `q^18`
reaches index nine for `T2` and index six for `T3`, beyond the three pivots.
The characteristic polynomial is

\[
 P(t)=t^3-139656t^2-59208339456t-1467625047588864.         \tag{SD4}
\]

The preregistered conditions were distinct real roots, no zero root, and no
opposite pair of roots. They hold: the discriminant is
`606037485049196709344808901017600>0`, the constant term is nonzero, and

\[
 \operatorname{Res}(P(t),P(-t))
 =-1113023000511109845739295110772461437714432000000\ne0.
                                                               \tag{SD5}
\]

These exact predicates were specified before the computation, not inferred
from a sampled eigenvalue plot. Sturm controls independently place the three
roots in `(-165110,-165109)`, `(-26809,-26808)`, and `(331573,331574)`.

Write the roots as `alpha_i`. Commuting Hecke operators preserve the three
simple `T2` eigenspaces. A nonzero simultaneous eigenform has nonzero first
coefficient: otherwise `(T_n f)_1=a_f(n)` would force all its coefficients to
vanish. Its real eigenline can thus be normalized by `a_f(1)=1`.
The source rows give

\[
 a_{f_i}(2)=\alpha_i,\qquad
 a_{f_i}(3)=\frac{34416831456+194184\alpha_i-\alpha_i^2}{72}.
                                                               \tag{SD6}
\]

The polynomial conditions imply both that the three `alpha_i^2` are distinct
and that the three pair products `alpha_i alpha_l` (`i<l`) are distinct.
For the latter, any equality of different pairs shares a nonzero root and
would imply equality of the remaining roots.

Use unitary normalization `lambda_i(n)=a_{f_i}(n)n^(-35/2)` and define

\[
 Z=\zeta(s),\quad S_i=L(s,\operatorname{sym}^2 f_i),\quad
 C_{il}=L(s,f_i\times f_l),\quad i<l.                    \tag{SD7}
\]

There are **seven** primitive objects, of degrees `1,3,3,3,4,4,4`.
All lifting and distinction hypotheses must be paid before using common-prime
flexibility. The proof is the FI section-3 argument with its inputs checked
anew: each level-one GL2 representation has trivial central character and is
unramified at every finite prime. Any self-twist, or twist relating two such
representations, must be quadratic. A ramified quadratic character gives
nontrivial scalar inertia, so cannot preserve an unramified parameter. There
is no nontrivial quadratic character of Q unramified at every finite prime.
Distinct `alpha_i` exclude the remaining trivial twist. This also excludes
dihedral induction and its associated quadratic self-twist.

Gelbart--Jacquet therefore supplies three cuspidal adjoint GL3 lifts, equal
here to symmetric squares because the central characters are trivial.
Ramakrishnan supplies the three cuspidal GL4 tensor products, since each
pair is non-dihedral and not twist-equivalent. At prime two their coefficients
are respectively `alpha_i^2/2^35-1` and `alpha_i alpha_l/2^35`.
SD5-SD6 distinguish the inputs within each equal degree; degrees distinguish
the remaining groups. Deligne gives unit-modulus finite GL2 Satake parameters;
their explicit symmetric-square and tensor products give the finite-place
Ramanujan bounds for all six lifts. No general GL4 Ramanujan conjecture is used.

The primitive local identity FI6, valid for every pair of these eigenforms,
and literal unfolding now give

\[
 I_s|_{(f_i)}=A_{36}(s)M(s),\quad
 A_{36}=\pi^{-s}\Gamma(s)(4\pi)^{-s-35}\Gamma(s+35),
\]
\[
 M_{ii}=ZS_i,\quad M_{il}=M_{li}=C_{il}\ (i<l),\qquad
 Q_W=A_{36}^{3-j}\frac{\Delta(M)}{P_W(M)},
 \quad \Delta(M)=\det M,\quad P_W(M)=\det(V^*MV).
                                                               \tag{SD8}
\]

The cross entries agree meromorphically because the eigenforms have real
q coefficients; they are not zero. For complex `s`, `M` is symmetric but
not asserted Hermitian. The `V^*` in SD8 cannot be replaced by `V^T`.
The factor `A36` is holomorphic and nonzero on `Re s>1`.

## 3. Exact symmetric-matrix algebra: all subspaces, not just samples

Let

\[
 M=\begin{pmatrix}x&a&b\\a&y&c\\b&c&z\end{pmatrix},\qquad
 \Delta=(xy-a^2)z-(xc^2+yb^2-2abc).                     \tag{SD9}
\]

This polynomial is irreducible over C. Indeed `xy-a^2` is a primitive
linear polynomial in `y` over the UFD `C[x,a]`, hence irreducible by Gauss's
lemma. It does not divide the second bracket: at `x=y=a=1,b=0,c=1`, the
first polynomial is zero and the bracket is one. Thus SD9 is primitive and
linear in `z` over `C[x,y,a,b,c]`; Gauss's lemma proves irreducibility.

For fixed `V` of rank `j`, Cauchy--Binet on diagonal `M` gives

\[
 P_W(\operatorname{diag}(x_1,x_2,x_3))
   =\sum_{|I|=j}|\det V_I|^2\prod_{i\in I}x_i.          \tag{SD10}
\]

The polynomial is nonzero and homogeneous of degree `j`. If it were a
monomial in all six symmetric entries, its nonzero diagonal restriction
would also be a monomial. SD10 would have exactly one nonzero Pluecker
coordinate. For `j=1` that means a coordinate line. For `j=2`, after choosing
the two pivot rows, the other row must be zero: its two minors with the pivot
rows vanish. Thus `W` is a coordinate plane. But a coordinate plane has
`P_W=constant*(x_i x_l-m_il^2)`, not a monomial. Consequently

\[
 P_W\text{ is a monomial}\quad\Longleftrightarrow\quad
 j=1\text{ and }W\text{ is a coordinate eigenline}.     \tag{SD11}
\]

If `P_W` is not a monomial, it has an irreducible noncoordinate factor `F`.
Its degree is at most two, so it cannot divide the irreducible cubic `Delta`.
It cannot divide any coordinate variable either. By the Nullstellensatz,
the hypersurface `F=0` therefore has a complex point with

\[
 P_W(M)=0,\qquad\Delta(M)\ne0,\qquad xy z a b c\ne0.
                                                               \tag{SD12}
\]

For clarity, if no such point existed, `Delta*x*y*z*a*b*c` would vanish
on `F=0`, hence a power would lie in `(F)`. Since `(F)` is prime, `F` would
divide that product, a contradiction. Conversely irreducibility and
`deg P_W<3` show that `Delta=0` has a point with `P_W!=0` and all six
entries nonzero. These are torus targets, not targets with an Euler-product
entry equal to zero. The general factor/zero-set implication is the classical
Nullstellensatz; see Stacks, Theorem 10.34.1 (tag 00FV).

An explicit held-out Hecke-plane falsifier is especially useful:

\[
 M_0=\begin{pmatrix}1&1&1\\1&1&2\\1&2&1\end{pmatrix},
 \quad P_{\langle e_1,e_2\rangle}(M_0)=0,\quad\Delta(M_0)=-1.
                                                               \tag{SD13}
\]

Every entry is nonzero. Permuting coordinates treats all three Hecke-stable
planes. This is not by itself an actual period counterexample: the next
section supplies the seven-input analytic realization and contour transfer.

## 4. Native nonconstancy and complete tails

Each entry of `M(s)` equals
`zeta(2s) sum_n a_{f_i}(n)a_{f_l}(n)n^(-s-35)`. For `V` fixed, expansion
of the corresponding Gram determinant by Cauchy--Binet gives nonnegative
ordinary Dirichlet coefficients: they are squared absolute Fourier minors,
multiplied by coefficients of `zeta(2s)^j`. These expansions are absolutely
convergent on `Re s>1`, by the finite-place coefficient bounds below.
The first three q functionals are independent on `S36`, so some `j` by `j`
Fourier minor using indices among `1,2,3` is nonzero. Thus `P_W(M(s))` has
a nonzero coefficient at some index at most six, for every such `W`.

For the full determinant, SD6 makes the first-three-q determinant equal
to `-Vandermonde(alpha_1,alpha_2,alpha_3)/72`. Consequently the first
nonzero ordinary Dirichlet coefficient of `Delta(M(s))` is exactly

\[
 [6^{-s}]\Delta(M(s))=\frac{\operatorname{disc}P}{72^2\,6^{35}}>0.
                                                               \tag{SD14}
\]

Indices one through five and index seven vanish. As an additional prediction
made before the coefficient computation, the Hecke recurrence
`a_f(4)=alpha^2-2^35` implies

\[
 [8^{-s}]\Delta(M(s))=\frac{\operatorname{disc}P}{8^{35}}.
                                                               \tag{SD15}
\]

Only the distinct tuple `(1,2,4)` contributes at index eight; square-divisor
factors would require an earlier nonzero full determinant coefficient and
do not contribute. The scaled ratio between SD15 and SD14 is `72^2=5184`.

Each entry of `M` has coefficient modulus bounded by `d_4(n)`. With
`V^*V=1_j`, Cauchy--Binet for its two constant coefficient factors gives

\[
 |[n^{-s}]P_W(M(s))|\le j!\binom3j d_{4j}(n),\qquad
 |[n^{-s}]\Delta(M(s))|\le6d_{12}(n).                    \tag{SD16}
\]

Indeed the bound for a `j` by `j` matrix minor is `j! d_(4j)`, and
`(sum_I |det V_I|)^2 <= binom(3,j) sum_I |det V_I|^2=binom(3,j)`.
Thus the constants are `3 d4` for lines, `6 d8` for planes, and `6 d12`
for the full determinant. These bound the entire omitted tails uniformly in
all common prime phases. FI13 gives an explicit tail tending to zero on each
closed sub-half-plane inside `Re s>1`.

## 5. Actual realization, noncancellation, and distinct-point counting

Apply the correction-aware Booker--Thorne Proposition 3.1 to the seven
verified inputs SD7. Take the prime cutoff `3/2`, so no primes are omitted.
For a target matrix from SD12 set `Z=1`, take the three `S_i` to be its
diagonal entries and the three `C_il` to be its off-diagonal entries. All
seven coordinates are nonzero. Choose an annulus containing them. The theorem
realizes this tuple at every sufficiently near-one real sigma using a single
common phase at each prime. The reflected zero target is treated identically.
The explicit SD13 target lies in the fixed annulus `R=2`.

Because `P_W` and `Delta` are constant-coefficient homogeneous polynomials
in the entries, their twisted ordinary Dirichlet coefficients are their
untwisted coefficients multiplied by the same `chi(n)`. Their first nonzero
coefficients from section 4 survive, so neither twisted function is identically
zero. No automorphy of the arbitrary prime twist is asserted.

At the pole target, choose a small closed disk about sigma, strictly inside
the desired substrip, with `Delta_chi` nonzero on the full disk and
`P_{W,chi}` nonzero on its boundary. Pay both tails in SD16; simultaneously
approximate the finitely many remaining prime phases by one vertical shift.
Rouche produces denominator zeros while the full-disk numerator margin
excludes cancellation. The holomorphic nonzero factor `A36^(3-j)` leaves
genuine poles of the actual `Q_W`. At the zero target interchange the roles.

Prime-log rational independence gives positive lower density of good positive
shifts. A fixed divisor lies in translated radius-rho disks for at most
`2 rho` measure of shifts. Restricting shifts to `rho<t<T-rho` therefore
gives the distinct-point lower bound `c_W T` separately for zeros and poles,
without a multiplicity estimate. This is the FI paired-contour argument with
the new targets and complete degree-12 tails, not a denominator-zero inference.

For a coordinate eigenline `P_W=ZS_i`, which has no zeros on `Re s>1` by
absolute Euler-product convergence. Both the full determinant and `A36` are
holomorphic there, so its quotient has no poles. All noncoordinate lines
and all planes have SD12 targets. This completes the classification.

## 6. Finite replay, prior art, and boundaries

The producer replays the frozen HC primitive modular-series/echelon source,
checks both constructions, Hecke action beyond the pivots, characteristic and
resultant identities, exact root-isolation controls, and the held-out
SD14-SD15 determinant coefficients. Bounded polynomial controls implement
`det(V^* M V)` for declared Gaussian-rational subspaces, retain conjugation,
and verify the explicit noncancelling Hecke-plane target and Pluecker diagonal
identities. That finite subspace list is not an exhaustive Grassmannian census.
Those control matrices need not be orthonormal: their positive Gram determinant
is recorded, and the normalized quotient is
`det(V^*V) A36^(3-j) Delta/P_W`. This changes no divisor or protected target.
All full-determinant coefficients through index 36 are covered: a distinct
tuple `a<b<c` with `abc<=36` has `c<=18`, so the frozen Fourier cap suffices;
the square-divisor contributions from `zeta(2s)^3` are retained.

All local arithmetic is exact, with explicit type/bit/work/byte/tree caps.
The fixture is reconstructed from frozen primitive sources and four current
artifact hashes, with literal Git blob and LF-normalized SHA256 bindings.
Normal and optimized Python have the same strict rejection contract. No
numerical period, infinite prime product, prime phase, or zero is evaluated.

Primary analytic inputs are [Gelbart--Jacquet](https://www.numdam.org/article/ASENS_1978_4_11_4_471_0.pdf)
Theorem 9.3, [Ramakrishnan](https://www.maths.tcd.ie/EMIS/journals/Annals/152_1/ramak.pdf)
Theorem M and Proposition 2.3.1, and
[Booker--Thorne](https://msp.org/ant/2014/8-9/ant-v8-n9-p01-s.pdf)
Proposition 3.1 with its [correction](https://msp.org/ant/2014/8-9/ant-v8-n9-x01-Correction-ZerosOfLFunctions.pdf).
The required algebraic zero-set implication is the classical
[Nullstellensatz](https://stacks.math.columbia.edu/tag/00FV).
These are established theories, not claimed new abstract results.

The source-specific conclusion is a rank-three classification and a rigorous
failure of blanket Hecke-stable-plane protection. It proves neither a theorem
for all weights nor an unrestricted Euler-flexibility hypothesis for arbitrary
automorphic inputs. It supplies no optimal eta, effective height onset,
unsigned asymptotic, simplicity or critical-line theorem, and no RH implication.
