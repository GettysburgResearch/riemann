# X-91324 — exact renormalized Fisher-feature regression

This experiment checks the algebraic renormalization in `L-91325` on a finite
exponential family whose probabilities and quarter-turn characters are all
Gaussian rationals.

The source has support `{-1,0,2}`, base masses `(1,2,3)`, and tilt
`exp(-a)=1/2`, giving probabilities `(8,8,3)/19`. At three nonzero
quarter-turn frequencies the verifier checks exactly:

```text
k_t = varphi(t) h_t;
E h_t = E k_t = 0;
-partial_a log Theta(t) = E[sigma h_t]
                       = E[sigma k_t]/varphi(t);
K(t,t) = |varphi(t)|^2 H(t,t);
|k_t(Y)|^2 <= 4.
```

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_RENORMALIZED_FISHER_FEATURE
```

The finite regression verifies the exact renormalization identities. The
safe-line exponential decay and Hardy uncertainty theorem in `R-91324` are
analytic proofs, not numerical claims.
