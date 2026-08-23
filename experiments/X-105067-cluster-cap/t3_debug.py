import numpy as np, random
random.seed(7); rng=np.random.default_rng(7)
# regenerate trial 2 exactly as in t2_capscan
def gen(trial_target):
    random.seed(7); rng=np.random.default_rng(7)
    for trial in range(trial_target+1):
        g=random.choice([1.0,4.0,16.0]); a,b=-g/2,g/2
        reals=[(a,random.choice([1,1,2])),(b,random.choice([1,1,3]))]
        for extra in range(random.randint(0,3)):
            side=random.choice([-1,1]); d=10**rng.uniform(-2,1)
            reals.append(((b if side>0 else a)+side*d, random.randint(1,3)))
        m=random.randint(1,5)
        deep=[]
        for j in range(m):
            y=10**rng.uniform(np.log10(g*1e-4), np.log10(g*0.49))
            x=rng.uniform(a-0.5*y, b+0.5*y)
            deep.append((x,y,random.randint(1,4)))
        other=[]
        for k in range(random.randint(0,3)):
            kind=random.choice(['sh','nonov'])
            if kind=='sh':
                y=g/2*10**rng.uniform(0,0.3); x=rng.uniform(a,b); mm=1
                if (g/(2*y))**2*mm<0.3: other.append((x,y,mm))
            else:
                y=10**rng.uniform(-2,0); side=random.choice([-1,1])
                x=(b if side>0 else a)+side*(y+10**rng.uniform(-2,0)*y); other.append((x,y,1))
    return g,a,b,reals,deep,other
g,a,b,reals,deep,other=gen(2)
print("g",g,"reals",reals); print("deep",deep); print("other",other)
z=0.2360795278400003
import mpmath as mp
mp.mp.dps=40
def hp(t):
    v=mp.mpf(0)
    for (c,mn) in reals: v-=mn/(mp.mpf(t)-c)**2
    for (x,y,mm) in deep+other:
        s=mp.mpf(t)-x; v+= mm*2*(y*y-s*s)/(s*s+y*y)**2
    return v
print("h'(z)=",hp(z), "h'(z-1e-4)",hp(z-1e-4),"h'(z+1e-4)",hp(z+1e-4))
for (x,y,mm) in deep: print("pair",x,y,"dist",abs(z-x),"in I?",abs(z-x)<y)
for (x,y,mm) in other: print("other",x,y,"dist",abs(z-x),"in I?",abs(z-x)<y, "ov?", (x-y<b) and (x+y>a), "yshallow?", y>=g/2)
