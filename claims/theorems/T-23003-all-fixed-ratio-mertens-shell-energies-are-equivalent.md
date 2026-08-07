# T-23003 — All fixed-ratio Mertens shell energies are equivalent

Claim ID: `T-23003`  
Title: One fixed-ratio shell energy theorem controls every other ratio, including the dyadic Euler-aligned shell and the exact `2/3` first Farey cell  
Status: **PROPOSED EXACT COMPOSITION THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Dependencies: `L-23008`; PR #229 `L-23003/T-23002`; PR #234 `T-23401/L-23405`  
Scope: exact scalar bridge; no packet-level Heath--Brown decoder is asserted

## 1. Cumulative shell exponent

For a fixed `0<c<1`, define `Q_c` and `A_c` as in `L-23008` and put

\[
\Theta_c
=
\limsup_{X\to\infty}
{\log(1+\mathcal A_c(X))\over2X}.
\tag{T-23003.1}

The two-sided constant comparisons `L-23008.13`--`L-23008.14` immediately give

\[
\boxed{
\Theta_c=\Theta_d
\qquad(0<c,d<1).}
\tag{T-23003.2}

Thus the growth exponent is independent of the fixed shell ratio.

## 2. Block formulation

For a fixed block width `B>0`, let

\[
E_{c,B}(J)
=
\int_J^{J+B}|Q_c(t)|^2dt.
\tag{T-23003.3}

The following are equivalent for one, hence every, fixed ratio:

1. `A_c(X)=exp(o(X))`;
2. `E_(c,B)(J)=exp(o(J))` for every fixed `B`;
3. `E_(c,1)(J)=exp(o(J))`.

Indeed a block is bounded by the cumulative energy, while a sum of `O(X)`
subexponential unit blocks is still `exp(o(X))`.

Combining this observation with (T-23003.2) gives

\[
\boxed{
E_{c,B}(J)=e^{o(J)}
\quad\Longleftrightarrow\quad
E_{d,B}(J)=e^{o(J)}.}
\tag{T-23003.4}

No loss depending on the output scale occurs.

## 3. Dyadic shell versus first Farey cell

Take

\[
d=\frac12,
\qquad
c=\frac23.
\]

The dyadic shell is

\[
I_{1/2}(x)=M(x)-M(x/2),
\]

and has the Euler-aligned multiplicative structure of PR #234 `L-23405`.
The exact first positive Farey cell of PR #229 is a nonzero fixed complex
multiple of

\[
I_{2/3}(D)=M(D)-M(\lfloor2D/3\rfloor).
\]

`L-23008` gives the explicit causal transfer

\[
\boxed{
Q_{2/3}(t)
=
\sum_{k\ge0}2^{-k/2}
\left[
 Q_{1/2}(t-k\log2)
 -\sqrt{\frac23}\,
  Q_{1/2}\!\left(t-\log\frac32-k\log2\right)
\right].}
\tag{T-23003.5}

Its total-variation norm is at most

\[
{1+\sqrt{2/3}\over1-1/\sqrt2}.
\tag{T-23003.6}

The reverse filter is

\[
\boxed{
Q_{1/2}(t)
=
\sum_{j\ge0}(2/3)^{j/2}
\left[
 Q_{2/3}\!\left(t-j\log\frac32\right)
 -{1\over\sqrt2}
  Q_{2/3}\!\left(t-\log2-j\log\frac32\right)
\right].}
\tag{T-23003.7}

Therefore the dyadic energy theorem and the first-Farey-cell energy theorem are
exactly equivalent at the required exponential scale.

## 4. RH conclusion from the aligned ratio

PR #234 `T-23401` identifies the fixed-ratio shell exponent with the
rightmost-zero displacement.  Equivalently, the Mellin transform

\[
\int_1^\infty I_c(x)x^{-s-1}dx
={1-c^s\over s\zeta(s)}
\tag{T-23003.8}

has a numerator with zeros only on `Re s=0`.

Consequently any proof of

\[
\boxed{
E_{1/2,B}(J)=e^{o(J)}}
\tag{T-23003.9}

for one fixed `B>0` gives

\[
E_{2/3,B}(J)=e^{o(J)},
\]

then the square-root first-cell Mertens bound and

\[
\boxed{\mathrm{RH}.}
\tag{T-23003.10}

Conversely RH gives (T-23003.9).

Thus the positive inverse coefficients, positive generalized von Mangoldt
weights, reflected Selberg square, and digital recurrence available only at the
dyadic ratio may be used without losing the mandatory `2/3` audit coordinate.

## 5. What this repairs

The corrected high-order packet proposals properly declined to claim an exact
map

```text
balanced packet -> Delta_(2/3)^K M.
```

The present theorem does not restore that false map.  It supplies a different,
fully explicit scalar bridge:

```text
dyadic shell theorem
 -> causal l1 transfer
 -> exact 2/3 first-cell theorem.
```

A final proof may therefore work entirely in the Euler-aligned `c=1/2`
coordinate and export the first-cell consequence through (T-23003.5), rather
than through an unproved packet mutation.

## 6. Exact remaining theorem

After this bridge, the scalar completion is only

\[
\boxed{
\int_J^{J+B}
 e^{-t}|M(e^t)-M(e^t/2)|^2dt
=e^{o(J)}.}
\tag{T-23003.11}

The dyadic coefficient is the bounded multiplicative function

\[
b_2(n)=\mu(n)-\mathbf1_{2\mid n}\mu(n/2),
\]

whose inverse coefficients and generalized Selberg forcing are nonnegative and
whose centered dual recurrence has the digital kernel of PR #234 `L-23406`.

No proof of (T-23003.11) is supplied here.

## 7. Proof boundary

Closed exactly:

- ratio independence of the cumulative shell exponent;
- equivalence of fixed block and cumulative subexponential energies;
- the explicit mutually inverse dyadic/first-Farey causal filters;
- transfer of any dyadic proof to the required Mertens first cell and RH.

Open:

- the dyadic shell energy estimate (T-23003.11);
- RH.
