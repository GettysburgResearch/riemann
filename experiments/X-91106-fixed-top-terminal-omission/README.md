# X-91106 — Fixed top omission terminal-annulus certificate

Companion replay for `L-91115`.

```bash
python3 experiments/X-91106-fixed-top-terminal-omission/verify.py
```

Expected verdict:

```text
PASS_FIXED_TOP_TERMINAL_OMISSION
```

The checker uses exact `Fraction` arithmetic and directed rational square-root
enclosures. It verifies:

- all three terminal endpoint-derivative brackets exceed `2-sqrt(2)`;
- `2-sqrt(2)>7/12`;
- a top omission of width `W=10000` removes more than
  `5057 X^(-3/2)` of terminal response;
- the complete finite-mismatch and quantization overfill is below
  `4002 X^(-3/2)`;
- the retained strict terminal margin exceeds `1056 X^(-3/2)`.

The analytic endpoint derivative, support, carry and score arguments are in
`L-91115`. The replay does not prove the contracted rough-prime allocation or
RH.
