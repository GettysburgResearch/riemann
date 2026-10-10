# Lane 3 checkpoint 1 — contract audit and margin re-derivation

## 1. Margin formulas re-derived from L-99020 (CONFIRMED, with the exact algebra)

Source: L-99020 @ origin/review/gpt56-pro/99600-three-interface-hostile-audit,
claims/lemmas/L-99020-compact-score-free-hall-two-sort.md; greedy implementation
origin/claude/riemann-proof-review-8nz34i:experiments/X-105030-maximal-license-and-circ13/lane_repair/core.py, fast.py.

Key exact identities (verified by hand and numerically to <=1e-15):
- T_x(k)*rho_j(k) = Q_{x/k}(j)/sqrt(k)  (denominators 4sqrt(x/k)-3 cancel), so
  B_{x,j} (L-99020.6 aggregate) evaluated at any flow with demand equality and
  column sums c(e) equals  sum_e theta(e) Q_{x/e}(j)/sqrt(e) - sum_o Q_{x/o}(j)/sqrt(o),
  theta = c/T. This IS the orchestrator's M_j. CORRECT.
- s(k) = (5z-3)/(4z-3) = 5/4 + (3/4)/(4z-3), z=sqrt(x/k);  T(k)s(k) = (5/4)T(k) + (3/4)/sqrt(k).
  Hence, USING demand equality sum_e c(e) = D, the score margin
  M_sc = sum_o T(o)s(o) - sum_e c(e)s(e) = (3/4)[sum_o 1/sqrt(o) - sum_e theta(e)/sqrt(e)]
       = (3/4)[-B^s_x + sum_e (1-theta(e))/sqrt(e)].
  L-99020.7 (score inequality) <=> score edge term <= 0 <=> M_sc >= 0. CORRECT.
  (My edge_cases.py computes M_sc both ways; agreement to 1e-15 at every tested x.)
- The four aggregate tests {TB>=0, M_2>=0, M_3>=0, M_sc>=0} are exactly
  {demand coverable, B_{x,2}>=0, B_{x,3}>=0, L-99020.7} at the greedy flow.

## 2. Theorem R carries over verbatim to the frozen lattice (CONFIRMED)

Theorem R's three ingredients are index-set-agnostic:
(i) aggregates are affine in column sums c(e) given demand equality — unchanged;
(ii) rho_j(k) = Q_{x/k}(j)/(4sqrt(x/k)-3) is a function of Y=x/k alone,
    nonincreasing in k (L-105001 §1 derivative / Lemma 1 of the L-105031 deposit) —
    restriction of a monotone sequence to a sub-index-set is monotone;
(iii) s(k) = 5/4 + (3/4)/(4sqrt(x/k)-3) increasing in k for all k <= x
    (needs only 4sqrt(x/k)-3 > 0, i.e. x/k > 9/16 — automatic). 
So the greedy prefix fill c* on the frozen evens is simultaneously weakly optimal
for BOTH row aggregates and the score aggregate; product flow t(o,e)=T(o)c(e)/D
realizes any admissible column profile (needs D > 0: true for all x >= 2, since
d = 2 is active and odd). Feasibility <=> TB_s(x) >= 0 and the three margin tests
at c*. TB_s >= 1.676601 all x (L-105031(f)) => greedy fill always completes.
Ties: divisor values are distinct so the sort has no ties; rho_j ties (the
rho_j = 0 tail, Y < j) do not affect the optimum value; s is strictly increasing
so the greedy is the unique score-minimizer among row-maximizers. NO GAP.

Note also: the greedy c* is simultaneously optimal for EVERY j >= 2 (rho_j is
nonincreasing for all j by the same lemma), not just j = 2,3 — relevant to
finding F3 below.

## 3. Contract findings (the joints) — three FLAGS

FLAG F1 (consumer of the frozen block — MISMATCH OF ROLE, must be in honest scope).
L-99020's compact fibre is 1 <= x < 67 with squarefree 61-smooth support; for
x < 67 "squarefree <= x" and "squarefree 61-smooth <= x" coincide (no prime in
(61,67)), so the frozen lattice IS the L-99020 alphabet, continued past its
x < 67 ceiling. The adjudicated aggregate-license contract (L-105031 §1: only
B_{x,2} >= 0, B_{x,3} >= 0, L-99020.7, u >= 0 are consumed) was adjudicated for
the compact consumer at x < 67. At x >= 67 NO deposited consumer consumes the
frozen block: T-99020's composition consumes the compact fibres only, and
O-105010's moving-cut architecture consumes a GROWING Y^theta-smooth block
(Dickman-density alphabet), not a frozen 61-smooth one — indeed O-105010 §1
declares the fixed-alphabet architecture budget-infeasible from birth (the
divergence sum_{67<=p<=Y} 1/p). T-105040 is therefore an unconditional statement
about a well-defined finite-alphabet deformation family (the x -> infinity
continuation of the L-99020 block), NOT a consumed interface of the live
architecture. Its statement must say so; it must not claim to discharge
O-105010 §2.1's "uniform-in-theta smooth-fibre statement".

FLAG F2 (two rows only). The contract carries j = 2,3 rows + score. L-99020
speaks of "every component row" (all j >= 2) and T-99020's columns run over all
q >= 2. The restriction to j = 2,3 is adjudicated only inside L-105031 §1
("three aggregates") with the full audit referenced to the deposit report,
which records it at headline level only. T-105040 inherits this adjudication
as a dependency; if a re-audit ever finds the consumer needs B_{x,j} >= 0 for
some j >= 4, T-105040's greedy c* is STILL optimal for those rows (see §2), so
the theorem extends by adding margins M_j — but the deposited theorem would be
incomplete as stated. Record as an explicit dependency, not a proved fact.

FLAG F3 (per-edge vs aggregate). The aggregate license replaces L-99020.6's
per-edge ("coefficientwise") nonnegativity by the aggregate B_{x,j} >= 0. Under
the aggregate-optimal greedy the flow DOES carry anti-monotone edges (L-105031(b):
16.47% of demand at x = 10007^-), so per-edge nonnegativity is genuinely false
for c*. T-105040 is safe if and only if the L-105031 adjudication ("only the
aggregates are consumed") stands. Same dependency discipline as F2. The x = 2
firewall of R-99020 (the row sort never interpreted as a complete positive score
packet; its omitted declared-score coordinate at x = 2 would be negative) is
consistent with the frozen block: at x = 2 the row margins are exactly 0 (see
checkpoint 2) and the sort discipline language must be preserved verbatim.

## 4. Verdict on task 1

The margin formulas are RIGHT for the frozen lattice; the two-row + score
contract is carried over verbatim and correctly, but its authority at x >= 67
is inherited from L-105031's adjudication of the x < 67 consumer, and no
consumer consumes the frozen block at x >= 67 in the moving-cut architecture.
T-105040 must be framed as a model/limit theorem with F1-F3 as recorded
dependencies.
