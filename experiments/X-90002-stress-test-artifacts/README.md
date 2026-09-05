# X-90002 — stress-test artifacts (session 2026-08-08/09)

Backing `claims/refutations/R-90001` and `claims/observations/O-90001/2/3`:

- `cbvr.py`, `scan_chain.py` — CBVR residual-chain debt scan (R-90001); `indep.py` — independent from-scratch confirmation; `chain_results.json` — chain data.
- `sqhinge_lib.py` (exact reference solve), `sqhinge_scan.py`, `sqhinge_rows64.py`, `sqhinge_exact_witness.py` (directed-interval certifier), `sqhinge_results/` — SHARP scans to T=1e8 (O-90001).
- `gfep.py`, `scan.py` — GFEP extension scans (O-90002).
- `carry_profile_sign.py` — carry-profile sign scan on [1,1e7] (O-90003).

Environment: python3 + numpy (+ mpmath for certifications). SHA256SUMS covers all files.
