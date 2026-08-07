# R-15114 — `CP(K)` is the RH-bearing Möbius theorem, not a completed Type-II lemma

Claim ID: `R-15114`  
Title: The high-order centered packet retains an exact Möbius slice, so packet bookkeeping and standard norm inequalities do not complete `CP(K)`  
Status: **PROPOSED EXACT SCOPE REFUTATION PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Frozen target: PR #158 at `9ee33527aef3acbb281ebad367aeb1e51652d006`  
Dependencies: `L-15159`, `T-15123`; the packet schema of `L-15156/M-15112`  
Scope: refutes only the claim that the current proposal is review-ready without proving `CP(K)`; it does not refute the possibility of proving `CP(K)`

## 1. The question

The high-order proposal `M-15112` isolates one remaining theorem, called
`CP(K)`, asserting centered Type-I/Type-II packet recurrences with a coefficient
rate tending to zero. The question is whether this theorem is merely a technical
closure step that can be omitted before review.

It cannot.

## 2. Exact packet decoder

`L-15159` proves that the packet coefficient before the logarithmic factor is

\[
 A_{K,V}=\mu
 \qquad\text{through }V^K.
 \tag{R-15114.1}
\]

Consequently:

- after convolution with `log`, the recombined packet is exactly `Lambda`;
- after fixing the logarithmic variable at `q0`, the remaining packet is exactly
  `mu(m) log(q0)`.

At `q0=2`, the corresponding compact-window signal is a fixed translate and
nonzero scalar multiple of the Möbius safe signal.

## 3. The Möbius slice is RH-equivalent

`T-15123` gives

\[
 \Theta_\zeta
 =\limsup_{X\to\infty}
 {\log(1+E_{\mu,H}(X))\over2X},
 \tag{R-15114.2}
\]

where `E_(mu,H)` is the positive cumulative energy of the Möbius safe signal.
Thus

\[
 E_{\mu,H}(X)=\exp(o(X))
 \quad\Longleftrightarrow\quad
 \mathrm{RH}.
 \tag{R-15114.3}
\]

The fixed-`q0` Heath–Brown slice has the same exponent.

## 4. Finite packetization cannot hide the exponent

If a fixed-`q0` slice is divided into `R_K` destination packets with self-energies
`E_(K,tau)`, then

\[
 \max_\tau E_{K,\tau}
 \ge {E_{\mu,q_0}\over R_K^2}.
 \tag{R-15114.4}
\]

For fixed `K`, `R_K` is constant with respect to the block scale. Hence at least
one destination packet retains the full upper exponential exponent of the
Möbius source.

High identity order can reorganize the arithmetic source, expose factor
scales, and reduce combinatorial losses. It does not turn every packet into a
strictly easier source by algebra alone.

## 5. Why generic Type-II inequalities do not close the gap

The exact factorization supplies no external oscillatory parameter and no
modulus average. A balanced multiplicative convolution has factor logarithmic
scales whose sum is the output scale. Standard Cauchy, Young, Schur, or
large-sieve bounds applied after total variation either:

1. lose the signed binomial reconstruction;
2. pay the full output-scale mass;
3. or bound a local Möbius moment whose subexponential control is itself an
   RH-equivalent statement.

The fixed reserve of `L-15157` and the zero combinatorial rate of `L-15158` are
useful, but neither supplies the missing arithmetic cancellation.

This is consistent with current local-moment formulations of the Möbius
criterion: arbitrarily high critical-scale local moments recover the Mertens
bound, but those moment estimates are equivalent criteria rather than known
unconditional bounds.

## 6. Necessity statement

For the exact chain in `M-15112`:

\[
 \boxed{
 \text{`CP(K)` is necessary, or it must be replaced by a theorem of the same
 Möbius-energy strength.}}
 \tag{R-15114.5}
\]

It is not logically necessary for every possible proof of RH. One may instead
prove directly:

\[
 E_{\mu,H}(X)=\exp(o(X)),
\]

or the original prime/von-Mangoldt safe-energy bound. But each such replacement
already settles the same rightmost-zero exponent.

Therefore the current high-order packet work is **not a full proof proposal
ready for scarce independent-review time** while `CP(K)` remains open.

## 7. What survives

This scope correction does not affect:

- the safe-filter Hardy transfer;
- the prime/full-`Lambda` normal bridge;
- the high-order null quotient;
- the exact finite Heath–Brown identity;
- the first-crossing partition;
- the finite auxiliary-energy composition theorems;
- the exact regressions.

Those remain independently reviewable mathematical infrastructure.

## 8. Classification

```text
finite packet algebra and schemas:  PROPOSED / REVIEWABLE
CP(K) analytic estimate:            OPEN / RH-BEARING
M-15112 as a completed proposal:    BLOCKED
RH:                                  NOT PROVED
```
