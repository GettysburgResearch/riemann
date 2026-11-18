#!/usr/bin/env python3
"""Conservative title collision screen. This is not a mathematical corpus review."""
import pathlib,json,csv,re,collections
R=pathlib.Path(__file__).resolve().parents[1]
rows=[json.loads(x) for x in (R/'corpus/candidates.jsonl').read_text().splitlines()]
# Strong title-level collisions only. Ambiguous adjacent mathematics stays pending.
patterns=[
 (re.compile(r'zeta[ -]potential|\bζ[ -]potential',re.I),'Lexical collision: zeta potential in materials/colloid/biomedical analysis; no title-level relation to zeta/L-function mathematics.'),
 (re.compile(r'\b(QCD|quark|Higgs|chiral condens|Bose.Einstein condens|Bose condens|fermionic gas|nuclear matter|dark matter)\b',re.I),'Outside initial corpus scope: title is a physical-system calculation without an explicit RH/zeta-zero or precise mathematical-method transfer; reconsider only with concrete dependency evidence.'),
 (re.compile(r'\b(nanoparticle|cellular uptake|protein adsorption|blood|bloodstream|gene expression|DNA methylation|cancer|tumou?r)\b',re.I),'Lexical collision: biomedical/materials title with no explicit number-theoretic relevance.'),
]
records=[]
for w in rows:
 title=w['title'] or '';reason=None
 if not re.search(r'Riemann|zeta.function|zeta-function|L-function|prime number',title,re.I):
  for pat,why in patterns:
   if pat.search(title):reason=why;break
 # zeta-potential papers sometimes also contain "function", hence separate explicit collision.
 if re.search(r'zeta[ -]potential|\bζ[ -]potential',title,re.I):reason=patterns[0][1]
 records.append({'candidate_id':w['candidate_id'],'title':title,'decision':'rejected_title_collision' if reason else 'pending_primary_relevance_review','reason':reason or 'Discovery only; canonical bibliography, mathematical relevance and importance are not yet reviewed.','review_method':'Conservative deterministic title screen v0.1; this decision does not assess mathematical correctness.','selected':False})
with (R/'corpus/candidates_screening.csv').open('w',newline='') as f:
 d=csv.DictWriter(f,fieldnames=list(records[0]));d.writeheader();d.writerows(records)
with (R/'corpus/candidates_rejected.jsonl').open('w') as f:
 for r in records:
  if r['decision'].startswith('rejected'):f.write(json.dumps(r,ensure_ascii=False)+'\n')
summary=collections.Counter(r['decision'] for r in records)
(R/'corpus/candidates_screening_summary.json').write_text(json.dumps(dict(summary),indent=2))
print(dict(summary))
