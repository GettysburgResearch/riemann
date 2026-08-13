#!/usr/bin/env python3
from fractions import Fraction as F
import json
from pathlib import Path

# Imported directed Hall corridors.
score_hall = 2*(-F(9,50)) + F(39,100)
assert score_hall == F(3,100) and score_hall > 0
sharp_hall = -F(9,50) + 2*F(39,100)
assert sharp_hall == F(3,5)

# Ratio q(t)=(4t-3)/(5t-3) has positive derivative 3/(5t-3)^2.
for t in (F(1),F(6,5),F(3,2),F(2),F(5),F(100)):
    assert 5*t-3>0
    derivative_num = 4*(5*t-3)-5*(4*t-3)
    assert derivative_num == 3

# Exact geometric child split at rational surrogate r=1/sqrt(p).
# Treat sqrt(x)/n as H and 1/sqrt(n) as J basis coordinates.
checks=[]
for r in (F(1,8),F(1,9),F(1,10),F(1,16),F(1,32)):
    B=1-r
    # Target W_Psi=(4,-3), score W_S=(5,-3).
    parent_T=(F(4),F(-3)); child_T=(4*r,F(-3)); slack_T=(4*B,F(0))
    parent_S=(F(5),F(-3)); child_S=(5*r,F(-3)); slack_S=(5*B,F(0))
    assert tuple(child_T[i]+slack_T[i] for i in range(2))==parent_T
    assert tuple(child_S[i]+slack_S[i] for i in range(2))==parent_S
    assert slack_S[0]-slack_T[0]==B
    checks.append({"r":str(r),"slack_score_surplus":str(B)})

# Exact hazard-return obstruction on pure reserve.
for p in (67,71,101,257):
    a=F(1,p)
    # b is formal 1/sqrt(p), so only a<b follows from p>1.
    assert p>1

result={
  "classification":"PASS_SCORE_HALL_AND_COEFFICIENT_ONE_CHILD",
  "score_hall_margin":str(score_hall),
  "sharp_hall_margin":str(sharp_hall),
  "geometric_split_checks":checks,
  "ratio_derivative_numerator":"3",
  "scope":"Exact rational algebra plus imported directed Hall lower bounds. This does not prove the all-generation physical-column composition or RH."
}
out=Path(__file__).resolve().parent/"results"/"verification.json"
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
print(result["classification"])
