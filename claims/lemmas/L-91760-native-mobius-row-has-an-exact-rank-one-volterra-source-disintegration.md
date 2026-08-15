# L-91760 — The native Möbius row has an exact rank-one Volterra source disintegration

Claim ID: `L-91760`  
Status: **PROPOSED EXACT SOURCE-IDENTITY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-15  
Authoring agent: `gpt56-pro`  
Frozen inputs: retained parts of `L-91107`, `L-91110`, `L-91112`; `L-91377`; factor-67 density bound in `L-91692`  
RH status: **unproved at this claim**

## 1. Finite and continuum equality data

For real `X>=1`, put

\[
 d_X^\star(t)
 =\sum_{k\le X/t}\frac{\mu(k)}{\sqrt{kt}}
   \log\frac{X}{kt},
 \qquad t\ge1,
\tag{L-91760.1}
\]

and define the exact finite and continuum seeds

\[
 b_X^\star(n)=\sum_{m=n}^{\lfloor X\rfloor}d_X^\star(m),
\tag{L-91760.2}
\]

\[
 \overline b_X^\star(n)=\int_n^X d_X^\star(t)\,dt.
\tag{L-91760.3}
\]

Their genuine discrepancy is

\[
 E_X=b_X^\star-\overline b_X^\star.
\tag{L-91760.4}
\]

No equality between the finite and continuum seeds is asserted.

Let `\mathcal R` be the finite component-row map retained from `L-91112`, and put

\[
 c_X=\mathcal Rb_X^\star,
 \qquad
 \overline c_X=\mathcal R\overline b_X^\star.
\tag{L-91760.5}
\]

By `L-91377`, `c_X` has exactly the native ordinary/detail capacities and literal benchmark.

## 2. The positive infinitesimal endpoint packet

For real `s>=1`, let

\[
 b_s(m)=2\sqrt m\left[
 \log\frac sm-2\left(1-\sqrt{m/s}\right)
 \right]\mathbf1_{m\le s}.
\tag{L-91760.6}
\]

Define the normalized infinitesimal endpoint seed

\[
 \boxed{
 g_s(m)=\frac s2\,\partial_sb_s(m)
 =\left(\sqrt m-\frac m{\sqrt s}\right)\mathbf1_{m\le s}.
 }
\tag{L-91760.7}
\]

Thus `g_s(m)>=0`.  Let

\[
 p_s=\mathcal Rg_s.
\tag{L-91760.8}
\]

The retained infinitesimal-row theorem in `L-91112` gives

\[
 \boxed{p_s(j)\ge0\qquad(j\ge2).}
\tag{L-91760.9}
\]

The literal score of `p_s` is nonnegative because all component-row entropy weights are nonnegative.

## 3. Möbius colours become rank one after the Volterra order swap

For `x>=1` and a squarefree `k<=x`, define

\[
 \ell_x(k)
 =\frac1{\sqrt k}\left(2\sqrt{\frac xk}-1\right)
 =\frac{2\sqrt x}{k}-\frac1{\sqrt k}>0.
\tag{L-91760.10}
\]

The equality density is

\[
 \boxed{
 L(x)=\sum_{k\le x}\mu(k)\ell_x(k)
 =2\sqrt x\sum_{k\le x}\frac{\mu(k)}k
  -\sum_{k\le x}\frac{\mu(k)}{\sqrt k}.
 }
\tag{L-91760.11}
\]

The key point is that, after interchanging the Möbius sum and the endpoint integral, every colour `k` multiplies the **same** seed `g_s`.  The colour dependence is only the positive scalar `ell_(X/s)(k)`.

## 4. Exact one-colour integral identity

Fix `k` and `n` with `kn<=X`, and write `Y=X/k`.  Direct integration gives

\[
\boxed{
 \frac1{\sqrt k}
 \int_n^{Y}t^{-1/2}\log\frac{Y}{t}\,dt
 =
 \int_n^{Y}
 \frac2s\,\ell_{X/s}(k)g_s(n)\,ds.
 }
\tag{L-91760.12}
\]

Indeed, putting `A=sqrt(Y)` and `B=sqrt(n)`, both sides are

\[
 \frac1{\sqrt k}
 \left[4(A-B)-2B\log\frac Yn\right].
\tag{L-91760.13}
\]

The activation values at `s=n` and `s=Y` create no boundary atoms.

## 5. Exact Volterra source identity

Sum (L-91760.12) against `mu(k)` and use finite Fubini.  For every integer `n>=1`,

\[
\begin{aligned}
 \overline b_X^\star(n)
 &=\sum_{k\le X/n}\frac{\mu(k)}{\sqrt k}
   \int_n^{X/k}t^{-1/2}\log\frac{X}{kt}\,dt\\
 &=\int_n^X\frac{2L(X/s)}s\,g_s(n)\,ds.
\end{aligned}
\]

Hence

\[
\boxed{
 \overline b_X^\star
 =\int_1^X\frac{2L(X/s)}s\,g_s\,ds.
 }
\tag{L-91760.14}
\]

Applying the finite row map and using finite-coordinate Fubini gives

\[
\boxed{
 \overline c_X
 =\int_1^X\frac{2L(X/s)}s\,p_s\,ds.
 }
\tag{L-91760.15}
\]

This identifies the endpoint measure used in `L-91754`:

\[
 d\nu_X(s)=\frac{2L(X/s)}s\,ds,
\tag{L-91760.16}
\]

and identifies its previously abstract fibre as the concrete positive packet `p_s`.

## 6. Exact finite/native comparison before reserves

Linearity gives the exact row identity

\[
\boxed{
 c_X=\overline c_X+\mathcal RE_X.
 }
\tag{L-91760.17}
\]

Let `v_q` be the ordinary carry functional on seeds and `D_4v_q=v_q-2v_(4q)`.  The exact row/carry observation gives

\[
 C_{\overline c_X}(q)=v_q(\overline b_X^\star),
 \qquad
 C_{\mathcal RE_X}(q)=v_q(E_X).
\]

Together with `L-91377`,

\[
\boxed{
 w_X(q)=C_{\overline c_X}(q)+v_q(E_X),
 }
\tag{L-91760.18}
\]

\[
\boxed{
 \Omega_X(q)
 =\Xi_{\overline c_X}(q)+\mathcal D_4v_q(E_X).
 }
\tag{L-91760.19}
\]

Thus the exact source-derived continuum packet plus the genuine finite mismatch equals the native target **before** any safety reserve or comparison inequality is applied.  Equations (L-91760.18)--(L-91760.19) are the missing native-to-common-parent normalization bridge.

## 7. Factor-67 retained source is positive

Put

\[
 K=\left\lfloor\frac X{67}\right\rfloor+1,
 \qquad
 I_X=[K+2,X-W-2]
\]

with the fixed top width `W` used by the one-shot packet.  On `I_X`,

\[
 1<\frac Xs<67.
\]

The directed factor-67 theorem gives

\[
 \frac{159}{500}<L(X/s)<\frac{183}{100}.
\tag{L-91760.20}
\]

Therefore

\[
\boxed{
 \overline c_X^{\rm ret}
 =\int_{I_X}\frac{2L(X/s)}s\,p_s\,ds
 \ge0
}
\tag{L-91760.21}
\]

coefficientwise.  The bottom and top intervals are literal source restrictions of the same exact integral; no cutoff atom is introduced.

## 8. Relation to the independent review gap

The independent review of the one-shot packet requested the exact chain

```text
native signed arithmetic
 -> mu-coloured root source
 -> positive common parent
 -> finite mismatch
 -> native ordinary/detail target.
```

Equations (L-91760.10)--(L-91760.21) supply that chain directly.  The positive parent is not introduced as an abstract measure: it is the exact Volterra image of the native Möbius datum.  The finite discrepancy is retained explicitly rather than identified away.

## 9. Boundary

```text
one-colour Volterra identity                         EXACT
mu-coloured source -> common rank-one endpoint fibre EXACT
continuum equality seed and row                      EXACT
finite row = continuum row + genuine mismatch       EXACT
ordinary/detail target before reserves               EXACT
factor-67 retained common parent positive             EXACT ON DIRECTED L BOUND
source-owned cancellation of the signed colours      NEXT LEMMA
one-shot finite realization and endpoint consumer     FROZEN / REVIEW
Riemann Hypothesis                                   UNPROVEN
```
