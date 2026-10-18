"""Independent exact assembly checks for a complete generic tree witness."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib,time
import model,finite_controls
ROOT=Path(__file__).resolve().parent

def run(parameters,emit):
    start=time.time();p=json.loads(parameters.read_text());z=list(map(F,p['centers']));counts=p['counts'];eta=F(p['hub_correlation']);degree=p['degree']
    fixture=finite_controls.fixture(degree)
    _,raw=model.evaluate(z,counts,eta,degree);direct=model.direct_assembly(z,counts,eta,degree)
    finite_controls.require(raw==direct,'complete conditional raw EGF and cumulant assemblies agree')
    finite_controls.require(len(raw)==degree+1 and len(raw[:-1])!=degree+1,'full endpoint order retained')
    changed=list(counts);changed[-1]-=1
    finite_controls.require(model.direct_assembly(z,changed,eta,degree)!=raw,'promoted bulk multiplicity is load-bearing')
    finite_controls.require(model.evaluate(z,counts,F(0),degree)[1]!=raw,'positive hub is load-bearing')
    # The precise initial boundary promotion preserves the entire law, not
    # only its first two moments. Check it at every retained rational order.
    old=json.loads((ROOT/'parameters22.json').read_text());zz=list(map(F,old['centers']));cc=list(old['counts']);cc[0]-=254;cc+=[127];zz +=[2*zz[0],F(0),F(1,2)]
    finite_controls.require(model.evaluate(zz,cc,F(0),degree)[1]==model.evaluate(list(map(F,old['centers'])),old['counts'],F(0),degree)[1],'127 boundary dimers equal254 old fair spins through complete endpoint')
    out={'status':'FINITE_TREE_CONTROLS_PASS','degree':degree,'fixture':fixture,'raw_orders_compared':degree+1,'vertices':counts[0]+2*sum(counts[1:])+1,
        'direct_egf_cumulant_match':True,'promoted_multiplicity_mutation_rejected':True,'hub_deletion_rejected':True,'missing_highest_order_rejected':True,'bulk_promotion_boundary_identity':True,
        'input_hashes':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ['model.py','finite_controls.py','finite_tree_controls.py','parameters22.json']},'parameter_sha256':hashlib.sha256(parameters.read_bytes()).hexdigest()}
    txt=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n';emit.write_text(txt)
    print('FINITE_TREE_CONTROLS_PASS',hashlib.sha256(txt.encode()).hexdigest(),'seconds',time.time()-start,flush=True)
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--parameters',type=Path,required=True);p.add_argument('--emit',type=Path,required=True);a=p.parse_args();run(a.parameters,a.emit)
