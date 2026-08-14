# X-19882 — Exact three-route native-slack regression

This experiment is a `fractions.Fraction`-only synthetic regression for the
three new abstract results:

```text
L-19882  exact native detail-slack cocycle;
L-19883  four depth graph-Grams and generator intertwining;
L-19884  positive derivative-Hankel and Stieltjes double-Laplace string.
```

It also checks a finite subcritical affine-cost recurrence and the exact
discrete geometric analogue

\[
 \sum_{n=u}^{\infty}z^n(n-u)
 =\frac{z^{u+1}}{(1-z)^2}.
\]

## Run

```bash
python3 verify.py certificates/control.json \
  --output /tmp/x19882-verification.json
cmp /tmp/x19882-verification.json results/verification.json
python3 -m unittest discover -s tests -v
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_THREE_ROUTE_NATIVE_SLACK_PACKET
```

Retained proof-object digest:

```text
40097c04506b682b960086650a6d99ead02c5af877686d3de7285904bedd13b4
```

## What is exact

The checker verifies:

1. current response + root slack + full child capacities equals the parent
   native capacity;
2. insertion of child rows gives
   `final_slack = root_slack + sum alpha child_slack`;
3. the same equality holds after pairing with `Y_4`;
4. the total child coefficient is below `1/8`;
5. an affine local-cost recurrence stays within its geometric envelope;
6. all four graph-Gram blocks `(0,0),(0,1),(1,0),(1,1)` agree;
7. the explicit splitting isometry intertwines the depth generators;
8. a positive damped defect measure gives a PSD derivative Hankel matrix;
9. its finite Stieltjes data pass both truncated Hankel tests;
10. eleven fail-closed mutations are rejected.

## Boundary

This replay does **not**:

```text
reconstruct PR #473's common-parent factor-67 packet;
prove its native weighted root-slack bound;
construct the Xi depth graph-Gram completion DGGC_a;
prove the passive source identification PSI_a;
establish the Riemann Hypothesis.
```
