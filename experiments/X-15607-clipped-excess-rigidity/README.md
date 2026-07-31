# X-15607 — Exact clipped-excess rigidity regression

This standard-library-only checker replays the finite diagonal control for
`L-15621`.

It verifies:

- the exact lower-symbol relation `A >= G I-D`;
- the low-packet compression gate;
- the positive clipped excess;
- the four-defect decomposition;
- the threshold-count inequality;
- the robust complement floor;
- the zero-excess/flat-band equivalence.

Retained control:

```text
G=3, alpha=1, theta=1, eta=1/4
D=diag(2,2,6/5,1/2)
A=diag(1,1,9/5,5/2)
packet=span(e1,e2)

clipped excess                 1/5
uncaptured clipped trace       1/5
count above theta+eta          2
certified complement floor     9/5
actual complement floor        9/5
```

The zero-excess mutation uses `D=diag(2,2,1/2)` and verifies that the clipped
operator is exactly the flat packet projection.

Run:

```bash
python3 -m py_compile verify.py tests/test_verify.py
python3 verify.py certificates/synthetic.json
python3 -m unittest discover -s tests -v
sha256sum -c SHA256SUMS
```

The checker is a finite algebra regression. It does not evaluate the Suzuki
symbol or prove the cofinal clipped-excess bound.
