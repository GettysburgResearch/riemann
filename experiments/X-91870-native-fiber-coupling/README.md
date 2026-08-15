# X-91870 — Native-fibre physical-coupling audit

Run:

```bash
python3 native_fiber.py --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile native_fiber.py verify.py tests/test_native_fiber.py
```

The exact-rational replay checks native-source marginal typing, sector and owner
partitions, Hall marginals, actual one-use physical placements, tagged complete
cells, one label-blind quantizer, small-`q` coverage, ordinary `q/4q` assembly,
detail slack, `Y_4` price and endpoint orientation. It also checks Möbius
convolution and unique small/rough factorization through 5000.

It does not replay the frozen analytic AVLT, endpoint quadrature, all-column
estimates, prime-square theorem or Mellin--Landau theorem and does not establish
RH.
