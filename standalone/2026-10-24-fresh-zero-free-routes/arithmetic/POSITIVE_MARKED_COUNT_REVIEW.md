# Review of the ordinary-zeta marked-count reduction

Reviewer: the arithmetic-escape agent, separate from the author of
`POSITIVE_MARKED_COUNT_TARGET.md`.
Date: 24 October 2026.
Disposition: no material gap found in the analytic reductions at the
stated scope after the explicit hyperbola-scope clarification below.
The power-error estimate is still OPEN. This is internal mathematical
review, not external peer review or formal verification.

## 1. Frozen objects and authorship boundary

The root author's submitted mathematical note had SHA-256

`bdd25239aa91eedd2342fd34f1cbaf044ab86f0fcd75a7c03edf1aa568a56e24`.

The intermediate note, after the changes described in Section 3, had SHA-256

`bd19d7e8aaa17a5b387d05915a9f59fd2b38ed427ffca3ff16d7064c18d627fd`.

The final reviewed note, including the independently checked real-slit
formulas (8a)–(8d) requested by the root author, has SHA-256

`18e58007abfa604c3e884e60b4721e6b15c86e63335e23c147dcff13364540af`.

The finite sextic experiment source inspected here has SHA-256

`b4c34f39b8f0982734f98ad9403b6e3d5fd605169ce97596c2b13b95a58cde73`.

The reviewer previously authored the companion nonprincipal fractional
criterion and coefficient-continuation lemmas. The root author supplied
the ordinary-zeta pole subtraction, its explicit zero-free disk, the
whole-circle principal term, and the entire-parameter Taylor adapter.
This review independently reconstructs those arguments, but does not
misrepresent the reviewer's related prior authorship as wholly
independent discovery. The small-prime main-term calculation added in
Section 3 is a reviewer-authored addition, not a separately reviewed
theorem. The real-slit formulas were proposed by the root author, then
independently derived by this reviewer before being added with their
proof.

## 2. Load-bearing mathematical checks

### The disk is established without a zero census

Euler summation gives the displayed remainder
`h(s)=zeta(s)-1/(s-1)` and
`|h(s)|<=1/2+|s|/(2 Re s)` in `Re s>0`.
For `|s-1|<=r<=1/2`, the geometry bound
`|s|/Re s<=1/sqrt(1-r^2)` is correct. Therefore
`|(s-1)h(s)|<=13/24<1` on the radius-one-half disk.
The pole-normalized `G(s)=(s-1)zeta(s)` is nonzero there and has the
normalized analytic logarithm used by the note. No assertion about
zeros at larger heights enters this argument.

### The fractional circle has the correct branch and orientation

For `w=1+r exp(i theta)`, `-pi<=theta<=pi`, the expression
`log G(w)-log r-i theta` exponentiates to `zeta(w)`.
The endpoint values differ by `-2 pi i`, as required around a simple
pole. The parameterization is counterclockwise. The note does not
incorrectly treat the fractional integrand as a single-valued
holomorphic function inside the circle.

For integer parameters the branch disappears. The exact identities
`C_0=C_-1=0` and `C_1=X W_hat(1)/zeta(2)` follow by the residue
theorem, since `1/zeta` is holomorphic inside the circle, including
its zero at one. These signs also agree with the direct Mellin check:
the exterior Cauchy transform at `z=1` is
`W_hat(1)/[zeta(2)(s-1)]`.

The correction product `H_z` converges locally uniformly for `Re s>1/2`
and compact complex `z`-sets: the linear prime terms cancel. For real
`0<z<1`, its logarithm converges normally and it is nonvanishing. Thus
the principal term uses only values on an explicitly proved zero-free
low-height circle. It does not conceal the unknown high zeros in an
assumed main-term theorem.

### The real-slit and marked real-integral formulas

The circle can be collapsed onto the real slit for `0<z<1`. The lower
bank has pole factor `t^-z exp(i pi z)` and the upper bank has
`t^-z exp(-i pi z)`. The positive outer orientation gives the
**lower-minus-upper** jump, so the coefficient is `+sin(pi z)/pi`.
The inner circle vanishes since its magnitude is `O(delta^(1-z))`.

For nonnegative nonzero `W`, every factor of `Q_z(t;X)` is positive on
the slit, proving `C_z(X)>0`. This does not assert positivity of its
derivative or of the remainder.

Subtracting `Q_z(0;X)` leaves an `O(t)` numerator. The subtracted
formula is holomorphic for `Re z<2`, allowing differentiation at one.
The quotient `sin(pi z)/[pi(1-z)]` has derivative zero there; the
derivative of `sin(pi z)/pi` is minus one. These two facts yield exactly

\[
 C_\omega(X)=cX(h_1(1)-\log r)
              +\int_0^r\frac{cX-Q_1(t;X)}t\,dt.
\]

The endpoint is removable because `Q_1(0;X)=cX`, and its value is
`-partial_t Q_1(0;X)`. Only real low-height zeta values, its
pole-normalization, absolutely convergent right-half-plane zeta
values, and the absolutely convergent prime correction at one are
needed. This confirms that the exact principal term is concretely
evaluatable without a complex contour or an unknown zero list.

### The Mellin continuation is legitimate

For `Re s>1+r`, absolute convergence justifies interchanging the
`X`-integral and the parameterized circle, giving the kernel
`1/(s-w)`. The exterior Cauchy transform is holomorphic outside the
closed disk even though its boundary density is not periodic as a
fractional logarithmic germ.

The lower-range arithmetic term is entire: for `0<X<1`, only the unit
integer can meet the support `(1,2)`, and its support in `X` is bounded
away from zero. Its marked derivative is zero.

The assumed error bound for every positive epsilon gives local uniform
convergence of the error Mellin transform in `Re s>b`. The remaining
domain, the half-plane with the closed tangent disk removed, is
connected to the initial right half-plane. Every possible zero in it
has a sufficiently small surrounding disk wholly inside that domain.
The omitted disk itself is already proved zero-free.

At a zero of multiplicity `m`, the irrational fractional germ has
monodromy `exp(2 pi i m z)`. A finite-order zero of `W_hat` cannot
cancel it. For the marked criterion the monodromy increment is
`2 pi i m zeta(s)/zeta(2s)`, multiplied by `W_hat`; this is not
identically zero in a punctured neighborhood. The denominator is finite
and nonzero because `Re(2s)>1`. Hence both zero-free implications follow
from their respective error hypotheses.

Differentiation at `z=1` is made in the initial absolutely convergent
identity. The proof of the marked criterion uses its own error
hypothesis; it does not differentiate an estimate known only at one
parameter or assume the fractional error bound.

### Entire-parameter growth and Taylor interpolation

For all complex `v`,
`|1+v|<=exp(Re v+|v|^2/2)` follows from `1+t<=exp(t)` with
`t=2 Re v+|v|^2>=-1`. Applying this factorwise, canceling the linear
terms against `(1-p^-s)^z`, and summing `p^-2b` gives the claimed
`exp(C_b(|z|^2+|z|))` bound on the fixed circle.

Cauchy's coefficient bound at a parameter radius proportional to
`sqrt N` yields a tail `exp(-N log N/2+O(N))` on any fixed parameter
disk. At `N=ceil(6 log X/log log X)`, the total error after the
`X^(1+r)` factor is `X^(r-2+o(1))`, in particular
`X^(-3/2+o(1))` or smaller. Thus it is safely below the proposed
`X^(b+epsilon)` scale.

The arithmetic polynomial has sublogarithmic degree on squarefree
support, and the Taylor polynomial has the same degree order. The
positive-measure interpolation lemma therefore applies to their
difference. If the coefficient set is initially unbounded, select a
bounded positive-measure subset before fixing the compact parameter
disk; no estimate on an unbounded parameter set is needed.
At `z=-1`, the exact principal term is zero. The resulting conditional
smoothed Mobius estimate is therefore for the original arithmetic
sum, not for a manufactured remainder.

### The unmarked anchor is valid

The squarefree expansion, ordinary smooth integer counting, and the
tail of `sum mu(d)/d^2` give `O_W(sqrt X)` exactly as claimed. This
anchor says nothing by itself about the marked derivative. The marked
series' logarithmic branch shows precisely why such differentiation
would be illegitimate.

## 3. Reviewer edits and the failed hyperbola attempt

I made two edits to the root-authored note:

1. Replaced “Mellin inversion” by “Mellin transform” in the discussion
   of the initial arithmetic identity.
2. Added the exact uniform small-prime formula
   \[
   \sum_{\substack{m\ {\rm squarefree}\\p\nmid m}}W(m/Y)
   =\frac{Y\widehat W(1)}{\zeta(2)(1+1/p)}+O_W(\sqrt Y),
   \]
   and clarified that the small-prime and large-prime replacements
   produce a hybrid main expression whose difference from the exact
   `C_omega` has not been bounded in the note.

The formula's constant is uniform in `p`: expand the squarefree
condition, retain `p` out of the square divisor, and subtract residual
multiples of `p`. The main factor is
`(1-1/p)/(1-p^-2)=1/(1+1/p)`, and each complete integer sum has an
`O_W(1)` error. The sum of those errors and the completed divisor-series
tail are both `O_W(sqrt Y)`.

Summing these errors over `p<=sqrt X` costs `O_W(X^(3/4))` by the
integer majorant for `sum p^-1/2`. On the large-prime side, separately
using a prime error of exponent `beta` costs at most
`X^((1+beta)/2+epsilon)` over `m<<sqrt X`. The original condition
`p not dividing m` is retained; removing its excluded diagonal prime
squares in this range would cost only `O_W(sqrt X)`.

These are upper bounds for **parts of a proposed argument**, not an
assembled error estimate relative to `C_omega`, and not lower bounds
on the true error. The clarification prevents overpromoting this
failed attempt.

## 4. Finite sextic experiment: limited independent replay

I inspected the ring multiplication, primary-generator convention,
split and inert residue-field evaluations, zero propagation, and
quadratic energy polynomial. For the declared finite cases they are
consistent with the sharp-annulus interpretation in the code.

I independently implemented scalar modular exponentiation for the
local symbols and compared it with the vectorized implementation:

- 5,251 scalar-versus-vectorized local symbol evaluations agreed,
  including zero values at the prime modulus.
- The source's 88 factor reconstruction checks and 7,500 local
  multiplicativity checks passed again.
- At `U=64,D=128`, a separate scalar row-by-row Mobius accumulation
  gave the exact normalized moment `111/16`, agreeing with the energy
  polynomial evaluated at `z=-1`.

The scalar replay shares the source's ideal enumeration and
factorization routines; it is not a second independent ideal backend.
The execution receipt is `marked_review_check.json`. I did not rerun
the entire largest-case ladder. Integer bounds for the declared local
moduli are safely within signed 64-bit arithmetic, and the source's
row-energy guard covers its vector contractions. This review does not
assert that arbitrary future larger `run_case` arguments have adequate
local modular-overflow guards.

These finite checks concern sextic coefficient algebra, not the
ordinary-zeta principal-circle integral or its all-length error.
They supply no evidence for a new zero-free region.

## 5. Remaining mathematical decision

The new criterion changes the observable to a positive singly marked
squarefree count and removes the known pole by a completely specified
local term. The reduction is mathematically sound at the reviewed
scope. Its requested power error remains as difficult substantive
arithmetic work; no generic positivity or Tauberian argument in this
packet supplies it.

No smaller boundary, full RH result, or external novelty is certified
by this review.
