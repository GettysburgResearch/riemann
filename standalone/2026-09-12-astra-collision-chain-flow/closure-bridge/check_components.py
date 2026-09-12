"""Bounded exact algebra checks. These do not prove the unbounded RH premise."""
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial, isqrt
import hashlib, json

def need(test,message):
    if not test:raise ArithmeticError(message)

def mu(n):
    sign=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;sign=-sign
            if n%p==0:return 0
            while n%p==0:n//=p
        p+=1
    return -sign if n>1 else sign

def arithmetic():
    cuts=[];m=Q(0)
    for y in range(1,32):
        old=m;m+=Q(mu(y),y)
        if y>=2 and mu(y) and old*m<=0:cuts.append((y,m))
    checks=0
    for y,my in cuts:
        B=(y+1)**2-1;c={n:Q(mu(n)) for n in range(1,y+1) if mu(n)}
        if my:c[2*y]=-2*y*my
        z={}
        for r,a in c.items():
            for s,b in c.items():z[r*s]=z.get(r*s,Q(0))+a*b
        w=[Q(0)]*(B+1)
        for d,a in z.items():
            for n in range(d,B+1,d):w[n]+=a
        m=Q(0);ann=Q(0);Qk=Q(0);gram=Q(0)
        for n in range(1,B+1):
            need(2*c.get(n,Q(0))-w[n]==mu(n),'exact native Newton prefix')
            m+=Q(mu(n),n);Qk+=w[n]/n
            if n>y:ann+=m*m;gram+=Qk*Qk
            checks+=1
        P=sum((Q((2*y-n)*mu(n),n) for n in range(y+1,2*y)),Q(0))
        need(ann==gram+4*my*P,'exact collar identity')
        need(abs(4*my*P)<=Q(2*(y-1),y),'whole collar bound')
    return {'crossing_cuts':[y for y,m in cuts],'native_prefix_checks':checks}

def cmul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cpow(a,n):
    if n<0:return cpow((a[0],-a[1]),-n)
    out=(Q(1),Q(0))
    for _ in range(n):out=cmul(out,a)
    return out

def graph_checks():
    total=0
    for n,edges,weights in ((3,[(0,1),(1,2)],[1,2,3]),
                            (4,[(0,1),(0,2),(0,3)],[2,1,3,1]),
                            (4,[(0,1),(1,2),(2,3),(0,3)],[1,3,2,1])):
        ws=[Q(2+j,2) for j in range(len(edges))]
        Z=Q(0);v=Q(0);ch=[Q(0),Q(0)]
        for spins in product((-1,1),repeat=n):
            wt=Q(1)
            for (i,j),w in zip(edges,ws):
                if spins[i]==spins[j]:wt*=w
            x=sum(a*s for a,s in zip(weights,spins));Z+=wt;v+=wt*x*x
            p=cpow((Q(3,5),Q(4,5)),x)
            for k in range(2):ch[k]+=wt*p[k]
        Zb=Q(0);vb=Q(0);cb=[Q(0),Q(0)]
        for bits in product((0,1),repeat=len(edges)):
            groups=[{i} for i in range(n)];wt=Q(1)
            for chosen,(i,j),w in zip(bits,edges,ws):
                if not chosen:continue
                wt*=w-1
                a=next(g for g in groups if i in g);b=next(g for g in groups if j in g)
                if a is not b:a.update(b);groups.remove(b)
            wt*=2**len(groups);Zb+=wt
            cluster=[sum(weights[i] for i in g) for g in groups]
            vb+=wt*sum(a*a for a in cluster)
            prodcos=Q(1)
            for a in cluster:prodcos*=cpow((Q(3,5),Q(4,5)),a)[0]
            cb[0]+=wt*prodcos
            total+=1
        need(Zb==Z and vb==v and cb==ch,'complete FK expansion vs spin enumeration')
        need(v/Z>=sum(a*a for a in weights),'nonnegative correlation variance')
    return {'bond_panels':total,'graphs':3}

def series_and_constants():
    # A positive quadratic majorizes the only difficult branch of tripling.
    a=Q(5581,3840);need(Q(13,4)**2-8*a<0,'positive tripling quadratic')
    def low_exp(x,N=100):return sum((x**j/Q(factorial(j)) for j in range(N+1)),Q(0))
    def high_exp(x,N=100):
        need(x<N+2,'exponential remainder ratio')
        return low_exp(x,N)+x**(N+1)/factorial(N+1)/(1-x/Q(N+2))
    need(low_exp(Q(9,8))>3,'tripling large-argument branch')
    need(low_exp(Q(7,5))>4,'log four bound')
    need(Q(26)+Q(8,3)*Q(7,5)+Q(8,9)<31,'whole inverse-fourth zero sum')
    need(high_exp(Q(135,16))<5000,'native interaction bound')
    need(2*Q(58,10**14)/(225*5009)>Q(1,10**18),'native positive correlation floor')
    need(low_exp(Q(11,5))>Q(792,91),'native N5 support bound')
    for j in range(2,13):
        R=2**j;m=(2*j+4)*R*R
        jetexp=(4*j+4)*R*R
        tailexp=2*(m+1)-3*R*R-1
        minexp=(4*j+1)*R*R
        need(jetexp>minexp+1 and tailexp>minexp+1,'joint diagonal budget')
    need(2*(16384+1)-3840-1==28929,'finite N5 obstruction tail')
    need(21762>21760+1 and 28929>21760+1,'finite N5 obstruction margin')
    return {'dyadic_schedules':11,'finite_N5_obstruction_order':32768}

def check():
    return {'arithmetic':arithmetic(),'ferromagnetic':graph_checks(),
            'bridge':series_and_constants(),'rh_proved':False}

if __name__=='__main__':
    out=json.dumps(check(),sort_keys=True,indent=2)+'\n'
    print(out,end='');print('sha256 '+hashlib.sha256(out.encode()).hexdigest())
