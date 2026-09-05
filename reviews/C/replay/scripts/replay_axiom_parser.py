"""Bounded reviewer-created parser fixtures, NOT Lean or kernel replay."""
import hashlib,json,os,subprocess,sys,tempfile
from pathlib import Path
root=Path(__file__).resolve().parents[1]
source=root/'references/formal/audit_axiom_output.py'
b=source.read_bytes()
sha=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
if sha!='ef83fe752f6612617612b259109cfdcab8b108bc': raise SystemExit('source mismatch')
a="'Test.a' depends on axioms: [propext, Classical.choice, Quot.sound]\n"
cases={
'allowed':(a,0),
'no_axioms':("'Test.a' does not depend on any axioms\n",0),
'multiline':("'Test.a' depends on axioms: [propext,\n Classical.choice, Quot.sound]\n",0),
'empty':('',1),
'sorry':("'Test.a' depends on axioms: [sorryAx]\n",1),
'custom':("'Test.a' depends on axioms: [Mystery.positivity]\n",1),
'unexpected':(a+"'Test.b' does not depend on any axioms\n",1),
'unterminated':("'Test.a' depends on axioms: [propext\n",1),
'duplicate_allowed':(a+a,0),
'garbage_after_payload':(a.rstrip()+' arbitrary\n',1),
}
results=[]
for mode in ([],['-O']):
 for name,(text,expected) in cases.items():
  with tempfile.TemporaryDirectory(prefix='reviewC_axiom_') as d:
   p=Path(d);(p/'audit.py').write_bytes(b);(p/'output.txt').write_text(text);(p/'Print.lean').write_text('#print axioms Test.a\n')
   cmd=[sys.executable,*mode,'-I','audit.py','output.txt','Print.lean']
   r=subprocess.run(cmd,cwd=d,env={'PATH':os.environ.get('PATH','/usr/bin'),'HOME':d,'PYTHONDONTWRITEBYTECODE':'1'},capture_output=True,text=True,timeout=5)
   good=(r.returncode==0)==(expected==0)
   results.append({'case':name,'optimized':bool(mode),'command':cmd,'exit':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'expected_behavior':good})
   if not good:raise SystemExit('unexpected behavior '+name)
report={'classification':'EXACT_SOURCE_PARSER_FIXTURES_NOT_LEAN_BUILD','source_git_blob':sha,'source_commit':'8d16f8d9c475db290bc85e53d775b93b9bcdb336','python':sys.version,'runs':results,'count':len(results),'duplicate_output_rejected':False,'kernel_executed':False}
(root/'reports/axiom_parser_replay.json').write_text(json.dumps(report,indent=2)+'\n')
print('20/20 expected parser outcomes; duplicate allowed output accepted; no Lean execution')
