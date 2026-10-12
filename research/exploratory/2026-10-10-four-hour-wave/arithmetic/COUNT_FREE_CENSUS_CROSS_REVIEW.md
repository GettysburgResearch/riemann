# Independent count-free census guard review

Status: **ACCEPT for CF1--CF9 and the exact finite guard binding below.**
Reviewer: delegated arithmetic agent, independent of the outer-ray producer.
Review date: 2026-10-10 UTC. RH remains open.

I read COUNT_FREE_CENSUS_RECOVERY.md and its checker in full, and checked
the displayed positive theta and paired-product inputs in THEOREM.md. The
column consequence CF10 imports the separately reviewed column theorem;
this note does not independently reconstruct that theorem.

| Source | SHA-256 |
|---|---|
| `COUNT_FREE_CENSUS_RECOVERY.md` | `8b05e1b47a7cc423083fed2817813a5f20586cafc9015626815adc095498b9ce` |
| `check_count_free_census.py` | `d559d6554b91307ef169e5cb1f501ae12791ea636c0e9fa32f89203622d3cf3e` |
| `count_free_census.json` | `ce21c175914c1e1d3ad049a8b67e6528ae2f72baed309b4719c1ca8de48a7832` |
| `THEOREM.md` | `2b35a58b119a6f924658a702769c401126e708e592738551e992403004cdfe6d` |
| `CENSUS_FULL_COLUMN_SECTOR.md` | `db662f2f7c57a61413ecf16d3f4760fd1d5d315f8328bed70984340083960c43` |
| `native_candidates.json` | `bbb7fe9adce4fa9581cbb23fb558c62abafec4e568cb69c4d9f0324443ad8c20` |
| `native_slab_certificate.json` | `43d7e2748c674d658398da5f50efd6728b115dfb798d023ae364fa4d35cf1490` |
| `refined_prefix_candidates.json` | `cd8a4c8baa5a235823ebc546a7b92ab63b92113b6f1af7550a13e67b99c376b1` |
| `refined_prefix_moments.json` | `95204a030b6b86df781908aa7f472cf63edde02b226558b0713a1442177e08ba` |

The optimized independent command from `/workspace/riemann` was:

```bash
nice -n 19 /workspace/.riemann-tools/python/bin/python3 -B -O \
  research/exploratory/2026-10-10-four-hour-wave/xi/outer-ray/check_count_free_census.py \
  --output /tmp/count-free-census-independent-arithmetic.json
```

Exit zero; status `PASS_DIRECTED_COUNT_FREE_CENSUS_GUARDS`. The temporary output is
byte-identical to the official receipt, SHA-256 `ce21c175914c1e1d3ad049a8b67e6528ae2f72baed309b4719c1ca8de48a7832`.

The replay independently rebuilds the actual degree-six Gamma/zeta jet,
all8049 selected interval inverse-sixth terms, the native Xi seed greater
than99/200, and the exact rational whole-source exclusion guards at2048
and2240. The recovered positive simple-census counts are1561 and1739.
No complete-count routine is called. Old8049 and refined222 strict sign
facts are explicitly imported; historical Gram/Rosser and initial
uniqueness/count claims are unused by this proof.

The analytic proof handles selection correctly: only one occurrence is
removed from each disjoint sign interval; extra roots or multiplicities
remain in the complete sum. The positive theta disk with xi6=2pi^3/63
and the exact seed excludes every root in the radius11/2 disk. With the
complete half-width1/2 strip, every residual root lies in the acute
inverse-sixth sector. Thus each remaining occurrence contributes a positive
quantity, and a single residual root with real part at mostH violates the
strict upper-moment guard. This proves completeness and simplicity in the
stated smaller closed heights without a historical zero-count contract.

The analytic complete theta/product/strip identities remain imported
source inputs, and the native sign facts remain separately authenticated
finite inputs. This replay does not authenticate an infinite product from
finite JSON, reproduce every endpoint sign, or certify RH. The all-order
finite-column conclusion uses its named reviewed theorem and keeps its
finite height/order/horizontal domain.
