# X-15604 — Exact terminal-prime visible-block checker

This experiment checks the finite rational trust boundary of `L-15610` and
`T-15603`.

It performs no zeta, prime, gamma, or interval special-function evaluation. A
production producer must supply directed rational matrices and source hashes.

The checker verifies:

1. a positive packet metric;
2. the exact matrix pole-cancellation identity
   
   ```text
   raw terminal + polar
     = centered terminal + finite polar cross terms;
   ```
3. the operator-norm moat
   
   ```text
   theta^2 G - E G^-1 E >= 0;
   ```
4. the one-radius visible margin
   
   ```text
   beta=sigma^2-theta-omega-omega^2/h > 0;
   ```
5. the final radical/cross/assembly floor.

The retained synthetic packet has

```text
G=I_2,
E=[[1,2],[2,-1]],
theta=9/4,
sigma^2=3,
omega=1/4,
h=1.
```

Since `E^2=5I`,

```text
theta^2 I-E^2=(1/16)I.
```

The exact visible margin is

```text
7/16,
```

and the complete synthetic floor is

```text
-17/1000.
```

Proof-object SHA-256:

```text
efe937d456d9ea26977f7349468b9a70d293dbfd53b663e77f10c3d1a4100903
```

Run:

```bash
python experiments/X-15604-terminal-prime-visible/verify.py \
  experiments/X-15604-terminal-prime-visible/certificates/synthetic.json

python -m unittest discover \
  -s experiments/X-15604-terminal-prime-visible/tests -v
```

Eight adversarial tests pass. These are synthetic exact controls, not a
production Suzuki-symbol or RH certificate.
