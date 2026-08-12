# X-91122 — `P_79` terminal target-Hall certificate

Companion replay for `L-91342`.

```bash
python3 experiments/X-91122-p79-terminal-target-hall/verify.py
```

Expected verdict:

```text
PASS_P79_TERMINAL_TARGET_HALL
```

The checker uses only the Python standard library.  With exact `Fraction`
arithmetic and directed rational square-root/logarithm enclosures it proves:

- the no-upward SHARP-target Hall margin is greater than `7/100` for every
  active odd threshold throughout `1 <= x < 83`;
- the minimum directed Hall lower endpoint occurs at threshold `13` and the
  right limit `x -> 83-`;
- every target-normalized component profile
  `Q_Y(j)/(4 sqrt(Y)-3)` is strictly increasing through the same terminal
  window;
- all `3,321` component-cell derivative numerators exceed `1/6`.

The transport-to-positive-measure argument, score superordination, and exact
finite-row factorization are symbolic in `L-91342`.  The replay does not prove
the nonterminal rough source disintegration or RH.
