"""Reconstruct the R=4.72 finite obligations without changing frozen files."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,tempfile

def main():
    root=Path(__file__).resolve().parent
    manifest=json.loads((root/'COMPONENT_HASHES.json').read_text(encoding='utf-8'))
    for row in manifest['files']:
        data=(root/row['path']).read_bytes()
        if len(data)!=row['bytes'] or hashlib.sha256(data).hexdigest()!=row['sha256']:
            raise RuntimeError('component integrity failure: '+row['path'])
    targets=['three-hour-type/verify_logistic_constants.py',
      'three-hour-boundary/verify_logistic_curvature.py',
      'three-hour-type/verify_logistic_poly12_constants.py',
      'three-hour-type/verify_logistic_negative_arch.py',
      'three-hour-boundary/verify_logistic_degree12_primes.py',
      'two-hour-root-20261023/verify_ford_prime_gain.py',
      'two-hour-root-20261023/verify_p12_472_fraction.py',
      'two-hour-global-20261023/verify_general_ford.py',
      'two-hour-root-20261023/verify_shifted_euler.py',
      'two-hour-global-20261023/verify_shifted_ford.py']
    records=[]
    with tempfile.TemporaryDirectory(prefix='riemann-weighted-replay-') as temp:
        dest=Path(temp)/'packet';shutil.copytree(root,dest,ignore=shutil.ignore_patterns('__pycache__'))
        for relative in targets:
            outputs=[]
            for optimized in (False,True):
                command=[sys.executable,'-I','-S','-B']+(['-O'] if optimized else [])+[str(dest/relative)]
                result=subprocess.run(command,cwd=dest,text=True,capture_output=True)
                if result.returncode:raise RuntimeError(relative+'\n'+result.stdout+result.stderr)
                outputs.append(result.stdout)
            if outputs[0]!=outputs[1]:raise RuntimeError('normal/optimized disagreement: '+relative)
            records.append({'checker':relative,'normal_and_optimized':'PASS','stdout_sha256':hashlib.sha256(outputs[0].encode()).hexdigest()})
            print('PASS '+relative,flush=True)
    print(json.dumps({'status':'PASS','scope':'R=4.72 finite arithmetic obligations only',
      'components_authenticated':len(manifest['files']),'checks':records},indent=2))

if __name__=='__main__':main()
