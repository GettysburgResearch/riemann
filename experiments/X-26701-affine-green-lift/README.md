# X-26701 — Exact affine Green boundary-lift regression

This standard-library checker validates finite rational algebra for
`L-26701/L-26702`.

It verifies:

- the endpoint-projected Dirichlet Gram;
- an exact rational Green solve;
- reconstruction of every old carry target;
- the maximum-positive-slope boundary charge;
- pointwise dominance after the affine lift;
- preservation of every old prime-power response;
- one new boundary response at a prime oversupport;
- the formal prime-coordinate objective identity;
- the bound \(C^2\le\mathcal G\);
- five adversarial mutations.

It does **not** verify:

- the actual transcendental parabolic packet;
- the cofinal ABLC estimate;
- the inherited prime-ramp equivalence;
- RH.

Run:

```bash
python experiments/X-26701-affine-green-lift/verify.py
```
