# X-91670 — single-SHARP normalization hardening

This standard-library exact replay supports `R-91659`, `L-91670`, and the
algebraic shell of `T-91656`.

It checks:

```text
the old balanced/reserve row coefficients sum to 3;
the old one-copy native-row claim is false;
w_Psi = 3 w_(4/3) exactly;
the single-SHARP normalized row produces one Q_Y copy;
the target/score ratio is strictly increasing;
the single-SHARP least-prime recursion is source-disjoint;
60 exact finite-seed Fubini identities;
1,008 formal prime-log score-convolution identities;
the recursive loss coefficient is exactly one.
```

Run:

```bash
python3 verify.py --json results/verification.json
```

Retained verdict:

```text
PASS_SINGLE_SHARP_NORMALIZATION_HARDENING
proof object:
a5b07f68367447da089ef8d8fa84adf2ea2615b4fcbb8f038d7f23cf5dc49dda
```

Scope:

```text
factor-three refutation                         exact
single-channel replacement                      exact
Hall cells                                      not rerun here
outer endpoint certificate                      not rerun here
fixed-67 theorem                                delegated to X-91666
RH established by replay                        false
```
