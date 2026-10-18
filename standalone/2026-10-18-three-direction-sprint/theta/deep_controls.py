"""Exact structural/arithmetic and cross-protocol deep-source controls."""
from pathlib import Path
from fractions import Fraction as F
import ast,hashlib,json,sys,time
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'inherited'))
import primitive512 as deep
import pr886_primitive as old

def require(ok,message):
    if not ok:raise ValueError(message)

def normalized_ast(path):
    tree=ast.parse(path.read_text());tree.body=tree.body[1:] if isinstance(tree.body[0],ast.Expr) and isinstance(tree.body[0].value,ast.Constant) and isinstance(tree.body[0].value.value,str) else tree.body
    for node in tree.body:
        if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name):
            if node.targets[0].id=='BITS':node.value=ast.Constant(320)
            if node.targets[0].id=='DEGREE':node.value=ast.Constant(120)
    return ast.dump(tree,include_attributes=False)

def main():
    start=time.time();require(normalized_ast(ROOT/'primitive512.py')==normalized_ast(ROOT/'inherited/pr886_primitive.py'),'only intended executable precision constants differ')
    require(deep.BITS==512 and deep.DEGREE==180,'new precision constants')
    factor=1<<(deep.BITS-old.BITS)
    def nested(a,c):return a.lo>=c.lo*factor and a.hi<=c.hi*factor
    require(nested(deep.pi_interval(),old.pi_interval()),'higher pi enclosure nested in pinned old enclosure')
    probes=[F(-256),F(-4),F(-1,2),F(0),F(1,10),F(1,8),F(1),F(10),F(256)]
    for x in probes:require(nested(deep.exp(x),old.exp(x)),'higher exponential enclosure nested at '+str(x))
    require(4*196**2*3**11+6*196*3**6<10**11,'Cauchy density integer bound')
    require(F(53,4)<16 and F(675,64)<11 and F(375,64)<6,'actual cutoff and circle exponents')
    require(F(9,8)**4/2**51<F(1,2),'full omitted-index geometric ratio')
    source=json.loads((ROOT/'source_deep32.json').read_text());ancestor=json.loads((ROOT/'source32.json').read_text())
    require(source['degree']==32 and source['bits']==512 and source['counts']==[36,24,16,12,8,6,4],'complete deep source metadata')
    tests=0
    def record_nested(a,c):return a[0]>=c[0]*factor and a[1]<=c[1]*factor
    for key in ['variance']:
        require(record_nested(source[key],ancestor[key]),'nested full-source '+key);tests+=1
    for key in ['standardized_moments','standardized_cumulant_ratios']:
        for a,c in zip(source[key],ancestor[key]):require(record_nested(a,c),'nested complete '+key);tests+=1
    for key,a in source['raw'].items():require(record_nested(a,ancestor['raw'][key]),'nested raw complete moment '+key);tests+=1
    out={'status':'DEEP_CONTROLS_PASS','ast_only_BITS_DEGREE_change':True,'exponential_probes':list(map(str,probes)),'nested_source_intervals':tests,
        'input_hashes':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ['primitive512.py','source_deep.py','source_deep32.json','source32.json','inherited/pr886_primitive.py','deep_controls.py']}}
    txt=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n';(ROOT/'deep_controls.json').write_text(txt)
    print('DEEP_CONTROLS_PASS',hashlib.sha256(txt.encode()).hexdigest(),'seconds',time.time()-start,flush=True)

if __name__=='__main__':main()
