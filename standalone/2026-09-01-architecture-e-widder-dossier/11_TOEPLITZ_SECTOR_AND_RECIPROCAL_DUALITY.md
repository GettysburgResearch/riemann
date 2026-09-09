# Toeplitz sector, the 2026 cubic wedge, and reciprocal rectangle duality

Status: **EXACT BRIDGES PLUS EXPLICITLY IMPORTED 2026 RESULTS; RH REMAINS UNPROVED.**

The invariant count law is a Pólya-frequency problem.  This note connects it
to the strongest current coefficient-side theorems and adds an exact
reciprocal duality that exchanges Toeplitz order with Toeplitz shift.  The
result is a two-ended attack on the coefficient cone rather than a second
copy of the Widder derivative hierarchy.

No external priority claim is made.  Results from July 2026 are imported with
their stated scope.

## 1. Centered and invariant coefficient coordinates

The centered coefficient function used in the recent Toeplitz literature is

\[
 \boxed{
 G(z)=\frac18\xi_{\rm R}\left(
  \frac12+\frac{\sqrt z}{2}
 \right)
 =\sum_{n\ge0}a_nz^n,
 \qquad a_n>0.
 }
 \tag{1.1}
\]

The invariant function of this dossier is

\[
 \mathfrak X(u)
 =\xi_{\rm R}\left(
  \frac12+\sqrt{u+\frac14}
 \right).
\]

They are related by the exact affine identity

\[
 \boxed{
 \mathfrak X(u)=8G(4u+1).
 }
 \tag{1.2}
\]

Thus the invariant positive coefficients are the positive upper-binomial
transform

\[
 \boxed{
 c_n=8\,4^n\sum_{m\ge n}\binom mn a_m.
 }
 \tag{1.3}
\]

Both entire functions have order `1/2`.  RH is equivalent to either
coefficient sequence being `PF_infinity`.

The affine translation is useful for zero sectors: subtracting a positive
real number from a zero already in the left half-plane decreases its angular
deviation from the negative real axis.  Hence every Schoenberg sector bound
valid for the centered zeros transfers, with no loss, to the invariant zeros.

## 2. Imported verified-height sector cone

W. Michałowski,
*An explicit uniform cubic wedge for consecutive Toeplitz minors of the
Riemann xi coefficients*, arXiv:2607.16795, records the following application
of Schoenberg's sector theorem.

Let

\[
 D^G_{r,k}=\det[a_{k+j-i}]_{i,j=0}^{r-1},
 \qquad a_n=0\quad(n<0).
\]

Using the rigorous Platt--Trudgian verification through height

\[
 H=3{,}000{,}175{,}332{,}800,
\]

Schoenberg's theorem gives `PF_m` whenever

\[
 m+1\le\pi H.
\]

The present repository's conservative external lock uses `H=3*10^12` and
requires no simplicity.  Since `pi>3.14`, it follows conservatively that

\[
 \boxed{
 r\le9{,}419{,}999{,}999{,}999
 \Longrightarrow
 D^G_{r,k}\ge0
 \quad\text{for every }k\ge0.
 }
 \tag{2.1}
\]

The same sector conclusion holds for the invariant coefficient sequence
`(c_n)`, because of the angle-improving translation (1.2):

\[
 \boxed{
 r\le9{,}419{,}999{,}999{,}999
 \Longrightarrow
 D^{\mathfrak X}_{r,k}\ge0
 \quad\text{for every }k\ge0.
 }
 \tag{2.2}
\]

This is a coefficient-minor theorem, not the same indexing as the
`4.71*10^12` diagonal Widder cone.  The two results are complementary.

The external zero verification is imported through the existing repository
lock and was not rerun.

## 3. Imported uniform cubic tail

The main theorem of arXiv:2607.16795 is

\[
 \boxed{
 D^G_{r,k}>0
 \qquad
 (r\ge2,\ k\ge10^{18}r^3).
 }
 \tag{3.1}
\]

It is independent of numerical zero verification.  Its proof combines a
certified complex saddle analysis, an exact `q`-Pascal dilation semigroup, a
weighted Banach-algebra majorant and inertia preservation.

The theorem applies as stated to the centered coefficients `(a_n)`.  No
transfer of the cubic constant to the affine-translated invariant sequence is
asserted here.  A finite-order Pólya-frequency property is not automatically
preserved by every operation that preserves `PF_infinity`.

The cited paper explicitly identifies its scope:

```text
low Toeplitz order: paid by the verified-height sector theorem;
high shift k >> r^3: paid by the cubic wedge;
critical region k comparable with r: open.
```

The invariant count and Fock formulations in the preceding notes target this
open central region rather than duplicating the cubic tail.

## 4. Exact reciprocal rectangle duality

Let

\[
 A(z)=\sum_{n\ge0}\alpha_nz^n,
 \qquad \alpha_0=1,
\]

and define its signed reciprocal

\[
 \boxed{
 B(z)=\frac1{A(-z)}=\sum_{n\ge0}\beta_nz^n.
 }
 \tag{4.1}
\]

Use the one-sided convention `alpha_n=beta_n=0` for `n<0`, and put

\[
 D^A_{r,k}
 =\det[\alpha_{k+j-i}]_{i,j=0}^{r-1},
\]

\[
 D^B_{k,r}
 =\det[\beta_{r+j-i}]_{i,j=0}^{k-1}.
\]

### Theorem 4.1 — reciprocal rectangle identity

For every `r,k>=1`,

\[
 \boxed{
 D^A_{r,k}=D^B_{k,r}.
 }
 \tag{4.2}
\]

#### Proof

Formally write

\[
 A(z)=\prod_j(1+x_jz).
\]

Then `alpha_n=e_n(x)` and, from (4.1), `beta_n=h_n(x)`.  The determinant on
the left is the dual Jacobi--Trudi formula for the rectangular Schur function
with shape `(r^k)`:

\[
 D^A_{r,k}
 =\det[e_{k+j-i}]_{i,j=0}^{r-1}
 =s_{(r^k)}(x).
\]

The ordinary Jacobi--Trudi formula for the same rectangle gives

\[
 s_{(r^k)}(x)
 =\det[h_{r+j-i}]_{i,j=0}^{k-1}
 =D^B_{k,r}.
\]

The identity is polynomial in the formal coefficients and therefore holds for
arbitrary formal power series with constant term one.  `square`

The exact checker
[`verify_order_product_and_reciprocal.py`](verify_order_product_and_reciprocal.py)
reconstructs the reciprocal series and verifies (4.2) on 108 rational
rectangle cells.

## 5. Meaning of the duality

The identity exchanges the two difficult directions:

```text
large Toeplitz order r, fixed shift k for A
        <=>
fixed Toeplitz order k, large shift r for B=1/A(-z).
```

For the invariant count law, `B` is the complete-homogeneous or bosonic
partner of the elementary/fermionic coefficient sequence.  Under RH,

\[
 A(z)=\prod_j(1+x_jz),
 \qquad
 B(z)=\prod_j(1-x_jz)^{-1},
 \qquad x_j>0.
\]

Then every rectangle is the same positive Schur function viewed in two
bases.

Without RH, (4.2) remains exact, but it does not make finite-order positivity
self-dual automatically.  Proving `PF_k` for `A` from `PF_k` for `B`, or vice
versa, needs additional hypotheses.  The identity is a transport of the
precise minor, not a closure theorem.

## 6. Pole-dominance route on the reciprocal side

The poles of `B` are the negatives of the zeros of `A`.  If the first `k`
poles by modulus are positive real and separated from the remaining poles,
then a standard residue/Cauchy--Binet expansion shows that the fixed-order
minor

\[
 D^B_{k,n}
\]

is eventually positive as `n->infinity`.  In the finite model with exactly
`k` positive reciprocal variables,

\[
 B(z)=\prod_{j=1}^k(1-x_jz)^{-1},
 \qquad x_j>0,
\]

one has the exact identity

\[
 \boxed{
 D^B_{k,n}=s_{(n^k)}(x_1,\ldots,x_k)
 =(x_1\cdots x_k)^n>0.
 }
 \tag{6.1}
\]

Farther poles give an exponentially smaller perturbation in fixed order.
A rigorous infinite version must handle tied moduli, multiplicity and
confluent Vandermonde blocks.  The repository's verified-height theorem does
not assume simplicity, so no unconditional simplicity-based corollary is
claimed here.

This suggests a precise vertical-tail project:

> Prove a confluent reciprocal-tail theorem with explicit threshold from the
> verified real pole block and the exact tail geometry of the remaining
> invariant poles.

Through (4.2), that theorem would pay all sufficiently large Toeplitz orders
at each fixed shift.

An off-line conjugate pair explains why uniformity in the shift is hard.  If a
dominant pole selection cuts one member of a conjugate pair, the leading
finite exponential sum has an oscillatory phase.  The vertical minors are
therefore a direct detector of the same phase rotation seen by the E–Widder
power traces.

## 7. Combined coefficient frontier

The coefficient architecture now has three exact or imported regions:

1. **sector cone:** every minor order below `9.42*10^12`, at every shift;
2. **centered cubic wedge:** every `D^G_(r,k)` with `k>=10^18 r^3`;
3. **reciprocal duality:** every remaining rectangle can be read in the
   transposed bosonic coordinate.

The region not addressed by these theorems has both rectangle dimensions
large and lies away from the cubic tail.  In particular, the genuinely
RH-sensitive geometry remains the broad diagonal regime in which order and
shift are comparable.

The theta quasi-free gate attacks exactly that regime: one positive
contraction would make every rectangle Schur-positive simultaneously.

## 8. Concrete synthesis target

Let `A_v(z)=mathfrak X(vz)/mathfrak X(v)`.  A source-built contraction `K_v`
would provide

\[
 A_v(z)=\det(I-K_v+zK_v),
\]

and therefore

\[
 D^{A_v}_{r,k}
 =s_{(r^k)}(\kappa_1,\kappa_2,\ldots)\ge0
\]

for all rectangles at once.  The reciprocal would be

\[
 \frac1{A_v(-z)}
 =\det(I-zK_v)^{-1},
\]

so (4.2) would become literal fermion--boson equality of exterior and
symmetric-power characters.

This is the cleanest interface between:

- Architecture E's Stieltjes/Widder condition;
- the theta–Fock mixture;
- the Segre/Koszul exterior-character calculations;
- the modern Toeplitz-minor programme.

## 9. Review checklist

Independent review should check:

1. the affine relation (1.2) and coefficient transform (1.3);
2. the angle-improvement under left translation;
3. the exact scope of Schoenberg's sector theorem;
4. the conservative integer in (2.1)--(2.2);
5. that the July 2026 cubic wedge is imported only for the centered sequence;
6. the rectangle orientation in the two Jacobi--Trudi formulas;
7. formal-power-series passage in Theorem 4.1;
8. the absence of a claimed finite-order reciprocal closure;
9. the multiplicity boundary in the proposed reciprocal-tail route;
10. the distinction between imported coefficient theorems and the open
    source-built quasi-free determinant.
