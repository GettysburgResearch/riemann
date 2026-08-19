# L-99700 — The canonical scalar has a zero-free reciprocal-zeta Mellin consumer

Claim ID: `L-99700`  
Status: **PROVED EXACT ANALYTIC SYNTHESIS**  
Created: 2026-08-20  
Frozen sources: PR #649, PR #652, PR #653  
RH status: **not assumed**

## 1. The factor-67 SHARP defect

Put

\[
T(y)=(4\sqrt y-3)\mathbf 1_{y\ge1},
\]

\[
\beta(n)=\mu(n)-\mathbf 1_{67\mid n}\mu(n/67),
\]

and

\[
h(x)=\sum_{n\le x}\frac{\beta(n)}{\sqrt n}T(x/n).
\tag{L-99700.1}
\]

For `Re z>1`,

\[
\sum_{n\ge1}\frac{\beta(n)}{n^z}
=\frac{1-67^{-z}}{\zeta(z)}.
\tag{L-99700.2}
\]

The elementary target transform is

\[
\int_1^\infty T(y)y^{-s-1}\,dy
=\frac{s+3/2}{s(s-1/2)}.
\tag{L-99700.3}
\]

Consequently, initially for `Re s>1/2`, finite/absolute Fubini gives

\[
\boxed{
\widehat h(s)
:=\int_1^\infty h(x)x^{-s-1}\,dx
=
\frac{(1-67^{-(s+1/2)})(s+3/2)}
{s(s-1/2)\zeta(s+1/2)}.
}
\tag{L-99700.4}
\]

At `s=1/2`, the pole of `1/(s-1/2)` is cancelled by the zero of
`1/zeta(s+1/2)`. At every positive real `s`, the continuation is analytic. If
`rho` is a zeta zero with `Re rho>1/2`, then

\[
|67^{-\rho}|=67^{-\Re\rho}<1,
\]

so `1-67^{-rho}` cannot vanish. Every such zero therefore produces a genuine
pole of (L-99700.4) at `s=rho-1/2` with positive real part.

## 2. The fixed 5:3 scalar cross-check

For the canonical component rows put

\[
W_X=5c_X(2)+3c_X(3).
\]

The unsieved logarithmic coefficients are

\[
15h_X(2)+6h_X(3)+3h_X(4)+6\sum_{m\ge5}h_X(m),
\]

so the unsieved kernel is positive. With `z=s+1/2`, its exact transform is

\[
\boxed{
\int_1^\infty W_X X^{-s-1}\,dX
=
\frac6{s^2}
-
\frac{3(2^{-z}-1)(2^{-z}-2)}{s^2\zeta(z)}.
}
\tag{L-99700.5}
\]

The numerator is zero-free in `0<Re z<1`: `2^{-z}=1` forces `Re z=0`, while
`2^{-z}=2` forces `Re z=-1`. Thus one fixed scalar, rather than a row chosen
after a hypothetical zero, detects every open-strip zero.

## 3. Exact conclusion criteria

Either of the following is sufficient for RH:

1. for one fixed `A>1`,
   \[
   \int_{X/A}^{X}h(t)\frac{dt}{t}\ge0
   \quad\text{eventually};
   \]
2. writing `h=h_+-h_-`,
   \[
   \int_1^X h_-(t)\frac{dt}{t}=O_\varepsilon(X^\varepsilon)
   \quad\text{for every }\varepsilon>0;
   \]
3. `W_X>=0` eventually.

For the first criterion the positive logarithmic box has multiplier

\[
\frac{1-A^{-s}}s,
\]

which is zero-free in `Re s>0`. For the second criterion, the Mellin transform
of `h_-` is holomorphic in `Re s>0`; adding it to (L-99700.4) produces the
transform of the nonnegative density `h_+` without cancelling a pole. For the
third criterion, use (L-99700.5).

In each case the specialized Landau theorem forces the first singularity of a
nonnegative Mellin density to occur on the positive real axis. The displayed
continuations have no such positive-real singularity, while any off-line zeta
zero would give a nonreal pole in `Re s>0`. Functional-equation symmetry then
places every nontrivial zero on `Re z=1/2`.

## 4. Normative scope

The conclusion in this lemma uses no Hall flow, Volterra frame, random-key
child tree, score, radix-four capacity, prime-square moat, large-row
noncancellation, or finite-to-continuum calibration. Those constructions may
serve as arithmetic producers or cross-checks, but they are not antecedents of
the scalar analytic consumer.
