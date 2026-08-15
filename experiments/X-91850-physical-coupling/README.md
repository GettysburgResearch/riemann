# X-91850 — physical coupling compiler replay

Arithmetic class: `EXACT_RATIONAL`.

```bash
python3 physical_coupling.py
python3 verify.py --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile physical_coupling.py verify.py tests/test_physical_coupling.py
```

The replay checks the abstract Hall input marginals, positive row identity, first-owner and causal kernels, complete tagged cells, one label-blind quantizer, thinning discard, signed-observation firewall, native slack, 64 deterministic randomized fixtures and 15 hostile mutations. It authenticates no imported analytic theorem and does not prove RH.
