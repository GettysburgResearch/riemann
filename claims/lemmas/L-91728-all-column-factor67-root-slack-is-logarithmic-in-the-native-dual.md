# L-91728 — The repaired all-column factor-67 root slack is logarithmic in the native dual

Claim ID: `L-91728`  
Status: **PROPOSED COMPLETE ONE-SHOT NATIVE-DUAL ROOT-COST THEOREM ON FROZEN ALL-COLUMN INPUTS — REVIEW REQUIRED**  
Created: 2026-08-15  
Frozen inputs: PR #479 at `518b6a5ec2b49b7decbd4c2e349d0ee5b26bfc9b`; `L-91378`; fixed-width omission/base estimates; `Y_4` support computation of PR #477  
RH status: **unproved**

## 1. Correct scalar

Put

\[
 K=\left\lfloor X/67\right\rfloor+1,
 \qquad
 \tau_K=\frac{\sqrt K}{\sqrt K+130}.
\]

Let `r_X>=0` be the unused packet-native detail vector after the factor-67
Hall/first-owner packet, the all-column owner split, one square-root thinning,
one quantizer, the top/bottom omissions, one finite correction and one common
port, with full child packet capacities reserved once.  The local scalar is

\[
 \delta_X=\langle Y_4,r_X\rangle.
 \tag{L-91728.1}
\]

## 2. Sparse native dual

The radix-four dual satisfies

\[
 Y_4(q)=\sum_{h=0}^{v_4(q)}2^h\Lambda(q/4^h).
\]

Writing `q=2^em` with `m` odd gives

\[
 Y_4(2^e)=\bigl(2^{\lceil e/2\rceil}-1\bigr)\log2,
\]

\[
 Y_4(4^vp^a)=2^v\log p
 \quad(p\text{ odd prime}),
\]

and `Y_4(q)=0` otherwise.  Elementary comparison gives

\[
 \boxed{\sum_{q\ge2}\frac{Y_4(q)}{q^{3/2}}<11}
 \tag{L-91728.2}
\]

and, with `L=log(2X)`,

\[
 \boxed{\sum_{q\le X}\frac{Y_4(q)}q\le3+2L+2L^2.}
 \tag{L-91728.3}
\]

## 3. All-column mismatch/collar cost

PR #479 proves for every nonterminal physical column, including `q<K`,

\[
 |e_X(q)|<\frac{971}{4q\sqrt K}.
\]

Hence

\[
 \sum_{2\le q\le X/4}Y_4(q)|e_X(q)|
 <\frac{971}{4\sqrt K}(3+2L+2L^2)=o(1).
 \tag{L-91728.4}
\]

## 4. Native cost of the common thinning

The unused capacity created by `tau_K` has native cost at most

\[
 (1-\tau_K)J_\Lambda(X).
\]

Since `Lambda(n)<=log X` and

\[
 \sum_{n\le X}n^{-1/2}\log(X/n)<4\sqrt X,
\]

one has

\[
 J_\Lambda(X)<4\sqrt X\log X.
\]

Using `1-tau_K<130/sqrt(K)` and `sqrt(X/K)<sqrt(67)<33/4` gives

\[
 \boxed{(1-\tau_K)J_\Lambda(X)<4290\log X.}
 \tag{L-91728.5}
\]

This logarithmic native cost replaces the false bounded equality-score claim.

## 5. Knot collars and refinement

PR #479 proves that the endpoint measure is atomless and that finite activation
collars may be omitted before the split.  Choose the omitted positive packet to
have native score at most `X^-2`.  On the retained cells choose the positive
relative refinement so that it fits inside the all-column reserve and

\[
 \varepsilon_XJ_\Lambda(X)<X^{-2}.
\]

The combined collar/refinement native cost is `o(1)`.

## 6. Terminal, base and port

The fixed top and bottom omissions are positive current-owned packets.  The
finite base packet is fixed.  PR #479 gives one common port of normalized mass
below `252`, and children have zero port.  On the frozen fixed-width/base/port
estimates their total native cost is

\[
 E_{\rm term/base/port}(X)=O(1).
 \tag{L-91728.6}
\]

This is an explicit independent reconstruction input.

## 7. One-shot root bound

The final root slack is bounded by the preceding one-use charges.  Hence

\[
 \boxed{
 \delta_X\le A_0+4290\log(2X).
 }
 \tag{L-91728.7}
\]

This theorem applies only to the native factor-67 **root realization**.  It does
not assert that arbitrary positive descendants carry another finite root frame,
quantizer, collar or common port.  Their complete contribution is handled by
the positive causal envelope and the compact root-mass bound of `L-91731`.
Combining (L-91728.7) with `L-91731` gives

\[
 \boxed{
 J_\Lambda(X)-\mathcal H(d_X)
 =O(\log X)=o(\log^2X).
 }
 \tag{L-91728.8}
\]

This is compatible with
`J_Lambda(X)=4sqrt(X)-kappa_0 log(X)+O(1)` under RH.

```text
Y4 support and elementary sums                EXACT
all-column mismatch/collar native cost         o(1) / PR #479
square-root thinning native cost               <4290 log X
activation collar/refinement cost              o(1) / PR #479
fixed terminal/base/common-port cost           O(1) / FROZEN REVIEW
one-shot packet-native root slack              O(log X)
positive descendant contribution               O(1) / L-91731
complete native root deficit                   O(log X) / T-91724
Riemann Hypothesis                             UNPROVED
```
