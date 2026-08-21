# R-100700 — Regionwise absolute estimates destroy the critical carrier cancellation

Claim ID: `R-100700`  
Status: **PROVED INTERFACE FIREWALL**  
Created: 2026-08-20  
Depends on: `L-100700`--`L-100702`  
RH status: **unproved**

PR #691 assigned different tools to diagonal, short-interval, long-interval,
and divisor-renewal regions of the double-owner matrix. That assignment is
valid only if shared boundary interval states are retained with orientation.
It is false if the regions are estimated independently by absolute values or
positive majorants.

## Exact reasons

1. By `L-100700`, every rectangular bulk is a mixed coboundary and telescopes
to four boundary interval states. Taking absolute values before adjoining
neighboring rectangles removes this cancellation.

2. By `L-100701`, finite squaring gives

\[
E_{a:b}=Q_{a:b}-\sum_tQ_{a:t-1}R_tE_{t+1:b}.
\]

The transition packet is part of the native source. Dropping it is finite
Euler completion, not a proof about the original packet.

3. By `L-100702`, both the completed core and the transition sum carry the same
critical `sqrt(X)/log X` mode. Their difference restores the vanishing Euler
carrier. Separate nonnegative estimates therefore lose a power.

4. The diagonal one-owner wavelet is itself

\[
{c_0\sqrt X\over\log X}
+O(\sqrt X/\log^2X),
\qquad c_0>0.
\]

It is not a finite or subpower Type-I error.

## Binding rule

A valid continuation must preserve both of the following until after physical
observation:

```text
mixed-coboundary orientation across adjacent matrix regions;
completed-minus-first-transition carrier cancellation.
```

The following proof pattern is invalid:

```text
bound completed core positively;
bound transition packet positively;
bound diagonal owners absolutely;
add the three bounds.
```

It produces a power-sized upper bound even when the original zero-free wavelet
is subpower.

This firewall does not refute double-owner localization or finite squaring.
It specifies their correct joint use: as a balanced homotopy/coboundary, not as
independent positive producers.