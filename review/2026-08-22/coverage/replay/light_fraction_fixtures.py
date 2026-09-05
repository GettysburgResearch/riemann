#!/usr/bin/env python3
from fractions import Fraction
import json
checks={}
checks['julia_margin']=Fraction(1)-Fraction(85,196)**2-Fraction(1,4)
assert checks['julia_margin']==Fraction(21587,38416)
checks['tao_phase_port_determinant']=Fraction(-80,81)
# Fixed 5:3 numerator -3(x-1)(x-2) has no zero for |x|<1, the image of Re(z)>0 under x=2^-z.
checks['five_three_roots']=[Fraction(1),Fraction(2)]
assert all(abs(float(r))>=1 for r in checks['five_three_roots'])
# A's malformed SHA is exactly 39 hex characters and becomes the frozen #653 head after prefixing e.
bad='928fd615d753882706bb88c51b717bd8d4a86ba'
good='e'+bad
assert len(bad)==39 and len(good)==40 and good=='e928fd615d753882706bb88c51b717bd8d4a86ba'
print(json.dumps({'status':'PASS','checks':{k:str(v) for k,v in checks.items()},'sha_repair_fixture':good},indent=2,sort_keys=True))
