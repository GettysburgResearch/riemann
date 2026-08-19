# T-99250 — The factor-67 SHARP Harnack tail is the sole remaining producer

Claim ID: `T-99250`  
Status: **PROVED CONDITIONAL CLOSURE THEOREM + FINITE CERTIFICATE; TAIL OPEN**  
Created: 2026-08-19  
Frozen parent: PR #642 at `07aa0d4838458a1b2d3af9e5bc96616baa6b4767`  
RH status: **not established**

Let

\[
\Psi(x)=\sum_{n\le x}\frac{\mu(n)}{\sqrt n}(4\sqrt{x/n}-3)
\]

and

\[
\mathfrak H_{67}(x)=\Psi(x)-67^{-1/2}\Psi(x/67),
\]

with zero extension below `1`.

`L-99252` proves

\[
\mathfrak H_{67}(x)>0
\qquad(1\le x<100{,}000{,}001).
\]

Assume the single tail statement

\[
\boxed{
\mathfrak H_{67}(x)\ge0
\qquad(x\ge100{,}000{,}001).
}
\tag{T-99250.1}
\]

Then the defect is nonnegative globally. `L-99251` gives two independent
conclusion paths.

### Scalar path

The exact Mellin transform is

\[
\int_1^\infty\mathfrak H_{67}(x)x^{-s-1}dx
=
\frac{(1-67^{-(s+1/2)})(s+3/2)}
{s(s-1/2)\zeta(s+1/2)}.
\]

A nonnegative density has a real Landau singularity at its abscissa of
convergence, but the displayed continuation is analytic on every real `s>0`.
Every zero with real part greater than `1/2` produces a genuine nonreal pole,
because `1-67^{-rho}` cannot vanish there. This contradiction and functional
equation symmetry give RH.

### Component-row cross-check

Repeated division by `67` gives `Psi(x)>=0` globally. The exact positive kernel
of PR #642 then gives `c_X(j)>=0` for every fixed row. Its fixed-row
Mellin–Landau consumer gives the same conclusion.

Therefore

\[
\boxed{(T\text{-}99250.1)\Longrightarrow RH.}
\]

## Repaired and removed interfaces

The packet also proves the exact Radon–Nikodym common-parent map for PR #642:

\[
dM_Z=\mathbf1_{t\le Z}\frac{T(Z/t)}{T(Y/t)}dM_Y.
\]

This reconstructs normalized Hall monotonicity and source-faithful child
ownership. It is retained as a stress-tested interface theorem, but the scalar
path does not need the global common-parent tree.

The conclusion-facing DAG is now

```text
compact SHARP base on [1,67)
 + exact directed H67 certificate below 10^8+1
 + ONE scalar tail H67>=0
 -> nonnegative scalar Mellin density
 -> reciprocal-zeta pole exclusion
 -> functional equation
 -> RH.
```

No score, capacity, equality frame, Volterra anchor, endpoint quantizer,
row-specific noncancellation, terminal port, or prime-square interface remains
between the open producer and the conclusion.

## Exact boundary

```text
SHARP positive row kernel                     imported exact from PR #642
kernel normalized-profile theorem             proved exact here
kernel Radon–Nikodym child map                 proved exact here
raw child support cutoff                       refuted and repaired
factor-67 local square                         proved exact here
H67 sign for every real x<100000001            proved directed here
H67 sign for x>=100000001                      OPEN / RH-BEARING
accepted proof of RH                           NO
Riemann Hypothesis                             UNPROVED
```
