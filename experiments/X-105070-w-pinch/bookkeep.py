import json, math, os
# (A) grid sanity on lane S data: U=floor(X^{1/3}), N=floor(X/U); floor-cell size
SIGN_HUNT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'X-105057-sign-hunt')
rows = json.load(open(os.path.join(SIGN_HUNT, 'out_big.json')))['rows']
try:
    d = json.load(open(os.path.join(SIGN_HUNT, 'out_uscan.json')))
    rows += d if isinstance(d, list) else d['rows']  # out_uscan.json is a bare list (F7 fix)
except Exception as e: print("uscan skip:", e)
ok=0; bad=[]
maxdev=0
for r in rows:
    X,U,N=r['X'],r['U'],r['N']
    Uc=int(round(X**(1/3.)));
    while Uc**3> X: Uc-=1
    while (Uc+1)**3<=X: Uc+=1
    Nc=X//Uc
    if Uc==U and Nc==N: ok+=1
    else: bad.append((X,U,Uc,N,Nc))
    dev=abs(math.log(N)-(2/3.)*math.log(X))*X**(1/3.)
    maxdev=max(maxdev,dev)
print("rows:",len(rows),"U/N-formula ok:",ok,"bad:",bad[:3])
print("max X^{1/3}|log N-(2/3)log X| =",round(maxdev,4)," (P2.2 claims O(1) -> bounded)")
# (B) d-cutoff exactness incl. perfect cubes: integer d> floor(X^{1/3}) iff d>X^{1/3}
viol=0
for X in list(range(60,3000))+[k**3 for k in range(4,60)]:
    U=int(round(X**(1/3.)))
    while U**3>X: U-=1
    while (U+1)**3<=X: U+=1
    for d in range(1,U+3):
        if (d>U)!=(d>X**(1/3.)-1e-12 if abs(d**3-X)<0.5 else d>X**(1/3.)):
            pass
    # direct: d>U iff d^3>X (integers): check
    for d in range(1,U+3):
        if (d>U)!=(d**3>X): viol+=1
print("d-cutoff violations (d>U iff d^3>X):",viol)
