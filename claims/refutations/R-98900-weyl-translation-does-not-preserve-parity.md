# R-98900 — Weyl translation does not preserve the Fock parity coefficient

Claim ID: `R-98900`  
Status: **PROVED EXACT OPERATOR COUNTERIDENTITY**  
Created: 2026-08-18  
RH status: **not assumed**

Let `Gamma_s(H)` be bosonic symmetric Fock space, let

\[
\Pi=(-1)^{\mathsf N}=\Gamma(-I)
\]

be number parity, and let `W(f)` be the Weyl displacement.  The standard CCR
relations give

\[
\boxed{\Pi W(f)\Pi=W(-f).}
\tag{R-98900.1}
\]

Consequently

\[
\begin{aligned}
W(f)^*\Pi W(f)
 &=W(-f)\Pi W(f)\\
 &=W(-f)W(-f)\Pi\\
 &=\boxed{W(-2f)\Pi},
\end{aligned}
\tag{R-98900.2}
\]

with no phase in the last product because the two Weyl arguments coincide.
Thus a nonzero Weyl translation does **not** leave the trace-free parity
observable invariant.

For the Fock vacuum `Omega`,

\[
\langle\Omega,\Pi\Omega\rangle=1,
\]

whereas

\[
\boxed{
\langle W(f)\Omega,\Pi W(f)\Omega\rangle
 =\langle\Omega,W(-2f)\Pi\Omega\rangle
 =e^{-2\|f\|^2}.
}
\tag{R-98900.3}
\]

Therefore the assertion in PR #613 `L-98703`, step 3, that the pole carrier
may be removed by a Weyl translation which is unitary and hence “does not
affect the trace-free parity matrix coefficient” is false for every `f!=0`.
The missing compensator `W(-2f)` carries exactly the parity response of the
removed coherent carrier.

This refutes the published proof of `L-98703.1`; it does not prove that no
other heat-energy estimate can exist.
