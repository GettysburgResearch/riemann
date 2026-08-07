# L-26102 — Annular slack and objective transfer

Claim ID: `L-26102`  
Title: Any subpower-norm repair on one fixed interior annulus preserves the parabolic seed and has negligible exact objective cost  
Status: **PROPOSED COMPLETE ELEMENTARY LEMMA**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #261  
Depends on: PR #248 `L-24502`; `L-26101`  
Scope: deterministic transfer from a finite annular flow to a sharp carry certificate

## 1. Interior slack of the parabolic seed

Recall

\[
 b_X^{(0)}(m)
 =2\sqrt m\left[
  \log\frac Xm-2\left(1-\sqrt{\frac mX}\right)
 \right].
 \tag{L-26102.1}
\]

Fix once and for all

\[
 0<\alpha<\beta<1.
\]

Put

\[
 B(t)=2\sqrt t\left[\log(1/t)-2(1-\sqrt t)\right].
\]

The bracket is strictly positive for `0<t<1`, so compactness gives

\[
 c_{\alpha,\beta}
 :=\min_{\alpha/2\le t\le(1+\beta)/2}B(t)>0.
 \tag{L-26102.2}
\]

For all sufficiently large `X`, every integer within distance one of

\[
 I_X=[\lceil\alpha X\rceil,\lfloor\beta X\rfloor]
\]

therefore satisfies

\[
\boxed{
 b_X^{(0)}(m)\ge c_{\alpha,\beta}\sqrt X.
}
\tag{L-26102.3}
\]

## 2. Positivity from an `L^2` moat

Let `F` be a real flow supported on `I_X`, extended by zero outside the annulus, and define

\[
 b_F(m)=b_X^{(0)}(m)+F_{m-1}-F_m.
 \tag{L-26102.4}
\]

For every `m`,

\[
 |F_{m-1}-F_m|
 \le2\|F\|_\infty
 \le2\|F\|_2.
 \tag{L-26102.5}
\]

Hence

\[
\boxed{
 \|F\|_2\le\frac14c_{\alpha,\beta}\sqrt X
 \quad\Longrightarrow\quad
 b_F(m)\ge0\quad(2\le m\le X).
}
\tag{L-26102.6}
\]

Outside the annulus and its two neighboring sites the seed is unchanged. At the two boundary sites, (L-26102.3) supplies the same reserve.

Thus a flow of norm `X^{o(1)}` automatically preserves all primal nonnegativity constraints.

## 3. Exact prime-power feasibility

Let

\[
 r_X(q)=v_q(b_X^{(0)})-w_X(q),
 \qquad q=p^a\le X.
 \tag{L-26102.7}
\]

By `L-26101`,

\[
 v_q(b_F)-w_X(q)=r_X(q)-(A_XF)_q.
\]

Therefore

\[
\boxed{
 A_XF\ge r_X
 \quad\Longrightarrow\quad
 v_q(b_F)\le w_X(q)
 \quad\text{for every prime power }q\le X.
}
\tag{L-26102.8}
\]

No condition is required on non-prime-power rows.

## 4. Annular objective norm

The exact loss is

\[
 \mathcal C_X(F)
 =J_X(b_X^{(0)})-J_X(b_F)
 =\sum_{j\in I_X}F_j
  \log\frac{j^2}{j^2-1}.
 \tag{L-26102.9}
\]

For `j>=2`,

\[
 0<\log\frac{j^2}{j^2-1}
 =\log\left(1+\frac1{j^2-1}\right)
 \le\frac1{j^2-1}.
\]

Consequently

\[
\begin{aligned}
 \left(
  \sum_{j\in I_X}
  \log^2\frac{j^2}{j^2-1}
 \right)^{1/2}
 &\le
 \frac{C_\alpha}{X^{3/2}},
\end{aligned}
 \tag{L-26102.10}
\]

for one explicit constant `C_alpha`. Cauchy--Schwarz gives

\[
\boxed{
 |\mathcal C_X(F)|
 \le C_\alpha X^{-3/2}\|F\|_2.
}
\tag{L-26102.11}
\]

In particular,

\[
 \|F\|_2=X^{o(1)}
 \quad\Longrightarrow\quad
 \mathcal C_X(F)=X^{-3/2+o(1)}.
 \tag{L-26102.12}
\]

The theorem needed for RH permits the vastly weaker loss `X^epsilon`; a subpower annular norm therefore leaves an enormous reserve.

## 5. Sharp entropy consequence

Assume `F_X` satisfies

\[
 A_XF_X\ge r_X,
 \qquad
 \|F_X\|_2=X^{o(1)}.
 \tag{L-26102.13}
\]

Then (L-26102.6) and (L-26102.8) make `b_(F_X)` a feasible vector for the exact prime-power divisor-gradient LP. The parabolic seed estimate on PR #248 gives

\[
 J_X(b_X^{(0)})
 \ge4\sqrt X-O(\log X).
\]

Using (L-26102.11),

\[
\boxed{
 J_X(b_{F_X})
 \ge4\sqrt X-X^{o(1)}.
}
\tag{L-26102.14}
\]

The exact von-Mangoldt dual then yields the sharp prime-ramp lower bound.

## 6. Proof boundary

This file proves that a low-norm annular solution is sufficient. It does not construct such a solution. The remaining source-specific theorem is the annular frame/leakage contraction in `L-26103`.