# O-90011 — The balanced compact-current / odd-reserve gate

Claim ID: `O-90011` (provisional range; allocate before integration)  
Status: **OPEN RH-BEARING GATE + FINITE RECONNAISSANCE; NOT A THEOREM**  
Authoring agent: `gpt56-sol`  
Date: 2026-08-09  
Depends on: `L-34404`, corrected `L-34406`, `L-90010`  
Scope: isolates the sharpest local inequality suggested by the repaired Q4 state.

## 1. The exact gate

Let `e=(n,j)`, `k=n-j`, and fix a balanced cone
\[
\eta n\le j\le(1-\eta)n,
\qquad 0<\eta<1/2.
\]
Retain the deterministic odd-prime reserve increment
\[
\Delta_4R_{\rm odd}(e)
=R_{\rm odd}(4e)-16R_{\rm odd}(e).
\]
`L-34404` proves
\[
\Delta_4R_{\rm odd}(e)=\Theta_\eta(n\log n)>0
\]
cofinally.

Let
\[
B_\circ(s)=\frac{1-4^{1-s}}{\zeta(s)},
\qquad
q_\circ=B_\circ',
\]
and put
\[
Q_\circ(e)=\mathcal L_e(q_\circ).
\]
The most direct missing critical-scale domination is:

> **Balanced compact-current gate.** Prove, for every fixed `eta`, a finite
> constant `C_eta` such that cofinally
> \[
> \boxed{
> |Q_\circ(4e)|^2
> \le C_\eta\,\Delta_4R_{\rm odd}(e)
> +\operatorname{polylog}(n).
> }
> \tag{O-90011.1}
> \]

A coefficient below one would be especially strong, but even a controlled
source-matched constant is useful for the reflected ledger.  No such estimate
is proved here.

## 2. Exact Chebyshev form of the compact current

Since
\[
\zeta(s)B_\circ(s)=1-4^{1-s},
\]
differentiation gives
\[
\mathbf1*q_\circ
=\Lambda-4\,\delta_4*\Lambda+4(\log4)\delta_4.
\]
Thus on an aligned nontrivial row
\[
\boxed{
\begin{aligned}
Q_\circ(4n,4j)
={}&\psi(4n)-\psi(4j)-\psi(4k)\\
&-4\,[\psi(n)-\psi(j)-\psi(k)]-4\log4.
\end{aligned}}
\tag{O-90011.2}
\]
This is the exact RH-sensitive radix-four Chebyshev fluctuation already
identified after the withdrawal of the false prime-free claim `L-32305`.

Equation (O-90011.1) would therefore be a genuinely arithmetic theorem, not a
finite-filter tautology.

## 3. Why this is the right scale after R-90009 / L-90010

The corrected odd-source analysis proves
\[
\Delta_4R_{\rm odd}(e)
=\Delta_2R_{\rm odd}(2e)+4\Delta_2R_{\rm odd}(e),
\]
with each scale-two increment `Theta_eta(n log n)`.  It also routes the compact
current through two centered scale-two odd-current innovations plus an explicit
logarithmic bare gauge.

Thus both sides of (O-90011.1) now live in the **same odd carrier and the same
critical radix increments**.  This is precisely what was missing when the
compact current was compared to the oversized absolute matching-parity reserve
of order `n^2`.

If (O-90011.1) is proved with the collars already available for thin boundary
rows, it supplies the scale-matched local current domination needed by the Q4
reflected/scattering composition.  The remaining assembly still has to respect
the existing no-double-spend and terminal-state firewalls.

## 4. Finite reconnaissance

A direct sieve/prefix scan was made using the exact formulas

\[
R_{\rm odd}(e)
=O(e)^2-S_{\rm odd}(e),
\]
\[
O(e)=\log\operatorname{odd}\binom nj,
\]
and (O-90011.2).

For every integer
\[
20\le n\le5000
\]
and every quarter-balanced row
\[
\lceil n/4\rceil\le j\le\lfloor3n/4\rfloor,
\]
the observed ratio
\[
\frac{|Q_\circ(4e)|^2}{\Delta_4R_{\rm odd}(e)}
\]
was below `0.534`; the largest observed value was approximately
\[
0.53375
\]
at `(n,j)=(31,15)`.

This numerical pattern is **not evidence sufficient for promotion**.  The
source is RH-sensitive, and finite computation cannot distinguish eventual
off-line behavior.  It is recorded only because it identifies an unusually
sharp coefficient-one target with a large finite margin.

The balanced restriction is essential to the formulation: thin boundary rows
can have a ratio above one at small scales.  Those rows belong to the separate
polylogarithmic collar mechanism (`L-34005` / `L-34405`) rather than to an
interior reserve theorem.

## 5. Failed shortcut

One might try to obtain (O-90011.1) by differencing the full matching-parity
augmented curvature.  Finite exact-source tests reject that idea: its raw
scale-two and scale-four increments retain signed `n^2`-scale oscillations from
the explicit dyadic dressing.  The odd-carrier extraction is not cosmetic; it
is necessary to expose the `n log n` critical increment.

Likewise, positivity of the corrected vector curvature
\[
\Delta_2R_{\rm odd}+|I_2|^2
\]
is only a lower/storage identity and does not upper-bound the current.

## 6. Boundary

Proved elsewhere and used here:

```text
Delta_4 R_odd = Theta_eta(n log n)
exact centered scale-two odd relative state
exact compact-current two-tap routing
boundary current is polylog-local
```

Open:

```text
balanced compact-current gate (O-90011.1)
coefficient-one reflected dissipative placement
RH
```

No RH claim is made.