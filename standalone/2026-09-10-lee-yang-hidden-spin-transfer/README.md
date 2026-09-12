# Auxiliary-spin pair synthesis: what works and what does not

Status: **PROPOSED complete component proofs; independent review required.**
The requested Lee--Yang-compatible realization of the actual theta law and RH
remain UNPROVED. This is not a full RH proposal with a routine final check.

Read [PROOF.md](PROOF.md), then [SOURCES.json](SOURCES.json) and
[VALIDATION.md](VALIDATION.md). Parent source: PR #842 at
`c79c2f6c59640e5f5ef6e22b2ff745d3a8f5a0ff`. Earlier files are unchanged.

## Positive construction

For every finite weighted hidden pair ferromagnet B, a>0 and real b, the full
law proportional to `exp(-a*x^4-b*x^2) M_B(x)` has an explicit finite PAIR-Ising
realization in the limit, with every moment and complex-compact MGF converging.
All hidden configurations, extreme visible levels and remote tails are kept.
The underlying quartic scaling is classical Griffiths--Simon, not a novelty claim.

## Actual-source boundary

Even the WEAK closure of that entire class, allowing all parameters and hidden
graphs to change, excludes the actual theta law. In the squared coordinate
`g(u)=-log rho(sqrt(u))`, every member satisfies `g''>0` and `g'''<=0`.
Tightness plus Lee--Yang fourth-moment control gives uniform moments, and
log-concave compactness passes third differences to the limit. The actual
`-log w(sqrt(u))` instead has positive third derivative eventually. This does
NOT rule out the closure of all pair-Ising magnetizations.

A separate finite theorem treats a uniform visible Curie--Weiss block attached
uniformly to an arbitrary interacting hidden graph. Its full de-binomialized
level weights satisfy `R(2s)R(0)^3<=R(s)^4`. The parent's actual entropy source
requires log-approximation error at least

```
max(0,L^(2d-3)-[P(2)-4P(1)+3P(0)])/8.
```

For the actual theta polynomial approximants j>=4 and even L, this is at least
`max(0,L-1328)/8`. Thus increasing the number or strength of uniformly attached
hidden spins cannot supply the proposed vanishing-error replacement.
For arbitrary nonuniform graphs the same lower bound applies to
`epsilon + sum of absolute coupling departures from their uniform means`.
This is a necessary architectural cost, not a bound on all possible graphs.

A fully enumerated CONNECTED four-spin pair path has contrast ratio
`87701047604/44070501627 > 1.99`, showing explicitly why that finite inequality
must not be imposed on general pair graphs. It is not a theta realization.

## Review focus

Check HS1's pair-coupling sign and whole-tail limit, HS2's weak-to-log-density
compactness step and square-coordinate Jacobian, and HS4's actual source bounds.
The possible general nonuniform realization remains OPEN. No new theta integral,
actual zeta zero, general infeasibility theorem, or all-order moment fit was run.

```
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B check.py --self-test
python -I -S -B -O check.py --self-test
```

Bounded controls do not machine-prove the infinite analytic arguments. The
publication requests review of these stated components, not acceptance of RH.
