# L-26108 — Canonical annulus enlargement

Claim ID: `L-26108`  
Title: Enlarging the repair annulus can only improve the primal radius and the dual denominator, while preserving a fixed parabolic positivity moat  
Status: **PROPOSED COMPLETE ELEMENTARY LEMMA**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #261  
Depends on: `L-26102`, `L-26105`  
Scope: fixes the canonical proposal annulus at `[X/5,4X/5]`

## 1. Monotonicity in the repair support

Let `I subset I'` be two finite index sets, and let `A_I`, `A_(I')` be the corresponding prime-power divisor-gradient matrices. Define

\[
 \mathcal R_I(r)
 =\inf\{\|F\|_{\ell^2(I)}:A_IF\ge r\}.
 \tag{L-26108.1}
\]

Every flow on `I` extends by zero to `I'`, with the same norm and the same constraint correction. Therefore

\[
\boxed{
 \mathcal R_{I'}(r)\le\mathcal R_I(r).
}
\tag{L-26108.2}

Dually, for every nonnegative `lambda`,

\[
 \|A_{I'}^*\lambda\|_2^2
 =\|A_I^*\lambda\|_2^2
  +\sum_{j\in I'\setminus I}|(A^*\lambda)_j|^2,
\]

so

\[
\boxed{
 \|A_{I'}^*\lambda\|_2
 \ge\|A_I^*\lambda\|_2.
}
\tag{L-26108.3}

Thus the Annular Dual Frame inequality becomes only easier when the annulus is enlarged.

## 2. Positivity moat on the wider annulus

The parabolic profile

\[
 B(t)=2\sqrt t\left[\log(1/t)-2(1-\sqrt t)\right]
\]

is strictly positive on every compact subinterval of `(0,1)`. Hence

\[
 c_*=\min_{1/10\le t\le9/10}B(t)>0.
 \tag{L-26108.4}

For all sufficiently large `X`, the seed and the two sites adjacent to

\[
\boxed{
 I_X^{\rm can}
 =\left[\left\lceil\frac X5\right\rceil,
        \left\lfloor\frac{4X}{5}\right\rfloor\right]
}
\tag{L-26108.5}

therefore satisfy

\[
 b_X^{(0)}(m)\ge c_*\sqrt X.
 \tag{L-26108.6}

The positivity transfer of `L-26102` applies unchanged.

## 3. Objective cost

On `I_X^can`,

\[
 \left(
  \sum_{j\in I_X^{\rm can}}
  \log^2\frac{j^2}{j^2-1}
 \right)^{1/2}
 \ll X^{-3/2}.
 \tag{L-26108.7}

Thus the wider annulus preserves the same negligible objective-cost scale.

## 4. Multiplicative advantage

The ratio of the annular endpoints is four. Consequently the annulus contains positive-density families for which both

\[
 n,2n\in I_X^{\rm can}
\]

and

\[
 n,3n\in I_X^{\rm can}.
\]

This allows the exact dyadic and triadic additive identities in `L-26107`. The original discovery annulus `[9X/20,4X/5]` did not contain a complete doubling pair.

## 5. Reconnaissance consequence

Ordinary floating active-set runs on `[X/5,4X/5]` improve, rather than weaken, the observed conditioning and flow norm. Through the tested range the generated frame floor is larger and the flow norm smaller than on the original top-half annulus. This is discovery only; the monotonicity statements (L-26108.2)--(L-26108.3) are exact.

## 6. Proposal convention

The canonical `ADF` and `T-26101` use `I_X^can` from (L-26108.5). The narrower annulus retained in early active-set reconnaissance remains a valid subspace diagnostic, but it is not the final proof-facing support.

## 7. Proof boundary

Exact:

- primal-radius monotonicity;
- dual-denominator monotonicity;
- fixed seed slack and objective cost on the wider annulus.

Open:

- `ADF` on the canonical annulus;
- RH.