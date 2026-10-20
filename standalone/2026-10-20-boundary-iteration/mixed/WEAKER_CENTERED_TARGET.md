# A weaker centered estimate would already move the endpoint

20 October 2026. **Conditional research target only.** No estimate with
the positive saving below has been proved.

The exact diagonal cancellation is in
`CENTERED_INVERSE_INTERFACE.md`. This note calibrates a smaller
analytic target than bounding the entire raw inverse moment at row
scale in a longer column range.

Let \(H\) and \(D\) be the original inverse row and column
lengths. In the initial Poisson transformation put \(K=D^2/H\).
The normalized return factor is \(H/D\). After the original
diagonal and principal restoration are accounted for, let
\(\mathcal C\) denote the full signed off-diagonal expression
with this factor removed. It must retain all common-divisor sums,
punctures, shared smooth kernels, ray sectors, and actual masks.
The notation is not an isolated positive canonical child norm.

Suppose one could prove, in a fixed neighborhood of the binding
lengths, a complete return estimate of the form

\[
 I(H,D)\ll H+(H/D)K^{5/6-\theta}D^{1/6+\theta},
                  \qquad \theta>0.                    \tag{W1}
\]

A sufficient route would bound the full \(\mathcal C\) by the
displayed two-parameter power, with the same uniformity and losses
as the source. The power at \(\theta=0\) corresponds to the
existing amplified inverse exponent; no isolated-child version of
that centered assertion is inferred here.

For \(H=U,D=U^r\), direct substitution into (W1) gives

\[
 e_\theta(r)=\max\{1,\ 1/6+5r/6-\theta(r-1)\}.        \tag{W2}
\]

Thus the exponent saving at a long length \(r>1\) is
\(\theta(r-1)\). The desired cancellation need not reach the
stronger target \(\mathcal C\ll D\).

Use the scalar notation \(q=\delta P_\kappa(x)/D_\kappa(x)\),
\(L=5/6-\delta\) from
`CONDITIONAL_BOUNDARY_SENSITIVITY.md`. On the locally dominant
long branch, the new count is

\[
 R_{{\rm long},\theta}(t)=1/6+\theta+(L-\theta)t.
\]

Its crossing with the unchanged short count is

\[
 t_\theta=\frac{L+3q/2-\theta}{L+q-\theta},\qquad
 R_\theta=1-\delta+q(3/2-t_\theta),\qquad
 \left.\partial_\theta R_\theta\right|_0
             =-\frac{q(t_0-1)}{L+q}.                  \tag{W3}
\]

These formulas are local: \(L-\theta>0\), the crossing remains
inside the licensed range, and the flat contribution in (W2)
does not dominate. All are strict at the inherited critical class
for sufficiently small positive \(\theta\). Away from its
neighborhood the original estimates can be retained.

More generally, if an analytic improvement lowers the long inverse
exponent by \(\varepsilon_{\rm inv}\) at that critical crossing,
then its first-order effect on the optimized count is

\[
 \Delta R=-\frac{q_0}{L_0+q_0}\varepsilon_{\rm inv}
            +o(\varepsilon_{\rm inv}).                \tag{W4}
\]

The change of the crossing cannot be omitted; simply subtracting
the full inverse saving from the finished count would overstate
the gain.

Let \(\lambda=E_\ell\), and evaluate the source endpoint derivatives
at the critical point. The same implicit-function calculation as
the neighboring sensitivity note gives

\[
 \frac{dB}{d\varepsilon_{\rm inv}}\bigg|_0
 =-\frac{3h_0q_0}
 {16(L_0+q_0)(\lambda-E_\kappa/2)},\qquad
 \frac{dB}{d\theta}\bigg|_0
 =-\frac{3h_0q_0(t_0-1)}
 {16(L_0+q_0)(\lambda-E_\kappa/2)}<0.                  \tag{W5}
\]

Here the derivative changes only the local limiting scalar endpoint;
the comparison still requires strict source margins and a final
decrease of \(\ell\). The first-order shifts of the optimizing
\(\delta,b\) do not contribute because their endpoint derivatives
vanish at the critical point.

The unconditional cubic dispersion estimates inspected during this
session do not establish (W1). Their Fourier transform removes a
cubic Gauss coefficient against a cubic row character. The present
row is sextic; its Gauss multiplication instead returns the original
Möbius family through \(\gamma_1\gamma_2=\mu\alpha G\).
Likewise, the new positive pure-cubic mean has no estimate for the
signed two-profile expression in (W1). These are the unresolved
analytic interfaces, rather than a scalar optimization gap.
