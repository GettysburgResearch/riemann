#!/usr/bin/env python3
"""Independent bounded exact controls for Reviewer D pass 3.
No upstream producer is imported. No floating-point acceptance.
Analytic infinite theorems are NOT authenticated by these controls.
"""
import argparse, csv, hashlib, json, math
from fractions import Fraction as F
from pathlib import Path
import sympy as S

RESULTS=[]
def test(name, count, details):
    RESULTS.append({'name':name,'fixtures':count,'details':details})
def require(ok,msg):
    if not ok: raise ValueError(msg)
def eq(a,b,msg): require(S.cancel(a-b)==0,msg)

def factors(n):
    out={};p=2
    while p*p<=n:
        while n%p==0: out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1: out[n]=out.get(n,0)+1
    return out

def mu(n):
    fs=factors(n)
    return 0 if any(e>1 for e in fs.values()) else (-1)**len(fs)
def divs(n): return [d for d in range(1,n+1) if n%d==0]

def q(a=0,b=0): return (F(a),F(b))
def qa(x,y): return (x[0]+y[0],x[1]+y[1])
def qn(x): return (-x[0],-x[1])
def qs(x,y): return qa(x,qn(y))
def qm(x,y): return (x[0]*y[0]+2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def scale(x,r): return (x[0]*r,x[1]*r)
def invsqrt2power(r): return q(F(1,2**(r//2))) if r%2==0 else q(0,F(1,2**((r+1)//2)))
def peval(poly,x):
    out=q()
    for k,c in enumerate(poly):out=qa(out,scale(c,x**k))
    return out

# Rigorous fixed-denominator interval arithmetic, including rational log/sqrt.
BITS=90;DEN=1<<BITS
class I:
    def __init__(self,lo,hi=None):
        lo=F(lo);hi=lo if hi is None else F(hi)
        self.lo=F((lo.numerator*DEN)//lo.denominator,DEN)
        self.hi=F(-((-hi.numerator*DEN)//hi.denominator),DEN)
        require(self.lo<=self.hi,'interval order')
    def __add__(self,o):
        o=o if isinstance(o,I) else I(o)
        return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-o if isinstance(o,I) else self+I(-o)
    def __mul__(self,o):
        o=o if isinstance(o,I) else I(o)
        v=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(min(v),max(v))
    __rmul__=__mul__
    def inv(self):
        require(not self.lo<=0<=self.hi,'division through zero')
        return I(1/self.hi,1/self.lo)
    def dump(self):return [str(self.lo),str(self.hi)]

def sqrt_i(n):
    k=math.isqrt(n*DEN*DEN)
    return I(F(k,DEN), F(k if k*k==n*DEN*DEN else k+1,DEN))

def log_core(r):
    r=F(r);require(F(1)<=r<=2,'log reduced domain')
    z=(r-1)/(r+1);part=F(0);N=48
    for j in range(N):part+=2*z**(2*j+1)/(2*j+1)
    tail=2*z**(2*N+1)/((2*N+1)*(1-z*z))
    return I(part,part+tail)
LOG2=log_core(2)
def log_i(r):
    r=F(r);require(r>0,'positive log argument');k=0
    while r>=2:r/=2;k+=1
    while r<1:r*=2;k-=1
    return log_core(r)+k*LOG2

def log_vector(r):
    r=F(r);out=factors(r.numerator)
    for p,e in factors(r.denominator).items():out[p]=out.get(p,0)-e
    return {p:e for p,e in out.items() if e}
def add_vec(dest,v,c):
    for p,e in v.items():dest[p]=qa(dest.get(p,q()),scale(c,e))
    return {p:a for p,a in dest.items() if a!=q()}
def hinge(Y,n):
    r=F(Y,n)
    return {} if r<=1 else log_vector(min(F(4),r))
def band_mass(l,r,n):
    return {} if F(n)>=r else log_vector(r/max(l,F(n)))

def run():
    # Cardinal differential inverse and multiplicity-controlled values.
    u,z=S.symbols('u z',real=True);omega=S.Rational(1,3)+S.I/4
    # Gaussian Fourier transform, omitting the common sqrt(pi) factor.
    def gauss_transform(expr):
        pol=S.Poly(S.expand(expr/S.exp(-u*u)),u)
        return S.simplify(sum(cc*S.I**(-kk)*S.diff(S.exp(-z*z/4),z,kk)
                              for (kk,),cc in pol.terms()))
    cur=S.exp(-u*u)
    for m in range(1,5):
        cur=S.expand(S.I*S.diff(cur,u)-omega*cur)
        ft=gauss_transform(cur)
        eq(ft,(z-omega)**m*S.exp(-z*z/4),'Gaussian Fourier differential rule')
        eq(ft.subs(z,omega),0,'actual zero enabling resolvent division')
    test('cardinal_zero_division_ode',8,{'orders':[1,2,3,4],
         'checks':'Fourier differential multiplier and exact target zero'})
    for m in range(1,5):
        E=(z-omega)**m*(z-S.conjugate(omega))**m*(z-2)*(z+3)
        L=S.cancel(E/(z-omega)**m);L=L/L.subs(z,omega)
        Ls=S.cancel(E/(z-S.conjugate(omega))**m);Ls=Ls/Ls.subs(z,S.conjugate(omega))
        h=L-Ls
        for node,value in [(omega,1),(S.conjugate(omega),-1),(2,0),(-3,0)]:
            eq(h.subs(z,node),value,'cardinal interpolation')
    test('cardinal_values_with_multiplicity',16,{'target_Weil_value':'-2m; background values exactly zero'})
    K=S.Matrix([[2,1,S.Rational(1,2)],[1,3,S.Rational(1,4)],[S.Rational(1,2),S.Rational(1,4),1]])
    t=S.Matrix([1,-1,0]);M=(t.T*K.inv()*t)[0];Sch=K[:2,:2]-K[:2,2:]*K[2:,:2]
    Z=Sch-S.Matrix([1,-1])*S.Matrix([[1,-1]])/M
    require(Z.det()==0 and Z[0,0]>0 and Z[1,1]>0,'rank-one Schur bound')
    test('cardinal_schur_metric',1,{'cost':str(M),'residual_determinant':str(Z.det())})

    cs={1:F(1),2:-F(15,2),4:F(35,2),8:-F(15),16:F(4)}
    b={n:sum(c*mu(n//d) for d,c in cs.items() if n%d==0) for n in range(1,129)}
    for n in range(2,129):
        H=sum(c for k,c in cs.items() if k<=n)
        ps=sum(sum(c for k,c in cs.items() if k<=j) for j in range(n+1))
        target=H-F(2,n+1)*ps
        actual=F(0)
        for d in range(2,n+1):
            a,r=divmod(n,d);actual+=b[d]*F(a*(d-1-r),n+1)
        require(actual==target,'fourteen row finite carry')
        expected=-F(17,6) if n==2 else -F(1,2) if n==3 else F(101-11*n,n+1) if n<=7 else F(4*(n-31),n+1) if n<=15 else F(0)
        require(actual==expected,'fourteen row closed form')
        require(sum(b[d] for d in divs(n))==cs.get(n,F(0)),'renewal convolution')
    test('fourteen_row_and_divisor_reconstruction',127,{'last_nonzero_row':15,'all_rows_16_to_128_zero':True})
    r=S.sqrt(2);y,tv=S.symbols('y t')
    P=1-15/(2*r)*y+S.Rational(35,4)*y**2-15/(2*r)*y**3+y**4
    eq(P,(1-y/r)*(1-y/(2*r))*(1-r*y)*(1-2*r*y),'phase polynomial')
    kap=(43-30*r)/4;eq(P.subs(y,1),kap,'spectral lower edge')
    eq(S.diff(P,y).subs(y,1),2*kap,'renewal forcing moment')
    require(43**2>30**2*2,'positive edge')
    test('centered_symbol_and_forcing',4,{'lower_edge':'(43-30sqrt(2))/4'})
    require(3**2*2<8**2,'gauge negative at X=1')
    for X in [F(1,2),F(1),F(3,2),F(2),F(3),F(4),F(8),F(16)]:
        # Correct gauge: -3sqrt2 log_+(X/2)+4log_+(X/4).
        g={}
        if X>2:g=add_vec(g,log_vector(X/2),q(0,-3))
        if X>4:g=add_vec(g,log_vector(X/4),q(4))
        if X>=4:
            expanded={};expanded=add_vec(expanded,log_vector(X),q(4,-3));expanded=add_vec(expanded,log_vector(2),q(-8,3))
            require(g==expanded,'large endpoint gauge')
    test('riesz_activation_gauge',9,{'counterexample_X':'1','printed_gauge':'(3sqrt(2)-8)log(2)','true_gauge':'0'})

    for M0 in range(1,9):
        for L in range(0,16):
            require(sum(math.comb(M0+j-1,M0-1) for j in range(L+1))==math.comb(M0+L,M0),'Haar inverse mass')
    test('fixed_filter_inverse_mass',128,{'scope':'fixed M; no varying-order inference'})
    # Coefficients of 1/(1-2w^2) have an interior singularity but alternate zeros.
    coeff=[0 if n%2 else 2**(n//2) for n in range(20)]
    require(coeff[1]==0 and coeff[18]==512,'radius is not a per-index lower bound')
    test('filter_radius_not_pointwise_growth',1,{'odd_coefficients_zero':True})

    for n in range(2,301):
        fs=factors(n);v=fs.get(2,0);gn=4**(v//2);lhs={p:gn*e for p,e in fs.items()};rhs={}
        for d in divs(n):
            fd=factors(d)
            if len(fd)!=1:continue
            p,k=next(iter(fd.items()))
            c=1 if p!=2 or k%2 else 2**(k+1)-1
            val=c*4**(factors(n//d).get(2,0)//2)
            rhs[p]=rhs.get(p,0)+val
        require(lhs==rhs,'generalized-prime compiler')
    test('scale_four_positive_compiler',299,{'checked_n':'2..300','comparison':'formal prime-log coefficients'})

    # Goldbach/cosine formulas are identities for any real increment packet.
    for n in range(2,31):
        inc=[0]+[((7*j)%11)-5 for j in range(1,n+1)]
        B=[sum(inc[1:j+1]) for j in range(n+1)];c=3;C=B[n]-c
        energy=sum((C-B[j]-B[n-j])**2 for j in range(1,n))
        R1=sum((n-m)*inc[m] for m in range(1,n))
        Rmax=sum((n-max(a,b))*inc[a]*inc[b] for a in range(1,n) for b in range(1,n))
        Rp=sum((n+1-a-b)*inc[a]*inc[b] for a in range(1,n) for b in range(1,n) if a+b<=n)
        require(energy==(n-1)*C*C-4*C*R1+2*Rmax+2*Rp,'Goldbach expansion')
        require(n*C-2*sum(B[:n])==sum((2*m-n)*inc[m] for m in range(1,n+1))-n*c,'zero mode')
    test('goldbach_and_zero_mode',29,{'n':'2..30','arbitrary_signed_inputs':True})

    # Reconstruct both annular polynomials on every band from source W,A,B,Q.
    Av=[1,1,-8,-8,16,16];Bv=[0,-1,-8,0,32,16];Qv=[F(1),-F(7,8),F(7,32),-F(1,64)]
    lo=[0,5,-63,170];hi=[0,-F(1,3),1,-F(2,3)]
    polys=[]
    for j in range(10):
        mid=F(3,2**(j+2));pair=[]
        for vec in [Av,Bv]:
            pol=[q() for _ in range(4)]
            for rr in range(6):
                for sh in range(4):
                    v=mid*2**(rr+sh)
                    w=lo if v<=F(1,4) else hi if v<=1 else [0]*4
                    coef=scale(invsqrt2power(rr),vec[rr]*Qv[sh])
                    for power in range(4):pol[power]=qa(pol[power],scale(coef,w[power]*2**((rr+sh)*power)))
            pair.append(pol)
        polys.append(pair)
    expected=[
    [[(-F(1,3),0),(1,0),(-F(2,3),0)],[(0,0),(0,0),(0,0)]],
    [[(F(1,4),-F(1,3)),(-F(5,2),2),(4,-F(8,3))],[(0,F(1,3)),(0,-2),(0,F(8,3))]],
    [[(F(85,8),F(1,4)),(-127,-5),(336,16)],[(F(16,3),-F(1,4)),(-64,5),(F(512,3),-16)]],
    [[(-8,F(85,8)),(320,-254),(-2048,1344)],[(-4,-F(127,24)),(160,126),(-1024,-F(1984,3))]],
    [[(-F(316,3),-8),(4992,640),(-F(155648,3),-8192)],[(-F(382,3),4),(6080,-320),(-F(192512,3),4096)]],
    [[(80,-F(316,3)),(-12800,9984),(327680,-F(622592,3))],[(96,-22),(-15360,2176),(393216,-49152)]],
    [[(328,80),(-60416,-25600),(2359296,1310720)],[(F(2000,3),16),(-124928,-5120),(F(15204352,3),262144)]],
    [[(-256,328),(163840,-120832),(-16777216,9437184)],[(-512,F(1016,3)),(327680,-129024),(-33554432,F(32505856,3))]],
    [[(F(128,3),-256),(-65536,327680),(F(67108864,3),-67108864)],[(F(256,3),-256),(-131072,327680),(F(134217728,3),-67108864)]],
    [[(0,F(128,3)),(0,-131072),(0,F(268435456,3))],[(0,F(128,3)),(0,-131072),(0,F(268435456,3))]]]
    for j in range(10):
        for ch in range(2):
            require(polys[j][ch][0]==q(),'constant term zero')
            for k in range(1,4):require(polys[j][ch][k]==q(*expected[j][ch][k-1]),'source certificate coefficient')
    test('annular_certificate_all_coefficients',60,{'bands':10,'channels':2,'coefficient_field':'Q(sqrt(2))','source_blob':'c0d12f07d1aa224bc986c280df0a823eede5047d'})
    for ch in range(2):
        require(peval(polys[0][ch],F(1))==q(),'upper endpoint')
        require(peval(polys[9][ch],F(1,1024))==q(),'lower endpoint')
        for j in range(1,10):require(peval(polys[j-1][ch],F(1,2**j))==peval(polys[j][ch],F(1,2**j)),'band continuity')
    test('annular_endpoints',22,{'all_knots_continuous':True})
    require(F(251,32)<8 and 8*57<512 and F(135,64)*512==1080,'uniform kernel constants')
    test('annular_uniform_bounds',3,{'base_absolute_bound':'8','K1_bound':'456','filter_mass':'135/64'})
    for s in range(1,7):
        w=sum(F(lo[k],s+k)*F(1,4)**(s+k)+F(hi[k],s+k)*(1-F(1,4)**(s+k)) for k in range(1,4))
        wanted=(1-F(4,1)**(1-s))*F(s-1,3*(s+1)*(s+2)*(s+3))
        require(w==wanted,'Mellin W')
    test('annular_mellin_factor',6,{'integer_mellin_points':'1..6; exact integral'})

    X,H=1024,8;m,n=3,17;d=math.gcd(m,n);a,b=m//d,n//d
    require(F(X,1024)<m<n<=X and n-m>H and d*H<X and a<=H,'core counterexample')
    def real_q_interval(c): return I(c[0])+c[1]*sqrt_i(2)
    numerators=[]
    for atom in [m,n]:
        x=F(atom,X)
        band=next(j for j in range(10) if F(1,2**(j+1))<x<=F(1,2**j))
        J0=real_q_interval(peval(polys[band][0],x))
        J1=real_q_interval(peval(polys[band][1],x))
        num=log_i(atom)*J0+LOG2*J1
        require(num.lo>0 or num.hi<0,'counterexample pair is actually active')
        numerators.append(num.dump())
    test('annular_core_inequivalence',3,{'X':X,'H':H,'m':m,'n':n,'gcd':d,
         'omitted_category':'small reduced variable','actual_G_numerators':numerators})
    count=0
    for X in [32,64,128]:
        for H in [2,4,8]:
            vals=[m for m in range(1,X+1) if m%2 and mu(m)!=0 and 1024*m>X]
            for i,m in enumerate(vals):
                for n in vals[i+1:]:
                    d=math.gcd(m,n);a,b=m//d,n//d
                    cats=[n-m<=H, n-m>H and d*H>=X, n-m>H and d*H<X and a<=H, n-m>H and d*H<X and a>H]
                    require(sum(cats)==1,'disjoint pair ownership')
                    require(mu(m)*mu(n)==mu(a)*mu(b) and math.gcd(a,d)==math.gcd(b,d)==1,'gcd support')
                    count+=1
    test('disjoint_annular_sectors_and_gcd',count,{'X':[32,64,128],'H':[2,4,8]})
    for N in range(2,40):
        direct=sum(F(1,N*abs(j-k)) for j in range(N) for k in range(N) if j!=k)
        formula=2*sum(F(1,k) for k in range(1,N))-F(2*(N-1),N)
        require(direct==formula,'absolute Hilbert logarithmic loss')
    test('absolute_hilbert_kernel_is_not_bounded',38,{'Rayleigh':'2H_(N-1)-2(N-1)/N'})
    dd,ss=S.symbols('d s')
    eq(1/(dd+ss),1/dd-ss/dd**2+ss**2/(dd**2*(dd+ss)),
       'Hilbert averaging remainder identity')
    test('signed_hilbert_averaging_identity',1,{'interval_length':'delta/2'})
    require(4*F(22,7)+F(1,2)<14,'repaired mean square constant')
    test('signed_hilbert_repair_constant',1,{'result':'2T+14X'})

    # Harris model truncated harmonic product is independently positive for integer s.
    for sp in range(1,5):
        for N in range(1,25):
            primes=[p for p in range(2,N+1) if factors(p)=={p:1}]
            P=math.prod([1-F(1,p**(sp+1)) for p in primes])
            h=[F(N+1-n,N) for n in range(1,N+1)]
            lhs=sum(math.prod([1-F(1,p**sp) for p in factors(n)])*h[n-1]/n for n in range(1,N+1))
            rhs=P*sum(h[n-1]/n for n in range(1,N+1))
            require(lhs>=rhs,'weighted Jordan inequality')
    test('weighted_jordan_decreasing_tests',96,{'s':[1,2,3,4],'N':'1..24','infinite_measure_proof_not_replaced':True})
    # Terminal-scale bound and small-scale near-origin quadratic.
    kl=F(443,100);ll=F(693,1000);lu=F(694,1000)
    require(kl*kl<F(275,14),'kappa bound')
    terminal=-1+kl*F(1,2)*(1-lu)+lu-lu*lu/2  # decreasing in L on [ll,lu]
    small=kl-2+(2-kl)*F(7,10)-F(49,100)
    require(terminal>F(13,100) and small>0,'Green positive margins')
    test('green_terminal_and_near_origin',3,{'terminal_lower':str(terminal),'small_y_07_lower':str(small)})
    qv,Avv,Bvv,cv=S.symbols('q A B c',positive=True)
    rho=S.Rational(1,2)*u*u-cv*u**3/6
    # Polynomial near-origin Laplace jet formula, termwise monomials.
    def lap(poly):return S.expand(sum(cc*S.factorial(k)/qv**(k+1) for (k,),cc in S.Poly(poly,u).terms()))
    eq(qv*(qv+Avv)*(qv+Bvv)*lap(rho),1+lap(S.diff(rho,u,3)+(Avv+Bvv)*S.diff(rho,u,2)+Avv*Bvv*S.diff(rho,u)), 'boundary jet contact')
    test('green_boundary_contact',1,{'contact':1})

    z=S.symbols('z');aa=S.Rational(1,8);g=4
    E=math.prod([(z-d)**2+g*g for d in [S.Rational(3,8),S.Rational(1,8),-S.Rational(1,8),-S.Rational(3,8)]])
    quot=S.cancel(E.subs(z,z-aa)/E.subs(z,z+aa))
    target=((z-S.Rational(1,2))**2+g*g)/((z+S.Rational(1,2))**2+g*g)
    eq(quot,target,'net pole cancellation model')
    require(S.denom(quot).subs(z,S.Rational(1,4)+4*S.I)!=0,'raw crossed pole cancels')
    test('crossed_poles_need_net_multiplicity',2,{'depths':['3/8','1/8','-1/8','-3/8'],'a':'1/8','raw_crossed_pole':'1/4+4i','reduced_RHP_poles':0})
    F0,G0,F1,G1=S.symbols('F G Fb Gb')
    eq(1-F0*G0*F1*G1,1-F0*F1+F0*F1*(1-G0*G1),'kernel product identity')
    test('krein_product_algebra',1,{'only_model_kernel_identity':True})

    # P61 finite X=184 regeneration using the literal positive dictionary.
    N=184;coeff_f=[0]*(N+1);coeff_m=[0]*(N+1)
    def dictionary(k): return 0 if k==1 else 15 if k==2 else 3 if k==4 else 6
    for n in range(1,N+1):
        for d in divs(n):
            fd=factors(d)
            if any(e>1 for e in fd.values()) or any(p>61 for p in fd):continue
            coeff_f[n]+=mu(d)*dictionary(n//d)
            coeff_m[n]+=dictionary(n//d)
    fi=I(0);mi=I(0)
    for n in range(1,N+1):
        hh=log_i(min(F(4),F(N,n)))
        wt=sqrt_i(n).inv()*hh
        fi=fi+coeff_f[n]*wt;mi=mi+coeff_m[n]*wt
    old=40*fi-mi;new=42*fi-mi
    require(old.hi<F(-18,1) and new.lo>F(3,1),'P61 bias counterfixture')
    test('P61_X184_independent_directed_regeneration',1,{'40F-M':old.dump(),'42F-M':new.dump(),'precision_bits':BITS,'log_terms':48,'not_full_campaign':True})
    # All finite Euler sieve colors have convergent weighted variation after leading cancellation.
    require(F(25,8)+F(1,5)<5,'Euler ramp analytic constant')
    for eta in [F(0),F(1,4),F(49,100)]: require(eta-F(1,2)<0,'variation exponent')
    test('ramp_and_weighted_variation_constants',4,{'range':'0<=eta<1/2','no_infinite_check_claim':True})

    for n in range(1,129):
        conv=sum(mu(d)*dictionary(n//d) for d in divs(n))
        sparse=6*(n==1)-6*mu(n)+(9*mu(n//2) if n%2==0 else 0)-(3*mu(n//4) if n%4==0 else 0)
        require(conv==sparse,'literal five-three sparse dictionary')
    test('C4MBI_sparse_dictionary',128,{'source':'5Q2+3Q3; unit term retained'})

    co=[q(-F(3,2)),q(-F(3,2),F(9,2)),q(-6,F(9,2)),q(-6)]
    count=0
    for X in [F(1,2),F(1),F(3),F(4),F(7),F(16),F(25),F(64),F(129,2)]:
        for n in range(1,66):
            left={}
            for Y,c in [(X,q(-6)),(X/2,q(0,F(9,2))),(X/4,q(-F(3,2)))]:left=add_vec(left,hinge(Y,n),c)
            right={}
            ends=[X/16,X/8,X/4,X/2,X]
            for j,c in enumerate(co):right=add_vec(right,band_mass(ends[j],ends[j+1],n),c)
            require(left==right,'C4 band per-source atom')
            count+=1
    test('C4MBI_four_band_identity',count,{'real_rational_endpoints':9,'atom_cutoff':65,'logs_as_exact_prime_vectors':True})
    for n in range(2,301):
        if mu(n)==0:continue
        lhs={p:mu(n)*e for p,e in factors(n).items()}
        rhs={p:-mu(n//p) for p in factors(n)}
        require(lhs==rhs,'logarithmic owner identity')
    test('prime_owner_identity',sum(mu(n)!=0 for n in range(2,301)),{'unit_atom_handled_separately':True})

    for N in range(2,40):
        w={n:F((3*n)%7-2,n) for n in range(2,N+1)}
        dw={n:w[n]-2*w.get(4*n,F(0)) for n in w}
        # Check coefficient of each formal prime logarithm in radix-four duality.
        l={};rr={}
        for n,v in w.items():
            fs=factors(n)
            if len(fs)==1:l=add_vec(l,{next(iter(fs)):1},q(v))
            k=n;weight=1
            while True:
                fs=factors(k)
                if len(fs)==1:rr=add_vec(rr,{next(iter(fs)):1},q(weight*dw[n]))
                if k%4:break
                k//=4;weight*=2
        require(l==rr,'Y4 duality')
    test('native_radix_four_score_duality',38,{'arithmetic_benchmark_J_not_substituted':True})
    aa0=S.Matrix([2,3]);bb0=S.Matrix([1,-2]);weights=[F(1,5),F(2,5),F(3,5)];us=[F(1,2),F(2,3),F(3,4)]
    M=sum(weights);ubar=sum(w*u0 for w,u0 in zip(weights,us))/M;lo=F(1,2);hi=F(3,4);th=(ubar-lo)/(hi-lo)
    lhs=sum((S.Rational(w.numerator,w.denominator)*(aa0-S.Rational(u0.numerator,u0.denominator)*bb0) for w,u0 in zip(weights,us)), S.zeros(2,1))
    rhs=S.Rational(M.numerator,M.denominator)*(S.Rational(th.numerator,th.denominator)*(aa0-S.Rational(hi.numerator,hi.denominator)*bb0)+(1-S.Rational(th.numerator,th.denominator))*(aa0-S.Rational(lo.numerator,lo.denominator)*bb0))
    require(lhs==rhs and 0<=th<=1,'affine compression')
    test('affine_two_node_mean',1,{'theta':str(th),'zero_mass_convention_required':True})

    yy=S.symbols('y');res=17/(4+yy)**2-1/(1+yy)**2-16/(16+yy)**2
    wanted=yy*(378*yy**2+4401*yy+6048)/((1+yy)**2*(4+yy)**2*(16+yy)**2)
    eq(res,wanted,'Cauchy residual')
    test('cauchy_three_square_identity',1,{'numerator':[6048,4401,378]})
    require(-F(1,4)*2+F(17,32)*1-F(1,16)*F(1,2)==0,'physical kernel integral zero')
    # Integral of (1+k|t|)exp(-k|t|) is 4/k; the preceding is half-scaled.
    test('cauchy_physical_contact_mass',1,{'integral':0,'not_pointwise_nonnegative':True})
    for a in [F(1,2),F(1),F(3)]:
        for uv in [F(0),F(1,3),F(2),F(5)]:
            def detail(a):return ((2*a)**4/((2*a)**2+uv*uv)**2-a**4/(a*a+uv*uv)**2)/a**4
            cur=detail(a);tel=detail(a*16)
            for j in range(4):tel+=detail(a*2**j)-detail(a*2**(j+1))
            require(cur==tel,'all generation finite telescope')
    test('cauchy_finite_telescope',12,{'four_generations':True,'all_scale_limit_proved_analytically':True})
    return {'schema':'reviewer-D-pass3-controls-v1','named_checks':len(RESULTS),'fixtures':sum(t['fixtures'] for t in RESULTS),'checks':RESULTS,'scope':'bounded exact controls only; not formal verification of analytic theorems'}

def check_saved(path,result):
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    raw=Path(path).read_text();obj=json.loads(raw)
    require(obj==result and raw==text,'saved result differs from independent replay')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);p.add_argument('--compare',type=Path);a=p.parse_args()
    result=run();text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if a.compare:check_saved(a.compare,result)
    if a.output:a.output.write_text(text)
    else:print(text,end='')
