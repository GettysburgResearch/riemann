import numpy as np

def val(b, v, d=.14,k=0,g=0):
 D=1.2-d-g;pref=1/30+2*d/3-5*k/6-b/6
 xs=np.linspace(0,D/3,3001);Z=D-3*xs;T4=np.maximum.reduce([np.full_like(Z,b-v),v+2*Z,5*b/6-2*v/3+2*Z/3,b/3+v/3+5*Z/3]);T4=np.minimum.reduce([T4,b-v+2*Z,np.maximum.reduce([np.full_like(Z,b),2*Z,5*b/6+2*Z/3,b/3+5*Z/3])]);T2=np.minimum.reduce([b-v+Z,np.maximum(b+k,2*b+3*k+g-D+3*xs),(b-v+T4)/2]);f=[]
 for p in [2,3,4,5,6]:
  A=np.minimum(np.maximum(b-v+p*xs,v+2*p*xs),np.maximum(b+p*xs,b/2+2*p*xs));f.append(A/(2*p)+(p-2)/(2*p)*T2+T4/p/2-xs)
 tail=2*np.minimum.reduce(f);suffix=np.maximum.accumulate(tail[::-1])[::-1];short=np.maximum(b+k,2*b+3*k+g-D+3*xs);obj=pref+np.maximum(short,suffix);lo=max(0,(1.4-b+4*d-5*k)/18);obj[xs<lo]=100;ix=np.argmin(obj);return obj[ix], xs[ix], xs[ix+np.argmax(tail[ix:])]
for b in [.935,.95,.975,1,1.05,1.1]:
 vs=np.linspace(0,b/2,1001);out=[val(b,v) for v in vs];ix=max(range(len(vs)),key=lambda i:out[i][0]);print(b,vs[ix],out[ix])
