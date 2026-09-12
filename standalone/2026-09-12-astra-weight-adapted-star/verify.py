"""STAR26 full reconstruction. Python standard library; no stored source inputs.

--emit is a producer, not a verifier. --check reconstructs every native integral
and both fixed-point certificates, then strictly compares the complete receipt.
--self-test uses that freshly reconstructed receipt for eight comparison refusals
and one duplicate-key refusal; these are NOT nine fresh numerical CLI replays.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
from fractions import Fraction as F
from ball_core import B, Q, PI, ONE, exp, rad, sqrt_real
from native_source import primitive,standardized,LEFT,RIGHT,FOURIER
from star import COUNTS,ACTIVE,root_certificate,harmonic_tail
from controls import run as algebra_controls

ROOT=Path(__file__).resolve().parent


def require(ok,msg):
    if not ok:raise ValueError(msg)


def pairs(items):
    out={}
    for k,v in items:
        if k in out:raise ValueError('duplicate JSON key')
        out[k]=v
    return out


def nofloat(s):raise ValueError('floating JSON is outside the certificate contract')


def loads(s):return json.loads(s,object_pairs_hook=pairs,parse_float=nofloat,parse_constant=nofloat)


def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()


def encode(b):return [b.a,b.b,b.e]


def lower(b):return F(b.a-b.e,Q)


def upper(b):return F(b.a+b.e,Q)


def interval(lo,hi):
    require(lo<=hi,'invalid real interval')
    mid=(lo+hi)/2
    return B.real(mid).grow(rad((hi-lo)/2))


def authenticate():
    lines=(ROOT/'SHA256SUMS').read_text().splitlines()
    names=[]
    for line in lines:
        digest,name=line.split('  ')
        require('/' not in name and name not in names,'manifest name')
        p=ROOT/name
        require(not p.is_symlink() and p.is_file(),'nonregular payload')
        require(hashlib.sha256(p.read_bytes()).hexdigest()==digest,'payload hash: '+name)
        names.append(name)
    actual=sorted(p.name for p in ROOT.iterdir() if p.name!='SHA256SUMS')
    require(actual==sorted(names),'complete packet inventory')
    return len(names)


def parameters():
    p=loads((ROOT/'parameters.json').read_text())
    require(set(p)=={'schema','counts','active','centers','radius','bias_rule','tail_start','provenance'},'parameter keys')
    require(p['schema']=='STAR26 parameters v1','parameter schema')
    require(canonical(p['counts'])==canonical(list(COUNTS)),'group multiplicities')
    require(canonical(p['active'])==canonical(list(ACTIVE)),'active coordinates')
    require(p['bias_rule']=='tanh(J_i)=a_i/100','literal bias rule')
    require(type(p['tail_start']) is int and p['tail_start']==10**40,'entire harmonic tail start')
    require(type(p['radius']) is str and F(p['radius'])==F(1,10**24),'root-box radius')
    require(type(p['centers']) is list and len(p['centers'])==10,'root-box centers')
    require(all(type(x) is str and len(x)<=150 for x in p['centers']),'rational center format')
    centers=[F(x) for x in p['centers']]
    return p,centers


def reconstruct(progress=False):
    params,centers=parameters()
    require(lower(PI)>3 and upper(PI)<4,'pi bounds')
    require(lower(exp(3))>16,'entire-tail exponential bound')
    raw,ff,coverage=primitive(progress)
    mu,ku,var=standardized(raw)
    require(F(1,25)<lower(var) and upper(var)<F(1,20),'native variance')
    finite,weights,diff=root_certificate(centers,ku,mu)
    tails,tail_bounds=harmonic_tail(params['tail_start'])
    infinite,_,idiff=root_certificate(centers,ku,mu,tail=tails)
    for d in (diff,idiff):
        require(F(-115,1000)<lower(d) and upper(d)<F(-114,1000),'unmatched sixteenth moment')
    for r in (finite,infinite):
        require(F(r['delta_dyadic_upper'],Q)<F(1,10**28),'center displacement bound')
        require(F(r['contraction_dyadic_upper'],Q)<F(1267,10**14),'whole-box derivative bound')
    require(F(finite['delta_dyadic_upper'],Q)<F(4481,10**64),'finite displacement bound')
    require(F(infinite['delta_dyadic_upper'],Q)<F(1337,10**32),'harmonic displacement bound')
    require(lower(ff[0])>F(5,10**18) and upper(ff[0])<F(6,10**18),'left native sign')
    require(lower(ff[1])>F(-9,10**18) and upper(ff[1])<F(-8,10**18),'right native sign')
    require(upper(raw[0]*raw[2])<1,'uniform Fourier derivative bound')
    triple=ff[2].grow(rad(F(3,2)*(RIGHT-LEFT)))
    require(upper(triple)<F(-29,10**13),'entire triple interval is zero-free')
    slo=sqrt_real(lower(var));shi=sqrt_real(upper(var))
    sigma=interval(lower(slo),upper(shi))
    physical=[sigma*a for a in weights]
    couplings=[]
    for a in weights[:-1]:
        m=a/100
        # m < atanh(m) < m/(1-m^2), 0<m<1; whole root box.
        j=interval(lower(m),upper(m/(ONE-m*m)))
        require(lower(j)>F(4,10000) and upper(j)<F(4,1000),'strict ferromagnetic edges')
        couplings.append(encode(j))
    return {'schema':'STAR26 receipt v1','status':'PROPOSED; independent review required',
        'rh_proved':False,'all_order_realization_proved':False,
        'finite_spin_count':96,'finite_edge_count':95,'matched_even_orders':list(range(2,15,2)),
        'finite_algebra_controls':algebra_controls(),
        'bits':512,'parameters_sha256':hashlib.sha256((ROOT/'parameters.json').read_bytes()).hexdigest(),
        'raw_moments':{str(k):encode(v) for k,v in raw.items()},
        'standardized_moments':{str(k):encode(mu[k]) for k in range(0,17,2)},
        'standardized_cumulants':{str(k):encode(ku[k]) for k in range(2,17,2)},
        'variance':encode(var),'source_coverage':coverage,
        'fourier':{'arguments':[str(x) for x in FOURIER],'values':[encode(x) for x in ff],
            'triple_interval_value':encode(triple),'zero_claim':'some real zero in (LEFT,RIGHT); its triple is not a zero'},
        'finite_root':finite,'harmonic_root':infinite,
        'harmonic_tail':{'start':10**40,'amplitude':'1/(2 sqrt(native variance))',
            'conditional_cumulant_bounds':[str(x) for x in tail_bounds[1:]],
            'same_leading_MGF_growth':True,'complete_theta_identification':False},
        'finite_physical_weights':[encode(x) for x in physical],
        'finite_edge_coupling_enclosures':couplings}


def binding_receipt(result):
    """Readable receipt binding the ENTIRE freshly reconstructed exact record.
    Every stated inequality has already been checked by reconstruct().
    --dump-full exports all native balls, tails and root-enclosure data.
    """
    return {
        'schema':'STAR26 binding receipt v1',
        'reconstruction_sha256':hashlib.sha256(canonical(result)+b'\n').hexdigest(),
        'parameters_sha256':result['parameters_sha256'],
        'rh_proved':False,'all_order_realization_proved':False,
        'status':result['status'],'finite_spin_count':96,'finite_edge_count':95,
        'matched_even_orders':result['matched_even_orders'],
        'bits':512,'source_cells':192,'source_degree':128,'theta_indices':10,
        'expanded_source_terms':667,'pointwise_bounded_source_terms':1253,
        'raw_moment_orders':list(range(0,17,2)),'fourier_values_reconstructed':3,
        'root_box_radius':'1/1000000000000000000000000',
        'finite_displacement_upper':'4481/10^64',
        'harmonic_displacement_upper':'1337/10^32',
        'both_row_sum_contraction_upper':'1267/10^14',
        'both_sixteenth_moment_difference_interval':['-115/1000','-114/1000'],
        'finite_edge_coupling_interval':['4/10000','4/1000'],
        'harmonic_start':10**40,'harmonic_amplitude':'1/(2 sqrt(native variance))',
        'same_leading_MGF_growth':True,'complete_theta_identification':False,
        'native_zero_control':'some real gamma in (14.13472514173469,14.13472514173470), Xi(3 gamma)<-2.9e-12',
        'finite_algebra_controls':result['finite_algebra_controls'],
        'exact_inverse_identities_per_root':98,
        'full_record_export':'verify.py --check result.json --dump-full PATH_OUTSIDE_PACKET'
    }


def compare(expected,received):
    require(canonical(expected)==canonical(received),'complete reconstruction does not match receipt')


def self_test(expected):
    changes=[
        lambda x:x.update(rh_proved=True),
        lambda x:x.update(all_order_realization_proved=True),
        lambda x:x.update(finite_spin_count=95),
        lambda x:x.update(finite_edge_count=True),
        lambda x:x['matched_even_orders'].append(16),
        lambda x:x['source_coverage'].update(cells=191),
        lambda x:x['harmonic_tail'].update(complete_theta_identification=True),
        lambda x:x['raw_moments']['0'].__setitem__(0,x['raw_moments']['0'][0]+1),
    ]
    compare(expected,loads(canonical(expected)))
    for alter in changes:
        bad=copy.deepcopy(expected);alter(bad)
        try:compare(expected,bad)
        except ValueError:pass
        else:raise RuntimeError('changed receipt was accepted')
    try:loads('{"x":0,"x":1}')
    except ValueError:pass
    else:raise RuntimeError('duplicate-key JSON accepted')
    return {'pristine_comparison_acceptances':1,'changed_receipt_refusals':8,'duplicate_key_refusals':1}


def main():
    a=argparse.ArgumentParser(description=__doc__)
    g=a.add_mutually_exclusive_group(required=True)
    g.add_argument('--emit',type=Path);g.add_argument('--check',type=Path)
    a.add_argument('--self-test',action='store_true');a.add_argument('--progress',action='store_true');a.add_argument('--dump-full',type=Path)
    args=a.parse_args()
    if args.check:print('authenticated payloads:',authenticate(),flush=True)
    result=reconstruct(args.progress)
    data=canonical(result)+b'\n'
    if args.emit:
        args.emit.write_bytes(canonical(binding_receipt(result))+b'\n');print('PRODUCED; not a stored-receipt verification')
    else:
        compare(binding_receipt(result),loads(args.check.read_text()));print('FULL RECONSTRUCTION PASS')
    if args.dump_full:
        require(ROOT not in args.dump_full.resolve().parents,'dump the full record outside the packet')
        args.dump_full.write_bytes(data)
    if args.self_test:print(json.dumps(self_test(result),sort_keys=True))
    print('sha256:',hashlib.sha256(data).hexdigest())
    print('finite delta upper:',result['finite_root']['delta_dyadic_upper']/Q)
    print('harmonic delta upper:',result['harmonic_root']['delta_dyadic_upper']/Q)
    print('whole-box q upper:',max(result[t]['contraction_dyadic_upper'] for t in ('finite_root','harmonic_root'))/Q)
    print('sixteenth difference:',B(*result['finite_root']['sixteenth_difference']))

if __name__=='__main__':main()
