# X-zeta23-tensor-phase-hilbert

Replay the finite arithmetic and root-of-unity identities used by
`TENSOR_PHASE_CURRENT_HILBERT_BOUND.md`:

```bash
python3 experiments/X-zeta23-tensor-phase-hilbert/verify.py
```

Expected verdict:

```text
PASS_TENSOR_PHASE_CURRENT_HILBERT_BOUND
```

The replay checks:

- tensor root-of-unity DFT of every bare-source and current subset mode;
- the exact critical frame constant `5^k`;
- the binomial current/gauge collapse;
- phase-separated first moment and cancellation of every modeled phase-dependent second-moment term;
- the two-layer support law for `b_sharp=(epsilon-4 delta_4)*mu` through 20,000;
- at-most-two-mode overlap at every coefficient;
- weighted coefficient bounds for derivative orders zero, one, and two;
- the coherent channel-to-polynomial critical norm bound.

The replay does not certify the Montgomery–Vaughan theorem, the complete
reflected/Weil arithmetic floor, or RH.
