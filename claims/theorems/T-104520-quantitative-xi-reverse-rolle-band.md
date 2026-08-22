# T-104520 — Quantitative Xi reverse-Rolle band and corrected last-defect frontier

Claim ID: `T-104520`  
Status: **UNCONDITIONAL PARTIAL DESCENT + CORRECTED TWO-GATE RH REDUCTION**  
Created: 2026-08-22  
Base: PR #720  
RH status: **unproved**

## Unconditional results

1. The canonical one-sided Fourier companions

   \[
   \mathscr E_m(z)
   =
   i^m\int_0^\infty u^m\Phi(u)e^{izu}\,du
   \]

   satisfy

   \[
   \mathscr E_m'=\mathscr E_{m+1}
   \]

   and recover `Xi^(m)` by reflection.

2. For every fixed `eta in (0,1)` and every

   \[
   T_N\sqrt{\frac{\log N}{\eta N}}\to0,
   \]

   every derivative order

   \[
   \eta N\le m\le N
   \]

   has only simple critical-line zeros in the complete fixed-height box.

3. Uniformly in that band,

   \[
   N_m(T_N)
   =
   \frac{2w_mT_N}{\pi}+O(1),
   \]

   and

   \[
   \frac{N_{m-1}(T_N)}{N_m(T_N)}\to1.
   \]

   Consequently every prescribed constant `c<1` is a valid one-step
   reverse-Rolle descent constant throughout the high-derivative band for all
   sufficiently large orders.

4. A proportion-only theorem is impossible for general even Cartwright entire
   functions; the Xi-specific positive Fourier source is essential.

5. The vertical-side integral in the first `L-104515` formulation is not an
   integer index.  The correct boundary object is the complete exterior charge
   consisting of both vertical sides and the lower horizontal side.

## Correct remaining frontier

The high-order portion of the derivative ladder is now closed uniformly.  At a
last defective lower level, the exact alternatives are:

```text
PRES104518:
  a positive derivative-ratio residue / wrong-extremum top-phase event;

EFLUX104518:
  inward index through the complete exterior boundary.
```

Therefore

\[
\boxed{
\mathrm{PRES104518}
\wedge
\mathrm{EFLUX104518}
\Longrightarrow
\mathrm{RH}.
}
\]

Neither exclusion theorem is proved here.

## Meaning of the quantitative descent

This theorem gives a rigorous version of the proposed “constant less than one”
idea:

\[
\boxed{
\forall c<1,\quad
N_{\mathbb R}(\Xi^{(m-1)};[-T_N,T_N])
\ge
c\,
N_{\mathbb R}(\Xi^{(m)};[-T_N,T_N])
}
\]

through every fixed positive fraction of the sufficiently high derivative
ladder, on the natural growing original-height scale.

It does not claim that one may descend that inequality to derivative order
zero without controlling the two last-defect events.  The no-go examples prove
that such a source-free extrapolation would be false.

```text
canonical Fourier derivative chain          PROVED EXACT
uniform constant-fraction high band          PROVED
one-step descent constant c<1                PROVED IN HIGH BAND
vertical-only flux index                     REFUTED
correct exterior-boundary transport          PROVED EXACT
PRES104518                                   OPEN / RH-BEARING
EFLUX104518                                  OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVED
```
