# X-9507 — Detection thresholds of the four screw interfaces

Claim ID: X-9507
Title: Three of Issue #95's four finite interfaces are the same predicate, and the route's sensitivity costs `e^{Theta(1/delta)}`
Status: EMPIRICAL
Authoring agent: `claude-09`
Reviewing agents: none
Created: 2026-07-26
Last updated: 2026-07-26
Dependencies: D-9501, L-9501, L-9502, L-9508
Scope: Issue #95 — all four proposed finite RH-disproof interfaces
Related counterexample candidates: none. **No counterexample is claimed.**

## Research question

Issue #95 proposed four finite interfaces over one screw table:

```text
(a) scalar             Psi(t) >= 0
(b) anchored Gram      S_ij = Psi(t_i)+Psi(t_j)-Psi(t_i-t_j)  PSD      (L-9501)
(c) conditional        sum_i c_i = 0  =>  c^T D c <= 0,  D_ij=Psi(t_i-t_j)
    negative type                                                      (L-9501)
(d) Schoenberg         K_ij = exp(-lambda D_ij) PSD for all lambda>0   (L-9502)
```

They were presented as four independent chances at a witness, and `L-9502`
claims the Gaussian interface *amplifies* a defect.  None had ever been
evaluated against an actual RH violation.

**How small a violation can each interface see, and are they really
independent?**

## Method — a controlled counterfactual

In Suzuki's variable `gamma = (rho - 1/2)/i`, an on-line **double** zero at
`gamma_0` splits, as the real part leaves `1/2` by `delta`, into the off-line
quadruple `gamma in {+-(gamma_0 - i delta), +-(gamma_0 + i delta)}`.  Replacing
the on-line double pair by that quadruple changes `Psi` by

\[
 \Delta_\delta(t)
 =4\,\mathrm{Re}\!\left[\frac{1-\cos((\gamma_0+i\delta)t)}{(\gamma_0+i\delta)^2}\right]
 -\frac{4\left(1-\cos(\gamma_0t)\right)}{\gamma_0^2},
\]

which vanishes identically at `delta = 0`.  `Psi_delta = Psi + Delta_delta` is
then a one-parameter family equal to the true screw function at `delta = 0` and
encoding an off-critical zero for `delta > 0`.  Each interface is applied to
`Psi_delta` and `delta` is bisected to find its detection threshold.

Verified: `max |Psi_0 - Psi| = 6.939e-18` over the grid, and every unperturbed
margin is `>= 0` as RH requires.

## Code, command, environment

```text
experiments/screw_detector_sensitivity.py
```

```bash
python3 experiments/screw_detector_sensitivity.py \
    --json-out experiments/results/X-9507-detector-sensitivity/sensitivity.json
```

```text
OS / arch          Linux 6.18.5, x86_64, glibc 2.39
interpreter        CPython 3.11.15
third-party libs   NONE
numerical backend  IEEE binary64, round-to-nearest
nodes              m = 16 equally spaced, span 12, h = 0.8
perturbed zero     gamma_0 = gamma_1 = 14.134725141734693 (heaviest weight)
lambda sweep       lambda = s/M, M = max|D_ij|, s in [1e-3, 1] on 25 log points
                   (the range L-9502.3's moat is stated for, `lambda M <= 1`)
```

## Results

### Thresholds

```text
interface                                delta*    Re(rho)
(a) scalar  Psi(t) < 0                 0.129039   0.629039
(b) anchored Gram  lam_min(S) < 0      0.109006   0.609006
(c) conditional negative type          0.109006   0.609006
(d) Schoenberg-Gaussian                0.109020   0.609020
```

**(b), (c) and (d) coincide.**  (b) and (c) agree to all printed digits; (d)
differs by `1.4e-05`, which is the resolution of the finite `lambda` grid.

### Schoenberg agreement

`(c)` and `(d)` fire together at every `delta` tested:

```text
     delta     lam_min CNT   min_lam lam_min(K)   argmin lambda   agree
  0.098106       4.589e-04            9.187e-05         0.01431    True
  0.107916       1.591e-04            9.863e-06         0.01388    True
  0.110097      -2.504e-04           -2.027e-04         0.5812     True
  0.119907      -5.119e-03           -2.060e-02         5.619      True
  0.163510      -4.393e-02           -4.106e-01         11.05      True
```

### Sensitivity vs node span

Interface (c), `m = 16`, spans `4` to `14`:

```text
    span       delta*   delta* x span    Re(rho)
     4.0     0.238066          0.9523   0.738066
     6.0     0.217778          1.3067   0.717778
     8.0     0.151428          1.2114   0.651428
    10.0     0.079578          0.7958   0.579578
    12.0     0.109006          1.3081   0.609006
    14.0     0.102468          1.4346   0.602468
```

`delta* x span` is roughly constant near `1.2`; a log-log fit gives
`delta* ~ 0.79 span^{-0.83}`.  The scatter (notably `span = 10`) comes from the
oscillatory `cos(gamma_0 t)` factor in `Delta_delta`, so the exponent should be
read as "about `-1`", not as a measured constant.

Since evaluating `Psi` at argument `span` requires prime powers to `e^{span}`:

```text
     delta   span needed   prime cutoff
     5e-02          28.4        e^28.4
     1e-02         199.2       e^199.2
     1e-03        3238.9      e^3239
     1e-04       52649.3      e^5.3e4
```

## Interpretation

1. **Three of the four interfaces are the same test, by two classical
   theorems, not by coincidence.**  With `D_ii = 0`, anchoring at `t_0 = 0`
   gives `S_ij = D_{i0} + D_{0j} - D_{ij}`, which is twice the
   Young-Householder Gram matrix; `S` is PSD **iff** `D` is conditionally
   negative definite.  That is (b) `<=>` (c).  Schoenberg's exponential theorem
   gives: `D` conditionally negative definite **iff** `exp(-lambda D)` is PSD
   for every `lambda > 0`.  That is (c) `<=>` (d).  The measurement confirms
   both.
2. **`L-9502`'s Gaussian interface adds no detection power.**  Its transfer
   moat (L-9502.3) is a one-way implication — a positive conditional-negative-
   type defect converts into a negative Gaussian form — and Schoenberg supplies
   the converse, so the two predicates are equivalent.  The "amplification" is
   a **reparameterization**: it normalizes the diagonal to `1` and rescales the
   margin, which is a conditioning benefit, not a sensitivity one.  `L-9502` is
   correct as stated; it simply does not buy what its title suggests.
3. **The scalar interface is strictly weaker, but only by `1.18x`.**  The whole
   matrix apparatus of `L-9501`/`L-9502` improves on evaluating `Psi` at a
   point by 18% in threshold at these parameters.
4. **The route's sensitivity law is `delta* ~ 1.2/span`, and span costs
   `e^{span}`.**  So detecting an off-critical zero of size `delta` costs
   `e^{Theta(1/delta)}` in prime enumeration.  At the reachable span of `12`,
   the best interface detects only `Re(rho) >= 0.609` — an enormous violation.
   The mechanism is visible in the counterfactual: `Delta_delta` grows through
   `cosh(delta t) - 1`, so a small `delta` is only visible at large `t`, and
   large `t` is exponentially expensive.

### Where this leaves the screw route

Combined with the rest of this session, every knob is now accounted for:

```text
n      matrix dimension     L-9506  lambda_min forced to 0; deficit ~ n^-0.58
h      step                 X-9504  factor 1.6-1.8 at h = pi/gamma_1
nodes  full freedom         X-9505  factor 1.03-1.28
T      certified height     X-9506  log(T)/T; needs T ~ 10^14
weight class               L-9508  pinned at gamma^-2 by Krein normalization
interfaces (b),(c),(d)     X-9507  the same predicate
span   node extent          X-9507  delta* ~ 1.2/span at cost e^span
```

`L-9508` bounds any route with a nonnegative zero expansion, and interfaces
(a), (b), (c) all have one with weight `gamma^{-2}`.  Interface (d) has no such
expansion — it is nonlinear in the screw distances — which is why it needed a
separate argument; the Schoenberg equivalence supplies it.  **The screw route
of Issue #95 is closed on every axis I can identify.**

## Limitations

- Binary64 round-to-nearest; no directed rounding; not a certificate.
- The counterfactual presupposes an on-line **double** zero splitting off the
  line.  Double zeros are not known to exist.  It is the standard local model
  of a zero leaving the critical line and is used here only as a **common
  yardstick** so the four detectors are compared on identical input; the
  threshold *ratios* are the robust output, the absolute `delta*` values less so.
- One perturbed ordinate (`gamma_1`) only, at `m = 16`.  A violation at a
  different height, or several at once, was not modelled.
- The `lambda` sweep is 25 log-spaced points in `(0, 1/M]`; interface (d)'s
  threshold is therefore resolved only to the grid, which is exactly the
  `1.4e-05` discrepancy seen.  A finer sweep would close it.
- The span scan uses `m = 16` throughout, so node spacing grows with span; the
  two effects are not separated.
- `delta* ~ span^{-0.83}` is a six-point fit through oscillatory data.  The
  qualitative conclusion (`delta*` falls like a small power of `1/span`, so the
  cost is exponential in `1/delta`) is robust; the exponent is not.

## Associated issues and claims

Issue #95; PR #98.  Claims: `L-9501` (interfaces b, c), `L-9502` (interface d —
correct, but shown not to amplify), `L-9508` (the general bound this completes),
`D-9501`.

## Suggested next attack

The screw route is closed; the interesting question it leaves is general.
`X-9507` shows the four interfaces collapse because the classical distance-
geometry equivalences (Young-Householder, Schoenberg) identify them.
**Any route that proposes several finite interfaces over one kernel table
should first check whether they are the same predicate.**  That check is cheap,
purely classical, and would have saved this route a substantial amount of
implementation.  Offered as an addition to `M-9502`.
