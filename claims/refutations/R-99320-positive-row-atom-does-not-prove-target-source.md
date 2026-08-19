# R-99320 — Positive row atoms do not by themselves prove the target source positive

Claim ID: `R-99320`  
Status: **EXACT TYPE FIREWALL**  
Created: 2026-08-19

Let \(\eta_j(t)>0\) be the atom of `L-99320`. For an arbitrary signed scalar
source \(f(t)\),

\[
\int\eta_j(t)f(t)\frac{dt}{t}
\]

need not be nonnegative. Taking \(f=-\mathbf1_I\) on any interval \(I\) gives a
strictly negative row.

The implication used by the candidate is exactly

\[
\text{one source-faithful positive target decomposition}
\Longrightarrow
\text{one positive common row decomposition},
\]

not

\[
\eta_j\ge0
\Longrightarrow
\text{every signed Möbius target is positive}.
\]

This forbids:

- dropping the compact target Hall theorem;
- replacing the exact root target ledger by its total mass;
- taking absolute values before source ownership;
- treating bounded signed calibration as positive source;
- claiming RH from the kernel factorization alone.
