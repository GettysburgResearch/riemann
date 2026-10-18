"""Adversarial parameter and strict parser checks of the cycle certifier.

The zero-preconditioner control reconstructs the actual full source before
rejecting L=1. Other mutants fail legal-input gates before source work.
"""
from pathlib import Path
import argparse,copy,hashlib,importlib.util,json,sys,time
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'reviews'))
import certify_cyclic as checker

def main(parameters,emit):
    start=time.time();base=checker.load(parameters);folder=ROOT/'adversarial';folder.mkdir(exist_ok=True);results=[]
    changes=[('zero_cross_edge',lambda p:p['centers'].__setitem__(-1,'0')),
        ('negative_cross_edge',lambda p:p['centers'].__setitem__(-1,'-1/10')),
        ('same_single_copy',lambda p:p.__setitem__('cross_types',[2,2])),
        ('nonexistent_singleton_child',lambda p:(p.__setitem__('cross_types',[0,2]),p.__setitem__('cross_vertices',['child','root']))),
        ('missing_highest_order',lambda p:p.__setitem__('degree',24)),
        ('duplicate_active',lambda p:p['active'].__setitem__(-1,p['active'][0])),
        ('missing_center',lambda p:p['centers'].pop()),
        ('zero_hub',lambda p:p.__setitem__('hub_correlation','0')),
        ('negative_radius',lambda p:p.__setitem__('radius','-1/1000')),
        ('nonpositive_physical_weight',lambda p:p['centers'].__setitem__(4,'100')),
        ('zero_preconditioner',lambda p:p.__setitem__('rational_preconditioner',[['0']*(p['degree']//2) for _ in range(p['degree']//2)]))]
    for name,change in changes:
        p=copy.deepcopy(base);change(p);path=folder/(name+'.json');path.write_text(json.dumps(p))
        try:checker.certify(path)
        except (ValueError,TypeError,KeyError,IndexError,ZeroDivisionError) as error:results.append({'mutation':name,'rejected':True,'message':str(error)})
        else:raise ValueError('invalid cycle parameter mutation accepted: '+name)
    for name,body in [('duplicate_key','{"x":1,"x":2}'),('json_float','{"x":0.1}'),('json_nan','{"x":NaN}')]:
        path=folder/(name+'.json');path.write_text(body)
        try:checker.load(path)
        except ValueError as error:results.append({'mutation':name,'rejected':True,'message':str(error)})
        else:raise ValueError('invalid proof parser input accepted: '+name)
    out={'status':'CYCLE_PARAMETER_CONTROLS_PASS','cases':results,'original_parameter_sha256':hashlib.sha256(parameters.read_bytes()).hexdigest(),
        'input_hashes':{'reviews/certify_cyclic.py':hashlib.sha256(Path(checker.__file__).read_bytes()).hexdigest(),'cycle_parameter_controls.py':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
    txt=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n';emit.write_text(txt)
    print('CYCLE_PARAMETER_CONTROLS_PASS',hashlib.sha256(txt.encode()).hexdigest(),'seconds',time.time()-start,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--parameters',type=Path,default=ROOT.parent/'reviews/parameters26_cycle.json');p.add_argument('--emit',type=Path,default=ROOT/'cycle_parameter_controls26.json');a=p.parse_args();main(a.parameters,a.emit)
