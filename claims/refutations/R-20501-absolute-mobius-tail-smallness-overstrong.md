# R-20501 — Absolute Möbius-tail smallness is not necessary

Claim ID: `R-20501`  
Title: A large positive omitted-zero residual may coexist with a strict corrected-kernel floor  
Status: `EXACT FINITE SCOPE CORRECTION`  
Authoring agent: `gpt56-03-q`  
Created: 2026-08-01  
Dependencies: `L-20502`; `X-20501`  
Scope: the absolute-value synthesis target in `T-20301`  
Related counterexample candidates: none

## Refuted shortcut

The sufficient target

\[
|Q_W(Tc,Tc)|
+
\|C^{-1/2}Z_KJc\|^2
\le
\eta\|Jc\|_G^2,
\qquad
\eta\to0,
\tag{R-20501.1}
\]

charges positive and negative tail mass symmetrically.

That is unnecessary for a lower spectral floor.

## Exact counterexample

Use the retained graph and conditional frame of `X-20501`:

\[
J=
\begin{pmatrix}
1\\-1/4
\end{pmatrix},
\qquad
G_K=\frac{17}{16},
\]

with conditional selected-line frame

\[
Q_Y|_K=\frac98,
\qquad
\sigma^2=\frac{18}{17},
\]

and Schur correction

\[
Q_{\rm cross}|_K=\frac{49}{3200},
\qquad
\chi=\frac{49}{3400}.
\]

Now take a residual form whose restriction to the graph is

\[
Q_{\rm rem}|_K=100.
\]

Its absolute size is enormous relative to the metric:

\[
\frac{|Q_{\rm rem}|_K}{G_K}
=
\frac{1600}{17}.
\]

Thus every small absolute-tail target fails.

But the residual is positive, so its one-sided negative endpoint is

\[
\omega=0.
\]

`L-20502` certifies the conservative corrected floor

\[
\boxed{
\sigma^2-\omega-\chi
=
\frac{3551}{3400}>0.
}
\tag{R-20501.2}
\]

The actual corrected value is much larger because the positive residual was
discarded in the lower estimate.

## Correct conclusion

For lower-floor purposes, replace (R-20501.1) by

\[
Q_{\mathrm{rem},Y}|_K
\succeq-\omega G_K,
\tag{R-20501.3}
\]

together with the positive selected-line frame and the Schur-cross upper LMI.

Only the negative part of the complete residual matters.

## Scope

- The absolute criterion remains a valid sufficient condition.
- It must not be advertised as the exact remaining theorem.
- The one-sided residual is still RH-bearing; this correction does not prove it.
- Positive unselected line-zero mass may be arbitrarily large without harming
  the lower floor.
