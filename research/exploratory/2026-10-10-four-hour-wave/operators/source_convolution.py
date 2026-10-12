"""Directed closed formulas for W, its primitive, and F of exponential tests.

These identities are exploratory until independently reviewed.  Hypergeometric
flags abc and bc encode the exact parameter relations c-a-b=0 and c-b=1.
Every requested incomplete integral must stay in the half plane Re(length)>0.
"""

from flint import arb,acb

from enclose_analytic_upper import Source, f, require


class ConvolutionSource(Source):
    def __init__(self):
        super().__init__()
        self.agamma={}
        self.pi=arb.pi()
        self.gprimitive0=(7-self.pi-4*self.log2)/9
        self.w0=arb(1)/2+self.cb+arb(1)/6+self.log2/3-self.p2/self.b
        self.h1=self.primitive(acb(1),True)
        self.w1=self.w(acb(1),True)

    def gamma_parts(self,a):
        t=(-a).exp()
        logplus=(1+t).log()
        logminus=(1-t).log()
        atanh_t=(logplus-logminus)/2
        sb=(-self.b*a).exp()*atanh_t
        smb=-(self.b*a).exp()*((1-t*t).log()+t*t)/2
        return t,sb,smb,atanh_t

    def gamma_incomplete(self,key,a):
        require(a.real>0,('incomplete gamma positive real length',str(a)))
        z=self.val(key)
        b=self.b
        if key not in self.agamma:
            self.agamma[key]=self.a(z,key)[0]
        av=self.agamma[key]
        t,sb,smb,atanh_t=self.gamma_parts(a)
        slope=(sb-smb)/(2*b)
        if key==('r',3):
            db=(-b*a).exp()*(t.polylog(2)-(-t).polylog(2))/2
            expo=(db-slope)/(2*b)
        elif key==('r',-3):
            dmb=(b*a).exp()*((t*t).polylog(2)-t*t)/4
            expo=(dmb-slope)/(-2*b)
        else:
            if key==('r',1):
                sz=-(-a/2).exp()*(1-t*t).log()/2
            elif key==('r',-1):
                sz=(a/2).exp()*(atanh_t-t)
            else:
                alpha=acb(arb(5)/4)-z/2
                lerch=(t*t).hypgeom_2f1(1,alpha,alpha+1,abc=True,bc=True)/alpha
                sz=(-arb(5)*a/2).exp()*lerch/2
            linear=((z+b)*sb+(b-z)*smb)/(2*b)
            expo=(sz-linear)/(z*z-b*b)
        value=av-(z*a).exp()*expo
        require(value.is_finite(),('finite incomplete gamma',key,str(a)))
        return value

    def partial(self,key,a,prime_active):
        z=self.val(key)
        b=self.b
        zero_c=key==('r',-1)
        zero_b=key==('r',3)
        zero_minus_b=key==('r',-3)
        value=a*f((z+arb(1)/2)*a,zero_c)/2+self.cb*a*f((z-b)*a,zero_b)
        value-=self.p2*a*(f((z+b)*a,zero_minus_b)+f((z-b)*a,zero_b))/(2*b)
        value+=self.gamma_incomplete(key,a)
        if prime_active:
            width=a-self.log2
            value+=self.q2*(z*self.log2).exp()*width*(f((z+b)*width,zero_minus_b)
                                                        -f((z-b)*width,zero_b))/(2*b)
        require(value.is_finite(),('finite partial source',key,str(a)))
        return value

    def w(self,x,prime_active):
        b=self.b
        t=(-x).exp()
        gamma=(-x/2).exp()/6+(b*x).cosh()*(1+t).log()/3+(b*x).sinh()*(1-t).log()/3
        value=(x/2).exp()/2+self.cb*(-b*x).exp()+gamma-(self.p2/b)*(b*x).cosh()
        if prime_active:
            value+=(self.q2/b)*(b*(x-self.log2)).sinh()
        return value

    def primitive(self,x,prime_active):
        b=self.b
        r=(-x/2).exp()
        t=(-x).exp()
        atanh_r=((1+r).log()-(1-r).log())/2
        atanh_t=((1+t).log()-(1-t).log())/2
        # arctan(r) is analytic for |r|<1 on the chosen positive half plane.
        atan_r=((1+acb(0,1)*r).log()-(1-acb(0,1)*r).log())/(2*acb(0,1))
        gtail=-arb(4)/9*(atanh_r+atan_r-2*r)+arb(2)/9*((-b*x).exp()*atanh_t
                -(b*x).exp()*((1-t*t).log()+t*t)/2)
        value=(x/2).expm1()-(self.cb/b)*(-b*x).expm1()+self.gprimitive0-gtail
        value-=(self.p2/b**2)*(b*x).sinh()
        if prime_active:
            value+=(self.q2/b**2)*((b*(x-self.log2)).cosh()-1)
        return value

    def beta_f(self,key,t,left_active,right_active,endpoint=None):
        beta=self.val(key)
        e=beta.exp()
        t1,_=self.laplace(key)
        if endpoint==0:
            return -beta*t1-self.w0+e*self.w1
        tm1,_=self.laplace((key[0],-key[1]))
        if endpoint==1:
            return (-beta+arb(1)/(4*beta))*e*tm1-self.w1+e*self.w0+arb(1)/(4*beta)*(-t1+(e-1)*self.h1)
        left=self.partial((key[0],-key[1]),t,left_active)
        right=self.partial(key,1-t,right_active)
        k=(beta*t).exp()*(left+right)
        wl=self.w(t,left_active)
        wr=self.w(1-t,right_active)
        hl=self.primitive(t,left_active)
        hr=self.primitive(1-t,right_active)
        value=(-beta+arb(1)/(4*beta))*k-wl+e*wr+arb(1)/(4*beta)*(-t1-hl+e*(self.h1-hr))
        require(value.is_finite(),('finite F',key,str(t)))
        return value

    def basis_f(self,t,removed,trial,left_active,right_active,endpoint=None,bounds=False):
        sins=[]
        for j in range(1,removed+trial+1):
            value=self.beta_f(('i',j),t,left_active,right_active,endpoint)
            # At real points F[sin(j*pi*t)]=Im F[exp(i*j*pi*t)].  On a
            # conjugation-symmetric complex box, |F[sin]| is bounded by the
            # maximum absolute value of F[exp(i*j*pi*t)] on that box.
            sins.append(value.abs_upper() if bounds else value.imag)
        ep=self.beta_f(('r',1),t,left_active,right_active,endpoint)
        em=self.beta_f(('r',-1),t,left_active,right_active,endpoint)
        cb=(self.beta_f(('r',3),t,left_active,right_active,endpoint)
             +self.beta_f(('r',-3),t,left_active,right_active,endpoint))/2
        middle=[ep.abs_upper(),em.abs_upper(),cb.abs_upper()] if bounds else [ep.real,em.real,cb.real]
        return sins[:removed]+middle+sins[removed:]
