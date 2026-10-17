#!/usr/bin/env python3
"""Exact exponent/contour certificate. Does NOT verify imported analytic theorems."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as Q
from pathlib import Path

KEYS = {'alpha','beta','normalization','sigma_zero','sigma_good',
        'exception_exponent','w_line','z_line','delta','small_cutoff',
        'large_cutoff','large_z','principal_w','principal_z','total_loss',
        'claimed_saving'}

class CertificateError(ValueError):
    pass

def require(ok: bool, message: str) -> None:
    if not ok:
        raise CertificateError(message)

def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f'duplicate key: {key}')
        result[key] = value
    return result

def read_parameters(path: Path) -> dict[str,Q]:
    raw = json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique_object)
    require(isinstance(raw, dict) and set(raw)==KEYS, 'parameter fields differ')
    require(all(isinstance(v,str) for v in raw.values()), 'rational strings required')
    return {k: Q(v) for k,v in raw.items()}

def domain(x:Q, y:Q, z:Q) -> dict[str,Q]:
    return {'x':x, 'y':y, 'z':z, '6z+y-1':6*z+y-1,
            'x+6z-1':x+6*z-1, 'x+y-1':x+y-1,
            'x+y+6z-2':x+y+6*z-2,'6x+6z-5':6*x+6*z-5,
            'x-1/2':x-Q(1,2),'3x-2':3*x-2,'3x+y-5/2':3*x+y-Q(5,2)}

def margins(p:dict[str,Q]) -> dict[str,Q]:
    a,b=p['alpha'],p['beta']; h=1-a; C=a/2+h/6
    x1=1+p['delta']; y,z=p['w_line'],p['z_line']
    def E(x,y,z): return a/2+x-1+h*z+b*(y-1)
    def U(nu): return nu+(1-y)/2-z
    return {
        'theta': C-(a+b/2-Q(1,2)),
        'principal_w': C-E(x1,p['principal_w'],Q(1,6)+p['delta']),
        'principal_z': C-E(x1,Q(1),p['principal_z']),
        'small': C-E(x1,y,z)-p['small_cutoff']*U(Q(1)),
        'exceptional': C-E(x1,y,z)-p['large_cutoff']*U(p['exception_exponent']),
        'good': C-E(p['sigma_good'],y,z)-p['large_cutoff']*U(Q(1)),
        'large': C-E(Q(4),Q(4),p['large_z'])-p['large_cutoff']*(1-p['large_z'])
    }

def validate(p:dict[str,Q]) -> dict:
    a,b=p['alpha'],p['beta']; h=1-a; C=a/2+h/6
    require(0<b<a<1 and a+b>1, 'theta scale assumptions fail')
    require(p['normalization']==1-C, 'Mellin normalization does not match scales')
    s=p['sigma_zero']; n=6; q=2*s-1
    require(Q(2,3)<s<Q(11,12), 'sixth-order middle density branch required')
    den=n*q*(2*(n-1)-n*q)-2*(n-1)
    xm=(n*q*(n-2)-(n-1))/den
    yd=(n*q*(2*n-5)-2*(n-2))/den
    # Independently substitute every term of the detector, not just its closed answer.
    first = [(Q(1,2)-s)*yd+(1+v)/2
             for v in [xm,Q(1),Q(5,6)+xm/3,Q(1,3)+5*xm/6]]
    terms = first + [(2-2*s)*yd,1+(1-2*s)*xm]
    terms += [Q(1,3)+(Q(11,6)-2*s)*v for v in [xm,yd]]
    terms += [Q(5,6)+(Q(4,3)-2*s)*v for v in [xm,yd]]
    g = ((2*n-3)*q*(n+1-n*q)-2*(n-1))/den
    closed = 1-q*(q*n*n-(6*s-2)*n+3)/(q*(3-2*s)*n*n-4*s*n+2)
    require(Q(1,2)<xm<1<yd<2, 'mollifier/detector cutoffs outside range')
    require(max(terms)==g==closed, 'zero-density term reconstruction fails')
    require(g<p['exception_exponent']<1, 'exception exponent not above imported density')
    # All height exponents are linear in d; compare their coefficients, for every d.
    zh=1/(6-4*s)
    ht=[(Q(1,2)-s)*zh+Q(1,4),(2-2*s)*zh,Q(0),
        (Q(11,6)-2*s)*zh,(Q(4,3)-2*s)*zh]
    hd=(1-s)/(3-2*s)
    require(max(ht)==hd, 'height exponent reconstruction fails')
    require(p['sigma_good']>s, 'no good-rectangle buffer')
    x1=1+p['delta']; xg=p['sigma_good']; y=p['w_line']; z=p['z_line']
    require(0<p['small_cutoff']<h<p['large_cutoff'], 'frequency cutoffs not separated')
    require(p['large_z']>2, 'large contour must move right')
    require(z>Q(1,6) and 0<p['principal_z']<Q(1,6), 'z-pole directions fail')
    require(p['principal_w']<1<x1, 'w-pole directions fail')
    require(1+(1-y)/2-z>0 and p['exception_exponent']+(1-y)/2-z>0,
            'cannot bound U powers at upper endpoints')
    vertices = {
        'initial':(Q(4),Q(4),Q(2)),
        'absolute_x':(x1,Q(4),Q(2)),
        'principal_start_w':(x1,x1,Q(2)),
        'principal_start_z':(x1,x1,Q(1,6)+p['delta']),
        'principal_w_remainder':(x1,p['principal_w'],Q(1,6)+p['delta']),
        'principal_w_residue':(x1,Q(1),Q(1,6)+p['delta']),
        'principal_z_remainder':(x1,Q(1),p['principal_z']),
        'nonprincipal_good_x':(xg,Q(4),Q(2)),
        'nonprincipal_good_z':(xg,Q(4),z),
        'nonprincipal_good_w':(xg,y,z),
        'nonprincipal_bad_z':(x1,Q(4),z),
        'nonprincipal_bad_w':(x1,y,z),
        'large':(Q(4),Q(4),p['large_z'])}
    dm={name:domain(*xyz) for name,xyz in vertices.items()}
    for name,values in dm.items():
        require(min(values.values())>0,f'correction domain fails at {name}')
    # These radii are for the stated certificate's sigma values.
    radii=[Q(999,1000),Q(11799,10000),Q(47197,40000),Q(23599,20000)]
    require(radii==sorted(radii) and len(set(radii))==4, 'reciprocal radii not nested')
    require(2-radii[-1]>s and 2-radii[1]<=xg, 'reciprocal disks do not cover target')
    mm=margins(p)
    spare={key:value-p['total_loss']-p['claimed_saving'] for key,value in mm.items()}
    require(p['total_loss']>0,'positive total loss required')
    require(min(spare.values())>0, 'claimed saving not paid by all terms')
    boundary=p['normalization']+C-p['claimed_saving']
    require(boundary==1-p['claimed_saving']<Q(31,32),'no zero-free improvement')
    return {
        'scope':'Exact finite arithmetic only; analytic inputs and family adapter require mathematical review.',
        'density':{'sigma':s,'mollifier_exponent':xm,'detector_exponent':yd,
                   'all_N_exponents':terms,'maximum':g,'chosen_exception':p['exception_exponent'],
                   'height_coefficient_in_d':hd,'all_height_coefficients_in_d':ht},
        'scales':{'alpha':a,'beta':b,'M':a+b,'h':h,'C':C,'b':p['normalization'],
                  'theta_exponent':a+b/2-Q(1,2),'f_growth':C-p['claimed_saving'],
                  'zero_free_boundary':boundary},
        'margins':mm,'spare_after_total_loss':spare,
        'domain_vertices':len(vertices),'strict_domain_inequalities':len(vertices)*11,
        'domain_margins':dm,'reciprocal_radii':radii}

def serial(obj):
    if isinstance(obj,Q): return str(obj)
    if isinstance(obj,dict): return {k:serial(v) for k,v in obj.items()}
    if isinstance(obj,(tuple,list)): return [serial(x) for x in obj]
    return obj

def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--parameters',type=Path,default=Path(__file__).with_name('parameters.json'))
    args=parser.parse_args()
    try:
        result=validate(read_parameters(args.parameters))
    except (CertificateError,ValueError,TypeError,OSError) as exc:
        parser.exit(1,f'REJECTED: {exc}\n')
    print(json.dumps(serial(result),indent=2,sort_keys=True))

if __name__=='__main__':
    main()
