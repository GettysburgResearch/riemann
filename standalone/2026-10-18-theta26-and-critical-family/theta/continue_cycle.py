#!/usr/bin/env python3
"""Full-coordinate continuation on the first20 theta moment manifold.

Adds one positive cycle edge and retunes all46 original coordinates. Ordinary
Decimal output is exploratory; source moments themselves come from complete
directed source26 intervals. A sign change is a root-producer input only.
"""
from pathlib import Path
from decimal import Decimal as D,getcontext
import argparse,json,sys
import search_full as s
sys.path.insert(0,str(Path(__file__).resolve().parent/'extension'))
import explore_added_edge as e


def balanced(z,t,target,left,right,iterations=30,match=10,merit='raw'):
    z=list(z)
    active=s.FREE
    for n in range(iterations):
        value,jac=e.jet(z,t,active,left=left,right=right)
        error=s.norm(value[:match],target[:match])
        if error<D('1e-80'):
            return z,True,n,error
        step=s.direction(z,jac[:match],[y-x for x,y in zip(value[:match],target[:match])],active,'full')
        scales=[s.margins(z)[i] for i in active]
        natural=max(abs(v/a) for v,a in zip(step,scales))
        damping=D(1)
        while damping>D('1e-12'):
            trial=z[:]
            for i,d in zip(active,step):trial[i]+=damping*d
            if s.legal(trial):
                trialvalue,_=e.evaluate(trial,t,left=left,right=right)
                if merit=='natural':
                    correction=s.direction(z,jac[:match],[y-x for x,y in zip(trialvalue[:match],target[:match])],active,'full')
                    accept=max(abs(v/a) for v,a in zip(correction,scales))<natural
                else:
                    accept=s.norm(trialvalue[:match],target[:match])<error
                if accept:
                    break
            damping/=2
        else:
            return z,False,n,error
        z=trial
        if match==11:
            print('FIXED_CYCLE_NEWTON22',n,'ERROR',error,'DAMPING',damping,flush=True)
    return z,False,iterations,error


def main():
    p=argparse.ArgumentParser();p.add_argument('--left',type=int,default=3)
    p.add_argument('--right',type=int,default=8)
    p.add_argument('--max-t',type=D,default=D('.5'))
    p.add_argument('--start-step',type=D,default=D('.0001'))
    p.add_argument('--solve22',type=Path)
    args=p.parse_args();getcontext().prec=120
    target=s.get_target(26)
    original=json.loads((s.SOURCE/'parameters20.json').read_text())
    z=list(map(D,original['centers']))
    if args.solve22:
        seed=json.loads(args.solve22.read_text());z=list(map(D,seed['parameters']));t=D(seed['t'])
        answer,ok,n,err=balanced(z,t,target,args.left,args.right,iterations=140,match=11,merit='natural')
        value,_=e.evaluate(answer,t,degree=26,left=args.left,right=args.right)
        record={'status':'EMPIRICAL_ROOT_PRODUCER_NOT_CERTIFICATE','settled':ok,
                'left':args.left,'right':args.right,'t':str(t),'iterations':n,
                'parameters':[str(v) for v in answer],
                'residuals':[str(x-y) for x,y in zip(value,target)]}
        (s.ROOT/'cycle22_fixedt_center.json').write_text(json.dumps(record,indent=2)+'\n')
        print('FIXED_CYCLE22_END',ok,n,err,flush=True)
        return
    t=D(0);dt=args.start_step;rows=[]
    outfile=s.ROOT/f'cycle_{args.left}_{args.right}_full_continuation.json'
    crossed=False
    for iteration in range(250):
        attempt=min(args.max_t,t+dt) if rows else t
        trial,ok,n,err=balanced(z,attempt,target,args.left,args.right)
        if not ok:
            dt/=2
            print('RETRY',attempt,'STEP',dt,'RESIDUAL',err,flush=True)
            if dt<D('1e-10'):break
            continue
        z=trial;t=attempt
        value,mu=e.evaluate(z,t,degree=26,left=args.left,right=args.right)
        row={'t':str(t),'iterations':n,'first20_relative_residual':str(err),
             'r22':str(value[10]-target[10]),'r24':str(value[11]-target[11]),
             'r26':str(value[12]-target[12]),'parameters':[str(x) for x in z],
             'legal':s.legal(z)}
        rows.append(row)
        outfile.write_text(json.dumps({'status':'EMPIRICAL_CONTINUATION_NOT_CERTIFICATE',
            'left':args.left,'right':args.right,'precision':120,'rows':rows},indent=2)+'\n')
        print('CYCLE',args.left,args.right,'T',t,'R22',row['r22'],'R24',row['r24'],'N',n,flush=True)
        if D(row['r22'])<0:
            crossed=True
            print('EMPIRICAL_BRACKET22',rows[-2]['t'],row['t'],flush=True)
            break
        if t>=args.max_t:break
        if n<=6:dt=min(dt*D('1.5'),D('.025'))
        elif n>=14:dt/=2
    print('CONTINUATION_END','CROSSED' if crossed else 'NO_CROSSING',t,flush=True)


if __name__=='__main__':main()
