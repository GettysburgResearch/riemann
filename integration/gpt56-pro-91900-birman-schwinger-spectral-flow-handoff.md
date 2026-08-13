# Integration handoff — Birman–Schwinger spectral flow and infinitesimal safe Pick hierarchy

Date: 2026-08-13  
Branch: `research/gpt56-pro/91900-birman-schwinger-spectral-flow`  
Parent PR: `#430`  
Parent frozen head: `cedf2f5b43c99d6e6f9a760236432b123dd91770`  
Review head before this handoff: `3fdfa3b10f56dbd8d9718865512e93d2d37e263a`  
RH status: **unproved**

## Purpose

Correct the overstrong interpretation of the radial spectral-type route, then
replace it by a feedback/small-gain programme with a linear infinitesimal
shadow.

## Main correction

A diffuse radial source does not by itself exclude pure-point output.  The
rank-one Friedrichs control of `R-91900` creates a bound state from a purely
absolutely continuous medium through nonlocal feedback.  The conditional RLSL
theorem of the parent remains valid only if interval-module locality is proved
explicitly.

## Exact advances

```text
Birman--Schwinger eigenvalue/gain correspondence        EXACT
negative index = number of gains above one              EXACT
safe Xi Pick matrices as finite return operators        EXACT
feedback determinant and entropy                        EXACT
moving Cauchy-metric bounded-real identity               EXACT
all compatible connections as a skew-gauge LMI          EXACT
rational canonical-connection counterexample            EXACT
infinitesimal safe Caratheodory criterion                 PROPOSED COMPLETE
one/two-node actual-Xi infinitesimal positivity          PROPOSED COMPLETE
three-node high-off-line sharpness control               EXACT
```

## Exact finite return operator

For positive rational `u` and a finite positive rational packet `q`,

\[
 C_{ij}=\frac1{1+u+q_i+q_j},
 \qquad
 D_{ii}=\frac{\xi(1+q_i)}{\xi(1+u+q_i)},
\]

and

\[
 K=C^{-1/2}DCDC^{-1/2}.
\]

Then

\[
 C-DCD\succeq0
 \quad\Longleftrightarrow\quad
 K\preceq I.
\]

False RH would give a finite rational packet with one return eigenvalue above
one, subject to the continuation interface already declared in `T-91006`.

## Linear infinitesimal criterion

At `u=0`, the first Pick derivative is

\[
 \mathcal H_{ij}
 =\frac{\xi'/\xi(1+q_i)+\xi'/\xi(1+q_j)}
        {1+q_i+q_j}.
\]

`L-91904` proposes

\[
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal H[\mathbf q]\succeq0
\]

for every finite positive rational tuple.  This is the smallest surviving
safe-real criterion in the branch.

## New finite-order theorem

`L-91905` groups the centered Hadamard product by critical-line and off-line
zero orbits.  Using only `|Im rho|>1`, it proposes that

```text
F(x)/x decreases;
xF(x) increases;
```

for `F=Xi'/Xi` and `x>1/2`.  These two inequalities imply positivity of every
one- and two-node infinitesimal Pick matrix.

`R-91902` proves sharpness on a symmetric high-off-line control: at the safe
nodes

```text
3/5, 8, 36
```

the exact three-node determinant is

\[
-\frac{201516024836691562500}
       {1055839030806150723363641645963}<0.
\]

Thus order three is the first possible obstruction.

## Constructive connection route

Every metric-compatible connection has the form

\[
 \Gamma=\frac12C^{-1}C'+C^{-1}J,
 \qquad J^*=-J.
\]

The covariant dissipation is affine in `J`.  For one packet the completed
connection problem is a finite semidefinite feasibility problem with finite
primal and dual certificates.  A valid universal construction must derive
`J` from the completed arithmetic Julia ports, not from target positivity.

## Verification

```bash
cd experiments/X-91900-birman-schwinger-spectral-flow
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_BIRMAN_SCHWINGER_SPECTRAL_FLOW
```

Selected controls:

```text
Friedrichs threshold                       1.4426950408889634
bound-state kappa at coupling 2            0.5414940825367983
safe Xi Pick minimum eigenvalue            2.0765892e-10
safe Xi maximum return singular value       0.9999999239
canonical Xi sample remainder minimum      -5.4506935e-7
rational strict-Pick determinant            0.0788980...
rational canonical remainder determinant  -1.8485673e-9
planted-orbit three-node determinant       -1.9085866e-10
```

The Xi values are finite diagnostics.  The exact rational controls are
algebraic checks.  The replay does not prove a universal small-gain theorem or
RH.

## Review order

1. `R-91900`
2. `L-91900`
3. `L-91901`
4. `L-91902`
5. `R-91901`
6. `L-91903`
7. `T-91900`
8. `L-91904`
9. `L-91905`
10. `R-91902`
11. external source lock
12. experiment and report
13. parent `T-91800/R-91800`

## Highest-priority hostile joints

1. Centered Hadamard grouping and differentiated normal convergence in
   `L-91905`.
2. Caratheodory interpolation/identity-theorem converse in `L-91904`.
3. Exact bounded-type interface inherited from `T-91006`.
4. Whether a source-ordered skew gauge can be made packet-natural.

## Exact frontier

```text
radial diffuse-only conclusion                      REFUTED
a genuine interval-module RLSL                       STILL SUFFICIENT / OPEN
finite safe-real small gain                          OPEN / RH-EQUIVALENT
infinitesimal all-packet positivity                  OPEN / RH-EQUIVALENT
actual-Xi orders one and two                         PROPOSED UNCONDITIONAL
actual-Xi order three                                FIRST OPEN LEVEL
source-ordered skew connection                       OPEN
Riemann Hypothesis                                   UNPROVED
```
