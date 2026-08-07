# R-21903 — Positive-Hankel Selberg adjoints cannot absorb the long screw ramp

Claim ID: `R-21903`  
Title: Every globally positive Hankel adjoint has a half-exponential output envelope, while the constant Weil coordinate remains macroscopic halfway across the support  
Status: **SCOPE CORRECTION / EXACT NO-GO FOR THE PROPOSED `SH(L)` CONSTRUCTION**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Targets: `T-21901` Section 6; the proposed cellwise construction of `SH(L)`  
Dependencies: classical Bernstein--Widder representation for exponentially convex matrix functions; `L-20705`; `L-21905`

## 1. Positive Hankel adjoints

Let

\[
 F:[0,\infty)\longrightarrow \operatorname{Herm}_d
\]

be continuous and suppose its Hankel kernel is positive:

\[
 \sum_{i,j}v_i^*F(x_i+x_j)v_j\ge0
 \tag{R-21903.1}
\]

for every finite family `x_i>=0` and vectors `v_i in C^d`.  Assume also the
weighted integrability needed by the centered Selberg adjoint,

\[
 \int_0^\infty \|F(t)\|e^{t/2}dt<\infty.
 \tag{R-21903.2}
\]

Matrix Bernstein--Widder, obtained by applying the scalar theorem to every
quadratic form and polarizing, gives a positive matrix measure `M` with

\[
 \boxed{
 F(t)=\int_{(1/2,\infty)}e^{-st}\,dM(s).
 }
 \tag{R-21903.3}
\]

The support restriction follows from (R-21903.2).  Moreover

\[
 \int {dM(s)\over s-1/2}<\infty.
 \tag{R-21903.4}
\]

The centered Selberg adjoint is

\[
 (\mathscr L^*F)(y)
 =yF(y)+2\int_0^\infty F(x+y)e^{x/2}dx.
 \tag{R-21903.5}
\]

Substitution of (R-21903.3) gives the exact Loewner integral

\[
 \boxed{
 (\mathscr L^*F)(y)
 =\int_{(1/2,\infty)}
 \left(y+{2\over s-1/2}\right)e^{-sy}\,dM(s).
 }
 \tag{R-21903.6}
\]

In particular `mathscr L^*F(y)>=0`.

## 2. Universal half-exponential envelope

Put `a=s-1/2>0`.  For every `y>=0`,

\[
 \left(y+{2\over a}\right)e^{-(a+1/2)y}
 ={2\over a}e^{-y/2}
  \left(1+{ay\over2}\right)e^{-ay}.
 \tag{R-21903.7}
\]

Since

\[
 \left(1+{x\over2}\right)e^{-x}\le1
 \qquad(x\ge0),
 \tag{R-21903.8}
\]

one obtains the dimension-free Loewner bound

\[
 \boxed{
 0\preceq(\mathscr L^*F)(y)
 \preceq e^{-y/2}(\mathscr L^*F)(0).
 }
 \tag{R-21903.9}
\]

This is not a loose estimate.  It is a structural restriction on the complete
positive-Hankel adjoint cone.

The explicit adjoints of `L-21905` saturate the same spectral geometry: every
positive mixture is built from exponents `s>1/2` and therefore obeys
(R-21903.9).

## 3. Constant-coordinate stop-loss kernel

For the constant D-0001/Fourier coordinate, `L-20705` gives

\[
 K_{e_0}(\omega)=2\omega.
 \]

In the centered prime convention of `T-21901`, the kernel which must be
represented by the positive adjoint is therefore

\[
 \boxed{
 T_L(y)=2\left(1-{y\over L}\right)_+.
 }
 \tag{R-21903.10}
\]

It satisfies

\[
 T_L(0)=2,
 \qquad
 T_L(L/2)=1.
 \tag{R-21903.11}
\]

Suppose a positive-Hankel adjoint and a scalar residual satisfy

\[
 T_L(y)=(\mathscr L^*F)(y)+e_L(y).
 \tag{R-21903.12}
\]

Let

\[
 \delta_L=\max\{|e_L(0)|,|e_L(L/2)|\},
 \qquad r_L=e^{-L/4}.
 \]

Writing `a=(mathscr L^*F)(0)`, equations (R-21903.9)--(R-21903.12) give

\[
 a\le2+\delta_L,
 \qquad
 1-\delta_L\le r_La.
 \]

Consequently

\[
 \boxed{
 \delta_L\ge {1-2e^{-L/4}\over1+e^{-L/4}}.
 }
 \tag{R-21903.13}
\]

In particular,

\[
 \boxed{
 \liminf_{L\to\infty}\delta_L\ge1.
 }
 \tag{R-21903.14}
\]

Thus the residual cannot be `o(1)` in the uniform norm, in any norm dominating
the two displayed evaluations, or in an operator-valued cell ledger which
requires entrywise endpoint and midpoint closure.

## 4. Consequence for `SH(L)`

`T-21901` only asks that the **arithmetic pairing**

\[
 \langle\nu,e_L\rangle
 \]

be `o(1)`; it does not explicitly require `e_L=o(1)` pointwise.  Therefore
(R-21903.13) is not a logical disproof of every conceivable `SH(L)`.

It is, however, a disproof of the proposed construction by positive exponential
adjoints plus a small spline/endpoint residual.  The constant coordinate forces
that residual to retain a macroscopic portion of the full stop-loss ramp.
Proving its centered-prime pairing is `o(1)` is precisely the square-screw or
prime-polygon RH channel, not a finite interpolation remainder.

Equivalently:

```text
positive-Hankel adjoints close the short exponential sector;
the long stop-loss sector remains in e_L;
<nu,e_L>=o(1) is still the full scalar arithmetic theorem.
```

Hence `SH(L)` has not been completed by `L-21905`, and `T-21901` must not be
presented as having only a routine cell-stitching step left.

## 5. Required repair

A noncircular continuation must change the nonlinear equation before applying
Hankel positivity.  The natural operation is a finite difference of the
centered measure, because a squared difference converts the Selberg quadratic
term into a literal square while removing the long polynomial/ramp channel.
That exact equation is recorded separately in `L-21906`.

Any alternative must explicitly provide one of:

1. a conditionally positive Hankel theorem with the exact annihilated moments;
2. a signed Selberg factorization whose negative finite rank is paid by a
   separately proved transport reserve;
3. a direct cofinal proof of the residual pairing, acknowledging that this is
   the scalar RH-bearing statement.

## 6. Status boundary

- The representation and decay inequality are exact classical consequences.
- The constant-coordinate normalization is inherited from `L-20705`.
- This refutation does not reject the source frame, corrected-tail formula,
  ordinary-tail floor, or the implication `SH(L) => RH`.
- It rejects the claim that the positive-Hankel exponential cone itself
  constructs `SH(L)` with a vanishing local residual.
