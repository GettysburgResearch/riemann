# L-93901 — The live Volterra Möbius bulk has an exact two-channel positive coupling in every typed coordinate

Claim ID: `L-93901`  
Status: **PROVED EXACT SOURCE-MARGINAL COMPILER ON THE FROZEN VOLTERRA IDENTITY**  
Created: 2026-08-16  
Inputs: `L-91760`, `L-91870`, `L-93900`; factor-67 bounds for `L(x)` and `R(x)`  
RH status: **unproved**

Fix one retained endpoint `s` and put `x=X/s`, so `1<x<67`.  Every active
Möbius colour has `k<67`.

## 1. Two paired occurrence measures

Split every signed Möbius occurrence into the exact channels of `L-93900`:

\[
d\Sigma_{E}^{\pm}(s,k)
=\frac2s\mathbf1_{\mu(k)=\pm1}E_x(k)\,ds,
\]

\[
d\Sigma_{R}^{\pm}(s,k)
=\frac2s\mathbf1_{\mu(k)=\pm1}R_x(k)\,ds.
\]

The equality occurrence multiplies the common positive infinitesimal row
`p_s`; the reserve occurrence has zero component row.

## 2. Exact complete-graph couplings

For `A in {E,R}`, write

\[
P_A=\sum_{\mu(e)=1}A_x(e),
\qquad
N_A=\sum_{\mu(o)=-1}A_x(o).
\]

The factor-67 directed theorem gives

\[
P_E-N_E=L(x)>0,
\qquad
P_R-N_R=R(x)>0.
\]

Define, separately in each channel,

\[
t_A(o,e)=\frac{A_x(o)A_x(e)}{P_A}.
\]

Every negative occurrence is exhausted exactly, every positive occurrence is
matched plus a nonnegative residual, and all edge contributions cancel because
all colours in a fixed channel have the same typed feature.

There is no target-null Hall row bonus and no negative edge-score problem.

## 3. Exact residual fibre

The residual equality and reserve masses are `L(x)` and `R(x)`.  Therefore the
complete typed bulk fibre is

\[
\boxed{
\mathfrak B_x
=L(x)(1,2,p_s)
\oplus R(x)(2,1,0).
}
\tag{L-93901.1}
\]

Its marginals are

\[
\boxed{T(\mathfrak B_x)=L(x)+2R(x),}
\tag{L-93901.2}
\]

\[
\boxed{S(\mathfrak B_x)=2L(x)+R(x),}
\tag{L-93901.3}
\]

\[
\boxed{Q(\mathfrak B_x)=L(x)p_s.}
\tag{L-93901.4}
\]

Equation (L-93901.4) is the exact Volterra native component row.  Applying the
ordinary maps at `q` and `4q` separately and only then subtracting gives the
same identity in radix-four detail.

## 4. Measurability and ownership

On every quotient cell the active colour set is finite and all weights are
continuous algebraic functions of `sqrt(x)`.  The edge and residual kernels are
therefore Borel.  Each source occurrence is split exactly once in its own
channel and keeps the immutable label

```text
(endpoint cell, k, Möbius sign, equality/reserve channel, edge/residual owner).
```

The live generator `X-93900` enumerates the exact fibres `x=2,13,66`; the
`x=2` record also authenticates the single-channel separator of `R-93900`.

```text
actual Möbius occurrences                 explicit
negative channel marginals                exhausted exactly
positive channel marginals                matched plus residual
SHARP target and score                     exact
every component row and q/4q               exact
score obstruction of PR #501               bypassed structurally
Riemann Hypothesis                         unproved
```
