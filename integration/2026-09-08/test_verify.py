#!/usr/bin/env python3
"""Synthetic regression tests for candidate bookkeeping; not source theorem tests."""
from __future__ import annotations
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('candidate_verify', HERE / 'verify.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class CandidateTests(unittest.TestCase):
    def test_duplicate_json(self):
        with self.assertRaises(ValueError): v.decode(b'{"x":1,"x":2}')

    def test_nonfinite_json(self):
        for value in ['NaN','Infinity','-Infinity']:
            with self.assertRaises(ValueError): v.decode('{"x":'+value+'}')

    def test_paths(self):
        self.assertEqual(v.safe_name('a/b.md'), 'a/b.md')
        for name in ['', '../x', '/x', 'a/../x', 'a//x', 'a/./x', '.git/config', 'C:x', 'a\\b', 'a\n']:
            with self.assertRaises(ValueError): v.safe_name(name)

    def test_posix_navigation(self):
        self.assertEqual(v.link_target('a/b/c.md','../../RESULTS.md#scope'), ('RESULTS.md','scope'))
        self.assertEqual(v.link_target('a/c.md','#same'), ('a/c.md','same'))
        self.assertEqual(v.link_target('a/c.md','/README.md'), ('README.md',''))
        with self.assertRaises(ValueError): v.link_target('README.md','../outside')
        with self.assertRaises(ValueError): v.link_target('README.md','javascript:alert')

    def test_anchor_semantics(self):
        a = v.anchors('# Same\n## Same\n<a id="explicit"></a>\n```\n# Hidden\n```\n## $X$ and naïve\n')
        self.assertEqual(a, {'same','same-1','explicit','x-and-naïve'})

    def test_preservation(self):
        old={'README.md':('100644','blob','a'), 'formal/A.lean':('100644','blob','b')}
        cur=dict(old, **{'README.md':('100644','blob','c'),'new/good.md':('100644','blob','d')})
        v.check_preservation(old,cur,['new'])
        for change in ['delete','formal','outside']:
            bad=dict(cur)
            if change=='delete': del bad['formal/A.lean']
            if change=='formal': bad['formal/A.lean']=('100644','blob','e')
            if change=='outside': bad['other.md']=('100644','blob','f')
            with self.assertRaises(ValueError): v.check_preservation(old,bad,['new'])

    def test_tsv_schema(self):
        self.assertEqual(v.rows(b'a\tb\n1\t2\n'),[{'a':'1','b':'2'}])
        for data in [b'a\ta\n1\t2\n', b'a\tb\n1\n', b'a\n1\t2\n', b'a\n']:
            with self.assertRaises(ValueError): v.rows(data)

    def test_selection_contract(self):
        reviewed=[]; selected=[]; current={}
        for i in range(45):
            r={'packet':f'P{i}','source':'1','source_commit':'a'*40,'packet_path':f'standalone/p{i}','mandatory_repairs':'none'}
            reviewed.append(r)
            c=dict(r, principal_files='PROOF.md', current_statement=v.GUIDE+'/TEST.md',
                status='REVIEWED_SELECTION_PENDING_INTEGRATION_REVIEW', review_record=v.REVIEW+'/pass4/EXTRACTION.tsv',
                executable_status='ARCHIVAL_UNLESS_SPECIFICALLY_SELECTED_BY_EVIDENCE_GUIDE')
            selected.append({k: c[k] for k in v.FIELDS});current[r['packet_path']+'/PROOF.md']=('100644','blob','a')
        current[v.GUIDE+'/TEST.md']=('100644','blob','b')
        v.check_selection(selected,reviewed,current)
        for key,value in [('status','VERIFIED'),('executable_status','ALL_APPROVED'),('source_commit','b'*40),('mandatory_repairs','R01'),('principal_files','missing.md')]:
            bad=copy.deepcopy(selected);bad[0][key]=value
            with self.assertRaises(ValueError):v.check_selection(bad,reviewed,current)
        with self.assertRaises(ValueError):v.check_selection(selected[:-1],reviewed,current)
        bad=copy.deepcopy(selected);bad[-1]=bad[0]
        with self.assertRaises(ValueError):v.check_selection(bad,reviewed,current)

    def test_real_git_byte_authentication_and_navigation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            def git(*args):
                return subprocess.check_output(['git','-c','core.autocrlf=false','-c','core.hooksPath=/dev/null',*args],cwd=root,stderr=subprocess.DEVNULL)
            git('init','-q');git('config','user.name','Synthetic test');git('config','user.email','test@example.invalid')
            def write(name,text):
                p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(text.encode())
            write('README.md','[Target](docs/proof.md#result)\n')
            write('docs/proof.md','# Result\n')
            git('add','.');git('commit','-qm','synthetic fixture')
            index=v.tree(root,'HEAD')
            self.assertEqual(v.read(root,index,'docs/proof.md'),b'# Result\n')
            self.assertEqual(v.check_links(root,index,['README.md'])['local_links_and_anchors'],1)
            git('update-index','--assume-unchanged','docs/proof.md')
            write('docs/proof.md','# Wrong\n')
            self.assertEqual(git('status','--porcelain'),b'')
            with self.assertRaises(ValueError):v.read(root,index,'docs/proof.md')
            write('docs/proof.md','# Result\n')
            write('README.md','[Missing](docs/proof.md#absent)\n')
            git('add','README.md');git('commit','-qm','bad anchor fixture')
            with self.assertRaises(ValueError):v.check_links(root,v.tree(root,'HEAD'),['README.md'])
            write('README.md','[Missing](docs/absent.md)\n')
            git('add','README.md');git('commit','-qm','bad path fixture')
            with self.assertRaises(ValueError):v.check_links(root,v.tree(root,'HEAD'),['README.md'])
            p=root/'docs/proof.md';p.unlink();p.symlink_to(root/'README.md')
            with self.assertRaises(ValueError):v.read(root,index,'docs/proof.md')


if __name__ == '__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(CandidateTests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():raise SystemExit(1)
    print(json.dumps({'marker':'PASS_SYNTHETIC_CANDIDATE_TESTS','methods':result.testsRun,'skips':len(result.skipped),'full_repository_checked':False},sort_keys=True))
