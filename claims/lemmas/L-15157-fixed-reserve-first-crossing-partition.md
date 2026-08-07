# L-15157 — Fixed-reserve first-crossing partition

Claim ID: `L-15157`  
Title: The deterministic Heath--Brown factor partition has a strict logarithmic reserve independent of the identity order  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: the tuple ledger of `L-15156`  
Scope: repair of the unnecessary condition `delta_K<1/(2K)`; no packet estimate

## 1. Setup

Let

\[
 n=v_1v_2\cdots v_r,
 \tag{L-15157.1}
\]

where the ordered positive variables are the tuple variables of one exact
Heath--Brown coefficient row. Suppose

\[
 e^{J-C}\le n\le e^{J+C}
 \tag{L-15157.2}
\]

for one fixed support constant `C`.

Fix any number

\[
 \boxed{0<\delta<{1\over2}.}
 \tag{L-15157.3}
\]

No dependence on the Heath--Brown order is imposed.

Traverse the variables in their declared order. Stop at the first index `s`
for which

\[
 A=v_1\cdots v_s\ge e^{\delta J}.
 \tag{L-15157.4}
\]

If no such index occurs before the final variable, take `s=r`. Put

\[
 B=n/A.
\]

## 2. Exact dichotomy

### Type II

If

\[
 A\le e^{(1-\delta)J+C}
 \quad\text{and}\quad
 B\le e^{(1-\delta)J+C},
 \tag{L-15157.5}
\]

then both factor groups lie at a strict fraction of the output logarithmic
scale. Declare `(A,B)` Type II.

### Type I

Otherwise at least one group is small. More precisely:

- if `A>e^((1-delta)J+C)`, then by (L-15157.2)
  \[
  B<e^{\delta J};
  \]
- if `B>e^((1-delta)J+C)`, then
  \[
  A<e^{\delta J};
  \]
- if the threshold was never crossed before the final variable, then `B=1`.

Allowing a harmless enlargement of the support constant at endpoints, every
non-Type-II tuple therefore has a factor group bounded by

\[
 \boxed{e^{\delta J+O(C)}.}
 \tag{L-15157.6}
\]

Declare it Type I, with that group as the small packet.

This proves an exhaustive deterministic Type-I/Type-II partition for every
fixed `delta in (0,1/2)`.

## 3. Consequence for scale contraction

Every Type-II packet has factor scales at most

\[
 (1-\delta)J+O(C),
 \tag{L-15157.7}
\]

while every Type-I packet exposes one factor scale at most

\[
 \delta J+O(C).
 \tag{L-15157.8}
\]

The strict reserve can therefore be chosen once, for example

\[
 \delta={1\over5},
 \tag{L-15157.9}
\]

for every identity order `K`.

The order controls the finite coefficient dictionary and the available signed
packet cancellation, but it need not make the geometric scale reserve tend to
zero.

## 4. Quantitative improvement

In `T-15122`, one may take

\[
 \delta_K=\delta>0
 \tag{L-15157.10}
\]

uniformly. The increasing-order sufficient condition becomes simply

\[
 \boxed{\varepsilon_K\to0,}
 \tag{L-15157.11}
\]

in the linear recurrence, or

\[
 \varepsilon_K/(1-\kappa_K)\to0
 \tag{L-15157.12}
\]

for tensor packets.

This removes an artificial `1/K` loss from the full proposal.

## 5. Proof boundary

Closed here:

- the fixed-reserve deterministic partition;
- its exact Type-I/Type-II dichotomy;
- independence of the reserve from the identity order.

Not closed:

- bounds for either packet class;
- a vanishing coefficient rate;
- RH.
