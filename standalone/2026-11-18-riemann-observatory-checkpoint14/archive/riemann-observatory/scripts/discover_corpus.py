#!/usr/bin/env python3
"""Resumable OpenAlex candidate discovery; metadata only, never a reading audit."""
import argparse, csv, datetime, hashlib, json, pathlib, time, urllib.parse, urllib.request, re
ROOT=pathlib.Path(__file__).resolve().parents[1]
RAW=ROOT/'corpus/raw_discovery'; RAW.mkdir(exist_ok=True)
LOG=ROOT/'logs/discovery.jsonl'
CUTOFF='2026-11-17'
OFFLINE='--offline' in __import__('sys').argv
QUERIES=[
('riemann-hypothesis','Riemann hypothesis',600,'C,G'),
('zeta-function','zeta function',600,'A,B,D,E,F'),
('prime-number-theorem','prime number theorem',200,'A'),
('l-functions','L-functions',300,'A,E'),
('dirichlet-polynomials','Dirichlet polynomials',150,'A'),
('zero-density','zero density',150,'A'),
('zero-free-region','zero free region',100,'A'),
('pair-correlation','pair correlation zeta',100,'B'),
('random-matrices','random matrix zeta',100,'B,F'),
('mollifier','mollifier',100,'A,B'),
('nyman-beurling','Nyman Beurling',100,'C'),
('li-criterion','Li criterion',75,'C'),
('robin-inequality','Robin inequality',75,'C'),
('newman-constant','Newman constant',100,'B'),
('de-branges','de Branges',100,'D,F'),
('selberg-zeta','Selberg zeta',150,'D,E'),
('explicit-formula','explicit formula prime',100,'A,C'),
('critical-line','critical line',150,'A,B'),
('zeta-moments','moments zeta',150,'A,B'),
('zeta-universality','universality zeta',100,'B'),
('weil-conjectures','Weil conjectures',100,'E'),
('trace-formula','trace formula',150,'D,E'),
('scattering-automorphic','scattering automorphic',100,'D,E'),
('spectral-determinants','spectral determinants',100,'D,H'),
('canonical-systems','canonical systems',100,'D,H'),
('positive-definite-functions','positive definite functions',100,'C,F,H'),
('exponential-sums','exponential sums',150,'A'),
('subconvexity','subconvexity',100,'A,E'),
('lindelof','Lindelof hypothesis',100,'A'),
('riemann-von-mangoldt','Riemann von Mangoldt',75,'A,B'),
('beurling-primes','Beurling primes',100,'A,F'),
('hilbert-polya','Hilbert Polya',75,'D'),
('zeta-transfer','transfer operator zeta',100,'D,F'),
('montgomery','Montgomery pair correlation',75,'B'),
('approx-functional-equation','approximate functional equation',100,'A'),
('bombieri-vinogradov','Bombieri Vinogradov',100,'A'),
('automorphic-l-functions','automorphic L-functions',100,'E'),
('function-field-l-functions','function field L-functions',100,'E'),
('lagarias','Lagarias Riemann',75,'C'),
('baez-duarte','Baez Duarte',75,'C'),
('weil-positivity','Weil positivity',75,'C,E'),
('recent-riemann-hypothesis','Riemann hypothesis',100,'A,B,C,D,E,F,G'),
('recent-riemann-zeta','Riemann zeta',150,'A,B,C,D,F'),
('recent-dirichlet-polynomials','Dirichlet polynomials',100,'A'),
('recent-zero-density','zero density',100,'A'),
('recent-critical-line','critical line',100,'A,B'),
('recent-l-functions','L-functions',150,'A,E'),
('historical-primzahlen','Primzahlen',50,'A'),
('historical-nombres-premiers','nombres premiers',50,'A'),
('historical-fonction-zeta','fonction zeta',30,'A'),
('historical-riemann','Riemann',50,'A,F,H'),
]
def appendlog(x):
 with LOG.open('a') as f:f.write(json.dumps(x,ensure_ascii=False)+'\n')
def get_page(slug,term,page,n):
 path=RAW/f'{slug}-{page:03d}.json'
 if path.exists():return json.loads(path.read_text())
 if OFFLINE:return None
 start='2024-01-01' if slug.startswith('recent-') else '1859-01-01'
 end='1900-12-31' if slug.startswith('historical-') else CUTOFF
 sort='publication_date:desc' if slug.startswith('recent-') else 'cited_by_count:desc'
 params={'filter':f'title.search:{term},from_publication_date:{start},to_publication_date:{end}', 'per-page':n,'page':page,'sort':sort}
 url='https://api.openalex.org/works?'+urllib.parse.urlencode(params)
 time.sleep(1.2)
 for attempt in range(6):
  try:
   req=urllib.request.Request(url,headers={'User-Agent':'RiemannObservatory/0.1 (research bibliography; no automated source-audit claim)'})
   with urllib.request.urlopen(req,timeout=60) as response:data=json.load(response)
   envelope={'query':term,'query_scope':term+(' [2024-cutoff; date-ranked]' if slug.startswith('recent-') else (' [1859-1900; citation-ranked]' if slug.startswith('historical-') else ' [1859-cutoff; citation-ranked]')),'url':url,'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'provider':'OpenAlex','result':data}
   path.write_text(json.dumps(envelope,ensure_ascii=False))
   appendlog({'event':'fetch','query':term,'page':page,'results':len(data.get('results',[])),'raw_file':str(path.relative_to(ROOT)),'retrieved_at':envelope['retrieved_at']})
   return envelope
  except Exception as e:
   appendlog({'event':'error','query':term,'page':page,'attempt':attempt,'error':str(e)})
   if attempt<5:time.sleep(min(2**attempt,16))
 return None

def normalize_title(s):return re.sub(r'[^\w]+',' ',s.casefold()).strip()
def collect():
 works={};query_summary=[]
 for slug,term,target,families in QUERIES:
  obtained=0
  for page in range(1,(target+199)//200+1):
   n=min(200,target); wanted=min(200,target-(page-1)*200); env=get_page(slug,term,page,n)
   if not env:break
   results=env['result'].get('results',[])[:wanted];obtained+=len(results)
   for w in results:
    oid=w['id']; key=(w.get('doi') or oid).lower()
    if key not in works:
     loc=w.get('primary_location') or {}; source=loc.get('source') or {}
     works[key]={'candidate_id':'CAND-'+hashlib.sha256(key.encode()).hexdigest()[:12].upper(),'title':w.get('title'),'authors':[a.get('author',{}).get('display_name') for a in w.get('authorships',[])],'date':w.get('publication_date'),'year':w.get('publication_year'),'venue':source.get('display_name'),'publication_type':w.get('type'),'doi':w.get('doi'),'openalex_id':oid,'language':w.get('language'),'citation_count':w.get('cited_by_count'),'primary_topic':w.get('primary_topic'),'canonical_url':loc.get('landing_page_url'),'pdf_url':loc.get('pdf_url'),'is_oa':(w.get('open_access') or {}).get('is_oa'),'oa_url':(w.get('open_access') or {}).get('oa_url'),'referenced_works':w.get('referenced_works',[]),'related_works':w.get('related_works',[]),'discovery_queries':[],'family_candidates':[],'metadata_evidence':[],'status':'discovered_metadata_only','audit_level':None,'selected':False,'relevance_review':'pending','retrieved_at':env['retrieved_at']}
    rec=works[key]
    label=env.get('query_scope',term+' [1859-cutoff; citation-ranked]')
    if label not in rec['discovery_queries']:rec['discovery_queries'].append(label)
    rec['family_candidates']=sorted(set(rec['family_candidates'])|set(families.split(',')))
    rec['metadata_evidence'].append({'file':f'corpus/raw_discovery/{slug}-{page:03d}.json','provider_id':oid})
   if len(results)<wanted:break
  query_summary.append({'query':term,'target':target,'retrieved':obtained,'family_search_scope':families,'recent_date_ranked':slug.startswith('recent-')})
  print(slug,obtained,'unique',len(works),flush=True)
 # DOI duplicates already removed; title/year cross-ID duplicates retained and flagged rather than unsafe merges.
 title_groups={}
 for w in works.values():title_groups.setdefault((normalize_title(w['title'] or ''),w['year']),[]).append(w['candidate_id'])
 rows=list(works.values())
 for w in rows:w['possible_duplicate_ids']=[x for x in title_groups[(normalize_title(w['title'] or ''),w['year'])] if x!=w['candidate_id']]
 rows.sort(key=lambda w:(w['year'] or 9999,w['title'] or ''))
 (ROOT/'corpus/candidates.jsonl').write_text(''.join(json.dumps(w,ensure_ascii=False)+'\n' for w in rows))
 fields=['candidate_id','title','authors','date','year','venue','publication_type','doi','openalex_id','language','citation_count','canonical_url','pdf_url','is_oa','oa_url','discovery_queries','family_candidates','status','audit_level','selected','relevance_review','possible_duplicate_ids']
 with (ROOT/'corpus/candidates.csv').open('w',newline='') as f:
  out=csv.DictWriter(f,fieldnames=fields);out.writeheader()
  for r in rows:out.writerow({k:json.dumps(r[k],ensure_ascii=False) if isinstance(r.get(k),list) else r.get(k) for k in fields})
 summary={'cutoff':CUTOFF,'candidate_count':len(rows),'raw_hits':sum(q['retrieved'] for q in query_summary),'metadata_only':len(rows),'substantively_read_by_discovery_pipeline':0,'queries':query_summary,'duplicate_policy':'merge identical DOI or identical provider ID; flag normalized identical title/year across IDs','warning':'Candidate discovery is deliberately broad. Families are query scopes, not reviewed classifications. Citation count is not mathematical quality. Metadata may contain errors.'}
 (ROOT/'corpus/candidates_summary.json').write_text(json.dumps(summary,indent=2))
 print(json.dumps({k:v for k,v in summary.items() if k!='queries'},indent=2))
if __name__=='__main__':collect()
