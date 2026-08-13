# L-91549 — The affine child lift is score-loss nonexpansive on matched fibers, but is not physically detail-capacity faithful

> **CORRECTED AFTER `R-91558`.**  The entropy-amplification and conditional
> score-loss inequalities below are exact.  The former claim that the affine
> lift supplied a capacity-faithful fixed-67 physical assembly is false.
> `R-91558` gives the exact canonical counterexample `Y=3`, row `Q_3`,
> `m=67`, parent column `Q=200`.  The fixed-67 reset must use the nested
> identity embedding of `L-91559`, not this affine lift.

Claim ID: `L-91549`  
Status: **PARTIALLY RETAINED SCORE THEOREM / PHYSICAL DETAIL-CAPACITY APPLICATION REFUTED**  
Created: 2026-08-13  
Corrected: 2026-08-13  
Depends on: `L-91318`; corrected by `R-91558/L-91559`  
RH status: **unproved**

## 1. Child packing and loss

Let a positive typed child packet at endpoint `Y=X/m`, `m>=1`, have declared
source score

\[
 J_Y\ge0.
 \tag{L-91549.1}
\]

Let `d(n)>=0` be a finite child row packing with entropy score

\[
 \mathcal S_Y(d)=\sum_nd(n)G_n.
 \tag{L-91549.2}
\]

Its packet loss is

\[
 \boxed{
 \ell_Y(d)=J_Y-\mathcal S_Y(d).
 }
 \tag{L-91549.3}
\]

No positivity of `ell_Y` is required.

## 2. Exact affine score lift

Use

\[
 \Phi_m(n)=m(n+1)-1
 \tag{L-91549.4}
\]

and define

\[
 \boxed{
 D(\Phi_m(n))=m^{-1/2}d(n),
 }
 \tag{L-91549.5}
\]

with zero coefficients off the affine image.

`L-91318` proves:

1. exact carry covariance on the matched fiber `Q=mq`;
2. exact radix-four covariance on that same matched fiber;
3. nonnegativity of the lifted row;
4. entropy amplification
   \[
   \boxed{
   \mathcal S_X(D)
   \ge\sqrt m\,\mathcal S_Y(d)
   \ge\mathcal S_Y(d).
   }
   \tag{L-91549.6}
   \]

The fourth statement is global and independent of capacity feasibility.

## 3. Conditional inherited-loss inequality

If an external theorem has already proved that `D` is admissible in the parent
physical capacity ledger and if the child declared score enters with
coefficient one, then

\[
\begin{aligned}
 J_Y-\mathcal S_X(D)
 &\le J_Y-\mathcal S_Y(d)\\
 &=\ell_Y(d).
\end{aligned}
\]

Hence, under those two hypotheses,

\[
 \boxed{
 \ell_X^{\rm inherited}(D)
 \le\ell_Y(d).
 }
 \tag{L-91549.7}
\]

The favorable score reserve is

\[
 \mathcal S_X(D)-\mathcal S_Y(d)
 \ge(\sqrt m-1)\mathcal S_Y(d).
 \tag{L-91549.8}
\]

## 4. Target-mass homogeneity

For an actual child packet of target mass `omega>=0`, positive homogeneity gives

\[
 J_Y\mapsto\omega J_Y,
 \qquad
 d\mapsto\omega d,
 \qquad
 \ell_Y\mapsto\omega\ell_Y.
 \tag{L-91549.9}
\]

Therefore, whenever the externally supplied parent-capacity embedding exists,

\[
 \boxed{
 \ell_X^{\rm inherited}
 \le\omega\ell_Y(\widehat d).
 }
 \tag{L-91549.10}
\]

This algebra never creates a factor `sqrt(m)`, `m`, or `m^-1/2` in front of
the child loss.

## 5. The former physical-capacity application is false

Matched-fiber covariance does not imply feasibility at unmatched physical
columns.  Positive ordinary carry outside the matched fiber is adverse in an
upper-capacity problem, and the radix-four operator is not positive.

`R-91558` takes the canonical child component packet

\[
 d=Q_3,
 \qquad
 d(2)=\frac3{\sqrt2}\log\frac32,
 \tag{L-91549.11}
\]

which is detail feasible at endpoint `3`.  Its affine `m=67` image at endpoint
`201` consumes at physical detail column `200`

\[
 \frac{597}{201\sqrt{134}}\log\frac32
 \tag{L-91549.12}
\]

while the available target is only

\[
 \frac1{\sqrt{200}}\log\frac{201}{200}.
 \tag{L-91549.13}
\]

The first quantity is strictly larger.  Thus the following old implication is
withdrawn:

```text
child detail feasible
 -> affine fixed-67 image detail feasible at the parent.
```

Likewise, positivity and linearity alone do not justify summing arbitrary
affinely lifted finite children and invoking `L-91329`; that theorem requires
an independently proved positive endpoint-measure identity before
quantization.

## 6. Correct fixed-67 replacement

For the deterministic fixed-67 architecture, no dilation is necessary.  The
child and parent rows already live in the same physical row space.
`L-91559` proves the exact nested identity

\[
 d_X=a(Q_X-Q_{X/67})+d_{X/67},
 \tag{L-91549.14}
\]

with coefficientwise nonnegative current row and exact ordinary/radix-four
capacity replacement.  Its score is

\[
 \mathcal S(d_X)
 =a[\mathcal E(X)-\mathcal E(X/67)]
  +\mathcal S(d_{X/67}),
 \tag{L-91549.15}
\]

so the inherited loss again has coefficient one, now without any capacity gap.

## 7. Boundary

```text
matched-fiber affine carry covariance                EXACT
matched-fiber affine detail covariance               EXACT
affine entropy amplification                         EXACT
affine inherited-loss inequality                     EXACT CONDITIONAL
unmatched physical detail feasibility                FALSE / R-91558
fixed-67 affine capacity joint                        WITHDRAWN
fixed-67 identity-embedding capacity joint            EXACT / L-91559
Riemann Hypothesis                                   UNPROVEN
```
