# Addendum — the dyadic Cauchy-square gate is the preferred frontier

## Freeze

```text
parent branch: research/gpt56-pro/91004-radial-curvature-depth-projector
parent SHA:    82ee32348b05512514462966bfeb4e2de4ae5ecf
continuation:  research/gpt56-pro/91008-cauchy-square-clark-jordan
RH status:     UNPROVED
```

## Preferred theorem

The conclusion-producing target is now the fixed-dilation inequality

\[
 \boxed{
 \mathcal N_x(2a)\ge\mathcal N_x(a)
 \qquad(x\in\mathbb R,\ a>0),
 }
\]

where

\[
 \mathcal N_x(a)=\frac12
 \left[
 a\Re{\xi'\over\xi}(1/2+a+ix)
 -a^2\partial_a\Re{\xi'\over\xi}(1/2+a+ix)
 \right].
\]

This theorem is proposed equivalent to RH. Under RH its zero-side increment is
exactly a sum of two rational squares. Under false RH, a maximal-depth zero at
a fixed ordinate makes the lower-resolution term singular while the doubled
resolution remains regular.

## Source alignment

The arithmetic deformation

\[
 Q_a(s)=\frac{\zeta(s)}{\zeta(s+2a)}
\]

has coefficients

\[
 q_a(n)=\prod_{p\mid n}(1-p^{-2a})>0
\]

and the positive cocycle

\[
 Q_{a+b}(s)=Q_a(s)Q_b(s+2a).
\]

Thus the fixed dilation \(a\mapsto2a\) is aligned simultaneously with:

```text
zero side:      a two-channel Hermitian square;
source side:    a positive shifted sieve cocycle;
critical a=1/2: the Euler-totient coefficient phi(n)/n.
```

## Review order

1. `L-91008`
2. `L-91012`
3. `T-91004`
4. `L-91011`
5. `T-91003`
6. `L-91009/L-91010`
7. `R-91003`
8. `X-91008`

## Boundary

```text
dyadic zero-side factorization       EXACT
dyadic criterion reverse direction   PROPOSED COMPLETE
positive sieve source/cocycle         EXACT
critical-boundary Hermitian transfer  OPEN / RH-EQUIVALENT
Riemann Hypothesis                    UNPROVED
```
