# PR #476 — first broken arrows

Frozen head: `9f16ce483954d4233b68ee09cb6bec47400aa3cc`

## 1. Fatal normalization break

```text
T-91662 statement A
 -> T-91312 bounded equality-deficit envelope
 -> frozen T-91660.8: 4 sqrt(X)-H(d_X)=O(1)
 -> claimed native slack <=4 log X+C
```

Native feasibility gives `H(d_X)<=J_Lambda(X)`. Under the proposal's claimed RH conclusion,

```text
J_Lambda(X)=4 sqrt(X)-kappa_0 log(X)+O(1),
kappa_0=zeta'/zeta(1/2)>0.
```

Hence

```text
4 sqrt(X)-H(d_X)>=kappa_0 log(X)+O(1),
```

contradicting the frozen `O(1)` line. The correct recursive object is `J_Lambda-H`, obtained from an exact native slack-vector cocycle.

## 2. Fatal all-column coverage break

```text
L-91691.7--.10: mismatch/collar bound for q>=K
terminal omission: upper annulus
claim: all native columns feasible
```

Columns `2<=q<K` are not covered. An outer seed discrepancy at `n>=K` contributes to physical column `q<K` through multiples `n=jq>=K`. Exact source ownership does not make this response vanish.

Required split:

```text
jq<K       inner recursive owner
jq>=K      current outer mismatch owner
```

and a uniform comparison for every `q>=2`.

## 3. Target-mass application break

```text
L-91650: sum alpha_i<1/8
 -> L-91694.2: sum alpha_i m(A_i Q_i)<=rho m(P_s)
```

The implication needs a proved child target-mass comparison in the actual root-fiber normalization. The unweighted coefficient bound alone is insufficient.

## 4. Reserve analyticity break

```text
absolute cellwise Lipschitz coordinates
 -> uniform capacity-normalized epsilon_M->0
 -> bounded complete correction C
```

Native capacities vary and vanish at activation boundaries. The fixed normalized space, relative interpolation estimate, physical positive refinement and operator norm are asserted but not established.

## Relevant later successors

```text
PR #477  records the equality/native normalization firewall and proposes a native cocycle
PR #479  records and repairs the q<K physical-column gap
```

Neither successor is a dependency of frozen PR #476.
