# X-91118 — Adversarial PR #405 repairs

This small exact replay checks:

- the valid one-factor identity `wN(r)=wM(r)`;
- the exact two-factor cascade excess;
- the fixed diagonalization of the completed matrix family;
- the strict terminal constant `40000>28836`;
- rational radical bounds used in the real-column endpoint proof;
- the exact balanced-channel decomposition of the SHARP atom.

Run:

```bash
python3 verify.py
```

The replay does not certify RH or the open all-generation four-state projection.
