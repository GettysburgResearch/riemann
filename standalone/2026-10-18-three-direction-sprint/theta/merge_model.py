"""Hub tree after merging two old components by one positive edge.

The second component's hub edge is removed and a root/leaf cross edge is
inserted. The graph remains a tree. Conditional moments are polynomials;
at eta=0 and cross bias0 the original independent law is recovered.
"""
import model
Dual=model.Dual

def parity_vectors(A,B,p,single,leaf,degree):
    zero=A*0;one=zero+1
    even=[one]+[(A**n if single else p*A**n+(one-p)*B**n) if n%2==0 else zero for n in range(1,degree+1)]
    root=[zero]+[(A**n if single else p*A**n+(one-p)*B**n) if n%2 else zero for n in range(1,degree+1)]
    endpoint=[zero]+[(A**n if single else p*A**n+(-1 if leaf else 1)*(one-p)*B**n) if n%2 else zero for n in range(1,degree+1)]
    joint=[(one if not leaf else 2*p-1)]+[(A**n if single else p*A**n+(-1 if leaf else 1)*(one-p)*B**n) if n%2==0 else zero for n in range(1,degree+1)]
    return even,root,endpoint,joint

def merged_raw(z,selected,ends,eta,degree):
    i,j=selected;ai,aj=ends;r=z[-1]
    Mi,Ti,Ei,Ui=parity_vectors(*z[3*i:3*i+3],i==0,ai,degree)
    Mj,Tj,Ej,Uj=parity_vectors(*z[3*j:3*j+3],j==0,aj,degree)
    even=model.convolve_raw(Mi,Mj);edge=model.convolve_raw(Ei,Ej)
    root=model.convolve_raw(Ti,Mj);rootedge=model.convolve_raw(Ui,Ej)
    return [even[n]+r*edge[n] if n%2==0 else eta*(root[n]+r*rootedge[n]) for n in range(degree+1)]

def evaluate(z,counts,selected,ends,eta,degree):
    if len(z)!=3*len(counts)+1:raise ValueError('complete old plus merge edge coordinates')
    zero=z[0]*0;one=zero+1;total=[zero]*(degree+1);old=[]
    for i,count in enumerate(counts):
        A,B,p=z[3*i:3*i+3];mu=[one]+[(A**n if i==0 else p*A**n+(one-p)*B**n)*(one if n%2==0 else eta) for n in range(1,degree+1)]
        kap=model.cumulants(mu);old.append(kap);total=[a+count*b for a,b in zip(total,kap)]
    joint=model.cumulants(merged_raw(z,selected,ends,eta,degree));i,j=selected
    total=[a+b-ci-cj for a,b,ci,cj in zip(total,joint,old[i],old[j])]
    conditional=model.moments(total);raw=[v if n%2==0 else zero for n,v in enumerate(conditional)]
    kap=model.cumulants(raw);unit=model.unit_cumulants(degree)
    return [kap[2*r]/unit[2*r] for r in range(1,degree//2+1)],raw

def jet(z,counts,selected,ends,eta,degree,active):
    zero=z[0]*0;one=zero+1;zz=[Dual(v,[one if j==k else zero for k in active]) for j,v in enumerate(z)]
    vals,raw=evaluate(zz,counts,selected,ends,eta,degree)
    return [v.v for v in vals],[list(v.d) for v in vals],[v.v for v in raw]

def direct_assembly(z,counts,selected,ends,eta,degree):
    zero=z[0]*0;one=zero+1;out=[one]+[zero]*degree
    for i,count in enumerate(counts):
        count-=selected.count(i)
        A,B,p=z[3*i:3*i+3]
        base=[one]+[(A**n if i==0 else p*A**n+(one-p)*B**n)*(one if n%2==0 else eta) for n in range(1,degree+1)]
        power=[one]+[zero]*degree
        while count:
            if count%2:power=model.convolve_raw(power,base)
            count//=2
            if count:base=model.convolve_raw(base,base)
        out=model.convolve_raw(out,power)
    out=model.convolve_raw(out,merged_raw(z,selected,ends,eta,degree))
    return [v if n%2==0 else zero for n,v in enumerate(out)]
