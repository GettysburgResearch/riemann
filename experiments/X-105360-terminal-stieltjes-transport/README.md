# X-105360 — Terminal Stieltjes transport replay

This standard-library replay authenticates the finite exact scope of
`L-105360`, the atomic part of `T-105360`, and the terminal-slope firewall
`R-105360`.

Run:

```bash
python -B experiments/X-105360-terminal-stieltjes-transport/verify.py \
  --output experiments/X-105360-terminal-stieltjes-transport/results/verification.json
```

Expected verdict:

```text
PASS_X_105360_TERMINAL_STIELTJES_TRANSPORT
43 exact rational checks
```

The checker verifies:

- the exact update

  ```text
  beta_n(inner)=beta_n(outer)+sum_c w_c s_c^n;
  ```

- the boundary-function update

  ```text
  H_inner(z)=H_outer(z)+z sum_c w_c/(1-s_c z^2);
  ```

- exact even and shifted Stieltjes Hankel Gram factorizations through order
  three for a positive outer measure plus two crossed negative-residue pairs;
- the separator `H(z)=z-z^3`, whose terminal slope is positive but whose second
  confluent matrix has determinant `-1`.

Arithmetic class: exact `Fraction` arithmetic.

The replay does **not** evaluate Xi, machine-prove the infinite exhaustion
passage, establish `CRVH105330`, establish `TAIR105360`, establish
`OASH105350`, validate the moving-saddle theorem, or prove RH.
