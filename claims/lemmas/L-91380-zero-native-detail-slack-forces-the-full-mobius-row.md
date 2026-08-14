# L-91380 — Zero native detail slack forces the full Möbius row

Claim ID: `L-91380`  
Status: **PROVED EXACT INJECTIVITY / NO-SHORTCUT THEOREM**  
Created: 2026-08-14  
Depends on: the average-binomial carry matrix and `L-91377`  
RH status: **unproved**

## 1. Ordinary carry map is triangular and injective

For a finite row `d(n)`, `2<=n<=X`, its ordinary response is

\[
 C_d(q)=\sum_{n=q}^{X}\beta_{nq}d(n).
\]

The carry matrix is triangular in decreasing index. Its diagonal is

\[
\boxed{
 \beta_{qq}=\frac{q-1}{q+1}>0.
}
\tag{L-91380.1}
\]

Hence `d -> C_d` is injective: recover `d(X)` from `C_d(X)`, then descend in
`q`.

## 2. Radix-four transform is injective

For a finite ordinary vector `C`, put

\[
 \Xi(q)=C(q)-2C(4q).
\]

The inverse is the finite positive renewal

\[
\boxed{
 C(q)=\sum_{k\ge0}2^k\Xi(4^kq),
}
\tag{L-91380.2}
\]

where terms beyond `X` vanish. Thus `C -> Xi` is injective as well.

## 3. Exact saturation theorem

Suppose a finite row `d` has zero native detail slack:

\[
\boxed{
 \Xi_d(q)=\Omega_X(q)
 \qquad\text{for every }q.
}
\tag{L-91380.3}
\]

Equation (L-91380.2) gives

\[
 C_d(q)=w_X(q).
\]

By `L-91377`, the full Möbius row `c_X` has the same ordinary response. The
injectivity of Section 1 therefore yields

\[
\boxed{
 d=c_X.
}
\tag{L-91380.4}
\]

## 4. Consequence

A nonnegative exact-saturation packing exists if and only if the full native
Möbius row itself is nonnegative. Consequently exact zero slack is not a
simpler CFFP target.

The viable reset target is a nonnegative row with controlled **positive**
slack:

\[
0\le
\sum_qY_4(q)[\Omega_X(q)-\Xi_d(q)]
=o(\log^2X),
\]

or the stronger uniform bound supplied by NRCT.

```text
ordinary carry injectivity               EXACT
radix-four renewal injectivity            EXACT
zero detail slack -> full Möbius row      EXACT
zero-slack positive shortcut              EQUIVALENT TO NATIVE ROW SIGN
bounded positive-slack reset              OPEN / RH-BEARING
Riemann Hypothesis                        UNPROVEN
```
