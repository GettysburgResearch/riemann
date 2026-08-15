# L-91863 — The same-row response complement has direct native `Y_4` cost below `60989`

Claim ID: `L-91863`  
Status: **PROPOSED COMPLETE DIRECT NATIVE-COST THEOREM ON FROZEN ESTIMATES — REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: `L-91862`; exact native dual; frozen sparse-`Y_4`, all-column, terminal and omission estimates  
RH status: **unproved**

Assume `X>=10^12` and retain the single row identifier `rid_X` of `L-91861`.

## 1. Exact native deficit

For the nonnegative feasible row `d_X`, exact radix-four duality gives

\[
\boxed{
\Delta_X
:=J_\Lambda(X)-\mathcal H(d_X)
=\langle Y_4,e_X^{(4)}\rangle\ge0.
}
\tag{L-91863.1}
\]

The complement in (L-91863.1) is exactly the vector proved nonnegative in `L-91862`; no replacement row is introduced.

## 2. Common thinning: elementary absolute bound

For the Chebyshev function `psi`, the central-binomial argument gives

\[
\psi(2n)-\psi(n)\le\log {2n\choose n}\le2n\log2,
\]

and dyadic telescoping gives

\[
\psi(x)<4x\log2.
\]

Stieltjes integration then yields

\[
J_\Lambda(X)<16(\log2)\sqrt X.
\]

With `tau_K=sqrt(K)/(sqrt(K)+130)` and `K>X/67`,

\[
\boxed{(1-\tau_K)J_\Lambda(X)<12012.}
\tag{L-91863.2}
\]

This is unconditional and uses no estimate of `J_Lambda(X)-4sqrt(X)`.

## 3. Nonterminal signed comparison

The sparse dual satisfies

\[
\sum_{q\le X}\frac{Y_4(q)}q
\le3+2L+2L^2,
\qquad L=\log(2X).
\]

Pairing the all-column bulk comparison directly gives

\[
\frac{971}{4\sqrt K}(3+2L+2L^2)<4
\tag{L-91863.3}
\]

for `X>=10^12`. The identity bonus and anchored channels contribute zero comparison cost.

## 4. Terminal and omission costs

The terminal comparison is bounded by `4452q^{-3/2}` at its natural scale, while

\[
\sum_{q\ge2}\frac{Y_4(q)}{q^{3/2}}<11.
\]

Hence its complete absolute native cost is less than

\[
\boxed{4452\cdot11=48972.}
\tag{L-91863.4}
\]

The literal bottom/top omissions have combined native cost below one for `X>=10^12`. There is no auxiliary matrix port and no large-`X` base discrepancy. Whole-cell support removes activation-collar and interpolation costs from the controlling construction.

## 5. Total

The four and only four charge classes are

```text
common square-root thinning        <12012
nonterminal signed comparison      <4
terminal signed comparison         <48972
literal positive omissions         <1
-----------------------------------------
total                               <60989
```

Therefore

\[
\boxed{
0\le J_\Lambda(X)-\mathcal H(d_X)<60989.
}
\tag{L-91863.5}

Hall residualization, the row-only bonus, rough ownership, internal child placement, label erasure, and the block realization create no fifth charge: they are exact row identities before the single comparison.

## 6. Boundary

```text
same row in feasibility and Y4 pairing       exact
thinning                                      <12012
nonterminal signed comparison                 <4
terminal signed comparison                    <48972
positive omissions                            <1
bonus/anchor discrepancy                      zero
native deficit                                <60989
forbidden benchmark bridge                    absent
Riemann Hypothesis                            unproved
```
