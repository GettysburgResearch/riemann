# Theta–Darboux/Andreief factorization of the coefficient cone

Status: **PROPOSED EXACT SOURCE FACTORIZATION; INDEPENDENT REVIEW REQUIRED; THE RESULTING SIGN GATE, THE ALL-ORDER E–WIDDER INEQUALITY, AND RH REMAIN OPEN.**

The theta–Fock note identifies the invariant xi coefficient law as a positive
mixture of quasi-free fibers.  The obstacle is the common latent theta
selector: a positive mixture of determinants need not be one determinant.

This note rewrites that obstacle at the level of every Toeplitz minor.  The
result is an exact continuous Cauchy–Binet formula.  One factor is a strictly
totally-positive, completely explicit Pascal/Bessel kernel.  Every unresolved
sign is concentrated in one exterior determinant formed from the actual
Riemann theta kernel and its iterates under the invariant lowering operator.

The formula is source-local and contains no zeta zero.  It does not by itself
prove the sign of the remaining theta determinant.

## 1. Invariant coefficient basis

Use the actual even full-line Riemann kernel `Phi`, normalized by

\[
 \xi_{\rm R}\left(\frac12+x\right)
 =\int_{\mathbb R}\Phi(\tau)e^{x\tau}\,d\tau
 =2\int_0^\infty\Phi(\tau)\cosh(x\tau)\,d\tau.
 \tag{1.1}
\]

Retain

\[
 \mathfrak X(u)
 =\xi_{\rm R}\left(\frac12+\sqrt{u+\frac14}\right)
 =\sum_{n\ge0}c_nu^n.
\]

Define the invariant coefficient functions

\[
 \boxed{
 b_n(\tau)
 =[u^n]\cosh\left(\tau\sqrt{u+\frac14}\right),
 \qquad n\ge0.
 }
 \tag{1.2}
\]

Then

\[
 \boxed{
 c_n=2\int_0^\infty\Phi(\tau)b_n(\tau)\,d\tau.
 }
 \tag{1.3}
\]

All terms are positive.  The coefficient functions have the two exact forms

\[
 \boxed{
 b_n(\tau)
 =\sum_{m\ge n}
 \binom mn4^{-(m-n)}
 \frac{\tau^{2m}}{(2m)!}
 }
 \tag{1.4}
\]

and

\[
 \boxed{
 b_n(\tau)
 =\frac{\sqrt\pi}{2n!}
 \tau^{n+1/2}I_{n-1/2}(\tau/2).
 }
 \tag{1.5}
\]

The power-series form will be used for total positivity; the Bessel form
identifies the spectral family already visible in the theta–Fock packet.

## 2. The invariant lowering operator

Put

\[
 \boxed{
 L=\frac{d^2}{d\tau^2}-\frac14.
 }
 \tag{2.1}
\]

The generating function satisfies

\[
 L\cosh\left(\tau\sqrt{u+\frac14}\right)
 =u\cosh\left(\tau\sqrt{u+\frac14}\right).
\]

Coefficient comparison gives

\[
 \boxed{
 Lb_n=b_{n-1},
 \qquad b_{-1}=0.
 }
 \tag{2.2}
\]

Every `b_n` is even.  The actual kernel `Phi` and all `L^h Phi` are even and
superexponentially decreasing.  Therefore repeated integration by parts on
`(0,infinity)` has no boundary contribution: the endpoint `0` terms vanish by
evenness, and the endpoint at infinity vanishes by the theta tail.  Hence,
whenever `0<=h<=n`,

\[
 \boxed{
 c_{n-h}
 =2\int_0^\infty
 (L^h\Phi)(\tau)b_n(\tau)\,d\tau.
 }
 \tag{2.3}
\]

The first rung `L Phi` is the next invariant theta-current kernel.  The
entire ladder remains attached to the actual source before any determinant is
taken.

## 3. Strict total positivity of the coefficient kernel

### Theorem 3.1

The kernel

\[
 (\tau,n)\longmapsto b_n(\tau)
\]

is strictly totally positive of infinite order on

\[
 (0,\infty)\times\mathbb Z_{\ge0}.
\]

#### Proof

Write (1.4) as the composition

\[
 b_n(\tau)=\sum_{m\ge0}E(\tau,m)P(m,n),
 \tag{3.1}
\]

where

\[
 E(\tau,m)=\frac{\tau^{2m}}{(2m)!}
\]

and

\[
 P(m,n)=
 \begin{cases}
 \binom mn4^{-(m-n)},&m\ge n,\\
 0,&m<n.
 \end{cases}
\]

For increasing positive `tau_i` and increasing integer `m_j`, every minor of
`E` is a positive row/column scaling of the generalized Vandermonde

\[
 \det[(\tau_i^2)^{m_j}]>0.
\]

Thus `E` is strictly totally positive.  The Pascal kernel
`(m,n)->binom(m,n)` is totally nonnegative of infinite order; the powers of
four are positive row and column scalings, so `P` is also totally
nonnegative.

Apply finite Cauchy–Binet after truncating the intermediate index `m`, then
let the truncation tend to infinity.  Absolute convergence follows from the
factorials in `E`.  Every minor of the composition is nonnegative.  Strictness
follows from the single intermediate set `m_j=n_j`: the corresponding Pascal
minor is lower triangular with diagonal one, while the associated
Vandermonde minor of `E` is strictly positive.  `square`

This proof is independent of the recent real-order Bessel total-positivity
theorem.  Formula (1.5) shows that the two mechanisms agree on the same
kernel.

## 4. Arbitrary positive-index Toeplitz minors

Use the one-sided convention `c_n=0` for `n<0`.  Let

\[
 I=(i_1<\cdots<i_r),
 \qquad
 J=(j_1<\cdots<j_r)
\]

be integer row and column sets satisfying

\[
 \boxed{j_1\ge i_r.}
 \tag{4.1}
\]

Thus every entry `c_(j_q-i_p)` lies in the nonnegative coefficient range.
Translate both index sets by `-i_1` and put

\[
 h_p=i_p-i_1,
 \qquad
 n_q=j_q-i_1.
\]

Then

\[
 0=h_1<\cdots<h_r\le n_1<\cdots<n_r.
\]

Equation (2.3) gives the separated inner-product representation

\[
 \boxed{
 c_{j_q-i_p}
 =2\int_0^\infty
 (L^{h_p}\Phi)(\tau)b_{n_q}(\tau)\,d\tau.
 }
 \tag{4.2}
\]

Define

\[
 \mathcal T_I(\tau_1,\ldots,\tau_r)
 =\det[(L^{h_p}\Phi)(\tau_\ell)]_{p,\ell=1}^r
 \tag{4.3}
\]

and

\[
 \mathcal B_J(\tau_1,\ldots,\tau_r)
 =\det[b_{n_q}(\tau_\ell)]_{q,\ell=1}^r.
 \tag{4.4}
\]

Andreief's continuous Cauchy–Binet identity, followed by restriction to the
ordered chamber, gives the central factorization

\[
 \boxed{
 \det[c_{j_q-i_p}]_{p,q=1}^r
 =2^r\int_{0<\tau_1<\cdots<\tau_r}
 \mathcal T_I(\boldsymbol\tau)
 \mathcal B_J(\boldsymbol\tau)
 \,d\boldsymbol\tau.
 }
 \tag{4.5}
\]

By Theorem 3.1,

\[
 \boxed{
 \mathcal B_J(\boldsymbol\tau)>0
 \qquad(0<\tau_1<\cdots<\tau_r).
 }
 \tag{4.6}
\]

Thus every unresolved sign in the positive-index Toeplitz cone is isolated
in the one theta–Darboux exterior determinant `mathcal T_I`.

No independent theta selector remains in (4.5): the common-selector problem
has become one continuous exterior integral with a strictly positive test
kernel.

## 5. Consecutive rectangle form

For the consecutive Toeplitz minors

\[
 D_{r,k}
 =\det[c_{k+j-i}]_{i,j=0}^{r-1},
 \qquad k\ge r-1,
\]

(4.5) becomes

\[
 \boxed{
 D_{r,k}
 =2^r\int_{0<\tau_1<\cdots<\tau_r}
 \det[(L^i\Phi)(\tau_\ell)]_{i=0}^{r-1}
 \det[b_{k+j}(\tau_\ell)]_{j=0}^{r-1}
 \,d\boldsymbol\tau.
 }
 \tag{5.1}
\]

The second determinant is strictly positive.  It carries the Toeplitz shift
`k`; the first determinant is independent of `k` and contains the complete
arithmetic theta source.

This cleanly separates the two axes:

```text
Toeplitz order r  -> exterior rank of the theta-Darboux ladder;
Toeplitz shift k  -> positive Pascal/Bessel test kernel.
```

The imported cubic wedge controls the large-`k` tail by asymptotics.  Formula
(5.1) is an exact source representation of the complementary central region.

## 6. The theta–Darboux gate

A pointwise theorem

\[
 \mathcal T_I(\boldsymbol\tau)\ge0
\]

for every index set and ordered source packet would be sufficient for the
positive-index Toeplitz cone.  It is deliberately **not** asserted here.
Positive-source and positive-mixture firewalls show that such an entrywise
strengthening must be tested rather than assumed.

The exact necessary source target supplied by (4.5) is weaker and weighted.

### Theta–Darboux/Andreief gate `TDA`

For every increasing `I,J` satisfying (4.1), prove

\[
 \boxed{
 \int_{0<\tau_1<\cdots<\tau_r}
 \mathcal T_I(\boldsymbol\tau)
 \mathcal B_J(\boldsymbol\tau)
 \,d\boldsymbol\tau\ge0.
 }
 \tag{TDA}
\]

This is exactly the corresponding Toeplitz minor.  Its advantage over the
original statement is structural:

- `mathcal B_J` is now known to be strictly totally positive;
- all arithmetic dependence is in one explicit exterior current;
- the source scale is retained before integration;
- no average of Fredholm determinants is replaced by a determinant of an
  average;
- exterior rank and coefficient shift are separated.

A successful proof may use variation diminution rather than pointwise
positivity.  For example, it would suffice to control the sign changes of
`mathcal T_I` in the ordered chamber and show that the Pascal/Bessel kernel
places the integral on its positive side.

## 7. Relation to the quasi-free gate

The theta–Fock decomposition asks for one positive contraction whose entire
exterior character matches the arithmetic mixture.  Formula (4.5) is the
coefficient-minor version of the same demand.

Under a source-built contraction `K_v`, every minor would be a positive Schur
function of its eigenvalues.  In (4.5), the same Schur positivity must emerge
from the pairing of:

- the actual theta–Darboux exterior current `mathcal T_I`;
- the strictly positive coefficient propagator `mathcal B_J`.

Thus `TDA` is not a competing architecture.  It is the continuous
Cauchy–Binet form of the latent-selector removal required by `TQF(v)`.

The Segre/Koszul source may enter by organizing the exterior determinant
`mathcal T_I`; the Bessel/Pascal factor already supplies the positive
propagator that the Euler-characteristic calculations lacked.

## 8. Relation to the fixed-centre heat formulation

The companion note identifies

\[
 K(t)=e^{-t/4}\sum_\rho e^{-t\gamma_\rho^2}
\]

and reduces RH to complete monotonicity of `K`.  The operator `L` in the
present note is the same invariant lowering operator that shifts powers of
`u` in the theta coefficient expansion.  Hence the two source gates are
adjoint views of one ladder:

```text
coefficient side:  move L from b_n onto Phi, then use Andreief;
heat side:         move invariant derivatives into heat time, then use Laplace.
```

A positive intertwiner between `mathcal T_I` and the heat derivatives of `K`
would simultaneously settle the Toeplitz, quasi-free and E–Widder forms.

## 9. Immediate theorem-sized attacks

The next source work should be organized around the exact integral (5.1).

1. **Sign-variation census.**  Determine, analytically, the number and
   orientation of sign chambers of
   
   \[
   \det[(L^i\Phi)(\tau_\ell)]_{i=0}^{r-1}
   \]
   
   before attempting a pointwise theorem.
2. **Variation-diminishing integration.**  Use strict total positivity of
   `b_n(tau)` to transport that chamber information into the weighted sign of
   (5.1).
3. **Darboux factorization.**  Search for a source-defined sequence of
   first-order transforms that triangularizes the `L`-ladder while preserving
   the ordered theta endpoints.
4. **Heat intertwiner.**  Express the theta–Darboux determinant as a positive
   integral of fixed-centre heat derivatives or Bernstein cells.
5. **Boundary/reciprocal completion.**  Combine the positive-index chamber
   with the exact reciprocal rectangle identity for minors crossing the
   one-sided boundary.

A finite-rank result is useful only if it reveals a uniform sign-variation or
intertwining theorem.  Another broad minor scan is not the target.

## 10. Exact status

```text
invariant coefficient integral c_n=2 int Phi b_n        PROPOSED EXACT / REVIEW
lowering law L b_n=b_(n-1)                               PROPOSED EXACT / REVIEW
strict TP of the Pascal/Bessel coefficient kernel        PROPOSED COMPLETE / REVIEW
arbitrary-minor Andreief factorization                    PROPOSED EXACT / REVIEW
all arithmetic isolated in theta-Darboux determinant      PROPOSED EXACT / REVIEW
pointwise theta-Darboux positivity                        NOT ASSERTED
weighted theta-Darboux gate TDA                           OPEN / RH-BEARING
theta quasi-free gate TQF                                 OPEN / RH-EQUIVALENT
all-order E-Widder inequality                             OPEN / RH-EQUIVALENT
Riemann Hypothesis                                        UNPROVED
```

## 11. Review checklist

Independent review should check:

1. the full-line/half-line factor in (1.1)--(1.3);
2. the series and Bessel normalizations in (1.4)--(1.5);
3. self-adjoint boundary cancellation for repeated `L` integrations;
4. total positivity and strictness in Theorem 3.1;
5. the index translation in (4.2);
6. the factor `2^r` and ordered-chamber normalization in (4.5);
7. the orientation of both determinants;
8. the condition `j_1>=i_r`;
9. the distinction between pointwise and weighted theta-Darboux positivity;
10. the relationship to `TQF`, reciprocal duality and the heat trace.
