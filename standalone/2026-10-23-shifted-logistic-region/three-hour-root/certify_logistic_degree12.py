"""Directed certificate for the proposed R=4.815 degree-12 detector.

Imported helper supplies only interval arithmetic, the fixed kernel moments,
and the elementary J integral. All new polynomial data are exact integers.
The analytic kernel, prime and error bounds are separate reviewed inputs.
"""
from certify_logistic_master import *

C=[3500513104,-5906953599,-1574092731,18166603739,6213449589,
   -38436761903,-16088159026,168141762350,447056663730,616860378424,
   541372347258,298691298328,83048065550]
AUX=10**14
NORM=sum(c*c for c in C)+AUX*len(C)
AK=[Q(sum(C[j]*C[j+k] for j in range(13-k))+AUX*(13-k),NORM)
       *(1 if k==0 else 2) for k in range(13)]
A1=q(AK[1]); AP=q(sum(AK[1:])); CARCH=q('-3.00317')

def degree12_margin(A,l):
    c=iv.log(12+q(10**10)*iv.exp(-l))
    mu=1/(1+c/l);eta=A/l;sigma=1-A/(l+c);alpha=2*sigma-1
    z0=sigma-1;z1=z0+eta;z2=sigma-eta
    signal=A1*W(1-mu)-W(-mu)
    correction=eta*w0*(A1/z2+J(z0,alpha)-A1*J(z1,alpha)-A1*J(z2,alpha))
    error=51*eta**3*(1/(z0+alpha)**3+A1/(z1+alpha)**3+A1/z2**3)
    resource=w0*(A*AP/4+CARCH*eta/2)+q('1e-7')
    return signal+correction-error-resource+q('1.57')*eta-90*eta**3

def main():
    start=time.monotonic();target=Q(200,963);lmax=Q(823,10)
    if NORM!=1000000001299439064580929 or AK[0]!=1 or min(AK)<=0:
        raise RuntimeError('exact polynomial normalization/signs')
    ca=-AP*iv.log(2*iv.pi)/2+sum(q(AK[k])*iv.log(k)/2 for k in range(1,13))-q('.5541')
    if not ca<CARCH:raise RuntimeError('archimedean coefficient')
    if not iv.exp(q('21.233')*q(target))<q(lmax):raise RuntimeError('Littlewood endpoint')
    if not iv.log(q(3*10**12))>28:raise RuntimeError('verified height endpoint')
    if not q(target)/28<q('.0075'):raise RuntimeError('eta domain')
    if not 1-q(target)/(28+iv.log(12))>q('.99'):raise RuntimeError('sigma domain')
    pending=[(Q(0),target,Q(28),lmax,0)];accepted=[];evaluations=0;worst=None
    while pending:
        al,ah,ll,lh,depth=pending.pop()
        value=degree12_margin(box(al,ah),box(ll,lh));evaluations+=1
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
    if not degree12_margin(q(Q(1,4)),q(lmax))<0:
        raise RuntimeError('negative control: unsupported A')
    out={'status':'PASS','scope':'scalar degree-12 sufficient inequality only',
         'domain':{'A':['0','200/963'],'log_t':['28','823/10']},
         'trigonometric_polynomial':{'degree':12,'integer_square_coefficients':C,
             'auxiliary_square_weight':AUX,'normalization':str(NORM),
             'cosine_coefficients':[str(x) for x in AK]},
         'kernel_second_derivative_upper':'51','Carch_upper':'-3.00317',
         'prime_lower':'1.26*eta-90*eta^3','archimedean_upper':'-0.31*eta',
         'arithmetic':f'mpmath {mpmath.__version__} iv, {iv.dps} decimal digits',
         'accepted_boxes':len(accepted),'evaluations':evaluations,'negative_controls':1,
         'minimum_certified_lower_bound':str(worst),
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'base_source_sha256':hashlib.sha256(Path(__file__).with_name('certify_logistic_master.py').read_bytes()).hexdigest(),
         'seconds':time.monotonic()-start,'boxes':accepted}
    Path(__file__).with_name('LOGISTIC_DEGREE12_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ['boxes','trigonometric_polynomial']},indent=2))

if __name__=='__main__':main()
