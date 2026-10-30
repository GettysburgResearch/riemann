from fractions import Fraction as F
t=F(43643617,50000000); d=F(9,20); p=F(1,2); B=F(96232839,100000000); L=F(3853,2000); PB=F(49283557,50000000); PL=F(4503,2000); ell=F(11,3)-4*t; k=2*t-1; V=F(5,6)-d

def nvals():
 dd=3-p-2*p/(3*k);aa=2*(1-p)*(1-p/(3*k)); J=V*dd+d*aa;N=(1-d)*J+d*aa*V/2
 out=[('old',N/J)]
 for name,b,l,z,ic in [('C',B,L,F(9999,100000),False),('capC',B,L,F(9999,100000),True),('weakC7',B-F(7,4000),L,F(9999,100000),False),('capP',PB,PL,F(31,500),True)]:
  dd=3-p if ic else 3-p-4*p/l;aa=2 if ic else 2-4*p/l;c0=1-2*p*z if ic else 1-2*p*b/l;U=(1-p)*c0;J=V*dd+d*(1-p)*aa;N=(1-d)*J+V*d*U;out.append((name,N/J))
 return out
for name,n in nvals():
  def f(h):
    y=h-2*ell; dist=h+F(1,10**10); C=F(31,500)*dist
    return F(1,2)+F(13,75)*h-y/2-ell/2-F(9,100)*dist+d/2+d*p*(ell-C/2)+F(3,4)*dist*n-t
  a,b=f(F(793,1000)),f(F(806,1000)); assert min(a,b)>0
  print(name, 'lower endpoint gaps:',float(a),float(b))

h=F(793,1000); dist=h+F(1,10**10); cap=F(9999,100000)
dd=3-p; J=V*dd+d*(1-p)*2
def gap(z, numerator_fraction):
  U=(1-p)*(1-2*p*z); N=(1-d)*J+V*d*U
  y=h-2*ell; C=numerator_fraction*dist
  return (F(1,2)+F(13,75)*h-y/2-ell/2-F(9,100)*dist+d/2
          +d*p*(ell-C/2)+F(3,4)*dist*N/J-t)
z_star=cap+gap(cap,F(31,500))/(gap(cap,F(31,500))-gap(cap+1,F(31,500)))
c_star=F(31,500)+gap(cap,F(31,500))/(gap(cap,F(31,500))-gap(cap,F(31,500)+1))
lambda_max=(1-2*F(377,1000))/z_star
assert z_star>F(18,100) and c_star>F(9,100) and lambda_max<F(14,10)
print('optimistic threshold z:',float(z_star))
print('maximum lambda for B<=1, m>=.377:',float(lambda_max))
print('optimistic numerator fraction threshold:',float(c_star))
y=h-2*ell
actual_C_max=min(F(31,500)*dist,(2*y-(2-PB)*dist)/PL)
print('actual physical C cap, h=.793:',float(actual_C_max))
print('required C, h=.793:',float(c_star*dist))
assert actual_C_max<c_star*dist
required_physical_B=2-2*y/dist+PL*c_star
max_physical_lambda_if_B_one=(2*y/dist-1)/c_star
print('physical B required at existing lambda:',float(required_physical_B))
print('physical lambda cap if B<=1:',float(max_physical_lambda_if_B_one))
assert required_physical_B>1 and max_physical_lambda_if_B_one<F(13,10)
