import numpy as np, json, math
NP=1100000
pr=np.ones(NP+1,dtype=bool); pr[:2]=False
for p in range(2,int(NP**0.5)+1):
    if pr[p]: pr[p*p::p]=False
prm=np.nonzero(pr)[0]
mu=np.ones(NP+1,dtype=np.float64); mu[0]=0
for p in prm:
    mu[p::p]*=-1; mu[p*p::p*p]=0
nn=np.arange(NP+1,dtype=np.float64); nn[0]=1
m=np.cumsum(mu/nn)
C=0.10113  # (2/pi^2) I_w with I_w=2pi(3ln2-2): 4(3ln2-2)/pi
C=4*(3*math.log(2)-2)/math.pi
base='/tmp/claude-0/-home-user-riemann/d379fac9-baa2-5637-b561-9823a1c28acc/scratchpad/GRAND/progA2/laneS/'
rows=[]
d=json.load(open(base+'out_big.json'))['rows']
for r in d: rows.append(('big',r['U'],r['X'],r['N'],r['O'],r.get('H')))
for f,tag in [('out_uscan.json','uscan'),('out_uscan_onset.json','onset'),('out_uscan_top.json','top'),('out_uscan12.json','u12')]:
    for r in json.load(open(base+f)): rows.append((tag,r['U'],r['X'],r['N'],r['O'],None))
res=[]
for tag,U,X,N,O,H in rows:
    mU=m[U]; pred=C*mU*mU*N/math.log(N)
    res.append({'tag':tag,'U':U,'sqrtU_m':round(mU*math.sqrt(U),3),'pred':round(pred,3),'O':round(O,3),'H':H})
# correlation: pred vs O
import statistics
preds=[r['pred'] for r in res]; Os=[r['O'] for r in res]
mp_,mo=statistics.mean(preds),statistics.mean(Os)
cov=sum((p-mp_)*(o-mo) for p,o in zip(preds,Os))
corr=cov/math.sqrt(sum((p-mp_)**2 for p in preds)*sum((o-mo)**2 for o in Os))
print('Pearson corr(pred, O) over',len(res),'points:',round(corr,4))
# classification: pred>3.3 vs O>0
tp=sum(1 for r in res if r['pred']>3.3 and r['O']>0); fp=sum(1 for r in res if r['pred']>3.3 and r['O']<=0)
fn=sum(1 for r in res if r['pred']<=3.3 and r['O']>0); tn=sum(1 for r in res if r['pred']<=3.3 and r['O']<=0)
print('threshold pred>3.3: TP,FP,FN,TN =',tp,fp,fn,tn)
# linear fit O ~ a + b*pred
b=cov/sum((p-mp_)**2 for p in preds); a=mo-b*mp_
print('fit O = %.3f + %.3f * pred'%(a,b))
json.dump(res,open('pred_vs_O.json','w'),indent=0)
# print the big rows + extremes
print('\n big rows (X, U, sqrtU*m, pred, O, H):')
for r in res:
    if r['tag']=='big': print(' ',r['U'],r['sqrtU_m'],r['pred'],r['O'],r['H'])
print('\n top-|pred| rows:')
for r in sorted(res,key=lambda r:-r['pred'])[:12]: print(' ',r['tag'],r['U'],r['sqrtU_m'],r['pred'],r['O'])
print('\n positives with small pred (mismatches):')
for r in res:
    if r['O']>0 and r['pred']<1.0: print(' ',r['tag'],r['U'],r['sqrtU_m'],r['pred'],r['O'])
