# X-zeta23-gaussian-terminal

Replay the finite closed-form algebra and floating controls used by
`GAUSSIAN_TERMINAL_PAIR_ISOLATION.md`:

```bash
python3 experiments/X-zeta23-gaussian-terminal/verify.py
```

Expected classification:

```text
PASS_GAUSSIAN_TERMINAL_PAIR_ALGEBRA
```

The replay checks:

- the exact Gaussian evaluation kernel and normalized correlation formula;
- Hermitian kernel symmetry;
- exact target values `(+1,-1)` for the reflected-pair interpolant;
- the explicit decreasing target norm;
- reflection antisymmetry;
- finite-packet Gaussian decorrelation;
- the parabolic threat-edge depth budget;
- one deterministic terminal-packet leakage regression.

The replay is **not** a zero computation and certifies none of:

- the Riemann–von Mangoldt formula;
- the complete infinite zero-tail estimate;
- admissible-test continuity of the Weil explicit formula;
- an arithmetic lower floor;
- the Riemann Hypothesis.

The mathematical proof of the terminal-vertex theorem and infinite leakage
estimate is in the proof note, not in this finite diagnostic.
