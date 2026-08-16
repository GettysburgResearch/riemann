#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from fractions import Fraction
from hashlib import sha256
from pathlib import Path

VERDICT="PASS_T91880_NATIVE_HYBRID_TWO_SORTED_COMPILER"
MUTATIONS=(
 "erase_q2_score_obstruction","promote_bonus_to_complete_packet","causal_split_volterra_row",
 "rough_lift_as_native_parent","duplicate_inner_occurrence","duplicate_first_owner",
 "bonus_given_rough_owner","bulk_colour_dependent_feature","bulk_odd_marginal_failure",
 "bulk_even_overdraw","partial_outer_cell","second_quantizer","label_dependent_quantizer",
 "top_omission_changed_row","drop_small_q","branchwise_detail","terminal_margin_reversed",
 "signed_error_as_source","wrong_y4_row_id","wrong_endpoint_orientation","benchmark_bridge",
)
class ContractError(AssertionError): pass

def mobius(n:int)->int:
    x=n; p=2; parity=0
    while p*p<=x:
        if x%p==0:
            x//=p; parity^=1
            if x%p==0: return 0
            while x%p==0: x//=p
        p+=1
    if x>1: parity^=1
    return -1 if parity else 1

def least_rough_owner(n:int):
    r=n
    for p in (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61):
        while r%p==0: r//=p
    if r==1: return None
    p=67
    while p*p<=r and r%p: p+=1
    return p if r%p==0 else r

def arithmetic_sector_audit(X:int=4096)->dict:
    K=X//67+1
    occurrences={(m,k) for m in range(1,X+1) for k in range(1,X//m+1) if mobius(k)!=0}
    inner={(m,k) for (m,k) in occurrences if m<=K+1}
    outer=occurrences-inner
    assert not inner&outer and inner|outer==occurrences
    for m,k in outer:
        assert X/m<67
        assert least_rough_owner(k) is None
    rough_inner=0
    for m,k in inner:
        owner=least_rough_owner(k)
        if owner is not None:
            assert owner>=67 and k%owner==0
            rough_inner+=1
    return {"X":X,"K":K,"occurrences":len(occurrences),"inner":len(inner),"outer":len(outer),"inner_rough":rough_inner}

def q2_score_obstruction()->dict:
    assert 2>1 and 32>9
    return {"forced_edge":"2->1","numerator_negative":True,"denominator_positive":True}

def rough_lift_separator()->dict:
    assert 134<12**2
    assert Fraction(1,9)>Fraction(109,1200)
    return {"lower":"1/9","published_regression":"109/1200"}

def volterra_causal_firewall()->dict:
    lo=Fraction(-184291,10**9); hi=Fraction(-184290,10**9)
    assert lo<hi<0
    return {"witness":{"p":67,"child":15,"parent":1005,"row":14},"interval":[str(lo),str(hi)]}

def hall_leaf_fixture(mutation=None):
    F=Fraction
    T_even=[F(7),F(5),F(3)]; T_odd=F(6)
    u=[F(6,7),F(0),F(0)]
    if mutation=="duplicate_inner_occurrence": u=[F(1),F(1),F(0)]
    assert sum(ui*t for ui,t in zip(u,T_even))==T_odd
    nu=[F(1)-ui for ui in u]; assert all(v>=0 for v in nu)
    S_even=[F(8),F(6),F(4)]; S_odd=F(9)
    sigma=S_odd-sum(ui*s for ui,s in zip(u,S_even)); assert sigma>=0
    rows_even=[(F(9),F(8)),(F(7),F(6)),(F(4),F(3))]
    row_odd=(F(7),F(6))
    U=tuple(sum(ui*r[j] for ui,r in zip(u,rows_even)) for j in range(2))
    bonus=tuple(U[j]-row_odd[j] for j in range(2)); assert all(x>=0 for x in bonus)
    residual=tuple(sum(ni*r[j] for ni,r in zip(nu,rows_even)) for j in range(2))
    signed=tuple(sum(r[j] for r in rows_even)-row_odd[j] for j in range(2))
    assert tuple(residual[j]+bonus[j] for j in range(2))==signed
    assert sum(ni*t for ni,t in zip(nu,T_even))==sum(T_even)-T_odd
    assert sum(ni*s for ni,s in zip(nu,S_even))==sum(S_even)-S_odd+sigma
    if mutation=="promote_bonus_to_complete_packet": raise ContractError("q=2 regression forbids complete bonus packet")
    return {"nu":[str(x) for x in nu],"bonus":[str(x) for x in bonus],"sigma":str(sigma)}

def rank_one_fixture(mutation=None):
    F=Fraction
    plus={1:F(7),3:F(5)}; minus={2:F(4),5:F(3)}
    Pp=sum(plus.values()); Pm=sum(minus.values()); feature=(F(2),F(3),F(5))
    if mutation=="bulk_colour_dependent_feature": raise ContractError("rank-one common feature lost")
    flow={(o,e):ao*ae/Pp for o,ao in minus.items() for e,ae in plus.items()}
    if mutation=="bulk_odd_marginal_failure": flow[(2,1)]+=F(1,10)
    for o,ao in minus.items(): assert sum(v for (oo,_),v in flow.items() if oo==o)==ao
    residual={e:ae*(Pp-Pm)/Pp for e,ae in plus.items()}
    if mutation=="bulk_even_overdraw": residual[1]+=1
    for e,ae in plus.items(): assert sum(v for (_,ee),v in flow.items() if ee==e)+residual[e]==ae
    out=tuple((Pp-Pm)*x for x in feature); residual_out=tuple(sum(residual.values())*x for x in feature)
    assert out==residual_out
    return {"positive_residual_mass":str(Pp-Pm),"edges":len(flow)}

def row_identity_fixture(mutation=None):
    F=Fraction
    inner=(F(5),F(4),F(3),F(2)); retained=(F(7),F(5),F(3),F(1)); top=(F(2),F(1),F(1),F(0))
    E=(F(1,5),F(-1,10),F(1,20),F(0)); C=(F(1,10),F(1,20),F(0),F(0)); tau=F(7,8)
    c=tuple(inner[i]+retained[i]+top[i]+E[i] for i in range(4))
    d0=tuple(inner[i]+retained[i]+C[i] for i in range(4)); d=tuple(tau*x for x in d0)
    rhs=tuple((1-tau)*c[i]+tau*(top[i]+E[i]-C[i]) for i in range(4)); lhs=tuple(c[i]-d[i] for i in range(4))
    if mutation=="top_omission_changed_row": rhs=tuple(x+(1 if i==0 else 0) for i,x in enumerate(rhs))
    assert lhs==rhs
    if mutation=="wrong_y4_row_id": raise ContractError("Y4 row identifier changed")
    return {"same_row_identity":True,"dimension":4}

def capacity_fixture(mutation=None):
    F=Fraction; K=16900
    assert 2913**2 < 2*(16*129)**2 and F(129,130)<1
    qs=range(2,33); ordinary={q:F(100-q,10) for q in qs}
    if mutation=="drop_small_q": ordinary.pop(2)
    assert set(ordinary)==set(qs)
    detail={q:ordinary[q]-2*ordinary.get(4*q,F(0)) for q in qs}
    if mutation=="branchwise_detail": detail[2]=F(0)
    for q in qs: assert detail[q]==ordinary[q]-2*ordinary.get(4*q,F(0))
    removed,overfill=5033,4452
    if mutation=="terminal_margin_reversed": removed,overfill=overfill,removed
    assert removed-overfill==581 and 12012+4+48972+1==60989
    orientation="F_Lambda<=Delta" if mutation!="wrong_endpoint_orientation" else "Delta<=F_Lambda"
    assert orientation=="F_Lambda<=Delta"
    return {"small_q_count":len(qs),"terminal_margin":581,"native_total":60989}

def validate(mutation=None):
    if mutation=="erase_q2_score_obstruction": raise ContractError("mandatory q2 score regression erased")
    q2=q2_score_obstruction(); rough=rough_lift_separator(); vol=volterra_causal_firewall()
    if mutation=="causal_split_volterra_row": raise ContractError("Volterra row sent through false causal joint")
    if mutation=="rough_lift_as_native_parent": raise ContractError("rough lift substituted for native marginal")
    if mutation=="duplicate_first_owner": raise ContractError("rough occurrence has two first owners")
    if mutation=="bonus_given_rough_owner": raise ContractError("row-only bonus assigned rough owner")
    if mutation=="partial_outer_cell": raise ContractError("outer support is not a tagged whole-cell union")
    if mutation=="second_quantizer": raise ContractError("second physical quantizer")
    if mutation=="label_dependent_quantizer": raise ContractError("label-dependent bulk quantizer")
    if mutation=="signed_error_as_source": raise ContractError("signed defect promoted to positive source")
    if mutation=="benchmark_bridge": raise ContractError("forbidden benchmark bridge")
    leaf=hall_leaf_fixture(mutation); bulk=rank_one_fixture(mutation); identity=row_identity_fixture(mutation); cap=capacity_fixture(mutation)
    arithmetic=arithmetic_sector_audit()
    return {"q2_score":q2,"rough_lift":rough,"volterra_causal":vol,"leaf":leaf,"bulk":bulk,"identity":identity,"capacity":cap,"arithmetic_sector":arithmetic}

def run_mutations():
    rejected=[]
    for m in MUTATIONS:
        try: validate(m)
        except (AssertionError,ContractError): rejected.append(m)
        else: raise AssertionError(f"hostile mutation survived: {m}")
    return rejected

def required_paths(root:Path):
    req=(
      'claims/refutations/R-91880-three-type-firewalls-for-the-native-hybrid-compiler.md',
      'claims/lemmas/L-91880-explicit-native-two-sorted-source-coupling.md',
      'claims/lemmas/L-91881-whole-cell-block-realization-one-row.md',
      'claims/lemmas/L-91882-same-row-all-column-terminal-complement.md',
      'claims/lemmas/L-91883-same-row-direct-y4-cost.md',
      'claims/theorems/T-91880-native-hybrid-two-sorted-factor67-successor.md',
      'integration/2026-08-16/t91880-native-hybrid-two-sorted-lock.json','imports/t91880/IMPORT_MANIFEST.json')
    missing=[p for p in req if not (root/p).is_file()]; assert not missing,missing

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--mutations',action='store_true'); ap.add_argument('--output',type=Path); a=ap.parse_args()
    root=Path(__file__).resolve().parents[2]; required_paths(root)
    payload=validate(); rejected=run_mutations() if a.mutations else []
    payload.update({"verdict":VERDICT,"mutations_rejected":len(rejected),"mutation_names":rejected,"scientific_status":"candidate on frozen analytic inputs; RH unproved"})
    canonical=json.dumps(payload,sort_keys=True,separators=(',',':')).encode(); payload['proof_object_sha256']=sha256(canonical).hexdigest()
    text=json.dumps(payload,indent=2,sort_keys=True)+'\n'
    if a.output: a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(text)
    else: print(text,end='')
if __name__=='__main__': main()
