# X-91126 — P61 displacement-eight target Hall

Companion replay for `L-91347`.

```bash
python3 experiments/X-91126-p61-shift8-target-hall/verify.py
```

Expected verdict:

```text
PASS_P61_SHIFT8_TARGET_HALL
```

The standard-library checker uses exact reciprocal-prefix arithmetic and directed fixed-point square-root enclosures. It certifies:

- all `2^18=262144` divisor states of `P_61`;
- the uniform shifted reciprocal-prefix gate `A_8(t)>1/67`;
- the correlated nonterminal Hall lower bound `>9/5`;
- the child-prefix envelope `<3 sqrt(y)` on every activation cell;
- the exact negative radius-seven witness at `t=47`.

Together with the symbolic terminal-threshold argument in `L-91347`, these gates prove that every `P_61` one-prime target packet has a Ferrers transport supported on `e<=o+8`, and that no fixed radius at most seven can work globally.

The replay does not certify score or row subordination of a common transport and does not prove RH.
