# L-32408 — Bézout-reconstructed Möbius boundary is absorbed with coefficient one

Claim ID: `L-32408`  
Title: After complete parity Bézout synthesis, the diffuse unweighted Euler boundaries collapse to the original Möbius source, whose complete carry energy is dominated rowwise by the paired Selberg reserve except at one fixed bottom row  
Status: **PROPOSED COMPLETE EXACT FINITE/COFINAL LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-09-s`  
Created: 2026-08-09  
Dependencies: PR #263 `L-26205/L-26206`; `L-32406/L-32407`; `X-32402`  
Scope: fully synthesized unweighted carry boundary; source-convolved physical localization remains separate

## 1. Full synthesis must precede the boundary norm

Retain the two parity sources

\[
B_+(s)=p(2^{-s})\mathcal O(s),\qquad
B_-(s)=p(-2^{-s})\mathcal O(s),
\]

and the positive Bézout polynomial

\[
U(z)=\sum_{r=0}^3u_rz^r
\]

of `L-26206`, satisfying

\[
U(z)p(z)+U(-z)p(-z)=1.
\]

Hence, exactly,

\[
\frac1{\zeta(s)}
=(1-2^{-s})
\left[
 U(2^{-s})B_+(s)+U(-2^{-s})B_-(s)
\right].
\tag{L-32408.1}
\]

Let `b_+`, `b_-` be the coefficient sequences of the two parity sources. Equation (L-32408.1) is the coefficient identity

\[
\boxed{
\mu
=(\varepsilon-\delta_2)*
\sum_{r=0}^3u_r
\left[
 \delta_{2^r}*b_+
 +(-1)^r\delta_{2^r}*b_-
\right].
}
\tag{L-32408.2}
\]

Thus the unweighted source boundary may not be normed channel by channel. After the mandatory finite synthesis it is literally the ordinary Möbius source.

## 2. Exact carry image of the reconstructed boundary

For a source `b`, its unweighted carry image on a split `n=j+k` is

\[
Y_b(n,j)=\sum_{q\le n}b(q)\chi_{n,q}(j).
\]

Since

\[
\mathbf1*\mu=\varepsilon,
\]

the associated floor potential is

\[
H_\mu(x)=\sum_{q\le x}\mu(q)\left\lfloor\frac xq\right\rfloor
=\mathbf1_{x\ge1}.
\]

Therefore

\[
\boxed{
Y_\mu(n,j)=
\begin{cases}
0,&j\in\{0,n\},\\
-1,&1\le j\le n-1.
\end{cases}}
\tag{L-32408.3}
\]

No Möbius sum remains. In particular the complete reconstructed boundary energy on the uniform split row is

\[
\boxed{
\mathcal B_\mu(n)
:=\frac1{n+1}\sum_{j=0}^n|Y_\mu(n,j)|^2
=\frac{n-1}{n+1}.
}
\tag{L-32408.4}
\]

This is the cancellation hidden by separately measuring the plus and minus Euler boundaries.

## 3. Paired reserve

Retain the averaged parity-paired reserve

\[
\mathcal R_{\rm pair}(n)
=\frac1{n+1}\sum_{j=0}^n
\left[P_0(n,j)^2+P_1(n,j)^2-S_0(n,j)\right]
\tag{L-32408.5}
\]

from `L-32406/L-32407`.

The claim is

\[
\boxed{
\mathcal B_\mu(n)<\mathcal R_{\rm pair}(n)
\qquad(n=2\text{ or }n\ge4),
}
\tag{L-32408.6}
\]

while

\[
\boxed{
\mathcal R_{\rm pair}(3)=0,
\qquad
\mathcal B_\mu(3)=\frac12.
}
\tag{L-32408.7}
\]

Thus the fully synthesized unweighted boundary is absorbed with coefficient **one** on every row except the single fixed bottom row `n=3`.

## 4. Exact finite gate

The directed finite checker `X-32402` already computes a rigorous lower interval for `R_pair(n)` for every

\[
6\le n<30000.
\]

The strengthened replay checks the sharper rowwise inequality

\[
\boxed{
(n+1)\,\mathcal R_{\rm pair}(n)>n-1.
}
\tag{L-32408.8}
\]

The smallest directed margin occurs at

\[
\boxed{n=7,}
\]

where numerically for orientation only

\[
\mathcal R_{\rm pair}(7)=0.775163360674\ldots,
\qquad
\mathcal B_\mu(7)=\frac34,
\]

leaving a margin about `0.02516`. The proof object uses the same 96-bit directed logarithm intervals as `X-32402`; the decimal is not used as proof.

The direct rows `n=2,4,5` are checked by the existing exact small-row evaluator. Row `n=3` is retained as the explicit exception.

## 5. Cofinal tail

For `n>=30000`, `L-32407` imports the elementary tail lower bound

\[
\mathcal R_{\rm pair}(n)
\ge
\frac{n^2\log^22}{30}-36n-42n\log n.
\tag{L-32408.9}
\]

The right side already exceeds `174` at `n=30000` and is increasing thereafter. Since

\[
\mathcal B_\mu(n)<1,
\]

(L-32408.6) follows immediately throughout the infinite tail.

## 6. Consequence for the parity proof graph

Before this lemma the unweighted source boundary was tracked as separate plus/minus Euler channels. The minus channel has a diffuse dyadic floor potential and is a poor object to norm independently.

The correct order is

```text
plus/minus source boundaries
-> exact finite positive Bézout synthesis
-> final (1-delta_2) two-contact factor
-> ordinary Möbius source
-> constant carry charge -1
-> coefficient-one absorption by the paired reserve.
```

Accordingly the parity route no longer has an uncontrolled **carry-image** unweighted boundary at cofinal scale. The sole bottom exception is the fixed row `n=3`.

This does not by itself identify a pure carry row with the RH-sensitive independent-frequency physical source. The remaining production step is the pole-preserving source-convolved localization/congruence which places the synthesized boundary and the logarithmic moment block in the same Hermitian physical ledger.

## 7. Proof boundary

Closed here, subject to replay:

1. exact coefficient reconstruction of `mu` from the parity pair;
2. exact constant carry image of the reconstructed source;
3. exact row energy `(n-1)/(n+1)`;
4. coefficient-one absorption by the paired reserve for every row except `n=3`;
5. isolation of the single finite bottom exception.

Open:

1. the source-convolved independent-frequency physical congruence for the fully synthesized pair;
2. the resulting global block recurrence;
3. RH.
