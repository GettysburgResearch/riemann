"""Directed-interval replay for R=4.82 using two-prime positivity and E0."""
from certify_logistic_master import *

def extended_margin(A,l):
    eta=A/l
    return margin(A,l)+q('1.4547')*eta-2775*eta**3

def main():
    start=time.monotonic()
    target=Q(50,241)
    if not iv.exp(q('21.233')*q(target))<82:
        raise RuntimeError('Littlewood endpoint')
    if not q(target)/28<q('.0075'):
        raise RuntimeError('eta range')
    pending=[(Q(0),target,Q(28),Q(82),0)]
    accepted=[];evaluations=0;worst=None
    while pending:
        al,ah,ll,lh,depth=pending.pop()
        value=extended_margin(box(al,ah),box(ll,lh));evaluations+=1
        if value>0:
            if worst is None or value.a<worst:worst=value.a
            accepted.append([str(al),str(ah),str(ll),str(lh),str(value)])
            continue
        if depth>=32:raise RuntimeError(f'unresolved {al,ah,ll,lh,value}')
        if 5*(ah-al)>Q('.001')*(lh-ll):
            m=(al+ah)/2
            pending.extend([(al,m,ll,lh,depth+1),(m,ah,ll,lh,depth+1)])
        else:
            m=(ll+lh)/2
            pending.extend([(al,ah,ll,m,depth+1),(al,ah,m,lh,depth+1)])
    out={'status':'PASS','scope':'scalar extended detector inequality only',
         'domain':{'A':['0','50/241'],'log_t':['28','82']},
         'added_margin':'1.4547*eta-2775*eta^3',
         'arithmetic':f'mpmath {mpmath.__version__} iv, {iv.dps} decimal digits',
         'accepted_boxes':len(accepted),'evaluations':evaluations,
         'minimum_certified_lower_bound':str(worst),
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'base_source_sha256':hashlib.sha256(Path(__file__).with_name('certify_logistic_master.py').read_bytes()).hexdigest(),
         'seconds':time.monotonic()-start,'boxes':accepted}
    Path(__file__).with_name('LOGISTIC_PRIME_EXTENSION_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='boxes'},indent=2))

if __name__=='__main__':main()
