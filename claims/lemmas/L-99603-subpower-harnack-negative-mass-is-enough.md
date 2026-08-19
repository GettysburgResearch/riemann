# L-99603 — Subpower logarithmic negative mass of the SHARP Harnack defect implies RH

Claim ID: `L-99603`  
Status: **PROVED EXACT CONDITIONAL ANALYTIC THEOREM**  
Created: 2026-08-20  
Depends on: the exact SHARP Harnack transform of PR #647  
RH status: **not assumed**

Let

\[
\Psi(x)=\sum_{n\le x}\frac{\mu(n)}{\sqrt n}
       (4\sqrt{x/n}-3)
\]

with causal zero extension, and put

\[
\mathfrak H_{67}(x)
=
\Psi(x)-67^{-1/2}\Psi(x/67).
\tag{L-99603.1}
\]

Its exact Mellin transform is

\[
\mathcal M_H(s)
=
\frac{(1-67^{-(s+1/2)})(s+3/2)}
{s(s-1/2)\zeta(s+1/2)}.
\tag{L-99603.2}
\]

Define

\[
H_-(x)=\max\{-\mathfrak H_{67}(x),0\},
\qquad
N(T)=\int_1^T H_-(x)\frac{dx}{x}.
\tag{L-99603.3}
\]

Assume

\[
\boxed{N(T)=T^{o(1)}.}
\tag{L-99603.4}
\]

Then for every \(\sigma>0\), dyadic summation gives

\[
\int_1^\infty H_-(x)x^{-\sigma-1}\,dx<\infty.
\tag{L-99603.5}
\]

Indeed, for every \(\varepsilon<\sigma\), (L-99603.4) gives
\(N(2^{m+1})\ll_\varepsilon2^{\varepsilon m}\), while the contribution of
\([2^m,2^{m+1}]\) is at most

\[
2^{-\sigma m}
\bigl(N(2^{m+1})-N(2^m)\bigr).
\]

The resulting geometric series converges locally uniformly in
\(\Re s>0\). Thus the Mellin transform \(\mathcal M_-(s)\) of \(H_-\) is
holomorphic there.

Now put

\[
H_+(x)=\mathfrak H_{67}(x)+H_-(x)\ge0.
\]

Its Mellin transform is

\[
\mathcal M_+(s)=\mathcal M_H(s)+\mathcal M_-(s).
\tag{L-99603.6}
\]

The added term is holomorphic in `Re(s)>0`, so it cannot cancel a nontrivial
reciprocal-zeta pole. It also introduces no positive-real singularity. Landau's
theorem applied to the nonnegative density \(H_+\) therefore excludes every
zeta zero with real part greater than \(1/2\). Functional-equation symmetry
gives RH.

Hence

\[
\boxed{
N(T)=T^{o(1)}
\quad\Longrightarrow\quad RH.
}
\tag{L-99603.7}
\]

This is strictly weaker than PR #647's pointwise tail
\(\mathfrak H_{67}(x)\ge0\). It permits sparse or shallow negative excursions
and is the preferred scalar closure target for martingale, Type-II, or density
methods.
