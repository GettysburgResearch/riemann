# L-106052 — The midpoint temperature tangent splits into two Kummer prime-current charts

Claim ID: `L-106052`  
Programme aliases: `LFAM1.TANGENT_ROOT_FIBRE`, `STRESS.PRIME_CURRENT_CHARTS`, `LFAM2.KUMMER_TANGENT`  
Status: **PROVED EXACT GENERATOR/CHART THEOREM**  
Created: 2026-08-24  
Depends on: `L-106050--L-106051`; PR #719 `L-102900`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

For a character `chi`, put

\[
\Gamma_{t,\chi}
=\sigma_{t,\chi}*\sigma_{t,\chi}.
\]

At the midpoint, with `eta=chi^2`,

\[
\Gamma_{1/2,\chi}=E_\chi*S_\eta.
\]

Let

\[
\Lambda_\chi
=\sum_\ell\log(1+x_{\ell,\chi}).
\]

Differentiating the midpoint square gives

\[
\boxed{
\dot\Gamma_{1/2,\chi}
=2E_\chi*S_\eta*\Lambda_\chi.
}
\tag{L-106052.1}
\]

## 1. Quadratic-root tangent projectors

Let `kappa^2=1` and put

\[
P_\pm(n)=\frac{1\pm\kappa(n)}2.
\]

The two roots `chi` and `chi*kappa` share the same squared completion `S_eta`.
Moreover character twisting commutes with convolution, so

\[
E_{\chi\kappa}*\Lambda_{\chi\kappa}
=(E*\Lambda)\chi\kappa.
\]

The support of `S_eta` consists of arithmetic squares and hence is
`kappa`-trivial. Therefore

\[
\boxed{
\frac{
\dot\Gamma_{1/2,\chi}
\pm
\dot\Gamma_{1/2,\chi\kappa}
}{2}
=
2S_\eta*
P_\pm(E_\chi*\Lambda_\chi).
}
\tag{L-106052.2}
\]

Thus the Hadamard transform of a quadratic root fibre splits the complete
temperature tangent into its two quadratic source classes.

## 2. Critical prime current

Split

\[
\Lambda_\chi
=\Pi_{1,\chi}+\Pi_{\ge2,\chi},
\]

where

\[
\Pi_{1,\chi}(z)
=\sum_\ell\chi(p_\ell)p_\ell^{-z}
\]

and the second term contains powers at least two. Equation (L-106052.2) gives

\[
\boxed{
\frac{
\dot\Gamma_{1/2,\chi}
\pm
\dot\Gamma_{1/2,\chi\kappa}
}{2}
=
2S_\eta*P_\pm(E_\chi*\Pi_{1,\chi})
+
2S_\eta*P_\pm(E_\chi*\Pi_{\ge2,\chi}).
}
\tag{L-106052.3}
\]

The second term has the same polylogarithmic higher-prime-power operator cost
as in PR #719 `L-102900`. The first term is the critical owner/transfer current
split by one quadratic Kummer chart.

For a clean completed product, every nonowner occurs to even exponent. Hence
the chart label of the first term depends only on the unsquared owner product.

## 3. Principal positive inversion

In the principal square channel `eta=1`, let `omega` be the positive
square-lattice inverse of PR #719. Applying it to (L-106052.2) yields

\[
\boxed{
\omega*
\frac{
\dot\Gamma_{1/2,1}
\pm
\dot\Gamma_{1/2,\kappa}
}{2}
=
2P_\pm(\beta*\Lambda).
}
\tag{L-106052.4}
\]

Its first-chaos part is

\[
\boxed{
2P_\pm(\beta*\Pi_1).
}
\tag{L-106052.5}
\]

Adding the two charts recovers exactly the full native prime current:

\[
2P_+(\beta*\Pi_1)+2P_-(\beta*\Pi_1)
=2\beta*\Pi_1.
\tag{L-106052.6}
\]

Neither chart alone is source-complete.

## 4. Function-field reading

Over `F_q[T]`, (L-106052.2) is the quadratic Kummer decomposition of the
completion-temperature tangent. The critical term is a Kummer-twisted prime-
irreducible current, while higher powers remain a bounded geometric gauge.

## Scope

This theorem proves that the scalar temperature drift and the owner-conductor
Kummer phases act on the same prime-current generator. It does not orient the
two chart currents physically, prove `TKCA106050`, `SGIC102890`, or RH.
