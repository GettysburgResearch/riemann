from itertools import product
from collections import Counter

def mul(a,b):
    out=0
    for i in range(3):
        for j in range(3):
            v=0
            for k in range(3): v ^= ((a>>(3*i+k))&1)&((b>>(3*k+j))&1)
            out |= v<<(3*i+j)
    return out

def det(a):
    def at(i,j): return (a>>(3*i+j))&1
    return (at(0,0)*at(1,1)*at(2,2)+at(0,0)*at(1,2)*at(2,1)+at(0,1)*at(1,0)*at(2,2)+at(0,1)*at(1,2)*at(2,0)+at(0,2)*at(1,0)*at(2,1)+at(0,2)*at(1,1)*at(2,0))%2
E=sum(1<<(3*i+i) for i in range(3))
G=[a for a in range(512) if det(a)]
assert len(G)==168
inv={a:next(b for b in G if mul(a,b)==E) for a in G}

def power(a,n):
 r=E
 for _ in range(n):r=mul(r,a)
 return r

def order(a):return next(n for n in range(1,169) if power(a,n)==E)
def conj(g,a):return mul(mul(g,a),inv[g])
def closure(gens):
 s={E}; todo=[E]
 while todo:
  x=todo.pop()
  for g in gens:
   y=mul(x,g)
   if y not in s:s.add(y);todo.append(y)
 return s
classes=[];remain=set(G)
while remain:
 a=next(iter(remain)); c={conj(g,a) for g in G}; classes.append(c);remain-=c
classes.sort(key=lambda c:(order(next(iter(c))),min(c)))
print('class sizes orders',[(len(c),order(next(iter(c)))) for c in classes])
a=next(x for x in G if order(x)==7)
H={g for g in G if conj(g,a) in {power(a,k) for k in range(1,7)}}
assert len(H)==21
C7={power(a,k) for k in range(7)}
b=next(x for x in H if order(x)==3)
coset=lambda subgroup,x:{mul(y,x) for y in subgroup}
Hpow=[coset(C7,power(b,j)) for j in range(3)]
assert set.union(*Hpow)==H
invol=[g for g in G if order(g)==2]
J=None
for x,y in product(invol,invol):
 V=closure([x,y])
 if len(V)!=4:continue
 for g in G:
  if order(g)==3 and {conj(g,z) for z in V}==V:
   J=closure([x,y,g]); Jv=V; jg=g; break
 if J:break
assert len(J)==12 and len(Jv)==4
Jpow=[coset(Jv,power(jg,j)) for j in range(3)]
assert set.union(*Jpow)==J
# Cyclotomic rationals represented a+b*w, w²+w+1=0.
def add(x,y):return(x[0]+y[0],x[1]+y[1])
weights=[(1,0),(0,1),(-1,-1)]
def induced(H,cosets,c):
 rep=next(iter(c)); sm=(0,0)
 for g in G:
  v=conj(inv[g],rep)
  for j,S in enumerate(cosets):
   if v in S:sm=add(sm,weights[j]);break
 assert sm[0]%len(H)==0 and sm[1]%len(H)==0
 return sm[0]//len(H),sm[1]//len(H)
hvals=[induced(H,Hpow,c) for c in classes]
jvals=[induced(J,Jpow,c) for c in classes]
print('Ind 7:3',hvals)
print('Ind A4',jvals)
assert all(b==0 for a,b in hvals+jvals)
assert [a for a,b in hvals]==[8,0,-1,0,1,1]
assert [a for a,b in jvals]==[14,2,-1,0,0,0]
print('Verified Ind(7:3,omega)=8 and Ind(A4,omega)=6+8 on every conjugacy class')
# Exact induced seventh-root characters in Z[zeta_7], encoded modulo 1+...+x^6.
def red7(v): return tuple(v[i]-v[6] for i in range(6))
def induced7(c,k):
 rep=next(iter(c)); counts=[0]*7
 for g in G:
  v=conj(inv[g],rep)
  for j in range(7):
   if v==power(a,j):counts[(j*k)%7]+=1;break
 assert all(x%7==0 for x in counts)
 return red7([x//7 for x in counts])
Htrivial=[]
for c in classes:
 rep=next(iter(c)); n=sum(conj(inv[g],rep) in H for g in G)
 assert n%len(H)==0
 Htrivial.append(n//len(H))
assert Htrivial==[8,0,2,0,1,1]
print('Ind(7:3,1)=1+7',Htrivial)
for k in (1,3):
 vals=[induced7(c,k) for c in classes]
 print('Ind C7 lambda^',k,vals)
 assert vals[0]==(24,0,0,0,0,0)
 assert all(v==(0,0,0,0,0,0) for v in vals[1:4])
 # The two order-7 classes differ, and are sums of the two cubic Galois orbits.
 assert set(vals[4:])=={red7([0,1,1,0,1,0,0]),red7([0,0,0,1,0,1,1])}
print('Verified C7 inductions = 3+6+7+8 and 3bar+6+7+8 via class values')
