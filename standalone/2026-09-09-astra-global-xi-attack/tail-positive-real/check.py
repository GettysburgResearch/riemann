"""TPR26 bounded algebra and source-pinned transfer checks.
Does NOT machine-prove the analytic all-scale theorems or RH.
Default mode verifies the sealed package and fixed parent's receipt.
--full also runs the unchanged source-pinned 152-cell parent quadrature.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import comb,factorial
import argparse,hashlib,json,subprocess,sys
ROOT=Path(__file__).resolve().parent
INVENTORY={'PROOF.md','README.md','SOURCE_LOCK.json','VALIDATION.md','check.py',
           'test_check.py','verification.json','SHA256SUMS'}
PARENT='815ccae329a17327b873d21f05bc30c24db13e7e'
PARENT_BLOBS={'GLOBAL_ATTEMPT.md':'92e2562661055ffe53845569d458f5fb721ad100',
 'certify_truncation.py':'2b9220945e81293af2ca3d7e77e60e14b8848cea',
 'root_certificate.json':'4b224c4731efc77912180778c908d389a0ce8a8f'}

def require(ok,message):
    if not ok:raise ValueError(message)

def regular(path,max_bytes=1000000):
    require(not path.is_symlink() and path.is_file(),'regular nonsymlink file required')
    require(path.stat().st_size<=max_bytes,'oversize input')
    return path.read_bytes()

def load(path):
    def pairs(rows):
        out={}
        for k,v in rows:
            require(k not in out,'duplicate JSON key');out[k]=v
        return out
    def bad(x):raise ValueError('floating/nonfinite JSON prohibited')
    a=json.loads(regular(path).decode(),object_pairs_hook=pairs,parse_float=bad,parse_constant=bad)
    require(type(a) is dict and a,'nonempty JSON object required')
    return a

def canonical(a):return json.dumps(a,sort_keys=True,separators=(',',':'))

def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def authenticate(root=ROOT,parent=None):
    require({p.name for p in root.iterdir()}==INVENTORY,'incorrect package inventory')
    rows={}
    for line in regular(root/'SHA256SUMS').decode().splitlines():
        digest,name=line.split('  ')
        require(name in INVENTORY-{'SHA256SUMS'} and name not in rows,'bad/duplicate manifest path')
        require(len(digest)==64,'bad digest')
        rows[name]=digest
    require(set(rows)==INVENTORY-{'SHA256SUMS'},'incomplete checksum manifest')
    for name,digest in rows.items():
        require(hashlib.sha256(regular(root/name)).hexdigest()==digest,'package hash mismatch '+name)
    lock=load(root/'SOURCE_LOCK.json')
    require(lock['parent_commit']==PARENT and type(lock['parent_pr']) is int and lock['parent_pr']==835,'wrong frozen parent')
    require(lock['repository']=='GettysburgResearch/riemann','wrong repository')
    require(set(lock['source_files'])==set(PARENT_BLOBS),'parent inventory mismatch')
    parent=parent or root.parent
    for name,wanted in PARENT_BLOBS.items():
        b=regular(parent/name);d=lock['source_files'][name]
        require(blob(b)==wanted==d['git_blob'],'parent Git blob mismatch '+name)
        require(type(d['bytes']) is int and len(b)==d['bytes'],'parent size mismatch')
        require(hashlib.sha256(b).hexdigest()==d['sha256'],'parent SHA256 mismatch')
    return parent

def trim(a):
    a=list(map(Q,a))
    while len(a)>1 and not a[-1]:a.pop()
    return a

def add(a,b):return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def scale(a,c):return trim([Q(c)*v for v in a])
def mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)
def derivative(a):return trim([i*a[i] for i in range(1,len(a))] or [0])
def shifted(a,c):return trim([sum((a[j]*comb(j,i)*Q(c)**(j-i) for j in range(i,len(a))),Q(0)) for i in range(len(a))])
def evolve(a):return add(mul([0,2],derivative(a)),mul([Q(1,2),-2],a))
def rec(a):return [str(v) for v in a]

# Tiny Gaussian-rational algebra; no Python complex/float enters acceptance.
def ca(a,b):return (a[0]+b[0],a[1]+b[1])
def cm(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cs(a,c):return (a[0]*c,a[1]*c)
def ci(a):
    d=a[0]*a[0]+a[1]*a[1];require(d>0,'zero divisor')
    return(a[0]/d,-a[1]/d)
def cp(a,n):
    out=(Q(1),Q(0))
    for _ in range(n):out=cm(out,a)
    return out

def reconstruction(parent):
    p0=list(map(Q,[0,-6,4]));p1=evolve(p0);p2=evolve(p1)
    require(p1==list(map(Q,[0,-15,30,-8])),'first primitive derivative wrong')
    require(p2==[0,Q(-75,2),Q(165),Q(-112),Q(16)],'second primitive derivative wrong')
    rmin=add(add(p2,mul([0,2],p1)),mul([0,0,1],p0))
    fact=scale(mul(mul([0,1],[-5,2]),[15,-48,4]),Q(1,2))
    require(rmin==fact,'tilted curvature factorization')
    rhalf=add(add(p2,p1),scale(p0,Q(1,4)))
    tests={'positive_phi':p0,'negative_phi_prime':scale(p1,-1),
      'tilt_monotonicity':scale(add(p1,mul([0,1],p0)),-1),
      'broad_strip_curvature':rmin,
      'critical_strip_reserve':add(rhalf,[0,0,0,0,-4])}
    certs={}
    for name,p in tests.items():
        c=shifted(p,12)
        require(all(x>=0 for x in c) and c[0]>0,'positive shifted coefficients '+name)
        certs[name]=rec(c)
    require(Q(2,15)>Q(1,8),'sinc small-range bound')
    require(7+Q(165,16*12)+Q(75,32*12**2)<8,'scaled second derivative remainder')
    require(Q(17,4)+1<=Q(12,2),'exponential remainder decay')
    moment=sum((Q(c)*factorial(j)*3**(j+1) for j,c in enumerate([8,5,1])),Q(0))
    require(moment==123,'complete exponential polynomial integral')
    require(2*(moment+4)==254 and 254+1<256,'relative approximation constants')
    # Proves the starting point of the analytically decreasing tail-ratio bound.
    tail_ratio=17*Q(729,64)*4*2**2/Q(2**(6*2+3))
    require(tail_ratio<1 and Q(9,4)/64<1,'complete later-index ratio bound')
    require(Q(3,2)**6/2**15<Q(1,2),'theta consecutive ratios')
    require(8*Q(12)/(12-Q(5,4))<10,'mass upper bound')
    # Exact coefficient recurrence of the rescaled exponentials in (21).
    scaled=[]
    for r,p in enumerate([p0,p1,p2]):
        terms=[]
        for degree,c in enumerate(p):
            if c:terms.append({'power_of_q':degree-r-2,'exp_v_over_q':str(Q(2*degree,2)+Q(1,4)),'coefficient':str(c/(4*2**r))})
        scaled.append(terms)
    # Independent rational Laplace evaluation of the first correction (25).
    panels=[]
    for a in [Q(0),Q(1,4),Q(1),Q(2),Q(7)]:
      for b in [Q(0),Q(1,48),Q(-1,48)]:
        w=(a,b);iw=(-b,a)
        plus=ca((Q(1),Q(0)),iw);minus=ca((Q(1),Q(0)),cs(iw,-1))
        C=[]
        for j in range(3):C.append(cs(ca(cp(ci(plus),j+1),cp(ci(minus),j+1)),Q(factorial(j),2)))
        left=ca(ca(cs(C[1],Q(9,4)),cs(C[2],Q(-1,2))),cs(C[0],Q(-3,2)))
        ww=cm(w,w);den=ca((Q(1),Q(0)),ww)
        right=cs(cm(ca((Q(1),Q(0)),cs(cm(ww,ww),15)),ci(cp(den,3))),Q(-1,4))
        require(left==right,'first asymptotic correction identity')
        panels.append({'w':rec(w),'value':rec(left)})
    source=load(parent/'root_certificate.json')
    require(source['rh_proved'] is False,'parent scope flag')
    residual=Q(source['residual_upper']);slope=Q(source['derivative_lower'])
    require(residual<Q(2,10**57) and slope>Q(17,10**21),'parent actual interval conclusion')
    require(type(source['cells']) is int and source['cells']==152,'parent quadrature coverage')
    require(type(source['theta_terms']) is int and source['theta_terms']==3,'parent defining function')
    require(type(source['second_derivative_bound']) is int and source['second_derivative_bound']==1000,'parent second derivative ceiling')
    radius=Q(1,10**35);xr=Q(source['center_real']);yi=Q(source['center_imag'])
    require(0<xr-radius and xr+radius<68 and 0<yi-radius and yi+radius<Q(1,2),'full disk geometry')
    left=Q(2,10**57)+500*radius**2;right=Q(17,10**21)*radius
    require(left<right,'refined Rouche margin')
    derivative_ceiling=128*sum((Q(n**4,(6*n*n-5)**2) for n in range(1,4)),Q(0))
    require(derivative_ceiling<1000,'full-band first derivative bound')
    real_tail=Q(48**3,18*(4*64**2+68**2)*3**64)
    real_xi=real_tail-1000*radius-Q(2,10**57)
    require(real_tail>Q(8,10**32) and real_xi>Q(7,10**32),'whole Xi disk strictness')
    return {'schema':'TPR26-v1','rh_proved':False,'full_laguerre_sign_proved':False,
      'analytic_theorems_machine_proved':False,'parent_commit':PARENT,
      'primitive_derivative_polynomials':[rec(p0),rec(p1),rec(p2)],
      'positive_shifted_polynomials':certs,'scaled_derivative_terms':scaled,
      'rational_laplace_panels':panels,'complete_moment':'123',
      'later_index_majorant_start':str(tail_ratio),'uniform_relative_error_constant':256,
      'disk_transfer':{'radius':str(radius),'center_real':str(xr),'center_imag':str(yi),
         'refined_rouche_left':str(left),'refined_rouche_right':str(right),
         'global_first_derivative_ceiling':str(derivative_ceiling),
         'complete_tail_real_lower':str(real_tail),'complete_xi_real_lower':str(real_xi),
         'simple_F3_zero':True,'Xi_zero_free_same_disk':True,
         'parent_receipt_sha256':hashlib.sha256(regular(parent/'root_certificate.json')).hexdigest()},
      'executed_scope':'finite exact algebra and source-pinned parent-bound transfer; --full additionally replays parent quadrature'}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--parent',type=Path)
    ap.add_argument('--check',type=Path,default=ROOT/'verification.json')
    ap.add_argument('--full',action='store_true')
    ap.add_argument('--emit',action='store_true',help='producer only: skip own package seal, not source binding')
    args=ap.parse_args();parent=args.parent or ROOT.parent
    if not args.emit:parent=authenticate(parent=parent)
    else:
        # Even production binds all consumed old bytes; it is NOT an acceptance command.
        for name,wanted in PARENT_BLOBS.items():require(blob(regular(parent/name))==wanted,'producer parent drift')
    if args.full:
        flags=['-O'] if sys.flags.optimize else []
        cmd=[sys.executable,'-I','-S','-B',*flags,str(parent/'certify_truncation.py'),'--check',str(parent/'root_certificate.json')]
        p=subprocess.run(cmd,capture_output=True,timeout=700,check=False)
        require(p.returncode==0,'parent primitive replay failed: '+p.stderr.decode(errors='replace')[-1000:])
        require(p.stdout==regular(parent/'root_certificate.json'),'parent complete output byte mismatch')
    actual=reconstruction(parent)
    if not args.emit:require(canonical(load(args.check))==canonical(actual),'expected result differs from reconstruction')
    print(json.dumps(actual,sort_keys=True,indent=2))
if __name__=='__main__':main()
