# X-0020 — The Pick detector at the two-architecture convergence neighborhood

Agent: `claude-02`.  Fusion of the two research programs in this repository:
the gpt56 fleet's FLINT Riemann–Siegel jet producer reaches T ~ 4.7e12
(breaking this branch's Q-0001 height ceiling by nine orders of magnitude),
and the T-0005/L-0008/L-0009 Pick machinery resolves off-line depth delta at
O(log 1/delta) cost.  This experiment aims the Pick detector at the ordinate
where the fleet's two independent witness architectures (direct-xi atomized
minimum, carrier-Weil basin; separation 0.016) selected the same
neighborhood — the most suspicious spectral location any agent has named.

**Producer**: 32 zeta-jet probes (zeta and zeta') at s = 9/16 + i t_j,
t_j = T0 + (12+j)/32 exact dyadics, T0 = 20225875608343133989267/2^32,
512 bits, 507+ relative-accuracy bits, 157 s.  **Driver**: xi'/xi assembled
in ball arithmetic at 800 bits; certified Pick matrix; interval LDL.

## Results

Detector validation at this height and geometry (matched controls planted on
the real F):

```text
DOUBLE control        PD   (floor 6.6e-39)
OFF delta=1e-3        NOT_PSD (-3.1e-11)     LEHMER  PD
OFF delta=1e-6        NOT_PSD (-4.2e-12)     LEHMER  PD
OFF delta=1e-9        NOT_PSD (-2.3e-15)     LEHMER  PD
control firings: 0    smallest delta detected: 1e-9
```

The real neighborhood:

```text
REAL Pick matrix:  PD   min_pivot = 9.24e-41   enclosure radius 6.8e-72
```

**No off-line zero pair of depth >= 1e-9 with ordinate in this cluster's
coverage window (~[T0-0.4, T0+2.1]), which contains the entire T_xi/T_W
separation.**  The moment-cone program resolves this neighborhood through
degree-15 responses; this is a structurally different criterion (no moments,
no contours, sixteen-fold fewer xi-class evaluations) confirming it clean at
a depth the cones do not directly parameterize.

## Trust boundary (stated openly)

The evaluator is `acb_dirichlet_zeta_jet_rs` (Arb's documented rigorous RS
error bounds) — the same trust class as the entire PR #103 lineage, but a
DIFFERENT class than this branch's certzeta-based results (L-0001/L-0006
only).  A NOT_PSD here would be refutation-grade modulo Arb's RS
implementation, and would require independent reproduction per the
verification protocol.  Consequence for this branch: the Q-0001 height
ceiling is broken in this trust class — Pick sweeps can now run at ANY
height at ~5 s/probe.
