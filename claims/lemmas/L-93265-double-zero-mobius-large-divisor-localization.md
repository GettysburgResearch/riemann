# L-93265 — The double Mellin zero closes every small Mobius divisor and leaves one large-divisor tail

Claim ID: `L-93265`  
Status: **PROPOSED COMPLETE UNCONDITIONAL HYPERBOLA LOCALIZATION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-93261`; the elementary identity `Lambda=mu*log`  
Scope: the ordinary-prime-power part of the cubic Q4 scalar; no bound for the remaining large-divisor Mobius tail

## 1. Elementary forcing

Define for real `Y>=1`

\[
\boxed{
F_W(Y)=\sum_{m\le Y}(\log m)W(m/Y).
}
\tag{L-93265.1}
\]

Because `log 1=0`, one has `F_W(Y)=0` for `1<=Y<2`.

Let

\[
\mathcal L_W(X)=\sum_{n\le X}\Lambda(n)W(n/X).
\tag{L-93265.2}
\]

Using `Lambda=mu*log` and reversing a finite product sum gives the exact
hyperbola identity

\[
\boxed{
\mathcal L_W(X)
=
\sum_{d\le X}\mu(d)F_W(X/d).
}
\tag{L-93265.3}
\]

## 2. Double-zero forcing estimate

The explicit value

\[
\boxed{C_W=512}
\tag{L-93265.4a}
\]

is valid for every real `Y>=2`; in particular,

\[
\boxed{
|F_W(Y)|
\le 512{1+\log Y\over Y}.
}
\tag{L-93265.4}
\]

### Proof

Put

\[
f_Y(t)=(\log t)W(t/Y),
\]

extend it by zero outside `[1,Y]`, and interpret its second derivative as a
finite signed measure at the endpoints and at the one interior knot `Y/4`.
The second-order Euler formula with the periodic Bernoulli polynomial gives

\[
\left|
\sum_{m\in\mathbb Z}f_Y(m)-\int_\mathbb Rf_Y(t)dt
\right|
\le {1\over12}\operatorname{Var}(f_Y').
\tag{L-93265.4b}
\]

For `Y>=4`, write the two polynomial pieces as

\[
P_1(u)=5u-63u^2+170u^3,
\qquad
P_2(u)={-u+3u^2-2u^3\over3}.
\]

On a piece with `f_Y(t)=log(t)P(t/Y)`, one has

\[
f_Y''(t)
={1\over Y^2}
\left[
-{P(u)\over u^2}
+{2P'(u)\over u}
+\log(Yu)P''(u)
\right],
\qquad u=t/Y.
\tag{L-93265.4c}
\]

The nonlogarithmic brackets reduce exactly to

\[
{5\over u}-189+850u
\quad(0<u<1/4),
\]

and

\[
-{1\over3u}+3-{10\over3}u
\quad(1/4<u<1).
\]

Using `|P_1''|<=129`, `|P_2''|<=2`, direct integration gives the safe bound

\[
\int_1^Y|f_Y''(t)|dt
\le {39\log Y+79\over Y}.
\tag{L-93265.4d}
\]

The endpoint and knot contributions satisfy

\[
|f_Y'(1+)|\le {32\over Y},
\qquad
|f_Y'(Y-)|={\log Y\over3Y},
\]

and, because `P_2'(1/4)-P_1'(1/4)=-16/3`,

\[
|f_Y'(Y/4+)-f_Y'(Y/4-)|
\le {16\log Y\over3Y}.
\tag{L-93265.4e}
\]

Thus the Euler remainder in (L-93265.4b) is at most

\[
{14(1+\log Y)\over Y}.
\tag{L-93265.4f}
\]

The two exact moment identities of `L-93261` give, after `t=Yu`,

\[
\begin{aligned}
\int_1^Yf_Y(t)dt
&=-Y\int_0^{1/Y}W(u)\log(Yu)du.
\end{aligned}
\]

Since `|W(u)|<=32u`,

\[
\left|\int_1^Yf_Y(t)dt\right|
\le {32\over Y}\int_0^1v|\log v|dv
={8\over Y}.
\tag{L-93265.4g}
\]

This proves a constant far below `512` for `Y>=4`.  On `2<=Y<=4`, the crude
finite bound `|W|<=32x` is absorbed by (L-93265.4a).  No prime number theorem,
Mertens estimate, zero-free region, or RH-strength input is used.

## 3. Small divisors are harmless

Split (L-93265.3) at `d=sqrt(X)`. By (L-93265.4),

\[
\begin{aligned}
\sum_{d\le\sqrt X}|F_W(X/d)|
&\ll {1\over X}
\sum_{d\le\sqrt X}d(1+\log(X/d))\\
&\ll 1+\log X.
\end{aligned}
\tag{L-93265.5}
\]

Therefore

\[
\boxed{
\mathcal L_W(X)
=
\sum_{\sqrt X<d\le X/2}
\mu(d)F_W(X/d)
+O(1+\log X).
}
\tag{L-93265.6}
\]

The upper limit `X/2` is exact because `F_W(Y)=0` below two.

Restoring the explicit Q4 four-adic gauge changes the right side by only
`O(log X)`. Thus the complete cubic scalar is reduced to one large-divisor
Mobius tail plus a logarithmic ledger.

## 4. Exact balanced bilinear form

Reversing the order of the surviving finite tail in (L-93265.6) gives

\[
\boxed{
\sum_{\sqrt X<d\le X/2}\mu(d)F_W(X/d)
=
\sum_{2\le m<\sqrt X}(\log m)
\sum_{\sqrt X<d\le X/m}
\mu(d)W(md/X).
}
\tag{L-93265.7}
\]

This is a literal balanced hyperbola form:

```text
short variable:  2 <= m < sqrt(X);
long variable:   sqrt(X) < d <= X/m;
coefficient:     mu(d) log(m) W(md/X).
```

It is the natural entry point for a genuine bilinear-dispersion argument.  It
also exposes a firewall.  The kernel depends only on the product `md`; a
source-blind Cauchy inequality or generic large-sieve statement with no
additional phase simply recombines the convolution `mu*log=Lambda` and does not
supply square-root cancellation.  Any successful dispersion estimate must use
specific Möbius correlation, endpoint variation, or an added arithmetic phase.
No such estimate is imported here.

## 5. Why this is not CPBD renamed

The surviving object has no prime-block Gram, no common-half-plane count, and
no same-prime tower bookkeeping. It is the single signed transform

\[
\sum_{\sqrt X<d\le X/2}\mu(d)F_W(X/d)
\]

of an **elementary, explicitly decaying forcing**. Every small Mobius divisor,
every prime power correction, and the four-adic gauge has already been paid.

The unresolved estimate is cancellation among large Mobius divisors. Replacing
that cancellation by absolute values loses a full factor `sqrt(X)` and is not a
valid proof.

## 6. Design tradeoff

For the one-switch Abel kernel `J`, the logarithmic moment is nonzero, and the
analogous forcing has a linear main term rather than (L-93265.4). Thus:

```text
two-switch W:  double zero, bottom-free forcing, large-divisor tail;
one-switch J:  simpler sign geometry, but macroscopic forcing.
```

This is the exact scalar tradeoff isolated by the packet.

## 7. Boundary

```text
Lambda=mu*log hyperbola identity          EXACT
forcing O(log Y / Y)                      UNCONDITIONAL
small-divisor contribution                O(log X)
large-divisor Mobius tail                  OPEN / RH-BEARING
absolute-value closure                     INVALID
RH                                         UNPROVED
```
