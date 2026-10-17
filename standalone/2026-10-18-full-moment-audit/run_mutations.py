"""Execute genuinely corrupted diagnostic variants in optimized Python."""
import json
from pathlib import Path
import subprocess
import sys

CASES = {
 'drop-square-mask':'quadratic-square-removal',
 'impose-coprimality':'quadratic-square-removal',
 'collapse-product-length':'ordered-products',
 'omit-row-sixth-copies':'native-complete-rows',
 'substitute-conductor':'dual-conductor-identity',
 'drop-holder-cost':'Holder-support-price',
 'false-critical-anchor':'diagonal-anchor',
 'drop-subunit-tail':'subunit-tail',
}

def main():
    here=Path(__file__).resolve().parent
    results=[]
    for name,expected in CASES.items():
        p=subprocess.run([sys.executable,'-O','verify.py','--mutate',name],
                         cwd=here,capture_output=True,text=True,timeout=30)
        if p.returncode==0 or expected not in p.stderr:
            raise ValueError('Mutation did not fail at intended gate: '+name+'\n'+p.stderr)
        results.append({'mutation':name,'exit_code':p.returncode,'rejected_by':expected})
    print(json.dumps({'status':'all eight separately executed corruptions rejected','cases':results},indent=2,sort_keys=True))

if __name__=='__main__':main()
