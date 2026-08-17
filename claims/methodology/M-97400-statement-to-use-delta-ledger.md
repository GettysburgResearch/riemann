# M-97400 — Statement-to-use delta ledger for PRs #565 and #566

Status: **REUSABLE ADVERSARIAL METHOD WITH TWO EXACT FAILURES**

For every interface record:

```text
producer object and quantifiers;
consumer object and quantifiers;
coordinates and parity orientation;
source measure and ownership;
exact delta;
smallest witness.
```

## PR #565

| Field | Produced by PR #556 `L-96602` | Consumed by PR #565 `L-97101` |
|---|---|---|
| Parent | canonical positive annular packet | either canonical P61 packet or full parity source |
| Child removal | same-channel `A_pP_y` | swapped `SA_pP_y` |
| Positivity reason | literal source restriction | asserted from predecessor |
| Marginal | finite P61 `F,M` only for canonical packet | finite P61 `F,M` used after swap |
| Delta | swap changes the source channel | the two object types cannot coincide |
| Witness | one even atom | `(e,0)-S(e,0)=(e,-e)` |

## PR #566

| Field | Produced by reserve injection | Consumed by M-matrix lemma |
|---|---|---|
| Controlled scalar | `scalar(R_vw)` | `g_v=scalar(H_v)` |
| Inequality | `scalar(R_vw)>=alpha scalar(G_w)` | `g_v>=sum alpha g_w` |
| Delta | reserve versus Hall complement | no comparison is proved |
| Witness | `R=1, alpha G_w=1` | `H=1/2` |

The exact tests are retained in `X-97400-source-interfaces`.
