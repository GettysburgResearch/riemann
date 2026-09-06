#!/usr/bin/env python3
"""Reviewer B independent bounded reconstructions. No upstream producer imported.
Run: python checks.py --output checks.normal.json (also python -O).
SymPy is a declared trusted exact-algebra dependency, not a proof assistant.
All acceptance checks use explicit exceptions, never Python assert.
"""
import argparse, hashlib, json, math, platform
from fractions import Fraction
from pathlib import Path
import sympy as s

T,x,y,t=s.symbols('T x y t')
records=[]
def require(ok, message):
    if not bool(ok): raise RuntimeError(message)
def record(name, data): records.append({'id':name,'status':'PASS','data':data})
def eq(a,b): return s.cancel(s.expand(a-b)) == 0

# 1: literal principal Euler restoration, with all nonsquarefree cases retained.
for p in (3,5,7):
    for n in range(1,201):
        b=lambda m:s.mobius(m) if m%p else 0
        c=b(n)-(b(n//p) if n%p==0 else 0)
        require(c==s.mobius(n),'Euler restoration')
record('BCHK01',{'kind':'finite arithmetic','primes':[3,5,7],'n':[1,200]})

# 2: formal Witt factorization, independently by log coefficients.
gamma={n:sum(s.mobius(d)*s.Rational(1,2)**(n//d) for d in s.divisors(n))/n for n in range(1,13)}
for n in gamma: require(sum(d*gamma[d] for d in s.divisors(n))==s.Rational(1,2)**n,'Witt inversion')
record('BCHK02',{'gamma':[str(gamma[n]) for n in range(1,13)],'formal_degree':12})

# 3: exact F5 squarefree/evaluation-character control, no source histogram imported.
def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def rem(a,b,q):
    a=trim(a);b=trim(b)
    while a!=[0] and len(a)>=len(b):
        u=a[-1]*pow(b[-1],-1,q)%q;d=len(a)-len(b)
        for j,v in enumerate(b):a[d+j]=(a[d+j]-u*v)%q
        a=trim(a)
    return a
def gcd(a,b,q):
    a,b=trim(a),trim(b)
    while b!=[0]:a,b=b,rem(a,b,q)
    return a
def ev(a,z,q):
    v=0
    for c in a[::-1]:v=(v*z+c)%q
    return v
def chi(v,q):return 0 if v%q==0 else (1 if pow(v%q,(q-1)//2,q)==1 else -1)
import itertools
q=5; totals=[0]*5; family=[]
for coeff in itertools.product(range(q), repeat=5):
    a=list(coeff)+[1];der=[j*a[j]%q for j in range(1,6)]
    if len(gcd(a,der,q))!=1:continue
    family.append(a);u=1
    for j in range(5):u*=chi(ev(a,j,q),q);totals[j]+=u
tr=[]
for m in range(1,6):
    vals=[math.prod((a-z)%q for a in range(m))%q for z in range(q)]
    tr.append(-sum(chi(v,q) for v in vals)-(m%2==0))
expected=[0,2*q-3,3*(q-2)*tr[2],q*q-10+(4*q-10)*tr[3],(q*q-15)*tr[4]]
require(len(family)==2500 and totals==expected,'F5 multilinear squarefree identity')
record('BCHK03',{'candidate_count':3125,'squarefree_count':2500,'sums':totals,'auxiliary_traces':tr})

# 4: direct AGL orbit census over F3, including the nonfree strata.
q=3; polys=[]
for co in itertools.product(range(q),repeat=5):
    a=list(co)+[1]
    if len(gcd(a,[j*a[j]%q for j in range(1,6)],q))==1:polys.append(tuple(a))
def action(a,alpha,beta):
    out=[0]*6;sc=pow(pow(alpha,5,q),-1,q)
    for j,aj in enumerate(a):
        for k in range(j+1):out[k]=(out[k]+sc*aj*math.comb(j,k)*alpha**k*beta**(j-k))%q
    return tuple(out)
unseen=set(polys);orbits=[]
while unseen:
    a=min(unseen); orb={action(a,alpha,beta) for alpha in (1,2) for beta in range(q)}
    require(orb<=set(polys),'AGL source preservation'); unseen-=orb;orbits.append(orb)
mass=sum(Fraction(len(o),6) for o in orbits)
require(len(orbits)==29 and mass==27,'AGL counts/mass')
record('BCHK04',{'q':3,'models':len(polys),'orbits':len(orbits),'groupoid_mass':str(mass)})

# 5: two kernel conventions and the genuinely indefinite background.
nodes=[s.Integer(1),s.Integer(2)];u=s.Matrix([1/z for z in nodes]);B=s.ones(2)
for r in (1,2,3):
    require((B-r*u*u.T).det()==-s.Rational(r,4),'Loewner central sign')
    require((B+r*u*u.T).det()==s.Rational(r,4),'sum central sign')
nodes=[1,2,4]
L=s.Matrix([[1+a*a+a*b+b*b for b in nodes] for a in nodes])
H=s.Matrix([[1+a*a-a*b+b*b for b in nodes] for a in nodes])
require(L.det()==-36 and H.det()==36,'indefinite deflated backgrounds')
record('BCHK05',{'deflated_determinants':[-36,36],'central_signs':'opposite'})

# 6: polynomial factor locus, not isogeny or irreducibility.
q,a,b,r,v=s.symbols('q a b r v')
require(eq((1-r*T+q*T*T)*(1-v*T+q*T*T),1-(r+v)*T+(r*v+2*q)*T*T-q*(r+v)*T**3+q*q*T**4),'split expansion')
require(eq((1-5*T*T)**2,1-10*T*T+25*T**4),'non +q factor control')
record('BCHK06',{'factor_control':'(q,a,b)=(5,0,-10)','discriminant':80})

# 7: full six-weight plethysm and coefficient-curve identity.
w=[(3,0),(2,1),(1,2),(0,3)]
from collections import Counter
lhs=Counter((u[0]+v[0],u[1]+v[1]) for u,v in itertools.combinations(w,2))
rhs=Counter([(3,3)]+[(5-j,1+j) for j in range(5)])
require(lhs==rhs,'plethysm weights')
F3=-x**4+x*x*y+x*x+y**3-2*y*y
F4=lambda a,b:b*b+a*b-a*a-a**3
require(eq(F4(y-1,x*x-y),-F3),'plethysm curve')
record('BCHK07',{'weight_multiplicities':{str(k):v for k,v in sorted(lhs.items())}})

# 8: actual published noncommuting Gaussian-rational averaging control.
I=s.I; Ds=[s.Matrix([[2,1],[1,2]]),s.Matrix([[3,I],[-I,2]]),s.diag(1,4)]
Ls=[s.zeros(2),s.Matrix([[s.Rational(1,2),I/2],[0,0]]),s.Matrix([[0,0],[s.Rational(1,2),s.Rational(1,2)]])]
ws=[s.Rational(1,6),s.Rational(2,6),s.Rational(3,6)]
barD=sum((w*D for w,D in zip(ws,Ds)),s.zeros(2));barL=barD.inv()*sum((w*D*L for w,D,L in zip(ws,Ds,Ls)),s.zeros(2))
defect=sum((w*L.conjugate().T*D*L for w,D,L in zip(ws,Ds,Ls)),s.zeros(2))-barL.conjugate().T*barD*barL
variance=sum((w*(L-barL).conjugate().T*D*(L-barL) for w,D,L in zip(ws,Ds,Ls)),s.zeros(2))
require(s.simplify(defect-variance)==s.zeros(2),'Schur variance')
require(s.simplify(defect.det())==s.Rational(77,2316),'published variance determinant')
require(s.simplify(defect[0,0])>0,'strict averaging defect')
record('BCHK08',{'determinant':'77/2316','noncommuting':True})

# 9: quotient/tensor and source versus observation.
H1=s.Matrix([[4,1+2*I],[1-2*I,4]]); H2=s.Matrix([[4,1],[1,3]])
p1=s.Matrix([[1,I]]);p2=s.Matrix([[1,1-I]])
quot=lambda H,p:(p*H.inv()*p.conjugate().T).inv()
require(s.simplify(quot(s.kronecker_product(H1,H2),s.kronecker_product(p1,p2))-s.kronecker_product(quot(H1,p1),quot(H2,p2)))==s.zeros(1),'tensor quotient')
L=lambda alpha:s.Rational(alpha,2)/(x*(x-alpha))
require(eq(L(3)-L(1)*L(2),(3*x**3-9*x*x+5*x+3)/(2*x*x*(x-1)*(x-2)*(x-3))),'Mellin product firewall')
record('BCHK09',{'tensor_quotient':'exact','observations_multiply':False})

# 10: rational margins of the all-depth weight96 proof. Analytic premises separate.
require(13000<4**94 and 2**95>95000,'integer bases')
require(s.Rational(95**2,1)/(s.Rational(191,2)*s.Rational(88,7))>s.Rational(137,50)**2,'Gamma ratio margin')
eupper=s.Rational(163,60)+s.Rational(7,4320)
require(eupper<s.Rational(273,100)<s.Rational(2736261,1000000),'central criterion margin')
record('BCHK10',{'e_upper':str(eupper),'R_lower':'2736261/1000000','scope':'rational inequalities only'})

# 11: Chow/ambient Euler polynomials, not measured syzygy ranks.
P=1+20*T+48*T*T+20*T**3+T**4; N=s.expand((1-T)**3*P)
require(N==1+17*T-9*T*T-65*T**3+65*T**4+9*T**5-17*T**6-T**7,'Chow numerator')
K=s.expand((1-T)**20*P)
require([K.coeff(T,n) for n in range(7)]==[1,0,-162,1720,-9234,30456,-61370],'ambient Euler')
series=sum(s.binomial(n+2,2)**3*T**n for n in range(12))
require(all(s.expand((1-T)**10*series).coeff(T,n)==N.coeff(T,n) for n in range(12)),'source Hilbert sequence')
record('BCHK11',{'Chow_numerator':str(N),'ambient_first_coefficients':[1,0,-162,1720,-9234,30456,-61370]})

# 12: nondegenerate input alphabets, exceptional backward coefficient.
HA=lambda z:1/((1-2*z)*(1-3*z)*(1-5*z))
D=(1-4*T*T)*(1-9*T*T)*(1-25*T*T)
num=s.cancel(D*(HA(T)+HA(-T))/2)
require(num==1+31*T*T and s.degree(num,T)==2 and s.degree(D,T)==6,'multilinear counterexample')
record('BCHK12',{'A':[2,3,5],'B':[1,-1],'C':[1],'numerator':str(num),'generic_prediction_degree':3,'actual_degree':2})

# 13: a=0,m=6 disproves an unqualified persistence iff.
N6=s.cancel((1+T)**4*(1-T)**3/(1-T*T))
require(eq(N6,(1+T)*T*T*((T+1/T)**2-4)),'torsion gap')
require(s.discriminant(x*x-4,x)==16,'nonzero torsion discriminant')
record('BCHK13',{'a':0,'m':6,'R':2,'threshold':5,'spectrum_polynomial':'z^2-4','discriminant':16})

# 14: contraction sign, in the convention dh+hd=1-ip.
# Ordered basis [x,b,a,y], degrees [1,1,0,0].
d=s.zeros(4); d[2,1]=1; h=s.zeros(4);h[1,2]=1
pert=s.zeros(4);pert[2,0]=1;pert[3,1]=1
inc=s.Matrix([[1,0],[0,0],[0,0],[0,1]]);proj=inc.T
require(d*h+h*d==s.eye(4)-inc*proj,'contraction convention')
require((d+pert)**2==s.zeros(4),'perturbed differential')
plus=proj*pert*(s.eye(4)-h*pert).inv()*inc
minus=proj*pert*(s.eye(4)+h*pert).inv()*inc
inew=(s.eye(4)+h*pert).inv()*inc
require((d+pert)*inew==inew*minus and plus==-minus and minus[1,0]==-1,'signed transfer')
record('BCHK14',{'printed_arity2':1,'correct_arity2':-1,'convention':'dh+hd=1-ip'})

# 15: literal Delta3 zero but page3 differential nonzero (zigzag correction).
# x,y degree1 with filtration3,2; a,b degree0 with filtration1,0.
d1=s.zeros(4);d1[2,1]=1;d2=s.zeros(4);d2[2,0]=1;d2[3,1]=1
require((d1+d2)**2==s.zeros(4),'filtered complex')
require((d1+d2)*s.Matrix([1,-1,0,0])==s.Matrix([0,0,0,-1]),'page3 zigzag')
record('BCHK15',{'Delta3':0,'d3_on_x':'-b','correction':'x-y','claim':'components alone do not determine higher pages'})

# 16: complete support census and degree-six dimensions.
B={(0,0):1,(0,1):17,(0,2):11,(1,2):20,(1,3):65,(2,4):65,(2,5):20,(3,5):11,(3,6):17,(3,7):1}
slots={r:[(q,j,q+r-1,j+r) for q,j in sorted(B) if (q+r-1,j+r) in B] for r in range(1,6)}
require([len(slots[r]) for r in range(1,6)]==[6,6,4,2,0],'transfer slots')
dims={n:sum(math.comb(17,6-j)*v for (q,j),v in B.items() if 0<=6-j<=17 and q+6-j==n) for n in (6,5,4,3)}
require(list(dims.values())==[12376,152796,79407,357],'degree six groups')
require(sum((-1)**n*v for n,v in dims.items())==-61370,'degree-six Euler')
record('BCHK16',{'slots':{str(k):v for k,v in slots.items()},'degree6_dimensions':dims,'master_module_dimension':1000})

# 17: renewal coefficients via recurrence and formal exponential, independent routes.
S=lambda n:sum(s.Rational(1,d) for d in s.divisors(n))
yr={};gs={}
for n in range(1,7):
    gs[n]=s.expand(S(n)-sum(S(n-j)*yr[j] for j in range(1,n)));yr[n]=24*t*gs[n]/n
phi=sum(S(n)*T**n/n for n in range(1,7))
e=[s.Integer(1)]
# Exponential coefficients from n e_n = sum k f_k e_(n-k).
for n in range(1,7):e.append(s.expand(sum(-24*t*S(k)*e[n-k] for k in range(1,n+1))/n))
for n in gs:require(eq(gs[n],-n*e[n]/(24*t)),'renewal independent route')
expected=[1,s.Rational(3,2)-24*t,s.Rational(4,3)-54*t+288*t*t,s.Rational(7,4)-s.Rational(209,3)*t+864*t*t-2304*t**3,s.Rational(6,5)-s.Rational(185,2)*t+1450*t*t-8640*t**3+13824*t**4]
require(all(eq(gs[n],expected[n-1]) for n in range(1,6)),'published renewal coefficients')
require(gs[2].subs(t,s.Rational(1,16))==0,'first resonance')
record('BCHK17',{'g':[str(gs[n]) for n in range(1,7)],'first_resonance':'1/16','native_limit_certified':False})

# 18: orientation of Gamma source-energy ratios (Gamma cancels exactly).
J=10;k=100; r=2;v=1
ratio=s.Rational(J-v,J-r)**(k-1)
require(ratio>1,'DR7 orientation counterexample')
record('BCHK18',{'J':J,'k':k,'r':r,'s':v,'A_Jr_over_A_Js':str(ratio),'claimed_decay_possible':False})

# 19: native path incompatibility and sharp threshold attainment.
eps=(s.sqrt(10)-3)/2; cutoff=s.Rational(1,2)+eps
AA=1-cutoff; BB=(1-cutoff**2)/2;CC=AA
require(eq(eps*eps+3*eps,s.Rational(1,4)),'Reynolds sharp distance')
require(eq(BB,s.Rational(1,4)+eps) and eq(CC-AA*AA,2*BB-AA),'threshold attainment')
require(s.Rational(1,2)-s.Rational(1,2)**2>s.Rational(2,4)-s.Rational(1,2),'Reynolds violation')
record('BCHK19',{'forbidden_mean':['1/2','1/4','1/2'],'gap':'1/4','distance':'(sqrt(10)-3)/2'})

# 20: original-Gram tail inference, conditional on supplied certified bounds.
PH=s.Rational(2480322,10**12)
require(1+s.Rational(7,10)+s.Rational(7,10)**2/2+s.Rational(7,10)**3/6>2,'log2 rational upper proof')
require(128*s.Rational(9,2)*s.Rational(7,10)-288<116,'nu0 upper')
require(20*116*PH**2<s.Rational(1,48000000),'conditional Gram tail inequality')
record('BCHK20',{'PH_upper':str(PH),'nu0_upper':116,'conditional_lower_Gram':'1/48000000','upstream_Gram_rerun':False})

# 21: twisted convolution checked in the cyclic group algebra Z[z]/(z^5-1).
z=s.symbols('z');m=5;aa=[1,-2,3,0,2];bb=[2,1,-1,4,-3]
cc=[sum(aa[i]*bb[j] for i in range(m) for j in range(m) if (i+2*j)%m==n) for n in range(m)]
for hval in range(m):
    f=sum(cc[n]*z**(hval*n) for n in range(m))
    p=sum(aa[n]*z**(hval*n) for n in range(m))*sum(bb[n]*z**(2*hval*n) for n in range(m))
    require(s.rem(f-p,z**m-1,z)==0,'twisted convolution')
record('BCHK21',{'group_order':m,'convolution':cc,'conjugation':'negative Fourier indices equivalent'})

# 22: uniform-source principal obstruction / declared native history control.
vec=[3,3]+[-1]*8;norm=sum(a*a for a in vec);total=sum(vec)
require(Fraction(total*total,10*norm)==Fraction(1,65),'mean energy ratio')
require(total**4-norm**2==-660,'bilateral Wick control')
for m in (3,5,7):
    H=s.eye(m)-s.ones(m)/m
    require(H*s.ones(m,1)==s.zeros(m,1),'principal annihilation')
record('BCHK22',{'history_norm':norm,'history_sum':total,'mean_fraction':'1/65','bilateral_value_over_d':-660})

# 23: exact GP(23,2) upper threshold, corrected to a rational BELOW sqrt8.
n=23; A=s.zeros(2*n)
for j in range(n):
    for a,b in [(j,(j+1)%n),(n+j,n+(j+2)%n),(j,n+j)]:A[a,b]=A[b,a]=1
p=A.charpoly().as_poly();cut=s.Rational(7071,2500)
require(cut**2<8 and p.count_roots(cut,4)==1,'GP23 exact corrected bound')
P=x**3-2*x+7;Q=2*(x+2)*(x-1);HH=s.expand(P*P-2*Q*Q)
require(s.Poly(P,x).count_roots(-2,2)==0 and s.Poly(HH,x).count_roots(-2,1)==0,'GP negative-end Sturm')
require(s.Rational(5657,2000)**2>8,'old cutoff lies above target')
record('BCHK23',{'n':23,'charpoly_coefficients':[int(v) for v in p.all_coeffs()],'new_cutoff':str(cut),'eigenvalues_above_cutoff':1,'old_cutoff_sufficient':False})

# 24: density spike obstruction, all-order algebra plus three exact controls.
# rho/(1152/(pi^3*t^(3/2))) >=16/(pi*sqrt(epsilon)).
for m in (1,3,5):
    epsilon=s.Rational(1,m**6)
    require(16/s.sqrt(epsilon)/(s.Rational(22,7))==s.Rational(56,11)*m**3,'threshold spike')
record('BCHK24',{'sequence':'t_m=16*m^2+m^-6, odd m','ratio_lower_bound':'(56/11)*m^3','pointwise_asymptotic':False})

# 25: positive entire polynomial on positive reals, negative Toeplitz minor.
require(s.det(s.Matrix([[1,1],[2,1]]))==-1,'coefficient positivity countercontrol')
record('BCHK25',{'X':'1+u+2u^2','Toeplitz_minor':-1,'spectral_positivity_implies_coefficient_TP':False})

# 26: energy completion, not Hilbert-space inversion; finite approximants above limit.
for N in (1,2,4,8):
    energy=sum(s.Rational(1,4)**j for j in range(1,N+1))
    require(energy==(1-s.Rational(1,4)**N)/3 and energy<s.Rational(1,3),'energy completion')
record('BCHK26',{'a_j':'4^-j','b_j':'4^-j','energy_Riesz_norm2':'1/3','Hilbert_representative':'(1,1,...) not ell2','Galerkin_S_direction':'decreasing from above','unbounded_control_b_j':'2^-j'})

# 27: loss of outwardness by unpadded decimal shortening, exact rational example.
upper=Fraction(10**25+4,10**25); shortened=Fraction(1,1)
require(shortened<upper,'decimal shortening counterexample')
record('BCHK27',{'exact_upper':str(upper),'25_digit_shortening':'1.000000000000000000000000','is_upper_bound':False,'actual_Epstein_winding_rerun':False})

# 28: L-108524's defined associated polynomial is reversed relative to slopes.
lam,w,ss=s.symbols('lam w ss')
F=w*w-3*ss*w-8*ss*ss
associated=1-3*lam-8*lam*lam
slopes=lam*lam-3*lam-8
require(eq(F.subs(w,ss*lam),ss*ss*slopes),'diagonal blow-up slope polynomial')
require(eq(lam*lam*associated.subs(lam,1/lam),slopes),'reversed associated polynomial')
require(s.discriminant(associated,lam)==41 and s.discriminant(slopes,lam)==41,'separability survives reversal')
record('BCHK28',{'defined_associated':'1-3*lambda-8*lambda^2','actual_slope_polynomial':'lambda^2-3*lambda-8','multiplicity_argument_repairable':True})

payload={'schema':'reviewer-B-independent-checks-v1','scope':'28 named bounded reconstructions; no upstream full-suite or interval walk replay','records':records}
encoded=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
result={'payload':payload,'payload_sha256':hashlib.sha256(encoded).hexdigest(),'environment':{'python':platform.python_version(),'sympy':s.__version__},'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print('PASS_REVIEWER_B: '+str(len(records))+' named checks; payload '+result['payload_sha256'])
