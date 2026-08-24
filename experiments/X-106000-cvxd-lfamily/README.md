# X-106000 — CV/XD L-family squareclass moment replay

This standard-library replay authenticates the finite algebra in
`L-106000--L-106003` and `R-106000`.

Run:

```bash
python3 experiments/X-106000-cvxd-lfamily/verify.py \
  --output experiments/X-106000-cvxd-lfamily/results/verification.json
```

Expected:

```text
PASS_X_106000_CVXD_LFAMILY_SQUARECLASS_MOMENTS
exact_checks=376476
proof_object_sha256=a23b1c5a739a5634593df8c6ec750a857dd8690e79c31fc8b195f0859c2786d1
hybrid_collision_line_moment_proved=false
bqsp102870_proved=false
rh_established=false
```

## Exact checks

The replay uses integers, `fractions.Fraction`, and explicit finite-field
arithmetic. It checks:

- principal Euler completion for moduli `5,7,11,13`;
- marked-67 completion after the ramified completion;
- cyclic character orthogonality;
- exact rational character second moments;
- squareclass collision-line factorization over prime fields;
- quadratic core blindness and nonquadratic core visibility;
- the counting proof of the finite-field Gauss norm;
- complete additive line sums;
- collision geometry over
  `F_9 = F_3[x]/(x^2+1)` and
  `F_25 = F_5[x]/(x^2+2)`;
- the elementary family-dimension barrier.

## Boundary

The replay does **not**:

- evaluate zeta or a Dirichlet `L`-function;
- evaluate a function-field Frobenius matrix;
- prove incomplete weighted Gauss cancellation;
- prove the hybrid collision-line family moment;
- prove principal leverage at subpower cost;
- prove `BQSP102870`;
- prove RH.
