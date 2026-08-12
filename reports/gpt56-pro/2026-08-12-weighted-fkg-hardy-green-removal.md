# Weighted FKG, Hardy-square storage, and exact Green removal

## Status

```text
repository: gfreund123/riemann
branch:     research/gpt56-pro/91008-cauchy-square-clark-jordan
parent PR:  #396
RH:         UNPROVED
```

This continuation attacks the open Cauchy–Jordan Hardy intertwiner rather than adding another zero criterion.

## 1. All finite Green divisions are now positive

For

\[
 F_s(n)=\prod_{p\mid n}(1-p^{-s}),
 \qquad
 c_s=\zeta(1+s)^{-1},
\]

weighted Harris association proves

\[
 \sum_{n\le N}\frac{F_s(n)}n h(n)
 \ge
 \prod_{p\le N}(1-p^{-1-s})
 \sum_{n\le N}\frac{h(n)}n
\]

for every nonnegative decreasing weight `h`.

Taking truncated logarithmic powers gives nonnegative functions

\[
 E_{s,m}(t)
 =\sum_n\frac{F_s(n)}n
   \frac{(t-\log n)_+^m}{m!}
  -c_s\frac{t^{m+1}}{(m+1)!},
\]

with

\[
 \frac{Z_s(q)-c_s/q}{q^{m+1}}
 =\int_0^\infty e^{-qt}E_{s,m}(t)\,dt.
\]

Thus the centered Jordan source remains completely monotone after every finite Green division, including the full phase-resolved Hankel kernels.

## 2. The target residual space is canonical

The all-order Cauchy storage kernel has the Hardy-square mixture

\[
 F_m(u^2/a^2)
 =\int_0^\infty|\Psi_{m,a,r}(iu)|^2dr,
\]

where

\[
 \Psi_{m,a,r}(z)
 =\sqrt{(m+2)!W_m(r)}a^{m+2}
   \frac{z}{(z+a\sqrt r)^{m+3}}.
\]

The impulse response is an explicit causal exponential polynomial with zero total mass. Consequently the target of CJHI is no longer existential: it is the direct integral of these Hardy channels.

## 3. The apparent three-state problem is only a symmetric square

The three-state Cauchy all-pass matrix is fixed-orthogonally conjugate to the symmetric square of

\[
 R_a(u)=\frac1{\sqrt{a^2+u^2}}
 \begin{pmatrix}a&u\\-u&a\end{pmatrix}.
\]

The remaining completed colligation may therefore be built in two states and lifted functorially. A generic three-by-three interpolation theorem is unnecessary.

## 4. Exact Green-removal boundary density

For the sharp Cauchy numerator, put

\[
 \kappa=\sqrt{275/14}.
\]

Multiplying the three-Green arithmetic channel by the numerator produces exactly:

```text
one positive contact at t=0;
positive atoms F_(2a)(n)/n at t=log n;
one continuous density.
```

The continuous density is

\[
 \boxed{
 \mathcal B_{2a,a}(t)
 =-c_{2a}
  +\kappa aE_{2a,0}(t)
  +4a^2E_{2a,1}(t).
 }
\]

There is no further hidden boundary port on the arithmetic side.

## 5. Unconditional regions

The density is rigorously positive:

1. on the first logarithmic cell `0<=t<=log 2` for every `a>0`;
2. whenever
   \[
   t>T(a)=
   \frac{[1-\kappa a(1-\log2)-2a^2(\log2)^2]_+}
        {4a^2(1-\log2)};
   \]
3. for every `t>=0` once `a>=1/2`.

Between knots it is concave; every arithmetic knot creates an upward jump. Thus only knot left limits in the finite middle interval can obstruct positivity.

The terminal scale required by the coefficient-one recurrence is now completely closed on the arithmetic side.

## 6. Reconnaissance

The retained replay reports

```text
PASS_WEIGHTED_FKG_HARDY_GREEN_REMOVAL
checks: 1318
exact weighted-FKG checks: 531
```

A floating scan through `N=20,000` at

```text
a=0.01,0.03,0.05,0.1,0.2,0.4,0.8,1.5,3
```

found the minimum of the boundary density at the first knot in every case. The smallest sampled value was approximately

```text
0.0242170620  at a=0.01.
```

This is discovery evidence only.

## 7. Correct frontier

The remaining arithmetic statement is now the single finite-window inequality

\[
 \boxed{
 \mathcal B_{2a,a}(t)\ge0
 \qquad(0<a<1/2,\ \log2<t\le T(a)).
 }
\]

Even a proof of this density gate does not by itself authorize an RH claim. The positive arithmetic measure must still be inserted into the completed gamma/pole scattering system and identified with the critical-boundary Cauchy Hardy Gram.

The proof programme is therefore:

```text
weighted FKG all-Green hierarchy                  CLOSED
canonical Hardy target                            CLOSED
minimal two-state all-pass geometry               CLOSED
arithmetic Green removal at a>=1/2                CLOSED
arithmetic compact middle density, 0<a<1/2        OPEN
completed gamma/pole source-to-Hardy intertwiner  OPEN / RH-BEARING
RH                                                 UNPROVED
```

The next useful attack is a scale-uniform proof of the middle-density inequality, preferably from the logarithmic-integer product measure or a renewal/stop-loss theorem, followed by the completed boundary colligation. Another equivalent scalar is not needed.