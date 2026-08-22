# Lane 3 checkpoint 2 — edge cases and the jump law (script: edge_cases.py, run 2026-08-22)

All numbers below produced by my own from-scratch implementation (direct-sum Q,
fsum): edge_cases.py in this directory. Frozen lattice = 2^18 squarefree
divisors of P_61.

## E1. Degeneracy at the lower endpoint — THE THEOREM STATEMENT AS GIVEN IS FALSE AT x = 2

- M_2(2) = 0 EXACTLY (both Q_2(2) and Q_1(2) vanish: the only knot log(Y/m) terms are 0).
- M_3(x) = 0 IDENTICALLY on the whole interval 2 <= x <= 3 (Q_Y(3) = 0 for Y < 3,
  and Q_3(3) = 0). Verified: m3 = 0 at x = 2, 2.5, 2.9999999, 3.0 exactly;
  m3 = +1.9e-8 at x = 3.0000001 (positive immediately after).
- M_2(x) > 0 for x > 2 (0.0000000278 at x = 2.0000001; 0.148 at 2.5).
- TB(2) = +1.9497, M_sc(2) = +0.3307 — strictly positive.
=> "all four margins positive for every real x >= 2" must be weakened to
   ">= 0 for all x >= 2, with M_2 > 0 for x > 2 and M_3 > 0 for x > 3"
   (feasibility needs only >= 0, so the THEOREM survives; the SLOGAN does not).

## E2. Demands at tiny x

x in [2,3): odds {2}, evens {1} — demand exists from x = 2 (mu(2) = -1), greedy
fills on e = 1, theta(1) = T(2)/T(1) in (0,1) since TB > 0. x in [3,5): odds
{2,3}; x in [5,6): odds {2,3,5}; first even after 1 is 6. All four margins
computed and nonnegative on a 41-point-per-cell scan of [2,67):
  min TB   = 1.676601032 at x -> 33^-  (EXACTLY the L-105031(f) constant; 33 = 3*11 even)
  min m_sc = 0.273956906 at x -> 3^-
  min m2 = min m3 = 0 at the E1 degeneracies.
Integer sweep x = 2..2000 (frozen): NO negative margin anywhere; minima
  TB 1.698609923 (x=32), m_sc 0.330721814 (x=2), m2 = m3 = 0 (x=2).
Left-limits at every activation d <= 2000: min TB 1.676601033 (x->33^-),
  min m_sc 0.273956906 (x->3^-), min m2 0.294016071 (x->3^-), min m3 0 (x->3^-).
This matches and extends the deposited all-fibres verification (which was
FULL-SUPPORT, integer fibres + cut left-limits, sweep.py/scan.py; frozen = full
support only for x < 67 — no prime in (61,67), so the deposited x < 67 numbers
apply verbatim to the frozen block, incl. TB min 1.676601).

## E3. THE JUMP LAW — the orchestrator's stated direction is WRONG for rows/score

Measured at x = d(1-1e-9) vs x = d for every activation 6 <= d <= 70
(all displayed digits verified; predictions exact):

- TB jumps by mu(d)/sqrt(d): DOWN 1/sqrt(o) at odd activations, UP 1/sqrt(e)
  at even activations (measured = predicted to 6 decimals at every d).
- M_2, M_3: jump weakly UP at ODD activations (e.g. d=7: dm2=+0.157, dm3=+0.043;
  d=29: dm2=+0.005; zero when the greedy threshold even e* has x/e* < j so
  rho_j(e*) = 0, e.g. dm3 = 0 for d >= 17). CONTINUOUS at even activations
  (measured jumps 0.000000). Mechanism: the new odd's own row demand
  Q_{x/o}(j)/sqrt(o) is 0 at activation (Y = 1 < j) and grows continuously
  only from x = j*o; the demand jump 1/sqrt(o) forces extra greedy fill at the
  threshold even, adding rho_j(e*) * 1/sqrt(o) >= 0. A new even activates as the
  LARGEST even, receives theta = 0, changes nothing.
- M_sc: jumps STRICTLY UP at odd activations: jump = (1/sqrt(o))[2 - s(e*)] > 0
  since s(e*) < 2 for e* < x (measured, e.g. d=7: +0.246, d=61: +0.0553).
  Continuous at even activations.

CONSEQUENCE FOR LANE 2 (assembly instruction): the pattern "margins jump UP at
even activations, DOWN at odd activations" holds ONLY for TB. For M_2, M_3,
M_sc the activation jumps are WEAKLY UP AT ODDS and ZERO AT EVENS — activations
are never the dangerous points for rows/score. The dangerous set is:
 (a) for TB: the points x = o (odd activation, right value) and x -> e^- (left
     limits before even activations) — BOTH covered by L-105031(f)'s cell-endpoint
     enumeration (lattice.py evaluates both endpoints of every cell);
 (b) for M_2, M_3, M_sc: left-limits x -> d^- at ALL activations AND interior
     behavior BETWEEN breakpoints. The margins are continuous piecewise-smooth
     there with kinks on the finer mesh x = m*d (integer m, active d: the floor
     kinks of Q via H) and at greedy-threshold index changes; a between-breakpoints
     analysis must certify no interior dip below 0 on that finer mesh, e.g. by
     cell-wise derivative bounds or interval arithmetic. Evaluating only AT
     activation points (in either direction) is NOT sufficient for rows/score;
     evaluating only left-limits IS sufficient at activations but not between
     knots. Empirically m_sc decreases between odd activations at small x
     (0.3307 -> 0.2740 on [2,3)), so per-cell right-endpoint (left-limit) checks
     catch the cell minima seen so far; that monotonicity is NOT proved and must
     not be assumed silently.

## E4. Ties

No ties are possible in the greedy sort (divisor values distinct); rho_j ties
occur only on the rho_j = 0 tail (Y < j) where fill order doesn't affect rows,
and s strictly increasing breaks them for the score. No tie-breaking rule needs
to enter the theorem statement; record one sentence in the proof.
