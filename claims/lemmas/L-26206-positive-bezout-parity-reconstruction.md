# L-26206 — Positive Bézout reconstruction for the parity-paired Euler fiber

Claim ID: `L-26206`  
Status: `PROPOSED COMPLETE — exact finite filter-bank algebra pending independent review`  
Scope: fixed local two-adic source; no RH input  
Date: 2026-08-08  
Depends on: `L-26205`

Let

\[
p(z)=(1-z)(1-2z)(1-\sqrt2 z)^2.
\]

The two parity channels use `p(z)` and `p(-z)`.

## 1. Exact finite Bézout identity

Define

\[
\boxed{
\begin{aligned}
U(z)={}&\frac12
+\left(-\frac{11}{3}+\frac{7\sqrt2}{2}\right)z\\
&+\left(1+\frac{\sqrt2}{6}\right)z^2
+\left(\frac{14}{3}-3\sqrt2\right)z^3.
\end{aligned}}
\tag{L-26206.1}
\]

Then

\[
\boxed{
U(z)p(z)+U(-z)p(-z)=1.
}
\tag{L-26206.2}
\]

The identity follows by direct coefficient comparison. The left side is even; its coefficients at degrees `0,2,4,6` are respectively `1,0,0,0`.

Every coefficient of `U` is strictly positive:

\[
\frac12>0,
\qquad
\frac{21\sqrt2-22}{6}>0,
\qquad
1+\frac{\sqrt2}{6}>0,
\qquad
\frac{14-9\sqrt2}{3}>0.
\tag{L-26206.3}
\]

## 2. Perfect reconstruction of the odd Euler product

Retain

\[
B_+(s)=p(2^{-s})\mathcal O(s),
\qquad
B_-(s)=p(-2^{-s})\mathcal O(s),
\]

where

\[
\mathcal O(s)=\prod_{q\ {m odd\ prime}}(1-q^{-s}).
\]

Substituting `z=2^{-s}` in (L-26206.2) gives

\[
\boxed{
\mathcal O(s)
=U(2^{-s})B_+(s)
 +U(-2^{-s})B_-(s).
}
\tag{L-26206.4}
\]

Hence

\[
\boxed{
\frac1{\zeta(s)}
=(1-2^{-s})
\left[
 U(2^{-s})B_+(s)
 +U(-2^{-s})B_-(s)
\right].
}
\tag{L-26206.5}
\]

This is an exact finite causal reconstruction of the original inverse-zeta source from the two filtered channels. No Wiener inversion, infinite causal filter, or compact-substrip loss is required.

In physical logarithmic coordinates, only the shifts `0,log2,2log2,3log2` occur.

## 3. Critical normalization

After shifting to the centered variable `s=1/2+z`, replace `zeta=2^{-z}` and substitute `zeta/sqrt2` into (L-26206.2). The same identity gives a four-delay reconstruction of the normalized inverse-zeta signal from the normalized parity-paired fibers.

Thus the paired block criterion can be proved directly by finite block comparison; the analytic lower multiplier bound of `L-26205` is an independent check rather than the only reconstruction path.

## 4. Exact coefficient budget

Put

\[
U(z)=\sum_{j=0}^3u_jz^j.
\]

Then

\[
\boxed{
2\sum_{j=0}^3u_j^2
=\frac{2845}{18}-\frac{320\sqrt2}{3}.
}
\tag{L-26206.6}
\]

Moreover,

\[
\boxed{
\frac{45}{4}
-2\sum_{j=0}^3u_j^2
=\frac{5(768\sqrt2-1057)}{36}>0.
}
\tag{L-26206.7}
\]

The numerical values are approximately

\[
2\sum u_j^2=7.2061089024\ldots,
\qquad
\frac{45}{4}-2\sum u_j^2=4.0438910975\ldots.
\]

Equation (L-26206.7) is a useful normalization check for a future block Schur ledger. It is **not by itself** a contraction theorem: analysis and synthesis constants enter different operator positions, and arbitrary rescaling would change them reciprocally.

## 5. Why this matters for production

The paired source is now a finite perfect-reconstruction filter bank:

```text
analysis:    p(z), p(-z);
synthesis:   U(z), U(-z);
reserve:     |p(z)|^2+|p(-z)|^2 >=45/4;
delays:      at most three in synthesis.
```

A production reflected proof therefore does not need to guess an inverse source map. It must only decide whether the actual two-frequency Selberg ledger leaves a strict positive reserve after every finite synthesis boundary row is charged.

## 6. Proof boundary

Closed exactly:

- the positive-coefficient Bézout polynomial;
- finite reconstruction of the odd Euler product and `1/zeta`;
- the four-delay physical source map;
- the exact coefficient budget.

Not closed:

- a physical-block Schur reserve;
- a charge sum below that reserve;
- `PEFRC`;
- RH.
