# L-91559 — Nested component packets have an exact identity embedding in every radix-four detail column

Claim ID: `L-91559`  
Status: **PROVED EXACT PHYSICAL-CAPACITY REPLACEMENT THEOREM — LIVE ENTRY NORMALIZATION STILL REQUIRES REPLAY**  
Created: 2026-08-13  
Depends on: `L-24501`, retained `L-91112.25`, `L-91341`, `L-91545`, `L-91547`, `L-91553/L-91556`  
Supersedes for the fixed-67 reset: the capacity use of `L-91318/L-91549` refuted by `R-91558`  
RH status: **unproved**

## 1. The positive component row and its exact physical target

For real `Y>=1`, put

\[
 h_Y(m)=m^{-1/2}\log(Y/m)\mathbf1_{m\le Y},
 \qquad
 S_Y(n)=\sum_{m\ge n}h_Y(m),
 \tag{L-91559.1}
\]

and retain the exact positive component row

\[
 \boxed{
 Q_Y(n)
 =(n+1)\Delta^2\left[\frac{S_Y(n)}{n-1}\right]
 \ge0.
 }
 \tag{L-91559.2}
\]

Define the finite dilation ramp

\[
 \boxed{
 H(Z)=\sum_{k\le Z}k^{-1/2}\log(Z/k),
 }
 \tag{L-91559.3}
\]

with causal value zero for `Z<1`.

Apply the exact double-summation identity `L-24501` to the seed coordinate
`b(m)=S_Y(m)`.  Since

\[
 S_Y(kq)-S_Y(kq+1)=h_Y(kq),
\]

the ordinary carry response of the component row is

\[
\boxed{
 \begin{aligned}
 C_Y(q)
 &:=\sum_{n\ge2}Q_Y(n)\beta_{nq}\\
 &=\sum_{kq\le Y}h_Y(kq)\\
 &=\frac1{\sqrt q}H(Y/q).
 \end{aligned}
}
 \tag{L-91559.4}
\]

This is an exact finite identity for every integer `q>=2`.

Its radix-four detail response is therefore

\[
 \boxed{
 \Theta_Y(q)
 :=C_Y(q)-2C_Y(4q)
 =\frac1{\sqrt q}
  \left[H(Y/q)-H(Y/(4q))\right].
 }
 \tag{L-91559.5}

Thus a positive component row carries its own explicit physical
ordinary/detail capacity vector; no endpoint-density surrogate is needed.

## 2. Positivity and endpoint monotonicity of the detail target

The function `H` is continuous at every integer activation, because the
entering summand has value `log 1=0`.  Away from activation knots,

\[
 H'(Z)=\frac1Z\sum_{k\le Z}k^{-1/2}.
 \tag{L-91559.6}
\]

Put

\[
 D(Z)=H(Z)-H(Z/4).
 \tag{L-91559.7}
\]

On every smooth cell,

\[
\boxed{
 D'(Z)
 =\frac1Z
  \sum_{Z/4<k\le Z}k^{-1/2}
 \ge0.
}
 \tag{L-91559.8}
\]

Continuity at all knots gives the global statements

\[
 \boxed{
 \Theta_Y(q)\ge0,
 }
 \tag{L-91559.9}
\]

and

\[
 \boxed{
 1\le Y_1\le Y_2
 \Longrightarrow
 \Theta_{Y_1}(q)\le\Theta_{Y_2}(q)
 \quad(q\ge2).
 }
 \tag{L-91559.10}
\]

The ordinary target `C_Y(q)` is likewise nondecreasing in `Y`.

Separately, `L-91341` gives componentwise row monotonicity

\[
 \boxed{
 Q_{Y_2}(n)-Q_{Y_1}(n)\ge0
 \qquad(Y_2\ge Y_1).
 }
 \tag{L-91559.11}
\]

## 3. Exact nested replacement

Fix `1<=Y<=X` and `a>=0`.  Let `d_Y(n)>=0` be any finite child packing satisfying

\[
 \boxed{
 \sum_nd_Y(n)
 [\beta_{nq}-2\beta_{n,4q}]
 \le a\Theta_Y(q)
 \qquad(q\ge2).
 }
 \tag{L-91559.12}
\]

Embed it into the parent row space by the **identity map**:

\[
 \iota_{Y\to X}d_Y=d_Y.
 \tag{L-91559.13}
\]

No row index and no coefficient is changed.  Define

\[
 \boxed{
 d_X
 =a(Q_X-Q_Y)+d_Y.
 }
 \tag{L-91559.14}
\]

Equation (L-91559.11) gives `d_X>=0`.  Its detail response is

\[
\begin{aligned}
 \mathcal D_4C_{d_X}(q)
 &=a[\Theta_X(q)-\Theta_Y(q)]
   +\mathcal D_4C_{d_Y}(q)\\
 &\le a\Theta_X(q).
\end{aligned}
 \tag{L-91559.15}

Hence

\[
 \boxed{
 d_Y\text{ feasible for }a\Theta_Y
 \Longrightarrow
 a(Q_X-Q_Y)+d_Y
 \text{ feasible for }a\Theta_X.
 }
 \tag{L-91559.16}
\]

The same proof with `C_Y` gives ordinary-column feasibility.  The entropy score
is exact and coefficient one:

\[
 \boxed{
 \mathcal S(d_X)
 =a[\mathcal E(X)-\mathcal E(Y)]
  +\mathcal S(d_Y),
 }
 \tag{L-91559.17}
\]

where `mathcal E(Y)=sum_n Q_Y(n)G_n`.

There is no factor `67^(1/2)`, no matched/unmatched fiber, no positive leakage,
and no fractional physical column.

## 4. Positive source-measure version

Let `nu` be a positive finite source measure and let `kappa(n)>=0`.  At parent
endpoint `X`, source node `n` has quotient

\[
 Y_n=X/n.
 \tag{L-91559.18}
\]

For a fixed contraction `m>=1`, its child quotient is `Y_n/m`.  Define the
canonical parent and child rows

\[
 R_X^\nu
 =\sum_n\nu(n)\kappa(n)n^{-1/2}Q_{Y_n},
 \tag{L-91559.19}
\]

\[
 R_{X/m}^\nu
 =\sum_{n\le X/m}
  \nu(n)\kappa(n)n^{-1/2}Q_{Y_n/m}.
 \tag{L-91559.20}
\]

By (L-91559.11),

\[
 \boxed{
 R_X^\nu-R_{X/m}^\nu\ge0.
 }
 \tag{L-91559.21}
\]

Let the packet detail capacities be the corresponding positive sums of
`Theta`.  If `d_child` is any feasible packing for the canonical child packet,
then

\[
 \boxed{
 d_parent
 =R_X^\nu-R_{X/m}^\nu+d_child
 }
 \tag{L-91559.22}
\]

is nonnegative and feasible for the canonical parent packet.  This follows by
summing (L-91559.15) with positive coefficients.

The statement is stable under finite or countable positive direct sums by
monotone convergence whenever the parent capacity is finite.

## 5. Application to the post-Hall fixed-67 reset

Use the row-budgeted binary normalization of `L-91556`.  After target Hall,
`L-91545` gives positive residual sources `c_s,c_h` and positive row bonuses
`B_s,B_h` satisfying the exact native parent-row identity

\[
 \boxed{
 R_{\rm native,X}
 =R_{s,X}(c_s)+R_{h,X}(c_h)+B_s+B_h.
 }
 \tag{L-91559.23}
\]

The branch row coefficients are

\[
 \kappa_s=1-r^2,
 \qquad
 \kappa_h=r^2,
 \qquad
 \kappa_s+\kappa_h=1.
 \tag{L-91559.24}
\]

Apply Section 4 with `m=67` separately to `c_s,c_h`.  Let

\[
 R_{\rm can,child}
 =R_{s,X/67}(c_s|_{n\le X/67})
  +R_{h,X/67}(c_h|_{n\le X/67}).
 \tag{L-91559.25}
\]

Then the current row

\[
 \boxed{
 R_{\rm cur}
 =R_{\rm native,X}-R_{\rm can,child}
 }
 \tag{L-91559.26}
\]

is coefficientwise nonnegative: it is the sum of both positive component-row
differences, both positive activation frontiers, and `B_s+B_h`.

The exact finite equality row has ordinary response `w_X` and detail response
`Omega_X`.  Equation (L-91559.23) is an equality of the literal row vector, so
its response is unchanged by Hall.  If `d_s,d_h` are arbitrary feasible rows
for the two canonical child packet capacities at endpoint `X/67`, then

\[
 \boxed{
 d_X=R_{\rm cur}+d_s+d_h
 }
 \tag{L-91559.27
}

is nonnegative and satisfies

\[
 \boxed{
 \mathcal D_4C_{d_X}(q)\le\Omega_X(q)
 \qquad(q\ge2).
 }
 \tag{L-91559.28}
\]

Indeed, the native baseline response is exactly `Omega_X`; subtracting the
canonical child rows subtracts their exact positive packet capacities, and the
replacement rows consume no more than those same capacities.

This is the required capacity-faithful lift of arbitrary child packings.  It is
an identity embedding, not an affine Pascal dilation.

## 6. Consequences for the proof DAG

For the fixed-67 architecture, the following former obligations disappear:

```text
colored child columns;
positive projection from colors to physical columns;
matched versus unmatched affine fibers;
endpoint-measure identity L-91329.11 for recursive children;
sum-before-quantize treatment of child packings;
branchwise affine normalization in the loss recurrence.
```

The finite equality row, the Hall decomposition, and every replacement all live
in one common physical row space from the start.  Radix-four feasibility is
proved directly by the exact positive packet capacities `Theta_Y`.

The continuum B-spline producer and its finite mismatch/collar remain useful as
an independent construction and audit route, but they are not needed to lift a
fixed-67 recursive child.

## 7. Firewalls

This theorem does not rehabilitate the affine lift refuted by `R-91558`.  It also
does not prove the imported one-prime Hall theorem or the exact row-budgeted
entry; those are frozen inputs which must be replayed on the moving live parent.

The packet capacity in Sections 3--5 is the **literal carry/detail response of
the canonical component row**.  Replacing it by the scalar Hall target or by an
unrelated endpoint-density target is forbidden.

```text
component-row ordinary response                     EXACT
component-row radix-four target Theta_Y              EXACT / POSITIVE
Theta_Y monotone in endpoint                         EXACT
nested identity embedding                            EXACT
arbitrary canonical-child packing replacement        EXACT
fixed-67 physical detail assembly                    CLOSED ON FROZEN ENTRY
fixed-67 affine lift                                  NOT USED / REFUTED
live one-prime entry normalization                    REPLAY REQUIRED
Riemann Hypothesis                                   UNPROVEN
```
