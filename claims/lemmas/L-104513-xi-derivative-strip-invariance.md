# L-104513 — Every Xi derivative remains in the critical horizontal strip

Claim ID: `L-104513`  
Status: **PROVED UNCONDITIONALLY**  
Created: 2026-08-22  
RH status: **not assumed**

In the `t`-plane,

\[
\Xi(t)=\xi(1/2+it)
\]

has all of its zeros in the open horizontal strip

\[
|\Im t|<1/2.
\tag{L-104513.1}
\]

This is only the classical critical-strip theorem, not RH.

## Strip Gauss–Lucas lemma

Let `F` be a real entire function of order at most one whose zeros lie in

\[
|\Im z|\le H.
\]

Assume the genus-one canonical product is grouped by conjugation, so its
exponential coefficient is real. For `Im z>H`,

\[
\frac{F'(z)}{F(z)}
=
a+
\sum_\rho
\left(
\frac1{z-\rho}+\frac1\rho
\right).
\]

The constant and the grouped `1/rho` terms are real. Every remaining term has

\[
\Im\frac1{z-\rho}
=
-\frac{\Im z-\Im\rho}{|z-\rho|^2}<0.
\]

Locally uniform convergence therefore gives

\[
\Im\frac{F'(z)}{F(z)}<0
\qquad(\Im z>H).
\]

Thus `F'` has no zero above the strip. Conjugation gives the same conclusion
below it.

Applying the lemma inductively yields

\[
\boxed{
\Xi^{(k)}(z)\ne0
\qquad
(|\Im z|>1/2,\ k\ge0).
}
\tag{L-104513.2}
\]

## Consequence for the reverse-Rolle ledger

Every horizontal boundary chosen at height `H>1/2` is simultaneously zero-free
for the entire derivative ladder. All boundary transport in a fixed-height
cascade is therefore carried by the two vertical sides; no hidden horizontal
zero flux remains.
