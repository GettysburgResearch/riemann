from pathlib import Path
import urllib.request,urllib.parse,json,concurrent.futures,hashlib,time
root=Path(__file__).resolve().parents[2]
p=root/'sources/corpus_priority_round2'
p.mkdir(parents=True,exist_ok=True)
rs=json.loads((root/'corpus/curated_candidate_input_round3.json').read_text())
(p/'provisional_full_batch.json').write_text(json.dumps(rs,indent=2,ensure_ascii=False))
def go(r):
 doi=r['doi'].replace('https://doi.org/','')
 name=hashlib.sha256(doi.lower().encode()).hexdigest()[:16]+'.json'
 f=p/'crossref'/name;f.parent.mkdir(exist_ok=True)
 if f.exists():
  try:d=json.loads(f.read_text());return r['candidate_id'],True,d['message'].get('title'),name
  except:pass
 url='https://api.crossref.org/works/'+urllib.parse.quote(doi,safe='/')
 try:
  time.sleep(0.3)
  raw=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'RiemannObservatory-metadata-research/0.1'}),timeout=25).read()
  d=json.loads(raw);f.write_bytes(raw)
  return r['candidate_id'],True,d['message'].get('title'),name
 except Exception as e:return r['candidate_id'],False,str(e),name
with concurrent.futures.ThreadPoolExecutor(max_workers=1) as ex:
 for v in ex.map(go,rs):print(json.dumps(v,ensure_ascii=False),flush=True)

# Supplemental primary bibliographic evidence; downloaded privately, not read/audited automatically.
supplemental={
 'harper1305.html':'https://arxiv.org/abs/1305.4618v1',
 'conreyghosh1998_arxiv.html':'https://arxiv.org/abs/math/9807187',
 'mertens_repository.html':'https://ir.cwi.nl/pub/1823',
 'heath_brown_cv.pdf':'https://www.maths.ox.ac.uk/system/files/users/cv/rhbcv_3.pdf',
 'montgomery_bibliography.html':'https://public.websites.umich.edu/~hlm/rpubs.html',
}
for filename,url in supplemental.items():
 try:
  d=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25).read()
  (p/filename).write_bytes(d);print('supplemental',filename,len(d),hashlib.sha256(d).hexdigest())
 except Exception as e:print('supplemental_failed',filename,str(e))
