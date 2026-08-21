# PR #455 direct-row factor-67 claim status

Frozen proposal head: `9dba11b2f1130c0aa8dba5846ec3c2e658326474`  
Review cutoff: `2026-08-14T09:03:00Z`  
Review classification: **UNPROVEN / EXACT COUNTEREXAMPLE IN ROOT ENTRY**

| Object | Review verdict | Reason |
|---|---|---|
| `L-91666` | **verified** | fixed-67 finite corridor and analytic tail are valid |
| `L-91663` native response | **verified** | Möbius convolution gives `Gamma(c_X)=w_X`, `Xi(c_X)=Omega_X` |
| least-prime source ownership | **verified** | unique factorization and stopping rule are disjoint |
| `L-91556/L-91560` one-prime cocycle | **verified on frozen inputs** | survival/hazard row coefficients sum to one |
| same-index child replacement | **verified conditional** | exact once parent and child packets are correctly typed |
| coefficient-one loss algebra | **verified conditional** | formal identity is correct for one typed ledger |
| `L-91668.10--11` | **false** | cited channel realization gives `3 mu(n)n^-1/2 Q_(X/n)`, not one copy |
| `c_X>=0` from root Hallization | **not established** | depends on false `L-91668` row identity |
| continuum equality score to finite `c_X` | **gap** | same-packet normalization bridge is asserted, not proved |
| `L-91669` | **unproved** | one-row rule does not supply the missing realization and depends on `L-91668` |
| `T-91655` | **rejected as proof** | conclusion chain breaks at root entry |
| dependency manifest | **stale** | current `L-91669/T-91655` blobs differ; `R-91658` omitted |
| hardening replay | **out of scope for failure** | does not check `L-91668.10` or outer normalization bridge |
| endpoint dual | **verified** | feasible score is at most complete prime-power ramp |
| endpoint-to-RH imports | **not reached / separate audit** | root estimate not established |
| Riemann Hypothesis | **unproved** | no valid subquadratic native loss theorem |

## Exact root counterexample

With `Y=X/n`, `L-91330` gives

\[
w_a(X,n)\frac{Q_Y(j)}{a\sqrt Y-1}
=\frac1{\sqrt n}Q_Y(j).
\]

The two coefficients in `L-91668.5` sum to

\[
(1+\kappa_*)+(2-\kappa_*)=3.
\]

Therefore their signed row observation is

\[
3\frac{\mu(n)}{\sqrt n}Q_{X/n}(j),
\]

contradicting `L-91668.10` whenever the component row is nonzero.

## Provenance mismatches at the frozen head

```text
manifest L91669: 2563665b26e63df8bb21c1fdb74769a34aeed4f4
current  L91669: ed35b6487733a04097bb9d16ef8c04b34fd41597

manifest T91655: 393df457e9036c34b7ab562e48d755bc395690c5
current  T91655: 7c282e7d5214f2ac6a43200d810b2531274da397
```

`R-91658` is normative in the current theorem but absent from the manifest.

```text
full proposal: UNPROVEN / GAP
RH:            UNPROVEN
```
