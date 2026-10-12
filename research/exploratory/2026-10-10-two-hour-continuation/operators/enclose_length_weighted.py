#!/usr/bin/env python3
"""Fresh full-source weighted replay for the frozen physical21/20 R producer.
This verifies moments/matrix and provenance, not a second full R integration.
"""
import argparse,hashlib,json
from fractions import Fraction
from pathlib import Path
from flint import arb,arb_mat,ctx
from physical_length_source import OLD,PhysicalSource,build_length,projection_gram
from enclose_analytic_upper import require,positive_ldl
from check_window_family_log3 import certify as certify_family

PRODUCER='7da9c14f00654150acabd5815d49cd68ba577d3b4fc697d4f928a31a0893ecfb'
ADAPTER='b15da7904f2bdf4f4bc7e68b8dfe2f1de808bb0bac47a905d684c513dba24f1e'
LEGACY={'enclose_analytic_upper.py':'b3832a0cddc8bc1e2603c40240b608d1f06a868bda9436d8e88a146393fe007b',
        'source_convolution.py':'d53aa6c4e9c0e33d26c2327305bc1aa0ae9adef035ea4437ccd2a19b23bbf014',
        'taylor_convolution_source.py':'118e828d8bf4cb706fd94c9d179fb8d8de88319df8b20273c4e19284175af0da'}

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def balls(m):return [[m[i,j].str(65,more=True) for j in range(m.ncols())] for i in range(m.nrows())]

def verify(data):
    here=Path(__file__).parent
    require(data['producer_sha256']==PRODUCER==sha(here/'enclose_length_residual.py'),'frozen reviewed physical R producer')
    require(data['physical_source_adapter_sha256']==ADAPTER==sha(here/'physical_length_source.py'),'frozen physical source adapter')
    require(data['frozen_legacy_dependencies']==LEGACY,'complete frozen legacy dependency inventory')
    for name,h in LEGACY.items():require(sha(OLD/name)==h,('immutable source helper',name))
    require(data['taylor_gamma_helper_sha256']==LEGACY['taylor_convolution_source.py'],'frozen local gamma helper')
    require(data['exact_length']=='21/20','only physical length21/20')
    require(data['precision_bits']==256 and data['gauss_order']==76 and data['epsilon']=='2^-50','fixed continuum precision/order/epsilon')
    s=data['source_U_receipt']
    require(s['exact_length']=='21/20' and s['removed_sine_modes']==7 and s['trial_modes']==100 and s['precision_bits']==256,'fixed exact U/trial definition')
    require(s['physical_source_adapter_sha256']==ADAPTER,'source U adapter identity')
    require(s['physical_form_normalization']=='q=b*double_integral_on_[0,L]','physical native normalization')
    eps=Fraction(1,2**50)
    seen=0
    for segment in range(3):
        rows=sorted([r for r in data['coverage'] if r['segment']==segment],key=lambda r:Fraction(r['left']))
        require(bool(rows),'each physical source slab covered');previous=eps
        for row in rows:
            a,b=Fraction(row['left']),Fraction(row['right'])
            require(a==previous and 0<b-a<=Fraction(1,100),'exact capped panel adjacency')
            previous=b;seen+=1
        require(previous==1-eps,'exact terminal panel endpoint')
    require(seen==len(data['coverage'])==data['total_panels']==636,'complete fixed panel inventory')
    require(arb(data['endpoint_variation_bound'])<1,'full omitted interval modulus')
    L=arb(21)/20;mf=arb(data['uniform_F_bound'])
    require(arb(data['entrywise_FF_quadrature_error_total'])<4*L*mf.abs_upper()**2*arb((1,-152))+arb('1e-80'),'summed full FF Cauchy budget')
    require(arb(data['entrywise_Fp_quadrature_error_total'])<12*L*mf.abs_upper()*arb((1,-152))+arb('1e-80'),'summed full Fp Cauchy budget')
    return s

def enclose(path,last=128):
    require(last==128,'fixed complete weighted tail cutoff128')
    ctx.prec=256;data=json.loads(path.read_text());bound=verify(data)
    line=certify_family();ctx.prec=256
    L=arb(21)/20;source,u,coef,_=build_length(L,7,100)
    require(bound['length_ball']==L.str(65,more=True),'exact physical length ball')
    require(bound['exact_trial_z_coefficients_balls']==balls(coef),'fresh exact physical Galerkin coefficients')
    require(bound['U_matrix_balls']==balls(u),'fresh exact physical U matrix')
    source=PhysicalSource();tests=list(range(last+1))+['sinh']
    fc=arb_mat([source.basis_moment(test,7,100) for test in tests])*coef
    pp=arb_mat([[fc[i,j] for j in range(10)] for i in list(range(8))+[last+1]])
    gram=projection_gram(7,source);projection=gram.solve(pp)
    protected=arb_mat(last-7,10)
    for n in range(8,last+1):
        cross=source.b*((-1)**n*(source.b*L).cosh()-1)/(source.b**2+(arb.pi()*n/L)**2)
        for j in range(10):protected[n-8,j]=fc[n,j]-cross*projection[8,j]
    r=arb_mat([[arb(x) for x in row] for row in data['R_matrix_balls']])
    require(r.nrows()==r.ncols()==10,'complete physical R dimension10')
    first=arb(4)/5-244*L**2/(8*arb.pi())**2
    require(first>0,'positive full physical primitive weights')
    tail=1/(arb(4)/5-244*L**2/((last+1)*arb.pi())**2)
    cost=source.b*tail*r
    for n in range(8,last+1):
        delta=1/(arb(4)/5-244*L**2/(n*arb.pi())**2)-tail
        require(delta>0,'positive finite inverse-weight correction')
        for i in range(10):
            for j in range(10):cost[i,j]+=2*source.b/L*delta*protected[n-8,i]*protected[n-8,j]
    lower=(u-cost+(u-cost).transpose())/2;shift=arb('1e-11')
    pivots=positive_ldl(lower,shift)
    return {'status':'DIRECTED_PHYSICAL_LENGTH_WEIGHTED_LOWER_ACCEPT',
      'conditional_scope':'complete physical native length21/20 lower Schur bound, inheritedO1-O4; noRH',
      'exact_length':'21/20','R_receipt_path':str(path),'R_receipt_sha256':sha(path),'R_scalar_status':data['status'],
      'removed_sine_modes':7,'complement_dimension':10,'trial_modes':100,'precision_bits':256,'last_cosine_mode':128,
      'certified_finite_lower_eigenvalue':'1e-11','physical_parseval_factor':'2/L',
      'tail_inverse_weight_ball':tail.str(65,more=True),'primitive_line_certificate':line,
      'weighted_lower_matrix_balls':balls(lower),'shifted_LDL_pivots':[x.str(65,more=True) for x in pivots],
      'fresh_U_matrix_balls':balls(u),'exact_trial_z_coefficients_balls':balls(coef),
      'protected_high_cosine_moment_balls':balls(protected),'projection_F_moment_balls':balls(pp),
      'physical_source_adapter_sha256':ADAPTER,'frozen_legacy_dependencies':LEGACY,'producer_sha256':sha(Path(__file__)),
      'not_proved':['independent second fullR integration','uniform L2 gap','sign atlog3','all-window positivity','RH']}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('receipt',type=Path);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();r=enclose(a.receipt);a.out.write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({k:v for k,v in r.items() if k not in ['weighted_lower_matrix_balls','shifted_LDL_pivots','fresh_U_matrix_balls','exact_trial_z_coefficients_balls','protected_high_cosine_moment_balls','projection_F_moment_balls','primitive_line_certificate']},indent=2))
