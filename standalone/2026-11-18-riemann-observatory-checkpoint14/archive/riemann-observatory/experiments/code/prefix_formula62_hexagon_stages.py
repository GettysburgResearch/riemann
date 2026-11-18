"""Exact endpoint margins for equations (8)–(13) and Section 8.7.

Uses the fixed positive cutoff padding p and rho_high = p. Both
polynomial branches of margin 13 are checked independently.
"""
from fractions import Fraction as Q
from math import ceil, floor
R0=Q(311,400)
dR=Q(11,60000)
dz=Q(1,25000000)
p=Q(1,10**7)
a0=a1=z=Q(0)
mins=[None]*15
intervals = []
lines = []
for j in range(240):
    R=R0-j*dR
    D=Q(1,2)-a1
    wb=(R/2+z-a0)/D
    k=max(Q(45457,125000),Q(ceil(10**6*((5*wb/4-Q(5,6))/(3*wb/2-(1+R)/2-z)+Q(18,10**5))),10**6))
    F=Q(5,6)-(Q(5,4)-3*k/2)*wb-k*(1+R)/2-k*z
    endpoint_values = []
    for r in (R,R-dR):
        H=r/R
        u=(1-H)/6
        Y=H*z+(1/k-2)*u
        endpoint_values.append((r, Y - dz - p))
        S=(1-r)/2+Y
        s=S-u
        wp=wb+u*(1/k-Q(4,3))/(D*H)+p
        base=Q(5,6)-Q(3,4)*wp
        margins=[
            H*F-p,Q(137,1000)-S,Q(7,50)-S/H,Q(9,10)-r-S-4*u,Q(91,100)-r-S-4*u,
            Q(5,6)+Q(21,250)-r-S-3*u-Q(1,100),3*H-2*r-8*s-Q(1,5),
            r/2-s-Q(1,5),r/2-s-32*(Q(5,6)-k)*u/(k*k*D)-Q(1,10),
            H+u-H/6-Q(1,15)-3*r/4-s-Q(3,100),wb+p-Q(2,3),Q(79,100)-wp,
            base,base-Q(3,4)*((1-wp)/2+a0-a1*wp),Q(79,100)-r-(2+Q(1,10**11))*u]
        for i, t in enumerate(margins):
            entry=(t,j,r==R)
            mins[i]=entry if mins[i] is None else min(mins[i],entry)
        assert 0 <= a1 <= Q(2, 5) and a0-a1*R <= z and wb >= R
        assert 0 <= u <= Q(1, 10**4) and 0 < k < Q(1, 2)
        assert all(t > 0 for t in margins), (j, r, margins)
    znext=Q(floor(10**10*(Y-dz)),10**10)
    a1=(Y-z)/dR
    a0=Y-dz-2*p+a1*(R-dR)
    assert znext >= 0
    z=znext
    intervals.extend(endpoint_values)
    lines.append((a0, a1))
print('final', z)
for i,(v,j,r) in zip([1,2,3,4,5,6,7,8,9,10,11,12,'13a','13b',14],mins):
    print(i,float(v),j,'start R' if r else 'end r')

minimum_line_margin = min(
    available - (intercept - slope * radius)
    for intercept, slope in lines
    for radius, available in intervals
)
assert minimum_line_margin > 0
print("minimum global supporting-line margin", float(minimum_line_margin))
