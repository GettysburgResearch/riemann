# M-99812 — Random pairing program for the native rough Euler product

Status: **OPEN PROGRAM; NO RH CLAIM**

`L-99815` proves that every active weighted two-prime Euler block of the conclusion-complete box potential is strictly positive. Direct deterministic composition does not preserve a simple pointwise cone because activation thresholds proliferate.

The next mechanism is to average over pairings of the active rough primes before physical observation.

For a finite active prime set `P={p_1,...,p_k}`, let `Pi` range over perfect matchings when `k` is even. For each matching define

\[
\mathcal B_\Pi=\prod_{\{p,q\}\in\Pi}(I-p^{-1/2}U_p)(I-q^{-1/2}U_q).
\]

Algebraically every `B_Pi` equals the same native Euler product, since the factors commute. The value on `Phi` is therefore independent of the pairing. Pair averaging does not change the target; its purpose is to expose a decomposition of the common value into expectations of positive active two-prime blocks plus activation-boundary correction terms.

A valid proof must derive an exact telescoping identity of the form

\[
\prod_{p\in P}(I-p^{-1/2}U_p)\Phi
=\mathbb E_\Pi\sum_{\{p,q\}\in\Pi} W_{\Pi,p,q}\,\mathcal B_{p,q}\Phi_{\Pi,p,q}
+\mathcal R_P,
\]

with `W>=0`, every shifted potential `Phi_{Pi,p,q}` retaining the active-cube condition, and an explicit remainder `R_P` that is nonnegative or reduces to one unpaired first-owner term.

Averaging alone is not a proof: because all pair products are algebraically identical, any positivity must come from a genuine positive decomposition, not from the expectation symbol. This file is a firewall against silently replacing composition by pairwise positivity.
