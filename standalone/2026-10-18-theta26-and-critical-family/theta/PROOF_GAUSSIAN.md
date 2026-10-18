# Certified real-zero entire approximants through theta order 26

## Result and scope

There exist even entire functions with only real zeros whose Taylor expansions
agree with the actual normalized Xi function through orders **22, 24, and 26**.
The functions have the explicit form

\[
 P(z)=e^{-az^2}\prod_{j=1}^{N}(1-b_jz^2),
 \qquad a>0,\quad b_j>0,\quad a+\sum_jb_j=\tfrac12. \tag{1}
\]

Here `z` is the variance-one theta variable. The certified models use `N=64`
at order 22 and `N=128` at orders 24 and 26. Thus the polynomial factors have
degrees 128 and 256; **the numbers 22, 24, and 26 refer to matched Taylor
orders**, not to the degree of the entire functions or their polynomial factors.

Every function in (1) obeys the uniform whole-plane bound

\[
 \boxed{\quad |P(z)|\le e^{|z|^2/2}\quad(z\in\mathbb C).\quad} \tag{2}
\]

The existence statements are certified by complete-source directed interval
arithmetic and a contraction on a full rational parameter cube. They do not
depend on accepting the earlier proposed theta-20 Ising realization. The
source arithmetic backend and theta normalization are authenticated from the
pinned earlier packet; the source integrals are recomputed through order 26
with every Taylor, time, and theta-index remainder included.

These are finite entire-function approximation results. An unbounded-order
construction has not been proved. Consequently this packet proves neither
RH nor an improved zeta zero-free boundary. The all-order implication and its
remaining constructive requirement are stated precisely below.

## 1. The actual target, with normalization fixed

Let

\[
 F_\theta(z)=\frac{\xi(1/2+iz)}{\xi(1/2)}
             =\mathbb E e^{izT},
 \qquad v=\mathbb E T^2.
\]

The theta density and its complete-source enclosure are specified and proved
in [SOURCE26.md](SOURCE26.md). They give, in particular,

\[
 v=0.046209986230837941577867620860678\ldots>0.
\]

Define

\[
 H(z)=F_\theta(z/\sqrt v)=\mathbb E e^{izT/\sqrt v}.
\]

Then `H(0)=1`, `H` is even and entire, and its variance is exactly one. All
matching equations below concern this `H`. The physical Xi approximant is
`P(sqrt(v) z)`. It has only real zeros, agrees with `F_theta(z)` to the same
Taylor order, and satisfies `|P(sqrt(v) z)|<=exp(v|z|^2/2)`.

Write `kappa_(2r)` for the even cumulants of `T/sqrt(v)`. For `r>=2`, put

\[
 Q_r=\frac{(-1)^{r+1}r\kappa_{2r}}{(2r)!}. \tag{3}
\]

These are finite algebraic combinations of the source moments. No zeta-zero
sum is used to define or bound them. In particular, the notation in (3) does
not assume a real-zero product representation of Xi.

## 2. Why the finite equations give the claimed entire functions

Choose positive numbers `b_1,...,b_N` with sum less than `1/2`, and define
`a=1/2-sum_j b_j`. Near zero, the logarithm of (1) is

\[
 \log P(z)=-\tfrac12z^2-
       \sum_{r\ge2}\frac{z^{2r}}r\sum_{j=1}^{N}b_j^r. \tag{4}
\]

On the other hand, the cumulant definition gives

\[
 \log H(z)=-\tfrac12z^2+
       \sum_{r\ge2}\frac{(-1)^r\kappa_{2r}}{(2r)!}z^{2r}. \tag{5}
\]

Therefore the finite equations

\[
 \boxed{\qquad \sum_{j=1}^{N}b_j^r=Q_r,
       \qquad r=2,\ldots,M,\qquad} \tag{6}
\]

are exactly sufficient for `P(z)-H(z)=O(z^(2M+2))`. The constant and second
coefficients match by construction, and every odd coefficient is zero. Taking
`M=11,12,13` gives the three stated orders.

The exponential has no zeros. Every polynomial factor has the two real zeros
`+/-1/sqrt(b_j)`, with multiplicities retained if some parameters coincide.
Thus the global zero statement follows from the sign of the parameters and
does not use a numerical zero census.

Finally,

\[
 |e^{-az^2}|\le e^{a|z|^2},\qquad
 |1-b_jz^2|\le1+b_j|z|^2\le e^{b_j|z|^2}.
\]

Multiplying and using `a+sum b_j=1/2` proves (2). This argument needs no inverse
Fourier density and no positive probability-law realization of `P`.

## 3. Exact inputs and the full parameter domains

The input file `gaussian_parameters.json` records three finite rational centers,
their active coordinate indices, rational approximate inverse matrices, and
the rational radius

\[
 \rho=10^{-50}. \tag{7}
\]

Every decimal string in that file denotes its exact rational value. For a
model matching order `2M`, there are `m=M-1` active coordinates. Every other
`b_j` stays fixed at its recorded rational center. The active coordinates vary
independently throughout the entire closed infinity-norm cube of radius rho.
The checker verifies throughout that cube that every `b_j` is strictly positive
and that `a=1/2-sum b_j` is strictly positive.

The source `theta26_source.json` is bound by SHA-256
`c171903e4f60c189a929ccfcce36f7db034508e9ca10c85ed766338625558dcf`.
It contains complete outward intervals in units of `2^-512`. The checker can
rebuild it from the theta density with `--rebuild-source`; a source hash alone
is not the mathematical proof of the source. The proof of every integration
remainder is in SOURCE26.md.

Numerical searches used public zero-table entries as initial guesses. Those
entries are not loaded by the checker and are not assumptions of the theorem.
The checker uses only exact rational parameter data, the authenticated interval
backend, and the complete theta-source intervals.

## 4. Directed contraction certificate

Let `x` collect the active parameters, let `x_0` be their rational center, and
define the vector

\[
 f(x)=\left(\sum_{j=1}^{N}b_j^r-Q_r\right)_{r=2}^{M}.
\]

Let `R` be the recorded rational preconditioner. Its role is purely algebraic;
its origin in an ordinary-precision numerical inversion is not trusted. The
checker encloses every component of `f(x_0)` and every entry of the Jacobian on
the whole cube. The Jacobian formula is simply

\[
 \frac{\partial f_r}{\partial b_j}=r b_j^{r-1}. \tag{8}
\]

No sample grid, omitted configurations, or unbounded finite-sum tail occurs
in this step. All N terms of every power sum are included.

Directed interval arithmetic then supplies upper bounds

\[
 \beta\ge\|R f(x_0)\|_\infty,
 \qquad
 L\ge\sup_{x\in B}\|I-RDf(x)\|_\infty. \tag{9}
\]

The exact rational checks are

\[
 L<1,\qquad \beta+L\rho<\rho. \tag{10}
\]

For the actual theta vector, which lies in the complete source intervals,
`T(x)=x-Rf(x)` is consequently a strict contraction from the full cube into its
interior. Banach's fixed-point theorem gives a unique fixed point in the cube.
The bound `||I-RDf(x_0)||<1` also proves that the square matrix `R Df(x_0)` is
invertible, hence R itself is invertible. A fixed point therefore satisfies
`f(x)=0`. This establishes the existence claim without trusting an empirical
residual or presupposing that a numerical inverse is nonsingular.

The certified bounds are comfortably inside (10):

| Matched order | Factors N | Active coordinates | Upper bound for beta | Upper bound for L | Gaussian parameter a near center |
|---|---:|---:|---:|---:|---:|
| 22 | 64 | 10 | `1.155e-92` | `2.320e-38` | `0.07544076230992056` |
| 24 | 128 | 11 | `1.518e-90` | `5.857e-37` | `0.05410036642633601` |
| 26 | 128 | 12 | `1.194e-87` | `8.859e-35` | `0.05310885192096714` |

The displayed decimal bounds are rounded upward from the directed integer
receipt. Full endpoints, self-mapping slack, source binding, and input/code
hashes are in `gaussian_certificate.json`. The certified unknown solutions
lie in their full cubes; the center decimals are not asserted to be the exact
solutions.

## 5. A stronger all-order implication: the Gaussian reserve is optional

Suppose that for unbounded M one can solve (6) with finitely many positive
unit-multiplicity nodes. For this all-order statement, allow
`a=1/2-sum b_j` to be any real number. A finite sum budget is **not needed**.
The three certified finite models above satisfy the stronger condition a>0,
but their all-order consumer can use the larger class.

The reason is the elementary canonical-factor inequality

\[
 |(1-w)e^w|\le\exp(|w|^2/2),\qquad w\in\mathbb C. \tag{11}
\]

Indeed, `|1-w|^2=1-2 Re(w)+|w|^2`, and `log(1+u)<=u` proves (11)
when w is not one; the remaining case follows directly. Rewrite (1) as

\[
 P(z)=e^{-z^2/2}\prod_j\bigl[(1-b_jz^2)e^{b_jz^2}\bigr]. \tag{12}
\]

Since matching order four already fixes `sum b_j^2=Q_2`, every such real-node
model obeys the uniform whole-plane estimate

\[
 |P(z)|\le
 \exp\left(\frac{|z|^2}{2}+\frac{Q_2|z|^4}{2}\right). \tag{13}
\]

This bound is independent of the number of factors and of the sign or size
of a. It does not require positivity of an inverse Fourier density.

Montel's theorem now makes the cofinal sequence a normal family on the whole
plane. Any subsequential limit has every Taylor coefficient of H, since the
matching orders go to infinity. The identity theorem identifies it with H.
Every subsequence has the same limit, so the sequence converges to H locally
uniformly on the plane. Each approximant is nonzero in the two open
half-planes above and below the real axis. Hurwitz passes this property to H;
the limit is not identically zero because H(0)=1. Thus the cofinal
positive-node construction would prove RH.

For these entire products, solving the unbounded-order system (6) with
positive unit-multiplicity nodes is one sufficient construction. The Gaussian
reserve and probability-density positivity are optional restrictions. The
stronger companion theorem in `WEIGHTED_CANONICAL.md` also removes unit
multiplicity: arbitrary positive weighted nodes suffice, using holomorphic
canonical factors on the upper and lower half-planes. Fractional powers need
not be entire, and that companion proves convergence on the correct domains
by a direct imaginary-axis remainder estimate.

The remaining sufficient task is therefore **positive weighted feasibility
at unbounded orders**; none of the three finite certificates establishes it.
The separate extension note develops an exact moving-root operation and
makes its sign, size, and anchor-separation requirements explicit; it also
extends canonical-factor compactness to controlled complex-pair paths.

## 6. Reproduce and audit

With the pinned earlier theta source directory available:

```bash
python check_gaussian.py --source /path/to/pinned/theta --rebuild-source
python -O check_gaussian.py --source /path/to/pinned/theta
```

The first command reconstructs the complete source and checks the three
parameter cubes. The second also checks that optimized Python execution cannot
disable any acceptance test: all guards are ordinary explicit checks, not
assert statements. The checker uses the Python standard library and the
authenticated inherited interval backend. The exploratory producer's NumPy
and SciPy routines are not checker dependencies.

This is an independently checkable calculation, but the arithmetic backend is
inherited. A replay using the same backend is not an independent arithmetic
implementation. The packet's independent mathematical audit should therefore
review the primitive operations, new source remainders, normalization, and
contraction argument as well as replaying the resulting receipt.
