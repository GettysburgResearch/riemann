# Trigger the directed PA-1 certificate

This child branch launches the trusted-base workflow

```text
.github/workflows/x12102-directed-pa1.yml
```

for the exact positive anchor

```text
w = 1
x = 1
Re(s) = 3/2
T = 20225875608343133989267 / 2^32.
```

The workflow evaluates the new completed-xi primitive at 512 and 640 Arb bits,
requires functional-equation overlap and precision nesting, reconstructs the
single new moment by both the full seventeen-node and reduced one-point
contractions, and decides both degree-15 half-line moment matrices.

Possible proof-facing verdicts are:

```text
CERTIFIED_NEGATIVE_PA1_H0_SQUARE
CERTIFIED_NEGATIVE_PA1_H1_Y_SQUARE
CERTIFIED_POSITIVE_FULL_DEGREE15_PA1_CONE
UNRESOLVED_PA1_CONE.
```

No sign is asserted by this trigger file. A strict negative remains a nomination
pending independent completed-xi reproduction and review of the inherited
response and atomized count-deflation gates.
