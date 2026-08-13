# R-91558 — The affine fixed-67 lift overdraws an unmatched physical detail column

Claim ID: `R-91558`  
Status: **EXACT REFUTATION OF THE CAPACITY CLAIM IN `L-91549`; SCORE-AMPLIFICATION PART RETAINED**  
Created: 2026-08-13  
Targets: `L-91318`, `L-91324`, `L-91547`, `L-91549`, `L-91329.11`  
RH status: **unproved**

## 1. The claim under audit

For an integer dilation `m`, the affine Pascal map is

\[
 \Phi_m(n)=m(n+1)-1
 \tag{R-91558.1}
\]

and the proposed lifted child row is

\[
 D(\Phi_m(n))=m^{-1/2}d(n).
 \tag{R-91558.2}
\]

`L-91318` correctly proves exact carry and radix-four covariance on the matched
fiber `Q=mq`.  It also explicitly leaves positive projection to uncolored
physical columns open.  `L-91549.5` later treats the same lift as
capacity-faithful after sum-before-quantize assembly.  That stronger statement
is false for arbitrary feasible finite child rows, and it is already false for
a canonical positive component packet.

## 2. A canonical child at endpoint three

Take the child endpoint

\[
 Y=3
 \tag{R-91558.3}
\]

and the nonnegative row supported at `n=2` with coefficient

\[
 \boxed{
 d(2)=\frac{3}{\sqrt2}\log\frac32.
 }
 \tag{R-91558.4}
\]

This is exactly the positive component row `Q_3`:

\[
 Q_3(2)=\frac{3}{\sqrt2}\log\frac32,
 \qquad
 Q_3(n)=0\quad(n\ne2).
 \tag{R-91558.5}
\]

The averaged carry kernel satisfies

\[
 \beta_{2,2}=\frac13,
 \qquad
 \beta_{2,8}=0.
 \tag{R-91558.6}
\]

Hence the radix-four response at `q=2` is

\[
 d(2)[\beta_{2,2}-2\beta_{2,8}]
 =\frac1{\sqrt2}\log\frac32
 =\Omega_3(2).
 \tag{R-91558.7}
\]

For every `q>=3`, both carry terms vanish.  Thus `d` is a nonnegative
radix-four detail-feasible child packing, saturating its sole nonzero detail
column.

## 3. The fixed-67 affine lift

Set

\[
 m=67,
 \qquad
 X=mY=201.
 \tag{R-91558.8}
\]

The affine image of the only child row is

\[
 \Phi_{67}(2)=67\cdot3-1=200,
 \tag{R-91558.9}
\]

so

\[
 D(200)=\frac{3}{\sqrt{134}}\log\frac32.
 \tag{R-91558.10}
\]

Evaluate the parent detail column at the unmatched physical integer

\[
 Q=200,
 \qquad67\nmid200.
 \tag{R-91558.11}
\]

One has

\[
 \beta_{200,200}=rac{199}{201},
 \qquad
 \beta_{200,800}=0.
 \tag{R-91558.12}
\]

Therefore the lifted row consumes

\[
 \boxed{
 \mathcal D_4C_D(200)
 =\frac{597}{201\sqrt{134}}\log\frac32.
 }
 \tag{R-91558.13}
\]

At endpoint `X=201`, the physical target at this terminal column is

\[
 \boxed{
 \Omega_{201}(200)
 =\frac1{\sqrt{200}}\log\frac{201}{200}.
 }
 \tag{R-91558.14}
\]

## 4. Exact strict overdraw

The elementary inequalities

\[
 \log(1+x)>\frac{2x}{2+x}\quad(x>0),
 \qquad
 \log(1+x)<x\quad(x>0)
 \tag{R-91558.15}
\]

give

\[
 \log\frac32>\frac25,
 \qquad
 \log\frac{201}{200}<\frac1{200}.
 \tag{R-91558.16}
\]

Also

\[
 \sqrt{134}<12,
 \qquad
 \sqrt{200}>14.
 \tag{R-91558.17}
\]

Consequently

\[
 \mathcal D_4C_D(200)
 >\frac{597}{201\cdot12}\frac25
 =\frac{199}{2010},
 \tag{R-91558.18}
\]

whereas

\[
 \Omega_{201}(200)
 <\frac1{200\cdot14}
 =\frac1{2800}.
 \tag{R-91558.19}
\]

Since

\[
 \frac{199}{2010}>\frac1{2800},
 \tag{R-91558.20}
\]

one obtains the exact separation

\[
 \boxed{
 \mathcal D_4C_D(200)>\Omega_{201}(200).
 }
 \tag{R-91558.21}
\]

The overdraw factor is greater than `277`; numerically it is about `295`, but
no decimal estimate is used in the proof.

## 5. What survives

The following statements of `L-91318/L-91549` remain valid:

```text
matched-fiber carry covariance at Q=mq;
matched-fiber radix-four covariance;
nonnegativity of the lifted row;
entropy amplification G_(m(n+1)-1)>=mG_n;
score-loss nonexpansion once a capacity-faithful lift is separately supplied.
```

The following inference is refuted:

```text
arbitrary child detail feasibility
 + affine Pascal lift
 -> parent physical detail feasibility.
```

Positive off-fiber ordinary carry is not harmless for an upper-capacity
problem, and the radix-four operator is not positive.  Sum-before-quantize does
not repair the counterexample unless one first proves the exact endpoint-measure
identity `L-91329.11` in a corridor for which the single global finite correction
applies.  `L-91547` supplies a source-kernel split, not that endpoint-measure
identity.

## 6. Correct pivot

The deterministic fixed-67 architecture has a simpler repair: do **not** dilate
the child row.  A packing at endpoint `X/67` is already a finite row in the same
physical row space as endpoint `X`.  Direct identity embedding preserves all
carry responses, while both the ordinary target `w_X(q)` and the positive
component-detail target are monotone in the endpoint.

This repair is proved in `L-91559`.

```text
canonical child Q_3 detail feasible                  EXACT
fixed-67 affine image row                            EXACT
unmatched parent detail overdraw                     EXACT
L-91549 capacity-faithful affine claim               FALSE
matched-fiber and entropy statements                 RETAINED
identity-embedding repair                            L-91559
Riemann Hypothesis                                   UNPROVEN
```
