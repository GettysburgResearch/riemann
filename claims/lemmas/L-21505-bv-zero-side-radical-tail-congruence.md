# L-21505 — Compact-BV zero-side convergence gives the exact smooth-source radical-tail congruence

Claim ID: `L-21505`  
Title: The smooth source, sharp finite Fourier vector, and corrected tail share one absolutely convergent zero-side Weil domain  
Status: **PROPOSED — COMPLETE ZERO-SIDE FORM-DOMAIN THEOREM; CCM NORMALIZATION IDENTIFICATION SEPARATE**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: the centered zero-side Weil formula; the unconditional unit-window zero count; `L-16205`; `L-21504`  
Scope: form-domain half of Interface A in the PR #202 prolate/whole-matrix proposals

## 1. Centered zero-side form

Write every nontrivial zero as

\[
 \rho={1\over2}+is_\rho,
 \qquad
 s_\rho=\gamma_\rho+i\delta_\rho,
 \qquad |\delta_\rho|<\frac12.
 \tag{L-21505.1}
\]

Use the repository's centered polarized zero-side form

\[
 \boxed{
 Q_Z(f,g)
 =\sum_\rho m_\rho
 \overline{\widehat f(\overline{s_\rho})}
 \widehat g(s_\rho).
 }
 \tag{L-21505.2}
\]

The present lemma concerns absolute convergence and algebra of (L-21505.2).
Matching `Q_Z` to a particular CCM matrix still requires the exact common
Fourier/Mellin normalization.

## 2. Strip decay for compact BV functions

Let `g` have compact support in `[-L/2,L/2]` and bounded variation.  Its
Fourier transform is

\[
 \widehat g(z)=\int_{-L/2}^{L/2}g(t)e^{-izt}\,dt.
 \tag{L-21505.3}
\]

Stieltjes integration by parts gives, for `z!=0`,

\[
 |\widehat g(z)|
 \le {e^{|\operatorname{Im}z|L/2}\over|z|}
 \left(
  |g(-L/2+)|+|g(L/2-)|+\operatorname{Var}(g)
 \right).
 \tag{L-21505.4}
\]

Together with the trivial `L1` bound, this yields uniformly on the centered
zeta strip

\[
 \boxed{
 |\widehat g(\gamma+i\delta)|
 \le {C_{g,L}\over1+|\gamma|},
 \qquad |\delta|\le\frac12.
 }
 \tag{L-21505.5}
\]

A zero-extended finite Fourier polynomial on the interval is compact BV, so it
satisfies (L-21505.5), including its two endpoint jumps.

## 3. Absolute convergence of the zero-side form

The unconditional Riemann--von Mangoldt unit-window estimate gives

\[
 \#\{\rho:T\le|\gamma_\rho|<T+1\}
 \ll\log(2+T)
 \tag{L-21505.6}
\]

with multiplicity.  Hence

\[
 \sum_\rho {m_\rho\over(1+|\gamma_\rho|)^2}<\infty.
 \tag{L-21505.7}
\]

For compact BV functions `f,g`, equations (L-21505.5)--(L-21505.7) imply

\[
 \boxed{
 \sum_\rho m_\rho
 \left|
  \overline{\widehat f(\overline{s_\rho})}
  \widehat g(s_\rho)
 \right|<\infty.
 }
 \tag{L-21505.8}
\]

The same conclusion holds if either function is Schwartz and the other is
compact BV.  Consequently every expansion and rearrangement below is justified
term by term; no form-closure limit is needed.

## 4. Smooth arithmetic radical

Let `f` be a smooth two-cancellation arithmetic source as in `L-21504`, and put

\[
 h(t)=E(f)(e^t).
 \tag{L-21505.9}
\]

`L-21504` proves `h in S(R)`.  The Mellin factorization of `L-16205` gives

\[
 \widehat h(s_\rho)=0,
 \qquad
 \widehat h(\overline{s_\rho})=0
 \tag{L-21505.10}
\]

for every nontrivial zero, without assuming RH.  Therefore absolute convergence
immediately yields

\[
 \boxed{
 Q_Z(h,g)=Q_Z(g,h)=0
 }
 \tag{L-21505.11}
\]

for every compact BV `g` and every Schwartz `g` in the same convention.

This extends the weak radical identity from a smooth test core to the sharp
finite Fourier vectors used below.

## 5. Sharp finite vector and corrected tail

Let

\[
 y=\iota_L\Pi_N\Sigma_Lh
 \tag{L-21505.12}
\]

be the zero extension of the finite periodized Fourier projection.  It is
compact BV.  Define

\[
 W=h-y.
 \tag{L-21505.13}
\]

By `L-21504`, this `W` is exactly the alias-and-projection-corrected tail of
`L-19820`; it is a sum of one Schwartz function and one compact BV function.
Therefore all pairings among `h,y,W` are absolutely convergent in (L-21505.2).

Using `y=h-W` and (L-21505.11),

\[
\begin{aligned}
 Q_Z(y,y)
 &=Q_Z(h-W,h-W)\\
 &=Q_Z(W,W).
\end{aligned}
 \tag{L-21505.14}

More generally, for two smooth source columns `f,g`,

\[
 \boxed{
 Q_Z(y_f,y_g)=Q_Z(W_f,W_g).
 }
 \tag{L-21505.15}

Likewise

\[
 \boxed{
 Q_Z(y_f,k)=-Q_Z(W_f,k)
 }
 \tag{L-21505.16}
\]

for every compact BV or Schwartz test vector `k`.

Thus the finite source matrix, its cross maps, and the corrected-tail matrix are
exactly the same zero-side objects after the declared basis congruence.

## 6. Matrix consequence

Let `F_(L,N)` be any finite smooth source right inverse for the projected
periodized arithmetic map, and let

\[
 \mathcal W_{L,N}=W_{L,N}F_{L,N}.
 \tag{L-21505.17}
\]

On coefficient space, equations (L-21505.14)--(L-21505.15) give the exact
factorization

\[
 \boxed{
 A_{L,N}^{\rm zero}
 =\mathcal W_{L,N}^*Q_Z\mathcal W_{L,N}.
 }
 \tag{L-21505.18}
\]

No unproved fold convergence, smooth-core approximation, or hidden endpoint
limit remains.  The sharp endpoint jumps are already covered by the compact-BV
absolute convergence theorem.

## 7. What this closes

For the smooth differential cardinal frame, `L-21504` and the present lemma
jointly establish:

1. the global arithmetic image is logarithmically Schwartz;
2. periodization and every fold converge absolutely and smoothly;
3. the sharp finite Fourier projection belongs to an absolutely convergent
   zero-side Weil domain;
4. global radicality extends exactly to that sharp finite vector;
5. the finite matrix equals the corrected-tail zero matrix term by term.

This closes the **convergence and zero-side form-domain** parts of the source
bridge asserted abstractly in `L-19820`.

## 8. Remaining normalization and analytic gates

The theorem does not by itself prove that a named CCM/Suzuki matrix in another
coordinate convention equals `A_(L,N)^zero`.  A production congruence must still
bind:

```text
one-sided versus two-sided zero sums;
Fourier and Mellin signs;
period length and basis normalization;
parity/even-sector conventions;
endpoint and archimedean terms;
the exact coefficient change of basis.
```

After that finite normalization audit, the remaining substantive estimates are
the complete corrected-tail profile Gram, shrinking-strip derivative LMIs,
line-centered local-Weyl bound, and horizontal phase ledger.

## 9. Proof boundary

- The BV Fourier estimate and absolute zero-side convergence are elementary.
- The radical-tail identities are exact consequences of zero-side vanishing.
- No RH assumption is used.
- The theorem closes a genuine domain/convergence gap, but not the production
  normalization or the cofinal profile inequalities.
- It does not prove RH.
