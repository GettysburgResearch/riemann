# L-28103 — Fibered opposite-parity factor-five normal form

Claim ID: `L-28103`  
Title: The fixed opposite-parity factor-five transition package extends to the top source as a common-fiber matrix problem, while the RH-bearing boundary becomes the full reciprocal-free fiber  
Status: **PROPOSED EXACT SOURCE NORMAL FORM; PHYSICAL TRANSITION CERTIFICATE OPEN**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #281  
Dependencies: `L-28101`, `L-28102`; PR #269 `L-26901`--`L-26904`  
Scope: exact source organization; no factor-five physical LMI

## 1. Fixed source and top fiber

Retain the fixed source

\[
\omega_2
=
\mu-\frac32\delta_2*\mu+\frac12\delta_4*\mu
\]

and the top reciprocal-free fiber

\[
H_{K,V}
=
\ell*\mathbf1^{*(K-1)}*\mu_{>V}^{*(K-1)}.
\]

By `L-28101`,

\[
\boxed{
S_{K,V}=\omega_2*H_{K,V}.
}
\tag{L-28103.1}
\]

Write one fibered source representation as

\[
n=mh,
\qquad
m\in\operatorname{supp}\omega_2,
\quad
h\in\operatorname{supp}H_{K,V}.
\tag{L-28103.2}
\]

All collisions with the same product `n` must remain in the complete physical
Gram.

## 2. Fibered pointwise carry wavelet

For the fixed source, PR #269 defines

\[
Z_{n,m}(j)
=
\sum_{k\le n/m}\omega_2(k)\chi_{n,mk}(j)
=
g_m(n)-g_m(j)-g_m(n-j),
\tag{L-28103.3}
\]

where

\[
g_m(x)
=
\mathbf1_{m\le x<2m}
-
\frac12\mathbf1_{2m\le x<4m}.
\]

For one fixed fiber index `h`, replacing `m` by `mh` gives

\[
\boxed{
Z^{(h)}_{n,m}(j)
=
g_{mh}(n)-g_{mh}(j)-g_{mh}(n-j).
}
\tag{L-28103.4}
\]

Therefore every possible negative logarithmic Kummer transition in that fiber
lies in

\[
\boxed{
2mh\le n<5mh.
}
\tag{L-28103.5}
\]

This is an exact fiberwise localization. It does not take the sign of the
possibly signed coefficient `H_(K,V)(h)`.

## 3. Fibered transition matrices

Let `A_(n,m)` be any complete fixed-source transition matrix from the
independent-frequency physical block, including the carry transverse feature
and its boundary coordinate.

The fibered source matrix is obtained by:

1. translating both frequency variables by `log h`;
2. multiplying the two source coefficients by
   `H_(K,V)(h)` and its conjugate;
3. retaining every `h,h'` cross term.

In matrix notation this is exactly the common-fiber congruence

\[
\boxed{
A^{(K,V)}=M_{H_{K,V}}^*A\,M_{H_{K,V}}.
}
\tag{L-28103.6}
\]

Thus a full fixed-source matrix inequality lifts. A collection of rowwise scalar
signs does not suffice, because signed fiber cross terms remain.

## 4. Carry reserve and its scope

PR #269 proves an absolute carry-space Schur reserve for the pair

\[
(Z_{n,m},\,F_n),
\qquad
F_n(j)=\log\binom nj,
\]

on every sufficiently large row.

If that reserve is embedded in an exact independent-frequency physical LMI,
then `L-28102` lifts it to the complete top fiber with the same constant.

The following weaker operation is invalid:

```text
apply the scalar reserve separately for each h
and discard all h != h' cross terms.
```

Those cross terms contain the coherent Möbius hypercubes.

## 5. The lifted boundary firewall

For the fixed source, the positive first and second logarithmic carry moments
omit the unit source `m=1`. That coordinate is the bottom-charge and
fixed-ratio Mertens firewall.

After convolution with `H_(K,V)`, the unit-source boundary becomes

\[
\boxed{
\delta_1*H_{K,V}=H_{K,V}.
}
\tag{L-28103.7}
\]

It is not finite, negligible, or removable. It is precisely the complete
reciprocal-free top fiber whose multiplication by `omega_2` leaves the
rightmost-zero pole in `S_(K,V)`.

Therefore the fibered completion must estimate a physical
boundary/commutator carrying `H_(K,V)`. Pure carry-window coercivity cannot do
so: every carry window contains a zeta factor and cancels the pole.

## 6. Correct source decomposition

A production source map has the form

\[
\boxed{
I=P^{\rm trans}_{K,V}+B^{\rm fib}_{K,V}.
}
\tag{L-28103.8}
\]

The first term is the pole-canceling factor-five carry transition span. The
second retains the physical unit-source fiber and every boundary commutator
before the common zeta factor cancels.

## 7. Proof boundary

Closed exactly:

- factor-five localization in every fixed fiber;
- common-fiber matrix form of all transition rows;
- identification of the lifted unit-source boundary as `H_(K,V)`;
- the correct transverse/boundary division.

Open:

- exact production matrices for (L-28103.8);
- the fibered physical Schur reserve;
- the boundary recurrence;
- RH.
