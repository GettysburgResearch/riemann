# Gamma–Dirichlet continuation of the actual branching orbit

**Proposed component proofs; independent review required. RH and the
prescribed orbit's cofinal zero-confinement property remain open.**

This is an add-only continuation of PR #853, frozen at
`e0b82da7ecdd4ed21e47e8b6adbb8c5182eac048`. No prior source is edited.

Read `PROOF.md`, especially §§2–5 for the positive construction and §6 for the
attempted finishing inequality's failure on the *actual* first iterate.

For X_0~Gamma(5/2,rate5/2), X_(n+1)=(X_n+X_n')/U², the exact factorization is

    X_n=Gamma((5/2)2^n,rate5/2) * Z_n,
    C_n=B_n Z_n+(1-B_n)Z_n',  B_n~Beta((5/2)2^n,(5/2)2^n),
    Z_(n+1)=C_n/U²,   4^-n<=Z_n,C_n<=1.

The gamma factor and bounded variable are independent. It follows that the
complete paired Mellin transform is a gamma factor times the entire compact
mixing transform J_n(s)=E C_n^(s/2). All mixing moments are rational and have
an explicit recursion. Every pole and its order are identified. A centered
reciprocal-gamma normalization yields *entire* E_n converging locally uniformly
to xi on C and preserving the original H_n critical-strip zeros exactly.
This does not establish their zero locations.

The directed test proves

    -1.427840092064 <
       d/dsigma log|M_1(sigma+23i)/M_1(1-sigma-23i)| at sigma=1/2
    < -1.427840092063.

It uses the prescribed Gamma(5/2) law, not the preceding Gamma(1) countertest.
It rejects one natural modulus-monotonicity induction. It is **not a zero of
any function**, and does not refute zero-safety of this special orbit.

## Run

The sibling predecessor directory `2026-09-10-astra-branching-order/` must be
present; its `certificate.py` is authenticated before its exact interval
primitives are loaded. The download includes the unchanged predecessor.

```sh
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
sha256sum -c SHA256SUMS
```

`--write` is producer mode, not acceptance. The result records false RH and
zero-preservation flags. The five tests include actual subprocess refusals;
their real exit status controls the printed verdict. There is no conditional
unittest skip advertised as a passed check.

See `VALIDATION.md` for exact execution scope and unperformed checks,
`SOURCES.json` for frozen dependencies, and `REVIEW.md` for questions. The
all-depth analytic statements remain paper proofs, not consequences of the
bounded Python cases.
