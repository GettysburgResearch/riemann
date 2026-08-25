# L-106441 — Safe inner phases have zero adverse tail, but derivative companions are a different divisor

Claim ID: `L-106441`  
Status: **EXACT HARDY CONSEQUENCE + BINDING COMPANION FIREWALL**  
Created: 2026-08-25  
Depends on: `L-106440`; PR #729 `L-105627/L-105632` at observed head `4150f96e3d410de1724303c60d72a000c1ff05e0`  
RH status: **not assumed**

## 1. Safe vertical-shift all-pass

Let `F` be a real entire function and put

\[
V_H(x)={F(x-iH)\over F(x+iH)}.
\]

If every zero of `F(z+iH)` lies in the closed lower half-plane and the
canonical exponential factor has the inner orientation, then `V_H` is inner in
`C_+`. Equations `L-106440.10` and `L-105632` consequently give, for every
hard bandwidth and every predeclared source projection,

\[
\boxed{
\Delta_H^{\rm out}(V_H)\le0,
\qquad
\mathcal D_P(V_H)\le0.
}
\tag{L-106441.1}
\]

PR #729 proves this innerness assertion for

\[
V_H(x)={\Xi'(x-iH)\over\Xi'(x+iH)}
\]

throughout its zero-free safe region `H>=beta_1`, subject to the independent
review status recorded on that branch. Once that input is accepted, no
absolute Paley--Wiener coverage theorem is needed anywhere in the safe region.

## 2. The endpoint derivative companion is not a vertical shift

The endpoint block on the present branch uses

\[
\Theta_{\lambda,F}(x)
 ={F(x)-i\lambda F'(x)\over F(x)+i\lambda F'(x)},
\tag{L-106441.2}
\]

not `V_lambda`. The two multipliers agree only to first order in a formal
Taylor expansion and have different zero divisors.

The distinction is already exact for

\[
F(z)=z^2+\varepsilon^2,
\qquad \varepsilon>0.
\]

For every `H>varepsilon`,

\[
{F(z-iH)\over F(z+iH)}
\]

is inner: both zeros of the denominator lie in the lower half-plane.
By contrast,

\[
F(z)+i\lambda F'(z)
 =z^2+2i\lambda z+\varepsilon^2
\]

has the two zeros

\[
\boxed{
 i\bigl(\sqrt{\lambda^2+\varepsilon^2}-\lambda\bigr),
\qquad
-i\bigl(\sqrt{\lambda^2+\varepsilon^2}+\lambda\bigr).
}
\tag{L-106441.3}
\]

One lies in each open half-plane. After writing

\[
a=\sqrt{\lambda^2+\varepsilon^2}+\lambda,
\qquad
b=\sqrt{\lambda^2+\varepsilon^2}-\lambda,
\]

the derivative companion factors as

\[
\boxed{
\Theta_{\lambda,F}(z)
 ={(z-ia)(z+ib)\over(z+ia)(z-ib)}.
}
\tag{L-106441.4}
\]

It is one inner factor divided by another and is not inner, although the safe
vertical-shift quotient is.

Thus the implication

```text
safe vertical-shift innerness
 -> endpoint derivative-companion innerness
```

is false even for a real quadratic.

## 3. Exact bridge that would be sufficient

Let the endpoint symbol have a source-exact factorization

\[
U_T=V_TW_T,
\]

where `V_T` is an authenticated inner factor and `W_T` retains every remaining
zero and pole. Innerness proves the favorable sign only for `V_T`; a truncated
signed tail is not multiplicative, so one must also retain the Toeplitz
commutator created by the product. Equivalently, a valid bridge must provide
one of:

```text
an exact block-diagonal realization of the two factors;
a signed product-cocycle estimate at the declared bandwidth;
a zero-crossing-free homotopy from the derivative companion to the safe
vertical-shift companion.
```

No such bridge is inferred from Taylor approximation or source-norm closeness.
A narrow Blaschke dipole can change the partial index while remaining small in
ordinary norm.

## 4. Consequence for the live programme

The safe-region result of PR #729 removes adverse signed tails for the literal
vertical-shift Xi-prime phase. The present endpoint programme is therefore
reduced to two sharply typed tasks:

1. construct a source-exact safe/unsafe factor or homotopy for the **finite-alpha
   derivative companion**;
2. estimate the spectral outer tail and in-band hole of the unsafe residue by
   `L-106440`.

This is narrower than the former absolute sampling theorem, but it is not yet a
proof of `SIGNEDTAIL106430`.