# Consecutive zeta-zero isolation above the Platt–Trudgian endpoint

**Status.** New finite computation for review. The published anchor is $T_0=3\,000\,175\,332\,800$, with $N(T_0)=12\,363\,153\,437\,138$ nontrivial zeros of positive ordinate, all on the critical line. We extend the indexed sign-isolation stream starting with that last published index. Each numbered checkpoint gives its own exact count, guard, integer height and archive digest. The theorem being extended is explicitly identified; no claim of computational priority is made. [Platt–Trudgian, Theorem 1](https://doi.org/10.1112/blms.12460)

The [30,000-index checkpoint](checkpoint-0003.json) reaches integer height 3,000,175,339,809. At that integer the independent total count is 12,363,153,467,135. Three more indexed brackets are present through the final guarded neighborhood. The number of new **indices** and the difference of counts at the displayed **integer** have these different rounding conventions.

## Why a block certifies total-strip coverage

FLINT 3.6.0 evaluates the real scaled completed zeta function on the critical line by Platt's rigorous multi-evaluation with interpolation and error bounds. An opposite-sign pair supplies an open interval containing a critical-line zero. Indexed completeness uses Turing's method in addition to the signs. In FLINT's convention $N(t)$ counts all nontrivial zeros in the full critical strip with $0<\Im\rho\le t$, with multiplicity. Sufficient runs of good Gram blocks on both sides of a shared Gram point force equality between this count and its Gram index plus one. Between successive such anchors the difference of counts is known exactly. The implemented test separates at least that many sign changes before returning the indexed brackets. Consequently each returned interval accounts for one simple critical-line zero and there is no missing off-line zero in the associated indexed segment. Input precision and the Fourier-grid tuning affect successful isolation and the count returned; the caller consumes exactly that returned count. [Turing bound and zero-count API](https://github.com/flintlib/flint/blob/8d5454b96761fafe4d5a9da76a369a602f500f49/doc/source/acb_dirichlet.rst#L666) · [Native anchor and separation loop](https://github.com/flintlib/flint/blob/8d5454b96761fafe4d5a9da76a369a602f500f49/src/acb_dirichlet/platt_local_hardy_z_zeros.c#L1002) · [Index assignment and returned signs](https://github.com/flintlib/flint/blob/8d5454b96761fafe4d5a9da76a369a602f500f49/src/acb_dirichlet/platt_local_hardy_z_zeros.c#L690)

The [producer](isolate.py) calls the unrefined native interval API. It checks that each bracket is strictly ordered and positive and that consecutive open intervals have disjoint interiors. Each native call repeats the preceding final index and intersects both enclosures. Independently produced archive blocks also share a full index; the checker requires an open intersection at each join. A block has 10,001 brackets and adds exactly 10,000 new indices. A completed block is written atomically before its JSON manifest; incomplete trailing output is excluded. The initial index is already covered by the imported theorem.

The last archived root is used as an upper guard. Its exact lower bracket endpoint gives a height with total count equal to its index minus one. Rounding that endpoint down gives the reported verified integer height. With the count option the checker independently invokes FLINT's ordinary Riemann–Siegel/Turing count, distinct from its Platt grid path, at the historical endpoint, the exact dyadic guard and the integer height. It requires exact single integers and validates the integer count against the archived brackets. This second route shares FLINT's ball-arithmetic and Turing inputs.

## Data and replay

Each XZ archive contains the entire indexed interval stream for one block in increasing order. One ASCII line has the lower mantissa, lower exponent, a tab, upper mantissa and upper exponent. Each signed integer is lower-case hexadecimal. An endpoint $(m,e)$ has exact value $m2^e$. Each JSON manifest records the first and last indices, actual native return counts, working precisions, per-call SHA-256 digests and full compressed and plain-stream digests. The checkpoint root digest hashes the ordered block index and uncompressed stream digest pairs. The zero locations are encoded directly, including coincident outer endpoints of neighboring open brackets.

Use a Linux LP64 environment with Python, python-flint 0.9.0 and its FLINT 3.6.0 wheel library. The native release checkout is 8d5454b96761fafe4d5a9da76a369a602f500f49. SHA-256 hashes of the shared library used here and its release implementation of the local Platt isolator are respectively 871a4132fd1e9f3638391b2208e07088f8e3e72a10e41d45f58b150a60c2a1a9 and b1c18e82e913f381b6e44aeab48fbb1c00b0625b6606844f4ddf1e2a10485c5e. The LP64 binding follows the release's public [arf and interval layouts](https://github.com/flintlib/flint/blob/8d5454b96761fafe4d5a9da76a369a602f500f49/src/arf_types.h) and [isolation signature](https://github.com/flintlib/flint/blob/8d5454b96761fafe4d5a9da76a369a602f500f49/src/acb_dirichlet.h#L303).

To check hashes, coverage, overlapping indices and the independent total counts for checkpoint 3, run from this directory

```sh
python check_frontier.py --max-blocks 3 --count
```

To regenerate a specific block's native arithmetic, compare the raw sign-interval digests, and reconstruct and verify its merged stream, add the zero-based block number

```sh
python check_frontier.py --max-blocks 3 --replay-block 0 --count
```

To recreate three archive blocks into a fresh destination

```sh
python isolate.py --first-block 0 --stop-block 3 --output replay-blocks
python check_frontier.py --blocks replay-blocks --max-blocks 3 --count
```

The uncompressed-stream hash and arithmetic isolation provide independent levels of checking. Replaying only the artifact checker authenticates storage and indexing. Replaying the native call also reruns the underlying arithmetic. Different valid native implementations can produce different endpoints, so equality of stream hashes is specific to the stated implementation. The published earlier census is imported and was not rerun. No claim about zeros beyond the largest checked guard follows.
