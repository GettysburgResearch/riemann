# R-105390 — Growing-prefix domination does not control the omitted critical tail

Claim ID: `R-105390`  
Status: **PROVED EXACT SCOPE REFUTATION**  
Created: 2026-08-23  
Depends on: `T-105390`, `T-105371`  
RH status: **not assumed**

The growing-prefix theorem is a localization result, not a complete capacity
theorem.

## Exact matrix separator

Let the source matrix be

\[
A=I_2.
\]

Let a controlled prefix consume

\[
C_{\rm prefix}={2\over5}I_2.
\]

Then

\[
A-C_{\rm prefix}={3\over5}I_2\succ0.
\tag{R-105390.1}
\]

Now let the omitted tail contribute

\[
C_{\rm tail}={7\over10}I_2.
\]

The complete critical matrix is

\[
C=C_{\rm prefix}+C_{\rm tail}={11\over10}I_2,
\]

and therefore

\[
\boxed{
A-C=-{1\over10}I_2\prec0.
}
\tag{R-105390.2}
\]

Thus an arbitrarily large, perfectly controlled positive prefix reserve does
not constrain a separately omitted positive tail.

## Consequence for T-105390

`T-105390` proves that the first `r^(gamma_k)` actual Xi critical pairs do not
overfill the fixed order-`k` source matrix. It does not imply

```text
OSCC105371;
BRP105220;
or RH.
```

A valid continuation must estimate the complete omitted critical tail or prove
an exact transport/cancellation theorem that incorporates it. It may not infer
tail smallness merely from the safety of the growing central prefix.

## Scope

The separator is abstract finite-dimensional linear algebra, not an Xi
counterexample. It proves that no source-free logical implication from prefix
capacity to complete capacity exists. Special Xi structure may still control
the tail, but that control is the open theorem.
