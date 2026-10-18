"""Re-evaluate the saved candidates; successful replay is NOT moment matching."""
from pathlib import Path
import json,numpy as np
from models import MomentModel
ROOT=Path(__file__).resolve().parent
SPECS={
'groups_best0.json':([8]*4,False,0,True,True),
'groups6_best0.json':([32,6,2,2,1,1],False,0,True,True),
'gaussian_groups0.json':([6,2,2,1,1],True,0,True,False),
'rbm0.json':([1]*12,True,3,False,False),
'complete0.json':([1]*12,True,0,True,False),
'compound0.json':([1]*12,True,3,True,False),
'antiferro0.json':([1]*12,True,0,True,False),
}
def run():
    target=json.loads((ROOT/'target.json').read_text());out={}
    for name,(groups,gaussian,hidden,pairs,dummy) in SPECS.items():
        record=json.loads((ROOT/'records'/name).read_text());z=np.asarray(record['z'])
        model=MomentModel(groups,list(map(float,target['an'])),gaussian=gaussian,
                          hidden=hidden,pair_edges=pairs,retain_dummy_pairs=dummy)
        f,_=model.evaluate(z);norm=float(np.linalg.norm(f))
        if not np.isclose(norm,record['err'],rtol=1e-5,atol=1e-12):
            raise ValueError(f'{name}: saved candidate does not reproduce: {norm}')
        out[name]={'objective_norm':norm,'saved_objective_norm':record['err'],
                   'all_ten_residuals':f.tolist(),'represented_visible_spins':sum(groups),
                   'hidden_zero_weight_spins':hidden,'magnetization_states':len(model.M),
                   'independent_gaussian':gaussian,**model.admissibility(z)}
        if norm<1e-10:raise ValueError('unexpected near-root: needs separate review, never auto-certify')
    return {'execution':'CANDIDATE_REPLAY_OK','mathematical_result':'NO_DEGREE_20_CERTIFICATE',
            'RH_proved':False,'candidate_results':out}
if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
