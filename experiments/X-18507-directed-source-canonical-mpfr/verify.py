#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from fractions import Fraction
from pathlib import Path
from common import *

def verify(doc,trial,primitive_path):
    if doc.get('schema')!='riemann.x18506.local-directed-source-canonical.v1':raise ValueError('primitive schema')
    if trial.get('schema')!='riemann.x18507.trial.v1':raise ValueError('trial schema')
    if {'c':doc['support']['c'],'N':doc['support']['N']}!=trial['support']:raise ValueError('support mismatch')
    N=doc['support']['N'];d=N+1;P=mat_iv(doc['P_even']);E=mat_iv(doc['E_even']);A=madd(P,E)
    if doc['metric_diagonal']!=[1]+[2]*N or doc['Q_W']!=[1]*d:raise ValueError('source metric/basis')
    Qe=[]
    for k in range(1,d):
        v=[Fraction(0)]*d;v[0]=-2;v[k]=1;Qe.append(v)
    if doc['Q_E']!=Qe:raise ValueError('source kernel basis')
    Gdiag=[Fraction(1)]+[Fraction(2)]*N;GW=sum(Gdiag[i] for i in range(d));GE=[[Fraction(4)+(2 if i==j else 0)for j in range(N)]for i in range(N)]
    PW=qform(P,[Fraction(1)]*d);EW=qform(E,[Fraction(1)]*d);B=PW+EW;Z=[qform(A,v,[Fraction(1)]*d)for v in Qe];C=[[qform(A,Qe[i],Qe[j])for j in range(N)]for i in range(N)]
    h=Fraction(trial['h']);m=Fraction(trial['m']);X=[Fraction(v)for v in trial['X_N']];Y=[[Fraction(v)for v in row]for row in trial['coercivity_preconditioner_Y']]
    if len(X)!=N or len(Y)!=N or any(len(r)!=N for r in Y):raise ValueError('trial dimensions')
    if any(Y[i][i]==0 for i in range(N)) or any(Y[i][j]!=0 for i in range(N) for j in range(i)):raise ValueError('preconditioner not invertible upper triangular')
    Bsh=[[C[i][j]-pt(h*GE[i][j])for j in range(N)]for i in range(N)];H=congruence(Bsh,Y);gl,grows=gersh_lower(H)
    if gl<=0:raise ValueError('coercivity not certified')
    R=[Z[i]-sum((C[i][j]*pt(X[j])for j in range(N)),pt(0))for i in range(N)]
    Minv=[[Fraction(1,2)if i==j else Fraction(0)for j in range(N)]for i in range(N)]
    for i in range(N):
        for j in range(N):Minv[i][j]-=Fraction(1,1+2*N)
    penalty=qform([[pt(v)for v in row]for row in Minv],R)/pt(h)
    ZX=sum((Z[i]*pt(X[i])for i in range(N)),pt(0));trial_energy=B-pt(2)*ZX+qform(C,X);D=trial_energy-penalty;Dn=D/pt(GW);pivot=D-pt(m*GW);pn=pivot/pt(GW)
    if pivot.lo<=0:raise ValueError('direct LDL pivot touches zero')
    out={'schema':'riemann.x18507.direct-certificate.v1','support':doc['support'],'precision_bits':doc['precision_bits'],'primitive_sha256':file_sha(primitive_path),'trial_sha256':trial['trial_sha256'],'declared_metric':{'G_diagonal':[1]+[2]*N,'G_W':str(GW),'G_E':[[str(v)for v in row]for row in GE]},'Q_W':[1]*d,'Q_E':[[int(v) for v in row] for row in Qe],'P_W':iv_json(PW),'E_W':iv_json(EW),'B_W':iv_json(B),'Z_W':[iv_json(v)for v in Z],'C':[[iv_json(v)for v in row]for row in C],'X_N':[str(v)for v in X],'R_N':[iv_json(v)for v in R],'h':str(h),'M_inverse':[[str(v)for v in row]for row in Minv],'coercivity_gershgorin_lower':str(gl),'coercivity_gershgorin_rows':[str(v)for v in grows],'residual_penalty':iv_json(penalty),'D_N':iv_json(D),'D_N_normalized':iv_json(Dn),'m':str(m),'LDL_pivot_D_minus_mG':iv_json(pivot),'LDL_pivot_normalized':iv_json(pn),'delta_operator_norm_upper':'0','verdict':'CERTIFIED_DELTA_ZERO_SOURCE_CANONICAL_DIRECT_BLOCK','scope':'Actual cutoff-free D-0001 source-canonical quotient. This is not the PR-192 deficit-canonical augmentation.'}
    out['certificate_sha256']=canonical_sha(out);return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('primitive',type=Path);ap.add_argument('trial',type=Path);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();doc=json.loads(a.primitive.read_text());tr=json.loads(a.trial.read_text());out=verify(doc,tr,a.primitive);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'support':out['support'],'precision_bits':out['precision_bits'],'floor':[out['D_N_normalized']['lower'],out['D_N_normalized']['upper']],'verdict':out['verdict'],'sha256':out['certificate_sha256']},indent=2))
if __name__=='__main__':main()
