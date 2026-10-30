"""Retune the prior staged candidate in an isolated source tree, with input hashes pinned."""
import argparse, hashlib
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument('--baseline-src',required=True,help='Prior 0.8738702 candidate source tree')
p.add_argument('--out-src',required=True,help='Isolated candidate source tree')
a=p.parse_args();baseline=Path(a.baseline_src);out=Path(a.out_src)
files={
'Submissions/arvi_density/Return/Constants.lean':'70f31c0dd798cc558a31d4bcac51d052683436bfaab37d7906256d2818d8ef47',
'Submissions/arvi_density/Return/Endpoint.lean':'c690324cde8470940c970b604dc431d2028b09178958892f9d8b7dddb701c98c',
'Submissions/arvi_density/FinalF50.lean':'f9084f0a5978c6e9d8869d7ad7893582a9f198c2546c0522c1dfc539ccec290c',
'Candidate/Main.lean':'386e1af04c8a66f201e5b8b3a7ec8420cad47c4e5b0c7bff7e67c4cd29edc8a3'}
const_changes={'4369351/5000000':'4369347/5000000','630649/5000000':'630653/5000000','1007/1250':'80599/100000','641947/3750000':'641959/3750000','1370947/3750000':'2738993/7500000','868553/1875000':'3477089/7500000','1869351/2500000':'1869347/2500000','8056000001/10000000000':'8059900001/10000000000','6250/5608053':'6250/5608041','624212/16824159':'627089/16824123','163969805423850671/3377250000000000000':'164527223040750671/3377250000000000000'}
for filename,digest in files.items():
 raw=(baseline/filename).read_bytes();assert hashlib.sha256(raw).hexdigest()==digest,filename
 text=raw.decode()
 if filename.endswith('Constants.lean'):
  for old,new in const_changes.items():
   assert old in text,(filename,old);text=text.replace(old,new)
 else:
  text=text.replace('4369351 / 5000000','4369347 / 5000000').replace('4369351/5000000','4369347/5000000').replace('0.8738702','0.8738694')
 target=out/filename;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(text)
 print('generated',target)
