# L-104538 — Stationary horizontal minima transfer the fixed-order line proportion

Claim ID: `L-104538`  
Status: **PROVED EXACT IMPLICATION**  
Created: 2026-08-23  
Depends on: `L-104527`, `L-104537`  
RH status: **not assumed**

Let `R_3(T)` be the number of simple real zeros of `Xi'''` in `(-T,T)` in the
same short-window normalization used for the fixed-order Conrey proportion.
At such a zero `c`, assume `Xi''(c) != 0` and define the stationary horizontal
defect

\[
\delta_h(c)
={1\over h^2}
\log { |\Xi''(c-ih)|^2\over |\Xi''(c)|^2 }.
\tag{L-104538.1}
\]

By `L-104537`,

\[
\delta_h(c)
\longrightarrow
{\mathcal L_2(c)\over \Xi''(c)^2}
\qquad(h\to0),
\tag{L-104538.2}
\]

where

\[
\mathcal L_2(c)
=-\Xi''(c)\Xi''''(c).
\]

Thus the following are equivalent at every regular critical point:

```text
c is Rolle-generating for Xi'';
Xi''(c) Xi''''(c) < 0;
L_2(c) > 0;
h=0 is a strict horizontal minimum of |Xi''(c-ih)|;
delta_h(c) > 0 for all sufficiently small nonzero h.
```

## 1. Density form

Let `Q_H(T)` count the real zeros `c` of `Xi'''` for which `h=0` is a
nonnegative local horizontal minimum, equivalently `L_2(c)>=0`.  Suppose

\[
\liminf_{T\to\infty}{Q_H(T)\over R_3(T)}\ge q.
\tag{L-104538.3}
\]

The exact factor-two reverse-Rolle count gives

\[
\boxed{
\alpha_2\ge (2q-1)\alpha_3.
}
\tag{L-104538.4}
\]

In particular, with Conrey's unconditional input `alpha_3>0.9873`,

\[
\boxed{
q>{1\over2}
\quad\Longrightarrow\quad
\alpha_2>(2q-1)\,0.9873.
}
\tag{L-104538.5}
\]

Examples:

```text
q >= 3/4    -> alpha_2 > 0.49365;
q >= 9/10   -> alpha_2 > 0.78984;
q = 1       -> alpha_2 >= alpha_3 > 0.9873.
```

The `alpha_3` premise is load bearing.  No independent lower bound for
`alpha_2` is used in (L-104538.4--5).

## 2. Finite-shift form

For `h>0`, let `Q_h(T)` count the regular real zeros `c` of `Xi'''` satisfying

\[
|\Xi''(c-ih)|\ge |\Xi''(c)|.
\tag{L-104538.6}
\]

If there is a sequence `h_j downarrow 0` for which

\[
\liminf_j\liminf_{T\to\infty}{Q_{h_j}(T)\over R_3(T)}\ge q
\tag{L-104538.7}
\]

and the density of horizontally degenerate critical points

\[
\mathcal L_2(c)=0
\]

is zero, then (L-104538.3) follows and hence so does (L-104538.4).

This gives a conclusion-facing theorem involving actual horizontal shifts of
`xi''`, rather than a formal derivative sign.  Such shifts are accessible to
Levinson--Conrey mollified mean-value methods.

## 3. Correct target

The strongest global theorem `LAG2XI104550` asks for horizontal minima at every
real ordinate.  The fixed-order descent only requires the weaker statement

```text
SHMIN104580:
  more than half of Conrey's real Xi''' zeros are stationary horizontal minima
  of |Xi''(t-ih)| at h=0.
```

Any quantitative improvement beyond one half immediately produces a positive
unconditional `Xi''` line proportion from the `Xi'''` theorem alone.
