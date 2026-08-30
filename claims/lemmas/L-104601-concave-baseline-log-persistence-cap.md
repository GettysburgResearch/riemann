# L-104601 — Concave-baseline log-persistence is paid by off-line zero variation

Claim ID: `L-104601`  
Status: **PROVED EXACT**  
Created: 2026-08-24  
RH status: **not assumed**

## 1. A one-dimensional persistence inequality

Let `I=[a,b]`, let `C:I->R` be concave, let `Q` have bounded variation, and put

\[
U=C+Q.
\]

Assume first that `U` is Morse, has distinct critical values, and that its endpoint values are regular.  Let

\[
\operatorname{Pers}_{\rm fin}^{\uparrow}(U)
\]

be the sum of the lengths of all finite bars in the zero-dimensional persistence barcode of the upper excursion filtration `{U>y}`.

For a continuous piecewise monotone function one has the exact variation/barcode identity

\[
\operatorname{TV}(U)
=2\operatorname{Pers}_{\rm fin}^{\uparrow}(U)
 +2\max_I U-U(a)-U(b).
\tag{L-104601.1}
\]

A concave function has no finite upper-excursion bars, so

\[
\operatorname{TV}(C)=2\max_I C-C(a)-C(b).
\tag{L-104601.2}
\]

Subtracting (L-104601.2) from (L-104601.1), using

\[
\operatorname{TV}(C+Q)-\operatorname{TV}(C)
\le \operatorname{TV}(Q),
\]

and writing `q_* = inf_I Q`, gives

\[
\begin{aligned}
2\operatorname{Pers}_{\rm fin}^{\uparrow}(U)
&\le \operatorname{TV}(Q)
 -2(\max U-\max C)+Q(a)+Q(b)\\
&\le \operatorname{TV}(Q)+Q(a)+Q(b)-2q_*\\
&\le 3\operatorname{TV}(Q).
\end{aligned}
\]

Therefore

\[
\boxed{
\operatorname{Pers}_{\rm fin}^{\uparrow}(C+Q)
\le {3\over2}\operatorname{TV}_I(Q).
}
\tag{L-104601.3}
\]

The same conclusion holds for non-generic data by uniform approximation and lower semicontinuity of finite total persistence.  The constant `3/2` is deliberately safe; no sharpness claim is made.

## 2. Application to a real-zero gap of an even real entire function

Let `F` be an even real entire function of order at most one whose zeros lie in a fixed horizontal strip.  Let `G=(a,b)` be a bounded gap between consecutive real zeros of `F`.  Group the Hadamard product by real zeros and by the off-real symmetries

\[
\rho\mapsto\bar\rho,
\qquad
\rho\mapsto-\rho.
\]

On `G`, after assigning the harmless affine canonical-product term to the real block,

\[
\log|F(t)|=C_G(t)+Q_G(t),
\tag{L-104601.4}
\]

where

\[
C_G''(t)=-\sum_{\gamma\in Z(F)\cap\mathbb R}{m_\gamma\over(t-\gamma)^2}<0
\tag{L-104601.5}
\]

and hence `C_G` is concave.

For an off-real quadruple represented by `x+iy`, `x>0`, `y>0`, use the grouped orbit potential

\[
q_{x,y}(t)
=
\log\left(
 ((t-x)^2+y^2)((t+x)^2+y^2)
\right).
\tag{L-104601.6}
\]

For a purely imaginary pair use

\[
q_{0,y}(t)=\log(t^2+y^2).
\tag{L-104601.7}
\]

The grouped canonical product gives locally absolutely convergent derivative series, and therefore

\[
Q_G(t)=\sum_{\mathcal O}m_{\mathcal O}q_{\mathcal O}(t)
\]

in `BV(G)` after the canonical affine normalization.  Define the explicit off-line variation budget

\[
\boxed{
\mathcal J_F(G)
=
\sum_{\mathcal O}m_{\mathcal O}
 \operatorname{TV}_{G}(q_{\mathcal O}).
}
\tag{L-104601.8}
\]

Then

\[
\operatorname{TV}_G(Q_G)\le\mathcal J_F(G).
\tag{L-104601.9}
\]

Truncate the gap at `a+epsilon,b-epsilon`, apply (L-104601.3), and let `epsilon` decrease to zero.  The real-zero logarithmic singularities stay entirely in the concave block.  Thus

\[
\boxed{
\operatorname{Pers}_{\rm fin}^{\uparrow}
  (\log|F|;G)
\le {3\over2}\mathcal J_F(G).
}
\tag{L-104601.10}
\]

Apply the same statement to `-F`; equivalently use upper excursions of `\log|F|` separately on the positive and negative sign components.

## 3. Deep bars

A finite excursion bar has birth amplitude `M`, death amplitude `m`, and logarithmic depth

\[
d=\log(M/m)>0.
\]

For every `delta>0`, let `B_delta(F;G)` be the number of finite bars in `G` with `d>=delta`.  Markov's inequality and (L-104601.10) give

\[
\boxed{
B_\delta(F;G)
\le {3\over2\delta}\mathcal J_F(G).
}
\tag{L-104601.11}
\]

For `F=Xi^(k)`, every finite upper-excursion bar is exactly one wrong extremum of the parent `Xi^(k-1)`, under the persistence pairing of `L-104545`.  Hence (L-104601.11) is a source-visible bound for the **deep** reverse-Rolle defects.

## 4. Relation to the quantitative dipole programme

The pointwise dipole weights of `L-105061/L-105064` are designed to count every extra derivative zero with a bounded worst-case coefficient.  `L-105075` proves that this pointwise pricing is too expensive for a contracting descent.

The present theorem prices a different quantity: the actual logarithmic persistence of a false excursion.  A near-line orbit may carry a logarithmic variation comparable to `log(g/y)`; that is not discarded as an artifact.  It is charged only when it creates a genuinely deep bar.  Shallow bars are separated into an independent anti-concentration gate in `T-104610`.

## 5. Boundary

```text
concave-baseline persistence cap      PROVED EXACT
Hadamard off-line variation budget    PROVED ON GROUPED PRODUCT
fixed-order deep-bar bound            PROVED EXACT
normalized Xi off-line budget         NOT ESTIMATED HERE
RH                                    UNPROVED
```
