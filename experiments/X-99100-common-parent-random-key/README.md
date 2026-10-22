# X-99100 — Common-parent random-key interface replay

Run:

```bash
python3 verify.py --output results/verification.json
python3 -m unittest discover -s tests -v
```

The replay checks exact coefficient algebra, a finite common-parent model, normalize-last barycentric transfer, an integral Hall-flow control, and the two mandatory counterexamples. It explicitly records `native_application_established=false` and `rh_established=false`.
