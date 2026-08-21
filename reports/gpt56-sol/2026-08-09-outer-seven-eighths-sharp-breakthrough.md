# Outer-seven-eighths SHARP breakthrough

Status: **NEW COMPLETE PARTIAL THEOREM / INNER EIGHTH REMAINS RH-BEARING**

## Result

For the square-root hinge

\[
h_T(q)=q^{-1/2}-T^{-1/2}
\]

and its unique average-carry triangular inverse `c_T(j)`, the new theorem `L-32304` proves

\[
\boxed{c_T(j)>0\qquad(2\le j<T,\ j>T/8).}
\]

Thus any failure of SHARP is confined to the inner eighth `j<=T/8`.

## Mechanism

Let

\[
u_T(m)=\sum_{k\le T/m}\mu(k)h_T(mk),\qquad
S_T(j)=\sum_{m\ge j}u_T(m).
\]

The exact inverse formula collapses to

\[
\boxed{
jc_T(j)=(j+2)u_T(j)-ju_T(j+1)+\frac{2S_T(j)}{j-1}.}
\]

For `j>T/8`, only quotient cells `K=floor(T/j)<=7` occur. Their Mobius states are explicit affine functions of `j^-1/2` and `T^-1/2` determined by `mu(1),...,mu(7)`.

Every one of those states is positive. A fixed top-half tail contributes

\[
S_T(j)>\frac3{40}\sqrt T
\]

for `T>=40`. This pays the local negative drift in cells `K=5,6,7`. The only adverse quotient transition is `K=6 -> 5`, because `mu(6)=+1`; its complete loss is `<1/(2sqrt T)`, leaving the explicit margin `8/(45sqrt T)`.

The finite base `3<=T<40` is certified by directed integer-square inverse-root intervals in `X-32302`.

## Why this matters

PR #332 had proved only the generic top-half theorem `j>T/2`. The present proof crosses six additional quotient interfaces and reaches the first genuine arithmetic wall: at quotient `K=8` the Mobius state itself can become negative.

This is not finite extrapolation and does not use RH. It identifies precisely where the square-root source first needs correlated Mertens cancellation.

## Current frontier

```text
j > T/8              PROVED STRICTLY POSITIVE
j <= T/8             OPEN
5 c_T(2)+3 c_T(3)    zero-safe RH scalar / sign open
full SHARP            open
RH                    unproved
```

The preferred next attack is not another global positivity heuristic. It is either:

1. a correlated tail estimate beginning at quotient cell `K=8`; or
2. the much weaker zero-safe low-row scalar from PR #326.
