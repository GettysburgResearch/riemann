#!/usr/bin/env python3
"""Exact Gaussian-rational algebra checks for passive boundary realizations."""
from fractions import Fraction as Q
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
class Z:
 __slots__=('a','b')
 def __init__(self,a=0,b=0):
  if isinstance(a,Z):self.a,self.b=a.a,a.b
  else:self.a,self.b=Q(a),Q(b)
 def __add__(x,y):
  y=Z(y);return Z(x.a+y.a,x.b+y.b)
 __radd__=__add__
 def __neg__(x):return Z(-x.a,-x.b)
 def __sub__(x,y):return x+-Z(y)
 def __rsub__(x,y):return Z(y)+-x
 def __mul__(x,y):
  y=Z(y);return Z(x.a*y.a-x.b*y.b,x.a*y.b+x.b*y.a)
 __rmul__=__mul__
 def __truediv__(x,y):
  y=Z(y);s=y.a*y.a+y.b*y.b;assert s
  return Z((x.a*y.a+x.b*y.b)/s,(x.b*y.a-x.a*y.b)/s)
 def conj(x):return Z(x.a,-x.b)
 def __eq__(x,y):
  y=Z(y);return x.a==y.a and x.b==y.b
 def __repr__(x):return f'({x.a})+({x.b})i'
i=Z(0,1)
def zeros(n,m):return [[Z() for _ in range(m)] for _ in range(n)]
def eye(n):return [[Z(a==b) for b in range(n)] for a in range(n)]
def dag(A):return [[A[r][c].conj() for r in range(len(A))] for c in range(len(A[0]))]
def mm(A,B):return [[sum((A[r][j]*B[j][c] for j in range(len(B))),Z()) for c in range(len(B[0]))] for r in range(len(A))]
def add(A,B):return [[a+b for a,b in zip(ar,br)] for ar,br in zip(A,B)]
def scale(z,A):return [[Z(z)*a for a in ar] for ar in A]
def sub(A,B):return add(A,scale(-1,B))
def inverse(A):
 n=len(A);A=[list(row)+list(er) for row,er in zip(A,eye(n))]
 for c in range(n):
  p=next(r for r in range(c,n) if A[r][c]!=0);A[c],A[p]=A[p],A[c]
  q=A[c][c];A[c]=[x/q for x in A[c]]
  for r in range(n):
   if r!=c:
    q=A[r][c];A[r]=[x-q*y for x,y in zip(A[r],A[c])]
 return [row[n:] for row in A]
def det(A):
 if len(A)==1:return A[0][0]
 if len(A)==2:return A[0][0]*A[1][1]-A[0][1]*A[1][0]
 raise ValueError('Only small determinant needed')
def psd2(A):
 assert A==dag(A)
 assert all(A[j][j].b==0 and A[j][j].a>=0 for j in range(len(A)))
 if len(A)==2:assert det(A).b==0 and det(A).a>=0

def check_model(Om,G,k):
 n=len(Om);E=len(G);Gram=mm(dag(G),G)
 T=add(sub(scale(k,eye(n)),Om),scale(i/2,Gram));R=inverse(T)
 S=sub(eye(E),scale(i,mm(mm(G,R),dag(G))))
 assert mm(dag(S),S)==eye(E)
 Sprime=scale(i,mm(mm(G,mm(R,R)),dag(G)))
 QS=scale(-i,mm(dag(S),Sprime))
 target=mm(mm(G,mm(dag(R),R)),dag(G))
 assert QS==target;psd2(QS)
 return S,T
# Noncommuting rank-one factors on E=2, M=3; all coordinates Gaussian rational.
G=[[Z(1),Z(Q(6,5)),Z(0)],[Z(0),Z(Q(8,5)),Z(1)]]
E=2;M=3;centers=[Q(0),Q(1),Q(3)];Gram=mm(dag(G),G)
Om=zeros(M,M)
for j in range(M):
 for t in range(M):Om[j][t]=Z(centers[j]) if j==t else (i/2 if j>t else -i/2)*Gram[j][t]
assert Om==dag(Om)
widths=[Gram[j][j].a/2 for j in range(M)];assert widths==[Q(1,2),Q(2),Q(1,2)]
projections=[]
for j in range(M):
 col=[[G[a][j]] for a in range(E)];P=scale(1/(2*widths[j]),mm(col,dag(col)))
 assert mm(P,P)==P and P==dag(P);projections.append(P)
assert mm(projections[0],projections[1])!=mm(projections[1],projections[0])
grid=[Q(n,4) for n in range(-8,21)]
for k in grid:
 S,T=check_model(Om,G,k)
 assert all(T[j][t]==0 for j in range(M) for t in range(j))
 product=eye(E);bd=Z(1)
 for j in range(M):
  b=Z(k-centers[j],-widths[j])/Z(k-centers[j],widths[j]);bd=bd*b
  product=mm(product,add(eye(E),scale(b-1,projections[j])))
 assert S==product and det(S)==bd
# Arbitrary Hermitian model not prepackaged as the above cascade.
Om2=[[Z(0),Z(1)],[Z(1),Z(2)]];G2=[[Z(1),Z(1)],[Z(0),Z(1)]]
for k in grid:check_model(Om2,G2,k)
# Explicit dark state: full inverse singular at k=2, visible transfer stays defined.
Om_dark=[[Z(1),Z(0)],[Z(0),Z(2)]];G_dark=[[Z(1),Z(0)]]
Tfull=add(sub(scale(2,eye(2)),Om_dark),scale(i/2,mm(dag(G_dark),G_dark)))
assert det(Tfull)==0
Svis,_=check_model([[Z(1)]],[[Z(1)]],Q(2));assert mm(dag(Svis),Svis)==eye(1)
# One port can hide more than one visible state: rankG=1 but degreeM=2.
Om_oneport=[[Z(0),-i/2],[i/2,Z(1)]];G_oneport=[[Z(1),Z(1)]]
for k in grid:check_model(Om_oneport,G_oneport,k)
# All-pass but wrong half-plane: b^-1 with a=1/2 and ell=1 has QW(0)=-3.
wrong_half_plane_velocity=Q(1)-2/Q(1,2);assert wrong_half_plane_velocity==-3
result={'arithmetic':'Exact Gaussian rationals (pairs of Fraction), no floating point in the checks.','matrix_cascade':{'E':2,'M':3,'noncommuting_projections':True,'centers':[str(x) for x in centers],'widths':[str(x) for x in widths],'omega':[[repr(x) for x in row] for row in Om],'real_energy_checks':len(grid),'includes_resonance_centers':True,'identities':'Srealization=product Fj; S*S=I; Q=G R*R G*; T upper triangular; detS=product bj'},'arbitrary_Hermitian_model':{'omega':[[repr(x) for x in row] for row in Om2],'identities_checked':len(grid)},'dark_control':{'full_real_inverse_singular_at':2,'dark_removed_transfer_unitary':True,'meaning':'The finite dark eigenvalue at2 must be added separately to the visible secular count.'},'one_port_two_visible_states':{'rankG':1,'M':2,'stable_triangular_diagonal':'k+i/2, k-1+i/2','meaning':'Auxiliary phase degree is not bounded by rankG or edge count.'},'wrong_half_plane_control':{'ell':1,'width':'1/2','QW_at_center':str(wrong_half_plane_velocity),'meaning':'Real-axis unitarity alone does not imply positive phase velocity or the inner-class bound.'},'scalar_special_cases':'At k=d, root iff exp(i d ell)=-1. No zero eigen for gamma!=0. Gamma0 leaves an uncounted dark level. Coincident example ell=pi,Omega=diag(1,1),G=[1,0] has full multiplicity2 at k1, visible secular multiplicity1. These cases are proved analytically in the campaign.','proof_file':'proposals/independent_campaigns/factored_inner_round2.md','limitations':'Finite checks supplement the all-energy/domain proof and are not an independent verification of arbitrary matrices.'}
(ROOT/'experiments/results/factored_inner_round2.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if k not in ['matrix_cascade','arbitrary_Hermitian_model']},indent=2))
