# Exact GL(2) parity/rank-deflation pilot

Status: `EXACT_RATIONAL_SYNTHETIC_CONTROL_ONLY`.

This packet supplies finite algebra and hostile controls for programmes #738 and
#741.  It contains no LMFDB sweep, no numerical L-value, and no assertion about
an arithmetic GL(2) object.  The checked fixture is the explicitly labeled
synthetic entire family

\[
 \Lambda_r(z)=z^rG(z),\qquad
 G(z)=\exp(cz^2/2+dz^4/4),\qquad c,d\in\mathbf Q.
\]

The exponential is never evaluated: its logarithmic derivative
\(F_G(z)=cz+dz^3\) gives rational kernel entries at rational nodes.

## Normalization and parity contract

Use the unitary GL(2) coordinate \(s\), with central point \(s=1/2\), and set
\(z=s-1/2\).  For a self-dual twist the centered completed function is assumed
to obey

\[
 \Lambda(-z)=\varepsilon\Lambda(z),\qquad \varepsilon\in\{+1,-1\}.
\]

If \(r=\operatorname{ord}_{z=0}\Lambda\), then
\(\varepsilon=(-1)^r\).  Factoring the *full* central order gives

\[
 \Lambda(z)=z^rG(z),\qquad G(-z)=G(z),\qquad
 F_\Lambda(z):=\frac{\Lambda'(z)}{\Lambda(z)}
     =\frac r z+F_G(z).
\]

The root number alone supplies only

\[
 r_{\rm forced}=\frac{1-\varepsilon}{2}\in\{0,1\}.
\]

Consequently, parity-only deflation leaves the even excess order
\(e=r-r_{\rm forced}\).  In particular, sign \(-1\) and analytic rank three
leaves an order-two atom after the forced simple zero is removed.  Sign \(+1\)
does not authorize any deflation, even if the actual central order is two.

The pilot does not define a classical holomorphic \(s\)-normalization.  A later
arithmetic adapter must make the unitary shift from weight/conductor/gamma data
explicit before calling this algebra.

## Two kernel conventions and the central atom

All nodes in this pilot are positive centered rationals \(x_i>0\).  Put
\(u_i=x_i^{-1}\).  The word “Pick” is not used without a formula because the
two relevant conventions have opposite central-zero signs.

### Standard divided-difference Loewner kernel

\[
 L_F(x,y)=
 \begin{cases}
  \dfrac{F(x)-F(y)}{x-y},&x\ne y,\\[4pt]
  F'(x),&x=y.
 \end{cases}
\]

For \(F(z)=r/z\), including on the diagonal,

\[
 L_{r/z}(x,y)=-\frac r{xy}.
\]

Hence

\[
 L_{F_\Lambda}=L_{F_G}-r uu^{\mathsf T},\qquad
 L_{F_G}=L_{F_\Lambda}+r uu^{\mathsf T}.
\]

The raw central atom is negative semidefinite and rank one when \(r>0\).

### Actual-Xi-style sum/Hankel kernel

The integrated actual-Xi Pick packet instead uses

\[
 H_F(x,y)=\frac{F(x)+F(y)}{x+y}.
\]

For the same logarithmic derivative,

\[
 H_{r/z}(x,y)=+\frac r{xy},
\]

so

\[
 H_{F_\Lambda}=H_{F_G}+r uu^{\mathsf T},\qquad
 H_{F_G}=H_{F_\Lambda}-r uu^{\mathsf T}.
\]

Here the raw atom is positive semidefinite.  A determinant sign observed before
declaring the kernel convention is therefore uninterpretable.

## Exact determinant and inertia consequences

Both cases have

\[
 M(r)=B+\sigma r uu^{\mathsf T},\qquad
 \sigma=\begin{cases}-1&\text{divided difference},\\+1&\text{sum kernel}.
 \end{cases}
\]

The determinant is affine in \(r\), even when \(B\) is singular:

\[
 \det M(r)=\det B+\sigma r\,u^{\mathsf T}\!\operatorname{adj}(B)u.
\]

If \(B\) is invertible, this is

\[
 \det M(r)=\det B\bigl(1+\sigma r\,u^{\mathsf T}B^{-1}u\bigr).
\]

By rank-one interlacing, each of the positive and negative inertia counts can
change by at most one.  On \(u^\perp\), the quadratic form is unchanged.  These
facts impose two firewalls:

1. A raw divided-difference negative direction may be only the legitimate
   central zero.
2. Full deflation cannot cure a negative direction already present in \(B\).

The implementation computes determinant, rank, and Sylvester inertia over
`Fraction`; it uses no floating-point eigenvalue threshold.

## Checked controls

Inertia is displayed as \((n_+,n_-,n_0)\).  The quadratic controls use
\(c=1,d=0\), nodes \((1,2)\), and background matrix \(B=\mathbf1\mathbf1^T\).

| control | convention | raw determinant / inertia | parity-deflated | fully deflated |
|---|---|---|---|---|
| sign \(-1\), \(r=1\) | divided difference | \(-1/4\), \((1,1,0)\) | \(0\), \((1,0,1)\) | \(0\), \((1,0,1)\) |
| sign \(-1\), \(r=1\) | sum | \(+1/4\), \((2,0,0)\) | \(0\), \((1,0,1)\) | \(0\), \((1,0,1)\) |
| sign \(-1\), \(r=3\) | divided difference | \(-3/4\), \((1,1,0)\) | \(-1/2\), \((1,1,0)\) | \(0\), \((1,0,1)\) |
| sign \(-1\), \(r=3\) | sum | \(+3/4\), \((2,0,0)\) | \(+1/2\), \((2,0,0)\) | \(0\), \((1,0,1)\) |
| sign \(+1\), \(r=2\) | divided difference | \(-1/2\), \((1,1,0)\) | unchanged | \(0\), \((1,0,1)\) |
| sign \(+1\), \(r=2\) | sum | \(+1/2\), \((2,0,0)\) | unchanged | \(0\), \((1,0,1)\) |

The hostile quartic control uses \(c=d=1\) and nodes \((1,2,4)\).  After full
deflation its divided-difference background has determinant \(-36\) and inertia
\((2,1,0)\); its sum-kernel background has determinant \(+36\) and inertia
\((1,2,0)\).  Thus deflation is exact bookkeeping, not a positivity theorem.

The fixture also contains a positive-sign/odd-order mismatch and confirms that
the API rejects it before constructing a matrix.

## Nominated quadratic-twist moment

Fix a source-locked self-dual primitive GL(2) object \(f\).  For fundamental
quadratic discriminants in an explicitly defined sign subfamily
\(\mathcal D_\varepsilon(X)\), let

\[
 r_d=\operatorname{ord}_{s=1/2}\Lambda(f\otimes\chi_d,s),\qquad
 e_d=r_d-\frac{1-\varepsilon}{2}\in2\mathbf Z_{\ge0}.
\]

For either convention, the exact residual after parity-only rather than full
deflation is

\[
 M_d^{\rm parity}-M_d^{\rm full}=\sigma e_d uu^{\mathsf T}.
\]

Therefore the detector-relevant second moment is exactly

\[
 \frac1{|\mathcal D_\varepsilon(X)|}
 \sum_{d\in\mathcal D_\varepsilon(X)}
 \left\|M_d^{\rm parity}-M_d^{\rm full}\right\|_F^2
 =\left(\sum_i x_i^{-2}\right)^2
 \frac1{|\mathcal D_\varepsilon(X)|}\sum_d e_d^2.
\]

**First arithmetic target (`TWIST-EXCESS-RANK-L2`).** Prove a uniform bound
\(\sum_d e_d^2\ll_f|\mathcal D_\varepsilon(X)|\) for one fully specified twist
family.  The stronger minimalist target is average \(e_d^2=o(1)\).  Neither is
claimed here.  The latter entails density-one minimal rank plus control of the
high-rank tail; it must not be advertised as a finite-matrix consequence.

This target is preferable to averaging raw determinant signs: its normalization
is exact, convention-independent after squaring, and isolates precisely the
central-rank contamination.

## Arithmetic adapter still required

Before any genuine GL(2) row enters this atlas, lock all of the following:

- the object, conductor, weight, nebentypus, self-duality, and unitary completed
  normalization;
- the discriminant range, bad-prime exclusions, and independently checked root
  number;
- the rigor level of the asserted central order (proved, interval-certified, or
  exploratory numerical only);
- zero-free evaluation nodes and certified values of the *deflated* logarithmic
  derivative.

The present synthetic fixture satisfies none of those arithmetic data fields by
design.

## Reproduction

From the repository root:

```powershell
python research\l-families\atlas\gl2\verify.py
python tests\test_gl2_deflation.py
```

The verifier reads `fixtures/synthetic_controls.json` and prints a deterministic
JSON report.  The focused suite checks 15 exact identities and hostile cases.

## Files

- `deflation.py`: exact API and rational linear algebra;
- `fixtures/synthetic_controls.json`: four positive controls plus one fail-closed
  parity mismatch, all explicitly synthetic;
- `verify.py`: deterministic control report;
- `tests/test_gl2_deflation.py`: focused regression suite.
