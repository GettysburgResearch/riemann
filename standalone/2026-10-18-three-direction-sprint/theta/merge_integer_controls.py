"""Independent scaled-integer full307-vertex raw EGF for the tree merge.

This uses explicit selected-cluster spin enumeration, without the merge
conditional cumulant formula or an AD/cumulant calculation in the reference.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb,lcm
import argparse,hashlib,itertools,json,sys,time
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'inherited'))
import pr886_primitive as b
import merge_model as mm

def require(ok,message):
    if not ok:raise ValueError(message)

def conv(a,da,c,dc):
    n=min(len(a),len(c))-1
    return [sum(comb(k,j)*a[j]*c[k-j] for j in range(k+1)) for k in range(n+1)],da*dc

def power(a,da,count):
    out=[1]+[0]*(len(a)-1);den=1
    while count:
        if count%2:out,den=conv(out,den,a,da)
        count//=2
        if count:a,da=conv(a,da,a,da)
    return out,den

def check(parameters,emit):
    began=time.monotonic();p=json.loads(parameters.read_text());z=list(map(F,p['centers']));counts=p['counts'];eta=F(p['hub_correlation']);degree=p['degree'];types=tuple(p['merge_types']);ends=tuple(p['merge_ends'])
    Q=2*lcm(*(v.denominator for v in z+[eta]));ints=[int(v*Q) for v in z];H=int(eta*Q);out=[1]+[0]*degree;den=1
    for i,count in enumerate(counts):
        count-=types.count(i);A,B,P=ints[3*i:3*i+3]
        if i==0:base=[A**n*(Q if n%2==0 else H) for n in range(degree+1)];db=Q
        else:base=[(P*A**n+(Q-P)*B**n)*(Q if n%2==0 else H) for n in range(degree+1)];db=Q*Q
        require(base[0]==db and count>=0,'complete exact independent-block count')
        block,dp=power(base,db,count);out,den=conv(out,den,block,dp)
    weights=[];edges=[];chosen=[]
    for copy,i in enumerate(types):
        A,B,P=ints[3*i:3*i+3];root=len(weights)
        if i==0:weights.append(A);chosen.append((root,None))
        else:
            require((A+B)%2==0 and (A-B)%2==0,'complete exact physical weight scale')
            weights.extend([(A+B)//2,(A-B)//2]);chosen.append((root,root+1));edges.append((root,root+1,2*P-Q))
        if copy==0:edges.append((None,root,H))
    endpoints=[chosen[j][ends[j]] for j in range(2)];require(None not in endpoints,'existing selected endpoints');edges.append((*endpoints,ints[-1]));pair=[0]*(degree+1)
    for spins in itertools.product((-1,1),repeat=len(weights)):
        mass=1
        for a,c,q in edges:mass*=Q+q*(1 if a is None else spins[a])*spins[c]
        value=sum(w*s for w,s in zip(weights,spins))
        for n in range(degree+1):pair[n]+=mass*value**n
    require(pair[0]==2**len(weights)*Q**len(edges),'exact selected tree-cluster normalization')
    out,den=conv(out,den,pair,pair[0]);raw=mm.evaluate([b.I.coerce(v) for v in z],counts,types,ends,eta,degree)[1]
    for n in range(degree+1):
        if n%2:require(raw[n].lo==raw[n].hi==0,'exact odd symmetrization');continue
        D=den*Q**n
        require(raw[n].lo*D<=out[n]*b.SCALE<=raw[n].hi*D,'complete raw integer EGF contained in directed merged-model interval')
    result={'status':'MERGE_INTEGER_CONTROLS_PASS','degree':degree,'vertices':counts[0]+2*sum(counts[1:])+1,'exact_even_orders':degree//2+1,'selected_cluster_configurations':2**len(weights),'conditional_normalizer':'1','parameter_sha256':hashlib.sha256(parameters.read_bytes()).hexdigest(),'input_hashes':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ['merge_integer_controls.py','merge_model.py','model.py','inherited/pr886_primitive.py']}}
    txt=json.dumps(result,sort_keys=True,separators=(',',':'))+'\n';emit.write_text(txt)
    print('MERGE_INTEGER_CONTROLS_PASS',hashlib.sha256(txt.encode()).hexdigest(),'seconds',time.monotonic()-began,flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--parameters',type=Path,default=ROOT/'parameters26_merge.json');ap.add_argument('--emit',type=Path,default=ROOT/'merge_integer_controls26.json');a=ap.parse_args();check(a.parameters,a.emit)
