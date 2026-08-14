# L-91385 — The zero row gives logarithmic proportional debt for every positive typed causal packet

Claim ID: `L-91385`  
Status: **PROVED EXACT GENERATOR BOUND — POSITIVE TYPED ENTRY SEPARATE**  
Created: 2026-08-14  
Depends on: positive component packets  
RH status: **unproved**

## 1. Component entropy bound

For `Y>=1`, let

\[
 E(Y)=\sum_{2\le n\le Y}
 \frac{\log n}{\sqrt n}\log(Y/n)
\]

be the literal entropy of the positive component row and put

\[
 T(Y)=4\sqrt Y-3.
\]

Since `log n<=log Y`,

\[
 E(Y)\le(\log Y)
 \sum_{n\le Y}n^{-1/2}\log(Y/n).
\]

The summand is decreasing in `n`, and integral comparison gives

\[
 \sum_{n\le Y}n^{-1/2}\log(Y/n)
 \le4\sqrt Y-4-\log Y<4\sqrt Y.
\]

Also `T(Y)>=sqrt(Y)`.  Hence

\[
\boxed{
 E(Y)\le4T(Y)\log(3Y).
}
\tag{L-91385.1}
\]

## 2. Causal residual

Let `p>=67`, `r=p^-1/2`, and define the positive typed causal packet

\[
 G_{p,Y}=P_Y-rP_{Y/p}
\]

with causal zero extension.  Its target is

\[
 T_p(Y)=T(Y)-rT(Y/p).
\]

When the child is active,

\[
 T_p(Y)\ge(1-r^2)T(Y)
 \ge\frac{66}{67}T(Y).
\tag{L-91385.2}
\]

The positive part of the residual literal benchmark is at most `E(Y)`.  Thus

\[
\boxed{
 [E(Y)-rE(Y/p)]_+
 \le5\log(3Y)\,T_p(Y).
}
\tag{L-91385.3}
\]

The constant five is deliberately conservative.

## 3. Zero-row producer

All ordinary, radix-four and boundary capacities of a positive typed causal
packet are nonnegative.  The zero row is therefore feasible.  Its deficit is
the positive part of the packet benchmark, and (L-91385.3) gives

\[
\boxed{
 \Delta(G_{p,Y})
 \le5\log(3Y)\,m(G_{p,Y}),
 \qquad m:=T.
}
\tag{L-91385.4}
\]

Integrating over any finite positive source measure preserves the bound with
`log(3Y)` replaced by the logarithm of the parent scale.

## 4. Meaning

The constant-debt theorem is not necessary in a strictly subcritical branching
architecture.  Logarithmic debt per unit target mass is already sufficient.

This lemma does not construct the exact positive typed entry of the native
signed arithmetic packet or prove that its child ledger is measured by the same
`T` mass.
