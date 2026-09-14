# R-106620 — Vanishing scale does not imply a cofinal Rouché rate

Claim ID: `R-106620`  
Status: **PROVED EXACT FIREWALL; CORRECTS THE HEIGHT INFERENCE IN T-106610**  
Created: 2026-08-26  
RH status: **unproved**

## 1. Quantifier mismatch

`L-106603` proves the following finite-window statement. For each fixed
regular window and each prescribed zero-cluster error, there exists a
window-dependent threshold \(\delta_T>0\) such that every admissible analytic
scale satisfying

\[
\|a_T\|_{\infty}<\delta_T
\]

preserves the required zero clusters.

It does **not** prove a lower bound for \(\delta_T\). Therefore the asymptotic
fact

\[
\|a_T\|_\infty=O(1/\log T)\longrightarrow0
\]

does not imply \(\|a_T\|_\infty<\delta_T\). The threshold may shrink faster
than every prescribed cofinal rate because the window may contain arbitrarily
tight zero clusters.

## 2. Exact finite counterfamily

Let

\[
p_\epsilon(z)=z^2+\epsilon^2,
\qquad
a_\epsilon>0.
\]

The original zeros are \(\pm i\epsilon\), while

\[
p_\epsilon+i a_\epsilon p_\epsilon'
=
z^2+2ia_\epsilon z+\epsilon^2
\]

has zeros

\[
z_\pm=-ia_\epsilon
\pm i\sqrt{a_\epsilon^2+\epsilon^2}.
\]

Choose \(\epsilon_n=e^{-n}\) and \(a_n=1/n\). Then \(a_n\to0\), but one
perturbed zero is at distance asymptotic to \(2/n\) from the lower original
zero. It leaves every disjoint cluster disk whose radius is \(O(\epsilon_n)\).
Thus a scale can tend uniformly to zero while still being far above the
Rouché threshold of the corresponding window.

## 3. Consequence for the Riemann--Siegel gauge

The exact factorization of `L-106610--L-106612` remains valid. What does not
follow from the current repository is that the particular scale

\[
a_{\rm RS}=1/\vartheta'
\]

inherits the `3/4000` denominator-height bound from `L-106603`.

A valid repair must either:

1. prove a quantitative Xi zero-cluster threshold
   \(\delta_T\gg1/\log T\); or
2. use a scale for which companion height is bounded directly, without a
   diagonal Rouché inference.

`L-106620--L-106621` implement the second repair by freezing the
Riemann--Siegel scale on mesoscopic windows.
