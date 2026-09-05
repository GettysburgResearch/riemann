"""Independent bounded controls for the omitted-review supplement.
Exact Fraction/dyadic arithmetic; not a Lean build or proof of imported analysis.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json,sys,hashlib
from dyadic_interval import I,S,ceildiv

def need(p,msg):
    if not p:raise RuntimeError(msg)

def exp_endpoint(n):
    if n<0:return 1/exp_endpoint(-n)
    k=max(0,n.bit_length()-128)
    while n > S*(1<<k):k+=1
    z=I(Q(n,S*(1<<k)));v=I(1);t=I(1)
    for j in range(1,49):
        t=t*z/j;v+=t
    e=ceildiv(3*S,factorial(49))
    v=I.raw(v.lo,v.hi+e)
    for _ in range(k):v=v*v
    return v

def exp(x):
    x=I(x);return I.raw(exp_endpoint(x.lo).lo,exp_endpoint(x.hi).hi)

def enc(x):return [str(Q(x.lo,S)),str(Q(x.hi,S))]
def interval_contains(x,q):return x.lo*Q(1,S)<=q<=x.hi*Q(1,S)

def poly_mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def weighted_integral(poly):
    e=exp(2);J=[(e-1)/2]
    for n in range(1,len(poly)):J.append((e-n*J[-1])/2)
    return sum((a*b for a,b in zip(poly,J)),I(0))

def main():
    groups={};checks=0
    for a in range(-7,8):
        for b in range(1,8):
            q=Q(a,b);need(interval_contains(I(q),q),'parse enclosure');checks+=1
            for r in [Q(-7,11),Q(2,9),Q(5,4)]:
                need(interval_contains(I(q)+I(r),q+r),'addition');checks+=1
                need(interval_contains(I(q)*I(r),q*r),'multiplication');checks+=1
                need(interval_contains(I(q)/I(r),q/r),'division');checks+=1
    groups['rational_interval_operations']=checks
    for q in [Q(0),Q(1,9),Q(2),Q(49,64)]:
        z=I(q).sqrt();need(Q(z.lo,S)**2<=q<=Q(z.hi,S)**2,'sqrt');checks+=1
    need(I(0).sin().lo<=0<=I(0).sin().hi,'sin zero')
    need(I(0).cos().lo<=S<=I(0).cos().hi,'cos zero')
    need(I.pi()>Q(314159265358979323846,10**20),'pi lower')
    need(I.pi()<Q(314159265358979323847,10**20),'pi upper');checks+=4
    need(exp(0).lo<=S<=exp(0).hi,'exp zero');checks+=1
    groups['elementary_series_and_square_roots']=9
    u=1/I(2).sqrt();H=I(Q(3,2))-u*u.cos()/u.sin()
    h269=(1345000*H-2680)/1340003
    c280=2*I(Q(726237,700000)).sqrt()-1+Q(2603,700000)
    h280=(H-Q(279,140000))/(1-c280/280)
    for z,l,h in [(H,Q(67250070367941164573,10**20),Q(67250070367941164574,10**20)),
                  (h269,Q(67300852792777976132,10**20),Q(67300852792777976133,10**20)),
                  (h280,Q(6730096522791369,10**16),Q(6730096522791371,10**16))]:
        need(z>l and z<h,'record enclosure');checks+=1
    need(h280>h269 and h269>Q(673,1000),'record comparison');checks+=1
    groups['record_constants']={'checks':4,'H0':enc(H),'269':enc(h269),'280':enc(h280),'c280':enc(c280)}
    q=[Q(1)]
    for _ in range(5):q=poly_mul(q,[Q(1),Q(-2)])
    q=poly_mul(q,[Q(1),Q(-1)])
    qp=[(j+1)*q[j+1] for j in range(len(q)-1)]
    phi=weighted_integral(poly_mul(q,q));psi=weighted_integral(poly_mul(qp,qp))
    a2=(psi-1-phi)/(4*phi);need(a2>0,'positive Conrey A2')
    a=a2.sqrt();ea=exp(2*a);F=2*phi*a*(ea+1)/(ea-1)+Q(1,2)
    need(F<exp(Q(1,50)),'Conrey fifth fallback');checks+=2
    groups['Conrey_fifth_functional']={'checks':2,'Phi':enc(phi),'Psi':enc(psi),'A_squared':enc(a2),'F5':enc(F),'exp_1_50':enc(exp(Q(1,50))),'analytic_Conrey_theorem_reproved':False}
    B2=Q('-11.2745354467343289715797194361');B3=Q('-2.11516352829808095816974122805')
    combo=5*B2+3*B3;need(combo<Q('-62.7181678185658877324'),'568 fixed supplied endpoints')
    for x in range(-20,21):
        for y in range(-3,4):need(5*(2*x-1-y)+(5*y-x-1-3*x*x)==-3*(x-1)*(x-2),'568 identity')
    need(all(not(L%2==0 and (-1)**(L-1)>0) for L in range(1,33)),'568 parity')
    checks+=289;groups['568_regression']={'checks':289,'combined_supplied_upper':str(combo),'primitive_endpoints_reproduced':False}
    for p in [3,5,7,11,13]:
        for a in range(p):
            f=[Q(-1) if t==a else Q(1,p-1) for t in range(p)]
            need(sum(f)==0,'local mean');need(sum(x*x for x in f)/p==Q(1,p-1),'local variance');checks+=2
            for b in range(p):
                if b==a:continue
                g=[Q(-1) if t==b else Q(1,p-1) for t in range(p)]
                need(sum(x*y for x,y in zip(f,g))/p==Q(-1,(p-1)**2),'local covariance');checks+=1
    groups['LongGaps_local_covariance']={'primes':[3,5,7,11,13],'scope':'finite identity only; not full long-gap proof'}
    rho=Q(1,20);need(2*rho-(2*rho-rho*rho/2)==Q(1,800),'Catalan leading coefficient');checks+=1
    groups['Catalan_tax']={'coefficient':'1/800','original_paper_attribution_reverified':False}
    # Strict convexity/KKT fixture: the first coordinate saturates its cap.
    us=[Q(4),Q(1)];vs=[Q(1),Q(2)];R=Q(2);lam=Q(1)
    eps=[min(Q(1),u/(lam*v)) for u,v in zip(us,vs)]
    need(eps==[Q(1),Q(1,2)] and sum(v*e for v,e in zip(vs,eps))==R,'water filling')
    need(us[0]/vs[0]>=lam and us[1]/(vs[1]*eps[1])==lam,'KKT');checks+=2
    groups['Cartan_water_filling']={'eps':['1','1/2'],'closed_budget':'2','strict_budget_minimum_claimed':False}
    result={'status':'PASS_SUPPLEMENT_FINITE_CONTROLS','checks':checks,'groups':groups,'rh_proved':False,'seven_point_exhaustion_in_this_script':False,'full_Lean_build':False}
    out=Path(sys.argv[1]);out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(result['status'],checks)
if __name__=='__main__':main()
