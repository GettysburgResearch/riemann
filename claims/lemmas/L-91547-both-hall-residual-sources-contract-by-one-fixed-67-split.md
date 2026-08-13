# L-91547 — Both Hall residual sources contract by one fixed deterministic 67-split

> **CAPACITY ASSEMBLY CORRECTED AFTER `R-91558`.**  The source, target, score
> and component-row split below is exact.  The former instruction to affine-lift
> the fixed-67 finite child is withdrawn: affine lifting can overdraw unmatched
> detail columns.  The correct physical operation is the nested identity
> embedding proved in `L-91559`.

Claim ID: `L-91547`  
Status: **PROVED EXACT SYMMETRIC POST-HALL CONTRACTION / IDENTITY-EMBEDDING THEOREM**  
Created: 2026-08-13  
Corrected: 2026-08-13  
Depends on: `L-91540`, `L-91545`, `R-91558`, `L-91559`  
RH status: **unproved pending merged producer and native-entry audits**

## 1. Positive source measures after Hall

By `L-91545`, the target-bearing outputs of the one-prime survival and hazard
Hall networks are genuine positive source measures

\[
 c_s\ge0,
 \qquad
 c_h\ge0
 \tag{L-91547.1}
\]

in paired positive kernel types at the common parent endpoint `X`.  Their target
masses satisfy

\[
 \boxed{
 \mathfrak T_{s,X}(c_s)+
 \mathfrak T_{h,X}(c_h)
 =\mathfrak T_X^{\rm parent}.
 }
 \tag{L-91547.2}
\]

Every matched Hall edge has already been removed into a target-null positive
current row bonus.  No next-prime color is attached to `c_s` or `c_h`.

## 2. Apply the same source split to both types

For `tau in {s,h}` define

\[
 \theta_\tau(n)=\mathbf1_{n\le X/67}.
 \tag{L-91547.3}
\]

The actual child source measure is

\[
 \boxed{
 c_\tau^{\rm child}
 =c_\tau|_{\{n\le X/67\}},
 }
 \tag{L-91547.4}
\]

retaining the same paired type `tau` and evaluated at endpoint `X/67`.
For each scalar kernel `K=T_tau,S_tau`, `L-91540` gives

\[
 \boxed{
 K_{\tau,X}(c_\tau)
 =K_{\tau,X/67}(c_\tau^{\rm child})
  +K_\tau^{\rm residual},
 \qquad
 K_\tau^{\rm residual}\ge0.
 }
 \tag{L-91547.5}
\]

For the exact component row, endpoint monotonicity gives

\[
 \boxed{
 R_{\tau,X}(c_\tau)
 =R_{\tau,X/67}(c_\tau^{\rm child})
  +R_\tau^{\rm residual},
 \qquad
 R_\tau^{\rm residual}\ge0.
 }
 \tag{L-91547.6}
\]

The activation frontier `n>X/67` is included in the positive residual.

## 3. Subprobability target weights

Normalize the parent target in (L-91547.2) to one and put

\[
 \omega_\tau
 =\mathfrak T_{\tau,X/67}(c_\tau^{\rm child}).
 \tag{L-91547.7}
\]

Summing the positive target residuals gives

\[
 \boxed{
 \omega_s\ge0,
 \qquad
 \omega_h\ge0,
 \qquad
 \omega_s+\omega_h\le1.
 }
 \tag{L-91547.8}
\]

Both child endpoints equal

\[
 \boxed{Y_s=Y_h=X/67<c_0X.}
 \tag{L-91547.9}
\]

The scalar target/score statement is independent of how a finite child packing
is placed back into the parent row space.

## 4. Why arithmetic colors are no longer recursive

The original binary-return architecture sent the hazard output through a
variable-`p` affine child lift and sent survival to the next ordered rough prime.
Neither operation is needed after `L-91545`:

```text
Hall has already made both target-bearing outputs positive sources;
paired-type endpoint monotonicity supplies a geometric endpoint split;
the factor-54 consumer needs contraction, not arithmetic provenance.
```

Thus the following remain removed from the load-bearing source ledger:

```text
ordered-prime survival recursion;
unique-next-prime Hall color transport;
variable-p hazard normalization;
repeated one-prime Hall projection.
```

## 5. Correct physical child placement

The child row at endpoint `X/67` and the parent row at endpoint `X` are vectors
indexed by the same average-binomial row variable.  Therefore use the identity
embedding

\[
 \boxed{
 \iota(d)(n)=d(n).
 }
 \tag{L-91547.10}
\]

Do not apply the affine map `n -> 67(n+1)-1`.

`L-91559` identifies the exact positive component-detail target

\[
 \Theta_Y(q)
 =q^{-1/2}
  [H(Y/q)-H(Y/(4q))]
 \tag{L-91547.11}
\]

and proves that it is monotone in `Y`.  For the canonical child packet, any
nonnegative row `d_child` satisfying its detail capacities may replace the
canonical component row directly:

\[
 \boxed{
 d_{\rm parent}
 =R_\tau^{\rm residual}+d_{\rm child}.
 }
 \tag{L-91547.12}
\]

The result is nonnegative and consumes no more than the canonical parent detail
capacity at every physical integer column.  Scores are inserted with coefficient
one because the identity embedding changes neither row coefficients nor
entropy.

Applying this simultaneously to `c_s,c_h`, and retaining the Hall bonuses in
the current row, gives the exact parent-capacity replacement theorem
`L-91559.27--28`.

## 6. Why the affine instruction was wrong

`R-91558` proves that the canonical detail-feasible child `Q_3`, affinely lifted
by `67` to endpoint `201`, overdraws the unmatched physical detail column
`200` by a factor greater than `277`.  Matched-fiber covariance and positive
off-fiber ordinary carry do not imply radix-four capacity feasibility.

Accordingly, the old statements

```text
fixed-67 child -> affine Pascal image;
affine leakage is harmless;
L-91329 automatically repairs arbitrary lifted finite children
```

are withdrawn from this theorem.

## 7. Boundary

```text
positive survival/hazard residual sources           EXACT
same deterministic 67 source split for both types    EXACT
both child endpoints equal X/67                      EXACT
child target weights sum <=1                         EXACT
component-row current residual nonnegative           EXACT
fixed-67 identity physical embedding                 EXACT / L-91559
fixed-67 affine detail embedding                     FALSE / R-91558
ordered-prime recursive color joint                  REMOVED
live one-prime entry normalization                    REPLAY REQUIRED
Riemann Hypothesis                                   UNPROVEN
```
