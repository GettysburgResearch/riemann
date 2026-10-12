#!/usr/bin/env python3
"""Directed implementation controls for the separately proved local evaluator.

Overlap checks are consistency controls, not a substitute for the analytic
Cauchy/log-tail theorem. Literal integral sums use an explicit complete tail.
"""
import argparse,hashlib,json
from pathlib import Path
from flint import arb,acb,ctx
from taylor_convolution_source import TaylorConvolutionSource
from source_convolution import ConvolutionSource
from enclose_analytic_upper import require


def run():
    ctx.prec=256
    require(arb(1).exp()<arb(11)/4,'e<11/4')
    require((arb(1)/2).exp()<2,'e^(1/2)<2')
    require((arb(3)/2).exp()<5,'e^(3/2)<5')
    require(arb(16).log()<3,'log16<3')
    require(arb(4).log()<arb(3)/2,'log4<3/2')
    helper=TaylorConvolutionSource();old=ConvolutionSource()
    require(ctx.cap==10,'series context restored to its original default')
    keys=[('i',sign*j) for sign in(1,-1) for j in(1,10,50,100,105)]
    keys.extend(('r',j) for j in(-3,-1,1,3))
    lengths=['.00000001','.001','.05','.1','.2','.3']
    controls=[]
    for a in lengths:
        for key in keys:
            new=helper.gamma_incomplete(key,acb(a));previous=old.gamma_incomplete(key,acb(a))
            require(new.overlaps(previous),('independent closed-form overlap',key,a))
            require(ctx.cap==10,'every cached series path restores context cap')
            controls.append({'key':list(key),'length':a,'overlap':True,
                             'enclosure':new.str(45,more=True)})
    literal=[];terms=4096
    for key,a in [(('i',105),'.00000001'),(('i',-100),'.1'),
                  (('i',1),'.3'),(('r',-3),'.3'),(('r',3),'.05')]:
        length=acb(a);z=helper.val(key);value=acb(0)
        for j in range(1,terms+1):
            lam=2*j+arb(1)/2
            value+=((z-lam)*length).expm1()/((z-lam)*(lam*lam-helper.b**2))
        # For j>J, Re(z)<=3/2, lam-Re(z)>=j and lam²-b²>=4j².
        # Integral of each omitted absolute term is <=1/(4j³), whose
        # complete sum is <=1/(8J²) by the decreasing integral bound.
        radius=arb(1)/(8*terms**2)
        delta=arb(0,radius.upper())
        literal_enclosure=value+acb(delta,delta)
        accelerated=helper.gamma_incomplete(key,length)
        require(literal_enclosure.contains(accelerated),('literal complete gamma control',key,a))
        literal.append({'key':list(key),'length':a,'literal_terms':terms,
                        'complete_tail_bound':'1/(8*4096^2)','contains_new_ball':True})
    # Above the cutoff and on a complex length the reviewed source is used.
    for key,a in[(('i',105),acb('.5')),(('r',3),acb('.1','.001')),
                 (('r',4),acb('.1'))]:
        require(helper.gamma_incomplete(key,a).overlaps(old.gamma_incomplete(key,a)),
                'unchanged reviewed fallback consistency')
    here=Path(__file__).parent
    return {'status':'LOCAL_GAMMA_TAYLOR_DIRECTED_CONTROLS_ACCEPT',
      'scope':'finite implementation controls; analytic complete error theorem remains essential',
      'precision_bits':256,'closed_form_overlap_controls':controls,
      'literal_complete_integral_controls':literal,'series_cap_restored':True,
      'real_only_cutoff':'3/10','adaptive_degrees':[[32,128],[64,256],[64,512]],
      'sha256':{name:hashlib.sha256((here/name).read_bytes()).hexdigest() for name in
         ['taylor_convolution_source.py','LOCAL_GAMMA_TAYLOR_ENCLOSURE.md','check_local_gamma_taylor.py','source_convolution.py']}}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    data=run();a.out.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k!='closed_form_overlap_controls'},indent=2))
