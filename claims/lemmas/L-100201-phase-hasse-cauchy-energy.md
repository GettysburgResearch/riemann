# L-100201 — The phase-Hasse edge boundary has an exact Cauchy energy bound

Claim ID: `L-100201`  
Status: **PROVED EXACT FINITE PHASE-ENERGY THEOREM**  
Created: 2026-08-20  
Inputs: PR #672, `L-99990--L-99991`  
RH status: **not assumed**

Let \(E\) be a finite family of labelled Hasse edges. An edge
\(e=(b_e,p_e)\) has nonnegative mass \(J_e\), base product \(b_e\), and prime
label \(p_e\). Put

\[
M=\sum_{e\in E}J_e
\]

and define the phase boundary symbol

\[
\mathscr S_J(\gamma)
=
\sum_{e\in E}
J_e\,b_e^{i\gamma}(1-p_e^{i\gamma}).
\tag{L-100201.1}
\]

For \(\tau>0\), let

\[
P_\tau(\gamma)=\frac{\tau}{\pi(\tau^2+\gamma^2)}.
\]

Weighted Cauchy--Schwarz gives pointwise

\[
|\mathscr S_J(\gamma)|^2
\le
M\sum_eJ_e|1-p_e^{i\gamma}|^2.
\tag{L-100201.2}
\]

The characteristic function of \(P_\tau\) is \(e^{-\tau|u|}\), hence

\[
\int_{\mathbb R}|1-p^{i\gamma}|^2P_\tau(\gamma)\,d\gamma
=
2(1-p^{-\tau}).
\tag{L-100201.3}
\]

Therefore

\[
\boxed{
\int_{\mathbb R}|\mathscr S_J(\gamma)|^2P_\tau(\gamma)\,d\gamma
\le
2M\sum_eJ_e(1-p_e^{-\tau})
\le2M^2.
}
\tag{L-100201.4}
\]

This closes every interaction *between the edge terms of one prescribed
phase-Hasse boundary* at total-mass scale. In particular, no separate
cross-edge Gram or Schur completion is needed.

If a compact logarithmic potential \(\Phi\) is represented by a Fourier
density whose reciprocal-\(P_\tau\) square norm is finite, then Fourier
inversion and (L-100201.4) give an absolute boundary bound of size

\[
O_\Phi(M).
\tag{L-100201.5}
\]

The theorem is deliberately local to the edge boundary. The untransported
parity residual of each Euler cube is not an edge term and is treated in
`R-100201`.
