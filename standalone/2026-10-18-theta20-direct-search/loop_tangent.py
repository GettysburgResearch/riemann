"""Exploratory 54-edge tangent LP; NOT a finite path or a feasibility certificate."""
import mpmath as mp,numpy as np,itertools,json,math
from scipy.optimize import linprog
from pathlib import Path
mp.mp.dps=65;D=20;ROOT=Path(__file__).parent
z=list(map(mp.mpf,'''0.02343569648142543775120088775367609426491086234504899054044219316999640308767490261513
0.1070957167276771702552325357241092630223472697946054142104949823566403437102016776379
0.2446673577219747520373727287597583778978710203617998359270402925773390596236905383194
0.2919416967601924064292186393474014608467676022902386921193713791523545179719715276204
0.3476034895366412120080621227987830711384723099858026598048380971781530320875987393973
0.5674166374210215080912954316596138872372453325840509702055376082266196163577391039834
0.2897846583828664467716133091359697924204361912670292640917491873556436863517496177915
0.285106960506357706089081531203097991605528412720188898221269899
0.21811514164552528184246309503065283598611525249195627842878797072607479900766357846
0.2844037863870823099088343478652428282944372775369968850115851336
0.2327486353683527055846102198792843860059290118843680888009609953
0.02825402729825051218911783093665512304102681680929219109613482945
0.5915373150873377549476007244677940805783641636233705680049972343
0.6032168772890429065370141679337670387786816624294401533290302553
0.5036039081386797480508431260269859758308374974424268429940971176
0.6053654566123613692908052088457471014261216262097624406546304461
0.5130183625044329556484716517837961157125151081248916400903395168
0.8675370755772718104785334726352241574197343933372702385826209840567181316024514528019'''.split()))
# Correct verbatim source probability at index13.
z[13]=mp.mpf('0.6032168772890429065370141679337670387786816624294401533290302553')
MULT=[256,10,1,1,1,1,1,1,1,1,1];K=[mp.mpf('.01')]*11;K[6]=K[7]=3
active=[0,1,2,3,4,5,6,8,17];old=frozenset((7,9));q0=mp.mpf('.0001')
facts=[mp.factorial(k) for k in range(D+1)]
def mul(a,b):return [mp.fsum(a[j]*b[k-j] for j in range(k+1)) for k in range(D+1)]
def inv(a):
 b=[1/a[0]]+[mp.mpf(0)]*D
 for k in range(1,D+1):b[k]=-mp.fsum(a[j]*b[k-j] for j in range(1,k+1))/a[0]
 return b
def log(a):
 b=[mp.mpf(0)]*(D+1)
 for k in range(1,D+1):b[k]=a[k]-mp.fsum(j*b[j]*a[k-j] for j in range(1,k))/k
 return b
def exp(a):
 b=[mp.mpf(1)]+[mp.mpf(0)]*D
 for k in range(1,D+1):b[k]=mp.fsum(j*a[j]*b[k-j] for j in range(1,k+1))/k
 return b
def even(a):return [x if not(k%2) else x*0 for k,x in enumerate(a)]
def setup(z):
 gs=[];rat=[];l=[mp.mpf(0)]*(D+1)
 for i in range(11):
  a=z[i];p=mp.mpf(1) if i<5 else z[17] if i==5 else z[12+i-6];b=z[11]*K[i]*a
  g=[mp.mpf(1)]+[p*a**k*(b if k%2 else 1)/facts[k] for k in range(1,D+1)]
  h=[b]+[p*a**k*(1 if k%2 else b)/facts[k] for k in range(1,D+1)]
  rat.append(mul(h,inv(g)));lg=log(g);l=[x+MULT[i]*y for x,y in zip(l,lg)]
 return exp(l),rat

def model(z,edges=()):
 base,rat=setup(z);cache={frozenset():base}
 def C(S):
  if S not in cache:
   out=base
   for i in S:out=mul(out,rat[i])
   cache[S]=out
  return cache[S]
 es=[(old,q0)]+[(frozenset(e),q) for e,q in edges]
 total=[mp.mpf(0)]*(D+1)
 for mask in range(1<<len(es)):
  s=frozenset();weight=mp.mpf(1)
  for j,(e,q) in enumerate(es):
   if(mask>>j)&1:s=s^e;weight*=q
  c=C(s);total=[x+weight*y for x,y in zip(total,c)]
 norm=total[0];M=even([x/norm for x in total]);return log(M)[2::2]

if __name__=='__main__':
 eps=mp.mpf('1e-35');J=[]
 for i in active:
  zz=z[:];zz[i]+=1j*eps;J.append([mp.im(v)/eps for v in model(zz)])
 J=mp.matrix([[J[j][i] for j in range(9)] for i in range(10)])
 A=J[:9,:];R=A**-1
 rows=[];tans=[];gam=[];pairs=[]
 for e in itertools.combinations(range(11),2):
  if frozenset(e)==old:continue
  der=mp.matrix([mp.im(v)/eps for v in model(z,[(e,mp.j*eps)])]);t=-R*der[:9]
  g=(der[9]+(J[9,:]*t)[0])*facts[20]
  pairs.append(e);gam.append(float(g));tans.append(list(map(float,t)))
 T=np.array(tans).T;gam=np.array(gam)
 print('negative responses',[(e,float(g)) for e,g in zip(pairs,gam) if g<-.01],flush=True)
 # Keep the linearized active change within 20% of weights/probability margins.
 limit=np.array([float(z[i]*.2) if i<12 else float(min(z[i]-.5,1-z[i])*.2) for i in active])
 out=linprog(gam,A_ub=np.r_[T,-T],b_ub=np.r_[limit,limit],bounds=[(0,.05)]*len(pairs),method='highs')
 print(out.message,'linear top change',out.fun)
 selection=[(e,float(x)) for e,x in zip(pairs,out.x) if x>1e-8]
 print(selection,flush=True)
 json.dump({'status':'exploratory tangent LP; not a finite continuation proof','base':[str(x) for x in z],'pairs':pairs,'gammas':gam.tolist(),'tangents':T.tolist(),'q':out.x.tolist(),'linear_change':float(out.fun),'active':active},open(ROOT/'loop_lp_recomputed.json','w'),indent=2)
