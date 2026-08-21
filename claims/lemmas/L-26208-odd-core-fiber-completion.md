# L-26208 — Odd-core completion makes every Euler fiber half-pole-null

Claim ID: `L-26208`  
Status: `PROPOSED COMPLETE — exact finite source grouping and jet algebra pending independent review`  
Scope: bridge from the Euler fiber to PR #272's boundary-jet programme  
Date: 2026-08-08  
Depends on: `L-26202`; PR #272 `L-26201/L-26203`

Let

\[
p(z)=(1-z)(1-2z)(1-\sqrt2 z)^2
=\sum_{\nu=0}^4p_\nu z^\nu.
\tag{L-26208.1}
\]

For an odd squarefree integer `m`, define the complete normalized atomic fiber

\[
\boxed{
\nu_m
=\frac{\mu(m)}{\sqrt m}
 \sum_{\nu=0}^4
 p_\nu 2^{-\nu/2}
 \delta_{\log m+\nu\log2}.
}
\tag{L-26208.2}
\]

This is exactly the restriction of the coefficient source `b_E(n)/sqrt(n)` to one odd core.

## 1. Exact half-pole nullity

For the half-pole jet

\[
A(\nu)=\int e^{x/2}d\nu(x),
\]

one has

\[
\begin{aligned}
A(\nu_m)
&=\mu(m)
 \sum_{\nu=0}^4p_\nu\\
&=\mu(m)p(1)=0.
\end{aligned}
\tag{L-26208.3}
\]

Hence every complete odd-core fiber lies in the exact half-pole-null cone of PR #272 `L-26201`.

For every derivative order `r`, its Green derivative form is therefore the rank-one positive Gram

\[
\boxed{
Q_r(\nu_m,\nu_{m'})
=8C(\nu_m)\overline{C(\nu_{m'})},
}
\tag{L-26208.4}
\]

where

\[
C(\nu)=\int e^x d\nu(x).
\]

The logarithmic jet is not required to vanish: the exact negative matrix of PR #272 is killed once `A=0`.

## 2. Finite odd-core oversupport completion

For a real endpoint `Y>=1`, define

\[
\boxed{
\widetilde\beta_Y
=\sum_{\substack{m\le Y\\m\ {\rm odd}}}\nu_m.
}
\tag{L-26208.5}
\]

Its support lies in

\[
[0,\log(16Y)].
\]

For every integer `n<=Y`, write `n=2^\nu m` with `m` odd. Then `m<=Y`, and the coefficient of `delta_(log n)` in (L-26208.5) is exactly

\[
\boxed{
\frac{b_{\mathcal E}(n)}{\sqrt n}.
}
\tag{L-26208.6}
\]

Thus the source inside the physical endpoint is unchanged. The additional atoms form one explicit four-layer collar in `(Y,16Y]`.

Unlike truncation by `n<=Y` followed by filtering, the source (L-26208.5) is a direct sum of complete half-pole-null columns. Therefore its complete derivative-Hankel matrix is positive semidefinite before any quotient-cell norm is taken.

## 3. Exact collar firewall

The collar is not discarded. Its half-pole jet is the negative of the inner source jet:

\[
A(\widetilde\beta_Y^{\rm collar})
=-\sum_{n\le Y}b_{\mathcal E}(n).
\tag{L-26208.7}
\]

The right side is the four-scale Mertens fiber

\[
M(Y)-(2+2\sqrt2)M(Y/2)
 +(2+4\sqrt2)M(Y/4)-4M(Y/8).
\tag{L-26208.8}
\]

It remains RH-bearing. The point of odd-core completion is not to delete this scalar, but to retain it inside a complete positive packet rather than export every quotient fragment as an independent indefinite jet.

## 4. Consequence for boundary-jet production

In the notation of PR #272, if the source columns are chosen as the complete fibers `nu_m`, then

\[
\boxed{
J_A\widetilde\beta_Y=0,
}
\tag{L-26208.9}
\]

where `J_A` is the half-pole-value component of the boundary-jet map. The complete unrestricted derivative-Hankel negative charge therefore vanishes on the fiber span.

A quotient or support partition may split one fiber into several cells. The cross terms between those cells are load bearing and must be retained until the fiber is recombined. A block-diagonal estimate of the cell jets would reintroduce a false negative charge which is absent on the actual source.

This gives a concrete repair rule for the Boundary-Jet Domination programme:

```text
complete odd-core fibers first;
partition their physical images second;
retain all within-fiber cross terms;
only then form the source-image Schur short.
```

## 5. What remains

Odd-core completion closes the unrestricted half-pole-Hankel defect on every source fiber. It does not by itself prove that the complete physical/Peano quotient ledger equals the desired carry or shell quantity. A production theorem must still show:

1. every quotient and support cell is included;
2. the collar has zero direct contribution on the declared causal physical block or is routed explicitly;
3. all within-fiber cross terms survive the two-frequency reflected realization;
4. the remaining endpoint and lower-scale rows have nonnegative total reserve.

## 6. Proof boundary

Closed exactly:

- complete five-tap odd-core source grouping;
- preservation of every inner coefficient;
- half-pole nullity of every complete fiber;
- positivity of every unrestricted Green derivative Gram on the fiber span;
- exact RH-bearing collar projection.

Not closed:

- the complete fiberwise quotient identity;
- a cofinal physical-block contraction;
- RH.
