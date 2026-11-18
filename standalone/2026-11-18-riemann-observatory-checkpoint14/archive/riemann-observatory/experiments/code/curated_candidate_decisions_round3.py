from pathlib import Path
import json,hashlib,re,html,csv,collections
root=Path(__file__).resolve().parents[2]; p=root/'sources/corpus_priority_round2'
rs=json.loads((p/'provisional_full_batch.json').read_text()); access={x['candidate_id']:x for x in json.loads((p/'primary_url_access_checks.json').read_text())}
reasons={
'CAND-7E305063E813':('A,B','Historical critical-line proof development after Hardy1914.','Read original quantifiers and quantitative count; locate proof inputs used by later positive-proportion methods.',['PAPER-S007']),
'CAND-5963EEF02A58':('A','Classical analytic zeta estimates by Littlewood, absent from inspected corpus.','Identify exact conditional and unconditional growth/zero estimates before attributing later near-line bounds.',['PAPER-M001','PAPER-E007']),
'CAND-A75867957D85':('A','Foundational moment theorem antecedent to modern moments and mollifiers.','Reconstruct second/fourth-moment normalizations and off-diagonal errors from original paper.',['PAPER-E009']),
'CAND-E39F04327F9A':('A,B','Original1935 numerical/analytic zero work needed for verification history.','Identify exact zero-count certification method and what was established at finite height.',['PAPER-A002']),
'CAND-454FB8542468':('A,B','Separate1936 same-title continuation, not a title-only duplicate of1935 paper.','Read its relation to1935 paper and preserve changed hypotheses/results rather than merging by title.',['PAPER-A002']),
'CAND-95D3C6A02FCA':('A','Classical mean-square error analysis, a central moment dependency.','Extract exact Atkinson formula assumptions, truncation ranges and oscillatory remainder.',['PAPER-A001']),
'CAND-94CD8ACEE088':('A,B,F','Foundational rigorous numerical zero-certification method.','Audit completeness of a finite zero list and the integration/counting bound used in later verification.',['PAPER-A002']),
'CAND-3B86F55BE11E':('A,B,C','Derivative zeros provide a precise RH-adjacent and critical-line dependency.','Read exact derivative-zero counts and dependence on RH before transplanting a converse-Rolle intuition.',['PAPER-A003']),
'CAND-329B94C7E05F':('A,B,F','Landmark universality phenomenon constrains naive approximation/positivity intuition.','Read original permitted target functions, compact sets and nonvanishing assumptions; distinguish translates from critical zeros.',['PAPER-E001']),
'CAND-9CAA7299D311':('A','Original zero-density improvement is a required historical comparator for large-value advances.','Extract the uniform sigma range, logarithmic powers and large-value inequality feeding the density estimate.',['PAPER-A001']),
'CAND-9752E9A8A32D':('A','Fourth-moment asymptotic is a central proven benchmark for conjectural higher moments.','Audit Dirichlet-polynomial lengths and off-diagonal treatment before comparing sixth-moment conjectures.',['PAPER-A001']),
'CAND-7C83AC92A057':('A','Classical zero-density benchmark immediately relevant to modern density/mollifier comparisons.','Extract exact exponent piecewise in sigma and constants/uniformity; avoid a rounded density label.',['PAPER-A001','PAPER-A006']),
'CAND-D845FA532C41':('A','Fractional moments connect integer moments, large values and zero-density tools.','Extract fixed-moment parameter range, conditional assumptions and dependence of implicit constants.',['PAPER-A001']),
'CAND-3618E116DC48':('A,B','Derivative/discrete mean values are dependencies of zero simplicity and reciprocal-derivative questions.','Distinguish averaging over ordinates from continuous t integrals and state all RH assumptions.',['PAPER-E003','PAPER-A003']),
'CAND-3126BDDE0401':('A','Foundational mollified mean-square dependency; author identity requires correction against author bibliography.','Extract arbitrary versus Mobius-structured polynomial restrictions and exact admissible lengths.',['PAPER-A001','PAPER-A003']),
'CAND-E2FA625F993F':('B','Historical pair-correlation test-function refinement after Montgomery.','Audit exact admissible majorants/minorants and RH conditions before importing into unconditional complex-zero tests.',['PAPER-E009','PAPER-A003']),
'CAND-0F494051698A':('A,F','Important algorithmic antecedent to high-height zero statistics and rigorous computation.','Separate evaluation complexity from certified root completeness and numerical precision.',['PAPER-A002']),
'CAND-B1799D1EDE19':('A,B','Pair-correlation conjecture implications bridge zeros and primes beyond the proven bandwidth.','Read exact uniformity hypotheses and arithmetic equivalences rather than using an informal conjecture label.',['PAPER-E009','PAPER-A006']),
'CAND-DA1BBABD6A69':('A,B','Historical40percent critical-line milestone central to mollifier evolution.','Audit mollifier length, shifted derivative choices and exact count including simple versus all critical zeros.',['PAPER-A003']),
'CAND-4AC624D7B1FA':('A,D,E','Spectral fourth-moment formula is a plausible precise transfer source to analytic zero problems.','Read spectral/Kloosterman transform conditions, test regularity and residue terms before proposed transfers.',['PAPER-A001']),
'CAND-85537F6D3441':('C','Early real-variable arithmetic reformulation preceding the strong Nyman criterion.','Identify exact approximation family and norm hypotheses compared with2002strengthening.',['PAPER-E001','PAPER-E007']),
'CAND-81D237C6353B':('A','Fourth-moment refinement complements the explicit spectral formula; metadata identifies Ivic, not Iwaniec.','Compare exact remainder estimates to1979 and1993 sources without conflating similarly named authors.',['PAPER-A001']),
'CAND-243CB05082A0':('A,B','Historically influential sixth-moment conjecture; must remain labelled conjectural.','Read explicit conjectured coefficient and derivation; locate which prime/divisor correlations remain unproved.',['PAPER-E009']),
'CAND-C8B53E505055':('A','Relevant explicit zero-free work but current audit budget prioritizes foundational Ford and modern explicit benchmarks.','Defer substantive selection until comparison establishes whether it supplies a distinct reusable bound or method.',['PAPER-A001']),
'CAND-425FBEC9487C':('A','Key Vinogradov-method and explicit zeta-bound dependency for zero-free regions.','Read exact sigma/height uniformity and constants before treating later explicit regions as improvements.',['PAPER-A001']),
'CAND-0C2EE3F2C932':('C,E','General strong approximation criterion may delimit what transfers beyond the classical zeta case.','Extract axioms on the Dirichlet series and Lp/domain assumptions; compare actual generality withE001.',['PAPER-E001','PAPER-L001']),
'CAND-1F36EEA8B347':('A,B,E','Major moments recipe organizes arithmetic factors and random-matrix predictions.','Separate proved identities from conjectural moment asymptotics; record exact shifts, averaging regime and arithmetic factors.',['PAPER-E009']),
'CAND-10E751474D7F':('A,B,D','Explicit hybrid prime/zero factorization offers a concrete bridge rather than a vague matrix analogy.','Audit truncation/error conditions and whether estimates are pointwise, averaged or conditional on RH.',['PAPER-E009']),
'CAND-A38902B3C3C2':('A','Major conditional moment bounds form the precise predecessor to Harper and resonance/large-value comparisons.','Extract fixed-k and RH quantifiers and the epsilon loss; trace the Dirichlet-polynomial bound.',['PAPER-A001']),
'CAND-1D048E097D34':('A,B','Critical-line proportion milestone after Conrey; central mollifier dependency.','Read exact proportions, simple-zero count and mollifier coefficient constraints; no abstract-only theorem record.',['PAPER-A003']),
'CAND-073BC7B4A7D0':('A','Sharp conditional moment bounds refine the Soundararajan input and are repeatedly reused.','Read fixed-k dependence, polynomial decomposition and RH condition before making uniform-k inferences.',['PAPER-A001']),
'CAND-D0B2713003CD':('B,C,D','Hilbert-space extremal formulation of pair correlation directly supports positivity/certificate campaigns.','Read reproducing-kernel axioms, bandwidth dependence and which extremal bounds are proved under RH.',['PAPER-E009','PAPER-A003']),
'CAND-823D1C1A4F3A':('A,F','Explicit trigonometric positivity is a concrete optimization mechanism for zero-free regions.','Audit coefficient nonnegativity certificates and analytic constants, including independent reproducibility.',['PAPER-A001']),
'CAND-164017B84F00':('A,H','Decoupling supplies a substantive cross-field input to exponential sums and zeta growth.','Extract exact exponent and scale conditions and trace how decoupling enters; compare to large-value obstacles.',['PAPER-A001']),
'CAND-7135914D26F6':('A,B','Later mollifier critical-line benchmark is necessary context for2026simple-critical advances.','Read exact distinction between critical-line fraction and simple critical zeros, and the technical moment inputs.',['PAPER-A003','PAPER-A004']),
'CAND-ECE6A8EFEBD2':('B,C,F','Semidefinite optimization offers reproducible pair-correlation extremal certificates.','Distinguish numerical SDP output from proved feasible certificates and preserve RH/test-support conditions.',['PAPER-E009','PAPER-A003']),
'CAND-5EC595F2B6F6':('A,F','Recent explicit zero-free benchmark needed for the execution-date frontier.','Read all height ranges and verified constants, then compare like-for-like regions and computational inputs.',['PAPER-A001','PAPER-A002']),
'CAND-DD8D1906CE3D':('B,E','Higher-correlation automorphic work is central to the random-matrix transition and support restrictions.','Extract which L-functions, averaging regimes, hypotheses and Fourier supports are actually proved.',['PAPER-E009','PAPER-G002']),
'CAND-EE643A1A7A83':('A,E','Precise bridge between central nonvanishing and exceptional real zeros; highlighted by Conrey2003.','Read exact family and nonvanishing threshold; distinguish classical RH from the Landau-Siegel zero obstruction.',['PAPER-A001']),
'CAND-44DAA3512B72':('A,B,E','Ratios conjectures systematically predict derivative and correlation expressions.','Separate established random-matrix identities from L-function conjectures and preserve shifts/uniformity.',['PAPER-L001','PAPER-E009']),
'CAND-9674802E43F1':('C,E','Selberg-class extension of Li criterion is useful for testing exactly which axioms the criterion needs.','Compare published theorem with withdrawn2009manifestation; do not infer mathematical error from withdrawal alone.',['PAPER-E008','PAPER-L001']),
'CAND-80E83412AF97':('C,E,G','Publisher-registered withdrawn manifestation is version history, not another independent theorem paper.','Preserve withdrawal metadata and investigate relation to2010article; no reason for withdrawal established.',['PAPER-E008','PAPER-L001']),
'CAND-9F09FA0A54FA':('C,E','Later equivalent relations for the Selberg class can clarify the arithmetic axioms behind positivity.','Extract exact class restrictions and logical equivalences before comparing finite-prefix Li countermodels.',['PAPER-E008','PAPER-L001']),
'CAND-CURATED-MV1974':('A,H','Explicit mean-value dependency of original Montgomery1973Eq28, then cited as to appear.','Read Hilbert inequality hypotheses and justify infinite Dirichlet-series L2 passage with weighted coefficient sum.',['PAPER-E009']),
'CAND-CURATED-GM1987':('A,B','Exact later endpoint/error antecedent named by BGSTB; closes a specific historical dependency gap.','Read Lemma8 at original source and separate proved endpoint uniformity from pair-correlation conjectures.',['PAPER-E009','PAPER-A006']),
'CAND-CURATED-OTR1985':('A,B,F,G','Rigorous disproof of a stronger conjecture formerly promising an RH route; valuable negative knowledge.','Read analytic/computational proof and distinguish disproving |M(x)|<sqrt(x) from disproving RH.',['PAPER-E001','PAPER-E008']),
'CAND-CURATED-LEV1974':('A,B','Original one-third critical-line milestone explicitly discussed by Conrey2003.','Read original short proof, exact lower-bound wording and mollifier length; avoid replacing printed title with a common paraphrase.',['PAPER-S007','PAPER-A003'])}
# Existing records used only for identity linkage; no mutation of selected corpus.
existing=[]
for f in (root/'papers').glob('*records*.jsonl'):
 for l in f.read_text().splitlines():
  try:existing.append(json.loads(l))
  except:pass
for l in (root/'corpus/bibliography.jsonl').read_text().splitlines():
 try:existing.append(json.loads(l))
 except:pass
def nd(s):return (s or '').lower().replace('https://doi.org/','').strip()
def clean(s):return re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>','',s))).strip()
def ds(v):
 a=(v or {}).get('date-parts',[[]])[0];return '-'.join(str(x).zfill(2) if i else str(x) for i,x in enumerate(a)) or None
out=[]
for r in rs:
 cid=r['candidate_id'];doi=nd(r.get('doi'));mf=p/'crossref'/(hashlib.sha256(doi.encode()).hexdigest()[:16]+'.json');m=json.loads(mf.read_text())['message'] if mf.exists() else {}
 title=clean((m.get('title') or [r['title']])[0]);auth=[' '.join(filter(None,[a.get('given'),a.get('family')])) for a in m.get('author',[])] or r.get('authors',[])
 facts=[];extraev=[];arxiv=None;primary=m.get('resource',{}).get('primary',{}).get('URL','https://doi.org/'+doi)
 if cid=='CAND-3126BDDE0401':
  auth=['R. Balasubramanian','J. B. Conrey','D. R. Heath-Brown'];facts.append('OpenAlex and current publisher landing omit Balasubramanian; corrected from coauthor Heath-Brown CV entry52, not merely inferred from citations.');extraev.append({'url':'https://www.maths.ox.ac.uk/system/files/users/cv/rhbcv_3.pdf','locator':'Publications entry52, PDFp7','local':'sources/corpus_priority_round2/heath_brown_cv.pdf'})
 if cid=='CAND-E2FA625F993F':auth=['P. X. Gallagher'];extraev.append({'url':'https://www.degruyterbrill.com/document/doi/10.1515/crll.1985.362.72/html','locator':'Publisher citation lines145–161; toolresponse local'})
 if cid=='CAND-B1799D1EDE19':auth=['D. A. Goldston'];facts.append('Crossref supplies title/pages but no author list; author corroborated by discovered OpenAlex and primary reference lists; original byline not inspected.')
 if cid=='CAND-DA1BBABD6A69':auth=['J. B. Conrey'];extraev.append({'url':'https://www.degruyterbrill.com/document/doi/10.1515/crll.1989.399.1/html','locator':'Publisher citation lines145–161; print1989 versus archiveonline2009'})
 if cid=='CAND-85537F6D3441':auth=['Luis Báez-Duarte'];facts.append('Normalized author typography from Baezduarte to established author identity PAPER-E001; no mathematical theorem extracted here.')
 if cid=='CAND-243CB05082A0':
  title='A conjecture for the sixth power moment of the Riemann zeta-function';auth=['J. B. Conrey','A. Ghosh'];arxiv='math/9807187';facts.append('Crossref omits title and truncates pages to775; actual arXiv metadata and publisher search citation establish title and775–780.');extraev.append({'url':'https://arxiv.org/abs/math/9807187','locator':'citation_title/author/date and journal-ref; retrievedlanding','local':'sources/corpus_priority_round2/conreyghosh1998_arxiv.html'})
 if cid=='CAND-073BC7B4A7D0':
  arxiv='1305.4618v1';primary='https://arxiv.org/abs/1305.4618v1';auth=['Adam J. Harper'];facts.append('arXiv DOI is DataCite, not found at Crossref; actual arXiv landing verifies v1 dated2013-05-20. Journal publication not verified.');extraev.append({'url':primary,'locator':'citation metadata and submission history','local':'sources/corpus_priority_round2/harper1305.html'})
 if cid=='CAND-CURATED-OTR1985':
  auth=['A. M. Odlyzko','H. J. J. te Riele'];extraev.append({'url':'https://ir.cwi.nl/pub/1823','locator':'Repository citation_author/title/journal/pages metadata','local':'sources/corpus_priority_round2/mertens_repository.html'});facts.append('Repository record and journal metadata identify same1985work;1984CWIreport manifestation is not counted as separate work.')
 if cid=='CAND-CURATED-LEV1974':facts.append('Canonical publisher title is At Least One-Third, not the common paraphrase More than one-third. Printed title retained; no mathematical audit implied.')
 if cid in ['CAND-E39F04327F9A','CAND-454FB8542468']:facts.append('Same-title1935and1936papers have distinct DOIs/volumes/pages; not deduplicated solely on title.')
 if cid=='CAND-329B94C7E05F':facts.append('DOI identifies English translation in Math USSR Izvestiya9(1975)443–453; MathNet landing also identifies Russian original. Treat translations as manifestations of one work.')
 if cid=='CAND-D0B2713003CD':facts.append('Firstonline2014, printed2017volume725; year field uses print year2017, both dates preserved.')
 if cid=='CAND-164017B84F00':facts.append('Firstonline2016; authoritative AMSURL and JAMSvolume30issue1 are2017publication; year field uses2017.')
 if cid=='CAND-7135914D26F6':facts.append('Firstonline2019-12-06, print2020volume7article2; year field uses2020.')
 if cid=='CAND-ECE6A8EFEBD2':facts.append('Provider candidate year2019 differs from journal volume361February2020; year field uses2020.')
 if cid=='CAND-80E83412AF97':facts.append('Crossref title explicitly WITHDRAWN. No withdrawal reason independently obtained. Similar-title2010DOI may be replacement/related manifestation; relation requires source-history check, not assumed theorem error.')
 year=(m.get('published-print') or m.get('published') or {}).get('date-parts',[[r.get('year',2013)]])[0][0]
 if cid=='CAND-164017B84F00':year=2017
 if cid=='CAND-073BC7B4A7D0':year=2013
 fam,reason,obj,deps=reasons[cid]
 decision='priority_candidate_verified_metadata'
 if cid=='CAND-C8B53E505055':decision='defer'
 if cid=='CAND-80E83412AF97':decision='reject'
 evidence=[{'url':'https://api.crossref.org/works/'+doi,'locator':'publisher-deposited bibliographic metadata only; no mathematical text inspection','local':str(mf.relative_to(root))}] if mf.exists() else []
 evidence+=extraev
 matches=sorted(set(x.get('id',x.get('paper_id')) for x in existing if nd(x.get('doi'))==doi and doi and x.get('id',x.get('paper_id'))))
 if matches:
  decision='defer';facts.append('Existing selected/recorded work found by DOI at final snapshot; retain linkage, do not create another selected work.')
 row={'candidate_id':cid,'provider_id':r.get('openalex_id'),'provider_ids':{'openalex':r.get('openalex_id'),'doi':doi},'title':title,'canonical_title':title,'authors':auth,'doi':doi,'arxiv':arxiv,'year':year,'date':ds(m.get('published-print') or m.get('published')) if m else '2013-05-20','online_date':ds(m.get('published-online')),'print_date':ds(m.get('published-print')),'venue':(m.get('container-title') or ['arXiv preprint'])[0],'volume':m.get('volume'),'issue':m.get('issue'),'pages':'775–780' if cid=='CAND-243CB05082A0' else m.get('page'),'article_number':m.get('article-number'),'canonical_url':('https://arxiv.org/abs/'+arxiv) if cid=='CAND-073BC7B4A7D0' else 'https://doi.org/'+doi,'primary_url':primary,'urls':[primary,'https://doi.org/'+doi],'decision':decision,'reason':reason,'dependency_objective':obj,'dependency_paper_ids':deps,'linked_existing_paper_ids':matches,'evidence':evidence,'evidence_locator':'Crossref registered identity plus explicit supplemental primary bibliographic passages listed in evidence; no full mathematical reading','query_url':'https://api.crossref.org/works/'+doi if m else primary,'identity_confidence':'high_bibliographic_identity' if cid!='CAND-B1799D1EDE19' else 'high_title_doi_pages_author_corroborated_not_original_byline','version_and_dedup_notes':facts or ['Published manifestation verified by DOI metadata; exhaustive corrections/version history not investigated.'],'family':fam.split(','),'selected':False,'full_text_reviewed':False,'substantively_read':False,'audit_level':None,'verification_scope':'Bibliographic candidate triage only. Priority does not mean selected, accessed mathematical source, read, analyzed, or audited.','primary_url_access_check':access.get(cid),'discovery_provenance':r.get('discovery_provenance','Existing corpus/candidates.jsonl, '+cid+'; expert historical/dependency triage informed by originalMontgomery1973 and Conrey2003bibliography/narrative.'),'curated_at':'2026-11-17'}
 out.append(row)
assert len({r['candidate_id'] for r in out})==len(out)
out.sort(key=lambda r:(r['year'],r['canonical_title']))
f=root/'corpus/curated_candidate_decisions_round3.jsonl';f.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in out))
cols=['candidate_id','provider_id','canonical_title','authors','year','doi','arxiv','decision','reason','dependency_objective','canonical_url','primary_url','identity_confidence','linked_existing_paper_ids']
with (root/'corpus/curated_candidate_decisions_round3.csv').open('w',newline='') as a:
 w=csv.DictWriter(a,fieldnames=cols);w.writeheader()
 for r in out:w.writerow({k:json.dumps(r[k],ensure_ascii=False) if isinstance(r[k],list) else r[k] for k in cols})
print('rows',len(out),'decisions',dict(collections.Counter(r['decision'] for r in out)),'newcurated',sum(r['provider_id'] is None for r in out),'existinglinks',[(r['candidate_id'],r['linked_existing_paper_ids']) for r in out if r['linked_existing_paper_ids']])
