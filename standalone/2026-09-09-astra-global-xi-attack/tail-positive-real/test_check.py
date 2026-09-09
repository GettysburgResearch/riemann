"""Actual CLI rejection controls for TPR26; no analytic theorem is proved here."""
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse,hashlib,json,shutil,subprocess,sys,unittest
ROOT=Path(__file__).resolve().parent
FLAGS=['-O'] if sys.flags.optimize else []
PARENT=ROOT.parent

def seal(root):
    names=sorted(p.name for p in root.iterdir() if p.name!='SHA256SUMS')
    (root/'SHA256SUMS').write_text(''.join(hashlib.sha256((root/n).read_bytes()).hexdigest()+'  '+n+'\n' for n in names))

def receipt(root,change):
    p=root/'verification.json';v=json.loads(p.read_text());change(v)
    p.write_text(json.dumps(v,sort_keys=True,indent=2)+'\n');seal(root)

def replace(root,path,before,after,reseal=True):
    p=root/path;s=p.read_text()
    if s.count(before)!=1:raise RuntimeError('mutation must change exactly one source location')
    p.write_text(s.replace(before,after))
    if reseal:seal(root)

class Checks(unittest.TestCase):
    def run_case(self,mutator=None):
        with TemporaryDirectory() as tmp:
            base=Path(tmp)/'parent';base.mkdir()
            for name in ['GLOBAL_ATTEMPT.md','certify_truncation.py','root_certificate.json']:
                shutil.copy2(PARENT/name,base/name)
            root=base/'tail-positive-real';shutil.copytree(ROOT,root)
            if mutator:mutator(root,base)
            p=subprocess.run([sys.executable,'-I','-S','-B',*FLAGS,str(root/'check.py')],
                             capture_output=True,timeout=30)
            if mutator:
                self.assertNotEqual(p.returncode,0,p.stdout.decode())
            else:
                self.assertEqual(p.returncode,0,p.stderr.decode())
                self.assertEqual(p.stdout,(root/'verification.json').read_bytes())
    def test_pristine(self):self.run_case()
    def test_resealed_semantic_results(self):
        cases=[
          lambda v:v.update(rh_proved=True),
          lambda v:v.update(full_laguerre_sign_proved=True),
          lambda v:v.update(uniform_relative_error_constant=255),
          lambda v:v.update(rh_proved=0),
          lambda v:v['disk_transfer'].update(complete_xi_real_lower='1'),
          lambda v:v['disk_transfer'].update(radius='1/10'),
        ]
        for change in cases:
            with self.subTest(change=cases.index(change)):
                self.run_case(lambda r,b:receipt(r,change))
    def test_resealed_source_and_binding(self):
        cases=[
          lambda r,b:replace(r,'check.py','[0,-6,4]','[0,-5,4]'),
          lambda r,b:replace(r,'check.py','moment==123','moment==122'),
          lambda r,b:replace(r,'SOURCE_LOCK.json','815ccae329a17327b873d21f05bc30c24db13e7e','0000000000000000000000000000000000000000'),
          lambda r,b:(b/'certify_truncation.py').write_bytes((b/'certify_truncation.py').read_bytes()+b'\n# changed\n'),
        ]
        for j,change in enumerate(cases):
            with self.subTest(case=j):self.run_case(change)
    def test_structure_and_types(self):
        def duplicate(r,b):
            p=r/'verification.json';s=p.read_text();p.write_text(s.replace('{','{"schema":"duplicate",',1));seal(r)
        def floating(r,b):
            replace(r,'verification.json','"uniform_relative_error_constant": 256','"uniform_relative_error_constant": 256.0')
        def link(r,b):
            p=r/'PROOF.md';outside=b/'copy.md';p.rename(outside);p.symlink_to(outside)
        cases=[duplicate,floating,
          lambda r,b:(r/'PROOF.md').write_bytes((r/'PROOF.md').read_bytes()+b'changed'),
          lambda r,b:(r/'README.md').unlink(),
          lambda r,b:(r/'EXTRA').write_text('unexpected'),
          lambda r,b:(r/'SHA256SUMS').write_text(''),link]
        for j,change in enumerate(cases):
            with self.subTest(case=j):self.run_case(change)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--parent',type=Path)
    args,rest=parser.parse_known_args()
    if args.parent:PARENT=args.parent
    unittest.main(argv=[sys.argv[0],*rest],verbosity=2)
