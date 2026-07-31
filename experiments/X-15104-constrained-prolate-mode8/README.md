# X-15104 — exact constrained prolate mode-8 algebra

This experiment checks the finite rational identities used by `L-15110`.

It verifies one four-mode synthetic system with

```text
defects                  1/1000, 1/100, 1, 2
integral coefficients    3, 4, 5, 0
zero-integral target     (4,-3,0,0)
constrained complement   span{(3,4,-5,0),(0,0,0,1)}
```

The exact outputs are

```text
target Rayleigh                  53/12500
raw mode-next floor              1/2
centered mode-next floor         6197/12500
projected residual squared       729/78125000
Fuchs 4-to-8 rational factor     105/4096
final rational coefficient       105/15488 times sqrt(3)/pi^4
```

Run:

```bash
python verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
python -m unittest discover -s tests -v
```

The checker does not evaluate prolate functions, the Weil form, or zeta. It is a
finite-algebra regression for the proof and rejects false floors, residuals,
constraints, and asymptotic constants.
