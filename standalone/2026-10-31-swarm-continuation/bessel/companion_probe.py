"""Ordinary binary64 source quadratures; exploratory, not interval evidence."""
import math, cmath, json
from pathlib import Path
from scipy.integrate import quad
from scipy.optimize import brentq

def phi_real_half(t):
    y=math.exp(t)
    if y>250:return 0.0
    return sum((4*math.pi**2*n**4*y*y-6*math.pi*n*n*y)*y**.25*math.exp(-math.pi*n*n*y) for n in range(1,10))

def phi_imag_half(theta):
    if theta>=math.pi/2:return 0.0
    y=cmath.exp(1j*theta)
    if theta<1.1:
        ans=sum((4*math.pi**2*n**4*y*y-6*math.pi*n*n*y)*cmath.exp(1j*theta/4-math.pi*n*n*y) for n in range(1,22))
    else:
        eps=y-1j
        d1=0j;d2=0j
        for k in range(15):
            p=math.pi*(k+.5)**2
            term=2*eps**(-.5)*cmath.exp(-p/eps)
            ell1=-1/(2*eps)+p/(eps*eps)
            ell2=1/(2*eps*eps)-2*p/(eps**3)
            d1+=term*ell1;d2+=term*(ell1*ell1+ell2)
        ans=cmath.exp(1j*theta/4)*(2*y*y*d2+3*y*d1)
    return ans.real

def X(E):
    b=math.sqrt(E)
    return quad(lambda t:phi_real_half(t)*math.cos(b*t),0,4,epsabs=2e-15,epsrel=2e-13,limit=300)[0]

def Xp(E):
    b=math.sqrt(E)
    return quad(lambda t:-phi_real_half(t)*t*math.sin(b*t)/(2*b),0,4,epsabs=2e-15,epsrel=2e-13,limit=300)[0]

def J(E):
    b=math.sqrt(E)
    angular=quad(lambda theta:phi_imag_half(theta)*(math.cosh(b*theta)+math.cosh(b*(math.pi-theta))),0,math.pi/2,epsabs=1e-8,epsrel=3e-13,limit=500)[0]
    sine=quad(lambda t:phi_real_half(t)*math.sin(b*t),0,4,epsabs=2e-15,epsrel=2e-13,limit=300)[0]
    return (angular-math.sinh(math.pi*b)*sine)/math.pi,angular/math.pi,-math.sinh(math.pi*b)*sine/math.pi

if __name__=='__main__':
    roots=[]
    # These values only seed narrow real brackets. No complete zero census is made.
    # Higher rows were deliberately removed because binary64 cancellation became
    # severe enough that this quadrature was no longer a useful diagnostic.
    known_z=[14.134725141734693,21.022039638771555,25.01085758014569]
    for z in known_z:
        guess=z*z/4
        e=brentq(X,guess-.05,guess+.05,xtol=2e-12)
        j,angular,sine=J(e);xp=Xp(e)
        row={'E':e,'z':2*math.sqrt(e),'Xprime':xp,'J':j,'angular':angular,'sine':sine,'J_over_Xprime':j/xp}
        roots.append(row);print(row,flush=True)
    nu=.25
    angular=quad(lambda theta:phi_imag_half(theta)*(math.cos(nu*theta)+math.cos(nu*(math.pi-theta))),0,math.pi/2,epsabs=2e-12,epsrel=2e-11,limit=500)[0]
    real=quad(lambda t:phi_real_half(t)*math.sinh(nu*t),0,4,epsabs=2e-15,epsrel=2e-13,limit=300)[0]
    measured=(angular+math.sin(math.pi*nu)*real)/math.pi
    exact=-1/(2*math.sqrt(2)*math.pi)
    control={'energy':-1/16,'quadrature':measured,'exact_special_value_as_binary64':exact,'absolute_difference':abs(measured-exact)}
    Path(__file__).with_name('COMPANION_PROBE.json').write_text(json.dumps({'scope':'ordinary binary64 quadrature with finite integration and theta cutoffs; not directed or certified; only the first three diagnostic rows are retained','special_value_control':control,'rows':roots},indent=2)+'\n')
