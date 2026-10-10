import numpy as np, json, math
res=json.load(open('pred_vs_O.json'))
a,b=-3.716,2.023
rs=[r['O']-(a+b*r['pred']) for r in res]
print('residual O-(a+b*pred): mean %.3f sd %.3f max|.| %.3f'%(np.mean(rs),np.std(rs),max(abs(x) for x in rs)))
tp=sum(1 for r in res if r['pred']>1.84 and r['O']>0); fp=sum(1 for r in res if r['pred']>1.84 and r['O']<=0)
fn=sum(1 for r in res if r['pred']<=1.84 and r['O']>0); tn=sum(1 for r in res if r['pred']<=1.84 and r['O']<=0)
print('threshold pred>1.84 (=3.72/2.02): TP FP FN TN =',tp,fp,fn,tn)
onset=[r for r in res if r['U'] in (2780,2782,2800,2820,2840)]
print('onset rows:',onset)
# slope-only fit through background -3.716? and slope if forced pred coeff 2 exactly:
import statistics
preds=[r['pred'] for r in res]; Os=[r['O'] for r in res]
num=sum((o+3.716)*p for o,p in zip(Os,preds)); den=sum(p*p for p in preds)
print('forced-intercept slope:',round(num/den,3))
