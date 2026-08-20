# T100700 implication matrix — combinations rather than isolated gates

Frozen producer base: PR #691 at `c85123d6c25b5b2ade89ab30a736f9b18844a489`.

Scientific status: all decomposition and gluing arrows below marked **P** are proved.  The two regional estimates marked **O** remain open.  RH is unproved.

## Semantic nodes

| ID | Role | Statement | Status |
|---|---|---|---|
| `P_DO` | producer | exact coefficient double-owner partition `L-100605` | **P** |
| `P_HDO` | producer/transport | two-sided convex Hilbert double-owner partition `L-100700` | **P** |
| `E_EP` | local energy | endpoint Cauchy phase budget `L-100701` | **P** |
| `N_LONG` | long normal form | interior squaring + positive divisor renewal `L-100702` | **P** |
| `N_SHORT` | short normal form | centered root-free moment double-owner form `L-100703` | **P** |
| `E_SH` | signed/energy estimate | `SCME100704` on diagonal and `p_j/p_i<=8` | **O** |
| `E_LO` | signed estimate | `LRNM100704` on `p_j/p_i>8` | **O** |
| `D_MW` | detector | subpower negative mass of the minimal wavelet implies RH | **P**, inherited |
| `C_GLUE` | composition | `E_SH + E_LO -> D_MW` | **P**, `L-100704` |

## Exact matrix

```text
native Euler source
       |
       | P_DO + P_HDO
       v
least/greatest-owner blocks (i,j), used once
       |
       +------------------------------+
       |                              |
       | i=j or p_j/p_i <= 8          | p_j/p_i > 8
       v                              v
N_SHORT                          N_LONG
centered finite moments          interior Euler squaring
root term removed                endpoint owners untouched
cross-block terms removed        divisor signs exposed
factorial tail subpower          later dilation renewal positive
       |                              |
       | E_SH                         | E_LO
       +---------------+--------------+
                       |
                       | C_GLUE
                       v
subpower logarithmic negative mass of G_mu
                       |
                       | D_MW
                       v
                      RH
```

The source partition is exact; the short and long regions are disjoint and exhaustive.  No Hall reserve, root square, completion inverse, owner packet, or endpoint collar is spent in both columns.

## Proven combination rules

1. **Complementary norms.**  The short region is consumed through an `L^2(dX/X)` estimate, whereas the long region is consumed only through a one-sided `L^1(dX/X)` estimate.  Cauchy--Schwarz converts the former to the negative-mass norm required by the detector.

2. **Stronger substitutes.**  Any theorem implying `SCME100704` may replace the short hypothesis; any theorem implying `LRNM100704` may replace the long hypothesis.  In particular:

   ```text
   pointwise G_lo >= 0  -> LRNM100704;
   blockwise DOMC energy on the short region -> SCME100704;
   blockwise DORN one-sided control on the long region -> LRNM100704.
   ```

3. **Two-ended localization is required.**  First-owner estimates alone leave an arbitrary future profile; largest-owner estimates alone leave an arbitrary past/cofactor profile.  They may be combined only after the common double-owner refinement.  `R-100700` is binding.

4. **RH-equivalent nodes remain useful.**  `E_SH`, `E_LO`, or their conjunction may be RH-bearing.  Their value is that each has strictly less source geometry than the global detector: bounded endpoint ratio and centered moments in one column; a finite interior interval with positive post-divisor transport in the other.

## Why no single existing estimate closes both columns

- centered phase/moment methods preserve cancellation but do not orient long interior Euler intervals after completion;
- deterministic squaring/renewal methods orient long intervals but do not control the dense short near-collision Gram;
- a root-containing Hardy/GCD square is RH-equivalent and cannot substitute for either regional statement;
- source-blind physical collapse loses a power and cannot be inserted between `P_DO` and the regional normal forms.

## Exact first open arrows

```text
N_SHORT -> E_SH   (short/diagonal centered near-collision energy)
N_LONG  -> E_LO   (long-interval explicit-divisor one-sided renewal)
```

The conclusion theorem itself has no further hidden interface:

```text
SCME100704 + LRNM100704 -> RH.
```
