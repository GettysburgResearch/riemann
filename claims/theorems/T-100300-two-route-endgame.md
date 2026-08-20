# T-100300 — Two strongest closure endgames after the latest repository wave

Claim ID: `T-100300`  
Status: **UNCONDITIONAL INTEGRATOR; TWO EXPLICIT RH-EQUIVALENT GATES OPEN**  
Created: 2026-08-20  
Base: PR #680 at `64e8e138dde15bfdb02d532041ace945c600c912`  
External sources: PRs #676, #679, #681  
RH status: **unproved**

After the native-source, normalization, spectral-abscissa, positive-flux, and
Hasse-divergence audits, the minimal-wavelet Hardy square is a diagnostic
equivalent to RH rather than an independent proof. The two strongest remaining
mechanisms are the following.

## Route A — one-sided critical activation coarea

The centered-Bernstein hierarchy proves every supercritical carrier remainder.
PR #679 reduces the first critical quadratic envelope to three moments on each
activation cell. `L-100300` integrates every negative excursion exactly:

\[
\mathfrak D(Y)
=
\sum_I
\sum_{(\alpha,\beta)\subset I,\ P_I<0}
\left[
-2A_I\log t+\frac{2B_I}{t}+\frac{C_I}{t^2}
\right]_\alpha^\beta.
\]

No global pointwise conjecture is needed. The exact conclusion gate is

\[
\boxed{\mathrm{CATD}_{100300}:\ \mathfrak D(Y)=Y^{o(1)}.}
\]

`L-100301` proves

\[
\boxed{\mathrm{CATD}_{100300}\iff RH.}
\]

Its remaining content is a one-sided sum of explicit prime-activation Turán
deficits.

## Route B — zero-moment Vaughan dispersion

Apply one additional boundary-safe half-order notch to the ordinary-Möbius
minimal wavelet. `L-100310` proves a genuine \(Y^{-3/2}\) complete-lattice
estimate. The exact Vaughan identity then gives

\[
\mathcal W_1(X)
=
O(X^{-1/6})
+
\mathcal B_{\lfloor X^{1/3}\rfloor}(X),
\]

where

\[
\mathcal B_U(X)
=
\sum_{\substack{r,s>U\\X/16\le rsm\le X}}
\frac{a_U(r)a_U(s)\mu(m)}{\sqrt{rsm}}
K_1(X/(rsm)).
\]

All Type-I, carrier, diagonal, and normalization terms have disappeared. The
exact conclusion gate is

\[
\boxed{
\mathrm{BVD}_{100310}:\ 
\int_2^Y(\mathcal B_{\lfloor X^{1/3}\rfloor}(X))_-\frac{dX}{X}
=Y^{o(1)}.
}
\]

`L-100312` proves

\[
\boxed{\mathrm{BVD}_{100310}\iff RH.}
\]

## Final disposition

```text
Route A supercritical hierarchy              proved
Route A exact cell/minimum/jump ledger       proved
Route A cellwise negative-area coarea        proved
CATD100300                                   open / RH-equivalent

Route B extra half-order zero moment         proved
Route B complete Type-I decay                proved
Route B exact Vaughan decomposition          proved
Route B integrable unbalanced term           proved
BVD100310 balanced trilinear                 open / RH-equivalent

Riemann Hypothesis                           unproved
```

The routes are genuinely distinct at their last arithmetic step: Route A is a
one-sided activation/Turán problem for the duplicate-67 critical envelope;
Route B is a signed compact trilinear dispersion problem for the ordinary
Möbius source.
