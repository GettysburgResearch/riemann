#!/usr/bin/env python3
"""Read-only Git-object check for C4 source pins. Does not fetch or execute sources."""
import argparse,csv,hashlib,json,re,subprocess,sys
from pathlib import Path

def run(repo,*args):
 p=subprocess.run(['git','-C',str(repo),*args],capture_output=True,timeout=20)
 if p.returncode:raise ValueError('required Git object unavailable: '+' '.join(args))
 return p.stdout

def main():
 ap=argparse.ArgumentParser();ap.add_argument('riemann_checkout',type=Path);ap.add_argument('--mathlib-checkout',type=Path,required=True)
 a=ap.parse_args();root=Path(__file__).resolve().parents[1]
 repos={'GettysburgResearch/riemann':a.riemann_checkout,'leanprover-community/mathlib4':a.mathlib_checkout}
 rows=list(csv.DictReader((root/'SOURCES.tsv').open(),delimiter='\t'));out=[]
 if len(rows)!=22:raise ValueError('expected 22 source records')
 for r in rows:
  commit=r['commit_sha'];path=r['path'];sha=r['git_blob_sha']
  if not re.fullmatch('[0-9a-f]{40}',commit) or not re.fullmatch('[0-9a-f]{40}',sha):raise ValueError('bad source identity')
  repo=repos[r['repository']]
  obj=run(repo,'rev-parse',f'{commit}:{path}').decode().strip()
  if obj!=sha:raise ValueError('blob mismatch for '+r['source_id'])
  data=run(repo,'cat-file','blob',sha)
  actual=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
  if actual!=sha:raise ValueError('Git blob bytes mismatch')
  out.append({'source_id':r['source_id'],'blob':sha,'bytes':len(data),'status':'MATCH'})
 print(json.dumps({'status':'PASS_SOURCE_OBJECTS_ONLY','records':out,'scientific_acceptance':False},sort_keys=True))

if __name__=='__main__':
 try:main()
 except (ValueError,KeyError,OSError,subprocess.TimeoutExpired) as e:print('FAIL: '+str(e),file=sys.stderr);sys.exit(2)
