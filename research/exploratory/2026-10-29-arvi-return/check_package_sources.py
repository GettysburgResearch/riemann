"""Compare pinned package worktrees with pristine+tracker-patch audit worktrees.

Requires the explicit paths from the active build environment; does not modify them.
This audits source trees, not the provenance of compiled package caches.
"""
import hashlib,json,subprocess
from pathlib import Path

root=Path('/workspace/scratch/qproject/.lake/packages')
manifest=Path('/workspace/scratch/qproject/lake-manifest.json')
tracker=Path('/tmp/tracker')
expected={
 'PrimeNumberTheoremAnd': (Path('/workspace/scratch/pnt-patch-audit'),tracker/'verifier/actions/patches/PrimeNumberTheoremAnd-lean4341.patch'),
 'rellich-kondrachov': (Path('/workspace/scratch/rellich-patch-audit'),tracker/'verifier/actions/patches/rellich-kondrachov-lean4341.patch')}
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def git(path,*args):return subprocess.check_output(['git','-C',str(path),*args],text=True)
assert digest(manifest)=='5c6d8777513f3fa9eee95a8475ea8d2109e7efaff4b315d8c22d4d2714ec9c79'
result={'scope':'package source trees only; not compiled-cache authentication','manifest_sha256':digest(manifest),'packages':[]}
for entry in json.loads(manifest.read_text())['packages']:
 name=entry['name'].strip('«»');actual=root/name
 head=git(actual,'rev-parse','HEAD').strip(); assert head==entry['rev']
 status=git(actual,'status','--porcelain','--untracked-files=all').splitlines()
 ignored_lean=[p for p in git(actual,'ls-files','--others','--ignored','--exclude-standard','*.lean').splitlines() if not p.startswith('.lake/')]
 assert not ignored_lean,(name,ignored_lean)
 record={'name':name,'pinned_revision':entry['rev'],'head':head,'changes':[],'ignored_lean_outside_lake':ignored_lean}
 if name in expected:
  baseline,patch=expected[name]
  expected_head=git(baseline,'rev-parse','HEAD').strip();assert expected_head==head
  expected_status=git(baseline,'status','--porcelain','--untracked-files=all').splitlines();assert status==expected_status,(name,'status mismatch')
  record['tracker_patch_sha256']=digest(patch)
  assert record['tracker_patch_sha256']=={'PrimeNumberTheoremAnd':'0890432340c0025973bcfe070b634355fa366cc831595f68526e4c73c8903d82','rellich-kondrachov':'0c121d8517dfeadc93ef24fe2deb56beec7cb3998e2552dee8f61c780b1408c8'}[name]
  for line in status:
   relative=line[3:];a=actual/relative;b=baseline/relative
   assert a.is_file() and b.is_file() and digest(a)==digest(b),(name,relative)
   record['changes'].append({'status':line[:2],'path':relative,'sha256':digest(a)})
  record['matches_pinned_plus_tracker_patch']=True
 else:
  assert not status,(name,status)
  record['matches_pinned_tree']=True
 result['packages'].append(record)
print('packages',len(result['packages']),'PNT changes',len(next(p for p in result['packages'] if p['name']=='PrimeNumberTheoremAnd')['changes']),'Rellich changes',len(next(p for p in result['packages'] if p['name']=='rellich-kondrachov')['changes']))
out=Path(__file__).with_name('package-source-audit.json');out.write_text(json.dumps(result,indent=2)+'\n')
