# T-96200 — Hardened affine–Volterra closure contract after the native-gap correction

Claim ID: `T-96200`  
Status: **CORRECTED CONDITIONAL COMPOSITION; NOT A COMPLETE RH PROOF**  
Created: 2026-08-16

The exact affine-cell compression and all-column physical packing survive. The corrected composition is:

\[
\boxed{
J_\Lambda-\mathcal H(d_X)
=
F_\Lambda+
\bigl(P_\Lambda-\mathcal H(d_X)\bigr).
}
\]

The physical affine–Volterra construction gives
\[
0\le P_\Lambda-\mathcal H(d_X)<3457
\]
on its exact row and retained-cell inputs.

Consequently either of the following closes the endpoint route:

1. prove \(F_\Lambda(X)=o(\log^2X)\) directly;
2. prove a stronger source theorem giving
   \[
   J_\Lambda(X)-\mathcal H(d_X)=o(\log^2X)
   \]
   without replacing \(J_\Lambda\) by the \(Y_4\) pairing.

The second route must carry a declared-score ledger in addition to the physical ordinary/detail ledger.

The previous T-94000 implication is withdrawn. The following remain independently valid:

```text
review-#503 negative firewall;
Volterra rank-one source identity;
affine-cell exact compression;
same-row q / 4q / detail observation;
retained-cell physical error bounds;
one-thinning all-column feasibility.
```

The imported PR #508 tail is not accepted until the MPFR artifact and actual source marginal both pass.

RH remains unproved.
