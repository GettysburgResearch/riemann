# X-23001 — Finite inverse boundary and principal-part regression

This standard-library-only experiment checks the exact synthetic algebra behind
`L-23006` and `L-23007`.

It verifies:

- the global coefficient identity
  `A_(K,V)=mu-mu*r_V^(*K)` on finite truncations;
- exactness through `V^K`;
- `r_V=mu` on the first shell `(V,2V]`;
- the first K-fold Möbius boundary tensor;
- the adjacent-order identity
  `A_(K+1,V)-A_(K,V)=mu_V*r_V^(*K)`;
- preservation of the complete negative Laurent principal part at synthetic
  zeros of multiplicity one, two, and three;
- disappearance of every negative Laurent coefficient in an order difference.

The result is a regression for finite convolution and local Laurent algebra. It
does **not** prove an asymptotic estimate for the Möbius function, `BTP(K)`, or
RH.

Run:

```bash
python verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
python -m unittest discover -s tests -v
```
