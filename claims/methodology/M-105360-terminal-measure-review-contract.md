# M-105360 — Hostile review contract for the terminal Stieltjes-measure reduction

Claim ID: `M-105360`  
Status: **REVIEW PROTOCOL**  
Created: 2026-08-23  
RH status: **unproved**

This packet sharpens the boundary side of PR #729. Reviewers should treat it as
an exact transport and quantifier-reduction theorem, not as a proof of either
source-specific sign gate.

## Required review order

1. Verify the orientation of `L-105217` and the sign in

   \[
   H_1-H_2
   =\sum_c {\rho_c\over z-c}.
   \]

2. Pair `+-c` using definite parity and check

   \[
   \rho_c\left({1\over z-c}+{1\over z+c}\right)
   =z{-2\rho_c/c^2\over1-z^2/c^2}.
   \]

3. Check that `rho_c<=0` gives the positive atom

   \[
   {-2\rho_c\over c^2}\delta_{1/c^2}.
   \]

4. Verify the moment update

   \[
   \beta_n(\Omega_1)-\beta_n(\Omega_2)
   =\sum_c(-2\rho_c/c^2)c^{-2n}.
   \]

5. In `T-105360`, verify that local uniform convergence `H_N -> az` on one
   fixed disk gives convergence of every origin coefficient by Cauchy's
   formula.

6. Check summability of the infinite atomic measure from the `beta_0` identity,
   not from an unproved absolute estimate on individual residues.

7. Check that the support of the inner measure is compact: exterior points
   satisfy `|c|>=c_m>0`, so `1/c^2` is bounded and accumulates only at zero.

8. Replay the exact rational fixtures and the terminal-slope separator.

## Load-bearing firewalls

```text
definite parity                               REQUIRED for paired atoms;
real simple noncommon crossed critical points REQUIRED in the stated theorem;
positive residue                              creates a negative atom;
nonreal critical pair                         not one Stieltjes atom;
common or multiple critical point             requires a confluent jet ledger;
positive terminal slope only                  INSUFFICIENT;
local uniform affine terminal germ            SUFFICIENT terminal form;
CRVH105330                                     OPEN for low-order Xi;
TAIR105360                                     OPEN for low-order Xi;
RH                                             UNPROVEN.
```

## Terminal limit discipline

A valid proof of `TAIR105360` must retain:

- the exact boundary Cauchy function `H_(F,Omega)`, not the raw quotient `F/F'`;
- the interior critical-pole subtraction;
- one common regular symmetric exhaustion;
- a fixed complex disk on which local uniform convergence holds;
- all higher origin moments, not merely `H_N'(0)`.

The abstract separator `H(z)=z-z^3` has `H'(0)=1` but a negative second
confluent direction. It is the binding reason that terminal slope alone cannot
replace the affine-germ theorem.

## Replay contract

```bash
python -B experiments/X-105360-terminal-stieltjes-transport/verify.py \
  --output experiments/X-105360-terminal-stieltjes-transport/results/verification.json
```

Expected verdict:

```text
PASS_X_105360_TERMINAL_STIELTJES_TRANSPORT
```

The replay authenticates finite rational atomic transport and the abstract
firewall. It does not evaluate Xi, prove `CRVH105330`, prove `TAIR105360`,
validate the moving saddle, or establish RH.
