# R-15115 — Euler closure leaves an RH-bearing balanced Möbius core

Claim ID: `R-15115`  
Title: Closing every packet with a macroscopic unrestricted lattice variable does not prove `CP(K)`; the complementary truncated-Möbius packet retains the full rightmost-zero exponent  
Status: **PROPOSED EXACT SCOPE THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Updated: 2026-08-07 to make every Euler-selected coordinate a complete active lattice  
Dependencies: `L-15159`, `T-15123`, `L-15160`; terminal closure on PR #165 `L-15449/L-15450`  
Scope: exact proof boundary after the strongest current Euler closure; no assertion that the balanced packet theorem is false

## 1. The fixed-logarithm source

Fix `q0>=2`. By `L-15159`, the complete signed Heath--Brown packet with the
final logarithmic variable fixed at `q0` is exactly

\[
 Q_{K,V;q_0,H}(x)
 ={\log q_0\over\sqrt{q_0}}
 Q_{\mu,H}^{(V^K/q_0)}(x-\log q_0)
 \tag{R-15115.1}
\]

on every block lying inside the coefficient endpoint. In particular, the
`q0=2` slice is a translated nonzero multiple of the Möbius safe signal.

`T-15123` gives its upper exponential energy exponent as the rightmost zeta-zero
displacement `Theta_zeta`.

## 2. A complete-lattice Euler partition

In a tuple of the `j`-th Heath--Brown row, after `q=q0` is fixed, the remaining
unrestricted variables are

\[
 r_1,\ldots,r_{j-1}.
\]

Let the common compact window have support `[u_-,u_+]`, and fix `eta>0`.
For one unrestricted coordinate `r_i`, freeze every other variable and write
`A_i` for their complete product, including `q0`. The active `r_i` lattice is
then

\[
 {e^{x-u_+}\over A_i}\le r_i\le {e^{x-u_-}\over A_i}.
 \tag{R-15115.2}
\]

Assign a frozen prefix to the first index `i` for which

\[
 A_i\le e^{(1-\eta)J-u_+-2}.
 \tag{R-15115.3}
\]

The condition is independent of `r_i`. Hence, after the other coordinates are
frozen, the selected coordinate is still summed over its **complete active
integer lattice**; no artificial lower cutoff is inserted. On `J<=x<=J+1`,
(R-15115.2)--(R-15115.3) force every active value of that coordinate to be at
least `e^(eta J+1)`.

All tuple contributions with the same selected coordinate and frozen-prefix
type are recombined with their exact binomial and Möbius signs before an
estimate is made. `L-15160`, with Euler order `R>1/(2eta)`, then gives

\[
 \boxed{
 E_{K,q_0}^{\rm Euler}(J)
 =\exp(-c_{K,eta}J+o_K(J))}
 \tag{R-15115.4}
\]

for a suitable smooth safe window, after the fixed-order divisor and coefficient
ledger is included. The first-order terminal theorem of `L-15449/L-15450` is
the special case in which this complete free lattice carries the terminal
large scale.

The residual packet consists exactly of frozen prefixes for which

\[
 A_i>e^{(1-\eta)J-u_+-2}
 \qquad\text{for every unrestricted coordinate }i.
 \tag{R-15115.5}
\]

For any active tuple in this residual packet,

\[
 r_i={n\over A_i}\le e^{\eta J+O_K(1)}
 \tag{R-15115.6}
\]

for every `i`. Thus the Euler/residual decomposition is source-bound and never
uses a truncated lattice in the Euler term.

## 3. The residual source is truncated-Möbius dominated

Equation (R-15115.6) gives

\[
 r_1\cdots r_{j-1}
 \le \exp((j-1)\eta J+O_K(1)).
 \tag{R-15115.7}
\]

Since the active total product has logarithm `J+O_K(1)`, the product of the
truncated Möbius variables satisfies

\[
 \log(d_1\cdots d_j)
 \ge [1-(j-1)\eta]J-O_K(1).
 \tag{R-15115.8}
\]

For `eta<1/(2K)`, at least half of the physical logarithmic scale is therefore
carried by the variables

\[
 d_i\le V=\exp(J/K+O_K(1)).
\]

No one of these variables is an unrestricted integer lattice. Their Möbius
weights and truncation boundaries are exactly the part not touched by Euler
summation.

The deterministic first-crossing algorithm can split these variables into
balanced factor groups, but it cannot turn them into the free-variable normal
form of `L-15160`. This is the balanced truncated-Möbius core.

## 4. The residual sector retains the spectral exponent

Let `h_mu(J)`, `h_Euler(J)`, and `h_bal(J)` denote the Gram vectors of the full,
Euler-closed, and residual fixed-`q0` slices. The exact prefix partition gives

\[
 h_\mu=h_{\rm Euler}+h_{\rm bal}.
 \tag{R-15115.9}
\]

Equation (R-15115.4) gives

\[
 \|h_{\rm Euler}(J)\|=\exp(-cJ+o(J)).
\]

If `Theta_zeta>0`, `T-15123` gives an unbounded sequence of blocks on which

\[
 \|h_\mu(J)\|=\exp((\Theta_\zeta-o(1))J).
\]

The reverse triangle inequality therefore forces

\[
 \boxed{
 \limsup_{J\to\infty}
 {\log(1+\|h_{\rm bal}(J)\|^2)\over2J}
 =\Theta_\zeta.}
 \tag{R-15115.10}
\]

The same conclusion is automatic when `Theta_zeta=0`, because the logarithm
contains `1` and all three energies are then subexponential.

If the residual source is divided into finitely many balanced destination
packets, Gram Cauchy--Schwarz gives, as in `L-15159`,

\[
 \boxed{
 \max_\tau E_{K,\tau}^{\rm balanced}(J)
 \ge {\|h_{\rm bal}(J)\|^2\over R_K^2}.}
 \tag{R-15115.11}
\]

Hence at least one balanced packet retains the full rightmost-zero exponent.

## 5. Consequence for `CP(K)` and `BTP(K)`

The strongest current Euler machinery closes:

1. terminal Type-I rows;
2. their cutoff transitions;
3. more generally, every source-bound prefix class for which one unrestricted
   coordinate has a complete active lattice carrying a fixed positive
   logarithmic fraction.

It does not close the complementary packet in which the macroscopic scale is
carried by truncated Möbius variables. Equations (R-15115.10)--(R-15115.11)
show that this complementary balanced family remains RH-bearing.

Therefore the broad theorem `CP(K)` may be reduced to the balanced theorem
`BTP(K)`, but it has not been proved. Any proof of `BTP(K)` with a
subexponential or vanishing-rate scale contraction is a genuine proof of the
Möbius safe-energy criterion and hence of RH.

This is not a circularity objection and does not show that `BTP(K)` is false.
It prevents terminal or higher-order Euler closure from being presented as the
completion of the whole packet.

## 6. Proof boundary

Closed here:

- a source-bound partition whose Euler coordinates remain complete active
  lattices;
- exponential closure of every Euler-selected prefix class under `L-15160`;
- identification of the residual truncated-Möbius balanced core;
- retention of the rightmost-zero exponent by that residual core;
- reduction `CP(K) -> BTP(K)` at the level of the remaining analytic burden.

Open:

- a subexponential estimate for the balanced truncated-Möbius core;
- `BTP(K)` / `CP(K)`;
- RH.
