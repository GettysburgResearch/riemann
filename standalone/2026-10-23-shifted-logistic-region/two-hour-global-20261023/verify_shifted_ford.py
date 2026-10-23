"""Exact endpoint replay for the shifted-center detector; analytic inputs separate."""
from pathlib import Path
from fractions import Fraction as Q
import runpy,hashlib,json
P=Path(__file__).with_name('verify_general_ford.py')
SHA='da64b1b653dfb771773efc530e2ffbe605f665f835251e578891f888c89cfa27'
if hashlib.sha256(P.read_bytes()).hexdigest()!=SHA:raise ArithmeticError('frozen arithmetic engine')
n=runpy.run_path(str(P))
I,req,W,W0,WM,PI,H,U,CURV,COEFF,logp,logi,expp,expi,disp=(n[k] for k in ('I','require','W','W0','WMINUS','PI','H','U','CURVATURE','COEFF','log_point','log_i','exp_point','exp_i','display'))
K=12;EPS=Q(1,10**14);D=2*10**18;AA=Q(469028,10**6);BB=Q(399399,10**5)
def margin(R,L):
 R,L=Q(R),Q(L);A=1/R;h=L+logp(K);la=A/h;eta=Q(1,2)-la
 req(L>=40 and A<=Q(22,100),'endpoint domain')
 eup=(logp(K)+EPS)/L
 # The signal uses h_actual/L−1 <= eup; every adverse term uses la_upper.
 # Combine C−.805 at actual lambda first. C<=.9 gives .095lambda.
 jsum=I(0);hsum=I(0)
 for j,b in enumerate(COEFF[1:],1):
  hj=L+logp(j)
  shift=hj+logi(1+D*expi(-hj))
  J=shift/6+logi(AA*shift+BB)+Q(1,D)
  jsum+=b*J;hsum+=b*hj
 # x=d−lambda = B*(h_actual−L)/(L*h_actual).
 # Using h_upper in the small numerator and h_lower in denominator is safe.
 x=A*(logp(K)+EPS)/(L*h)
 result=(COEFF[1]*W(eup)/W0-WM/W0
     -Q('.3334')*PI**2*COEFF[1]*la*x/(4*eta**2)
     -la/(2*eta)*jsum-Q('.095')*la
     -(2*H/W0)*la**3/eta**2*(hsum/2+3)
     -(19+4*sum(COEFF[1:])/W0)*la**3-Q(1,10**20))
 return result

def main():
 req(H.hi<70,'H bound')
 req(W0.lo>6 and CURV.hi<70,'kernel constants')
 req(sum(COEFF[1:])<4 and all(b>0 for b in COEFF),'polynomial coefficients')
 req(100*expp(-40).hi<EPS,'global minimum window')
 a=Q(299,100)
 req(70*(a**-3+(a+2)**-3+1/(4*(a+2)**2))<4,'E_f bound')
 req(Q(197,196)*Q('.0463')/14<Q('.00333'),'real zero remainder')
 req(4+70*Q('.00333')<6,'normalized real error')
 gamma_lower=sum((Q(1,j) for j in range(1,101)),Q(0))-logp(100)-Q(1,200)
 req((1-gamma_lower/2-logp(2)-logi(PI)/2).hi<Q('-.55'),'real archimedean gain')
 req(expp(Q(8,5)).hi<6 and PI.lo>3,'gamma constants')
 req(logp(40*AA+BB).lo>3 and Q(4,6)+Q(44,40)<3,'critical quotient monotonicity')
 req(Q(22,100)/40<Q(1,160),'kernel remainder range')
 req(Q(1,2)-Q(22,100)/40>Q(49,100),'half-strip width range')
 req(Q(1600)/expp(10).lo**60<Q(1,10**100),'bad cotangent tail')
 checks=[]
 for R,L in [('4.75','50.5'),('4.72','52'),('4.70','53'),('4.65','55.5'),('4.60','58.5'),('4.55','61.5')]:
  v=margin(R,L);req(v.lo>0,'endpoint '+R)
  checks.append({'R':R,'log_t':L,'lower':str(v.lo),'upper':str(v.hi),'lower_decimal':disp(v.lo)})
 for R,L in [('4.70','50'),('4.60','55')]:
  v=margin(R,L);req(v.hi<0,'negative endpoint control '+R)
 out={'status':'pass','scope':'shifted Ford exact endpoints and primitive constants only; Euler/analytic hypotheses external',
      'engine_sha256':SHA,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'inputs':{'C_upper':'9/10','weighted_poisson_additive':'3','window':'100'},
      'endpoints':checks,'negative_controls':2}
 Path(__file__).with_name('SHIFTED_FORD_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
 print(json.dumps(out,sort_keys=True))
if __name__=='__main__':main()

