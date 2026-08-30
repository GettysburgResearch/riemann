# T-104590 — Unit-weight Levinson phase and marked-moment fixed-order frontier

Claim ID: `T-104590`  
Status: **UNCONDITIONAL EXACT REDUCTIONS + TWO FIXED-ORDER GATES**  
Created: 2026-08-23  
Depends on: `T-104540`, `L-104542--L-104544`  
RH status: **unproved**

## 1. What is removed

The previous amplitude route proved a weighted majority and then asked for
critical-value regularity. `L-104542` removes the amplitudes exactly.

For

\[
f(t)=\Xi''(t)
\]

and any positive parameter `lambda`, define

\[
E_\lambda(t)=\Xi''(t)-i\lambda\Xi'''(t).
\]

On every regular interval,

\[
\boxed{
G-W
=
\frac{1}{\pi}\Delta\arg E_\lambda+O(1),
}
\tag{T-104590.1}
\]

where `G-W` is the good-minus-wrong count among the real `Xi'''` zeros. The
error is bounded independently of `lambda` and the number of zeros.

Thus `lambda` may be chosen at the natural mollifier scale

\[
\lambda_T=\frac{a}{\log T}
\tag{T-104590.2}
\]

without changing the asymptotic count.

In the `s`-plane,

\[
E_{\lambda_T}(t)
=
-\left[
\xi''(s)+\lambda_T\xi'''(s)
\right],
\qquad
s=\frac12+it.
\tag{T-104590.3}
\]

## 2. Route A — one Levinson phase

Define

```text
UPHASE104590 — unit-weight phase drift

For some fixed a>0 and eta>0, prove on Conrey's regular height sequence

  Delta arg [xi'' + (a/log T) xi''']
  >= eta pi R_3(T) + o(R_3(T)),

where the argument is the continuous critical-line branch and R_3(T) is the
number of certified real xi''' zeros.
```

Then (T-104590.1) gives

\[
\boxed{
\mathrm{UPHASE104590}
\Longrightarrow
\alpha_2\ge\eta\alpha_3
>
0.9873\,\eta.
}
\tag{T-104590.4}
\]

This is a single classical Levinson argument coordinate. It is not a
critical-value amplitude condition.

## 3. Route B — marked two moments

For a source-visible positive normalizer `w_T`, define the exact weighted bias

\[
D_T
=
\sum_{\Xi'''(c)=0}
\varepsilon_c w_T(c)|\Xi''(c)|
\]

and marked second moment

\[
B_T
=
\sum_{\Xi'''(c)=0}
w_T(c)^2\Xi''(c)^2.
\]

`L-104543` proves

\[
\frac{G-W}{R_3(T)}
\ge
2\frac{(D_T)_+^2}{R_3(T)B_T}-1.
\tag{T-104590.5}
\]

`L-104544` writes `B_T` as one exact thin-strip contour.

Define

```text
CM2X104590 — critical marked two-moment estimate

For some eta>0, prove

  (D_T)_+^2 / [R_3(T) B_T] >= (1+eta)/2 + o(1)

with one fixed source-visible normalizer.
```

Then

\[
\boxed{
\mathrm{CM2X104590}
\Longrightarrow
\alpha_2\ge\eta\alpha_3
>
0.9873\,\eta.
}
\tag{T-104590.6}
\]

## 4. Relation between the routes

The routes are complementary:

```text
UPHASE104590
  counts orientations exactly through one bounded phase observable;

CM2X104590
  proves a positive orientation density from one signed first moment and one
  analytic marked second moment.
```

Neither route uses Conrey's independent `alpha_2>0.9584` row.

The phase route is the closest rigorous formulation of Levinson's original
intuition. The marked-moment route is the closest to existing discrete moment
technology.

## 5. Exact boundary

```text
unit-amplitude reverse-Rolle identity      PROVED EXACT
lambda-uniform phase law                   PROVED EXACT
weighted two-moment count bound            PROVED EXACT
marked critical contour                    PROVED EXACT

UPHASE104590                               OPEN
CM2X104590                                 OPEN
alpha_2 from alpha_3                       NOT YET ESTABLISHED
Riemann Hypothesis                         UNPROVED
```
