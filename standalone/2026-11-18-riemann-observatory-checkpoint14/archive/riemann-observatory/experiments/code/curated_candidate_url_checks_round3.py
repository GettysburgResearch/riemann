from pathlib import Path
import urllib.request,json,hashlib,concurrent.futures,urllib.error
p=Path(__file__).resolve().parents[2]/'sources/corpus_priority_round2'
rs=json.loads((p/'provisional_full_batch.json').read_text())
def run(r):
 doi=r['doi'].replace('https://doi.org/','');mf=p/'crossref'/(hashlib.sha256(doi.lower().encode()).hexdigest()[:16]+'.json')
 if not mf.exists():u='https://arxiv.org/abs/1305.4618v1'
 else:
  m=json.loads(mf.read_text())['message'];u=m.get('resource',{}).get('primary',{}).get('URL','https://doi.org/'+doi)
 u=u.replace('http://','https://',1)
 req=urllib.request.Request(u,method='HEAD',headers={'User-Agent':'Mozilla/5.0'})
 d={'candidate_id':r['candidate_id'],'url_checked':u,'method':'HEAD','scope':'URL accessibility only; no mathematical full text read'}
 try:
  a=urllib.request.urlopen(req,timeout=8);d.update(status=a.status,resolved_url=a.url,content_type=a.headers.get('Content-Type'))
 except urllib.error.HTTPError as e:d.update(status=e.code,error=str(e))
 except Exception as e:d.update(status=None,error=str(e))
 return d
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 out=list(ex.map(run,rs))
(p/'primary_url_access_checks.json').write_text(json.dumps(out,indent=2))
from collections import Counter
print(dict(Counter(str(x['status']) for x in out)))
