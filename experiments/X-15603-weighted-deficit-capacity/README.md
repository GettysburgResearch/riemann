# X-15603 — Exact weighted-deficit capacity regression

This standard-library-only experiment verifies the finite algebra behind
`L-15610`, `L-15611`, and `L-15612`.

It checks three logically independent facts.

1. **External source repair preserves rank.** Starting from
   `P=span(e1,e2)`, the constraint `ell(x)=x1+2x2+x3`, and the external
   corrector `Q(c)=c e3`, the graph repair gives `e1-e3,e2-2e3`. Both repaired
   vectors satisfy the constraint, and their exact Gram has positive LDL pivots
   `2,3`. The packet dimension remains two.
2. **Weighted-deficit index saturation needs no subspace alignment once the
   low-Rayleigh gate is imposed.** The synthetic deficit operator has
   eigenvalues `3/2,6/5,1/2,1/10` and threshold `G-Gamma=1`, so its exact
   dangerous index is two. A different two-dimensional packet nevertheless has
   its complete compression below `t=19/20`, forcing
   `N_A(t)=N_A(Gamma)=2` by min--max.
3. **Low compression automatically captures deficit trace.** The same packet
   satisfies `A|L <= alpha I` with `alpha=17/20`. Since `A=G I-D`, it captures
   at least
   ```text
   dim(L) * (G-alpha) = 23/10
   ```
   of the total deficit trace `33/10`. The uncaptured trace is therefore at
   most `1=G-Gamma`, giving the exact complement floor `Gamma=1` without a
   principal-angle calculation.

Run:

```bash
python experiments/X-15603-weighted-deficit-capacity/verify.py
```

Expected verdict:

```text
PASS_EXACT_L15610_L15611_L15612_REGRESSION
```

Proof-object SHA-256:

```text
54957a3ec9eae3ebf59d06576b996f4baf7126e214281d5add7d5dc9f3cbf726
```

This is a synthetic exact regression. It does not evaluate the Suzuki symbol,
build a production zeta radical packet, prove the cofinal integrated-deficit
margin, or prove RH.
