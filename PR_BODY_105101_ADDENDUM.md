## Checkpoint 2 — exact fixed-window residue flux

This checkpoint continues T-105100 without heavy computation.

For a real entire \(F\), under explicit simple-zero and pole-free-boundary
hypotheses,

\[
M_{2,F}(T)
=\frac1{2\pi i}\int_{\partial\Omega_{T,\eta}}
\frac{F(z)^2}{F'(z)F''(z)}\,dz
-C_F(T,\eta)-D_F(T,\eta).
\]

The packet expands all four counterclockwise edges, reduces them to two real
flux integrals under parity, and specializes conditionally to
\(F=\Xi^{(k-1)}\), \(k\ge1\).

This closes a direct fixed-window representation only. It does not transport
the global L-105100 \(V_2,V_4\) ledger, prove Xi-derivative simplicity, control
common zeros, supply an admissible asymptotic flux estimate, prove
RCMV104530, or prove RH.

New claims:

- L-105101: complete entire-window residue ledger;
- T-105101: correct continuation frontier;
- R-105101: global-ledger localization firewall;
- M-105101: hostile review contract.

The exact replay uses only rational and Gaussian-rational arithmetic. It
includes executable edge-sign mutations, strict finite-segment boundary
classification, removable-singularity controls, and an independent
\(V_2,V_4\) reconstruction of each global polynomial ledger.

Replay:

    python -B experiments/X-105101-entire-window-residue-flux/verify.py \
      --output experiments/X-105101-entire-window-residue-flux/results/verification.json

    python -B -m unittest discover \
      -s experiments/X-105101-entire-window-residue-flux/tests \
      -p "test_*.py" -v

No Xi evaluation, numerical contour quadrature, broad suite, or heavy
campaign was run.
