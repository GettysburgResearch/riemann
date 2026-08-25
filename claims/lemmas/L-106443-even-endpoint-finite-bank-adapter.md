# L-106443 — Finite four-channel bank for every fixed even Xi endpoint

Claim ID: `L-106443`  
Status: **PROVED AT TRUNCATED FOURIER / REGULAR-WINDOW SCOPE; COFINAL TAIL INCLUDED FOR FIXED ORDER**  
Created: 2026-08-25  
Depends on: `L-105260`, `L-105500`, `L-106413--L-106414`, `L-106440--L-106441`  
RH status: **not assumed**

Fix one even order `K=2m`.  Truncate the positive and negative Xi Fourier
halves at `L_T=log T`, choose

\[
\lambda_TL_T={1\over200},
\]

and form the endpoint numerator and denominator of `L-106440`.

## 1. Source-exact four-channel adapter

Expansion by the signs of the two Fourier variables gives exactly four
source-owned channels:

```text
(+,+), (-,-): same-sign Hankel channels;
(+,-), (-,+): reflected Toeplitz channels.
```

The direct-sum Paley--Wiener construction of `L-106413` is insensitive to the
fixed derivative order: replacing the second endpoint by `Xi^(K)` only
multiplies its declared Fourier coordinate by the fixed monomial `u^K`.
The source support, orientation labels and channel dimension are unchanged.

With `P_(K,T)` the resulting predeclared source projection, `L-106441` gives

\[
\boxed{
\|H_{U_{0,K,T}}P_{K,T}\|_{\mathcal S_2}^2
 \le
 \left({1596808\over1568239201}+o(1)\right)
 N(T,2T)
 <\left({1\over982}+o(1)\right)N(T,2T).
}
\tag{L-106443.1}

The estimate is an upper bound for the visible negative Hardy charge only; no
absolute coverage of the companion model space is used.

## 2. Actual-Xi tail

For fixed `K`, every omitted Fourier density is a fixed polynomial in `u,v`
times the classical Xi density.  The superexponential tail estimate of
`L-106414` therefore gives

\[
\boxed{
\text{truncation error at }L_T=\log T=o(N(T,2T)).
}
\tag{L-106443.2}

No constant deteriorates with `T`.  This statement is fixed-order; no
uniformity in a growing `K(T)` is asserted.

## 3. Common and confluent events

The common-factor reduction and confluent Cauchy-index ledger of `L-105500`
and `L-106413` apply verbatim to the two endpoint companions.  Common real
multiplicity transfers directly to the parent zero count, and nonreal
confluent blocks retain their exact signed index.  They create no undeclared
positive-density analytic error.

## 4. Scope

The lemma proves the visible source payment for each fixed even endpoint.  The
unobserved signed tail remains the explicit residue Gram of `L-106442`; that
term is neither dropped nor bounded here.