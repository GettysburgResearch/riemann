# HBR29 — native two-scale cutoff and high-mode Mellin control

**Status:** proposed component mathematics; independent review required. RH is not proved.

**Exact source:** HBR28 / PR #872 at `45281093179434e08d28d8e589a8c70d70ead5b9`. This is an add-only proposed continuation, not a change to that packet or main.

## Results

The comparison Mellin mass has square-root Laplace coordinate `r=log(2c)+O(1)`, while the native survival cutoff has `r=2log(2c)+O(1)`, where `c=2m-1`. This separation removes the predecessor's factorial-loss error estimate.

- A complete, explicit normalized absolute Mellin error is at most `2 c(c+2)(3/5)^c+192/c`, uniformly over every imaginary height in `0<=Re s<=1`.
- On `|Im s|<=K log(2c)`, the normalized comparison and native functions have the zero-free gamma profile `Gamma(1+i Im(s)/log(2c))`. Their **relative** ratio is `1-2^(1-s)/c [1+i Im(s)/log(2c)+o_K(1)]`, with both infinite tails controlled.
- This gives growing-window nonvanishing for the MODE functions, not Xi. The forced boundary zero at `s=0` is retained in the raw companions.
- Every sufficiently high individual odd-reflected companion has BOTH phase signs on a suitable fixed band segment. It cannot supply the proposed all-band phase ending.
- The exact finite arithmetic-shift coefficients are a classical Meixner–Pollaczek family, with an explicit symmetric tridiagonal matrix. Its eigenvalues are NOT Xi zeros.

Read [PROOF.md](PROOF.md), then [REVIEW.md](REVIEW.md). The open step is a signed combination or a genuinely source-specific descent preserving exclusion of off-critical zeros. No such theorem is supplied. The positive-response homotopy in #876 is a different construction and is not completed here.

## Reproduce the bounded checks

From this directory:

```sh
python -I -S -B check.py --check result.json --self-test
python -I -S -B -O check.py --check result.json --self-test
```

Each command authenticates the complete packet, reconstructs **1,605** exact rational controls, accepts a pristine copied CLI, and rejects eight actual changed-copy CLI invocations. One mutation changes the native delayed primitive from 4 to 3 after resealing the manifest; independent native moments detect it. Duplicate keys and numerical type aliases are rejected. No `assert` implements acceptance.

`check.py --write PATH` is producer-only and unauthenticated. Normal and optimized execution use the SAME backend and author; this is not independent mathematical review or a proof-assistant formalization. The checksum inventory is reproducibility information, not a signature or protection against arbitrary replacement of the whole checker.

## Optional floating diagnostics

```sh
python -B diagnostic.py --output /tmp/hbr29_coarse.json
python -B diagnostic.py --fine --output /tmp/hbr29_fine.json
```

Requires NumPy and SciPy. Each configuration uses four modes and 36 complex panels. This is **NONCERTIFYING** method-of-steps ODE integration and quadrature. The origin uses a leading Taylor term, the real integral is truncated, all errors are nondirected, and at c=2047 the tiny epsilon underflows to zero. Agreement is diagnostic, not an enclosure. Retained JSON files do not enter mathematical acceptance, except that their bytes are bound by the packet inventory.

## Publication and delivery

The authoring session did not push or open a PR. The connector exposed reads but no write action; no authenticated CLI publication was available. The supplied patch targets the frozen #872 head, with suggested branch `research/astra/20260912-two-scale-brownian-cutoff`. The predecessor's fifteen files, all other research, main and canonical/formal status are unchanged.

A separate publisher must record the ACTUAL resulting remote SHA and PR URL. Do not count the local fixture tree as a repository head or the author checks as an independent review.
