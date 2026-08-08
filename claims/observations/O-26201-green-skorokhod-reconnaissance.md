# O-26201 — Green–Skorokhod carry reconnaissance through `X=20000`

Observation ID: `O-26201`  
Title: The canonical parabolic Green equality has a thin shrinking negative boundary layer, while the clipped and contact lower certificates beat the seed throughout the retained scan  
Status: **FLOAT64 RECONNAISSANCE — NOT A CERTIFICATE**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #260  
Dependencies: `L-24502`, `L-24509`, `L-26202`, `L-26203`  
Scope: discovery only

## 1. Producer

`experiments/X-26201-green-dipole-skorokhod/recon.py` constructs, in ordinary
NumPy binary64 arithmetic:

1. every prime power through `X`;
2. the exact-formula parabolic seed evaluated in binary64;
3. the endpoint-projected divisor profiles and dense Green Gram;
4. the midpoint solve
   \[
   G_XT_X=v(b_X^{(0)})-w_X;
   \]
5. the equality vector `b_X^star`;
6. the clipped Green–dipole lower/upper ledgers;
7. the prefix Skorokhod contact debt.

No directed interval, condition-number enclosure, independent solver, or
asymptotic theorem is supplied.

## 2. Retained table

| `X` | Green rank | negative coordinates | first negative | minimum `b*` | clipped total gap | clipped lower minus seed | prefix contact debt |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 50 | 23 | 11 | 40 | `-2.0067e-1` | `1.1352` | `+1.5846` | `4.2481e-1` |
| 100 | 35 | 15 | 86 | `-1.2664e-1` | `1.6486` | `+1.7873` | `4.2943e-1` |
| 200 | 60 | 22 | 178 | `-8.6583e-2` | `1.3687` | `+2.3859` | `3.4022e-1` |
| 500 | 114 | 30 | 470 | `-5.2239e-2` | `1.3557` | `+2.9169` | `3.1678e-1` |
| 1,000 | 193 | 40 | 960 | `-3.3349e-2` | `1.1014` | `+3.3782` | `2.0361e-1` |
| 2,000 | 333 | 51 | 1,946 | `-1.7150e-2` | `9.2552e-1` | `+3.8004` | `1.1579e-1` |
| 5,000 | 711 | 72 | 4,926 | `-9.8197e-3` | `6.9804e-1` | `+4.2998` | `7.8893e-2` |
| 10,000 | 1,280 | 95 | 9,898 | `-5.6041e-3` | `6.7026e-1` | `+4.5843` | `4.8692e-2` |
| 20,000 | 2,328 | 117 | 19,869 | `-2.8755e-3` | `5.0205e-1` | `+4.9225` | `2.6225e-2` |

At every retained level:

\[
\boxed{
\mathcal L_X^{\rm GS}>J_X(b_X^{(0)}).
}
\]

The same strict inequality held in a separate scan at every integer
`2<=X<=500`.

This is the strongest empirical signal in the pass. It suggests the
pointwise finite theorem

\[
\mathcal L_X^{\rm GS}\ge J_X(b_X^{(0)})
\]

rather than merely a subpower deficit.

## 3. Boundary-layer pattern

The negative Green coordinates are confined to the terminal part of the
physical interval. Their count grows slowly relative to `X`, while their depth
decreases.

For example:

```text
X=1000:   negative support 960..1000,  depth 3.33e-2
X=5000:   negative support 4926..5000, depth 9.82e-3
X=20000:  negative support 19869..20000, depth 2.88e-3
```

The data are consistent with a boundary layer of width near a square-root scale
and depth near an inverse square-root scale, but no fit or asymptotic is
claimed.

## 4. Signed dipole balance

For the clipped state, the weighted positive and negative residual masses are
close:

```text
X=2000:   D_plus 0.462889, D_minus 0.462628
X=10000:  D_plus 0.335141, D_minus 0.335115
X=20000:  D_plus 0.251027, D_minus 0.251018
```

This is exactly the cancellation that would be lost by bounding the two ledgers
before signed endpoint recombination.

The prefix contact debt is smaller still and decreases to about `0.0262` at
`X=20000`.

## 5. Numerical limitations

The Green Gram is dense. Its solve was performed with ordinary
`numpy.linalg.solve`; the maximum equality replay discrepancy reaches roughly
`1.8e-10` at `X=20000`.

The table does not certify:

- positive definiteness at a production precision;
- any exact sign;
- the source normalization;
- the cofinal boundary-layer law;
- `GDS`;
- the prime-ramp estimate;
- RH.

## 6. Production recommendation

The first proof-grade ladder should use exact rational profiles and a directed
linear solve at

```text
X=50, 100, 200, 500,
```

then reproduce:

1. every equality row;
2. the clipped layer cake;
3. `D_plus`, `D_minus`;
4. the exact lower certificate;
5. the seed comparison;
6. the prefix contact formula.

Only after those finite rows are independently reproduced should the symbolic
contact-cell descent be audited.
