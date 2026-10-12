#!/usr/bin/env python3
"""Reject stale/old R producer and stale gamma helper in the new contract.

All inputs here are synthetic diagnostics with a real exact U definition and
full exact coverage. None claims to contain a valid continuum Gram integral.
"""
import hashlib,json
from pathlib import Path
from enclose_residual_phase8_taylor import panels
from enclose_weighted_lower_taylor import enclose
from enclose_analytic_upper import require


def run():
    here=Path(__file__).parent
    source=json.loads((here/'directed_upper_codim8_trial100.json').read_text())
    coverage=[{'segment':s,'left':str(a),'right':str(b)} for s in range(3) for a,b in panels()]
    producer='f10b2dad34ab16aa6f66f4693093be60657b5d395432bf29f1af33ede8bf3256'
    helper='118e828d8bf4cb706fd94c9d179fb8d8de88319df8b20273c4e19284175af0da'
    base={'epsilon':'2^-50','coverage':coverage,'total_panels':len(coverage),
      'endpoint_variation_bound':'.0002','uniform_F_bound':'6e14',
      'entrywise_FF_quadrature_error_total':'0','gauss_order':76,'precision_bits':256,
      'source_U_receipt':source,'producer_sha256':producer,
      'taylor_gamma_helper_sha256':helper,'status':'SYNTHETIC_PROVENANCE_NEGATIVE_CONTROL'}
    cases=[('stale_producer','producer_sha256','0'*64,
            'R receipt uses frozen reviewed continuum producer'),
           ('old_reviewed_producer','producer_sha256',
            'a670ceaa43de2a1c7ad96f4798af15e49a8ddf851362bcfc0ff7304c9bd99f1f',
            'R receipt uses frozen reviewed continuum producer'),
           ('stale_gamma_helper','taylor_gamma_helper_sha256','0'*64,
            'R receipt local gamma helper frozen')]
    path=here/'.stale_Taylor_R_negative_control.json';receipts=[]
    try:
        for name,key,value,expected in cases:
            data=dict(base);data[key]=value;path.write_text(json.dumps(data))
            try:
                enclose(path)
            except ArithmeticError as error:
                require(str(error)==expected,('correct provenance rejection',name,str(error)))
                receipts.append({'case':name,'rejection':str(error)})
            else:
                raise ArithmeticError(('invalid source binding accepted',name))
    finally:
        if path.exists():path.unlink()
    return {'status':'TAYLOR_SOURCE_BINDING_NEGATIVE_CONTROLS_ACCEPT',
      'scope':'synthetic diagnostics; no continuum integral or effective sign claimed',
      'full_exact_coverage_panels':len(coverage),'same_exact_U_definition':True,
      'rejections':receipts,'sha256':{name:hashlib.sha256((here/name).read_bytes()).hexdigest()
        for name in['check_weighted_taylor_provenance.py','enclose_weighted_lower_taylor.py',
                    'enclose_residual_phase8_taylor.py','taylor_convolution_source.py']}}


if __name__=='__main__':print(json.dumps(run(),indent=2))
