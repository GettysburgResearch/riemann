# X-91130 — True causal P61 shifted-eight Hall certificate

This experiment verifies the actual causal Hall margins for the `P_61` one-prime splice. Unlike the refuted `L-91350/X-91127` reduction, it retains every parent cutoff `d <= py` and every child cutoff `d <= y`.

Run:

```bash
python3 verify.py
```

The checker uses only the Python standard library, exact `Fraction` arithmetic, and outward fixed-point square-root intervals with scale `10^42`.

It checks all odd `P_61` thresholds below `4096`, every parent activation boundary in `(t,t+8]`, every child activation cell in `1 <= y < 67`, the constraint `py >= t`, both target and score channels, and every possible convex cell minimum. The theorem file supplies an exact analytic bound for all thresholds at least `4096`.

The result certifies target/score Hall feasibility. It does not certify a common row packet, a global reset recurrence, or RH.
