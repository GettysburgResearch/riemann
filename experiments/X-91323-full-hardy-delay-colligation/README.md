# X-91323 — exact full-Hardy delay colligation regression

This experiment checks the finite polynomial model of `L-91323`.

For `Theta(z)=z^m`,

```text
H2 = K_Theta orthogonal-sum z^m H2.
```

A raw integer delay generally moves both the model and completed-amplitude
coordinates. The exact output has three orthogonal channels:

```text
forced model state;
returned amplitude state;
escaped negative-power prefix.
```

The verifier uses exact Gaussian-integer arithmetic to check:

- the explicit block formula, including nonzero amplitude-to-model forcing;
- all pairwise three-channel cross-Gram identities in a five-input packet;
- the upper-triangular state semigroup;
- the escaped-prefix cocycle;
- the full packet Pythagorean identity.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_FULL_HARDY_DELAY_COLLIGATION
```

This is an exact regression for the Hardy geometry. It does not test the
completed arithmetic domination or RH.
