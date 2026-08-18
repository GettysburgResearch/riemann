# X-98400 future-profile invariant

The exact verifier checks quotient closure, transition words, the triangular
state-minimality certificate, the exact normalized Stieltjes bridge, and the
critical exponent algebra.  It also validates the retained metadata of the
selected-horizon `N=10^8` diagnostic.

The large C++ scan uses the exact quotient recurrence but long-double
arithmetic.  It is diagnostic only.

Replay:

```bash
python3 verify.py certificates/control.json --output /tmp/x98400.json
cmp /tmp/x98400.json results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
sha256sum -c SHA256SUMS

g++ -O3 -std=c++17 scan_fcbi.cpp -o /tmp/x98400-scan
/tmp/x98400-scan 100000000 > /tmp/fcbi-100m.json
```
