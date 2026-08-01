#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,math
from fractions import Fraction
from pathlib import Path
import mpmath as mp
mp.mp.dps=220
from common import *

def mpf(q): return mp.mpf(q.numerator)/q.denominator
def dyadic(x,bits): return Fraction(int(mp.nint(x*mp.power(2,bits))),1<<bits)

def compress(doc):
    N=doc['support']['N'];d=N+1;A=madd(mat_iv(doc['P_even']),mat_iv(doc['E_even']))
    q=[Fraction(1)]*d;Qe=[]
    for k in range(1,d):
        v=[Fraction(0)]*d;v[0]=-2;v[k]=1;Qe.append(v)
    B=qform(A,q);Z=[qform(A,v,q) for v in Qe];C=[[qform(A,Qe[i],Qe[j]) for j in range(N)] for i in range(N)]
    M=[[Fraction(4)+(2 if i==j else 0) for j in range(N)] for i in range(N)]
    return B,Z,C,M

def main():
    ap=argparse.ArgumentParser();ap.add_argument('primitive',type=Path);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--bits',type=int,default=240);a=ap.parse_args()
    doc=json.loads(a.primitive.read_text());N=doc['support']['N'];B,Z,C,M=compress(doc)
    Cm=mp.matrix([[mpf(C[i][j].mid)for j in range(N)]for i in range(N)]);Mm=mp.matrix(M);LM=mp.cholesky(Mm);H=LM**-1*Cm*(LM.T**-1);lam=min(mp.eigsy(H,eigvals_only=True));e2=int(mp.floor(mp.log(lam,2)))-8
    while True:
        h=Fraction(2)**e2;Bm=mp.matrix([[mpf((C[i][j]-pt(h*M[i][j])).mid)for j in range(N)]for i in range(N)])
        try:L=mp.cholesky(Bm);break
        except:e2-=4
    Ymp=L.T**-1;Y=[[Fraction(0)for _ in range(N)]for __ in range(N)]
    for i in range(N):
        for j in range(i,N):Y[i][j]=dyadic(Ymp[i,j],a.bits)
    xmp=mp.lu_solve(Cm,mp.matrix([mpf(z.mid)for z in Z]));X=[dyadic(xmp[i],a.bits)for i in range(N)]
    # estimate normalized direct midpoint and choose a conservative dyadic m below one quarter of it
    b=mpf(B.mid);z=mp.matrix([mpf(v.mid)for v in Z]);s=(b-(z.T*xmp)[0])/(1+2*N);me=int(mp.floor(mp.log(s,2)))-2;m=Fraction(2)**me
    out={'schema':'riemann.x18507.trial.v1','support':{'c':doc['support']['c'],'N':doc['support']['N']},'primitive_sha256':file_sha(a.primitive),'round_bits':a.bits,'h_exponent':e2,'h':str(h),'m_exponent':me,'m':str(m),'X_N':[str(v)for v in X],'coercivity_preconditioner_Y':[[str(v)for v in row]for row in Y]}
    out['trial_sha256']=canonical_sha(out);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'support':{'c':doc['support']['c'],'N':doc['support']['N']},'h':str(h),'m':str(m),'trial_sha256':out['trial_sha256']},indent=2))
if __name__=='__main__':main()
