# R-91620 — Scalar entropy equality does not identify the annular model output

Claim ID: `R-91620`  
Status: **EXACT SOURCE-IDENTIFICATION FIREWALL**  
Created: 2026-08-12  
Depends on: `L-91620/L-91621`; `R-91407`; `R-91520`  
RH status: **unproved**

## 1. The tempting shortcut

The one-node annular log mass is nonnegative and additive.  The arithmetic
source also has natural additive logarithmic quantities.  It is tempting to
prove equality of two scalar totals and declare the annular output absent.

That inference is not valid without a canonical source-to-model
factorization.

## 2. Positive scalar totals admit arbitrary hidden splits

Fix any `L>0`.  For every `0<=h<=L`,

\[
 L=(L-h)+h
\]

is a decomposition into two nonnegative terms.  Reading the first term as a
critical/stable output and the second as a hyperbolic output is compatible with
the same total scalar.

Therefore the assertions

\[
 \mathscr L^{\rm arith}=L
\]

and

\[
 \mathscr L^{\rm crit}+\mathscr L^{\rm st}=L
\]

must be proved as outputs of the **same isometry or multiplicative
factorization** before one may conclude that the hyperbolic channel is zero.

## 3. One node detects absence but not source provenance

A nonconstant Blaschke product satisfies

\[
 |B(\eta)|<1
\]

at every interior point.  Hence one node is enough to detect whether the
annular factor is constant.

But the scalar value `|B(eta)|` does not reveal which arithmetic source port
produced it.  Distinct Blaschke zero configurations can have the same modulus
at one node.  For example, at `eta=1`,

\[
 \zeta_1=\frac15,
 \qquad
 \zeta_2=\frac3{10}+i\sqrt{\frac{47}{100}}
\]

satisfy

\[
 |b_{\zeta_1}(1)|^2
 =|b_{\zeta_2}(1)|^2
 =\frac49.
\]

The one-node scalar is a perfect **zero/nonzero detector** after the model
factor has been identified; it is not, by itself, a source-identification
theorem.

## 4. Entropy curves do not repair the omission

`L-91620` writes the scalar log mass as the complete resolvent curve

\[
 t\longmapsto
 \frac{2\eta H}{1+2\eta tH}.
\]

This curve is determined by the single scalar `H`.  Knowing it at every
`t in [0,1]` supplies no additional source provenance.  A hidden nonnegative
annular remainder can still be absorbed into an undeclared stable scalar unless
the common multiplicative map has already been constructed.

## 5. Correct target

The valid conclusion-producing statement is a source-ordered decomposition

\[
 \mathscr L^{\rm arith}
 =\mathscr L^{\rm crit}
  +\mathscr L^{\rm st}
  +\Lambda^{\rm ann}
  +\mathscr L^{\rm aux}
\]

with all four terms produced by one declared factorization, followed by exact
or cofinal exhaustion of the first two outputs.

## 6. Exact boundary

```text
one-node annular log mass detects nonconstant B       EXACT
same scalar total identifies model provenance          FALSE
full resolvent entropy curve repairs provenance        FALSE
source-ordered multiplicative factorization            OPEN / RH-BEARING
Riemann Hypothesis                                     UNPROVED
```
