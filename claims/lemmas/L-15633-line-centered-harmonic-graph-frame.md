# L-15633 — The line-centered harmonic graph is a sub-square-root support frame

Claim ID: `L-15633`  
Title: A coercive line-centered harmonic minimizer preserves the complete source-frame envelope and gives a graph-only PR #191 soft-block bound  
Status: `PROVED ABSTRACT GRAPH/SHORTING THEOREM; PRODUCTION PROFILE DERIVATIVES DECLARED`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: `L-15632`; `L-16226`; `L-18512`  
Scope: support averaging of the finite profile-soft block without an operator estimate on the whole ambient space  
Related counterexample candidates: none

## 1. Purpose

`L-15632` uses a relative perturbation LMI on the complete low-plus-harmonic
block. A production support-average need not estimate the perturbation on the
whole ambient sector. It is enough to control:

1. the perturbation on one line-centered harmonic graph; and
2. the residual of that trial solve in the actual block.

Both are finite Hilbert-valued phase families. This lemma also proves that the
line-centered harmonic minimizer does not destroy the sub-square-root profile
envelope.

## 2. Line-centered graph

Use the notation of `L-15632`. Thus

\[
 \mathcal H^0
 =\begin{pmatrix}B^0&(Z^0)^*\\Z^0&C^0\end{pmatrix}
 \succeq0,
 \tag{L-15633.1}
\]

\[
 C^0\succeq h_0M,
 \qquad
 B^0\preceq\ell D.
 \tag{L-15633.2}
\]

Put

\[
 X_0=(C^0)^{-1}Z^0,
 \qquad
 J_0s=(s,-X_0s).
 \tag{L-15633.3}
\]

Then

\[
 J_0^*\mathcal H^0J_0\succeq0
 \tag{L-15633.4}
\]

and

\[
 \boxed{
 X_0^*MX_0\preceq{\ell\over h_0}D.
 }
 \tag{L-15633.5}
\]

## 3. Graph-only direct-short theorem

Let the actual block be

\[
 \mathcal H=\begin{pmatrix}B&Z^*\\Z&C\end{pmatrix},
 \qquad
 C\succeq hM,
 \qquad h>0.
 \tag{L-15633.6}
\]

Assume the two finite graph estimates

\[
 \boxed{
 J_0^*(\mathcal H-\mathcal H^0)J_0
 \succeq-\varepsilon D
 }
 \tag{L-15633.7}
\]

and

\[
 \boxed{
 (Z-CX_0)^*M^{-1}(Z-CX_0)
 \preceq\nu^2D.
 }
 \tag{L-15633.8}
\]

Then the actual harmonic Schur complement satisfies

\[
 \boxed{
 B-Z^*C^{-1}Z
 \succeq-\left(\varepsilon+{\nu^2\over h}\right)D.
 }
 \tag{L-15633.9}
\]

### Proof

By (L-15633.4) and (L-15633.7),

\[
 J_0^*\mathcal HJ_0\succeq-\varepsilon D.
\]

Apply `L-18512` with trial solve `X_0`, ambient floor `C>=hM`, and residual
`Z-CX_0`. Equation (L-15633.8) gives (L-15633.9). QED.

Thus a production proof may support-average only the trial energy and residual,
not the complete ambient operator.

## 4. Amplitude envelope of the graph

Let

\[
 \mathcal A_U:S\to Y,
 \qquad
 \mathcal A_E:E\to Y
 \tag{L-15633.10}
\]

be any amplitude channel entering the support large sieve. Suppose

\[
 \mathcal A_U^*\mathcal A_U\preceq B_U^2D,
 \qquad
 \mathcal A_E^*\mathcal A_E\preceq B_E^2M.
 \tag{L-15633.11}
\]

The graph amplitude is

\[
 \mathcal A_{J_0}=\mathcal A_U-\mathcal A_EX_0.
 \tag{L-15633.12}
\]

Using (L-15633.5),

\[
 \boxed{
 \mathcal A_{J_0}^*\mathcal A_{J_0}
 \preceq
 \left(
 B_U+B_E\sqrt{\ell/h_0}
 \right)^2D.
 }
 \tag{L-15633.13}
\]

Therefore the line-centered harmonic lift has the same asymptotic envelope as
the low and ambient frames whenever `ell/h_0=O(1)`.

## 5. Support derivative of the minimizer

Use covariantly whitened blocks

\[
 \mathbf C=M^{-1/2}C^0M^{-1/2},
 \qquad
 \mathbf Z=M^{-1/2}Z^0D^{-1/2},
 \tag{L-15633.14}
\]

and

\[
 \mathbf X=M^{1/2}X_0D^{-1/2}
 =\mathbf C^{-1}\mathbf Z.
 \tag{L-15633.15}
\]

Here differentiation includes the declared metric transports, so no derivative
of a square root is omitted. Let a dot denote logarithmic support derivative.
Assume

\[
 \|\dot{\mathbf C}\|\le c_C,
 \qquad
 \|\dot{\mathbf Z}\|\le c_Z.
 \tag{L-15633.16}
\]

Since `mathbf C>=h_0 I`, differentiation of
`mathbf C mathbf X=mathbf Z` gives

\[
 \dot{\mathbf X}
 =\mathbf C^{-1}
  (\dot{\mathbf Z}-\dot{\mathbf C}\mathbf X).
 \tag{L-15633.17}
\]

Together with (L-15633.5),

\[
 \boxed{
 \|\dot{\mathbf X}\|
 \le{1\over h_0}
 \left(
 c_Z+c_C\sqrt{\ell/h_0}
 \right).
 }
 \tag{L-15633.18}
\]

Thus a logarithmic line-centered ambient floor prevents the harmonic minimizer
from introducing a new support-conditioning scale.

## 6. Support-average application

Suppose the low and ambient amplitude/derivative envelopes are bounded by
`mathfrak B_T`, the block ratios satisfy

\[
 h_0\asymp\ell\asymp\log T,
 \tag{L-15633.19}
\]

and `c_C,c_Z` are at most polylogarithmic multiples of the same envelope. Then
(L-15633.13) and (L-15633.18) show that the graph trial-energy family and its
actual residual family satisfy the Hilbert-valued hypotheses of `L-16226` with
an envelope of the same order.

Consequently, if

\[
 \mathfrak B_T=o\!\left(\sqrt{T/\log T}\right),
 \tag{L-15633.20}
\]

one may choose a support in every retained dyadic block for which

\[
 \varepsilon_T=o(\log T),
 \qquad
 {\nu_T^2\over h_T}=o(\log T).
 \tag{L-15633.21}
\]

If the graph is whitened by a regularized soft metric `Dhat` and

\[
 \widehat D|_{S_T}\preceq q_TG_T,
 \qquad
 q_T\log T\to0,
 \tag{L-15633.22}
\]

then (L-15633.9) gives

\[
 \boxed{
 \left\|
 \left[
 G_T^{-1/2}\mathscr S_TG_T^{-1/2}
 \right]_{-}
 \right\|\to0.
 }
 \tag{L-15633.23}
\]

## 7. Relation to the complete prime-side matrix

The trial-energy family in (L-15633.7) is evaluated from the complete actual
prime/polar/archimedean matrix. Its line-centered comparison is positive by the
zero-side formula. The residual family in (L-15633.8) contains the complete
low--harmonic response.

Thus (L-15633.7)--(L-15633.8) retain every cancellation available to the direct
matrix of PR #191. A separate norm for the terminal-prime matrix is neither
required nor recommended.

## 8. Proof boundary

- The graph-only shorting theorem and harmonic-minimizer bounds are exact.
- Applying the support large sieve requires proof-grade amplitude and covariant
  support-derivative ledgers for the actual low and harmonic frames.
- This lemma does not emit those production ledgers and does not prove RH.
