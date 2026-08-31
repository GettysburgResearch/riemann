# A global scalar frame from an increasing grading genus

Status: new theorem draft for independent review before its replay is written.
This is a declared regularization of the actual compact Frobenius family.
It is not the original integral full-place Euler function, and the grading
does not select a unique regularization policy.

The fixed-order tower is frozen at
`8985f69d22f8de6254405aa27ca511b3cd21f57c`; its proof blob is
`890e66e5faa77143dfcc7dc72d7cbe30ee0959a1`. It uses the actual F7 source
and its constant-field powers, not a new field or curve. Canonical factors
and determinant regularization are classical, as credited in that packet.
The proofs below use their elementary product formulas for this source.

## 1. Source blocks and an arbitrary genus policy

Keep the same orthonormal Frobenius eigenbasis as in the fixed-order packet.
For e≥1, put Q=7^e, lambda=i sqrt(7), and take the actual even-grade
multiplicity

    a_n=(1/(2n)) sum_(d|n, d odd) mu(d) 2^(n/d),
                         n even, n≥4.                    (1.1)

The two eigenvalues of the grade-n block of D_e(z) are
lambda^e z^n and (-lambda)^e z^n, each repeated a_n times. Formula (1.1)
gives a_n>0 and a_n~2^(n-1)/n on even grades. The same source-defined
operator is compact for |z|<1; no different Hilbert space or Schatten
domain is being asserted here.

A genus policy is any sequence of positive integers p_n on these even
grades. It need not be monotone. Define

    E_(p-1)(w)=(1-w) exp(sum_(1≤h<p) w^h/h),
    B_(e,n,p)(z)=product_(epsilon=±1)
                      E_(p-1)((epsilon lambda)^e z^n)^(a_n),
    D_(e,pbullet)(z)=product_(even n≥4) B_(e,n,p_n)(z).     (1.2)

Products are ordered by the actual grading, and each block uses the same
source Frobenius. The following normal-convergence statement is about the
block products, not an ordinary fixed-p Fredholm determinant.

**Theorem GGC1.** The products in (1.2) converge normally to a holomorphic
function with value one at zero on every compact subdisk of |z|<1 if and
only if p_n tends to infinity. Under this condition the zeros are exactly
the finite-multiplicity failures of invertibility of 1-D_e(z).

**Proof of sufficiency.** Fix r<1 and let M=7^(e/2). For all sufficiently
large n, M r^n≤1/2. On that disk the logarithm of each individual canonical
factor is normalized at zero, and

    |log B_(e,n,p_n)(z)| ≤ 4 a_n (M r^n)^(p_n)/p_n.       (1.3)

Also M r^n≤r^(n/2) eventually. Since p_n→infinity, choose a fixed P with
2 r^(P/2)<1 and then n large enough that p_n≥P. The right side of (1.3)
is bounded by C (2 r^(P/2))^n/n. Its sum converges. The finitely many
omitted blocks are entire functions with their actual zeros retained.
Thus the tail is a holomorphic unit on the compact disk and the product
is holomorphic. The same argument on slightly larger disks gives normal
convergence. At any interior point only finitely many blocks can vanish,
and the tail is a unit; this proves the zero statement.

**Proof of necessity.** If p_n does not tend to infinity, an infinite
subsequence has the same value p. Let h0=p for even e and
h0=2 ceil(p/2) for odd e. Choose a real r with
2^(-1/h0)<r<1. For large n in that subsequence the block logarithm is
real and its leading nonzero term is

    -a_n tr(Frob_7^(e h0)) r^(n h0)/h0
      ~ -tr(Frob_7^(e h0))/(2h0) · (2 r^h0)^n/n.          (1.4)

The coefficient is nonzero. Later trace orders are smaller by a geometric
factor r^n (or r^(2n) when e is odd), and the relative error in (1.1)
tends to zero. Thus the block values tend to zero or infinity, not one.
This happens for every r in that open interval. If the partial products
had a locally uniform holomorphic limit on the unit disk, its value one
at zero would make it nonzero at some r in the interval. The ratio of two
successive partial products would then tend to one there, contradicting
(1.4) along the subsequence. This also rules out concealing the failure
as an identically zero product. QED.

## 2. A global frame is explicit, but not unique

For two divergent policies p_n and q_n, use the convention that an oriented
sum from p to q-1 is the negative reversed sum if q<p. Cancellation of
the identical proper determinant in each block gives

    D_(e,qbullet)/D_(e,pbullet)=exp(U_(p,q)(z)),
    U_(p,q)(z)=sum_n a_n sum_(p_n≤h<q_n)
                          tr(Frob_7^(eh)) z^(nh)/h.       (2.1)

The identity means equality after multiplication, including at zeros.
It does not divide two zero values. Each finite-head summand is a
polynomial. In the tail, the difference is bounded by the two summable
logarithm bounds in (1.3), so U is a single-valued holomorphic function on
the entire unit disk. The ratio is therefore a global holomorphic unit.

Comparison with a fixed-order determinant on its Schatten disk works the
same way: there the constant-order tail is summable, and the quotient is a
unit. These quotients provide an explicit global frame for the determinant
line constructed in the frozen fixed-order packet. An abstract global
trivialization theorem is unnecessary. The original p=1 frame does not
extend: its scalar germ still has the exact radius proved in that packet.

Different genus policies give different frames. For example changing only
p_4 changes (2.1) by a nonzero finite trace polynomial as soon as a surviving
trace order is crossed. Thus the grading supplies a natural indexing for a
chosen policy; it does not prove uniqueness of that policy or preserve the
native scalar normalization.

## 3. Linear policies and the exact Frobenius norm law

For an integer kappa≥1 choose p_n=kappa n. For a fixed complex phase xi,
let D_(e,kappa)(z;xi) denote the same product with both eigenvalues
multiplied by xi. The proof of (1.3) is uniform when xi ranges over a compact
set, so these products are jointly holomorphic for |z|<1 and xi in C.

For d≥1 the finite canonical-factor identity gives on the whole unit disk

    D_(ed,kappa)(z^d;1)
       = product_(omega^d=1) D_(e,d kappa)(z;omega).       (3.1)

The change kappa→d kappa is essential. Indeed the left block has genus
kappa n and argument w^d; factoring it into d canonical factors uses genus
d kappa n. Normal convergence justifies passage from the exact finite
identity to the products. The phase acts on Frobenius, not on the grading
variable. When e is odd, symmetry of the two source eigenvalues yields

    D_(2e,kappa)(z^2;1)=D_(e,2kappa)(z;1)^2.              (3.2)

These are statements for the regularized cohomological multiplier. They do
not assert an identical scalar substitution law for the full place-Euler
source or for its boundary correction.

## 4. Exact zeros force a natural boundary

For every divergent policy, the zero set in Theorem GGC1 includes all roots

    (epsilon lambda)^e z^n=1,
                 n even≥4, epsilon=±1.                  (4.1)

Their radii are 7^(-e/(2n)), tending to one. Their angular meshes tend to
zero, so they accumulate at every point of the unit circle. Their positive
multiplicities are a_n for distinct eigenvalues and 2a_n when the two
Frobenius powers coincide. No infinite tail or exponential counterterm can
cancel them. A nonzero meromorphic extension across a unit-circle point
cannot have zeros accumulating at that point. Since the product is one at
zero, it has a meromorphic natural boundary at |z|=1.

This gives a single-valued global scalar representative of the determinant
section on its maximal compact-operator disk. It does not give a scalar
continuation of the original Fredholm germ through its earlier branch
circle. The two scalar functions already differ near zero.

## 5. The full AFTER source and the separate good-place zeros

Let H_(2,e)=E_(chi,Q)(z) P_(E,Q)(z^2) be the actual single-generator AFTER
source at Q=7^e. Its integral formal series has single-valued meromorphic
continuation to |z|<1. For every finite even N,

    H_(N,e)=H_(2,e) product_(even 4≤n≤N) P_(E,Q)(z^n)^(a_n)

is holomorphic on its proved finite-ladder disk. The equality uses the
actual fact that the two elliptic Frobenius factors of this fixed family
agree after every constant-field extension.

Define the new regularized scalar

    Hhat_(e,pbullet)=H_(2,e) D_(e,pbullet).               (5.1)

For every divergent genus policy this is holomorphic on the unit disk.
To prove this, fix r<1 and choose N so H_(N,e) is holomorphic past r and
7^(e/2) r^(N+2)<1. Then (5.1) is H_(N,e), multiplied by the finite-head
exponential counterterm and by the tail of the canonical product. The
latter is a holomorphic unit on |z|≤r: its proper factors have no zeros
there, and its logarithms satisfy (1.3). Thus all interior arithmetic
poles of H_(2,e) are canceled by actual finite cohomological factors.
The global frame also represents the full finite-source determinant line
of the fixed-order packet, with its cutoff condition retained.

One must not infer the natural boundary of (5.1) from (4.1): some of those
weight-circle zeros precisely cancel poles of H_(2,e). Instead use the
separate, pinned full-place source theorem. At
`7b320b3a9a55a16e73d99dd9bbab5bf592d50c93`, the proof
`COHERENT_QUADRATIC_PLACE_EULER.md` has blob
`2b5b7ef94b0c4c6326a0e06221d01d23475ec58e`. Its Section 3 proves that the
geometrically connected S3 times C2 cover has completely split good places
of every sufficiently large degree d, and that their zeros z^d=-1/2
survive finite extraction. Its geometric input
`RAMIFIED_TWISTED_GLOBAL_COMPLETION.md`, blob
`e54a39f39833f446fec68840f28b7466fe52aa67`, establishes the genus-nine joint
cover: the quadratic cover ramifies at zero where the S3 cover is unramified,
so it cannot be a geometric subcover of the S3 cover. This also excludes a
constant-field component. The source theorem applies after each extension
Q=7^e; it is not a count observed in a bounded prime-field panel.

At such a good-place zero the modulus is 2^(-1/d), which is never a radius
7^(-e/(2n)). Hence D_(e,pbullet) is holomorphic and nonzero there. The
factor P_(E,Q)(z^2) is also a unit there. The pinned source proof already
excludes cancellation by ramified factors or finite cohomology in E_chi.
These surviving zeros are dense along the unit circle, proving that (5.1)
also has a meromorphic natural boundary. This uses actual good-place zeros,
not multiplication of two arbitrary functions with natural boundaries.

## 6. A small coefficient proves the normalization changed

Take e=kappa=1. Since a_4=2, the first block is exactly

    (1+7z^8)^2 exp(-14z^8).

All other blocks start in degree at least 36. Therefore

    D_(1,1)(z;1)=1-49z^16+(686/3)z^24+O(z^32).          (6.1)

The native pure multiplier instead starts with 1+14z^8. Thus even the
first changed coefficient is visible without a numerical evaluation.
Moreover H_(2,1) has integral coefficients and constant term one. All
coefficients of (6.1) below degree 24 are integral, but its degree-24
coefficient is not. Consequently Hhat_(1,1) has a nonintegral degree-24
coefficient. It cannot be silently identified with the original integral
place-Euler source. This does not exclude generalized objects that
deliberately allow nonintegral coefficients.

More generally the first nonconstant term for the linear policy is

    -(7^(2 e kappa)/kappa) z^(16 kappa).                 (6.2)

The operator, its cohomological eigenvalues, and its zero divisor were kept;
the scalar frame and arithmetic coefficients were changed. A global scalar
regularization is a positive analytic completion with this stated cost,
not a recovery of the original source normalization.
