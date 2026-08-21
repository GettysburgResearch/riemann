# Integration handoff — Pascal-cycle MFT normal form

Add after `L-26205` and the ternary refutation:

```text
L-27204  Pascal cycles generate the full split kernel;
M-27201  fail-closed cycle-corrected MFT certificate;
X-27204  exact kernel/basis regression;
O-27203  state-dependent repair warning.
```

This does not replace the MFT hinge. It makes the hinge constructive:

```text
canonical signed balanced tree flow
+ explicit fundamental cycle coordinates
-> nonnegative exact flow.
```

The directed `X=10^7,n=63` ternary counterexample must remain a mutation in any
future cycle producer.
