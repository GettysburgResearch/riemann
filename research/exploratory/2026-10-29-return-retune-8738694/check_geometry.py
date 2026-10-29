from fractions import Fraction as F
T=F(8738694,10**7);h=F(80599,100000);cap=F(619,10000);B=F(49283557,50000000);L=F(4503,2000);ell=F(11,3)-4*T;x=1+ell-h;y=h-2*ell;k=2*T-1;dm=F(19,25);dp=h+F(1,10**10);sg=T-(4+y-x)/6
checks={
'parameters': 0<ell and F(1,6)<ell<F(1,5) and ell<x<y<F(1,2) and x+y==1-ell and 0<2*x-y-ell and 1+3*ell-2*(x+y)<0 and sg==x/2+(y-x)/12,
'BoundsN':F(873,1000)<T<F(7,8) and F(793,1000)<h<F(806,1000) and F(440,1000)<y<F(467,1000) and F(1672,10000)<ell<F(175,1000) and F(6,100)<y/2-h*(F(17,50)-F(1,6))-F(1,50) and F(4,25)*x-F(3,20)-F(51,100)*y+F(67,100)*dp-F(3,20)*ell<=sg-F(1,250),
'schedule':0<=cap<F(1,5) and F(3,4)<dm<=dp and y<dm<2*y and 2<=L<=F(9,2) and 0<B<=1 and 0<=1-B/2-(F(9,2)-L/2)*cap and F(1,5)<ell/dp and k<=F(3,4),
'physical cap restricted': cap<=F(31,500),
'floor loss constructor': (F(26,10000)+F(1,100)+2+F(1,8)+F(1,8))/10**8<F(1,250),
}
for a,b in checks.items():print(a,b)
assert all(checks.values())
print('theta,h,ell,x,y,cap:',T,h,ell,x,y,cap)
