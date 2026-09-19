#!/usr/bin/env python3
"""Exact finite controls for RBR26; not a proof of the analytic theorems or RH.

--emit is producer mode. --check authenticates the packet and reconstructs every
fixed finite case. No floating point or zeta oracle is used in acceptance.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import itertools
import json
import math
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCALE = 1 << 192
PUBLISHED = 1 << 40


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


@dataclass(frozen=True)
class Q:
    r: F = F(0)
    i: F = F(0)

    @staticmethod
    def lift(x):
        return x if isinstance(x, Q) else Q(F(x))

    def __add__(self, x):
        x = Q.lift(x)
        return Q(self.r+x.r, self.i+x.i)
    __radd__ = __add__

    def __neg__(self):
        return Q(-self.r, -self.i)

    def __sub__(self, x):
        return self + -Q.lift(x)

    def __rsub__(self, x):
        return Q.lift(x) + -self

    def __mul__(self, x):
        x = Q.lift(x)
        return Q(self.r*x.r-self.i*x.i, self.r*x.i+self.i*x.r)
    __rmul__ = __mul__

    def __truediv__(self, x):
        x = Q.lift(x)
        den = x.r*x.r+x.i*x.i
        need(den != 0, 'division by zero')
        return self*x.conj()*F(1, den)

    def __rtruediv__(self, x):
        return Q.lift(x)/self

    def __pow__(self, n):
        need(type(n) is int, 'noninteger Gaussian power')
        if n < 0:
            return (1/self)**(-n)
        out, base = Q(1), self
        while n:
            if n & 1:
                out = out*base
            base = base*base
            n >>= 1
        return out

    def conj(self):
        return Q(self.r, -self.i)

    def norm(self):
        return self.r*self.r+self.i*self.i


def poly_mul(p, q):
    out = [Q()]*(len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i+j] = out[i+j]+x*y
    return out


def poly_pow(p, n):
    out = [Q(1)]
    for _ in range(n):
        out = poly_mul(out, p)
    return out


def peval(p, x):
    out = Q()
    for c in reversed(p):
        out = out*x+c
    return out


def deriv(p, m=1):
    for _ in range(m):
        p = [i*p[i] for i in range(1, len(p))]
    return p


def integral(p, a, b):
    return sum((p[j]*(b**(j+1)-a**(j+1))/F(j+1)
                for j in range(len(p))), Q())


def solve(a, b):
    n = len(b)
    mat = [[Q.lift(v) for v in row]+[Q.lift(rhs)] for row, rhs in zip(a,b)]
    for j in range(n):
        pivot = next((i for i in range(j,n) if mat[i][j] != Q()), None)
        need(pivot is not None, 'singular system')
        mat[j], mat[pivot] = mat[pivot], mat[j]
        z = mat[j][j]
        mat[j] = [v/z for v in mat[j]]
        for i in range(n):
            if i != j:
                z = mat[i][j]
                if z != Q():
                    mat[i] = [x-z*y for x,y in zip(mat[i],mat[j])]
    return [row[-1] for row in mat]


def det(a):
    n = len(a)
    if n == 0:
        return Q(1)
    return sum(((-1)**j*a[0][j]*det([row[:j]+row[j+1:] for row in a[1:]])
                for j in range(n)), Q())


def psd(a):
    n = len(a)
    need(all(a[i][j] == a[j][i].conj() for i in range(n) for j in range(n)), 'not Hermitian')
    for mask in range(1,1<<n):
        ind = [i for i in range(n) if mask>>i & 1]
        d = det([[a[i][j] for j in ind] for i in ind])
        need(d.i == 0 and d.r >= 0, 'negative principal minor')


def terms_add(out, exponent, coefficient):
    out[exponent] = out.get(exponent,Q())+coefficient
    if out[exponent] == Q():
        del out[exponent]


def state(terms, lam, initial=Q()):
    out = {lam: Q.lift(initial)} if initial != Q() else {}
    for u, c in terms.items():
        need(u != lam, 'the finite modal corpus uses distinct poles')
        v = c/(u-lam)
        terms_add(out, u, v)
        terms_add(out, lam, -v)
    return out


def norm(terms):
    out = Q()
    for u,c in terms.items():
        for v,d in terms.items():
            need(u.r+v.r < 0, 'nonintegrable modal source')
            out -= c*d.conj()/(u+v.conj())
    need(out.i == 0 and out.r >= 0, 'invalid modal norm')
    return out.r


def packf(x):
    return [str(x.numerator),str(x.denominator)]


def packq(z):
    return [packf(z.r),packf(z.i)]


def adjoint_cases():
    rows = []
    for m in range(1,9):
        for a,b in ((F(5,4),F(7,4)),(F(3,2),F(5,2))):
            mass = (b**(2*m-1)-a**(2*m-1))/F(2*m-1)
            # Interior polynomial obtained by integrating from the right endpoint.
            p = [Q()] * (2*m)
            p[m-1] = Q((-1)**m*F(math.factorial(m-1),1)/mass)
            for _ in range(m):
                integ = [Q()]+[p[j]/F(j+1) for j in range(len(p))]
                integ[0] = -peval(integ,Q(b))
                p = integ
            # Zero high coefficients are kept to avoid hidden degree assumptions.
            left = [Q()]*m
            for j in range(m):
                left[j] = Q((-1)**j*F(math.comb(m-1,j),1)/mass
                            *(b**(2*m-1-j)-a**(2*m-1-j))/F(2*m-1-j))
            need(peval(left,Q(0)) == Q(1), 'left normalization')
            for j in range(m):
                need(peval(deriv(p,j),Q(b)) == Q(), 'right jet')
                need(peval(deriv(p,j),Q(a)) == peval(deriv(left,j),Q(a)), 'matching jet')
            dm = deriv(p,m)
            n2 = integral(poly_mul(dm,dm),a,b)
            expect = F(math.factorial(m-1)**2,1)/mass
            need(n2 == Q(expect), 'optimal norm')
            # Independent moment Cauchy--Schwarz equality and an orthogonal perturbation.
            moment = integral([Q() for _ in range(m-1)]+dm,a,b)
            need(moment == Q((-1)**m*math.factorial(m-1)), 'moment constraint')
            c = ((b**(2*m)-a**(2*m))/F(2*m))/mass
            perturb = [Q()]*m+[Q(1)]
            perturb[m-1] = -Q(c)
            orth = integral(poly_mul(dm,perturb),a,b)
            need(orth == Q(), 'orthogonal perturbation')
            rows.append({'m':m,'a':packf(a),'b':packf(b),'mass':packf(mass),'norm2':packf(expect)})
    return rows


def resonance_cases():
    rows = []
    points = [Q(1),Q(2),Q(1,F(1,2)),Q(3,F(-2,3))]
    for m,a,w in itertools.product(range(1,7),(F(1,2),F(1),F(2)),(F(1),F(2),F(3))):
        lam = Q(0,w)
        coeff = [None]+[Q((-1)**(m-j)*math.comb(2*m-j-1,m-j))/(2*lam)**(2*m-j)
                        for j in range(1,m+1)]
        for z in points:
            got = sum((coeff[j]/(z-lam)**j+coeff[j].conj()/(z+lam)**j
                       for j in range(1,m+1)),Q())
            need(got == 1/(z*z+w*w)**m, 'partial fractions')
        Dm = math.factorial(m)*(2*lam)**m/(lam+a)**(2*m+1)
        G = 1/(lam+a)**(2*m+1)
        leading = 2*coeff[m].norm()/math.factorial(m-1)**2
        lower = 2*m*m*(G/Dm).norm()
        need(leading == lower, 'sharp leading energy')
        r = F(2)
        window = (r**(2*m-1)-1)/F(2*m-1)
        rows.append({'m':m,'a':packf(a),'omega':packf(w),'annular_constant':packf(window*lower)})
    return rows


def cascade_cases():
    banks = [((F(1,2),F(0)),),
             ((F(1,4),F(1)),(F(1,4),F(-1))),
             ((F(1,8),F(0)),(F(1,4),F(2)),(F(1,4),F(-2))),
             ((F(1,10),F(1)),(F(1,10),F(-1)),(F(1,5),F(3)),(F(1,5),F(-3)))]
    rows=[]
    for bank in banks:
        n=len(bank); widths=[a for a,w in bank]
        A=[[Q(-widths[j]) if j<i else Q(-widths[i],bank[i][1]) if i==j else Q()
            for j in range(n)] for i in range(n)]
        S=[[Q(widths[i]) if i==j else Q() for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                lhs=sum((A[k][i].conj()*S[k][j]+S[i][k]*A[k][j] for k in range(n)),Q())
                rhs=-widths[i]*widths[j]-(widths[i]**2 if i==j else 0)
                need(lhs==Q(rhs), 'storage certificate')
        lin=[];rhs=[]
        for i in range(n):
            for j in range(n):
                row=[Q()]*(n*n)
                for k in range(n):
                    row[k*n+j] += A[k][i].conj()
                    row[i*n+k] += A[k][j]
                lin.append(row);rhs.append(-widths[i]*widths[j])
        sol=solve(lin,rhs); P=[sol[i*n:(i+1)*n] for i in range(n)]
        psd(P);psd([[S[i][j]-P[i][j] for j in range(n)] for i in range(n)])
        x0=[Q(F(i+1,n+1),F((-1)**i,n+2)) for i in range(n)]
        xs=[]
        for j in range(n):
            forcing={}
            for k in range(j):
                for u,c in xs[k].items(): terms_add(forcing,u,-widths[k]*c)
            xs.append(state(forcing,A[j][j],x0[j]))
        y={}
        for j in range(n):
            for u,c in xs[j].items(): terms_add(y,u,-widths[j]*c)
        tail=norm(y)
        quadratic=sum((x0[i].conj()*P[i][j]*x0[j] for i in range(n) for j in range(n)),Q())
        need(quadratic==Q(tail), 'whole-tail Lyapunov/modal mismatch')
        for b in (F(2),F(3),F(5)):
            inp={Q(-b):Q(1)};loss=F(0)
            for a,w in bank:
                x=state(inp,Q(-a,w))
                out=dict(inp)
                for u,c in x.items(): terms_add(out,u,-a*c)
                need(norm(inp)==norm(out)+a*a*norm(x), 'individual energy ledger')
                loss+=a*a*norm(x);inp=out
            need(norm(inp)+loss==F(1,2*b), 'cascade telescope')
            # Independently reconstruct residues of the final rational transfer.
            poles=[Q(-b)]+[Q(-a,w) for a,w in bank]
            direct={}
            for p in poles:
                c=Q(1)
                for a,w in bank: c*=p-Q(0,w)
                for q in poles:
                    if q!=p: c/=p-q
                terms_add(direct,p,c)
            need(direct==inp and norm(direct)==norm(inp),'transfer/modal reconstruction')
            rows.append({'bank':[[packf(a),packf(w)] for a,w in bank],
                         'input_rate':packf(b),'output':packf(norm(inp)),
                         'removed':packf(loss),'tail_control':packf(tail)})
        for alpha,beta in itertools.product((F(1,4),F(1),F(2)),(F(-3),F(0),F(1),F(5))):
            z=Q(alpha,beta); W=Q(1); low=F(1)
            for a,w in bank:
                W*=(z-Q(0,w))/(z+Q(a,-w))
                low*=alpha*alpha/(alpha+a)**2
            need(low<=W.norm()<=1, 'uniform interior retention')
    return rows


def mobius_sieve(n):
    mu=[1]*(n+1);mu[0]=0
    prime=[True]*(n+1)
    for p in range(2,n+1):
        if prime[p]:
            for j in range(p,n+1,p):
                prime[j]=False;mu[j]*=-1
            for j in range(p*p,n+1,p*p): mu[j]=0
    return mu


def mobius_trial(n):
    p=2; sign=1
    while p*p<=n:
        if n%p==0:
            n//=p;sign=-sign
            if n%p==0:return 0
        p+=1
    return -sign if n>1 else sign


def floorf(x): return x.numerator//x.denominator

def ceilf(x): return -floorf(-x)


def log_increment(k):
    # log((k+1)/k) = 2 atanh(1/(2k+1)), complete positive remainder.
    q=F(1,2*k+1);s=F(0);power=q;j=0
    while True:
        s+=2*power/F(2*j+1);power*=q*q;j+=1
        rem=2*power/F(2*j+1)/(1-q*q)
        if rem*SCALE< F(1,4):break
    return F(floorf(s*SCALE),SCALE),F(ceilf((s+rem)*SCALE),SCALE)


def native_cases():
    ys=list(range(1,33))+[63,127,255,511]
    mu=mobius_sieve(max(ys))
    need(all(mu[n]==mobius_trial(n) for n in range(1,len(mu))), 'Mobius reconstruction')
    m=F(0);M=0;energy=F(0);past=F(0);slo=F(0);shi=F(0);rows=[]
    for k in range(1,max(ys)+1):
        m+=F(mu[k],k);M+=mu[k];energy+=m*m;past+=F(M*M,k*(k+1))
        lo,hi=log_increment(k);coef=m*M
        if coef>=0:slo+=coef*lo;shi+=coef*hi
        else:slo+=coef*hi;shi+=coef*lo
        if k in ys:
            end=F(((k+1)*m-M)**2,k+1)
            need(energy==past+end,'native terminal identity')
            directlo=(energy+past+2*slo+end)/4
            directhi=(energy+past+2*shi+end)/4
            losslo=energy-(energy+past-2*slo+end)/4
            losshi=energy-(energy+past-2*shi+end)/4
            need((directlo,directhi)==(losslo,losshi),'direct/loss native mismatch')
            need(0<directlo<=directhi<energy,'native passivity interval')
            rows.append({'Y':k,'F':packf(energy),'terminal_square':packf(end),
                         'output_dyadic':[floorf(directlo*PUBLISHED),ceilf(directhi*PUBLISHED)],
                         'prefix_output_dyadic':[floorf((directlo-end/4)*PUBLISHED),ceilf((directhi-end/4)*PUBLISHED)],
                         'full_tail_energy':packf(end/4),
                         'gain_dyadic':[floorf((energy-directhi)*PUBLISHED),ceilf((energy-directlo)*PUBLISHED)]})
    return rows


def scalar_cases():
    rows=[]
    for a,b,w in itertools.product((F(1,4),F(1,2),F(1)),(F(2),F(3)),(F(0),F(1),F(3))):
        inp={Q(-b):Q(1)}; x=state(inp,Q(-a,w)); y=dict(inp)
        for u,c in x.items(): terms_add(y,u,-a*c)
        want=(b*(b+a)+w*w)/(2*b*((b+a)**2+w*w))
        need(norm(y)==want,'scalar closed norm')
        rows.append({'a':packf(a),'b':packf(b),'omega':packf(w),'energy':packf(want)})
    # Exact rational controls of the Fourier numerator lower bound.
    for R,t in itertools.product(range(1,9),range(0,9)):
        cosine=F(1-t*t,1+t*t);sine=F(2*t,1+t*t)
        lhs=(R-cosine)**2+sine*sine-(R-1)**2
        need(lhs==2*R*(1-cosine) and lhs>=0,'Fourier lower-bound algebra')
    return rows



def poly_add(p, q):
    out = list(p)+[Q()] * max(0,len(q)-len(p))
    for j,c in enumerate(q): out[j] += c
    return out


def square_integral(p, a=F(1), b=F(2)):
    value = integral(poly_mul(p,[c.conj() for c in p]), a,b)
    need(value.i == 0 and value.r >= 0,'polynomial squared norm')
    return value.r


def taper_cases():
    """Finite exact controls for the all-future completion proof.

    The forcing norm is exact. Young's inequality, not a sampled terminal
    trajectory, supplies the complete stable-output bound in the manuscript.
    """
    banks=[tuple((F(1,m),F(1)) for _ in range(m)) for m in range(1,7)]
    banks += [((F(1,4),F(1)),(F(1,4),F(-1))),
              ((F(1,8),F(2)),(F(1,8),F(2)),(F(1,4),F(-2))),
              ((F(1,10),F(0)),(F(1,5),F(1)),(F(1,5),F(-1)),(F(1,10),F(0)))]
    rows=[]
    for bank in banks:
        L=len(bank)
        # Chi(1+w)=1-integral_0^w t^L(1-t)^L dt / Beta(L+1,L+1).
        beta=F(math.factorial(L)**2,math.factorial(2*L+1))
        chi=[Q(1)]
        for j in range(L+1):
            coeff=-F((-1)**j*math.comb(L,j),L+j+1)/beta
            chi=poly_add(chi,[coeff*c for c in poly_pow([Q(-1),Q(1)],L+j+1)])
        need(peval(chi,Q(1))==Q(1) and peval(chi,Q(2))==Q(),'taper endpoints')
        for j in range(1,L+1):
            need(peval(deriv(chi,j),Q(1))==Q() and peval(deriv(chi,j),Q(2))==Q(),
                 'taper join derivative')
        # Zero-output dynamics A+bc^T has only imaginary diagonal eigenvalues.
        widths=[a for a,w in bank]
        for j in range(L):
            for k in range(L):
                Ajk=Q(-widths[k]) if k<j else Q(-widths[j],bank[j][1]) if k==j else Q()
                actual=Ajk+widths[k]
                expected=Q(0,bank[j][1]) if k==j else Q(widths[k]) if k>j else Q()
                need(actual==expected,'zero dynamics triangularization')
        inverse_norm2=math.prod((F(1,a*a) for a,w in bank),start=F(1))
        for omega in sorted(set(w for a,w in bank)):
            m=sum(w==omega for a,w in bank)
            shifted=[Q(1)]
            for a,w in bank: shifted=poly_mul(shifted,[Q(0,omega-w),Q(1)])
            need(all(shifted[j]==Q() for j in range(m)) and shifted[m]!=Q(),
                 'exact frequency multiplicity')
            for kind in ('top','mixed'):
                pol=[Q()]*m
                if kind=='top': pol[-1]=Q(1)
                else:
                    pol=[Q(F((-1)**j,j+1),F(j,2*j+3)) for j in range(m)]
                terms=[]
                for j,qj in enumerate(shifted):
                    if qj==Q():continue
                    for degree,pd in enumerate(pol):
                        if pd==Q():continue
                        need(j>=m and degree<m,'power budget')
                        qpoly=deriv([Q()]*degree+chi,j)
                        if not qpoly:continue
                        terms.append((degree-j,qj*pd,qpoly))
                C2=len(terms)*sum((coef.norm()*square_integral(poly)
                                   for power,coef,poly in terms),F(0))
                need(C2>0 and all(power<=-1 for power,coef,poly in terms),'finite taper budget')
                for R in (1,2,8,32):
                    forcing=[]
                    for power,coef,poly in terms:
                        forcing=poly_add(forcing,[coef*F(R)**power*c for c in poly])
                    norm2=R*square_integral(forcing)
                    need(norm2<=C2/R,'complete forcing budget failed')
                    rows.append({'length':L,'omega':packf(omega),'multiplicity':m,
                                 'mode':kind,'R':R,'forcing_norm2':packf(norm2),
                                 'forcing_budget':packf(C2/R),
                                 'whole_output_budget':packf(inverse_norm2*C2/R)})
    # Separate exact algebra for a matched compact wave, q=exp(-aT).
    for a,q in itertools.product((F(1,4),F(1),F(3)),(F(1,10),F(1,2),F(9,10))):
        prefix=(1-q*q)/(2*a)
        tail=(1-q)**2/(2*a)
        need(prefix+tail==(1-q)/a and prefix+tail<=1/a,'matched wave complete tail')
    return rows


def buffer_cases():
    rows=[]
    for beta,m in itertools.product((F(51,100),F(3,5),F(3,4),F(99,100)),(1,2,3)):
        alpha=beta-F(1,2);r=F(2);a=(1/beta+r)/2;b=(a+r)/2
        need(1<a<b<r and beta*a>1,'invalid direct-annulus buffer')
        need(beta-alpha+F(1,2)==1,'early-source exponential accounting')
        J=beta**(-m-1)+(m+1)*beta**(-m-2)
        norm2=F(math.factorial(m-1)**2,1)/((b**(2*m-1)-a**(2*m-1))/F(2*m-1))
        # Hypothetical frequency one only tests this rational constant formula.
        c=1/(4*(beta*beta+1)**2*J*J*norm2)
        need(c>0,'annular lower constant')
        rows.append({'beta':packf(beta),'m':m,'a':packf(a),'b':packf(b),
                     'leakage_exponent':packf(beta*a-1),'lower_constant_frequency_one':packf(c)})
    return rows


def factor(n):
    out={};p=2
    while p*p<=n:
        while n%p==0:
            out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1:out[n]=out.get(n,0)+1
    return out


def form_add(lhs,rhs,mult=F(1)):
    c,logs=lhs;d,rs=rhs;out=dict(logs)
    for prime,value in rs.items():
        out[prime]=out.get(prime,F(0))+mult*value
        if out[prime]==0:del out[prime]
    return c+mult*d,out


def filtered_prefix_form(coef,X):
    # Actual scalar a=1/2, omega=0. Exact rational + rational prime-log form.
    if X<=1:return F(0),{}
    stop=ceilf(X)-1; m=F(0);M=0; FF=F(0);EE=F(0);logs={}
    for k in range(1,stop+1):
        m+=F(coef[k],k);M+=coef[k];end=min(F(k+1),X)
        FF+=m*m*(end-k);EE+=M*M*(F(1,k)-1/end)
        ratio=end/k
        for sign,integer in ((1,ratio.numerator),(-1,ratio.denominator)):
            for prime,exponent in factor(integer).items():
                logs[prime]=logs.get(prime,F(0))+sign*exponent*m*M/2
                if logs[prime]==0:del logs[prime]
    return (FF+EE)/4,logs


def conv_int(a,b,N):
    out=[0]*(N+1)
    for j in range(1,N+1):
        if a[j]:
            for k in range(1,N//j+1):out[j*k]+=a[j]*b[k]
    return out


def prefix_energy(a):
    m=F(0);out=F(0)
    for n in range(1,len(a)):
        m+=F(a[n],n);out+=m*m
    return out


def dephasing_cases():
    rows=[]
    for X,S in itertools.product((16,32,64),((2,),(2,3),(2,3,5))):
        N=X-1;mu=mobius_sieve(N);mean=(F(0),{});cost=F(1)
        for prime in S:
            r=F(math.isqrt(prime*(1<<32)),1<<16)
            need(1<r and r*r<=prime,'prime-root lower enclosure')
            cost*=(r+1)/(r-1)
        base_energy=prefix_energy(mu)
        for signs in itertools.product((-1,1),repeat=len(S)):
            actual=[]
            for n in range(N+1):
                signature=1
                if n:
                    fs=factor(n)
                    for prime,eps in zip(S,signs):signature*=eps**fs.get(prime,0)
                actual.append(mu[n]*signature)
            forward=[0]*(N+1);inverse=[0]*(N+1);forward[1]=inverse[1]=1
            for prime,eps in zip(S,signs):
                rf=[0]*(N+1);ri=[0]*(N+1);rf[1]=ri[1]=1;power=prime;j=1
                while power<=N:
                    rf[power]=1-eps;ri[power]=(eps-1)*eps**(j-1)
                    power*=prime;j+=1
                forward=conv_int(forward,rf,N);inverse=conv_int(inverse,ri,N)
            need(conv_int(forward,mu,N)==actual,'Euler source forward identity')
            need(conv_int(inverse,actual,N)==mu,'Euler source inverse identity')
            e=prefix_energy(actual)
            need(e<=cost*cost*base_energy and base_energy<=cost*cost*e,'two-way finite source bound')
            mean=form_add(mean,filtered_prefix_form(actual,F(X)),F(1,1<<len(S)))
        rough=[mu[n] if n and math.gcd(n,math.prod(S))==1 else 0 for n in range(N+1)]
        expected=(F(0),{})
        for bits in itertools.product((0,1),repeat=len(S)):
            d=math.prod(prime for prime,bit in zip(S,bits) if bit)
            expected=form_add(expected,filtered_prefix_form(rough,F(X,d)),F(1,d))
        need(mean==expected,'filtered Parseval with shifted cutoffs')
        rows.append({'X':X,'primes':list(S),'signatures':1<<len(S),
                     'mean_rational':packf(mean[0]),
                     'mean_prime_logs':[[prime,packf(v)] for prime,v in sorted(mean[1].items())],
                     'rational_comparison_cost_upper':packf(cost)})
    return rows

def canon(x):
    return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()


def seal(body):return {'body':body,'sha256':hashlib.sha256(canon(body)).hexdigest()}


def reconstruct():
    a=adjoint_cases();r=resonance_cases();c=cascade_cases();n=native_cases();s=scalar_cases();t=taper_cases();buf=buffer_cases();dp=dephasing_cases()
    return seal({'schema':1,'status':'PROPOSED; RH AND NATIVE FILTER CAPTURE OPEN',
                 'parent':'99101457b32b6f10f4eda88ca998048404b860ea',
                 'scope':'finite exact controls; analytic limits are written proofs, not numerical certificates',
                 'native_phase_filters':'zero frequency only; no actual critical zero input',
                 'interval_denominator':PUBLISHED,
                 'coverage':{'adjoint_cases':len(a),'rational_resonances':len(r),
                             'cascade_cases':len(c),'native_panels':len(n),'native_max':511,
                             'scalar_cases':len(s),'rational_boundary_controls':72,
                             'interior_filter_controls':48,'taper_cases':len(t),'matched_wave_controls':9,'off_line_buffer_controls':len(buf),'filtered_dephasing_panels':len(dp),'twist_signatures':sum(v['signatures'] for v in dp)},
                 'taper_scope':'exact forcing norm; complete output bounded by proved Young inequality',
                 'adjoint':a,'resonances':r,'cascades':c,'native':n,'scalar':s,'tapers':t,'off_line_buffers':buf,'dephasing':dp})


def load(path):
    def pairs(xs):
        d={}
        for k,v in xs:
            need(k not in d,'duplicate JSON key');d[k]=v
        return d
    def bad(x):raise ValueError('noninteger JSON number')
    return json.loads(path.read_text(),object_pairs_hook=pairs,parse_float=bad,parse_constant=bad)


def authenticate():
    path=ROOT/'MANIFEST.json'
    need(path.is_file() and not path.is_symlink(),'missing manifest')
    files=load(path)
    need(type(files) is dict and bool(files),'empty manifest')
    actual={p.name for p in ROOT.iterdir()}
    need(actual==set(files)|{'MANIFEST.json'},'packet inventory mismatch')
    for name,sha in files.items():
        p=ROOT/name
        need(p.parent==ROOT and p.is_file() and not p.is_symlink(),'unsafe packet path')
        need(hashlib.sha256(p.read_bytes()).hexdigest()==sha,'file hash mismatch: '+name)


def accept(got,expected):
    need(type(got) is dict and set(got)=={'body','sha256'},'invalid envelope')
    need(got['sha256']==hashlib.sha256(canon(got['body'])).hexdigest(),'wrong semantic digest')
    need(canon(got)==canon(expected),'reconstructed payload mismatch')


def adverse(expected):
    def altered(fn):
        b=copy.deepcopy(expected['body']);fn(b);return seal(b)
    mutations=[lambda b:b.update(status='RH PROVED'),
               lambda b:b['coverage'].update(native_max=512),
               lambda b:b['coverage'].update(native_panels=True),
               lambda b:b['coverage'].update(native_max=511.0),
               lambda b:b['adjoint'].pop(),
               lambda b:b['native'][0].update(terminal_square=['0','1']),
               lambda b:b['cascades'][0].update(tail_control=['0','1']),
               lambda b:b['resonances'][0].update(annular_constant=['1','1']),
               lambda b:b.update(native_phase_filters='all actual zeros'),
               lambda b:b['native'][0]['output_dyadic'].__setitem__(0,0),
               lambda b:b['tapers'][0].update(whole_output_budget=['0','1']),
               lambda b:b.update(taper_scope='unfiltered input norm is uniformly bounded')]
    refused=0
    for fn in mutations:
        try:accept(altered(fn),expected)
        except ValueError:refused+=1
        else:raise ValueError('accepted resealed mutation')
    need(refused==len(mutations),'wrong refusal count')
    # Exercise the actual strict parser separately.
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/'bad.json';p.write_text('{"a":1,"a":2}')
        try:load(p)
        except ValueError:pass
        else:raise ValueError('duplicate accepted')
    return refused


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--emit',type=Path,help='unauthenticated producer output')
    ap.add_argument('--check',type=Path)
    ap.add_argument('--self-test',action='store_true')
    args=ap.parse_args()
    need(bool(args.emit)!=bool(args.check),'choose exactly one of --emit/--check')
    if args.check:authenticate()
    expected=reconstruct()
    if args.emit:
        args.emit.write_bytes(canon(expected)+b'\n')
        print('PRODUCED',expected['sha256'])
    else:
        accept(load(args.check),expected)
        print('PASS_EXACT_RBR26',expected['sha256'])
    if args.self_test:print('RESEALED_MUTATIONS_REJECTED',adverse(expected),'DUPLICATE_KEY_REJECTED')
    print(json.dumps(expected['body']['coverage'],sort_keys=True))

if __name__=='__main__':
    main()
