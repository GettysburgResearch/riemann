# X-zeta23-xi-cardinal-capture

This regression exercises the finite Hilbert-space algebra behind
`XI_CARDINAL_GRAM_CAPTURE.md` on a planted-zero toy entire function

```text
F(z)=P(z) sqrt(pi) exp(-z^2/4).
```

The inverse Fourier source of the exact target-pair cardinal difference is a
polynomial-Hermite multiple of `exp(-u^2)`.  It is therefore an explicit member
of every weighted strip space used by the theorem.

The verifier checks:

- exact cardinal values `(+1,-1,0,...)` at the planted zero packet;
- positivity of the strip evaluation Gram
  ```text
  kappa_a(z,w)=4a/[4a^2+(z-conj(w))^2];
  ```
- monotonic increase of the minimum capture cost as nuisance constraints are
  added;
- the packet-independent upper bound supplied by the weighted cardinal-source
  norm;
- equality of inverse-Gram and target-Schur capture costs;
- the rank-one target-Schur lower bound;
- convergence of compact exponential-window Grams to the strip Gram;
- exact local Weil value `-2` for the reflected pair.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_XI_CARDINAL_GRAM_CAPTURE
```

The computation is a regression of the algebra only.  The theorem's zeta input
is the classical Riemann Xi Fourier kernel and the analytic zero-resolvent
argument in the proof note.
