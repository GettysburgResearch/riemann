# T-105350 — The sharp Xi boundary gate is one origin-anchored Stieltjes hierarchy

Claim ID: `T-105350`  
Status: **MAJOR EXACT QUANTIFIER REDUCTION; XI STIELTJES SIGN OPEN**  
Created: 2026-08-23  
Depends on: `L-105328--L-105351`, parent `T-105220`, `T-105330`  
RH status: **unproved**

## 1. Advance over the separated-packet frontier

`T-105330` expresses the boundary gate through every Cauchy–Vandermonde
determinant at every separated real packet. `L-105350` proves that analyticity
removes the packet geometry completely:

```text
all separated Loewner packets on one interval
    iff
all confluent Hankel matrices at one fixed analytic anchor.
```

For a symmetric Xi window the anchor is canonically zero and parity reduces
the data to one scalar sequence.

## 2. The origin sequence

For the last defective derivative `F=Xi^(k)` and one regular symmetric window,
let

\[
H=H_{F,\Omega}
\]

be the parent boundary Cauchy function and define

\[
\boxed{
\beta_n(F;\Omega)
={1\over2pi i}\int_{\partial\Omega}
{F(\zeta)/F'(\zeta)\over\zeta^{2n+2}}\,d\zeta.
}
\tag{T-105350.1}
\]

Put

\[
\mathsf E_j=[\beta_{r+s}]_{r,s<j},
\quad
\mathsf O_j=[\beta_{r+s+1}]_{r,s<j}.
\tag{T-105350.2}
\]

Then

\[
\boxed{
\mathsf E_j\succeq0\text; and }\mathsf O_j\succeq0
\quad(j\ge1)
\Longleftrightarrow
\mathscr R_{F,\Omega}\succeq0
\text{ on every real packet.}
}
\tag{T-105350.3}
\]

The factors `F'(x_i)` in the boundary Bezoutian are a real diagonal
congruence away from critical nodes; critical rows vanish. Thus (T-105350.3)
is exactly the all-packet boundary component of `BRP105220`.

## 3. Stieltjes and safe-axis forms

The matrix hierarchy is equivalent to a positive compactly supported measure
`nu_(F,Omega)` on `[0,infinity)` with

\[
\boxed{
H="z\int_0^\infty{d\nu(s)\over1-sz^2}.
}
\tag{T-105350.4}
\]

Equivalently, the literal boundary safe-axis scalar is Stieltjes:

\[
\boxed{
{H(iy)\over iy}
={1\over2pi i}\int_{\partial\Omega}
{F(\zeta)/F'(\zeta)\over\zeta^2+y^2}\,d\zeta
=\int_0^\infty{d\nu(s)\over1+s y^2}.
}
\tag{T-105350.5}
\]

This is the exact source coordinate that a complete-monotonicity, safe-axis,
Laplace, or continued-fraction attack must prove. Existing actual-Xi Pick
results cannot be imported until their function, normalization and exhaustion
are identified with this boundary Cauchy scalar.

## 4. New conclusion graph

Define `OASH105350` to be the complete origin-anchored Stieltjes-Hankel
hierarchy (T-105350.2) in every window of the exact exhaustion. Then

\[
\boxed{
\mathrm{OASH105350}
\Longleftrightarrow
\mathrm{BCVH105330}
\Longleftrightarrow
\text{boundary-PSD component of }\mathrm{BRP105220}.
}
\tag{T-105350.6}
\]

The critical determinant hierarchy still supplies the other exact block:

\[
\mathrm{CRVH105330}
\Longleftrightarrow
\mathrm{PRES105220}
+\text{absence of nonreal critical correction}
\]

on the simple noncommon stratum. Therefore

\[
\boxed{
\mathrm{CRVH105330}
\wedge
\mathrm{OASH105350}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-105350.7}
\]

Neither antecedent is proved for fixed low-order Xi.

## 5. Why the reduction matters

The former boundary gate quantified over:

```text
every packet size;
every collection of separated real nodes;
every coefficient vector;
every exhaustion window.
```

The exact analytic reduction retains only:

```text
one canonical anchor zero;
hanne scalar contour sequence beta_n;
two nested Hankel families;
every exhaustion window.
```

It remains all-order, as it must. `R-105350` gives a rational odd function for
which the first two confluent matrices and every one-/two-node principal
restriction of a selected packet are positive, while the third order is negative.

## 6. Immediate work packages

```text
SAFE-STIELTJES-105350:
  identify the boundary scalar H(iy)/(iy) with a positive Stieltjes/Laplace
  transform from the explicit Xi source, retaining the interior-pole
  subtraction exactly;

HANKEL-GRAM-105350:
  derive a same-source Gram formula for E_j and O_j before any truncation or
  absolute value;

TERMINAL-MEASURE-105350:
  prove positivity of one outer-window Stieltjes measure and transport it
  inward using L-105217 plus CRVH105330;

CONFLUENT-105350:
  splice common-zero and multiple-critical jets into the anchor sequence.
```

## 7. Exact boundary

```text
one-anchor Hamburger-Loewner equivalence         PROVED EXACT
Xi parity -> one Stieltjes sequence              PROVED EXACT / FINITE WINDOW
safe-axis boundary scalar identity                PROVED EXACT
Nall-packet BCVH <-> origin Hankel hierarchy      PROVED EXACT
bounded confluent-order bootstrap                REFUTED
CRVH105330                                          OPEN / SHARP RH-BEARING
OASH105350                                          OPEN / SHARP RH-BEARING
moving saddle global dominance                     OPEN
Riemann Hypothesis                                  UNPROVEN
```
