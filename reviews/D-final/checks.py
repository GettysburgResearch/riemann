#!/usr/bin/env python3
"""Independent bounded algebra for Reviewer D's closeout. No upstream imports.
These checks do not prove the analytic theorems or rerun prime/zero campaigns.
"""
from __future__ import annotations
import argparse, itertools, json, math, platform
from fractions import Fraction as F
from pathlib import Path
import sympy as s

RECORDS = []
def require(condition, message):
    if not condition:
        raise ValueError(message)
def same(a, b, message):
    require(s.simplify(a-b) == 0, message)
def record(name, count, result):
    require(type(count) is int and count > 0, 'invalid count')
    RECORDS.append({'name': name, 'fixtures': count, 'result': result})
def rat(x):
    x = F(x)
    return f'{x.numerator}/{x.denominator}'
def divisors(n):
    return [d for d in range(1,n+1) if n%d == 0]
def mu(n):
    f=s.factorint(n)
    return 0 if any(e>1 for e in f.values()) else (-1)**len(f)
def conv(a,b,N):
    return [F(0)]+[sum((a[d]*b[n//d] for d in divisors(n)),F(0)) for n in range(1,N+1)]
def prime_power(n):
    return n>=2 and len(s.factorint(n))==1

def run():
    RECORDS.clear()
    # The primal and the INCORRECT printed separator can both hold.
    A=G=b=z=1; u=-1; v=1
    require(A*z==b and G*z>=0 and z>=0, 'primal')
    require(A*u+G*v>=0 and v>=0 and b*u<0, 'wrong-sign counterexample')
    record('Farkas_plus_sign_counterexample',1,{'A':1,'G':1,'b':1,'z':1,'u':-1,'v':1})
    count=0
    for A,G,b in itertools.product(range(-2,3),repeat=3):
        feasible=(b==0) if A==0 else (F(b,A)>=0 and G*F(b,A)>=0)
        witnesses=[(u,v) for u in range(-6,7) for v in range(7)
                   if A*u-G*v>=0 and b*u<0]
        require(feasible != bool(witnesses), f'correct dual alternative {A,G,b}')
        count+=1
    record('Corrected_one_variable_Farkas_grid',count,{'dual':'A^T u-G^T v>=0; v>=0; b^T u<0'})
    B=s.Matrix([[1,-1],[s.sqrt(2),-s.sqrt(2)]]); y=s.Matrix([-s.sqrt(2),1]); b=s.Matrix([0,-1])
    require(B.T*y==s.zeros(2,1) and (b.T*y)[0]==-1,'algebraic separator')
    require(not s.sqrt(2).is_rational,'irrationality')
    record('Real_data_need_not_have_rational_separator',1,{'dual_ray':'t*(-sqrt(2),1), t>0','primal':'infeasible'})
    phases=[s.Integer(1),-s.Integer(1),s.I,-s.I,s.Rational(3,5)+s.I*s.Rational(4,5)]
    for d in phases:
        same(s.re(1-d),s.expand_complex((1-d)*s.conjugate(1-d))/2,'real part vector')
    require(1-(-s.I) != 1,'unsymmetrized value not real')
    record('One_sided_vector_generator_real_part',len(phases),{'counterexample':'D=-i, f=1: 1+i versus 1'})
    X=s.Matrix([[1,2+s.I],[3,0]]); U=s.diag(1,s.I); LX=U*X*U.conjugate().T-X
    val=-s.trace(X.conjugate().T*LX); diff=U*X*U.conjugate().T-X
    same(s.re(val),s.trace(diff.conjugate().T*diff)/2,'HS real part')
    require(s.im(val)!=0,'HS counterexample has imaginary part')
    record('Matrix_conjugation_generator_HS_real_part',1,{'negative_inner_product':str(s.expand(val))})
    x=s.symbols('x',real=True)
    source_norm=s.integrate(s.exp(-2*x*x),(x,-s.oo,s.oo))
    fourier_norm=s.integrate(s.pi*s.exp(-x*x/2),(x,-s.oo,s.oo))
    same(fourier_norm,2*s.pi*source_norm,'Plancherel factor')
    record('Fredholm_inherited_Fourier_normalization',1,{'factor':'2*pi','correct_leading_coefficient':'Re psi(1/4+iT/2)-log pi'})
    sigma=s.symbols('sigma',positive=True)
    rnorm=s.integrate(s.exp(-2*s.Abs(x))/4,(x,-s.oo,s.oo))
    same(rnorm,s.Rational(1,4),'resolvent norm')
    same(rnorm*s.sqrt(s.pi/(2*sigma)),s.sqrt(s.pi/(2*sigma))/4,'HS trace')
    record('Gaussian_confinement_trace',1,{'trace_B':'sqrt(pi/(2*sigma))/4'})
    def rem(m,k,z):
        return (-1)**k*(max(F(0),1-z)**m-sum(((-1)**j*math.comb(m,j)*z**j for j in range(k)),F(0)))
    t=s.symbols('t'); zs=[F(0),F(1,3),F(1),F(4,3),F(3)]
    count=0
    for m in range(2,8):
        for k in range(1,m+1):
            for z in zs:
                r=rem(m,k,z)
                integrand=(s.Rational(z.numerator,z.denominator)-t)**(k-1)*(1-t)**(m-k)
                val=s.factorial(m)/s.factorial(m-k)/s.factorial(k-1)*s.integrate(integrand,(t,0,s.Rational(min(z,F(1)))))
                same(s.Rational(r),val,'Taylor remainder integral')
                require(r>=0,'Taylor sign'); count+=1
    record('Euler_Taylor_integral_remainders',count,{'m_max':7,'z_count':len(zs)})
    count=0
    for m in range(3,9):
        for k in range(1,m):
            for z in zs:
                for c in [F(1),F(3,2),F(2)]:
                    require(rem(m,k,c*z)<=c**k*rem(m,k,z),'dilation remainder');count+=1
    record('Taylor_dilation_bound',count,{'orders':'k<m<=8'})
    q=s.symbols('q'); count=0
    for m in range(2,9):
        directly=2*4**m*(sum((-1)**j*s.binomial(m,j)/(j-2*q) for j in range(2,m+1))+m/(2*q-1)-1/(2*q))
        target=2*4**m*s.factorial(m)/(2*q*(2*q-1)*s.prod(j-2*q for j in range(2,m+1)))
        same(directly,target,'critical Mellin symbol');count+=1
    record('Critical_Taylor_Mellin_symbol',count,{'fundamental_strip':'1/2<Re(s)<1'})
    count=0
    for m in range(2,9):
        target=2*4**m*s.factorial(m)/(2*q*(2*q-1)*s.prod(j-2*q for j in range(2,m+1)))
        for j in range(2,m+1):
            same(s.limit((q-s.Rational(j,2))*target,q,s.Rational(j,2)),-4**m*(-1)**j*s.binomial(m,j),'residue')
            count+=1
    record('Critical_Taylor_positive_real_residue_cancellation',count,{'warning':'analytic B-values and zeta-pole cancellation are separate inputs'})
    count=0
    for m in range(2,9):
        for y in [F(1,16),F(1,4),F(1),F(4),F(9)]:
            root=s.sqrt(s.Rational(y)); form=(1-root)**m+m*root-1 if y<1 else m*root-1
            z=F(math.isqrt(y.denominator),math.isqrt(y.numerator))
            same(root**m*s.Rational(rem(m,m-1,z)),form,'native critical kernel')
            count+=1
    record('Critical_Taylor_source_kernel_rescaling',count,{'m_min':2,'m_max':8})
    bound=F(8,3)*F(536,535)
    require(bound<F(163,60),'prime label threshold')
    record('Supercritical_prime_label_threshold',1,{'zeta_bound_over_local_factor':rat(bound),'exp_lower':rat(F(163,60))})
    def qa(n,A):
        return math.prod((1-F(1,int(p)**A) for p in s.factorint(n)),start=F(1))
    count=0
    for A,B in itertools.product(range(1,4),repeat=2):
        for n in range(1,81):
            value=sum((qa(d,A)*qa(n//d,B)*F(1,(n//d)**A) for d in divisors(n)),F(0))
            require(value==qa(n,A+B),'Jordan convolution');count+=1
    record('Jordan_divisor_cocycle_exact_rational',count,{'parameter_convention':'A=2a, B=2b'})
    count=0
    for n in range(1,49):
        total=F(0)
        for d in divisors(n):
            for e in divisors(n//d):
                f=n//d//e
                weight=qa(d,1)*qa(e,2)*qa(f,1)/e/f**3/qa(n,4)
                left=qa(d,1)*qa(e*f,3)/(e*f)/qa(n,4)*qa(e,2)*qa(f,1)/f**2/qa(e*f,3)
                right=qa(d*e,3)*qa(f,1)/f**3/qa(n,4)*qa(d,1)*qa(e,2)/e/qa(d*e,3)
                require(weight==left==right,'coassociativity');total+=weight;count+=1
        require(total==1,'probability partition')
    record('Jordan_coassociation_and_probability',count,{'n_max':48})
    count=0
    for k in range(1,6):
        rs=[F(1,j+9) for j in range(k)]
        survival=math.prod((1-r for r in rs),start=F(1)); lam=[]; acc=F(1)
        for r in rs: lam.append(acc*r);acc*=1-r
        require(sum(lam)+survival==1,'hazard total')
        require(sum(lam[i]*rs[i] for i in range(k))<F(1,8),'child coefficient')
        lhs={bits:(-1)**sum(bits)*math.prod((rs[i] for i,b in enumerate(bits) if b),start=F(1)) for bits in itertools.product([0,1],repeat=k)}
        rhs={bits:F(0) for bits in lhs};rhs[(0,)*k]=survival
        for i in range(k):
            for tail in itertools.product([0,1],repeat=k-i-1):
                coef=lam[i]*(-1)**sum(tail)*math.prod((rs[h] for h,b in enumerate(tail,i+1) if b),start=F(1))
                for own in [0,1]: rhs[(0,)*i+(own,)+tail]+=(-1)**own*coef
        require(lhs==rhs,'first-owner monomials');count+=len(lhs)
    record('First_owner_full_monomial_identity',count,{'k_max':5})
    probs=[s.Rational(1,2),s.Rational(1,3),s.Rational(1,6)]; atoms=[0,1,3]
    mean=sum(p*a for p,a in zip(probs,atoms)); moments={j:sum(p*(a-mean)**j for p,a in zip(probs,atoms)) for j in range(5)}
    var=moments[2]; tau=moments[4]-var**2-moments[3]**2/var
    require(tau>0,'anchor rank'); P=lambda a:(a-mean)**2-var-moments[3]*(a-mean)/var
    same(sum(p*P(a) for p,a in zip(probs,atoms)),0,'orthogonality0')
    same(sum(p*(a-mean)*P(a) for p,a in zip(probs,atoms)),0,'orthogonality1')
    same(sum(p*P(a)**2 for p,a in zip(probs,atoms)),tau,'norm2')
    record('Anchor_second_jet_Gram_Schmidt',1,{'variance':str(var),'tau_squared':str(tau)})
    count=0
    for l in range(-3,4):
        lhs=sum(p*(l+a)**4 for p,a in zip(probs,atoms))
        rhs=((l+mean)**2+var)**2+(2*s.sqrt(var)*(l+mean)+moments[3]/s.sqrt(var))**2+tau
        same(lhs,rhs,'second jet norm');count+=1
    record('Anchor_second_jet_norm_identity',count,{'scope':'finite positive law'})
    count=0
    for Q in range(2,257):
        chain=[];n=Q;k=0
        while True:
            chain.append((n,2**k))
            if n%4: break
            n//=4;k+=1
        visible=[n for n,w in chain if prime_power(n)]
        require(bool(visible)==any(prime_power(Q//4**k) for k in range(10) if Q%(4**k)==0),'Y4 support');count+=1
    record('Y4_null_columns_support',count,{'range':'2<=Q<=256','historical_5000_census_not_rerun':True})
    def beta(n,q):
        a,r=divmod(n,q)
        return F(a*(q-1-r),n+1)
    count=0
    for Q in range(4,33):
        target={q:F(0) for q in range(2,Q+1)};n=Q;k=0
        while n>=2:
            target[n]=F(2**k)
            if n%4: break
            n//=4;k+=1
        h={}
        for q in reversed(range(2,Q+1)):
            h[q]=(target[q]-sum((beta(n,q)*h[n] for n in range(q+1,Q+1)),F(0)))/beta(q,q)
        for q in range(2,Q+1):
            require(sum((beta(n,q)*h[n] for n in range(q,Q+1)),F(0))==target[q],'triangular inverse');count+=1
        require(h[Q]==F(Q+1,Q-1) and h[Q-1]==-F(Q*(Q-3),(Q-1)*(Q-2)),'top transfer')
    record('Y4_full_triangular_columns',count,{'Q_min':4,'Q_max':32,'index_floor':2})
    N=120; one=[F(0)]+[F(1)]*N; muv=[F(0)]+[F(mu(n)) for n in range(1,N+1)]
    eta=[F(0)]
    for n in range(1,N+1):
        eta.append(math.prod((F(math.comb(2*int(e),int(e)),4**int(e)) for e in s.factorint(n).values()),start=F(1)))
    require(conv(eta,eta,N)==one,'eta square')
    record('Half_divisor_convolution_square',N,{'n_max':N})
    count=0
    for U in [1,3,8,16]:
        b=[F(0)]+[muv[n] if n>U else F(0) for n in range(1,N+1)]
        small=[F(0)]+[muv[n] if n<=U else F(0) for n in range(1,N+1)]
        a0=conv(small,one,N);a=[F(0)]+[F(n==1)-a0[n] for n in range(1,N+1)]
        require(a==conv(b,one,N),'a=b*1')
        h=conv(b,eta,N)
        balanced=conv(conv(a,a,N),muv,N)
        require(balanced==conv(b,a,N)==conv(h,h,N)==conv(conv(b,b,N),one,N),'balanced factorizations')
        count+=N
    record('Vaughan_full_coefficient_factorizations',count,{'n_max':N,'cutoffs':[1,3,8,16]})
    count=0
    for d in range(1,49):
        for e in range(1,49):
            if mu(d)*mu(e)==0: continue
            g=math.gcd(d,e);a=d//g;b=e//g
            require(mu(g*a*b)**2==1 and mu(d)*mu(e)==mu(a)*mu(b),'gcd source');count+=1
    record('Vaughan_squarefree_gcd_reparameterization',count,{'d_e_max':48})
    count=0
    for X in range(8,301):
        U=0
        while (U+1)**3<=X:U+=1
        for d in range(U+1,math.isqrt(X)+1):
            for e in range(d,X//d+1):
                require(e<d*d,'parabolic cutoff');count+=1
    record('Vaughan_exact_floor_parabolic_support',count,{'X_max':300})
    y=s.symbols('y',positive=True)
    forms=[2*(s.sqrt(y)-1),2*s.sqrt(2)-s.sqrt(2*y)]
    same(y*s.diff(forms[0],y)-forms[0]/2,1,'Aminus first')
    same(y*s.diff(forms[1],y)-forms[1]/2,-s.sqrt(2),'Aminus second')
    same(forms[0].subs(y,2),forms[1].subs(y,2),'spline continuity')
    record('Ratio_four_half_kernel',3,{'support':'[1,4]','endpoint_values':'a.e. for integral identities'})
    x,t,a=s.symbols('x t a',positive=True); F0,F1=s.symbols('F0 F1')
    K=2*(x-s.sqrt(x*t))/t**s.Rational(3,2)
    V=lambda f:(2*x*x*s.diff(f,x,2)-x*s.diff(f,x)+f)/(2*s.sqrt(x))
    same(V(s.sqrt(x)),0,'mode sqrt');same(V(x),0,'mode x');same(V(K),0,'open-cell Green')
    same(s.diff(K,x).subs(x,t),t**(-s.Rational(3,2)),'Green jump')
    A=2*(F0-a*F1)/s.sqrt(a);B=2*F1-F0/a
    same((A*s.sqrt(x)+B*x).subs(x,a),F0,'Green boundary value')
    same(s.diff(A*s.sqrt(x)+B*x,x).subs(x,a),F1,'Green boundary derivative')
    record('Volterra_modes_boundary_and_jump',6,{'a':'strictly positive','derivative_jump_mass':'t^(3/2)*jump(f prime)'})
    lower=F(86883,100000);upper=F(86884,100000)
    require(lower**6+lower**4<1<upper**6+upper**4,'plastic interval')
    cap=F(8,7)*upper**7-8*sum((lower**(9+4*j)/F(9+4*j) for j in range(1,7)),F(0))
    require(cap<F(1,4),'negative score cap')
    record('Plastic_negative_score_six_term_cap',1,{'cap_lt':'1/4','positive_root_bracket':[rat(lower),rat(upper)]})
    m4=4*(F(1,16)+F(1,8)*(F(2,7)+F(4,49)))
    require(m4==F(85,196),'prime mass arithmetic')
    reserve=1-m4*m4-F(1,4)
    require(reserve==F(21587,38416)>F(1,2),'reserve correction')
    record('Julia_prime_mass_and_existing_margin_repair',2,{'m4_upper':rat(m4),'reserve_lower':rat(reserve),'not_a_new_margin_discovery':True})
    D=[F(1),F(2),F(3,2),F(1)];ds=[D[0]]+[D[j]-D[j-1] for j in range(1,4)];count=0
    for M in itertools.product([-1,0,1],repeat=4):
        seq=list(map(F,M))+[F(0)];up=sum((max(F(0),seq[i+1]-seq[i]) for i in range(4)),F(0))
        left=sum((ds[i]*seq[i] for i in range(4)),F(0))
        right=sum((D[i]*(seq[i]-seq[i+1]) for i in range(4)),F(0))
        require(left==right and left>=F(9,10)*seq[0]-F(6,5)*up,'signed Abel');count+=1
    record('Carry_prefix_signed_Abel_payment',count,{'primitive_d64_generator_not_run':True})
    ps=[2,3,5,7];mass=sum((F(1,p) for p in ps),F(0));squares=sum((F(1,p*p) for p in ps),F(0));count=0
    for Y in [8,16,40,80]:
        for k in range(2,5):
            ordered=sum((F(1,math.prod(tup)) for tup in itertools.product(ps,repeat=k) if math.prod(tup)<=Y),F(0))/math.factorial(k)
            distinct=sum((F(1,math.prod(tup)) for tup in itertools.combinations(ps,k) if math.prod(tup)<=Y),F(0))
            bound=squares*mass**(k-2)/2/math.factorial(k-2)
            require(0<=ordered-distinct<=bound,'repeated prime union');count+=1
    record('Dickman_repeated_prime_union_bound',count,{'prime_set':ps})
    def rough(n,p): return n==1 or min(s.factorint(n))>=p
    def rough_source(Y,p):
        return sum((F(mu(n),n)*(F(Y,n)**2+F(Y,n)) for n in range(1,math.floor(Y)+1) if rough(n,p)),F(0))
    count=0
    for Y in range(1,65):
        for p,pp in [(2,3),(3,5),(5,7),(7,11)]:
            require(rough_source(F(Y),p)==rough_source(F(Y),pp)-rough_source(F(Y,p),pp)/p,'Bellman source recurrence');count+=1
    record('Bellman_literal_least_prime_identity',count,{'test_base':'h(t)=t^2+t on t>=1','no_analytic_corridor_test':True})
    weights=[F(1,3),F(1,5),F(1,7)]; atoms=[F(1),F(3,2),F(2)];weights2=[F(1,4),F(1,6),F(1,8)]
    delta=max(abs(sum(weights[:j+1])-sum(weights2[:j+1])) for j in range(3));M=max(sum(weights),sum(weights2));count=0
    for k in range(1,5):
        nodes=sorted(set(sum((atoms[i] for i in tup),F(0)) for tup in itertools.product(range(3),repeat=k)))
        for threshold in nodes:
            values=[]
            for ww in [weights,weights2]:
                values.append(sum((math.prod((ww[i] for i in tup),start=F(1)) for tup in itertools.product(range(3),repeat=k) if sum((atoms[i] for i in tup),F(0))<=threshold),F(0)))
            require(abs(values[0]-values[1])<=2*k*delta*M**(k-1),'CDF convolution telescope');count+=1
    record('Dickman_CDF_convolution_discrepancy',count,{'signed_factor_control':'2*k*delta*M^(k-1)'})
    # Point mass source and a step base: closed endpoint equality is essential.
    count=0
    for Y in range(1,21):
        jumps={1:F(0),2:F(3,2),5:F(-1,3)};source={1:F(1),3:F(-1,3),7:F(1,7)}
        h=lambda x:sum((v for a,v in jumps.items() if a<=x),F(0))
        A=lambda x:sum((v for a,v in source.items() if a<=x),F(0))
        left=sum((v*h(F(Y,n)) for n,v in source.items()),F(0));right=sum((v*A(F(Y,a)) for a,v in jumps.items()),F(0))
        require(left==right,'Stieltjes endpoint Fubini');count+=1
    record('Signed_Stieltjes_endpoint_transfer',count,{'atom_ownership':'closed n*a<=Y'})
    for alpha,a,b in [(F(3,5),F(4,5),F(2)),(F(2,3),F(5,6),F(3))]:
        theta=(b-a)/(b-alpha);require(0<theta<1,'three-lines exponent')
    epsilon=F(1,4)
    require(-4+2*epsilon<-1 and -2+2*epsilon<-1,'double Hardy majorant')
    record('Reciprocal_zeta_Hardy_exponent_contract',3,{'epsilon':'1/4','t_power':'-7/2','gamma_power':'-3/2','analytic_theorem_not_finitely_verified':True})
    M=s.Matrix([[3,s.Rational(1,4)+s.I/8],[s.Rational(1,4)-s.I/8,2]])
    small=M-s.eye(2)
    require(small[0,0]>0 and small.det()>0,'midpoint positivity')
    record('Finite_Hermitian_midpoint_moat',1,{'delta':'1','allowed_operator_radius_lt':'1','actual_xi_primitives_not_run':True})
    return {'schema':'riemann.review.D.closeout.checks.v1','python':platform.python_version(),'sympy':s.__version__,
            'proof_status':'BOUNDED_RECONSTRUCTION_ONLY','named_checks':len(RECORDS),
            'fixtures':sum(r['fixtures'] for r in RECORDS),'checks':RECORDS}

def pairs(items):
    out={}
    for k,v in items:
        require(k not in out,'duplicate JSON key');out[k]=v
    return out
def load_strict(path):
    return json.loads(Path(path).read_text(),object_pairs_hook=pairs,
                      parse_float=lambda x: (_ for _ in ()).throw(ValueError('float forbidden')),
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError('constant forbidden')))
def strict_equal(a,b):
    if type(a) is not type(b): return False
    if isinstance(a,dict):
        return a.keys()==b.keys() and all(strict_equal(a[k],b[k]) for k in a)
    if isinstance(a,list):
        return len(a)==len(b) and all(strict_equal(x,y) for x,y in zip(a,b))
    return a==b

def main():
    p=argparse.ArgumentParser();p.add_argument('--check');args=p.parse_args()
    data=run()
    if args.check:
        require(strict_equal(load_strict(args.check),data),'retained output mismatch')
        print(f"PASS {data['named_checks']} named checks / {data['fixtures']} fixtures")
    else:print(json.dumps(data,indent=2,sort_keys=True))
if __name__=='__main__':main()
