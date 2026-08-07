# R-23002 — Generic critical-cluster operator closure fails

Claim ID: `R-23002`  
Title: The remaining signed-correlation gate cannot be closed by a uniform Farey-cluster operator norm or by deleting finitely many cells  
Status: **PROVED SCOPE CORRECTION, STACKED ON THE EXACT REFUTATION IN PR #231**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Dependencies: PR #231 `R-22802`; `L-23003`; `T-23002`  
Scope: proposed completions of `L-23002` and `T-23001`

## 1. The false shortcut

A natural attempted closure is to localize all reduced Farey frequencies into
critical cells of width `1/D`, view physical localization as a cluster matrix,
and prove a uniform estimate

\[
 \|\mathcal C_D\|=D^{o(1)}.
 \tag{R-23002.1}
\]

Such an estimate, combined with the `O(D)` Bohr/Jordan energy, would give the
critical local moment by Cauchy--Schwarz.

This shortcut is false.

## 2. Exact row obstruction

PR #231 proves that for every fixed positive cell index `k`, the numerator
`a=1` produces an entry of order one for a positive proportion of all
 denominators

\[
 \frac{D}{k+1/2}<q\le\frac{D}{k-1/2}.
\]

Consequently that row has Euclidean norm at least

\[
 c_k\sqrt D,
\]

and therefore

\[
\boxed{
 \|\mathcal C_D\|\ge c_k\sqrt D.
}
\tag{R-23002.2}
\]

Removing any fixed finite collection of rows does not help: the same argument
applies to the first retained fixed positive row.

Thus (R-23002.1) cannot hold.

## 3. The obstruction is not an artifact of arbitrary vectors

`L-23003` shows that for the actual Möbius coefficient vector the first positive
cell is

\[
 B_{D,1}
 =\left(\frac{i}{2\pi}+\frac1{2\pi^2}\right)
 [M(D)-M(2D/3)].
\]

Therefore the coherent row is not merely a worst-case direction irrelevant to
arithmetic.  It is exactly an RH-equivalent Mertens increment.

The correct scalar estimate may still be true because the Möbius signs and the
completed endpoint channel can cancel across the full physical form.  But that
cancellation is absent from a uniform operator norm and is destroyed by
Cauchy--Schwarz over arbitrary coefficient vectors.

## 4. Consequences for proposed proofs

The following implication is invalid:

```text
Bohr/Jordan energy O(D)
+ generic critical-cluster operator D^o(1)
=> physical local energy O(D^(2+epsilon)).
```

The operator premise is false.

A valid completion must retain, before any absolute value or arbitrary-vector
norm:

1. the signs `mu(d)`;
2. the divisor coupling in `U_q(D),V_q(D)`;
3. the endpoint channels `M_D/3` and `x^2 R_D`;
4. the common signed cell contraction;
5. or an equivalent physical-space identity.

Likewise, the compact stop-loss positive-Hankel shortcut is independently
refuted by `R-23001`.

## 5. Correct surviving target

The strongest scalar statement currently isolated is

\[
\boxed{
 \int_{D/2}^{D}
 \left|
  1+S_D(x)+\frac{M_D}{3}+x^2R_D
 \right|^2dx
 \ll_\varepsilon
 D^{1+\varepsilon}(1+\mathcal B_D),
}
\tag{R-23002.3}
\]

for the **specific completed Möbius packet**.  Since `mathcal B_D<<D`, this
would imply the analytic-totient second-moment criterion and RH.

No proof of (R-23002.3) is supplied here.

## 6. Status boundary

This refutation narrows the search and protects the review boundary.  It does
not refute the scalar Möbius-specific estimate and does not prove RH.
