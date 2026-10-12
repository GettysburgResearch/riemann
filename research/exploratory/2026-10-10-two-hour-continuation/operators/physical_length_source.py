"""Full-source physical-coordinate adapter at exact length21/20.
Old reviewed helpers remain immutable; new formulas require independent audit.
"""
from pathlib import Path
import sys
OLD=Path(__file__).resolve().parents[2]/"2026-10-10-four-hour-wave"/"operators"
sys.path.insert(0,str(OLD))
from flint import arb,acb,arb_mat,ctx
from taylor_convolution_source import TaylorConvolutionSource
from enclose_analytic_upper import Source,f,fp,basis,block,transpose,cholesky,identity
from enclose_analytic_upper import require,positive_ldl

L_NUM=21
L_DEN=20

class LengthSource(Source):
    def __init__(self,length):
        self.length=length
        super().__init__()
        lam0=2*(self.terms+1)+arb(1)/2
        self.gamma_error=((self.b-lam0)*length).exp()/((lam0-self.b)**2*lam0*(1-(-2*length).exp()))
        self.gamma_derivative_error=self.gamma_error*(length+1/(lam0-self.b))

    def val(self,key):
        return acb(arb(key[1])/2) if key[0]=='r' else acb(0,arb.pi()*key[1]/self.length)

    def laplace(self,key):
        if key in self.cache:return self.cache[key]
        z=self.val(key);b=self.b;L=self.length
        av,ap=self.a(z,key);expo=acb(0);expop=acb(0)
        for j in range(1,self.terms+1):
            lam=2*j+arb(1)/2;base=(-lam*L).exp()/(lam*lam-b*b)
            expo+=base/(lam-z);expop+=base/(lam-z)**2
        delta=arb(0,self.gamma_error.upper());deltap=arb(0,self.gamma_derivative_error.upper())
        gv=av-(z*L).exp()*expo+acb(delta,delta)
        gp=ap-(z*L).exp()*(L*expo+expop)+acb(deltap,deltap)
        zp=key==('r',-3);zm=key==('r',3);zc=key==('r',-1)
        value=L*f((z+arb(1)/2)*L,zc)/2+self.cb*L*f((z-b)*L,zm)+gv
        value-=self.p2*L*(f((z+b)*L,zp)+f((z-b)*L,zm))/(2*b)
        deriv=L*L*fp((z+arb(1)/2)*L,zc)/2+self.cb*L*L*fp((z-b)*L,zm)+gp
        deriv-=self.p2*L*L*(fp((z+b)*L,zp)+fp((z-b)*L,zm))/(2*b)
        width=L-self.log2;factor=(z*self.log2).exp()*width
        vplus=f((z+b)*width,zp);vminus=f((z-b)*width,zm)
        value+=self.q2*factor*(vplus-vminus)/(2*b)
        deriv+=self.q2*factor*(self.log2*(vplus-vminus)+width*(fp((z+b)*width,zp)-fp((z-b)*width,zm)))/(2*b)
        require(value.is_finite() and deriv.is_finite(),'finite length-family transform')
        self.cache[key]=value,deriv;return value,deriv

    def double(self,alpha,beta):
        ta,tpa=self.laplace(alpha);tb,tpb=self.laplace(beta)
        if alpha[0]==beta[0] and alpha[1]+beta[1]==0:return self.length*(ta+tb)-tpa-tpb
        tma,_=self.laplace((alpha[0],-alpha[1]));tmb,_=self.laplace((beta[0],-beta[1]))
        s=self.val((alpha[0],alpha[1]+beta[1])) if alpha[0]==beta[0] else self.val(alpha)+self.val(beta)
        return ((s*self.length).exp()*(tma+tmb)-ta-tb)/s

def build_length(length,removed=7,trial=100):
    source=LengthSource(length);funcs=basis(trial,removed);n=len(funcs);dim=removed+3
    q=arb_mat(n,n);gram=arb_mat(n,n)
    for i in range(n):
        for j in range(i,n):
            qv=acb(0);gv=acb(0)
            for a,ca in funcs[i]:
                for beta,cb in funcs[j]:
                    qv+=ca*cb*source.double(a,beta)
                    zero=a[0]==beta[0] and a[1]+beta[1]==0
                    z=source.val((a[0],a[1]+beta[1])) if a[0]==beta[0] else source.val(a)+source.val(beta)
                    gv+=ca*cb*length*f(z*length,zero)
            require(qv.imag.contains(0) and gv.imag.contains(0),'real length-family matrix symmetry')
            q[i,j]=q[j,i]=source.b*qv.real;gram[i,j]=gram[j,i]=gv.real
    ei=range(dim);hi=range(dim,n);orth=transpose(cholesky(block(gram,ei,ei))).inv()
    qee=transpose(orth)*block(q,ei,ei)*orth
    constraints=transpose(orth)*block(gram,ei,hi);qeh=transpose(orth)*block(q,ei,hi)
    qvv=block(q,hi,hi)-transpose(constraints)*qeh-transpose(qeh)*constraints+transpose(constraints)*qee*constraints
    qve=transpose(qeh)-transpose(constraints)*qee;correction=qvv.solve(qve)
    u=qee-transpose(qve)*correction;u=(u+u.transpose())/2
    top=orth*(identity(dim)+constraints*correction);coeff=arb_mat(n,dim)
    for i in range(dim):
        for j in range(dim):coeff[i,j]=top[i,j]
    for i in range(trial):
        for j in range(dim):coeff[i+dim,j]=-correction[i,j]
    try:
        pivots=positive_ldl(u,arb('1e-10'))
    except ArithmeticError:
        pivots=[]
    return source,u,coeff,pivots

class PhysicalSource(TaylorConvolutionSource):
    def __init__(self):
        self.length=arb(L_NUM)/L_DEN
        super().__init__()
        lam0=2*(self.terms+1)+arb(1)/2
        self.gamma_error=((self.b-lam0)*self.length).exp()/((lam0-self.b)**2*lam0*(1-(-2*self.length).exp()))
        self.gamma_derivative_error=self.gamma_error*(self.length+1/(lam0-self.b))
        self.h1=self.primitive(acb(self.length),True)
        self.w1=self.w(acb(self.length),True)
    def val(self,key):
        return acb(arb(key[1])/2) if key[0]=='r' else acb(0,arb.pi()*key[1]/self.length)
    def laplace(self,key):
        return LengthSource.laplace(self,key)
    def double(self,alpha,beta):
        return LengthSource.double(self,alpha,beta)
    def beta_f(self,key,t,left_active,right_active,endpoint=None):
        beta=self.val(key);L=self.length;e=(beta*L).exp()
        tl,_=self.laplace(key)
        if endpoint==0:return -beta*tl-self.w0+e*self.w1
        tml,_=self.laplace((key[0],-key[1]))
        if endpoint==1:
            return (-beta+arb(1)/(4*beta))*e*tml-self.w1+e*self.w0+arb(1)/(4*beta)*(-tl+(e-1)*self.h1)
        left=self.partial((key[0],-key[1]),t,left_active)
        right=self.partial(key,L-t,right_active)
        k=(beta*t).exp()*(left+right)
        wl=self.w(t,left_active);wr=self.w(L-t,right_active)
        hl=self.primitive(t,left_active);hr=self.primitive(L-t,right_active)
        value=(-beta+arb(1)/(4*beta))*k-wl+e*wr+arb(1)/(4*beta)*(-tl-hl+e*(self.h1-hr))
        require(value.is_finite(),('physical F finite',key,str(t)))
        return value
    def moment(self,key,test):
        beta=self.val(key);L=self.length
        tb,_=self.laplace(key);tmb,_=self.laplace((key[0],-key[1]));k0=tb;kL=(beta*L).exp()*tmb
        d0=self.double(('r',0),key)
        if test==0:
            t0,tp0=self.laplace(('r',0))
            da=((beta*L).exp()*(L*(t0+tmb)-tp0)-tp0-d0)/beta
            return k0-kL+arb(1)/4*(L*d0-da)
        if isinstance(test,int):
            nu=arb.pi()*test/L
            ds=(self.double(('i',test),key)-self.double(('i',-test),key))/(2*acb(0,1))
            return k0-(-1)**test*kL-(nu+arb(1)/(4*nu))*ds
        require(test=='sinh','physical moment test')
        def ex(sign):
            a=self.val(('r',3*sign));e=(a*L).exp()
            return k0-e*kL+(a-arb(1)/(4*a))*self.double(('r',3*sign),key)+arb(1)/(4*a)*e*d0
        return (ex(1)-ex(-1))/2
    def basis_moment(self,test,removed,trial):
        sin=[self.moment(('i',j),test).imag for j in range(1,removed+trial+1)]
        ep=self.moment(('r',1),test);em=self.moment(('r',-1),test)
        ch=(self.moment(('r',3),test)+self.moment(('r',-3),test))/2
        require(ep.imag.contains(0) and em.imag.contains(0) and ch.imag.contains(0),'physical moment real symmetry')
        return sin[:removed]+[ep.real,em.real,ch.real]+sin[removed:]

def projection_gram(removed,source):
    L=source.length;b=source.b;n=removed+2;g=arb_mat(n,n);g[0,0]=L
    for j in range(1,removed+1):g[j,j]=L/2
    g[0,n-1]=g[n-1,0]=((b*L).cosh()-1)/b
    for j in range(1,removed+1):
        cross=b*((-1)**j*(b*L).cosh()-1)/(b*b+(arb.pi()*j/L)**2)
        g[j,n-1]=g[n-1,j]=cross
    g[n-1,n-1]=(2*b*L).sinh()/(4*b)-L/2
    positive_ldl(g)
    return g
