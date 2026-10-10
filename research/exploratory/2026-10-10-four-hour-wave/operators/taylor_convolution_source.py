"""Literal incomplete-gamma enclosure by an analytic/log expansion near zero.

Only strictly positive real lengths at most3/10 use this acceleration. Other
lengths use the unchanged reviewed hypergeometric source. See the separate
derivation; this helper requires independent review before acceptance.
"""
from math import factorial
from flint import arb,acb,acb_series,acb_poly,ctx
from source_convolution import ConvolutionSource
from enclose_analytic_upper import require


class TaylorConvolutionSource(ConvolutionSource):
    def __init__(self):
        super().__init__()
        n=65
        old_cap=ctx.cap
        ctx.cap=n+1
        x=acb_series([0,1],prec=n+1)
        ex=(-x).exp()
        quotient=acb_series([-ex[k+1] for k in range(n)],prec=n)
        xx=acb_series([0,1],prec=n)
        plus=(self.b*xx).exp();minus=(-self.b*xx).exp()
        cc=(plus+minus)/2;ss=(plus-minus)/2
        aa=(-xx/2).exp()/6+cc*(1+(-xx).exp()).log()/3+ss*quotient.log()/3
        bb=ss/3
        require(aa.prec>=n and bb.prec>=n,'full local gamma series precision')
        self.taylor_a=[aa[k] for k in range(n)]
        self.taylor_b=[bb[k] for k in range(n)]
        ctx.cap=old_cap
        self.taylor_cache={}
        self.exp_factorials={e:factorial(e+1) for e in(128,256,512)}
        require((arb(9)/20).exp()<2,'real exponential on0<=x<=.3 less than2')
        require(arb(1)/6+self.log2/3<arb(2)/5,'literal gamma supremum below.4')

    def series_polynomials(self,key,degree,exponential_degree):
        cache_key=(key,degree,exponential_degree)
        if cache_key not in self.taylor_cache:
            z=self.val(key)
            n=degree+exponential_degree+1
            old_cap=ctx.cap
            ctx.cap=n
            x=acb_series([0,1],prec=exponential_degree+1)
            ee=(z*x).exp()
            ep=acb_series([ee[k] for k in range(exponential_degree+1)],prec=n)
            aa=acb_series(self.taylor_a[:degree+1],prec=n)*ep
            bb=acb_series(self.taylor_b[:degree+1],prec=n)*ep
            require(aa.prec>=n and bb.prec>=n,'full product series precision')
            plain=acb_poly([aa[k]/(k+1)-bb[k]/((k+1)**2) for k in range(n)])
            logarithmic=acb_poly([bb[k]/(k+1) for k in range(n)])
            cutoff={128:arb(1)/100,256:arb(1)/10,512:arb(3)/10}[exponential_degree]
            zr=z.abs_upper()*cutoff
            exp_error=zr.exp()*zr**(exponential_degree+1)/self.exp_factorials[exponential_degree]
            require(exp_error<1,'finite exponential Taylor error below1 on full tier')
            denominator=degree+2
            gamma_error=3*cutoff**denominator/(1-cutoff)*(arb(8)/denominator+2*(-cutoff.log()/denominator+arb(1)/(denominator**2)))
            error=gamma_error+arb(2)/5*cutoff*exp_error
            require(error>0,'positive complete local source error')
            delta=arb(0,error.upper())
            self.taylor_cache[cache_key]=(plain,logarithmic,delta)
            ctx.cap=old_cap
        return self.taylor_cache[cache_key]

    def gamma_incomplete(self,key,a):
        if (key[0]=='r' and abs(key[1])>3) or not(
                a.imag.is_zero() and a.real>0 and a.real<=arb(3)/10):
            return super().gamma_incomplete(key,a)
        degree,exponential_degree=(32,128) if a.real<=arb(1)/100 else(
            (64,256) if a.real<=arb(1)/10 else(64,512))
        plain,logarithmic,delta=self.series_polynomials(key,degree,exponential_degree)
        value=a*(plain(a)+a.log()*logarithmic(a))
        result=value+acb(delta,delta)
        require(result.is_finite(),'finite literal local gamma enclosure')
        return result
