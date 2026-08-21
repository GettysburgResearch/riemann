# PR #455 single-SHARP final proposal — frozen claim-status audit

Frozen proposal head: `1b502acbe511776178da3dc916e3cd3464cd5e77`  
Normative content: `c696d2a356eeacb3097d4ea6cc727b84548d7a03`  
Review cutoff: `2026-08-14T12:39:10Z`

| Object or implication | Review status | Reason |
|---|---|---|
| `R-91659` historical factor-three diagnosis | **verified** | Old channel coefficients sum to three. |
| `w_Psi=3w_(4/3)` | **verified exact** | Direct atom algebra. |
| one-copy row observation | **verified exact** | Produces `n^-1/2 Q_(X/n)`. |
| finite Fubini for `b_X^star` | **verified exact** | Same finite labelled pairs. |
| `R[b_X^star]=c_X` | **verified exact** | Linear row operator. |
| `b_X^star=bar b_X^star+E_X` | **verified typing** | Respects `R-91102`. |
| `Score(c_X)=P_Lambda(X)` | **verified algebraic identity** | Prime-log convolution. |
| `J_X^eq=4sqrt(X)` distinct from `P_Lambda(X)` | **verified correction** | No equality is used. |
| same-index child replacement | **verified conditional exact** | Once positive parent/child rows exist. |
| fixed-67 entropy difference | **no new objection** | Blocked upstream in final use. |
| `L-91550` Hall corridors | **finite-window only** | Certified for `1<=x<55`. |
| stopped-parent survival Hall at `y=13` | **false for every prime `p>=67`** | Necessary prefix at `t=13` is negative. |
| `L-91670` global `M_1>1/20` | **false** | `N=71,j=70,Y=72` gives `0<M_1<1/20`. |
| global normalized-row monotonicity | **not decided** | Probe remains positive; written proof is out of scope. |
| `L-91621` positive stopped-leaf Hall output | **refuted as stated** | Hall hypothesis fails. |
| `L-91663` positive complete parent row | **blocked** | Depends on failed producer. |
| `L-91671` equality-deficit recurrence | **blocked** | Positive parent ledger is absent. |
| `T-91656` | **rejected as proof** | Load-bearing implication is false. |
| Riemann Hypothesis | **unproved** | Final chain does not reconstruct. |

## Exact replay

```bash
python3 experiments/X-91672-stopped-leaf-hall-prefix-counterexample/verify.py \
  --json experiments/X-91672-stopped-leaf-hall-prefix-counterexample/results/verification.json
```

```text
PASS_PR455_STOPPED_LEAF_HALL_PREFIX_COUNTEREXAMPLE
d010a2ec2e1efa95efa98c237958a25166ae486381c6ace5d633d5f2016bace1
```
