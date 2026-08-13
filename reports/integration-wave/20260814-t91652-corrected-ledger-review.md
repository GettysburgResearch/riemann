# Review of the corrected provenance-causal ledger

Review cutoff: `2026-08-14T15:45:05Z`  
Main at start: `c1a16aabc6d8e05e167893e8c8c35b20543f36ad`  
Reviewed PR #439 head: `706445c01d4a5c9f852a4faf1329bd9858dc727a`  
Normative mathematical source: `7df7775f19bd7a0dae04887ff200f114a4b54df8`  
Lock-creation commit: `affca32327a6764b1e7ac9956bdbb80c5ef93725`  
Lock blob: `0e540aa962e07c6c9b8cfb56b0798c7d1e2439fb`  
Predecessor review: PR #443 at `1659819dad021e4a048b911b62c0f266d0d62327`

## Executive verdict

The corrected ledger repairs all five defects identified in the preceding review at the local theorem level:

1. `L-91657` bounds the correct sign of the compact causal debt.
2. `L-91658` states the child-placement normalization and deficit covariance.
3. `L-91659` names a native/current/recursive root ledger.
4. `L-91660` proves the finite endpoint dual inequality directly.
5. The new lock and validator are real, fail-closed repository artifacts.

The central realized identity and recursive coefficient contraction remain valid:

```text
P_X = s_k P_X
    + sum_i lambda_i (P_X-r_i U_{p_i}P_{X/p_i})
    + sum_i alpha_i U_{p_i}P_{X/p_i},

sum_i alpha_i < 1/8.
```

Nevertheless the complete RH composition is **UNPROVEN / GAP**. The decisive unresolved theorem is `L-91659`: it defines the current datum as a difference, but does not derive one globally typed, feasible, bounded-debt current complement from the locked finite-window producers.

A second independent issue is that `t91652-full-ledger-lock.json` freezes its listed objects but is not a transitive proof lock. Several declared dependencies of the external endpoint-to-RH consumer are omitted.

```text
corrected causal core                              VERIFIED
abstract packet-envelope contraction               VERIFIED CONDITIONAL
root native/current/recursive physical producer    UNPROVEN / GAP
endpoint finite dual inequality                    VERIFIED
external endpoint-to-RH chain                      IMPORT AUDIT INCOMPLETE
full corrected ledger                              UNPROVEN / GAP
Riemann Hypothesis                                 UNPROVEN
```

## Exact repairs

### L-91657: compact causal debt

**Verdict: VERIFIED.** Put

```text
D(u)=E(u)-(5 sqrt(u)-3),  r=p^(-1/2),  v=u/p.
```

The actual shortfall is `-D(u)+rD(v)`. If `v>=67`, monotonicity and positivity of `D` make it nonpositive. If `v<67`,

```text
[-D(u)+rD(v)]_+ <= r |D(v)|
                  <= 67^(-1/2) max_{1<=w<=67}|D(w)|.
```

This is the correct sign repair.

### L-91658: same-index placement

**Verdict: VERIFIED WITH FIXES.** The theorem correctly separates

```text
U_m P_Y                  normalized same-index embedding;
m^(-1/2) U_m P_Y         arithmetic placement of one child;
c U_m P_Y                child with actual parent coefficient c.
```

It states the needed covariance

```text
F_X(U_mP_Y)=U_m F_Y(P_Y),
Delta_X(cU_mP_Y)=c Delta_Y(P_Y).
```

The normalization agrees with resident `L-91361`. The remaining fix is to declare `U_m` on the exact global data type used by `L-91659`, not only on the local quotient packet of `L-91653`.

### L-91660: finite endpoint bridge

**Verdict: VERIFIED.** Ordinary feasibility and

```text
G_n = sum_{q<=n} Lambda(q) beta_{nq},  Lambda(q)>=0
```

give

```text
Score(d) <= sum_q Lambda(q) w_X(q) = P_Lambda(X).
```

Hence

```text
F_Lambda(X) <= J_Lambda(X)-Score(d),
F_Lambda(X) <= Delta_X(N_X).
```

The sign and normalization are correct.

### T-91650: envelope consumer

**Verdict: VERIFIED WITH FIXES.** Once a producer supplies current debt `C`, child mass `rho<1/8`, and endpoint contraction by 67,

```text
Lambda(X) <= C + rho Lambda(X/67)
```

implies `Lambda(X)<8C/7`. The file should replace its stale dependency on `L-91656` by corrected `L-91657`.

## First load-bearing gap: L-91659

`L-91659` defines

```text
N_X = (ell_X,J_Lambda(X),w_X,Omega_X,q_X,Gamma_X,Xi_X,b_X),
Zhat_X = sum_e nu_X(e) Ahat_{X,e}^{(67)},
C_X = N_X - R_X Zhat_X.
```

The equality `N_X=C_X+R_XZhat_X` is therefore definitional. It does not prove that `C_X` is the admissible current packet claimed later.

Four interfaces remain missing.

### 1. One common data type

`L-91653` uses a local packet

```text
P=(ell,J,T,S,q,Gamma,Xi,b),
```

where `T` is a scalar SHARP target and `S` a declared score, with literal score also present. `L-91659` instead inserts vector targets `w_X,Omega_X` into the tuple and omits explicit declared/literal score coordinates. No map identifies these two spaces. Thus `N_X`, `R_XZhat_X`, and `C_X` are not yet shown to live in one vector space with one feasible-set functor and one deficit.

### 2. Local factor-54 scale versus global endpoint

The imported Hall results `L-91340/L-91341` work on a bounded normalized ratio `1<=x<=c0^(-1)<55`. The outer producer has a continuum endpoint `s` and local ratio `x=X/s`. `L-91659` writes `W_S(X,e)`, uses fewer than 55 nodes, and simultaneously uses global benchmark `J_Lambda(X)`.

If `X` is global, the bounded Hall hypothesis does not follow. If it is local, the RH-facing benchmark is mistyped. The missing theorem must integrate the local Hall packets over the outer endpoint law and identify the resulting global certificate.

### 3. Undefined root-atom realization

The physical realization of `Ahat_{X,e}^{(67)}` is not specified. It could mean a packet at `X/e`, an arithmetic placement `e^(-1/2)U_eP_{X/e}`, or an integrated outer packet. These choices give different coefficient mass, score, capacities, and deficit covariance.

### 4. Feasibility and one-use accounting

The row label

```text
d_cur=d_edge+d_outer+d_port
```

and the ordered safety/collar/terminal/port instructions are not yet a source-ordered complete-data identity. The proof must show that Hall residual and outer producer are complementary, all capacities have the claimed direction, every correction is charged once, and the current packet has uniformly bounded positive deficit.

The needed theorem is

```text
N_X=C_X+R_X Zhat_X,
C_X feasible,
Delta_X(C_X)<=C_root,
mhat(Zhat_X)<=54.
```

The deposited file proves only the formal equality after defining `C_X` as the difference.

## Dependency-lock review

The lock artifact and blob are real. Its validator checks the entries it enumerates, duplicate paths/identifiers, external commit reachability, mandatory interfaces, and the restricted use of `L-91112.25--26`. No passing result was fabricated.

But it is not a transitive proof lock. For example:

- external `T-90008` declares `L-90004`, `T-90006`, and analytic contour/Landau inputs that are absent;
- external `L-90020` declares `L-90016` and a prime-number-theorem input that are absent;
- transitive dependencies of `T-90011` are not recursively enumerated.

A validator pass would prove immutability of the listed set, not mathematical completeness of the DAG. The claim “full machine-readable dependency graph” is therefore too strong. Either recursively freeze the external theorem DAG or declare the external theorems atomic imports outside this review.

## Reviewed proof DAG

```text
local base packet
 -> same-index child placement                 VERIFIED WITH FIXES
 -> realized causal identity                   VERIFIED
 -> recursive coefficient mass <1/8           VERIFIED
 -> causal row/capacity positivity             VERIFIED
 -> compact causal debt                        VERIFIED
 -> abstract envelope contraction              VERIFIED CONDITIONAL

local Hall and outer producers
 -/> global typed root certificate             UNPROVEN / GAP
 -/> feasible bounded-debt current complement  UNPROVEN / GAP
 -/> one-use root inequality                    UNPROVEN / GAP

root deficit
 -> finite F_Lambda inequality                 VERIFIED
 -> o(log^2 X)                                 CONDITIONAL ON ROOT
 -> RH                                          IMPORT DAG INCOMPLETE
```

The first open arrow is

```text
bounded local Hall packets indexed by x=X/s
  -/-> one globally typed Zhat_X and feasible C_X.
```

## Integration recommendation

Retain the corrected causal debt, child normalization, free-certificate framework, causal positivity, `<1/8` contraction, direct finite dual inequality, and provenance validator as route infrastructure.

Do not promote `L-91659` or the corrected full ledger to proved status. Require one frozen theorem that defines a common global data space, realizes every root atom from local coordinates, constructs the current feasible row, proves one-use correction accounting, and establishes the uniform `C_root` bound.

No heavy scan was rerun. The decisive remaining objections are type, scale, and dependency-DAG issues.

```text
T-91652 corrected ledger  UNPROVEN / GAP
RH                         UNPROVEN
```
