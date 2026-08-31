# Exact logarithmic residues of the Frobenius ladder

Status: independent proof draft by `/root/recent_landscape`, requested by the
coordinating agent. No new computation, replay, freeze or publication is claimed.
This is separate from `REGULARIZED_FROBENIUS_TOWER.md`. The mechanisms used below
are classical Euler-transform and normal-convergence arguments; the contribution
is their exact application to the declared source multiplicities and Frobenius
parameters, not a new general natural-boundary theorem.

The multiplicities are those of the frozen actual S3 source in `MATHEMATICS.md`
at `64075f1a3f81529f217dee1ae139656dfb9356f3`. Write

\[
 a_j:=a_{2j}=\frac1{4j}\sum_{d\mid j,\ d\text{ odd}}\mu(d)4^{j/d},
 \qquad j\ge1.                                                   \tag{1}
\]

Thus `a_1=1`, all `a_j` are nonnegative integers, and `a_j<=4^j/j`.
The actual pure ladder omits `j=1`. This omission is retained throughout.

## 1. A meromorphic logarithmic derivative from the actual source

First work with any nonzero odd integer `b` with `|b|>1`, and define

\[
 F_b(x)=\prod_{j\ge2}(1-bx^j)^{a_j}.                              \tag{2}
\]

The product converges normally on `|x|<1/4`, with its finitely many possible
head zeros retained. Its logarithm at zero is initially defined on a smaller
zero-free neighborhood if necessary. Put

\[
 A(u)=\sum_{j\ge1}a_j u^j
     =-\frac14\sum_{d\ge1,\ d\text{ odd}}\frac{\mu(d)}d
                      \log(1-4u^d).                              \tag{3}
\]

For `|u|<1/4`, (3) follows by substituting `j=dk` into (1), using absolutely
convergent sums. Differentiation gives

\[
 A'(u)=\sum_{d\ge1,\ d\text{ odd}}
                 \frac{\mu(d)u^{d-1}}{1-4u^d}.                   \tag{4}
\]

Equation (4) is a single-valued meromorphic function on `|u|<1`.
Indeed on each compact subdisk only finitely many denominators have zeros;
for all remaining `d`, the denominator is bounded away from zero and the
numerator is dominated by a geometric series. This assertion is about `A'`;
it does not declare the logarithms in (3) single-valued on the whole disk.

We now prove that `F_b'/F_b` has a single-valued meromorphic continuation to
`|x|<1`. This step is needed before a natural-boundary assertion can be made.
Fix `0<r<1`. Choose integers `H,J>=1` satisfying

\[
 4r^{H+1}<1,\qquad |b|r^{J+1}<1/2.                               \tag{5}
\]

Keep the finite head `2<=j<=J` as its actual polynomial factors. For the tail,
the identity of germs is

\[
 \log\prod_{j>J}(1-bx^j)^{a_j}
 =-\sum_{h\ge1}\frac{b^h}{h}
       \left(A(x^h)-\sum_{j\le J}a_jx^{jh}\right).               \tag{6}
\]

For `h<=H`, the derivative of each bracket is meromorphic on the unit disk
by (4), minus an entire polynomial. For `h>H`, the original power series
for `A(x^h)` converges on `|x|<=r`. Both this part of (6) and its derivative
converge normally there. For the derivative, an explicit bound is

\[
 \sum_{j>J}\sum_{h>H}j a_j |b|^h r^{jh-1}
 \le \frac{2|b|^{H+1}}r\sum_{j>J}(4r^{H+1})^j<\infty.           \tag{7}
\]

The undifferentiated sum is bounded in the same way. Thus the finite-head
logarithmic derivative, the finitely many meromorphic low-`h` terms and the
normally convergent high-`h` tail construct the claimed meromorphic continuation.
Different choices of `r,H,J` agree by the meromorphic identity theorem, since
they agree with the original germ. No unjustified globally convergent double
logarithmic series is being asserted.

## 2. Exact residues and dyadic monodromy

Let `x0` satisfy `4 x0^m=1`. Choose `r>|x0|` and `H>=m` in the preceding
argument. Among the low-`h` terms, the only singular logarithms at `x0` have
`hd=m`, with `d` odd. Different products `hd` have different radii and cannot
give the same point. Consequently the exact residue is

\[
 \mathop{\rm Res}_{x=x_0}\frac{F_b'(x)}{F_b(x)}
 =c_m(b):=\frac1{4m}\sum_{d\mid m,\ d\text{ odd}}
                      \mu(d)b^{m/d}.                             \tag{8}
\]

No finite-head zero meets such a point: `bx0^j=1` and `4x0^m=1` would imply
`|b|^m=4^j`, impossible because `b` is odd and `|b|>1`. The high-`h` tail
is analytic, and the other low-`h` terms are analytic locally. Therefore
each continued local branch has the more precise form

\[
 F_b(x)=(1-4x^m)^{c_m(b)} U(x),                                  \tag{9}
\]

where `U` is holomorphic and nonzero on a sufficiently small neighborhood
after choosing the local branches. In particular (8) is not inferred from
a finite coefficient table, or merely from the zeros of the original factors.

For `m=2^v`, the only odd divisor is one, so

\[
 c_{2^v}(b)=\frac{b^{2^v}}{2^{v+2}}.                            \tag{10}
\]

This residue is nonzero and has denominator exactly `2^(v+2)` in lowest terms.
The local multiplicative monodromy therefore has exact order `2^(v+2)`.
For the F7 polynomial pair, `b=-7`; the first three residues are
`-7/4`, `49/8`, and `2401/16`.

The globally regrouped expression
`sum_m c_m(b) log(1-4x^m)` is useful as an identity of sufficiently small
germs, with the omitted `j=1` factor corrected. It need not converge on the
whole unit disk: `|b|^m` grows. Equations (5)--(7), rather than that unjustified
regrouping, provide the continuation and residue proof.

## 3. Natural boundary and the finite-cover obstruction

For dyadic `m`, all the points

\[
 x=4^{-1/m}\exp(2\pi i k/m),\qquad 0\le k<m,
\]

are genuine poles of the meromorphic logarithmic derivative by (10).
Their radii tend to one and their angular grids become dense. Hence every
point of `|x|=1` is an accumulation point of interior poles. A meromorphic
function on a neighborhood of a point cannot have poles accumulating at
that point. It follows that **the unit circle is a meromorphic natural boundary
of the single-valued continuation of `F_b'/F_b`**.

The corresponding scalar statement is deliberately precise. The function
`F_b` already has interior algebraic branches, so it is not called a
single-valued meromorphic function on the entire unit disk. Instead, no
branch obtained by continuation of its germ can extend meromorphically to
a neighborhood of any point of the unit circle while agreeing on an interior
open set. Such an extension would provide a meromorphic continuation of its
logarithmic derivative there, contradicting the preceding pole accumulation.

Nor can one fixed finite branched cover of the unit disk make this scalar
continuation meromorphic everywhere over the interior. If the cover has degree
`D`, every local ramification index is at most `D`. At a point (10), a local
pullback can remove the branch only when that index is divisible by
`2^(v+2)`. These denominators are unbounded. This is a statement about finite
branched covers of this scalar continuation, not an obstruction to every
possible operator or sheaf category.

## 4. Translation to the actual Frobenius family

For F7, the elliptic eigenvalues are `lambda=i sqrt(7)` and `-lambda`.
The pure source multiplier in the grading variable `z` is

\[
 K_7(z)=\prod_{j\ge2}(1+7z^{4j})^{a_j}=F_{-7}(z^4).             \tag{11}
\]

Thus the auxiliary variable in (2) is **`x=z^4`**, not `z` or `z^2`.
The first scalar Taylor radius is `1/sqrt(2)`, while the outer meromorphic
natural boundary of its continued logarithmic derivative is `|z|=1`.
These are different assertions. Pullback by `z^4` preserves each interior
residue since the relevant points are nonzero and unramified, and preserves
density at the unit circle.

For every constant-field degree `e>=1`, retain the same eigenbasis as in the
regularized-tower note. Directly from the pair of Frobenius eigenvalues,

\[
 K_{7^e}(z)=
 \begin{cases}
 F_{-7^e}(z^4),&e\text{ odd},\\
 F_{(-7)^{e/2}}(z^2)^2,&e\text{ even}.
 \end{cases}                                                     \tag{12}
\]

The same proof therefore applies to every pure ladder in this constant-field
family. In the second line the residues are doubled, but their dyadic
denominators remain unbounded. No new finite-field enumeration is needed.

If a fixed meromorphic function `H2` on `|z|<1` is multiplied into (12), its
logarithmic derivative has integer residues at every interior zero or pole.
It cannot cancel the nonintegral dyadic residues above. Consequently the
same meromorphic natural-boundary and unbounded-monodromy conclusions hold
for `H2 K_(7^e)`. For the actual full AFTER source this hypothesis is supplied
by the following frozen source chain, not by the finite atlas:

* `COHERENT_QUADRATIC_PLACE_EULER.md`, commit
  `5104c38614461a3e080c93631b855094d0e5961a`, blob
  `2b5b7ef94b0c4c6326a0e06221d01d23475ec58e`, section 3, constructs the
  single-valued meromorphic continuation of the actual coherent place Euler
  function on the unit disk. Its finite compact-support Koszul extraction has
  integral exponents, retains the actual bad factors, and leaves a normally
  convergent remainder on each prescribed compact subdisk.
* `CONSTRUCTIBLE_POLE_CLEARING_SOURCE.md`, commit
  `c3cdd2528595cbf22c31d88a40c8a611b6385752`, blob
  `7ed7f6d68327df4c5f395142503253b19e8938e4`, equation (2.1) and section 4,
  identifies the actual finite-ladder function as `H2=E_chi(z) P_E(z^2)`.
  The multiplier is a finite polynomial, so the same meromorphy holds. The
  source construction applies after every constant-field extension as well.

Therefore the full AFTER functions in this constant-field family have the
same logarithmic-derivative natural boundary and finite-cover obstruction.
The finite-ladder factor has value one at zero and is not identically zero.
Its integer residues cannot remove the fractional parts of the displayed
dyadic residues. No analogous all-unit-circle theorem for the full BEFORE
correction is asserted here.

## 5. Compatibility with the determinant-line construction

The regularized Frobenius tower constructs a holomorphic line and section
over the compact-operator disk by changing local scalar frames. That is
compatible with everything above. Its transition functions remove specified
finite trace terms on their honest common domains; they do not preserve the
native scalar germ in a single global nowhere-zero frame.

The obstruction proved here belongs to that specified scalar normalization.
It does not imply a topologically nontrivial line on the disk, does not
invalidate the regularized local products, and does not enlarge an ordinary
Schatten domain. The all-grade pole/monodromy computation adds information
beyond the first Taylor-radius obstruction, without substituting a different
normalization for the source-faithful scalar.
