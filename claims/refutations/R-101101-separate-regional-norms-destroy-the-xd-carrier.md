# R-101101 — Separate regional norms destroy the XD carrier cancellation

Claim ID: `R-101101`  
Status: **PROVED EXACT NO-GO**  
Created: 2026-08-21  
Depends on: `L-101101`  
RH status: **unproved**

Let `P>0`, and take the exact two-coordinate fixture

\[
v=(-P,+P).
\]

Then the physical sum is zero:

\[
\langle v,e_+\rangle=0.
\]

Nevertheless

\[
|v_1|+|v_2|=2P,
\qquad
\|v\|_2^2=2P^2.
\]

Thus no estimate obtained by taking absolute values, positive edge variation,
or independent Hilbert norms of the two regions can recover the cancellation
in the physical sum.

The fixture is not artificial at the scale level: `L-100710--L-100711` prove
that it is the leading asymptotic vector of the literal short/long source
partition.

Therefore the implication

```text
short regional energy + long regional one-sided estimate -> XD
```

is unusable when the short norm is taken before carrier projection. The
carrier-preserving projection of `L-101101` is mandatory.
