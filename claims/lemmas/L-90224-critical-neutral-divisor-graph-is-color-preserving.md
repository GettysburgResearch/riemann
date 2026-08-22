# L-90224 — The critical-neutral odd-annulus divisor graph is color-preserving

Claim ID: `L-90224`  
Status: **PROPOSED COMPLETE EXACT PARITY-FIREWALL LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: `L-90223` odd-annulus normal form  
Scope: exact obstruction to the literal divisibility max-flow attack; no sign theorem and no RH conclusion

## 1. Active graph

Retain the critical-neutral kernel

\[
\kappa(y)=
\begin{cases}
y^{-1/2}-1,&1\le y<2,\\
\sqrt2-(1+\sqrt2)y^{-1/2},&2\le y<4,\\
\sqrt2y^{-1/2}-1/2,&4\le y<8,\\
0,&\text{otherwise}.
\end{cases}
\]

Its unique zero in `(1,8)` is

\[
 y_0=\frac32+\sqrt2.
\]

For an endpoint `X`, let the active vertices be the odd squarefree integers

\[
 \mathcal V_X=\{m:X/8<m\le X\}.
\]

Join `m` to `n` when `n=pm` for an odd prime `p` and both endpoints are active.
Define the signed kernel color of a nonzero vertex by

\[
 \chi_X(m)=\operatorname{sgn}
 \left(\mu(m)\kappa(X/m)\right).
\]

## 2. Only primes `3,5,7` occur

If `n=pm` and both vertices lie in `(X/8,X]`, then

\[
 p=\frac nm<8.
\]

As `p` is odd,

\[
 \boxed{p\in\{3,5,7\}.}
\tag{L-90224.1}
\]

## 3. Every edge preserves color

Put

\[
 y=\frac Xn.
\]

Because `n<=X` and `m>X/8`,

\[
 1\le y<\frac8p\le\frac83<y_0.
\]

Therefore

\[
 \kappa(y)\le0,
\]

with equality only at the harmless endpoint `y=1`. On the other hand

\[
 py=\frac Xm,
 \qquad p\le py<8,
\]

and `p>=3>y_0`, so

\[
 \kappa(py)>0.
\]

Squarefreeness gives

\[
 \mu(n)=-\mu(m).
\]

Thus the Möbius sign and the kernel sign both reverse across the edge, and

\[
\boxed{
 \chi_X(n)=\chi_X(m)
}
\tag{L-90224.2}
\]

whenever both contributions are nonzero.

## 4. Components are monochromatic

Equation (L-90224.2) propagates along every path. Hence every connected
component of the active divisibility graph is monochromatic.

The graph is extremely shallow. A product of two distinct allowed edge primes
is at least `3*5=15>8`, so no strictly increasing divisibility chain can contain
two edges. Components are stars or isolated vertices, although two lower
vertices may meet at one common upper vertex.

## 5. Exact max-flow cut

Let negative signed kernel mass be supply and positive signed kernel mass be
demand. Any transport network whose allowed arcs are contained in the active
divisibility graph has no arc between opposite colors.

Therefore the union of all negative components is a cut with

```text
positive supply on the cut side;
zero capacity to every positive component.
```

Consequently:

\[
\boxed{
\text{No flow supported only on active divisibility/comparability edges can}
\text{ certify the critical-neutral sign.}
}
\tag{L-90224.3}
\]

This is not merely failure of one greedy matching. The natural graph itself
preserves the obstruction it was supposed to cancel.

## 6. What remains possible

A successful exact combinatorial proof must use at least one ingredient absent
from the literal divisor graph:

1. transport between incomparable components, for example prime substitution;
2. an external unit/boundary reservoir;
3. a signed multi-channel coupling before positivity is imposed;
4. an analytic estimate of the aggregate parity imbalance.

The theorem is a parity firewall, not a refutation of the critical-neutral
criterion or of RH.
