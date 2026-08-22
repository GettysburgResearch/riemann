# T-104500 successor handoff

## Read first

1. `R-104500`
2. `L-104500`
3. `L-104501`
4. `L-104502`
5. `L-104503`
6. `T-104500`
7. the exact replay and source lock

## Strongest proved results

```text
factor-two polynomial defect conservation       exact
adjacent-critical-value interval identity        exact
complex off-real-zero/winding transport          exact
Riccati/Pick derivative dynamics                 exact
fixed-scaled-box high derivative real zeros      unconditional
fixed finite-depth scaled derivative cascade     unconditional
```

## First open arrows

```text
GBOX104500
  compact cosine limit -> expanding original-height rectangles;

RPCH104500
  derivative-ratio Pick/winding data -> cumulative integer charge <2.
```

## Recommended next attacks

### Route A — quantitative Fourier saddle

Use the positive Fourier kernel of Xi and the tilted probability measure
proportional to `u^(2n) Phi(u) du`.  Prove exponential-moment concentration
around its saddle uniformly for complex `t` in a fixed original-height
rectangle.  The target is a Rouche-safe approximation to `cos(t/C_n)` on all
zero disks and their complement.

### Route B — source-locked Riccati Pick transport

Construct the actual derivative-ratio kernels

```text
K_k(z,w)=[h_k(z)-conj(h_k(w))]/[z-conj(w)]
```

on one common rectangle.  Bound their negative spectral mass, relate it to the
wrong-extremum residues, and combine with the exact boundary argument variation
of `F_k/F_(k+1)`.  Do not reuse the order-three critical reserve across levels.

### Route C — growing-order Levinson–Conrey integer upgrade

Make the exceptional proportion uniform for `k=k(T)` and strong enough that

```text
exceptional proportion * total derivative-zero count < 2.
```

The exceptional count is even, hence zero.  Feed that actual zero-free high
order into the exact cascade rather than descending a percentage.

## Status

RH remains unproved.  The programme now has exact state variables and exact
integer closure, but two quantitative estimates remain.
