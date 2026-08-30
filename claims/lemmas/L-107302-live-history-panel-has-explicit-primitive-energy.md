# L-107302 — The live one-hundred-history panel has explicit primitive energy

Claim ID: `L-107302`  
Status: **PROVED EXACT FOR THE SOURCE-LOCKED LIVE PANEL ON PR #765**  
Created: 2026-08-30  
Depends on: `L-107300`, `L-107301`; the live history panel at PR #765 head
`a30276a5be049749ebb2147f30f000dd5659298b`  
RH/GRH status: **not assumed**

The live shared-fibre collision packet on PR #765 contains a one-sided
ten-history coefficient vector with pattern

\[
a=(3,3,-1,-1,-1,-1,-1,-1,-1,-1).
\tag{L-107302.1}
\]

The right side has the same pattern.  All one hundred bilateral histories
lie in one physical residue cell, and the literal bilateral coefficient is
rank one,

\[
z_{ij}=\overline{a_i}a_j.
\]

## 1. One-sided mean and primitive energy

Exactly,

\[
\sum_i a_i=-2,
\qquad
\|a\|^2=2\cdot9+8=26.
\tag{L-107302.2}
\]

With ten histories, the mean and primitive energies from `L-107301` are

\[
\boxed{
\|a_M\|^2=\frac{|-2|^2}{10}=\frac25,
\qquad
\|a^\circ\|^2=26-\frac25=\frac{128}{5}.
}
\tag{L-107302.3}
\]

Thus only \(1/65\) of the one-sided energy lies in the mean channel:

\[
\frac{\|a_M\|^2}{\|a\|^2}
=
\frac1{65}.
\tag{L-107302.4}
\]

## 2. Bilateral four-grade ledger

The four tensor-grade energies are

\[
\begin{array}{c|c}
\text{grade}&\text{energy}\\ \hline
M\otimes M&4/25\\
P\otimes M&256/25\\
M\otimes P&256/25\\
P\otimes P&16384/25.
\end{array}
\tag{L-107302.5}
\]

Their sum is

\[
\frac{4+256+256+16384}{25}=676=\|z\|^2.
\]

The residue aggregate is

\[
\sum_{i,j}z_{ij}
=
\left|\sum_i a_i\right|^2=4,
\]

so its squared magnitude is \(16\).

For a single occupied physical cell, `L-107300.12` therefore gives

\[
\boxed{
\mathscr W_\iota(z)
=
d_{\ell,\rho}(16-676)
=
-660\,d_{\ell,\rho}.
}
\tag{L-107302.6}
\]

This is an actual native coefficient calculation, not an arbitrary vector in
the kernel of the occupancy map.

## 3. The equal-history calibration has the opposite sign

The smaller live calibration on PR #765 has two equal one-sided histories.
For

\[
a=b=(1,1),
\]

one has

\[
\left|\sum_{ij}\overline{a_i}b_j\right|^2=16,
\qquad
\sum_{ij}|a_i|^2|b_j|^2=4,
\]

and hence

\[
\boxed{
\mathscr W_\iota=12\,d_{\ell,\rho}>0.
}
\tag{L-107302.7}
\]

Therefore live support collision does not have a universal sign.  The
history coefficients and their primitive energy are load-bearing.

## Consequence

The source-authorized ten-history panel supplies a concrete primitive
channel with a moat of \(660d_{\ell,\rho}\).  A valid signed recombination
theorem may use this primitive energy, but it must keep cross-group terms,
equal arithmetic tuples with different retained labels and conductor
recombination.  No global estimate is claimed.
