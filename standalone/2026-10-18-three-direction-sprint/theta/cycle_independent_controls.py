"""Independent full-hub enumeration and integer raw-EGF cycle checks.

The complete model uses scaled integer raw moments, avoiding the model's
conditional cumulant recurrence and its rational quotient implementation.
The miniature graph includes the hub as an explicitly enumerated spin.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb,lcm
import argparse,hashlib,importlib.util,itertools,json,sys,time
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'inherited'))
import pr886_primitive as b
import model as tree
spec=importlib.util.spec_from_file_location('independently_loaded_cyclic',ROOT.parent/'reviews/cyclic_model.py');cm=importlib.util.module_from_spec(spec);spec.loader.exec_module(cm)

def require(ok,message):
    if not ok:raise ValueError(message)

def miniature(z,counts,types,ends,eta,degree=12):
    weights=[F(0)];dw=[{}];components=[];edges=[]
    for i,count in enumerate(counts):
        A,B,p=z[3*i:3*i+3]
        for copy in range(count):
            root=len(weights)
            if i==0:
                weights.append(A);dw.append({0:F(1)});components.append((i,root,None))
            else:
                weights.extend([(A+B)/2,(A-B)/2]);dw.extend([{3*i:F(1,2),3*i+1:F(1,2)},{3*i:F(1,2),3*i+1:F(-1,2)}]);components.append((i,root,root+1));edges.append((root,root+1,2*p-1,{3*i+2:F(2)}))
            edges.append((0,root,eta,{}))
    left=next(c for c in components if c[0]==types[0]);right=next(c for c in components if c[0]==types[1] and c is not left)
    endpoint=[left[1 if ends[0]=='root' else 2],right[1 if ends[1]=='root' else 2]]
    edges.append((*endpoint,z[-1],{len(z)-1:F(1)}));active=[j for j in range(len(z)) if j not in(1,2)];vertices=len(weights)
    raw=[F(0)]*(degree+1);derivative=[[F(0)]*len(active) for _ in raw]
    for spins in itertools.product((-1,1),repeat=vertices):
        prob=F(1,2**vertices);factors=[1+q*spins[a]*spins[c] for a,c,q,d in edges]
        for factor in factors:prob*=factor
        value=sum(w*s for w,s in zip(weights,spins));dvalue={k:sum(v.get(k,0)*s for v,s in zip(dw,spins)) for k in active}
        dprob={k:sum((prob*d.get(k,0)*spins[a]*spins[c]/factor for (a,c,q,d),factor in zip(edges,factors)),F(0)) for k in active}
        for n in range(degree+1):
            raw[n]+=prob*value**n
            for j,k in enumerate(active):derivative[n][j]+=dprob[k]*value**n+(n*prob*value**(n-1)*dvalue[k] if n else 0)
    Z=raw[0];dz=derivative[0];dnormal=[[(v*Z-raw[n]*dd)/(Z*Z) for v,dd in zip(row,dz)] for n,row in enumerate(derivative)];normal=[v/Z for v in raw]
    zz=[cm.Dual(v,[F(j==k) for k in active]) for j,v in enumerate(z)];_,got=cm.evaluate(zz,counts,eta,degree,types,ends)
    require([v.v for v in got]==normal,'explicit full-hub spin enumeration versus cyclic raw moments')
    require([list(v.d) for v in got]==dnormal,'explicit normalized graph derivatives versus cyclic AD')
    return {'types':list(types),'ends':list(ends),'vertices':vertices,'configurations':2**vertices,'degree':degree,'derivative_coordinates':len(active),'exact_normalizer':str(Z)}

def iconvolve(a,da,c,dc):
    n=min(len(a),len(c))-1
    return [sum(comb(k,j)*a[j]*c[k-j] for j in range(k+1)) for k in range(n+1)],da*dc

def ipower(a,da,count):
    out=[1]+[0]*(len(a)-1);den=1
    while count:
        if count%2:out,den=iconvolve(out,den,a,da)
        count//=2
        if count:a,da=iconvolve(a,da,a,da)
    return out,den

def full_integer_assembly(p):
    z=list(map(F,p['centers']));counts=p['counts'];eta=F(p['hub_correlation']);degree=p['degree'];types=tuple(p['cross_types']);ends=tuple(p['cross_vertices']);Q=2*lcm(*(v.denominator for v in z+[eta]));ints=[int(v*Q) for v in z];H=int(eta*Q)
    out=[1]+[0]*degree;den=1
    for i,count in enumerate(counts):
        count-=types.count(i);A,B,P=ints[3*i:3*i+3]
        if i==0:
            base=[A**n*(Q if n%2==0 else H) for n in range(degree+1)];db=Q
        else:
            base=[(P*A**n+(Q-P)*B**n)*(Q if n%2==0 else H) for n in range(degree+1)];db=Q*Q
        require(base[0]==db and count>=0,'complete exact independent block count')
        power,dp=ipower(base,db,count);out,den=iconvolve(out,den,power,dp)
    weights=[];edges=[];chosen=[]
    for i in types:
        A,B,P=ints[3*i:3*i+3];root=len(weights)
        if i==0:weights.append(A);chosen.append((root,None))
        else:
            # Q contains an extra factor2, so physical half-weights are integers.
            require((A+B)%2==0 and (A-B)%2==0,'common exact physical weight scale')
            weights.extend([(A+B)//2,(A-B)//2]);chosen.append((root,root+1));edges.append((root,root+1,2*P-Q))
        edges.append((None,root,H))
    endpoints=[chosen[j][0 if ends[j]=='root' else 1] for j in range(2)];edges.append((*endpoints,ints[-1]));pair=[0]*(degree+1)
    for spins in itertools.product((-1,1),repeat=len(weights)):
        mass=1
        for a,c,q in edges:mass*=Q+q*(1 if a is None else spins[a])*spins[c]
        value=sum(w*s for w,s in zip(weights,spins))
        for n in range(degree+1):pair[n]+=mass*value**n
    require(pair[0]>0,'exact selected-cluster normalizer positive')
    out,den=iconvolve(out,den,pair,pair[0]);raw=cm.evaluate([b.I.coerce(v) for v in z],counts,eta,degree,types,ends)[1]
    for n in range(degree+1):
        if n%2:require(raw[n].lo==0 and raw[n].hi==0,'exact global odd symmetrization');continue
        D=den*Q**n
        require(raw[n].lo*D<=out[n]*b.SCALE<=raw[n].hi*D,'complete integer raw EGF value contained in directed cyclic interval')
    return {'degree':degree,'vertices':counts[0]+2*sum(counts[1:])+1,'integer_scale_decimal_digits':len(str(Q)),'exact_even_orders_compared':degree//2+1,'assembly':'scaled integer conditional raw EGF, explicit selected-cluster enumeration, no cumulant recurrence'}

def main(parameters,emit):
    start=time.time();fixtures=[]
    z=[F(3,7),F(0),F(1),F(7,9),F(-1,5),F(4,5),F(5,8),F(1,8),F(3,5),F(2,7)]
    for ends in itertools.product(('root','child'),repeat=2):fixtures.append(miniature(z,[1,1,1],(1,2),ends,F(1,11)))
    fixtures.append(miniature(z,[1,1,1],(0,1),('root','child'),F(1,11)))
    fixtures.append(miniature(z[:6]+[z[-1]],[1,2],(1,1),('root','child'),F(1,11)))
    out={'status':'INDEPENDENT_CYCLIC_CONTROLS_PASS','fixtures':fixtures}
    if parameters:
        p=json.loads(parameters.read_text());out['complete_model']=full_integer_assembly(p);out['parameter_sha256']=hashlib.sha256(parameters.read_bytes()).hexdigest()
    out['input_hashes']={'cyclic_model.py':hashlib.sha256(Path(cm.__file__).read_bytes()).hexdigest(),'cycle_independent_controls.py':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'inherited/pr886_primitive.py':hashlib.sha256((ROOT/'inherited/pr886_primitive.py').read_bytes()).hexdigest()}
    txt=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n';emit.write_text(txt)
    print('INDEPENDENT_CYCLIC_CONTROLS_PASS',hashlib.sha256(txt.encode()).hexdigest(),'seconds',time.time()-start,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--parameters',type=Path);p.add_argument('--emit',type=Path,default=ROOT/'cycle_independent_controls.json');a=p.parse_args();main(a.parameters,a.emit)
