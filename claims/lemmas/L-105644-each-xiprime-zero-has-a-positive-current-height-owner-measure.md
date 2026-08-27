# L-105644 — Each Xi-prime zero has a positive current-height owner measure

Claim ID: `L-105644`  
Status: **PROVED EXACT ONE-ZERO SCALE-TRANSPORT THEOREM**  
Created: 2026-08-25  
Depends on: `L-105624`, `L-105641--L-105643`  
RH status: **not assumed**

## 1. The current profile decreases in total height

For a positive even source, `L-105641` gives

\[
R_H(\xi)
={e^{-H\xi}\over
 \displaystyle\mathbb E_\xi
 {\sinh(2HX_\xi)\over2HX_\xi}},
\qquad H>0,\ \xi\ge0.
\tag{L-105644.1}
\]

For every fixed `xi`, the numerator is nonincreasing in `H`. The function

\[
g(z)={\sinh z\over z}
\]

is strictly increasing on `(0,infinity)` because

\[
z\cosh z-\sinh z>0.
\]

Therefore the denominator in (L-105644.1) is nondecreasing in `H`, and

\[
\boxed{
H\longmapsto R_H(\xi)
\text{ is nonincreasing.}
}
\tag{L-105644.2}

Moreover,

\[
\boxed{
\lim_{H\downarrow0}R_H(\xi)=1,
\qquad
0<R_H(\xi)\le e^{-H\xi}.
}
\tag{L-105644.3}

For the standard Xi source, `L-105624/L-105640` also give that

\[
\boxed{
\xi\longmapsto R_H(\xi)
\text{ is nonincreasing.}
}
\tag{L-105644.4}

Both monotonicities are load bearing below.

## 2. One fixed derivative zero

Let

\[
\rho=\alpha+i\gamma,
\qquad
\gamma>0,
\]

be one zero of `Xi'`, with multiplicity handled by repetition. At total height
`0<=H<gamma`, the shifted denominator `Xi'(z+iH)` has an upper zero at depth

\[
y=\gamma-H.
\]

The normalized model-space vector of that one Blaschke factor is

\[
\phi_{\rho,H}(\xi)
=
\sqrt{2(\gamma-H)}
 e^{-(\gamma-H)\xi}e^{-i\alpha\xi}.
\tag{L-105644.5}
\]

Define its actual current-profile charge

\[
\boxed{
Q_\rho(H)
=
2(\gamma-H)
\int_0^\infty
R_H(\xi)e^{-2(\gamma-H)\xi}\,d\xi,
\qquad 0\le H<\gamma,
}
\tag{L-105644.6}

and put `Q_rho(H)=0` for `H>=gamma`.

Equivalently,

\[
Q_\rho(H)
=
\langle M_{R_H}\phi_{\rho,H},\phi_{\rho,H}\rangle.
\]

The horizontal coordinate `alpha` cancels from the charge.

## 3. The charge decreases from one to zero

At `H=0`, (L-105644.3) gives

\[
\boxed{Q_\rho(0)=1.}
\tag{L-105644.7}

At the crossing height, the exponential cap gives

\[
0\le Q_\rho(H)
\le
{2(\gamma-H)\over H+2(\gamma-H)},
\]

so

\[
\boxed{
\lim_{H\uparrow\gamma}Q_\rho(H)=0.
}
\tag{L-105644.8}

It remains to prove monotonicity. Let `0<=H_1<H_2<gamma`. First,

\[
R_{H_2}(\xi)\le R_{H_1}(\xi)
\]

by (L-105644.2). Second, the probability density

\[
2(\gamma-H)e^{-2(\gamma-H)\xi}
\]

is exponential with rate `2(gamma-H)`. Increasing `H` decreases the rate and
therefore shifts the random variable stochastically to the right. Since
`R_(H_1)` is nonincreasing in `xi`,

\[
\mathbb E_{H_2}R_{H_1}
\le
\mathbb E_{H_1}R_{H_1}.
\]

Combining the two comparisons yields

\[
\boxed{
Q_\rho(H_2)\le Q_\rho(H_1).
}
\tag{L-105644.9}

For the strict Xi source the decrease is strict away from degenerate limits.

## 4. A canonical probability measure on descent height

The nonincreasing right-continuous survival function `Q_rho`, with endpoint
values one and zero, defines a positive Stieltjes probability measure

\[
\boxed{
d\nu_\rho(H)=-dQ_\rho(H)}
\tag{L-105644.10}
\]

on `[0,gamma]`. Its total mass is exactly

\[
\boxed{
\nu_\rho([0,\gamma])=1.
}
\tag{L-105644.11}

Thus one unit of topological multiplicity is represented as a positive,
source-owned distribution over the heights at which the shifted denominator
approaches that zero.

For a finite zero packet `Z`, define

\[
\nu_Z=\sum_{\rho\in Z}m_\rho\nu_\rho.
\]

Then

\[
\boxed{
\nu_Z([0,\infty))
=\sum_{\rho\in Z}m_\rho.
}
\tag{L-105644.12}

The raw zero count is therefore the total mass of a positive current-height
owner measure.

## 5. Relation to the collar theorem

The survival function obeys the explicit envelope

\[
\boxed{
Q_\rho(H)
\le
{2(\gamma-H)\over2\gamma-H}.
}
\tag{L-105644.13}

Hence zeros at fixed depth retain a fixed positive amount of owner mass below
the boundary, whereas a boundary-near zero concentrates its owner measure in a
shrinking height interval.

This reconciles the two facts isolated by `L-105643/R-105640`:

```text
at one fixed height, a shallow zero can be source-cheap;
across all heights, that same zero still owns exactly one positive unit.
```

## 6. New common target for pointwise and shell routes

The all-pass shell programme counts an integer jump when a zero crosses a
height. The differential-microscope programme carries the smooth current
profile `R_H`. Equation (L-105644.10) is a canonical positive regularization of
that jump.

Define the remaining transfer:

```text
HOWNXFER105644 — height-owner transfer

Identify the current-height owner measure -dQ_rho with the signed height flow
of the physical Xi-prime all-pass, including the two-trace point evaluation,
common-zero confluence and the cofinal endpoint ledger.
```

A successful transfer would let the pointwise phase reserve and the integrated
all-pass index consume the same positive unit measure rather than estimate one
another by absolute values.

## 7. Scope

The sum of the individual owner measures is an exact divisor-atom
decomposition. It is not asserted to equal the trace of a nonorthogonal
multi-zero model space at each fixed height. The theorem does not prove
`HOWNXFER105644`, `BCOLLAR105643`, `POINTID105630`, or RH.