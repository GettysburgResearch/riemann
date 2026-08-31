# A regularized Frobenius tower and its determinant line

Status: proposed theorem continuation, not integrated. Root proof; new replay
and independent exact-commit review are pending. This note constructs an
analytic operator parent and also states precisely which scalar normalization
it cannot preserve. It does not claim an RH consequence or a canonical metric.

Sources: the actual F7 source and the multiplicities are frozen in
`MATHEMATICS.md` at `64075f1a3f81529f217dee1ae139656dfb9356f3`.
The full-source AFTER-radius theorem is `ARITHMETIC_RADIUS_DICHOTOMY.md`
at `075f9b203aefefb4a29f3279b6de1c4127093af6`. The BEFORE comparison is
`INFINITE_EXTENSION_ORDER.md` at `b3fde737e790e38ae15c20ce0858e72104c55550`;
the all-field BEFORE statement, if used, needs its own subsequent freeze.
The BEFORE conclusion below is proved directly from the local formulas.

The regularized determinant itself is classical. For its convention see
Britz--Carey--Gesztesy--Nichols--Sukochev--Zanin,
[The product formula for regularized Fredholm determinants, (1.3)](https://arxiv.org/abs/2007.12834).
All product, continuation, and gluing claims needed here have elementary
proofs for the specified diagonal family. No general multiplicative anomaly
formula or abstract determinant-line theorem is needed.

## 1. One source, all constant-field extensions

Let e>=1, Q=7^e, and retain the fixed source a=1,b=0. Its two elliptic
cohomology factors over F7 both have polynomial 1+7T^2. Choose one complex
Frobenius eigenbasis, declare it orthonormal, and retain the SAME basis on
constant-field extension. Write lambda=i sqrt(7). In each even grade n>=4
the pure adjoining multiplier has eigenvalues lambda^e and (-lambda)^e,
each repeated a_n times, where

    a_n = (1/(2n)) sum_(d|n, d odd) mu(d) 2^(n/d).          (1.1)

Define the Hilbert direct sum and its operator by

    H = direct-sum_(even n>=4) C^(2 a_n),
    D_e(z) = direct-sum_(even n>=4) z^n Frob_7^e.          (1.2)

The chosen inner product is declared data, not an arithmetic polarization.
For every real p>=1,

    D_e(z) belongs to S_p  iff |z|<2^(-1/p),
    D_e(z) is compact     iff |z|<1.                      (1.3)

At z=0 these assertions include the zero operator. For |z|>=1 it is not
compact. For |z|>1 it is unbounded. Formula (1.1) gives
a_n~2^(n-1)/n along even n, while the singular values in grade n are
7^(e/2)|z|^n. Their p-power sum proves (1.3), including divergence at
equality. Uniform tail estimates also show that D_e is holomorphic in
compact-operator norm on the unit disk, and in S_p norm on the stated
S_p disk. Multiplication by any fixed power of n does not change these
convergence thresholds, so termwise operator differentiation is justified.

## 2. Exact scalar domains of the regularizations

For an integer p>=1 set

    E_(p-1)(w)=(1-w) exp(sum_(1<=h<p) w^h/h),
    Delta_(e,p)(z)=product_(eigenvalues w of D_e(z)) E_(p-1)(w).
                                                                  (2.1)

On the S_p disk this is the ordinary p-regularized Fredholm determinant.
Indeed for |w|<=1/2 its logarithm is -sum_(h>=p)w^h/h, bounded by
2|w|^p. Remove finitely many eigenvalues to achieve that inequality on
each compact disk; the tail product converges normally. The finite head
is retained as entire factors, including all of its zeros.

Let

    h0(e,p)=p                 if e is even,
    h0(e,p)=2 ceil(p/2)       if e is odd.                (2.2)

**Theorem RFT1.** The Taylor series of Delta_(e,p) at zero has exact
radius 2^(-1/h0). At each point z0 satisfying 4 z0^(2h0)=1, its local
continuation from inside that circle has the form

    (1-4z^(2h0))^eta times a holomorphic nonzero function,
    eta=(-7)^(e h0/2)/(2h0),                            (2.3)

in a small slit neighborhood of z0. In particular eta is not an integer.
When e and p are odd, Delta_(e,p)=Delta_(e,p+1) as germs; the larger
radius is realized by the honest S_(p+1) determinant.

Proof. Odd h have zero block trace precisely when e is odd. For the
remaining h, the trace of the grade-n block is
2 a_n (-7)^(eh/2) z^(nh). Formula (1.1) implies

    2 a_n = 2^n/n + b_n,
    |b_n| <= (2^(floor(n/3)+1)-2)/n.                   (2.4)

The n=2 term has been excluded throughout. Removing it changes a
logarithmic generating series only by a polynomial. The first nonzero
trace order h0 therefore contributes

    eta log(1-4z^(2h0)) + a polynomial + a holomorphic remainder.

The remainder from (2.4) is holomorphic for |z|<2^(-1/(3h0)). The next
nonzero trace order is h0+1 in even e and h0+2 in odd e. Choose a radius
r strictly between 2^(-1/h0) and both of the corresponding next
convergence thresholds. Then choose a grade cutoff N so large that
7^(e/2) r^(N+2)<1/2. In the tail n>N the sum over all later h is
bounded by a constant times sum_n (2^n/n) r^(n h_next). It converges
normally. This justifies summing the tail logarithms past the first
circle; the finite head supplies entire factors.

No finite-head zero lies on that circle: such a zero would require
7^(e h0)=2^(2n), which is impossible. Thus the remaining local factor
is nonzero at every z0 in (2.3). The numerator in eta is odd and its
denominator 2h0 is even, so eta is nonintegral even after reduction.
This proves the exact radius. If e,p are odd, the p-th power trace
vanishes in every block; the two regularizations agree first where
both products converge and then as germs. QED.

For e=1, p=1 and p=2 both have radius 1/sqrt(2). The ordinary
Fredholm determinant is nevertheless defined only on the trace-class
disk |z|<1/2; the Hilbert--Schmidt regularization extends its scalar
germ to the larger disk. For e=2 the p-th regularization has radius
2^(-1/p), and increasing p changes the original scalar germ.

## 3. Frobenius powers and cyclic norms

**Theorem RFT2.** For integers d,e,p>=1 the following identity of
germs holds, and holds on the common domains of the displayed honest
regularized products:

    Delta_(ed,p)(z^d)
      = product_(omega^d=1) det_(dp)(1-omega D_e(z)).     (3.1)

This is a change of constant field with a simultaneous, specified change
of regularization order. The proof is the elementary identity

    E_(p-1)(w^d)=product_(omega^d=1) E_(dp-1)(omega w).

The polynomial part follows from product(1-omega w)=1-w^d; in the
exponential part only powers divisible by d survive the sum of roots
of unity. Apply this identity to each retained Frobenius eigenvalue.
The shared absolute convergence domain is |z|<2^(-1/(dp)).

For e odd the spectrum is symmetric, so d=2 gives the particularly
simple identity

    Delta_(2e,p)(z^2)=Delta_(e,2p)(z)^2.                (3.2)

The pure F49/F7 identity from the first completion packet is its p=1
case, using Delta_(1,2)=Delta_(1,1). Neither (3.1) nor (3.2) is asserted
for the full boundary Hilbert ratio or the complete place-Euler object.

The full AFTER object itself has an exact constant-field parity law:

    radius H_after,7^e = 1/sqrt(2) if e is odd,
    radius H_after,7^e = 1/2       if e is even.          (3.3)

For odd e both elliptic traces are zero, so the first exponent alpha
in the frozen arithmetic theorem vanishes, and the finite source zero
orders are nonnegative. For even e the two traces equal
2(-7)^(e/2), hence alpha=(-7)^(e/2)/2 is a nonintegral half-integer.
No integer finite-source zero order removes it. This proves (3.3).

The full BEFORE object has radius 1/2 for every e. To see this without
a new finite-field sweep, note that infinity is always split, since
7^e=1 modulo 3, and contributes the local exponent -1/3. For odd e
the two rational old branches still have opposite signs; their combined
ratio has a nonzero constant term plus a square-root correction, and
the remaining degree-two branch is interior-analytic at z=1/2. Thus
the full exponent is an integer minus 1/3. For even e all four old
branches are rational with positive quadratic sign, contributing -1
in total; combined with alpha this gives an integer plus a half-integer
minus 4/3. Neither exponent is integral. The source-restoration argument
of the frozen infinite-extension theorem proves holomorphy on |z|<1/2
in exactly the same way for each Q; finite arithmetic poles are first
cleared by choosing the finite ladder deep enough. Thus the first
circle is a real obstruction, not a pole of an uncancelled ratio formula.

## 4. A holomorphic line over the entire compact-operator disk

For q>p the determinants satisfy on |z|<2^(-1/p)

    Delta_(e,q)/Delta_(e,p)
       = exp(sum_(p<=h<q) Tr(D_e(z)^h)/h).              (4.1)

This means equality after multiplying by the right-hand side even at
zeros; no division at a zero is required. The right side is holomorphic
and nowhere zero because every displayed power is trace class on that
disk. The identity follows eigenvalue by eigenvalue and from absolute
convergence. These factors satisfy the cocycle identity by addition of
the finite trace sums.

Glue trivial lines over the nested disks |z|<2^(-1/p) using (4.1), with
frames chosen so that Delta_(e,p) times its local frame is independent
of p. This constructs a holomorphic line L_e and a holomorphic section
on the full unit disk. Its zeros are exactly the finite-multiplicity
failures of invertibility of 1-D_e(z). This is an explicit determinant
line for the declared compact family. The construction does not assert
that the scalar functions Delta_(e,p) are equal on overlaps.

There is an equally direct source version for the complete AFTER ladder.
Choose radii r_j increasing to one and increasing even cutoffs N_j so that

    H_(N_j) is holomorphic on |z|<r_j,
    sqrt(Q) r_j^(N_j+2)<1.                              (4.2)

The finite-ladder domain theorem permits both conditions. If k>j, then
H_(N_k)=H_(N_j) times the finite product of the actual P_D(z^n)^B_n
and P_E(z^n)^C_n for N_j<n<=N_k. EVERY such factor is a unit on the
smaller disk by (4.2), not merely by finite-ladder holomorphy. These
unit transition functions glue a holomorphic line and section over
the unit disk. Finite-source zeros are retained as section zeros.
Changing to a cofinal cutoff sequence gives the same construction up
to the explicit transition isomorphisms on a common refinement.

Near zero the convergent original tail supplies a local frame in which
this section is the original full H_infinity germ. Such a frame cannot
extend to a holomorphic nowhere-zero frame on the unit disk: in that
frame the section would give a holomorphic scalar extending its germ,
contradicting the proved radius 1/2 or 1/sqrt(2). The same obstruction
applies to the native p=1 frame of L_e. This is a statement about a
specified frame, not a claim that a holomorphic line on the disk is
topologically nontrivial. No global trivialization theorem is needed.

Finally Delta_(e,p)=1 modulo z^(4p) as formal series; all generator
grades are at least four. Hence Delta_(e,p) tends coefficientwise to
1 as p tends to infinity. Multiplying by a fixed H_2 gives H_2 as the
formal limit, not the native infinite completion. Restoring the removed
trace terms to preserve the original germ restores its analytic radius
obstruction. This prevents a regularization tower or a line-valued
completion from being silently substituted for the source-faithful scalar.

## 5. What the proposed finite replay can and cannot certify

The proposed replay checks the actual PBW multiplicities, Frobenius power
recurrences, regularized finite products and their formal logarithms,
cyclic-norm identities without approximate roots, and the parity and
nonintegrality statements for a declared finite panel. The all-grade
radius, operator ideal, and line-gluing claims rely on the proofs above.
The next target is a source-pinned independent replay and proof audit,
not an inference from a table of regularization orders.
