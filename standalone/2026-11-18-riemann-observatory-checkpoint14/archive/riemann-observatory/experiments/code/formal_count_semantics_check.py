"""Static count-definition identity check for the pinned AF source.
Not Lean elaboration; finiteness/multiplicity proof review is documented separately.
"""
from pathlib import Path
import json,re,hashlib,subprocess,sys
B=Path(__file__).resolve().parents[2]
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else B/'sources/formal_round2/zeta-23-lean-v1.0'
a=R/'comparator/ChallengeDeps.lean';b=R/'Zeta23/Statement.lean'
names=['IsNontrivialZero','zeroMult','zerosIn','Ncount','Ndist','N0','N0star','N0simple','Nsimple']
def definition(path,name):
 line=next(x for x in path.read_text().splitlines() if re.match(r'^def '+re.escape(name)+r'\b',x))
 return re.sub(r'\s+','',line)
rows=[]
for name in names:
 x,y=definition(a,name),definition(b,name);assert x==y
 rows.append({'name':name,'whitespace_normalized_literal_definition_matches':True})
paths=['comparator/ChallengeDeps.lean','Zeta23/Statement.lean','Zeta23/Statement/Seam.lean','Zeta23/Statement/SeamClosed.lean','Zeta23/Defs.lean','Zeta23/Final.lean','Zeta23/FinalMult.lean','Zeta23/ThmD/Mult.lean','comparator/Solution.lean','comparator/Solution/Multiplicity.lean','.lake/packages/mathlib/Mathlib/Analysis/Analytic/Order.lean','.lake/packages/mathlib/Mathlib/Data/Set/Card.lean','.lake/packages/mathlib/Mathlib/Algebra/BigOperators/Finprod.lean']
out={'kind':'static_count_definition_identity_and_inspected_source_hashes_NOT_Lean_proof','commit':subprocess.check_output(['git','-C',str(R),'rev-parse','HEAD'],text=True).strip(),'count_definitions':rows,'source_sha256':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths},'semantic_review':'audits/adversarial_reviews/AF_count_semantics_skeptic_round2.md','scope':'Nine literal public/library zeta count definitions checked. Source proofs of finite positive order and finite windows read independently; their complete Lean closure was not built by this reviewer.'}
assert out['commit']=='3635e74826a4c1fcece7d1cd2b6fa75e43a00510'
(B/'experiments/results/formal_count_semantics_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'count_definitions_matched':len(rows),'source_hashes':len(paths),'scope':out['scope']},indent=2))
