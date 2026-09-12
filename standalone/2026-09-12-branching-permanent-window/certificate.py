"""Whole-source polynomial enclosure and infinite-depth window certificate.
No gamma/zeta/zero oracle, root finder or binary64 number is used in acceptance.
"""
from fractions import Fraction as Q
from math import comb,factorial
from pathlib import Path
import hashlib,json,argparse,time
from intervals import I,C,S,BITS,ceildiv,exp_i,pi_i

GRID=32768
H=Q(2,GRID)
DEGREE=120                 # degree in -z^2/1024
SCALE=32
CUTOFFS=(Q(2),Q(1),Q(1,2))
HEIGHT=30
DEPTH=32
RATE=Q(31,80)
B=[Q(60),Q(366),Q(3135),Q(71463,2),Q(2044911,4)]

def source_polynomial():
    """Positive discrete Simpson moments, before alternating in z.
    phi terms 1,2,3 on their COMPLETE prescribed grids; later terms are paid.
    """
    derivative_bounds()
    pi=pi_i();a=exp_i(2*H);b=exp_i(H/2)
    e2=I.of(1);eh=I.of(1)
    cuts=[int(u/H) for u in CUTOFFS]
    if any(Q(k)*H!=u or k%2 for k,u in zip(cuts,CUTOFFS)):raise ValueError('grid coverage')
    q=[pi*n*n for n in (1,2,3)]
    lo=[0]*(DEGREE+1);hi=[0]*(DEGREE+1)
    evaluations=0
    for j in range(GRID+1):
        w=I.of(0)
        for k,qn in zip(cuts,q):
            if j>k:continue
            x=qn*e2
            phi=eh*(4*x*x-6*x)*exp_i(-x)
            wt=1 if j in (0,k) else (4 if j%2 else 2)
            w+=wt*phi
            evaluations+=1
        w=w*(2*H/3)
        if w.lo<0:raise ValueError('positive theta summand guard')
        tl=th=S
        j2=j*j
        for d in range(DEGREE+1):
            lo[d]+=w.lo*tl;hi[d]+=w.hi*th
            if d<DEGREE:
                den=(1<<18)*(2*d+1)*(2*d+2)
                tl=tl*j2//den;th=ceildiv(th*j2,den)
        e2=e2*a;eh=eh*b
    c=[I(x//S,ceildiv(y,S)) for x,y in zip(lo,hi)]
    if not 0<c[0].lo<c[0].hi<S:raise ValueError('total mass ceiling')
    return c,evaluations

def derivative_bounds():
    """Independent primitive recurrence; do not trust a copied moment table."""
    p={1:Q(-6),2:Q(4)}; out=[]
    for r in range(5):
        out.append(6*sum((abs(v)*factorial(j-1) for j,v in p.items()),Q()))
        nxt={}
        for j,v in p.items():
            nxt[j]=nxt.get(j,Q())+(2*j+Q(1,2))*v
            nxt[j+1]=nxt.get(j+1,Q())-2*v
        p={j:v for j,v in nxt.items() if v}
    if out!=B:raise ValueError('theta derivative primitive mismatch')
    return out

def bounds(c):
    derivative_bounds()
    # The three omitted time tails start at q exp(2U)>72.
    if not min(3*Q(8,3)**4,12*Q(8,3)**2,27*Q(8,3))>=72:raise ValueError('time tail exponent')
    time_tail=12*(72**2+2*72+2)*Q(3,8)**72
    # Every omitted theta index n>=4. q0=16*pi>48; parent gamma bound
    # 8 q^2 exp(-q)/(q-3/2) < 9q exp(-q) <= 432 (3/8)^48.
    index_tail=432*Q(3,8)**48
    if not index_tail+time_tail<Q(1,10**15):raise ValueError('complete theta tails')
    # Both signed and complex Simpson remainders are paid via an L1 Peano bound.
    L=3*sum((comb(4,r)*B[r]*31**(4-r) for r in range(5)),Q())
    simpson=H**4*L/36
    cos_tail=Q(64)**(2*DEGREE+2)/factorial(2*DEGREE+2)/(1-Q(64**2,(2*DEGREE+3)*(2*DEGREE+4)))
    # Derivative-4 discrepancy between cosine and its finite Taylor polynomial.
    tail4=16*Q(64)**(2*DEGREE-2)/factorial(2*DEGREE-2)/(1-Q(64**2,(2*DEGREE-1)*(2*DEGREE)))
    fourth=3*24*c[2].abs_upper()/SCALE**4+tail4
    if not fourth<1:raise ValueError('complete polynomial fourth derivative bound')
    model=simpson+index_tail+time_tail+cos_tail
    orbital=Q(6,175)*(2*31**3+3)*RATE**DEPTH
    return {'simpson':simpson,'time_tail':time_tail,'index_tail':index_tail,
            'cosine_tail':cos_tail,'model_error':model,'orbit_error':orbital,
            'fourth_derivative_bound':Q(1)}

def jets(c,z):
    # Automatic exact Taylor shift for polynomial in x=-z^2/1024, through jet 3.
    z=C.of(z);x=[-z*z/(SCALE*SCALE),-2*z/(SCALE*SCALE),C(Q(-1,SCALE*SCALE))]
    v=[C(c[-1]),C(),C(),C()]
    for a in reversed(c[:-1]):
        v=[sum((v[j-i]*x[i] for i in range(min(2,j)+1)),C())+(C(a) if j==0 else C()) for j in range(4)]
    return v

def value(c,z):
    x=-z*z/(SCALE*SCALE);v=C(c[-1])
    for a in reversed(c[:-1]):v=v*x+C(a)
    return v

def delta_interval(d):
    x,y=d
    if x and y:raise ValueError('axis-parallel segment required')
    r=abs(x or y)
    iv=I.of(r);s=I(-iv.hi,iv.hi)
    return C(s,0) if x else C(0,s)

def lower_linf(z):
    def d(i):return i.lo if i.lo>0 else (-i.hi if i.hi<0 else 0)
    return max(d(z.re),d(z.im))

def winding(points):
    n=0
    for a,b in zip(points,points[1:]):
        cross=a[0]*b[1]-a[1]*b[0]
        if a[1]<=0<b[1] and cross>0:n+=1
        if b[1]<=0<a[1] and cross<0:n-=1
    return n

def contour(c,rect,step,err,expected):
    xl,xr,yl,yr=map(Q,rect)
    corners=[(xl,yl),(xr,yl),(xr,yr),(xl,yr),(xl,yl)]
    nodes=[corners[0]]
    for a,b in zip(corners,corners[1:]):
        dist=abs(b[0]-a[0])+abs(b[1]-a[1]);m=ceildiv(dist.numerator*step.denominator,dist.denominator*step.numerator)
        nodes.extend([(a[0]+Q(j,m)*(b[0]-a[0]),a[1]+Q(j,m)*(b[1]-a[1])) for j in range(1,m+1)])
    poly=[];minmargin=None
    for j,(a,b) in enumerate(zip(nodes,nodes[1:])):
        if j==0:poly.append(value(c,C(*a)).midpoint())
        mid=((a[0]+b[0])/2,(a[1]+b[1])/2);half=((b[0]-a[0])/2,(b[1]-a[1])/2)
        v=jets(c,C(*mid));d=delta_interval(half)
        enclosure=((v[3]*d+v[2])*d+v[1])*d+v[0]
        h=abs(half[0])+abs(half[1])
        enclosure=enclosure.inflate(h**4/24+err)
        margin=lower_linf(enclosure)
        if margin<=0:raise ValueError('unprotected contour segment '+str((j,a,b)))
        minmargin=margin if minmargin is None else min(minmargin,margin)
        p=value(c,C(*b)).midpoint()
        # Polygon representatives must be inside the same convex zero-free enclosure.
        for t in (poly[-1],p):
            if not(enclosure.re.lo<=t[0]<=enclosure.re.hi and enclosure.im.lo<=t[1]<=enclosure.im.hi):raise ValueError('polygon/enclosure mismatch')
        poly.append(p)
    if poly[0]!=poly[-1]:raise ValueError('unclosed polygon')
    n=winding(poly)
    if n!=expected:raise ValueError('wrong COMPLETE contour count '+str(n))
    return {'rectangle':[str(x) for x in (xl,xr,yl,yr)],'segments':len(nodes)-1,
            'count':n,'minimum_linf_margin':str(Q(minmargin,S)),
            'polygon_sha256':hashlib.sha256(json.dumps(poly,separators=(',',':')).encode()).hexdigest()}

CENTRES=[Q('14.134725'),Q('21.022040'),Q('25.010858')]

def reconstruct():
    c,evals=source_polynomial();b=bounds(c);err=b['model_error']+b['orbit_error']
    rec=[]
    rec.append(contour(c,[0,HEIGHT,Q(-1,2),Q(1,2)],Q(1,50),err,3))
    for x in CENTRES:
        rec.append(contour(c,[x-Q(1,100),x+Q(1,100),Q(-1,100),Q(1,100)],Q(1,500),err,1))
    slopes=[]
    for x,floor in zip(CENTRES,[Q(1,1000),Q(1,100000),Q(1,1000000)]):
        v=jets(c,C(x));iv=I.of(Q(1,100));delta=I(-iv.hi,iv.hi)
        d=(v[1].re+2*v[2].re*delta+3*v[3].re*delta*delta).inflate(Q(1,100)**3/6+4*b['model_error'])
        margin=d.lo if d.lo>0 else (-d.hi if d.hi<0 else 0)
        if Q(margin,S)<=floor:raise ValueError('root slope certificate')
        if 4*b['orbit_error']>=floor/2:raise ValueError('future derivative margin')
        slopes.append({'centre':str(x),'derivative_interval':d.rec(),'absolute_slope_lower':str(floor),
                       'zero_displacement_coefficient':str(Q(6,175)*(2*31**3+3)/floor)})
    return {'schema':'BPW26-1','rh_proved':False,'cofinal_height_confinement_proved':False,
            'source':'literal Gamma(5/2) shared-uniform branching orbit',
            'all_depths_from':DEPTH,'window_height':HEIGHT,'positive_height_zero_count':3,
            'normalization':'H_n(1/2+i z); same critical-strip zeros as E_n',
            'grid':GRID,'cutoffs':[str(u) for u in CUTOFFS],
            'degree_in_squared_variable':DEGREE,'scale':SCALE,'bits':BITS,
            'theta_node_evaluations':evals,'bounds':{k:str(v) for k,v in b.items()},
            'polynomial_coefficients':[a.rec() for a in c],
            'contours':rec,'root_slopes':slopes}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',type=Path,required=True);args=p.parse_args()
    t=time.monotonic();r=reconstruct();args.write.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('PRODUCED_BPW26',int(time.monotonic()-t))
