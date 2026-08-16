# T-96200 — Two-row global-shadow Mellin–Landau RH candidate

Claim ID: `T-96200`  
Status: **PROPOSED COMPLETE UNCONDITIONAL RH PROOF CANDIDATE — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Frozen base: PR #542 at `ca5fb69c15cda29b3b589660f9be44ea2f440677`

The candidate chain is

```text
fixed-product equal-knot cancellation                  R-96200
 -> global first-crossing/shadow transport for j=2,3  L-96200
 -> c_X(2),c_X(3) >= 0 for every real X
 -> exact fixed-row reciprocal-zeta Mellin transforms PR #542 / L-96000
 -> two row numerators have no common zero             L-96201
 -> Landau real-abscissa theorem                       L-96202
 -> Riemann Hypothesis.
```

The normalization firewall of PR #541 is respected. The proof does not identify physical `Y4` slack with the arithmetic gap and does not attempt to control `F_Lambda` through a packing cone. It replaces that endpoint consumer with two direct nonnegative row Mellin transforms.

```text
candidate complete on the written theorem chain   yes
accepted proof                                     no
Riemann Hypothesis                                 unproved pending reconstruction
first hostile target                               L-96200 ownership and reservoir exhaustion
```
