# X-93012 — Directed Cycle-Debt certificate replay

Arithmetic class: `EXACT_RATIONAL`  
Claim exercised: `L-93012`

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

The replay constructs exact two-channel sources, rational dual potentials, and
rational lower/upper capacity enclosures. It checks the certified bracket, the
three-part gap identity, contact localization, and hostile mutations.

The rank-sparsity proof is analytic and is not replayed.
The experiment does not export the critical Möbius source, evaluate the true
square-root capacities, prove a cofinal debt bound, or prove RH.
