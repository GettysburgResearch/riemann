"""Non-directed exploration prompted by new PR867; never a certificate."""
import json, subprocess, math, sys
from pathlib import Path
import mpmath as mp
mp.mp.dps=65

def git_json(sha,path):return json.loads(subprocess.check_output(['git','show',sha+':'+path],text=True))
sha='4c7898432546814812b2be8c72fc199e294354d1'
data=git_json(sha,'standalone/2026-09-12-astra-weight-adapted-star/parameters.json')
old=git_json('0640c9c59be0bf20c18258460a7517fb09728e82','standalone/2026-09-12-astra-interacting-cluster-realization/result.json')
x=[mp.mpf(a) for a in data['centers']]
active=data['active'];nu=data['counts'];k=mp.mpf('.01')

def cumulants(m):
    out=[mp.mpf(0)]*len(m)
    for n in range(1,len(m)):
        out[n]=m[n]-sum(math.comb(n-1,j-1)*out[j]*m[n-j] for j in range(1,n))
    return out

cs=cumulants([mp.mpf(j%2==0) for j in range(17)])
target=[mp.mpf(a+b)/mp.mpf(2)**321*cs[2*r] for r,(a,b) in enumerate(old['standardized_cumulant_ratios'],1)]
polys=[[],[0,1]]
for n in range(1,16):
    p=polys[-1];d=[(j+1)*p[j+1] for j in range(len(p)-1)];nxt=[0]*(len(d)+2)
    for j,a in enumerate(d):nxt[j]+=a;nxt[j+2]-=a
    polys.append(nxt)

def ev(p,x):
    out=mp.mpf(0)
    for c in reversed(p):out=out*x+c
    return out

def jet(x,k):
    K=[mp.mpf(0)]+[sum(nu[j]*x[j]**n*ev(polys[n],k*x[j]) for j in range(9))+(x[9] if n==1 else 0) for n in range(1,17)]
    m=[mp.mpf(1)]
    for n in range(1,17):m.append(sum(math.comb(n-1,j-1)*K[j]*m[n-j] for j in range(1,n+1)))
    kk=cumulants([a if j%2==0 else mp.mpf(0) for j,a in enumerate(m)])
    return [kk[2*r] for r in range(1,9)]

def replace(values):
    xx=x[:]
    for i,v in zip(active,values):xx[i]=v
    return xx

J=mp.matrix([[mp.diff(lambda z:jet(x[:j]+[z]+x[j+1:],k)[r],x[j]) for j in active] for r in range(7)])
last=mp.matrix([[mp.diff(lambda z:jet(x[:j]+[z]+x[j+1:],k)[7],x[j]) for j in active]])
err=jet(x,k)[7]-target[7]
print('initial residual16',mp.nstr(err,35),flush=True)
for control in ['k',3,4,6]:
    def changed(z):return jet(x,z) if control=='k' else jet(x[:control]+[z]+x[control+1:],k)
    at=k if control=='k' else x[control]
    dc=mp.matrix([mp.diff(lambda z:changed(z)[r],at) for r in range(8)])
    derivative=dc[7]-(last*mp.lu_solve(J,dc[:7,:]))[0]
    print('CONTROL',control,'slope',mp.nstr(derivative,25),'predstep',mp.nstr(-err/derivative,25),flush=True)

if '--solve' in sys.argv:
    for control in ['k',3,4,6]:
        initial=[x[j] for j in active]+[k if control=='k' else x[control]]
        def f(*vals):
            xx=replace(vals[:7]);kk=k
            if control=='k':kk=vals[7]
            else:xx[control]=vals[7]
            val=jet(xx,kk)
            return tuple((val[r]-target[r])/abs(target[r]) for r in range(8))
        try:
            answer=mp.findroot(f,tuple(initial),tol=mp.mpf('1e-40'),maxsteps=30)
            print('ROOT',control,[mp.nstr(t,40) for t in answer],flush=True)
        except Exception as ex:print('FAILED',control,str(ex)[:120],flush=True)

if '--minnorm' in sys.argv:
    current=x[:]
    def residual(v):return mp.matrix([(a-b)/abs(b) for a,b in zip(jet(v,k),target)])
    records=[]
    for iteration in range(60):
        f=residual(current);norm=mp.norm(f)
        print('MINNORM',iteration,mp.nstr(norm,12),mp.nstr(jet(current,k)[7]-target[7],15),flush=True)
        records.append({'iteration':iteration,'residual_norm':mp.nstr(norm,30),'parameters':[mp.nstr(v,50) for v in current]})
        if norm<mp.mpf('1e-38'):break
        columns=[mp.diff(lambda z:residual(current[:j]+[z]+current[j+1:]),current[j]) for j in range(10)]
        Jac=mp.matrix([[columns[j][i] for j in range(10)] for i in range(8)])
        try:step=Jac.T*mp.lu_solve(Jac*Jac.T,f)
        except ZeroDivisionError:break
        alpha=mp.mpf(1)
        while alpha>mp.mpf('1e-16'):
            trial=[current[j]-alpha*step[j] for j in range(10)]
            if min(trial)>0 and max(trial)<10 and mp.norm(residual(trial))<norm*(1-alpha/10):break
            alpha/=2
        if alpha<=mp.mpf('1e-16'):break
        current=trial
    Path(__file__).with_name('star-minnorm-scout.json').write_text(json.dumps({'status':'non-directed-scout-not-certificate','k':'.01','steps':records},indent=2)+'\n')
