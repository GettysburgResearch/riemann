"""Independent exact-dyadic primitive replay of ainta seven-point pressure.
The branch/subdivision design is credited to ainta/zeta-simple-zeros at
040c5e899e658aed7b56a2a87f501798fe10761d; primitive arithmetic is independent.
No special-function library, numpy or floating eigensolver is used.
"""
from dyadic_interval import I,S
from fractions import Fraction as Q
from math import nextafter,inf
from itertools import product
from functools import lru_cache
import json,time,hashlib,struct,sys
from pathlib import Path
G=4000;CUT=45600;SIZE=CUT+8

def down(x):return nextafter(float(x),-inf)
def ratio(n,d):return 0. if n==0 else down(Q(n,d))
def mul(a,b):return 0. if a==0 or b==0 else max(0.,nextafter(a*b,-inf))
def add(a,b):return 0. if a==b==0 else max(0.,nextafter(a+b,-inf))
CS=[0,ratio(1,3),ratio(2,5),ratio(1,2),ratio(2,3),1.,2.]
CU=[0,nextafter(float(Q(1,3)),inf),nextafter(float(Q(2,5)),inf),.5,nextafter(float(Q(2,3)),inf),1.,2.]
CQ=[0,Q(1,3),Q(2,5),Q(1,2),Q(2,3),Q(1),Q(2)]
PI=I.pi();SQ=I(2).sqrt();INV=1/SQ;K0=SQ*INV.sin()

def kernel(x):return (((SQ-2*PI*x)/2).sinc()+((SQ+2*PI*x)/2).sinc())/(2*K0)
def derivatives(x):
    def one(z):
        si,co=z.sincos();z2=z*z
        return si/z,(z*co-si)/z2,((2-z2)*si-2*z*co)/(z2*z)
    l=one(PI*x-INV);r=one(PI*x+INV)
    a=(l[0]+r[0])/2;b=PI*(l[1]+r[1])/2;c=PI*PI*(l[2]+r[2])/2
    return a*a/(K0*K0),2*a*b/(K0*K0),2*(b*b+a*c)/(K0*K0)
@lru_cache(maxsize=None)
def point_derivatives(numerator):
    return derivatives(I(Q(numerator, 2*G)))

class RM:
    def __init__(self,v):
        self.rows=[v];w=1
        while 2*w<=len(v):
            p=self.rows[-1];self.rows.append([min(p[i],p[i+w]) for i in range(len(v)-2*w+1)]);w*=2
        self.n=len(v)
    def get(self,l,r,fallback):
        if r>=self.n:return fallback
        if l<0 or r<l:raise ValueError('range')
        n=(r-l+1).bit_length()-1;return min(self.rows[n][l],self.rows[n][r-(1<<n)+1])
def pd(terms):
    # Check a strict exact-rational Hessian floor with outward dyadic LDL.
    a=[[I(0) for _ in range(6)] for _ in range(6)]
    for j,s,c in terms:
        c=I(Q(c))
        for i in range(j,j+s):
            for k in range(j,j+s):a[i][k]+=c
    for j in range(6):
        if not a[j][j]>0:return False
        for i in range(j+1,6):
            for k in range(i,6):
                a[k][i]-=a[k][j]*a[i][j]/a[j][j];a[i][k]=a[k][i]
    return True

def run(out):
    start=time.monotonic();vals=[];secs=[]
    for i in range(SIZE):
        x=I(Q(2*i+1,2*G),Q(1,2*G));k=kernel(x)
        lo=max(0.,down(k.abs_lower()));vals.append(mul(lo,lo))
        secs.append(-inf if i<3800 else down(derivatives(x)[2].lower()))
    rm=RM(vals);sm=RM(secs);target=nextafter(float(Q(19,5000)),inf)
    components=[]
    for i,v in enumerate(vals[:CUT]):
        if add(ratio(i,G*3000),mul(CS[1],v))<target:
            if components and i==components[-1][1]+1:components[-1]=(components[-1][0],i)
            else:components.append((i,i))
    stack=list(product(components,repeat=6));initial=len(stack);counts=dict(nodes=0,pressure=0,interval=0,tangent=0,splits=0)
    digest=hashlib.sha256()
    print('table built',time.monotonic()-start,'components',components,'initial',initial,flush=True)
    while stack:
        box=stack.pop();counts['nodes']+=1
        lows=[a for a,b in box];highs=[b for a,b in box]
        if sum(lows)>=CUT:kind='pressure'
        else:
            val=ratio(sum(lows),G*3000);ranges=[]
            for span in range(1,7):
                for j in range(7-span):
                    l=sum(lows[j:j+span]);r=sum(highs[j:j+span])+span-1
                    ranges.append((j,span,l,r));val=add(val,mul(CS[span],rm.get(l,r,0.)))
            if val>=target:kind='interval'
            else:
                terms=[];heur=[[0.]*6 for _ in range(6)];possible=True
                for j,span,l,r in ranges:
                    q=sm.get(l,r,-inf)
                    if q==-inf:possible=False;break
                    c=nextafter(q*(CS[span] if q>=0 else CU[span]),-inf);terms.append((j,span,c))
                    for i in range(j,j+span):
                        for k in range(j,j+span):heur[i][k]+=c
                if possible:
                    for j in range(6):
                        pivot=heur[j][j]
                        if pivot<=1e-12:possible=False;break
                        for i in range(j+1,6):
                            for k in range(i,6):
                                heur[k][i]-=heur[k][j]*heur[i][j]/pivot;heur[i][k]=heur[k][i]
                if possible:possible=pd(terms)
                if possible:
                    mid=[Q(a+b+1,2*G) for a,b in box];rad=[Q(b-a+1,2*G) for a,b in box]
                    v=I(sum(mid)/3000);grad=[I(Q(1,3000)) for _ in range(6)]
                    for j,span,l,r in ranges:
                        w,d,_=point_derivatives(sum(a+b+1 for a,b in box[j:j+span]));v+=CQ[span]*w
                        for k in range(j,j+span):grad[k]+=CQ[span]*d
                    for d,r in zip(grad,rad):v-=d.abs_upper()*r
                    possible=v>=I(Q(19,5000))
                if possible:kind='tangent'
                else:
                    widths=[b-a for a,b in box];j=max(range(6),key=widths.__getitem__)
                    if widths[j]==0:raise RuntimeError(('UNCLOSED_CELL',box,val))
                    a,b=box[j];m=(a+b)//2;left=list(box);right=list(box);left[j]=(a,m);right[j]=(m+1,b)
                    stack.append(tuple(left));stack.append(tuple(right));kind='splits'
        counts[kind]+=1;digest.update(repr((kind,box)).encode())
        if counts['nodes']%10000==0:print(counts,'pending',len(stack),flush=True)
    result={'verdict':'PASS_INDEPENDENT_DYADIC_SEVEN_POINT','target':'19/5000','grid':G,'dyadic_bits':128,'components':components,'counts':counts,'initial_boxes':initial,'kernel_table_sha256':hashlib.sha256(b''.join(struct.pack('>d',v) for v in vals)).hexdigest(),'second_table_sha256':hashlib.sha256(b''.join(struct.pack('>d',v) for v in secs)).hexdigest(),'traversal_sha256':digest.hexdigest(),'seconds':time.monotonic()-start,'zeta_bound_proved_by_this_code':False}
    Path(out).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':run(sys.argv[1])
