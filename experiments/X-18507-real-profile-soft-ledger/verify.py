#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

class V(RuntimeError): pass
@dataclass(frozen=True)
class I:
    lo:Fraction; hi:Fraction
    def __post_init__(self):
        if self.lo>self.hi: raise V('reversed interval')
    @staticmethod
    def p(x): return I(Fraction(x),Fraction(x))
    def __add__(self,o): return I(self.lo+o.lo,self.hi+o.hi)
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-o)
    def __mul__(self,o):
        p=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi);return I(min(p),max(p))
    def recip(self):
        if self.lo<=0<=self.hi: raise V('division by zero interval')
        p=(1/self.lo,1/self.hi);return I(min(p),max(p))
    def __truediv__(self,o): return self*o.recip()
    def square(self):
        if self.lo>=0:return I(self.lo*self.lo,self.hi*self.hi)
        if self.hi<=0:return I(self.hi*self.hi,self.lo*self.lo)
        return I(Fraction(0),max(self.lo*self.lo,self.hi*self.hi))
    def contains(self,o): return self.lo<=o.lo and o.hi<=self.hi
    def abs_upper(self): return max(abs(self.lo),abs(self.hi))

def q(x):
    if not isinstance(x,dict) or set(x)!={'numerator','denominator'}: raise V('bad rational')
    return Fraction(int(x['numerator']),int(x['denominator']))
def iv(x):
    if not isinstance(x,dict) or set(x)!={'lower','upper'}: raise V('bad interval')
    return I(q(x['lower']),q(x['upper']))
def canonical(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def psd2(a,b,d,strict=False):
    det=a*d-b.square()
    if strict:return a.lo>0 and d.lo>0 and det.lo>0
    return a.lo>=0 and d.lo>=0 and det.lo>=0

def quad(A,v,w):
    s=I.p(0)
    for i in range(2):
        for j in range(2):s+=A[i][j]*I.p(v[i]*w[j])
    return s

def verify(doc:dict[str,Any],repo_root:Path|None,skip_bindings:bool=False)->dict[str,Any]:
    if doc.get('schema')!='riemann.x18507.real-profile-soft-common-ledger.v1': raise V('schema')
    if doc.get('verdict')!='CERTIFIED_FIRST_REAL_COMMON_PROFILE_SOFT_LEDGER': raise V('false verdict field')
    src=doc['source_identity']
    L=src['localization_matrix'];F=src['source_synthesis_matrix']
    if L!=[[1,0],[0,1]] or F!=[[1,0],[0,1]]: raise V('source identity')
    soft=[int(x) for x in src['soft_column']];hard=[int(x) for x in src['hard_column']]
    G=int(src['metric_gram'])
    if sum(x*x for x in soft)!=G or sum(x*x for x in hard)!=G or sum(soft[i]*hard[i] for i in range(2))!=0: raise V('metric split')

    prof=doc['profile'];D=[[iv(x) for x in row] for row in prof['D_even']];K=[[iv(x) for x in row] for row in prof['K_even']]
    if not D[0][1].contains(D[1][0]) and not D[1][0].contains(D[0][1]): raise V('D symmetry')
    if not K[0][1].contains(K[1][0]) and not K[1][0].contains(K[0][1]): raise V('K symmetry')
    if not psd2(D[0][0],D[0][1],D[1][1],strict=True): raise V('D not positive')
    if not psd2(K[0][0],K[0][1],K[1][1]): raise V('K not PSD')
    comp=prof['compressed_normalized']
    Ds=quad(D,soft,soft)/I.p(G);Dh=quad(D,hard,hard)/I.p(G);Dsh=quad(D,soft,hard)/I.p(G)
    Ks=quad(K,soft,soft)/I.p(G);Kh=quad(K,hard,hard)/I.p(G);Ksh=quad(K,soft,hard)/I.p(G)
    for name,calc in [('D_soft',Ds),('D_hard',Dh),('D_cross',Dsh),('K_soft',Ks),('K_hard',Kh),('K_cross',Ksh)]:
        if not iv(comp[name]).contains(calc): raise V(f'{name} compression mismatch')
    M2=q(prof['graph_lmi']['M_squared_upper'])
    if not psd2(I.p(M2)-Ks,-Ksh,I.p(M2)-Kh): raise V('graph LMI fails')
    buf=prof['buffered_soft_export'];tau=q(buf['threshold_tau'])
    dettau=(Ds-I.p(tau))*(Dh-I.p(tau))-Dsh.square()
    if dettau.hi>=0 or not iv(buf['det_D_minus_tau_I']).contains(dettau): raise V('soft threshold not separating')
    if Ds.hi>=tau or Dh.lo<=tau: raise V('rayleigh split')
    gap=Dh-I.p(Ds.hi)
    angle=Fraction(2)*Dsh.abs_upper()/gap.lo
    if q(buf['projector_graph_angle_upper'])<angle: raise V('angle bound too small')

    ar=doc['complete_weil_matrix'];A=iv(ar['A_soft']);Z=iv(ar['Z_soft_hard']);C=iv(ar['C_hard'])
    if q(ar['hard_metric'])!=G or q(ar['soft_metric'])!=G: raise V('arithmetic metric')
    sh=doc['pr191_direct_short'];h=q(sh['hard_floor_h']);m=q(sh['target_floor_m'])
    coerc=C-I.p(h*G);pen=Z.square()/I.p(h*G);direct=A-pen;pivot=direct-I.p(m*G);exact=A-Z.square()/C
    for name,calc in [('hard_coercivity_pivot',coerc),('residual_penalty',pen),('direct_lower',direct),('shifted_ldl_pivot',pivot),('exact_schur',exact),('normalized_direct_lower',direct/I.p(G)),('normalized_shifted_ldl_pivot',pivot/I.p(G)),('normalized_exact_schur',exact/I.p(G))]:
        if not iv(sh[name]).contains(calc): raise V(f'{name} mismatch')
    if coerc.lo<=0 or pivot.lo<=0 or exact.lo<=0: raise V('direct soft sign failed')
    if q(sh['negative_part_upper'])!=0: raise V('negative part not zero')

    binding_status='SKIPPED'
    if not skip_bindings:
        if repo_root is None: raise V('repo root required for bindings')
        bindings=doc['bindings']
        for key,sha_key in [('arithmetic_certificate_path','arithmetic_certificate_sha256')]:
            path=repo_root/bindings[key]
            if not path.is_file() or sha(path)!=bindings[sha_key]: raise V(f'binding failed: {key}')
        zpath=repo_root/bindings['zero_config_path']
        if not zpath.is_file(): raise V('zero config missing')
        binding_status='PASSED'

    result={'schema':'riemann.x18507.real-profile-soft-common-ledger.verification.v1','input_proof_object_sha256':doc['proof_object_sha256'],'binding_status':binding_status,'soft_profile_upper':str(Ds.hi),'hard_profile_lower':str(Dh.lo),'projector_angle_upper':str(angle),'graph_M_squared':str(M2),'normalized_direct_floor_lower':str((direct/I.p(G)).lo),'normalized_shifted_ldl_lower':str((pivot/I.p(G)).lo),'normalized_exact_schur_lower':str((exact/I.p(G)).lo),'negative_part_upper':'0','verdict':'CERTIFIED_FIRST_REAL_COMMON_PROFILE_SOFT_LEDGER'}
    result['verification_sha256']=canonical(result)
    return result

def main():
    ap=argparse.ArgumentParser();ap.add_argument('certificate',type=Path);ap.add_argument('--repo-root',type=Path);ap.add_argument('--skip-bindings',action='store_true');ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    doc=json.loads(a.certificate.read_text());res=verify(doc,a.repo_root,a.skip_bindings);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(res,indent=2,sort_keys=True)+'\n');print(json.dumps(res,indent=2,sort_keys=True))
if __name__=='__main__':main()
