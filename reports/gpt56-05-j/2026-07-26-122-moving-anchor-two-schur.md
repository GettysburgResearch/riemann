# Session report — moving-anchor two-Schur direct-xi certificates

Agent: `gpt56-05-j`  
Issue: #122  
Date: 2026-07-26  
Branch: `agent/gpt56-05-j/122-moving-anchor-two-schur`  
Stacked base: draft PR #117

## Repository synthesis

The session began with a pass over the newest empirical and proof-producing work.

### Carrier route

The recovered `c=10^11`, `K=1024` carrier vector has a correction-composed directed positive interval. This is a strong finite-vector exclusion, not a whole-matrix theorem. PR #89 therefore moved threshold work to endpoint Green matrices and coherent rank-two packets.

### Value-only xi'/xi route

The original proof-grade feature table has exact feasible anchors, closing its current value-only dual cone. Cross-height and higher-precision finalists have so far resolved positive or remained zero-touching. This suggests changing primitive information rather than optimizing indefinitely over the same table.

### Direct completed-xi route

PR #103 produced the tightest current proof-grade atomized direct-xi table. Its apparent negative shift at ordinary precision was refuted positive at 512 bits. PR #116 then certified the complete degree-at-most-14 half-line nonnegative response cone on that table.

PR #117 observed that adding the exact node `t=0` introduces only one new moment and reduces the entire degree-15 cone to one Schur comparison. Its ordinary prediction is positive, but the proof workflow was still pending during this session.

### Support-gap route

PR #110 derived support-aware Hausdorff inequalities. New four-slab reconnaissance shows many tempting raw negative chords, but every tested row becomes positive after the load-bearing exact count correction. Natural-scale nodes are much better conditioned than inherited microscopic grids.

## Chosen attack

The strongest reusable structural feature was PR #117's one-new-moment phenomenon. The session asked whether `t=0` was special.

It is not.

For every positive exact moving anchor `t`, shift the spectral coordinate to

```text
z=y+t.
```

Zero extension multiplies every old response by `z`. Hence all new moments except the constant response are inherited. However, unlike `t=0`, the support is now `z>=t`, and the odd-degree half-line cone produces **two** linked Schur inequalities.

## Main theorem

For old moments `a_0,...,a_(2m)`, define

```text
A_k=sum_j binom(k,j)t^(k-j)a_j.
```

The new moments satisfy

```text
c_(k+1)=A_k.
```

Only `c_0` is new. The complete degree-`2m+1` response cone is positive exactly when

```text
theta_0 <= c_0 <= U_t,
```

where the lower and upper endpoints are exact Schur complements of two inherited `m x m` blocks.

A lower failure emits the explicit response

```text
q_0(z)^2.
```

An upper failure emits

```text
(z-t)q_1(z)^2 = y q_1(y+t)^2.
```

This supplies two qualitatively different finite RH-disproof mechanisms from one new primitive.

## Width eureka

The interval width is not accidental numerical space. The polynomial

```text
P_t(z)=t q_0(z)^2+(z-t)q_1(z)^2
```

is nonnegative for `z>=t` and satisfies `P_t(0)=0`. Therefore

```text
P_t(y+t)=(y+t)R_t(y)
```

for an old degree-even polynomial `R_t>=0`. Its old response is exactly

```text
L_old(R_t)=t(U_t-theta_0).
```

Thus the already-certified old cone protects nonemptiness of every moving-anchor interval. This also explains why raw gaps can become extremely small at large anchors without constituting a candidate.

## Independent replay identity

The new scalar can be reconstructed without a second full barycentric table:

```text
c_0 = beta_t (F(t)-F(u_r)) + L_old(P_(t,r)),
beta_t=-1/D(-t).
```

This uses one new-old point difference and the old moments. It provides a different arithmetic path and an exact overlap gate against the full direct contraction.

## Exact finite controls

X-12201 uses old moments

```text
(3,7,21,73,273)
```

and `t=2`. It reconstructs

```text
theta_0 = 101/135,
U_t     = 541/720,
width   = 7/2160.
```

The exact cases include:

- interior: `c_0=3/4`;
- lower violation: `c_0=7/10`, witness value `-13/270`;
- upper violation: `c_0=4/5`, witness value `-7/72`;
- both boundary cases.

The width polynomial evaluates to `7/1080=2*width`. An independent Python/Fraction reconstruction checked every threshold, witness value, boundary, and width identity before publication.

## PR #103 reconnaissance

At the atomized-minimum shift, ordinary high-precision anchor values remained inside the admissible interval. The dimensionless positions were approximately:

```text
t=1        rho=0.2173
t=4        rho=0.3005
t=16       rho=0.3448
t=64       rho=0.4010
t=256      rho=0.5132
t=1024     rho=0.6579
t=2^16     rho=0.9348
t=2^20     rho=0.9826
```

No candidate was found. The movement toward the upper wall motivates a two-sided scan, but the inherited width simultaneously contracts.

## Candidate proposals

### Candidate family A — shift-by-anchor ladder

For every PR #103 ordinate shift, evaluate only

```text
t in {1,4,16,64,256}.
```

Rank by `min(rho,1-rho)`, not raw slack. Any directed value outside `[0,1]` gives an explicit polynomial nomination immediately.

### Candidate family B — easy-half-plane independent controls

At `t=4`, the new point has `Re(s)=5/2`. A directed Euler product can be made arithmetically independent from the old Riemann-Siegel producer. This is the preferred end-to-end control before scanning many shifts.

### Candidate family C — support-scale anchors

For a count-certified slab with support radius `A`, include anchors near

```text
t in {A/4,A,4A}.
```

This connects the moving-node cone to PR #110's intrinsic support geometry while retaining only one new primitive per anchor.

## Artifacts

- `L-12201`: arbitrary-node one-new-moment identity;
- `T-12202`: complete two-Schur interval and explicit witnesses;
- `L-12203`: interval-width/old-cone identity;
- `L-12204`: reduced one-point-difference reconstruction;
- `M-12201`: production candidate protocol;
- `O-12201`: ordinary PR #103 anchor ladder;
- `X-12201`: exact standard-library checker and synthetic controls.

## Truth status

```text
new finite algebra                 PROPOSED
exact synthetic checker controls   PASSED by independent reconstruction
PR103 anchor ladder                EMPIRICAL POSITIVE
Riemann-xi moving-anchor interval  NOT YET PRODUCED
counterexample                     NOT FOUND
Z-#### candidate                   NONE
```

## Immediate next work

1. Produce a directed `t=4` primitive and both direct/reduced `c_0` intervals.
2. Replay the exact Schur witnesses against the PR #112 moments.
3. Scan the five-anchor ladder across every PR #103 shift.
4. Move to support-scale anchors on the independently certified slabs from PR #110.
5. Allocate a candidate only after a strict fixed-polynomial negative survives independent reproduction.