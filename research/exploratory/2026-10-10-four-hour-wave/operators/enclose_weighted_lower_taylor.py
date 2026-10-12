#!/usr/bin/env python3
"""Apply weighted primitive bound to the separately bound Taylor8 R receipt.

Original weighted checker remains frozen. New local gamma helper/provenance
requires its own independent review before acceptance.

The input's continuum integral enclosure must have been produced/reviewed;
this is a matrix/moment replay, not a second full integration replay.
"""
import argparse,hashlib,json
from fractions import Fraction
from pathlib import Path
from flint import arb,arb_mat,ctx
from enclose_analytic_upper import require,positive_ldl
from analytic_source_moments import moments
from check_codimension14 import certify as certify14
from check_codimension8_phase import certify as certify8


def clean_timing(value):
    if isinstance(value,dict):return {k:clean_timing(v) for k,v in value.items() if k!='elapsed_seconds'}
    if isinstance(value,list):return [clean_timing(v) for v in value]
    return value


def verify_coverage(data):
    epsilon=Fraction(1,2**int(data['epsilon'][3:]))
    seen=[]
    for segment in range(3):
        rows=sorted((x for x in data['coverage'] if x['segment']==segment),key=lambda x:Fraction(x['left']))
        require(bool(rows),'each literal source slab covered')
        previous=epsilon
        for row in rows:
            left,right=Fraction(row['left']),Fraction(row['right'])
            require(left==previous,'exact coverage adjacency')
            require(0<right-left<=Fraction(1,100),'positive capped panel width')
            previous=right
            seen.append(row)
        require(previous==1-epsilon,'exact coverage terminal endpoint')
    require(len(seen)==len(data['coverage'])==data['total_panels'],'complete coverage inventory')
    require(arb(data['endpoint_variation_bound'])<1,'endpoint modulus acceptance')
    mf=arb(data['uniform_F_bound'])
    require(arb(data['entrywise_FF_quadrature_error_total'])<4*mf.abs_upper()**2*arb((1,-2*data['gauss_order']))+arb('1e-80'),'summed Cauchy error budget')
    return str(epsilon)


def enclose(path,last=128,bits=256):
    ctx.prec=bits
    data=json.loads(path.read_text());coverage=verify_coverage(data)
    source=data['source_U_receipt'];removed=source['removed_sine_modes'];trial=source['trial_modes']
    require(removed==5,'supported reviewed primitive supporting line')
    frozen={11:('enclose_residual.py','e03d92bb09c1250b4a93e485aba6cc85bf2a4309b00e6d9217dbfbd39887cc92',60,80),
            5:('enclose_residual_phase8_taylor.py','f10b2dad34ab16aa6f66f4693093be60657b5d395432bf29f1af33ede8bf3256',50,76)}
    name,producer_hash,epsilon_bits,order=frozen[removed]
    require(data['producer_sha256']==producer_hash,'R receipt uses frozen reviewed continuum producer')
    require(hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()==producer_hash,'current continuum producer matches frozen review')
    require(data['epsilon']==f'2^-{epsilon_bits}' and data['gauss_order']==order,'frozen endpoint and Gaussian rule parameters')
    require(data['precision_bits']==256 and source['precision_bits']==256 and trial==100,'frozen directed trial precision/count')
    frozen_helpers={'enclose_analytic_upper.py':'b3832a0cddc8bc1e2603c40240b608d1f06a868bda9436d8e88a146393fe007b',
                    'source_convolution.py':'d53aa6c4e9c0e33d26c2327305bc1aa0ae9adef035ea4437ccd2a19b23bbf014',
                    'taylor_convolution_source.py':'118e828d8bf4cb706fd94c9d179fb8d8de88319df8b20273c4e19284175af0da'}
    for helper,expected in frozen_helpers.items():
        require(hashlib.sha256(Path(__file__).with_name(helper).read_bytes()).hexdigest()==expected,('frozen source helper',helper))
    require(data['taylor_gamma_helper_sha256']==frozen_helpers['taylor_convolution_source.py'],'R receipt local gamma helper frozen')
    require(source['source_sha256']==frozen_helpers['enclose_analytic_upper.py'],'R receipt sourceU producer frozen')
    certificate=certify8() if removed==5 else certify14()
    ctx.prec=bits
    alpha=arb(4)/5 if removed==5 else arb(13)/10
    constant=244 if removed==5 else 710
    mm=moments(removed,trial,bits,last)
    require(source['source_sha256']==mm['source_U_receipt']['source_sha256'],'identical reviewed source U producer')
    require(source['exact_trial_z_coefficients_balls']==mm['source_U_receipt']['exact_trial_z_coefficients_balls'],'identical exact trial definitions')
    dim=removed+3
    r=arb_mat([[arb(x) for x in row] for row in data['R_matrix_balls']])
    u=arb_mat([[arb(x) for x in row] for row in mm['source_U_receipt']['U_matrix_balls']])
    require(r.nrows()==r.ncols()==u.nrows()==dim,'matching complete matrix dimension')
    fc=arb_mat([[arb(x) for x in row] for row in mm['protected_high_cosine_moment_balls']])
    lam_first=alpha-constant/(arb.pi()*(removed+1))**2
    require(lam_first>0,'positive full primitive weight family')
    tail=1/(alpha-constant/(arb.pi()*(last+1))**2)
    b=arb(3)/2
    cost=b*tail*r
    for n in range(removed+1,last+1):
        coefficient=1/(alpha-constant/(arb.pi()*n)**2)-tail
        require(coefficient>0,'positive finite inverse-weight correction')
        row=n-removed-1
        for i in range(dim):
            for j in range(dim):
                cost[i,j]+=2*b*coefficient*fc[row,i]*fc[row,j]
    lower=(u-cost+(u-cost).transpose())/2
    shift=arb('1e-11')
    pivots=positive_ldl(lower,shift)
    return {'status':'DIRECTED_WEIGHTED_SINGLE_WINDOW_LOWER_ACCEPT',
      'conditional_scope':'literal L=1 full-source Schur lower bound conditional inheritedO1-O4; notRH',
      'R_receipt_path':str(path),'R_receipt_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
      'R_status':data['status'],'exact_normalized_coverage_epsilon':coverage,
      'complement_dimension':dim,'removed_sine_modes':removed,'trial_modes':trial,
      'last_cosine_mode':last,'precision_bits':bits,'certified_lower_eigenvalue':'1e-11',
      'tail_inverse_weight_upper':tail.str(45,more=True),
      'weighted_lower_matrix_balls':[[lower[i,j].str(45,more=True) for j in range(dim)] for i in range(dim)],
      'shifted_LDL_pivots':[x.str(45,more=True) for x in pivots],
      'fresh_source_moment_receipt':clean_timing(mm),'primitive_line_certificate':certificate,
      'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'trust_base':'reviewed full directed R producer plus Arb outward source/moment/matrix arithmetic',
      'not_proved':['independent fullR runtime replay','all windows','xi/Weil terminal adapter','RH']}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('receipt',type=Path);p.add_argument('--last',type=int,default=128)
    p.add_argument('--bits',type=int,default=256);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();r=enclose(a.receipt,a.last,a.bits);a.out.write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({k:v for k,v in r.items() if k not in ['weighted_lower_matrix_balls','shifted_LDL_pivots','fresh_source_moment_receipt','primitive_line_certificate']},indent=2))
