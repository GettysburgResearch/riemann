"""Copy explicitly pinned source dependencies into this isolated packet."""
from pathlib import Path
import subprocess, json, hashlib

ROOT = Path(__file__).resolve().parent
PIN = 'c93ca65a510b6acaf167f929b9bf7e67d742b05a'
PREFIX = 'standalone/2026-10-18-theta20-and-native-cancellation/theta/'
FILES = ['connected_blocks.py','tree_core.py','theta_source.py','pr886_primitive.py',
         'parameters20.json','certify20.py','check_connected.py']

def main():
    dest=ROOT/'inherited';dest.mkdir(exist_ok=True)
    records=[]
    for name in FILES:
        content=subprocess.check_output(['git','show',PIN+':'+PREFIX+name],cwd=ROOT)
        (dest/name).write_bytes(content)
        records.append({'file':'inherited/'+name,'commit':PIN,'path':PREFIX+name,
                        'sha256':hashlib.sha256(content).hexdigest()})
    (ROOT/'INHERITED.json').write_text(json.dumps(records,indent=2)+'\n')

if __name__=='__main__':main()
