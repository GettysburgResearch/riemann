# Finite-spectrum obstruction: exact cancellation exposes an off-axis quartet

Status: PROPOSED exact synthetic mathematics; independent review pending.
Scope: finite complete polynomial spectra; every positive real evaluation packet
of the specified sizes. No actual-xi sign claim and no infinite-background theorem.
Exact sources or dependencies: the corrected entire-source convention and the
order-three theorem in `reviews/C/pass4-math-completion/proofs/XI_SOURCE_REPAIR.md`,
especially X3--X8; its X9 already supplies the polynomial countermodel below.
The new proposed object is the uniform packet obstruction and its exact witness.
The distinct-location/multiplicity distinction also appears for a different
generalized-Schur kernel in `reviews/A/FINAL_AUDIT.md`, F13. The uniform
safe-axis packet bound here is obtained directly for (SO-1). The proof uses
elementary partial fractions, polynomial interpolation and real quadratic-form
inertia. No novelty or priority claim is made.
What was actually run: `python check_exact.py`, with standard-library rational
arithmetic, validates kernel identities, exact witnesses and the stated finite
controls. The output is `exact_checks.json`.
Smallest remaining gap: independent mathematical review of this new formulation;
application to actual xi would require controlling its complete infinite background.

## 1. One quartet and one critical pair

Fix real numbers

\[
r>0,\quad c>0,\quad B>0,\quad m_0>0,\quad m>0.
\]

For polynomial source identification take integer multiplicities. Let

\[
 D(x)=(x^2+c)^2+B^2,\qquad
 E(z)=(z^2+r)^{m_0}\bigl((z^2+c)^2+B^2\bigr)^m,
\]

up to any nonzero real normalization. On the positive real axis,

\[
 F(x)=\frac{E'(x)}{E(x)}
 =\frac{2m_0x}{x^2+r}+\frac{4mx(x^2+c)}{D(x)},
 \qquad K(x,y)=\frac{F(x)+F(y)}{x+y}.
\tag{SO-1}
\]

All these denominators are strictly positive. This is the same centered
safe-real-axis kernel as in the repaired source theorem. It is not the
arbitrary-height response with a translated pole at its ordinate.

**Proposition SO-A.** Every packet of six distinct positive nodes has inertia
\((4,2,0)\), in the order (positive, negative, zero). Every packet of five
distinct positive nodes has at least one strictly negative direction.
The conclusions hold for any positive multiplicities; increasing the
multiplicity of the critical reserve does not remove the obstruction.

### An exact real feature decomposition

For a coefficient vector \(w=(w_i)\) on distinct positive nodes \(x_i\), define

\[
\begin{aligned}
A&=\sum_i w_i\frac{x_i}{x_i^2+r},&
 C&=\sum_i w_i\frac1{x_i^2+r},\\
 U&=\sum_i w_i\frac{x_i(x_i^2+c)}{D(x_i)},&
 V&=\sum_i w_i\frac{x_i}{D(x_i)},\\
 L&=\sum_i w_i\frac{c(x_i^2+c)+B^2}{D(x_i)},&
 W&=\sum_i w_i\frac1{D(x_i)}.
\end{aligned}
\]

Direct partial-fraction algebra gives the identity

\[
\boxed{
w^{\mathsf T}Kw
=2m_0 A^2+2m_0r C^2+4m U^2+\frac{4m}{c}L^2
 -4m B^2 V^2-\frac{4mB^2(c^2+B^2)}{c}W^2.}
\tag{SO-2}
\]

One derivation writes \(\lambda=c+iB\) and uses

\[
 K_{\rm quartet}(x,y)
 =4m\Re\frac{xy+\lambda}{(x^2+\lambda)(y^2+\lambda)}.
\]

The real and imaginary parts of \(x/(x^2+\lambda)\) yield
\(4m(U^2-B^2V^2)\). Those of \(1/(x^2+\lambda)\) yield
\(4m[cT^2+2B^2TW-cB^2W^2]\), where
\(T=\sum_iw_i(x_i^2+c)/D(x_i)\). Completing this square with
\(L=cT+B^2W\) gives (SO-2).

### Why no nonzero coefficient vector cancels all six features

Use the simpler feature functions

\[
\phi(x)=\left(
\frac{x}{x^2+r},\frac1{x^2+r},
\frac{x(x^2+c)}{D(x)},\frac{x}{D(x)},
\frac{x^2+c}{D(x)},\frac1{D(x)}
\right).
\tag{SO-3}
\]

Multiplying by the positive common denominator
\(P(x)=(x^2+r)D(x)\) gives six polynomials of degree at most five.
Their coefficient matrix, in ascending monomial order and the displayed
feature order, has determinant

\[
\bigl((c-r)^2+B^2\bigr)^2>0.
\tag{SO-4}
\]

For an elementary check separate even and odd columns, writing \(t=x^2\).
Each parity block is the coefficient matrix of
\((t+c)^2+B^2\), \((t+c)(t+r)\), \(t+r\), with the odd block multiplied
by \(x\). The magnitude of each block determinant is the first polynomial
evaluated at \(t=-r\), namely \((c-r)^2+B^2\).
Thus the feature numerators span all polynomials of degree at most five.

For \(n\le6\) distinct nodes, evaluation of those polynomials has row rank
\(n\) by the Vandermonde theorem. Consequently the map from node coefficients
to the six feature sums is injective. The invertible change
\((T,W)\mapsto(L,W)\) does not change this conclusion.

For six nodes that map is an isomorphism. Equation (SO-2) therefore gives
four positive and two negative squares by a real congruence. For five nodes
the four homogeneous equations

\[
A=C=U=L=0
\tag{SO-5}
\]

have a nonzero solution \(w\). Injectivity forces \((V,W)\ne(0,0)\).
Equation (SO-2) is then strictly negative. This proves SO-A without
assuming that the four positive feature columns themselves have full rank.

**Exact rational witness.** If the parameters and nodes are rational, solve
the four equations (SO-5) by exact Gaussian elimination over \(\mathbb Q\).
Any nonzero rational null vector is a strict witness. Its contraction is

\[
-4mB^2\left(V^2+\frac{c^2+B^2}{c}W^2\right)<0.
\tag{SO-6}
\]

This procedure cancels the entire positive part of this complete finite
source. It is not a pair-only contraction with an omitted background.

## 2. A source-admissible example with order-three PSD

Use the already supplied X9 example

\[
H=1024,\quad \gamma_0=1,\quad a=1/4,\quad b=1025,
\quad r=1,\quad c=b^2-a^2,\quad B=2ab,\quad m_0=m=1.
\]

Its zeros are exactly the critical pair \(\pm i\) and the quartet
\(\pm a\pm ib\), all simple. A real normalization leaves (SO-1) unchanged.
The polynomial is even and has order zero. There are no omitted roots.
The repaired source budget holds: \(1/b^2<1/(9H)\), and
\(1/(9H)<2(\log H+1)/H\). The selected reserve occurs exactly once.

X3--X8 therefore prove PSD for every packet of size at most three,
including repeated evaluation nodes. Proposition SO-A proves failure
for every packet of five distinct positive nodes, and exactly two negative
directions for every packet of six distinct positive nodes. In particular
the high off-axis quartet can be detected using only safe nodes \(x>1/2\).

The checker supplies exact rational witnesses for nodes \(1,2,3,4,5\) and
for a packet crossing the former removable half-node. It also tests all
principal minors of sizes at most three within each five-node packet.
Those finite controls illustrate the cited all-node order-three theorem;
the finite scan is not its proof.

The multiplicity observation is separate and useful: replace the selected
critical pair by any multiplicity \(m_0\ge1\). Its positive kernel still
has rank two. The same four positive-feature equations expose a negative
direction on every five-node packet. A larger scalar reserve is therefore
not an all-order repair for this finite spectrum.

## 3. General finite spectrum: locations, rather than multiplicities

**Proposition SO-B.** Let an even real polynomial have exactly \(k\) distinct
critical pairs \(\pm i\gamma_j\), \(\gamma_j>0\), and \(\ell\ge1\) distinct
off-axis quartets \(\pm a_i\pm ib_i\), with \(0<a_i<b_i\), all carrying
positive integer multiplicities. Assume no root location is duplicated.
Define \(F=E'/E\) and the kernel (SO-1). Put

\[
d=2k+4\ell,\qquad p_+=2k+2\ell,\qquad p_-=2\ell.
\]

Every packet of \(d\) distinct positive nodes has inertia
\((p_+,p_-,0)\). Every packet of \(n\le d\) distinct positive nodes has
at least \(\max(0,n-p_+)\) negative directions. In particular, every
packet of \(p_++1\) distinct positive nodes is indefinite. For \(n>d\)
distinct nodes the inertia is \((p_+,p_-,n-d)\).

**Proof.** Each critical pair contributes the two positive squares from
(SO-2). Each quartet contributes two positive and two negative squares;
its \(c_i=b_i^2-a_i^2\) is positive. Multiplicities multiply the corresponding
square weights by positive numbers and do not alter the signature.

Take the common denominator made from each distinct quadratic or quartic
factor once, irrespective of multiplicity. The feature numerators span all
polynomials of degree below \(d\). Indeed the two critical features span
all degree-below-two numerators over their quadratic, and each quartet's
four features span all degree-below-four numerators over its quartic.
The factors are pairwise coprime, so the elementary partial-fraction
decomposition gives the whole degree-below-\(d\) rational function space.
Vandermonde evaluation has row rank \(n\) for \(n\le d\), and rank \(d\)
for \(n\ge d\).

For \(n\le d\), the image of the coefficient space in feature space has
dimension \(n\). Its intersection with the negative coordinate subspace
of dimension \(p_-\) has dimension at least
\(n+p_--d=n-p_+\). For \(n=d\) the feature map is an isomorphism.
For \(n>d\) it is onto and has kernel dimension \(n-d\). These facts
prove every asserted inertia bound.

## 4. A distant quartet leaves a gap of order b^(-8) on a fixed packet

**Proposition SO-C.** Fix five distinct positive nodes \(x_i\), a fixed
\(a>0\), \(r>0\), and positive multiplicities \(m_0,m\). Put

\[
c=b^2-a^2,\qquad B=2ab.
\]

For all sufficiently large \(b\), there is a unique coefficient vector
\(w(b)\) satisfying the four positive-feature cancellations (SO-5) and
the normalization

\[
\sum_iw_i(b)x_i^2=1.
\tag{SO-7}
\]

It is rational when all inputs are rational, and

\[
\begin{aligned}
w_i(b)&=\frac{x_i^2+r}{\prod_{j\ne i}(x_i-x_j)}+O(b^{-2}),\\
\boxed{w(b)^{\mathsf T}K_bw(b)}&=\boxed{-16ma^2b^{-8}+O(b^{-10})}.
\end{aligned}
\tag{SO-8}
\]

Constants in the remainders may depend on the fixed nodes, \(a,r,m\).
This is a fixed-packet asymptotic and does not assert uniformity when the
nodes or the number of source locations vary with \(b\).

**Proof.** Write \(s=b^{-2}\), \(A_0=a^2\), \(t=x^2\) and

\[
d_s(x)=1+2(t+A_0)s+(t-A_0)^2s^2.
\]

The quartet features have the following exact rational expressions:

\[
\begin{aligned}
U(x)/s&=\frac{x[1+(t-A_0)s]}{d_s(x)},\\
L(x)&=\frac{1+(t+2A_0)s-A_0(t-A_0)s^2}{d_s(x)},\\
V(x)&=\frac{xs^2}{d_s(x)},\qquad
W(x)=\frac{s^2}{d_s(x)}.
\end{aligned}
\tag{SO-9}
\]

Use \(U/s\), rather than \(U\), as one of the four equations defining
\(w(s)\). At \(s=0\) those four equations cancel
\(x/(x^2+r)\), \(1/(x^2+r)\), \(x\), and \(1\), while the fifth
row specifies the moment \(x^2\). Multiplying the five matrix columns by
\(x_i^2+r\) gives evaluations of

\[
x,\quad1,\quad x(x^2+r),\quad x^2+r,\quad x^2(x^2+r),
\]

which form a basis of the polynomials of degree at most four. The matrix
is invertible by Vandermonde evaluation. Its entries are rational functions
of \(s\), analytic near zero, so its normalized solution is unique and
analytic there. The stated limit \(w(0)\) follows from the identities
\(\sum_i x_i^j/Q'(x_i)=0\) for \(0\le j\le3\) and equals one for
\(j=4\), where \(Q(x)=\prod_i(x-x_i)\).

The first-order expansions of (SO-9) are

\[
U(x)/s=x[1-(t+3A_0)s]+O(s^2),\qquad
L(x)=1-ts+O(s^2).
\]

The exact cancellations and (SO-7) imply

\[
\sum_iw_i(s)=s+O(s^2),\qquad
\sum_iw_i(s)x_i=s\sum_iw_i(0)x_i^3+O(s^2).
\]

Expanding \(1/d_s=1-2(t+A_0)s+O(s^2)\) in the last two features gives

\[
V=-s^3\sum_iw_i(0)x_i^3+O(s^4),\qquad
W=-s^3+O(s^4).
\]

Finally \(B^2=4A_0/s\) and
\((c^2+B^2)/c=s^{-1}+O(1)\). Substitution into the exact negative-square
identity (SO-6) gives

\[
-16mA_0s^{-1}\bigl[O(s^6)+(s^{-1}+O(1))(s^6+O(s^7))\bigr]
=-16mA_0s^4+O(s^5).
\]

This proves (SO-8). The leading coefficient is independent of the reserve
multiplicity because its feature sums were canceled exactly.

The negative direction remains present at every finite height by SO-A,
while this normalized contraction tends to zero. Its Rayleigh quotient
has leading term
\(-16ma^2b^{-8}/\sum_iw_i(0)^2\). This explains a concrete finite-spectrum
loss in safe-axis visibility, without claiming a minimum-eigenvalue estimate
or a corresponding actual-xi bound.

## 5. Boundary of this obstruction

The original X9 source example is inherited; only the packet-size theorem,
factorization and exact annihilation formulation here are proposed additions.
The first failing packet need not have size five: size four can already fail
for other parameter choices. SO-A gives a uniform upper bound and does not
classify the order-four region.

Actual xi has an infinite complete critical and possible off-axis background.
The finite positive-feature count used here is then unavailable. Adding a
background changes both the kernel and the equations a witness must cancel.
The result neither contradicts actual-xi low-order positivity nor produces
an actual-xi violation. It identifies the missing mathematical ingredient:
low-order scalar curvature payment does not itself control arbitrarily
many independent feature directions.
