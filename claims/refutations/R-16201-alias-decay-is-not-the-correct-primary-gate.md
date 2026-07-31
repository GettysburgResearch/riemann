# R-16201 — Alias decay is not the correct primary prolate-tail gate

Claim ID: `R-16201`  
Status: **SCOPE NARROWING; L-16207 DECOMPOSITION RETAINED**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-07-31  
Targets: the suggested fixed-mode condition `eta_n(lambda)->0` in `L-16207`

## Verdict

The exact Poisson/alias decomposition in `L-16207` remains valid. The proposed
sufficient continuation

```text
eta_n(lambda)
 =||sum_(k>=2)r_n(k .)||
  /||r_n||
 ->0                                                         (R-16201.1)
```

should not be treated as the primary theorem and is not used by the corrected
source transfer `T-16202`.

Uniform radial prolate asymptotics show that sharp time limitation creates
oscillatory algebraic exterior tails throughout `1<x<infinity`. The arithmetic
samples at `2v,3v,...` can therefore survive at normalized leading order; their
individual disappearance is not structurally forced.

## Primary asymptotic evidence

For fixed mode and large spheroidal parameter `gamma`, Dunster proves a uniform
radial representation on the complete exterior interval `1<x<infinity` in
terms of a Bessel function with explicit `O(gamma^-1)` error. The exact
far-field form is

```text
constant_n(gamma)
 sin(gamma x-pi n/2)/(gamma x)
 [1+O(1/x)].                                               (R-16201.2)
```

Thus the exterior tail is not compactly concentrated at the first sampling
cell. Different fixed modes have mode-dependent phase corrections, and the
full Poisson sum must be analyzed coherently.

Primary reference:

- T. M. Dunster, *Asymptotics of Prolate Spheroidal Wave Functions*, J. Classical
  Analysis 11 (2017), arXiv:1601.00699v3, especially equations (1.24) and
  (6.5)--(6.9).

## Correct replacement

The source route needs only the full arithmetic tail profiles to have a
uniformly bounded and nondegenerate normalized Gram. `T-16202` assumes the
exact profile representation

```text
widehat(T_(n,lambda))(s)
 =sqrt(d_n/R_lambda)e^(-isx_lambda)
  Phi_(n,lambda)(s/R_lambda),                              (R-16201.3)
```

with a uniform `C1` decay envelope and

```text
0<cI<=Gram(Phi_lambda)<=CI.                               (R-16201.4)
```

Under these weaker conditions:

1. the complete tail Gram is uniformly equivalent to `diag(d_n)`;
2. the exact-radical target and next gap retain scales `d_4,d_8`;
3. Riemann--von Mangoldt gives normalized tail-Weil scalarization
   `O(1/log R_lambda)`;
4. no individual alias has to vanish.

## Project status

```text
L-16207 exact decomposition:                 PASSED
L-16207 alias-decay condition:               SUFFICIENT BUT SUPERSEDED
T-16202 full normalized profile condition:   CURRENT SOURCE THEOREM
```

This correction does not produce an RH proof. It prevents the project from
attacking an unnecessarily strong and potentially false subgoal.
