"""Kernel samples for independent union-of-events verification."""
import json,hashlib
from pathlib import Path
from harmonic import Gram
from arithmetic import canonical
from exact import BITS

def build():
    out=[]
    for b in (4,8,16,32,64,128,256):
        N=b*b-1;g=Gram(b,N,N+1)
        for d,e in ((1,N+1),(2,3),(2,N+1),(b,b+1),(b,2*b-1),(N,N+1)):
            out.append(dict(b=b,N=N,d=d,e=e,G=g.pair(d,e)))
    return dict(schema='DCN26-kernel-samples-1',bits=BITS,samples=out)
if __name__=='__main__':
    x=build();s=canonical(x);Path('reports').mkdir(exist_ok=True);Path('reports/kernel_samples.json').write_text(s+'\n')
    print('kernel samples',hashlib.sha256(s.encode()).hexdigest())
