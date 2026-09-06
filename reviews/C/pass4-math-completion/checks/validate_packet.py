#!/usr/bin/env python3
"""C4 integrity, scope and small hypergraph checker, NOT a proof checker."""
from __future__ import annotations
import argparse,csv,hashlib,json,re,sys
from pathlib import Path,PurePosixPath

# Literal inventories are independent of the user-supplied manifest/count fields.
EXPECTED_FILES = ('CENSUS_DELTA.tsv', 'CLAIMS.tsv', 'COUNTS.json', 'COVERAGE.tsv', 'EDGES.tsv', 'MANIFEST.json', 'NODES.tsv', 'README.md', 'REFERENCES.md', 'RELEASE_BLOCKERS.md', 'REPORT.md', 'SCOPE.json', 'SOURCES.tsv', 'SOURCE_VERSION_DIFFS.tsv', 'STRUCTURE_AND_EXTRACTION.md', 'VALIDATION.md', 'checks/math_checks.py', 'checks/result.json', 'checks/test_rejections.py', 'checks/validate_packet.py', 'checks/verify_source_checkout.py', 'evidence/ENVIRONMENT.json', 'evidence/MATH_EXECUTIONS.json', 'evidence/PACKAGE_EXECUTIONS.json', 'evidence/REJECTION_EXECUTIONS.json', 'evidence/math-normal.stderr', 'evidence/math-normal.stdout', 'evidence/math-optimized.stderr', 'evidence/math-optimized.stdout', 'lean/EntireXiRepair.lean', 'proofs/MELLIN_ANALYTIC_GAPS.md', 'proofs/OPERATOR_AUDIT.md', 'proofs/XI_SOURCE_REPAIR.md')
EXPECTED_SOURCES = {'SRC-P0': ['GettysburgResearch/riemann', '8d16f8d9c475db290bc85e53d775b93b9bcdb336', 'AGENTS.md', '0ad1dc2034c5d83e777343f77b41dcaf3683ef14'], 'SRC-P1': ['GettysburgResearch/riemann', '8d16f8d9c475db290bc85e53d775b93b9bcdb336', 'docs/REVIEWING.md', 'de7a9b67e1332d825c1688db07a0887e324f5ccb'], 'SRC-P2': ['GettysburgResearch/riemann', '8d16f8d9c475db290bc85e53d775b93b9bcdb336', 'canonical/2026-08-22/manifest.json', '446aec7e1c6d7b1d40a7747f3c9b161d03efdad3'], 'SRC-C0': ['GettysburgResearch/riemann', 'e0d1cb976030048275b5c2cda4275341650a350c', 'reviews/C/pass3/COVERAGE.tsv', '287b5e8169e7df0e46ba08f2ee4243b61de508de'], 'SRC-C1': ['GettysburgResearch/riemann', 'e0d1cb976030048275b5c2cda4275341650a350c', 'reviews/C/pass2/FORMAL_CATALOG_AUDIT.tsv', '1c8437c69188cac8e5b5d03e6cc87b10d14ae0d2'], 'SRC-C2': ['GettysburgResearch/riemann', 'e0d1cb976030048275b5c2cda4275341650a350c', 'reviews/C/CENSUS.tsv', '7f3bae32843289e5079e0e8eb4f9da60122f77a0'], 'SRC-X0': ['GettysburgResearch/riemann', '8d16f8d9c475db290bc85e53d775b93b9bcdb336', 'formal/comparator/ChallengeDeps/RiemannComparatorChallengeDeps/XiPickOrderThreeConditional.lean', '7d3dd6c98fd453d1810d80b0e1a39e2e4fbc7ab5'], 'SRC-X1': ['GettysburgResearch/riemann', '8d16f8d9c475db290bc85e53d775b93b9bcdb336', 'formal/RiemannFormal/Operator/XiSourceSpecific.lean', 'da684227de5443511b60d1fafa0b1ccafa1883ee'], 'SRC-X2': ['GettysburgResearch/riemann', '8d16f8d9c475db290bc85e53d775b93b9bcdb336', 'formal/RiemannFormal/Operator/ReciprocalConcavity.lean', '2f6604c5c3f4d7e0b18d047748d21b2701827aad'], 'SRC-X3': ['GettysburgResearch/riemann', '8d16f8d9c475db290bc85e53d775b93b9bcdb336', 'formal/RiemannFormal/Operator/PickAlgebra.lean', 'd19c19e0acb468bff19849cfebcdfbb8501e1b16'], 'SRC-X4': ['GettysburgResearch/riemann', '8d16f8d9c475db290bc85e53d775b93b9bcdb336', 'formal/RiemannFormal/Operator/XiOrderThree.lean', '8a57d165e4d585232d8976858871b99a0d39101e'], 'SRC-X5': ['GettysburgResearch/riemann', '8d16f8d9c475db290bc85e53d775b93b9bcdb336', 'formal/RiemannFormal/Operator/RepeatedNodes.lean', 'dc9e0792191207d7d0d9dcaafb80a08091cfb6c3'], 'SRC-U0': ['leanprover-community/mathlib4', '51e6992efd06126df61a496bebf8f49482a4e129', 'Mathlib/NumberTheory/LSeries/RiemannZeta.lean', '3c92195fce20df7fda41cfd823b3266f83cf3070'], 'SRC-U1': ['GettysburgResearch/riemann', '8d16f8d9c475db290bc85e53d775b93b9bcdb336', 'formal/RiemannFormal/Upstream/Zeta23Bridge.lean', '3a6cfe78869f6a9716d1e628de6ee3f9ca7501ee'], 'SRC-M0': ['GettysburgResearch/riemann', '8d16f8d9c475db290bc85e53d775b93b9bcdb336', 'formal/RiemannFormal/Analysis/Foundations.lean', '52b7a228c128d20dc5b57240b208fee104e624ed'], 'SRC-M1': ['GettysburgResearch/riemann', '8d16f8d9c475db290bc85e53d775b93b9bcdb336', 'formal/RiemannFormal/Analysis/MellinAPI.lean', 'bc2a284d9a51e13235fdc5e55866c87d1593105c'], 'SRC-M2': ['GettysburgResearch/riemann', '8d16f8d9c475db290bc85e53d775b93b9bcdb336', 'formal/RiemannFormal/Analysis/LandauConsumer.lean', '9c40d6b04303a717dd48f18d065483cf1673c122'], 'SRC-M3': ['GettysburgResearch/riemann', '8d16f8d9c475db290bc85e53d775b93b9bcdb336', 'formal/RiemannFormal/Analysis/SingularityTransfer.lean', 'e598973cbd533750399d3bd7b3c5790b906d85f8'], 'SRC-M4': ['GettysburgResearch/riemann', '8d16f8d9c475db290bc85e53d775b93b9bcdb336', 'formal/RiemannFormal/Analysis/FixedDetectorConsumer.lean', '312e1e94cd29e1fce7a0b0b5f89064c338d5db68'], 'SRC-M5': ['GettysburgResearch/riemann', '8d16f8d9c475db290bc85e53d775b93b9bcdb336', 'formal/RiemannFormal/Analysis/Reflection.lean', '8648ddbaeffca79a33fd257db15dfe1a4562ee17'], 'SRC-O0': ['GettysburgResearch/riemann', '465cb28ed8cbfa1bb071d9a85eeda9890decfe6b', 'standalone/2026-09-05-bernstein-chebyshev-growth/finite-window-coercivity/PROOF.md', '35d8d38a77bee896b0b2e729b095ccdef5d7a50f'], 'SRC-O1': ['GettysburgResearch/riemann', '465cb28ed8cbfa1bb071d9a85eeda9890decfe6b', 'standalone/2026-09-05-bernstein-chebyshev-growth/energy-schur-reduction/PROOF.md', '0d12ff6039dcc79f6576538edeebd2a0c5b539c0']}
EXPECTED_SCOPE = {'role': 'Reviewer C successor; formerly Reviewer A', 'repository': 'GettysburgResearch/riemann', 'target_pr': 798, 'target_branch': 'review/C/2026-09-05-post-release-audit', 'parent_head': 'e0d1cb976030048275b5c2cda4275341650a350c', 'scientific_baseline': '8d16f8d9c475db290bc85e53d775b93b9bcdb336', 'research_boundary_pr': 707, 'status': 'TARGETED_MATHEMATICAL_HANDOFF_COMPLETE_GLOBAL_C_ALLOTMENT_INCOMPLETE', 'independent_of_prior_A': False, 'trusted_formal_sources_modified': False, 'publication_receipt': 'external to source payload; see ZIP PUBLICATION_RECEIPT.json', 'actual_rh_proof': False, 'lean_compiled': False, 'global_census_complete': False, 'public_release_cleared': False, 'source_binding_complete': False, 'independent_of_792_original_author': True, 'whole_792_independently_accepted': False}
EXPECTED_RESULT_SHA256 = '4b264eb7d6de2bcb4f04a3372689587e85dbd11200acb91bcdb31e8abaed408c'
CLAIM_IDS={f'C4-M{i}' for i in range(1,11)}|{f'C4-X{i}' for i in range(1,17)}|{f'C4-O{i}' for i in range(1,12)}|{'C4-P1'}
EDGE_IDS={f'C4-E{i:02}' for i in range(1,25)}
OPEN_NODES={'H.MELLIN.NATIVE_SOURCE','H.MELLIN.NEGATIVE_MASS','H.XI.ACTUAL_BINDING','H.XI.COMPILED_REPAIR','H.OP.CONTINUUM_CERT','H.OP.ALL_LENGTHS'}
NODE_IDS=OPEN_NODES|{'H.MELLIN.ANALYSIS','H.MELLIN.ZERO_ADAPTERS','H.XI.SPECTRAL_DATA','XI.PSD3.PAPER','XI.PSD3.TRUSTED','H.OP.KERNEL','H.OP.GLOBAL_ADAPTER','OP.ONE_WINDOW.PSD','OP.ALL_WINDOWS.PSD','RH'}

def need(x,message):
 if not x:raise ValueError(message)
def unique(pairs):
 d={}
 for k,v in pairs:
  need(k not in d,'duplicate JSON key');d[k]=v
 return d
def load(p):return json.loads(p.read_text(encoding='utf-8'),object_pairs_hook=unique)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def safe_path(s):
 q=PurePosixPath(s)
 return isinstance(s,str) and s and not q.is_absolute() and '..' not in q.parts and '\\' not in s and str(q)==s

def rows(root,name,idkey,expected=None):
 with (root/name).open(newline='',encoding='utf-8') as f:
  r=csv.DictReader(f,delimiter='\t');headers=r.fieldnames
  need(headers is not None and len(set(headers))==len(headers),'bad table header '+name)
  out=list(r)
 need(out and all(None not in r and all(v is not None for v in r.values()) for r in out),'empty/ragged table '+name)
 ids=[r[idkey] for r in out];need(len(ids)==len(set(ids)),'duplicate identity '+name)
 if expected is not None:need(set(ids)==expected,'identity coverage '+name)
 return out

def main(root):
 need(root.is_dir(),'missing packet root')
 actual=set()
 for p in root.rglob('*'):
  need(not p.is_symlink(),'symlink not allowed')
  if p.is_file():actual.add(p.relative_to(root).as_posix())
 need(actual==set(EXPECTED_FILES),'file inventory mismatch')
 m=load(root/'MANIFEST.json')
 need(type(m) is dict and set(m)=={'schema','files'} and m['schema']=='riemann.review.C4.manifest.v1','manifest schema')
 need(type(m['files']) is list,'manifest records')
 seen=set()
 for r in m['files']:
  need(type(r) is dict and set(r)=={'path','bytes','sha256'},'manifest record schema')
  p=r['path'];need(safe_path(p) and p not in seen,'duplicate/unsafe manifest path');seen.add(p)
  need(type(r['bytes']) is int and r['bytes']>=0,'byte type')
  need(type(r['sha256']) is str and re.fullmatch('[0-9a-f]{64}',r['sha256']),'digest type')
  need((root/p).is_file(),'manifest missing file')
  need((root/p).stat().st_size==r['bytes'] and sha(root/p)==r['sha256'],'manifest mismatch '+p)
 need(seen==actual-{'MANIFEST.json'},'manifest coverage')
 scope=load(root/'SCOPE.json');need(canonical(scope)==canonical(EXPECTED_SCOPE),'declared scope mismatch')
 counts=load(root/'COUNTS.json');need(canonical(counts)==canonical({'source_files':22,'claim_dispositions':38,'edges':24,'hypothesis_and_conclusion_nodes':16}),'count inventory')
 src=rows(root,'SOURCES.tsv','source_id',set(EXPECTED_SOURCES))
 bys={s['source_id']:s for s in src}
 for s in src:
  need([s[k] for k in ['repository','commit_sha','path','git_blob_sha']]==EXPECTED_SOURCES[s['source_id']],'source pin mismatch '+s['source_id'])
  need(bool(s['inspection_scope']),'missing reading scope')
 claims=rows(root,'CLAIMS.tsv','claim_id',CLAIM_IDS)
 for c in claims:
  need(c['formal_execution']=='NOT_COMPILED','formal promotion')
  ss=c['source_ids'].split(';');need(all(x in bys for x in ss),'unknown source')
  need(c['source_commits']==';'.join(dict.fromkeys(bys[x]['commit_sha'] for x in ss)),'claim commit binding')
  need(c['source_paths']==';'.join(bys[x]['path'] for x in ss),'claim path binding')
  need(all(c.get(k) for k in ['source_claim','exact_scope','verdict','dependencies','evidence','required_repair','proposed_destination','independence']),'incomplete claim')
  if c['claim_id']=='C4-O11':need(c['verdict']=='OPEN_ARITHMETIC_PREMISE','operator sign promoted')
  file,_,anchor=c['evidence'].partition('#');need(safe_path(file) and (root/file).is_file(),'evidence target')
  if anchor:need(f'<a id="{anchor}"></a>' in (root/file).read_text(),'evidence anchor')
 nodes=rows(root,'NODES.tsv','node_id',NODE_IDS)
 for n in nodes:
  need((n['status']=='OPEN')==(n['node_id'] in OPEN_NODES),'open-node status changed')
  need(n['status'] in {'OPEN','ASSUMPTION','DERIVED'},'unknown node status')
 edges=rows(root,'EDGES.tsv','edge_id',EDGE_IDS)
 universe=CLAIM_IDS|NODE_IDS
 for e in edges:
  p=json.loads(e['premise_ids'],object_pairs_hook=unique)
  need(type(p) is list and p and all(type(x) is str and x in universe for x in p),'unknown/empty premise')
  need(len(p)==len(set(p)) and e['conclusion_id'] in universe,'edge identity')
  need(e['edge_type']=='CONJUNCTIVE_PAPER_IMPLICATION','edge type')
  file,_,anchor=e['evidence'].partition('#');need((root/file).is_file() and f'<a id="{anchor}"></a>' in (root/file).read_text(),'edge evidence')
 # Even granting every non-open component and named classical assumption,
 # the open native and all-length premises must still block RH.
 reached=CLAIM_IDS-{'C4-O11'}|{n['node_id'] for n in nodes if n['status']=='ASSUMPTION'}
 changed=True
 while changed:
  changed=False
  for e in edges:
   if set(json.loads(e['premise_ids']))<=reached and e['conclusion_id'] not in reached:
    reached.add(e['conclusion_id']);changed=True
 need('RH' not in reached and 'XI.PSD3.TRUSTED' not in reached,'open premise bypassed')
 rows(root,'CENSUS_DELTA.tsv','item_id',set(EXPECTED_SOURCES))
 rows(root,'COVERAGE.tsv','unit');rows(root,'SOURCE_VERSION_DIFFS.tsv','object')
 need(sha(root/'checks/result.json')==EXPECTED_RESULT_SHA256,'math payload changed')
 result=load(root/'checks/result.json')
 need(result['scope']['rh_proved'] is False and result['scope']['lean_compiled'] is False,'result scope')
 need(sum(result['groups'].values())==1092,'bounded fixture count')
 for c in ['M','X','O']:
  pass # no acceptance of analytic proofs is inferred from their presence
 candidate=(root/'lean/EntireXiRepair.lean').read_text()
 need('NOT COMPILED' in candidate,'candidate compiler boundary')
 need(not re.search(r'(?m)^\s*(?:axiom|sorry|admit)\b',candidate),'candidate placeholder declaration')
 out={'status':'PASS_C4_PACKET_INTEGRITY_AND_DECLARED_SCOPE','files':len(actual),'manifest_entries':len(seen),'sources':len(src),'claims':len(claims),'edges':len(edges),'rh_without_open_premises':False,'lean_compiled':False,'mathematical_truth_checked_by_validator':False}
 print(canonical(out));return out

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args()
 try:main(a.root)
 except (ValueError,KeyError,TypeError,OSError,json.JSONDecodeError) as e:print('FAIL: '+str(e),file=sys.stderr);sys.exit(2)
