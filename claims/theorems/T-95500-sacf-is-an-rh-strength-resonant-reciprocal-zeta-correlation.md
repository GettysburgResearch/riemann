# T-95500 — SACF is an RH-strength resonant reciprocal-zeta correlation

Claim ID: `T-95500`  
Status: **PROPOSED COMPLETE DIAGNOSIS/CONDITIONAL CONSUMER — SACF OPEN**  
Created: 2026-08-18  
Depends on: PR #580 at exact head `812e7fcbaff2dd1c2c53c885def7b6c0d0e68a05`; `L-95500`–`L-95504`; `R-95500/R-95501`

## 1. What the new analysis proves

After the exact PR #580 deletions, SACF is not an independent generic
coprime bilinear form. Reattaching the already-polylogarithmic sectors gives
the square of one annular Möbius packet. In gcd coordinates the common-divisor
state lies on the critical hyperplane and exactly factorizes the source as

\[
M_o(s_1)M_o(s_2).
\]

The ten Q4 bands contribute only explicit entire Mellin multipliers. The
logarithmic channel has no zero in the counterexample strip, and the boundary
channel cannot cancel its higher-order pole.

## 2. Exact strength statement

For \(H=\log^B(2X)\), let \(\mathcal S_H\) denote SACF. Then:

\[
|\mathcal S_H(X)|\ll X^{2\theta}
\quad\Longrightarrow\quad
\zeta(\rho)=0\Rightarrow\Re\rho\le\frac12+\theta.
\]

In particular:

\[
|\mathcal S_H(X)|\ll X^{1-\delta}
\quad\Longrightarrow\quad
\Re\rho\le1-\frac\delta2,
\]

and

\[
|\mathcal S_H(X)|\ll\log^A(2X)
\quad\Longrightarrow\quad
\mathrm{RH}.
\]

## 3. Unconditional gain that survives

The classical zero-free-region Mertens estimate and exact ten-band partial
summation give

\[
|\mathcal S_H(X)|
\ll_B
X\log^2(2X)e^{-c\sqrt{\log X}}+\log^{B+2}(2X).
\]

Thus the arithmetic coefficients do provide a genuine subexponential gain
over the source-blind `O(X polylog X)` scale.  The gain is not a fixed power,
so it does not yield a new fixed zero-free strip.

## 4. Disposition of the requested methods

```text
dyadic/ratio/gcd localization          retained exactly
common-divisor dispersion              exact Euler resonance, not free averaging
Vaughan/Heath–Brown                    exact derivative decompositions; balanced factor survives
determinant k=ab                       reconstructs shifted reciprocal-zeta pair
dual-frequency analysis               gives |M_o(s+it)|^2
positive-kernel completion             PSD and resonant, not cancelling
fixed-window large sieve               retains O(X) spacing loss
pretentious/zero-free input            would need fixed-strip or RH-scale strength
```

## 5. Correct frontier

The requested polylogarithmic SACF theorem remains unproved. The exact new
result is that its formulation already contains the classical reciprocal-zeta
square with no unused finite-band cancellation. Any successful continuation
must introduce genuinely new arithmetic information about the Möbius
coefficients; it cannot obtain the required gain solely from the Q4 band
geometry or from generic bilinear energy.

```text
critical gcd resonance                 PROVED EXACT
kernel noncancellation                  PROVED EXACT
classical subexponential SACF gain       PROVED
power-saving -> fixed zero-free strip  PROVED
polylog SACF -> RH                      PROVED CONDITIONAL
SACF                                   OPEN / RH-BEARING
FOCC / OCHD                            OPEN / RH-BEARING
Riemann Hypothesis                     UNPROVEN
```
