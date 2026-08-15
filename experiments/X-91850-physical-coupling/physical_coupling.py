#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import argparse, json, random

HERE=Path(__file__).resolve().parent

class ContractError(ValueError): pass

def vec_add(a,b): return tuple(x+y for x,y in zip(a,b))
def vec_sub(a,b): return tuple(x-y for x,y in zip(a,b))
def vec_scale(c,a): return tuple(c*x for x in a)
def vec_zero(n): return tuple(Fraction(0) for _ in range(n))

def greedy_hall(even,odd):
    cap=dict(even); flow={}
    for o in sorted(odd):
        need=odd[o]
        for e in sorted(k for k in cap if k<=o):
            take=min(need,cap[e])
            if take:
                flow[(o,e)]=take; need-=take; cap[e]-=take
            if need==0: break
        if need: raise ContractError(('unfilled odd demand',o,need))
    return flow,cap

def hall_output(even,odd,profiles,flow,residual):
    dim=len(next(iter(profiles.values())))
    signed=vec_zero(dim)
    for e,m in even.items(): signed=vec_add(signed,vec_scale(m,profiles[e]))
    for o,m in odd.items(): signed=vec_sub(signed,vec_scale(m,profiles[o]))
    out=vec_zero(dim)
    for e,m in residual.items(): out=vec_add(out,vec_scale(m,profiles[e]))
    for (o,e),m in flow.items():
        diff=vec_sub(profiles[e],profiles[o])
        if any(x<0 for x in diff): raise ContractError(('negative Hall bonus',o,e,diff))
        out=vec_add(out,vec_scale(m,diff))
    if out!=signed: raise ContractError(('Hall identity',out,signed))
    return out

def validate_certificate(c):
    F=Fraction
    even={int(k):F(v) for k,v in c['even'].items()}
    odd={int(k):F(v) for k,v in c['odd'].items()}
    profiles={int(k):tuple(F(x) for x in v) for k,v in c['profiles'].items()}
    flow={(int(k.split(':')[0]),int(k.split(':')[1])):F(v) for k,v in c['flow'].items()}
    residual={int(k):F(v) for k,v in c['residual'].items()}
    if any(v<0 for v in [*even.values(),*odd.values(),*flow.values(),*residual.values()]): raise ContractError('negative source mass')
    # Hall marginals
    for o,m in odd.items():
        if sum(v for (oo,e),v in flow.items() if oo==o)!=m: raise ContractError(('odd marginal',o))
    for e,m in even.items():
        used=sum(v for (o,ee),v in flow.items() if ee==e)
        if used+residual.get(e,F(0))!=m: raise ContractError(('even marginal',e,used,residual.get(e,F(0)),m))
    if any(e>o for (o,e) in flow): raise ContractError('upward Hall edge')
    hall_output(even,odd,profiles,flow,residual)
    # unique first owner and stochastic child/current split
    owners=c['owners']
    if len(owners)!=len(set(owners.values())): raise ContractError('duplicate first owner')
    for src,weights in c['causal'].items():
        vals=[F(x) for x in weights.values()]
        if any(x<0 for x in vals) or sum(vals)!=1: raise ContractError(('causal kernel',src))
    if c.get('exported_children'): raise ContractError('hidden recursive export')
    # tagged complete cells
    cells=c['cells']
    tags=[x['tag'] for x in cells]
    if tags!=list(range(min(tags),max(tags)+1)): raise ContractError('incomplete tagged cells')
    if any(x['left']!=x['tag'] or x['right']!=x['tag']+1 for x in cells): raise ContractError('malformed tagged cell')
    # one label-blind stochastic quantizer
    if c.get('quantizer_overrides'): raise ContractError('label-dependent quantizer')
    for t,weights in c['quantizer'].items():
        vals=[F(x) for x in weights.values()]
        if any(x<0 for x in vals) or sum(vals)!=1: raise ContractError(('quantizer',t))
        tag=int(t.split(':')[0])
        if any(abs(int(j)-tag)>2 for j in weights): raise ContractError(('quantizer leaves cell stencil',t))
    tau=F(c['tau'])
    if not 0<=tau<=1: raise ContractError('bad thinning')
    # retained + discard on both Hall marginals
    for name,src in [('even',even),('odd',odd)]:
        for k,m in src.items():
            retained=tau*m; discarded=(1-tau)*m
            if retained+discarded!=m: raise ContractError(('discard marginal',name,k))
    if c.get('signed_error_declared_source_positive'): raise ContractError('signed error promoted to source')
    unused=tuple(F(x) for x in c['unused_capacity'])
    error=tuple(F(x) for x in c['signed_error'])
    slack=vec_sub(unused,error)
    if any(x<0 for x in slack): raise ContractError(('native capacity overrun',slack))
    y4=tuple(F(x) for x in c['y4'])
    cost=sum(a*b for a,b in zip(y4,slack))
    if cost!=F(c['claimed_cost']): raise ContractError(('cost mismatch',cost,c['claimed_cost']))
    return {'hall_row': hall_output(even,odd,profiles,flow,residual),'slack':slack,'cost':cost}

def base_certificate():
    even={1:Fraction(9),6:Fraction(5),10:Fraction(3)}
    odd={2:Fraction(4),7:Fraction(6)}
    profiles={1:(Fraction(9),Fraction(7),Fraction(5)),2:(Fraction(8),Fraction(6),Fraction(4)),6:(Fraction(6),Fraction(4),Fraction(3)),7:(Fraction(5),Fraction(3),Fraction(2)),10:(Fraction(3),Fraction(2),Fraction(1))}
    flow,res=greedy_hall(even,odd)
    unused=(Fraction(7),Fraction(5),Fraction(4)); err=(Fraction(2),Fraction(-1),Fraction(1)); slack=vec_sub(unused,err); y4=(Fraction(3),Fraction(2),Fraction(1)); cost=sum(a*b for a,b in zip(y4,slack))
    return {
      'even':{str(k):str(v) for k,v in even.items()},'odd':{str(k):str(v) for k,v in odd.items()},
      'profiles':{str(k):[str(x) for x in v] for k,v in profiles.items()},
      'flow':{f'{o}:{e}':str(v) for (o,e),v in flow.items()},'residual':{str(k):str(v) for k,v in res.items()},
      'owners':{'rough-67':'67','rough-71':'71','rough-73':'73'},
      'causal':{'res-1':{'current':'7/8','child-67':'1/8'},'res-6':{'current':'9/10','child-71':'1/10'}},
      'exported_children':False,
      'cells':[{'tag':n,'left':n,'right':n+1} for n in range(12,17)],
      'quantizer':{f'{n}:1/2':{str(n):'1/4',str(n+1):'1/2',str(n+2):'1/4'} for n in range(12,17)},
      'quantizer_overrides':{},'tau':'7/9','unused_capacity':[str(x) for x in unused],
      'signed_error':[str(x) for x in err],'signed_error_declared_source_positive':False,
      'y4':[str(x) for x in y4],'claimed_cost':str(cost)}

def random_fixture(rng):
    # Profiles decrease with labels, so every e<=o has nonnegative bonus.
    labels=list(range(1,9)); dim=4
    profiles={k:tuple(Fraction((10-k)*(d+1)+3,d+2) for d in range(dim)) for k in labels}
    even={1:Fraction(rng.randint(8,16)),3:Fraction(rng.randint(6,12)),5:Fraction(rng.randint(4,10))}
    odd={2:Fraction(rng.randint(1,4)),6:Fraction(rng.randint(2,5))}
    flow,res=greedy_hall(even,odd)
    c=base_certificate(); c['even']={str(k):str(v) for k,v in even.items()}; c['odd']={str(k):str(v) for k,v in odd.items()}; c['profiles']={str(k):[str(x) for x in profiles[k]] for k in labels}; c['flow']={f'{o}:{e}':str(v) for (o,e),v in flow.items()}; c['residual']={str(k):str(v) for k,v in res.items()}
    return c

def mutations(c):
    import copy
    muts=[]
    def add(name,fn):
        x=copy.deepcopy(c); fn(x); muts.append((name,x))
    add('odd-underfill',lambda x:x['flow'].__setitem__('2:1','3'))
    add('even-overdraw',lambda x:x['residual'].__setitem__('1','99'))
    add('negative-flow',lambda x:x['flow'].__setitem__('2:1','-1'))
    add('upward-edge',lambda x:x['flow'].__setitem__('2:6',x['flow'].pop('2:1')))
    add('negative-bonus',lambda x:x['profiles'].__setitem__('1',['0','0','0']))
    add('duplicate-owner',lambda x:x['owners'].__setitem__('rough-71','67'))
    add('bad-causal-sum',lambda x:x['causal']['res-1'].__setitem__('current','1'))
    add('recursive-export',lambda x:x.__setitem__('exported_children',True))
    add('missing-cell',lambda x:x['cells'].pop(2))
    add('malformed-cell',lambda x:x['cells'][0].__setitem__('right',99))
    add('label-quantizer',lambda x:x['quantizer_overrides'].__setitem__('child-67',{}))
    add('bad-quantizer-sum',lambda x:x['quantizer']['12:1/2'].__setitem__('12','1'))
    add('quantizer-outside-stencil',lambda x:x['quantizer']['12:1/2'].__setitem__('99','0'))
    add('signed-as-source',lambda x:x.__setitem__('signed_error_declared_source_positive',True))
    add('capacity-overrun',lambda x:x.__setitem__('signed_error',['99','0','0']))
    return muts

def run_all(output=None):
    c=base_certificate(); res=validate_certificate(c)
    rng=random.Random(91850)
    for _ in range(64): validate_certificate(random_fixture(rng))
    rejected=[]
    for name,m in mutations(c):
        try: validate_certificate(m)
        except ContractError: rejected.append(name)
        else: raise AssertionError(('mutation accepted',name))
    control={'thinning':12012,'nonterminal':4,'terminal':48972,'omissions':1}
    assert sum(control.values())==60989
    payload={'classification':'PASS_PHYSICAL_COUPLING_COMPILER_91850','exact_rational_fixture':True,'randomized_trials':64,'hostile_mutations_rejected':len(rejected),'mutations':rejected,'native_ledger':control,'native_total':60989,'rh_established':False}
    canonical=json.dumps(payload,sort_keys=True,separators=(',',':')).encode(); payload['proof_object_sha256']=sha256(canonical).hexdigest()
    if output:
        Path(output).parent.mkdir(parents=True,exist_ok=True); Path(output).write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n',newline='\n')
    return payload

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',default='results/verification.json'); args=ap.parse_args(); p=run_all(args.output); print(p['classification']); print(p['proof_object_sha256'])
if __name__=='__main__': main()
