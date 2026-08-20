# R-100201 — Neutral-mode cancellation of Hasse edges does not cancel the cube root residual

Claim ID: `R-100201`  
Status: **EXACT LEDGER FIREWALL**  
Created: 2026-08-20  
Depends on: PR #670 and `L-100201`

For a weighted Euler cube with activities \(a_i\), the exact priority-Hasse
flow saturates every odd vertex and leaves

\[
\Delta_B=\prod_i(1-a_i)
\]

at the empty even vertex. For a monotone potential \(\Phi\), the signed cube
scalar has the exact form

\[
\boxed{
\Delta_B\Phi(\varnothing)
+
\sum_{e}J_e\,[\Phi(e^+)-\Phi(e^-)].
}
\tag{R-100201.1}
\]

If the outside source core has the opposite parity, the whole expression is
multiplied by \(-1\). The edge differences possess Fourier factors
\(1-p^{i\gamma}\), so their neutral mode vanishes and their Cauchy energy is
controlled by `L-100201`.

The root term

\[
\pm\Delta_B\Phi(\varnothing)
\]

has no such factor. It is not part of the edge symbol and is unchanged by
averaging the priority order. Therefore an edge-only phase estimate cannot
orient the full arithmetic source.

The exact remaining Route-A object is the cross-core residual

\[
\sum_{\text{outside cores }c}
\sigma(c)\Delta_c\Phi(c),
\tag{R-100201.2}
\]

together with the already controlled edge boundary. A valid closure must
transport or cancel (R-100201.2) between distinct squarefree cores before
physical same-product collapse.

This firewall does not refute phase-Hasse transport. It identifies its first
unpaid term.
