# L-32409 — Bézout current reconstruction leaves only a strictly delayed odd-core state plus a compact even gauge

Claim ID: `L-32409`  
Title: Differentiating the exact parity Bézout reconstruction of `1/zeta` produces no current-scale boundary: the derivative gauge is one dyadically delayed odd-core source plus three even delayed copies of the reconstructed Möbius source  
Status: **PROPOSED COMPLETE EXACT FILTER/CURRENT LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-09-s`  
Created: 2026-08-09  
Dependencies: PR #263 `L-26205/L-26206`; `L-32408`  
Scope: exact physical-source algebra; no global energy recurrence or RH conclusion

## 1. Exact parity reconstruction

Put

\[
z=2^{-s},\qquad L=\log2,
\]

\[
p(z)=(1-z)(1-2z)(1-\sqrt2z)^2,
\]

and

\[
\mathcal O(s)=\prod_{p\ {m odd}}(1-p^{-s}).
\]

The parity sources are

\[
B_+(s)=p(z)\mathcal O(s),\qquad
B_-(s)=p(-z)\mathcal O(s).
\]

Let `U` be the positive cubic Bézout polynomial of `L-26206`, so

\[
U(z)p(z)+U(-z)p(-z)=1.
\]

Define

\[
V_+(z)=(1-z)U(z),\qquad V_-(z)=(1-z)U(-z).
\]

Then

\[
\boxed{
B_0(s):={1\over\zeta(s)}
=V_+(z)B_+(s)+V_-(z)B_-(s).
}
\tag{L-32409.1}

For each source write its logarithmic current as the ordinary `s` derivative,

\[
q_0=B_0',\qquad q_+=B_+',\qquad q_-=B_-'.
\tag{L-32409.2}

(`q=-b\log` in coefficient notation.)

## 2. Differentiate before estimating

Since

\[
{dz\over ds}=-Lz,
\]

differentiating (L-32409.1) gives exactly

\[
\boxed{
q_0
=V_+(z)q_+ +V_-(z)q_- +\mathcal G(z,s),
}
\tag{L-32409.3}

where

\[
\mathcal G
=-Lz\left[V_+'(z)p(z)+V_-'(z)p(-z)\right]\mathcal O(s).
\tag{L-32409.4}

No triangle inequality or block localization has entered.

## 3. Exact factorization of the derivative gauge

Direct coefficient algebra with the explicit `U` gives

\[
-\left[V_+'(z)p(z)+V_-'(z)p(-z)\right]
=1+(1-z)Q(z),
\tag{L-32409.5}

with the odd polynomial

\[
\boxed{
Q(z)
={z\over3}\left[
 (6+17\sqrt2)
 -36\sqrt2\,z^2
 +(24+4\sqrt2)z^4
\right].
}
\tag{L-32409.6}

Because

\[
B_0=(1-z)\mathcal O,
\]

(L-32409.4)--(L-32409.6) become

\[
\boxed{
\mathcal G
=Lz\,\mathcal O(s)
+LzQ(z)B_0(s).
}
\tag{L-32409.7}

Moreover

\[
\boxed{
 zQ(z)
 ={6+17\sqrt2\over3}z^2
 -12\sqrt2\,z^4
 +{24+4\sqrt2\over3}z^6.
}
\tag{L-32409.8}

Thus the complete differentiated reconstruction is

\[
\boxed{
\begin{aligned}
q_0={}&V_+q_+ +V_-q_-\\
&+Lz\,\mathcal O\\
&+L\left[
 {6+17\sqrt2\over3}z^2
 -12\sqrt2 z^4
 +{24+4\sqrt2\over3}z^6
 \right]B_0.
\end{aligned}}
\tag{L-32409.9}

There is **no zero-delay reconstructed boundary term**.

## 4. Physical meaning

In centered logarithmic coordinates `s=1/2+it`, multiplication by `z^r` is translation by `r log 2` with critical amplitude `2^{-r/2}`.

Hence (L-32409.9) has the exact causal routing

```text
parity currents q_+, q_-
 -> finite synthesized current;

derivative gauge
 -> one odd-core state delayed by log 2;
 -> reconstructed Mobius boundaries delayed by
      2 log 2, 4 log 2, 6 log 2.
```

The compact even-delay boundary is precisely of the source type closed at carry-row scope by `L-32408`; it is not a new arithmetic source.

The odd Euler core obeys the exact one-step identity

\[
\boxed{
\mathcal O(s)=B_0(s)+z\mathcal O(s).
}
\tag{L-32409.10}

Thus the only new state species created by differentiation is one strict dyadic-delay odd-core state. On the critical line its delay amplitude is `2^{-1/2}`. Equation (L-32409.10) is an exact source identity, not by itself an energy-contraction theorem.

## 5. Why this advances the physical recurrence

Before differentiating the reconstruction, the plus/minus unweighted boundaries collapse to `B_0` by `L-32408`. Equation (L-32409.9) shows that the logarithmic current introduces no diffuse same-scale replacement:

```text
same-scale arithmetic current
    = finite parity current synthesis;

new gauge
    = strictly delayed odd core
      + compact even delayed B_0 boundary.
```

All delays are exact integer multiples of `log 2`, so no fractional block collar is created. A source-convolved independent-frequency proof may therefore keep the complete cross terms and charge only finitely many predecessor blocks plus the one odd-core state.

## 6. Proof boundary

Closed exactly here:

1. current-level differentiation of the parity perfect reconstruction;
2. explicit polynomial factorization of the derivative gauge;
3. absence of any zero-delay boundary term;
4. reduction of the compact gauge to three even dyadic delays of `B_0`;
5. exact one-delay recursion for the odd Euler core.

Open:

1. the Hermitian source-convolved block inequality which pays the finite delayed `B_0` gauges without double spending the paired reserve;
2. propagation/absorption of the delayed odd-core state in one global energy ledger;
3. RH.
